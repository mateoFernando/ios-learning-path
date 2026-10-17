# render

Convierte una ficha (`ficha.md` + `antes.swift` + `despues.swift`) en:

- `<slug>-carrusel.pdf` — 4 páginas 1080×1350, para subir a LinkedIn como documento
- `slide-01..04.png` — los mismos slides como imagen
- `<slug>.pdf` — ficha de estudio en A4

```bash
pip install -r render/requirements.txt
python3 -m playwright install chromium
python3 render/render.py render/fixtures/taskgroup --out out
```

- `style.css` → identidad visual (tokens en `:root`)
- `template.html` → estructura de los 4 slides y del PDF
- `config.yaml` → website del pie
- `assets/logo.svg` → logo del pie (reemplázalo por el tuyo, viewBox 48×48)
- `fixtures/` → ficha de prueba para iterar el diseño sin tocar `backlog/`

Avisa si un snippet pasa de 22 líneas o 64 columnas, o si un slide se desborda.
