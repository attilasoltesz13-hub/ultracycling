# Mintaoldalak (pilot, 0. lépés)

Három oldaltípus — fogalom, adat, protokoll — a 04 (Alvás) modulból, két PDF-motorral és két betűtípus-jelölttel. A tartalom illusztratív: a formátumot mutatja, a számok a kutatási fázisban cserélődnek.

| Fájl | Motor | Forrás |
| --- | --- | --- |
| `dist/samples/samples-chromium-{plex,inter}.pdf` | HTML + CSS → Chromium print (Playwright) | `samples.html` + `design/tokens/tokens.css` |
| `dist/samples/samples-typst-{plex,inter}.pdf` | Typst | `samples.typ` |

Ábrák: `figures/svg/*.svg` (a `{{FONT}}` helyőrzőt a build cseréli a választott családra; a HTML-ben inline SVG).

```
python3 build/samples/render_chromium.py all   # pip install playwright && playwright install chromium
build/samples/render_typst.sh all             # typst a PATH-on
```
