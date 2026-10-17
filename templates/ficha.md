---
titulo: "Nombre del tema tal como lo verá el lector"
slug: "nombre-del-tema"            # minúsculas, guiones, sin acentos
fecha: "AAAA-MM-DD"                # día de la sesión
tipo: "teoria"                     # teoria | bug
tema: "Concurrency"                # UNA palabra, como se verá en el pie de la portada
swift: "6.0"
ios_min: "17.0"
relacionado: []                    # slugs de fichas previas
---

## Portada

Máximo 3 frases. Qué es y por qué duele (el pain real, no la definición de la doc).
La primera frase es el gancho: debe entenderse sola.

## Ejemplo

Una frase de contexto. El código vive en `antes.swift` (lo que no funcionaba, o el
escenario de partida si es teoría) y el renderer lo incrusta aquí.

## Fix

Dos o tres frases: qué cambió y por qué ese cambio resuelve el pain.
El código vive en `despues.swift` y el renderer lo incrusta aquí.

## Feedback

- **Lección:** la idea que vale recordar en un año, en una frase.

Reflexión: dos párrafos cortos (4 a 6 frases en total). Por qué este caso importa más
allá del snippet: qué principio de diseño está detrás, cuándo lo vas a volver a ver, qué
cambió en cómo piensas el problema. Es la parte que diferencia tu post de la doc.

- **Ojo con:** una trampa o límite de la solución (una línea).
- **Doc:** [Título](https://developer.apple.com/…)
