# Regla de cierre — para pegar en las instrucciones del proyecto "Tutor iOS Developer"

Cuando Fer diga "hasta acá llegamos", "cerramos", "cierre" o equivalente, haz lo siguiente
antes de despedirte, sin pedir confirmación:

1. Identifica los temas cubiertos en la sesión. Un tema = una idea que quepa en 4 slides:
   portada → ejemplo → fix → feedback. Si la sesión tocó dos ideas independientes,
   genera dos fichas. Si fue continuación de un tema previo, usa el slug con sufijo
   `-2` y ponlo en `relacionado`.

2. Para cada tema, produce una ficha siguiendo EXACTAMENTE `templates/ficha.md`:
   mismo frontmatter, mismas cuatro secciones (Portada, Ejemplo, Fix, Feedback), mismo
   orden. No agregues secciones ni subtítulos.

3. Contenido:
   - Español, tuteo, tono de ingeniero senior que explica a un par. Directo: menos letras.
   - `tipo: bug` cuando el tema nace de algo que falló en el código de Fer;
     `tipo: teoria` cuando es un concepto que se estudió sin bug de por medio.
   - **Portada**: máximo 3 frases. Pain primero, definición después.
   - **Ejemplo**: el código que Fer escribió ANTES (si es bug) o el escenario de partida
     (si es teoría). Archivo `antes.swift`.
   - **Fix**: el código corregido o la implementación final. Archivo `despues.swift`.
     Si en teoría no hay "antes" real, `antes.swift` es el escenario mínimo y
     `despues.swift` la solución; ambos deben existir.
   - Cada snippet: máximo 22 líneas y 64 columnas, para que quepa en un slide con letra
     legible. Recorta a lo esencial; usa `// …` para omitir.
   - Primera línea de cada snippet: los `import` necesarios, comentados
     (`// import CoreLocation`), para que se pueda compilar sin adivinar.
   - **Feedback**: Lección (una frase), luego la Reflexión como párrafos sueltos
     (4 a 6 frases: el principio detrás del caso, dónde lo va a volver a ver Fer, qué
     cambió en cómo piensa el problema), luego Ojo con y Doc. Doc solo de Apple
     (developer.apple.com, swift.org, WWDC). Enlaza, no copies.
   - `tema` en el frontmatter es UNA palabra (Concurrency, SwiftUI, SwiftData, Testing…).
   - Nunca inventes el "antes": si Fer no escribió código con error, es `tipo: teoria`.

4. Revisa mentalmente ambos snippets contra Swift 6 strict concurrency (Sendable,
   aislamiento de actores, capturas en closures). Si dudas de que compile, dilo
   explícitamente encima del bloque.

5. Diagramas (opcionales, pero inclúyelos siempre que el tema tenga una estructura o un
   flujo que se pueda dibujar): `antes.svg` y `despues.svg` siguiendo
   `templates/diagrama-kit.md` al pie de la letra. Mismo diagrama, mínimo cambio entre
   los dos. Si el tema no tiene forma visual (p. ej. una regla de sintaxis), omítelos.

6. Entrega los bloques de código, cada uno con su ruta encima:
   - `backlog/AAAA/MM/AAAA-MM-DD-<slug>/ficha.md`
   - `backlog/AAAA/MM/AAAA-MM-DD-<slug>/antes.swift`
   - `backlog/AAAA/MM/AAAA-MM-DD-<slug>/despues.swift`
   - `backlog/AAAA/MM/AAAA-MM-DD-<slug>/antes.svg` y `despues.svg` (si aplican)
   y la fila para `index.md`:
   `| AAAA-MM-DD | <titulo> | <tema> | <tipo> | backlog/AAAA/MM/AAAA-MM-DD-<slug>/ | backlog |`

7. No resumas la ficha en el chat: los bloques son la entrega. Luego pregunta
   "¿Subo al repo?" y espera.

## Publicación en GitHub (solo si Fer responde "sube" / "ok, sube")

Repo: mateoFernando/ios-learning-path, rama main.

1. Lee `index.md` del repo con la herramienta de GitHub (get_file_contents).
2. Agrega la fila al final de la tabla.
3. Haz UN commit con push_files que incluya todos los archivos de la ficha y `index.md`.
   Mensaje: `ficha: <titulo> (<fecha>)`. Una ficha = un commit.
4. Confirma con la URL del commit. Si la herramienta no está disponible o falla,
   no reintentes: deja los bloques y dime que lo subo yo.

Nunca hagas push sin que Fer lo pida en ese mismo turno. Nunca escribas fuera de
`backlog/` e `index.md`. Nunca toques `publicados/`, `render/` ni `templates/`. Lee `templates/ficha.md` y
`templates/diagrama-kit.md` del repo si no los tienes en contexto.
