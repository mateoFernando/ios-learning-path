# iOS Learning Path

Camino de aprendizaje de Swift / SwiftUI documentado sesión a sesión. Cada tema es una
**ficha** de cuatro partes (portada → ejemplo → fix → feedback) que se renderiza a un
carrusel de 4 slides para LinkedIn y a un PDF de estudio, con una plantilla fija.

```
ios-learning-path/
├── REGLA-DE-CIERRE.md     ← instrucciones para el proyecto "Tutor iOS Developer"
├── DISEÑO.md              ← decisiones de diseño del carrusel y registro de cambios
├── index.md               ← el camino, en orden cronológico
├── templates/ficha.md     ← plantilla de CONTENIDO (lo que escribe el tutor)
├── templates/diagrama-kit.md ← cómo escribir los SVG antes/después
├── backlog/AAAA/MM/AAAA-MM-DD-<slug>/   ← fichas listas, aún no publicadas
│   ├── ficha.md
│   ├── antes.swift        (≤22 líneas, ≤64 columnas)
│   ├── despues.swift      (≤22 líneas, ≤64 columnas)
│   ├── antes.svg          (opcional)
│   └── despues.svg        (opcional)
├── publicados/            ← misma estructura; lo ya publicado, con fecha y link
└── render/                ← plantilla VISUAL y script: ficha → carrusel + PDF
```

## Flujo

1. **Sesión de estudio** en el proyecto Tutor. Al decir "hasta acá llegamos", el tutor
   genera la ficha siguiendo `REGLA-DE-CIERRE.md` y, con el ok, la sube a `backlog/`.
2. **Render y publicación** (Grok Bot, en rutina): toma la ficha más antigua de
   `backlog/`, corre `render/`, pide aprobación, publica en LinkedIn y mueve la carpeta
   a `publicados/`.
3. **Métricas** (Grok Bot, semanal): resumen de los posts y aviso si `backlog/` baja
   de 4 fichas.
