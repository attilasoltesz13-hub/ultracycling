# Mintaoldalak (pilot, 0. lépés)

Három oldaltípus — fogalom, adat, protokoll — a 04 (Alvás) modulból. A tartalom illusztratív: a formátumot mutatja, a számok a kutatási fázisban cserélődnek.

Döntések (2026-09-18): PDF-motor **Chromium print** (HTML + CSS, Playwright), betűtípus **Inter** + IBM Plex Mono; a bizonyíték-fokozatot **sáv-ikon** jelöli betű helyett. A Typst-változat és az IBM Plex Sans a git-előzményben (commit 3264bee) megvan, ha kellene.

```
pip install playwright && playwright install chromium
python3 build/samples/render_chromium.py     # → dist/samples/samples.pdf
```

Ábrák: `figures/svg/*.svg` (a HTML-ben inline másolat; a valódi build onnan illeszti be őket).
