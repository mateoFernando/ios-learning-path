# Diseño del carrusel — decisiones y registro

Leer antes de modificar `render/`. Cada decisión tiene su razón; si se cambia, actualizar aquí.

## Formato

- **4 slides, fijos:** Portada → Ejemplo → Propuesta → Reflexión. Funciona igual para un
  bug (antes/después) y para teoría (escenario/solución). No se agregan slides; si el
  contenido no cabe, se recorta el contenido.
- **1080×1350** (vertical, el formato que mejor rinde en LinkedIn móvil). Salida: PDF de
  4 páginas para subir como documento, PNG por slide, y un PDF A4 aparte como ficha de
  estudio.
- **Menos letras.** Portada máx. 3 frases; notas de ejemplo/fix 2–3 frases; reflexión
  4–6 frases. Snippets ≤22 líneas × 64 columnas.

## Visual

- **Dark mode tipo Apple:** fondo `#000`, tarjetas `#1C1C1E`, texto `#F5F5F7`,
  secundario `#98989D`. Un solo acento azul sistema `#0A84FF` para navegación.
- **Rojo `#FF453A` y verde `#30D158` solo con significado:** borde izquierdo del código
  "antes"/"después" y nodos/flechas del diagrama. Nunca como decoración.
- **Tipografía:** Inter Display para titulares (tracking apretado), Inter para texto,
  SF Mono / Menlo para código (en Linux cae a DejaVu Sans Mono; el resultado final se
  juzga en Mac).
- **Todo alineado a la izquierda.** Sin etiquetas en mayúsculas, sin "1 / 4", sin
  separadores con puntos medios.
- **El código es el protagonista** en los slides 2 y 3: título corto arriba, nota de
  2–3 líneas, bloque de código grande. El tamaño de fuente del código se calcula para
  que las líneas quepan (`render.py`, `px`).

## Cada slide

| Slide | Contiene | No contiene |
|---|---|---|
| Portada | título, 3 frases de pain, `Swift X · iOS Y+`, diagrama "antes" (si existe) | tags, nivel, avatar, nombre del autor |
| Ejemplo | h2 ("Lo que escribí" / "El escenario"), nota, `antes.swift` con borde rojo | título repetido |
| Propuesta | h2 ("Lo que funciona" / "La solución"), nota, `despues.swift` con borde verde | título repetido |
| Reflexión | lección como cita grande, diagrama "después" (si existe), 2 párrafos de reflexión, "Ojo con" | CTA, link al repo, link a la doc (va solo en el PDF A4) |

## Pie de página (igual en los 4)

- Izquierda: **logo + website** (`render/assets/logo.svg` + `website` en `config.yaml`).
  Se descartó "Fer · linkedin.com/in/…" por largo.
- Centro: cuatro puntos de progreso.
- Derecha: **una palabra** en azul: el `tema` del frontmatter en la portada
  (Concurrency, SwiftUI…), luego Ejemplo, Propuesta, Reflexión.

## Diagramas

- Opcionales: `antes.svg` (portada) y `despues.svg` (cierre). Deben ser el **mismo**
  diagrama con el mínimo cambio, para que la diferencia se lea sin leer.
- El estilo vive en `style.css` vía un kit de clases (`templates/diagrama-kit.md`); el SVG
  no lleva colores ni fuentes. Así el tutor puede generarlos y salen consistentes.
- Etiquetas de flechas debajo del diagrama, nunca encima de las flechas.

## Contenido (lo que define `templates/ficha.md`)

- Frontmatter: `titulo, slug, fecha, tipo (bug|teoria), tema (una palabra), swift,
  ios_min, relacionado`. Se quitaron `tags` y `nivel`: no aportaban en el slide.
- Secciones fijas: Portada, Ejemplo, Fix, Feedback. El Feedback lleva Lección (bullet),
  Reflexión (párrafos sueltos), Ojo con (bullet), Doc (bullet).
- La reflexión es lo que diferencia el post de la documentación: principio detrás del
  caso, dónde se vuelve a ver, qué cambió en cómo se piensa el problema.

## Registro de cambios

- **2026-10-16** — Primera versión: 7 slides, modo claro, mucho texto. Descartada.
- **2026-10-17** — Rehecho a 4 slides en dark mode. Portada → Ejemplo → Fix → Feedback.
- **2026-10-17** — Portada: fuera tags, nivel y avatar. Pie derecho: una palabra por
  slide. Cierre: fuera CTA y repo, entra la reflexión larga.
- **2026-10-17** — Diagramas antes/después con kit de clases.
- **2026-10-17** — Fuera el título repetido en slides 2–4 y el link a la doc en el
  cierre. Pie izquierdo: logo + website en lugar de nombre + LinkedIn.

## Pendientes / ideas

- Validar en celular el tamaño del código (slides 2 y 3) con SF Mono.
- Buscar referencias de carruseles que gusten para calibrar tipografía y aire.
- Logo definitivo (hoy es un monograma placeholder).
