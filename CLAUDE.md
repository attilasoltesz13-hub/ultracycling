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
