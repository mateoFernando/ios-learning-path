# Kit de diagramas (opcional por ficha)

Dos archivos SVG opcionales en la carpeta de la ficha, uno por estado:

- `antes.svg` → se muestra en la portada (el problema)
- `despues.svg` → se muestra en el cierre (la solución)

Deben ser el **mismo** diagrama con lo mínimo cambiado, para que la diferencia se lea
de un vistazo. Si uno de los dos no aporta, no lo incluyas; el renderer los omite.

## Reglas

- `viewBox="0 0 920 330"` y `class="diagram"`. Nada de `width`/`height` ni estilos inline:
  todo el color y la tipografía vienen del CSS por clase.
- Máximo 6 nodos. Texto corto: un nombre por nodo y, si hace falta, una línea en mono.
- Las etiquetas de flechas van debajo del diagrama (y≈318), no encima de las flechas.
- Marcador de flecha: define uno en `<defs>` con `class="d-arrow"` y un `id` único por archivo.

## Clases disponibles

| Clase | Uso |
|---|---|
| `d-node` | caja neutra (`rect` con `rx="16"` o `"18"`) |
| `d-node d-bad` / `d-node d-good` | caja resaltada en rojo / verde |
| `d-edge` | flecha neutra (`path`, `fill="none"`) |
| `d-edge d-bad` / `d-edge d-good` | flecha roja / verde |
| `d-title` | nombre del nodo (sans, 24px) |
| `d-sub` | detalle en mono (18px), debajo del nombre |
| `d-label` (+ `d-bad`/`d-good`) | etiqueta de una flecha o grupo |

## Esqueleto

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 330" class="diagram">
  <defs><marker id="m1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6"
    orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="d-arrow"/></marker></defs>

  <rect x="20" y="110" width="170" height="80" rx="18" class="d-node"/>
  <text x="105" y="143" class="d-title" text-anchor="middle">origen</text>
  <text x="105" y="170" class="d-sub" text-anchor="middle">detalle</text>

  <rect x="730" y="110" width="170" height="80" rx="18" class="d-node d-good"/>
  <text x="815" y="155" class="d-title" text-anchor="middle">destino</text>

  <path d="M190 150 L 730 150" class="d-edge d-good" marker-end="url(#m1)"/>
  <text x="460" y="318" class="d-label d-good" text-anchor="middle">qué pasa aquí</text>
</svg>
```

Ejemplo completo: `render/fixtures/taskgroup/antes.svg` y `despues.svg`.
