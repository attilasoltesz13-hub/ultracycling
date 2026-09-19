# Hosszú távon — Az ultrakerékpározás tudománya és gyakorlata

*The Long Way — The Science and Practice of Ultracycling*

Önállóan feldolgozható ultrakerékpáros oktatóanyag: egy forrásból készül egy
adatvizualizációs stílusú, álló A4-es PDF-tankönyv és egy statikus, interaktív
kísérőoldal. Előbb teljes magyar kiadás, utána angol.

## Felépítés

| Útvonal | Tartalom |
| --- | --- |
| `content/hu/NN-modul.md` | Modulszöveg (magyar), strukturált fejléccel |
| `content/en/NN-modul.md` | Angol változat, azonos szerkezet és blokk-azonosítók |
| `data/sources.yaml` | Hivatkozások DOI-val, bizonyíték-fokozattal, modul-hozzárendeléssel |
| `data/templates/` | Edzés-, alvás-, táplálkozási sablonok géppel olvasható formában |
| `design/` | Stílusguide, design tokenek, oldaltípus-sablonok, betűtípusok, ikonok |
| `figures/src` → `figures/svg` | Diagramok forráskódja és renderelt SVG |
| `assets/photos/` | Saját és szabad felhasználású fotók (forrás a `CREDITS.md`-ben) |
| `web/` | Kísérőoldal forrása: stíluslap, JS-eszközök, sablonok (lásd `web/README.md`) |
| `data/quiz/`, `data/tools/` | Kvízkérdések és a kalkulátorok paraméterei modulonként |
| `build/` | `render.py` (PDF, Chromium print) és `site.py` (statikus kísérőoldal), egy közös értelmezővel |
| `dist/` | Generált PDF és weboldal (nem verziókezelt) |
| `docs/` | Projektdokumentumok, döntésnapló |

## Jelrendszer

- **Bizonyíték-fokozat** (négysávos ikon): összesített kutatás (A) · terepvizsgálat (B) · szakmai tapasztalat (C) · feltörekvő (D)
- **Sablonelemek**: `fix` (általánosan érvényes) · `példa` (szemléltető érték) · `egyéni` (csak saját teszttel beállítható)
- **Szint**: Alap · Haladó · Elit — **Szakág**: önellátó · kísérős · brevet · 24h

## Modulok

Használati útmutató (0) · I. Elmélet és élettan (1–8) · II. Gyakorlat (9–14) · III. Sablonok, eszközök, feladatok (15–19) · Függelékek.
Kész modulok (vázlat, tényellenőrzött): **04 – Alvás, fáradtság, kognitív teljesítmény**, **08 – Pacing és versenystratégia**. Kísérőoldal: https://attilasoltesz13-hub.github.io/ultracycling/

## Build

    python3 build/render.py content/hu/08-pacing.md --draft  # dist/08-pacing.pdf (--refs: forrásjegyzékkel)
    python3 build/bibliography.py                              # dist/irodalomjegyzek.pdf (minden modul)
    python3 build/site.py                                      # dist/site/ (open dist/site/index.html)

## Licenc

Szöveg és ábrák: minden jog fenntartva (a kiadás előtt eldöntendő). Betűtípusok: SIL Open Font License, lásd `design/fonts/`.
