# Projekt-konvenciók (Claude Code)

- Nyelv: a tartalom magyar (`content/hu`), később angol (`content/en`); a kód és a commit-üzenetek angolul.
- Single source: minden tartalom Markdown a `content/` alatt; a PDF és a weboldal ebből épül. Soha ne szerkeszd a `dist/`-et kézzel.
- Minden számszerű állítás mellé `sources.yaml`-beli kulcs kell (`[@kulcs]`) és bizonyíték-fokozat (A–D).
- Sablonokban minden elem jelölve: `fix` / `példa` / `egyéni`. Direktívák: `:::evidence A`, `:::individual`, `:::protocol`, `:::task`, `:::summary`.
- Modul-fejléc (YAML): `id, title, title_en, level, disciplines, version, status, sources, estimated_pages`.
- Ábrák: forrás a `figures/src/` (Python/Vega), kimenet `figures/svg/`; színek csak a `design/tokens/` értékeiből.
- Betűtípus: csak OFL-licencű (IBM Plex / Inter), vendorozva a `design/fonts/` alatt.
- Nyelvi szabály (2026-09-18): a KÉSZ anyagban (`content/`) nem kerékpáros szakszó — élettani, alvástudományi, statisztikai — csak egyértelmű magyar magyarázattal az első előfordulásnál, a köznyelvi alak maradjon a szövegben (érzett erőkifejtés, figyelmi reakcióidő-teszt, belső napi óra, csuklón viselt mozgásérzékelő). A kutatási anyagok (`docs/`, `data/`) maradnak szakmaiak.
- Tartalmi jelölések: `:::page type=… level=… disc=…`, `:::you`, `:::protocol`, `:::figure src=… caption=… ev=…`; inline `{ev:A}`–`{ev:D}`, `{fix}` / `{példa}` / `{egyéni}`, `[@kulcs]`. Részletek: `design/styleguide.md` 7. pont.
- `references/` = szerzői jogvédett teljes szövegek helyi másolata, gitignore-olva; a `sources.yaml` `fulltext` mezője hivatkozik rá.
- Build: `python3 build/render.py content/hu/NN-….md --draft` → `dist/NN-….pdf` (túlcsordulás-jelentéssel); `python3 build/site.py` → `dist/site/` (statikus kísérőoldal, `web/` forrásból, ugyanazzal az értelmezővel). Munkafolyamat modulonként: kutatás → írás → ábrák + PDF → tényellenőrzés külön ügynökkel (forráskulcs szinten) → web → következő modul.
- Kísérőoldal-adatok: kvíz `data/quiz/NN-….yaml` (a helyes válasz a fájlban az első; a build keveri), kalkulátor-paraméterek `data/tools/*.yaml` fix/példa/egyéni megjegyzéssel. Böngészőben minden `localStorage`, szerver nincs.
