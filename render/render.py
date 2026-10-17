#!/usr/bin/env python3
"""
Renderiza una ficha (portada → ejemplo → fix → feedback) a:
  - carrusel para LinkedIn: PDF 1080×1350 de 4 páginas + slide-01..04.png
  - ficha de estudio: PDF A4

Uso:
    python3 render/render.py backlog/2026/10/2026-10-16-taskgroup [--out out] [--no-png]

Entrada: carpeta con ficha.md, antes.swift y despues.swift.
"""
import argparse
import re
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import SwiftLexer

HERE = Path(__file__).resolve().parent
SECTIONS = {"portada": "portada", "ejemplo": "ejemplo", "fix": "fix", "feedback": "feedback"}
MAX_LINES, MAX_COLS = 22, 64


def parse_ficha(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"{path}: falta el frontmatter YAML")
    front, body = yaml.safe_load(m.group(1)), m.group(2)

    raw, cur = {}, None
    for line in body.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            cur = SECTIONS.get(h.group(1).strip().lower())
            if cur is None:
                sys.exit(f"{path}: sección no permitida: '{h.group(1)}'")
            raw[cur] = []
        elif cur:
            raw[cur].append(line)
    missing = [k for k in SECTIONS.values() if k not in raw]
    if missing:
        sys.exit(f"{path}: faltan secciones: {missing}")

    md = markdown.Markdown(extensions=["extra"])
    s = {k: md.reset().convert("\n".join(v).strip()) for k, v in raw.items()}

    # Feedback: tres bullets fijos → leccion / ojo / doc
    items = [re.sub(r"\s+", " ", x).strip() for x in re.findall(r"<li>(.*?)</li>", s["feedback"], re.S)]
    fb = {}
    for it in items:
        mm = re.match(r"<strong>(Lección|Ojo con|Doc):</strong>\s*(.*)$", it, re.S)
        if not mm:
            sys.exit(f"{path}: línea de Feedback no reconocida: {it[:60]}")
        fb[{"Lección": "leccion", "Ojo con": "ojo", "Doc": "doc"}[mm.group(1)]] = mm.group(2)
    # Reflexión: los párrafos del Feedback que no son bullets
    fb["reflexion"] = "".join(re.findall(r"<p>.*?</p>", s["feedback"], re.S))
    for k in ("leccion", "ojo", "doc"):
        fb.setdefault(k, "")
    return front, s, fb


def render_code(path: Path, name: str):
    if not path.exists():
        sys.exit(f"falta {name}")
    src = path.read_text(encoding="utf-8").rstrip("\n")
    lines = src.split("\n")
    if len(lines) > MAX_LINES:
        print(f"AVISO: {name} tiene {len(lines)} líneas (máx {MAX_LINES}); se verá chico.")
    long_ = [i + 1 for i, l in enumerate(lines) if len(l) > MAX_COLS]
    if long_:
        print(f"AVISO: {name} supera {MAX_COLS} columnas en líneas {long_}; se cortará.")
    html = highlight(src, SwiftLexer(), HtmlFormatter(cssclass="highlight"))
    # px para que ~22 líneas quepan en ~860px de alto útil del slide
    px = max(16, min(22, int(860 / (max(len(lines), 1) * 1.45))))
    return html, px


def load_svg(path: Path):
    if not path.exists():
        return None
    return re.sub(r"<\?xml.*?\?>\s*", "", path.read_text(encoding="utf-8")).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ficha_dir")
    ap.add_argument("--out", default="out")
    ap.add_argument("--no-png", action="store_true")
    a = ap.parse_args()

    src = Path(a.ficha_dir).resolve()
    front, s, fb = parse_ficha(src / "ficha.md")
    antes, px_a = render_code(src / "antes.swift", "antes.swift")
    despues, px_d = render_code(src / "despues.swift", "despues.swift")
    cfg = yaml.safe_load((HERE / "config.yaml").read_text(encoding="utf-8"))
    css = (HERE / "style.css").read_text(encoding="utf-8")

    labels = (
        {"ejemplo": "Lo que escribí", "fix": "Lo que funciona", "feedback": "Lección"}
        if front.get("tipo") == "bug"
        else {"ejemplo": "El escenario", "fix": "La solución", "feedback": "Lección"}
    )
    tema = front.get("tema") or (front.get("tags") or ["iOS"])[0].replace("-", " ").title()
    diag = {"antes": load_svg(src / "antes.svg"), "despues": load_svg(src / "despues.svg")}
    logo = load_svg(HERE / "assets" / "logo.svg") or ""
    ctx = dict(f=front, s=s, fb=fb, cfg=cfg, css=css, labels=labels, tema=tema, diag=diag, logo=logo,
               code={"antes": antes, "despues": despues}, px={"antes": px_a, "despues": px_d})

    env = Environment(loader=FileSystemLoader(str(HERE)), autoescape=False)
    tpl = env.get_template("template.html")
    out = Path(a.out).resolve() / front["slug"]
    out.mkdir(parents=True, exist_ok=True)
    html_car = tpl.render(mode="carousel", **ctx)
    html_pdf = tpl.render(mode="pdf", **ctx)
    (out / "_carrusel.html").write_text(html_car, encoding="utf-8")
    (out / "_ficha.html").write_text(html_pdf, encoding="utf-8")

    with sync_playwright() as p:
        b = p.chromium.launch()

        page = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        page.set_content(html_car, wait_until="load")
        page.emulate_media(media="print")
        page.pdf(path=str(out / f"{front['slug']}-carrusel.pdf"), width="1080px", height="1350px",
                 print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        if not a.no_png:
            page.emulate_media(media="screen")
            slides = page.locator(".slide")
            for i in range(slides.count()):
                slides.nth(i).screenshot(path=str(out / f"slide-{i + 1:02d}.png"))
            over = page.evaluate("""() => [...document.querySelectorAll('.slide')]
                .map((s,i) => s.scrollHeight > s.clientHeight + 1 ? i+1 : null).filter(Boolean)""")
            if over:
                print(f"AVISO: desborde en slides {over}; recorta texto o código.")

        page = b.new_page()
        page.set_content(html_pdf, wait_until="load")
        page.emulate_media(media="print")
        page.pdf(path=str(out / f"{front['slug']}.pdf"), format="A4", print_background=True,
                 margin={"top": "14mm", "bottom": "14mm", "left": "14mm", "right": "14mm"})
        b.close()

    print(f"OK → {out}")


if __name__ == "__main__":
    main()
