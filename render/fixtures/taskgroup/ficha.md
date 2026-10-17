---
titulo: "TaskGroup: el array compartido que Swift 6 no te deja tocar"
slug: "taskgroup"
fecha: "2026-10-16"
tipo: "bug"
tema: "Concurrency"
swift: "6.0"
ios_min: "17.0"
relacionado: []
---

## Portada

Lanzas N tareas en paralelo, cada una guarda su resultado en un array, y Swift 6 no compila.
No es un capricho del compilador: dos tareas escribiendo el mismo array es un data race.
`TaskGroup` ya tiene el canal para recoger resultados; solo hay que usarlo.

## Ejemplo

Calcular el tiempo a pie a cada restaurante en paralelo. Cada tarea hija intenta
escribir en `ranked` desde dentro del `addTask`.

## Fix

Cada hija *devuelve* su valor y solo el padre toca el array, leyendo del grupo con
`for try await`. El orden de llegada es arbitrario, así que se ordena al final.

## Feedback

- **Lección:** En un `TaskGroup` las hijas devuelven, el padre recoge. Nada compartido se muta desde dentro.

El error del compilador no es un obstáculo: es el diseño de la concurrencia estructurada
hablando. Si una tarea hija necesita escribir en algo de afuera, el problema no es el
`Sendable`, es que el dato no tiene dueño claro.

Este mismo patrón vuelve en cualquier sitio donde haya paralelismo con resultado:
descargas de imágenes, validaciones por campo, llamadas a varios endpoints. La pregunta
que me quedó no es "cómo lo mutó", sino "quién debería ser el dueño del resultado".

- **Ojo con:** El orden de llegada no es el orden de `addTask`. Si importa, ordena o indexa por id.
- **Doc:** [TaskGroup](https://developer.apple.com/documentation/swift/taskgroup)
