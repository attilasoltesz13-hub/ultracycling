# Projekt-konvenciók (Claude Code)

- Nyelv: a tartalom magyar (`content/hu`), később angol (`content/en`); a kód és a commit-üzenetek angolul.
- Single source: minden tartalom Markdown a `content/` alatt; a PDF és a weboldal ebből épül. Soha ne szerkeszd a `dist/`-et kézzel.
- Minden számszerű állítás mellé `sources.yaml`-beli kulcs kell (`[@kulcs]`) és bizonyíték-fokozat (A–D).
- Sablonokban minden elem jelölve: `fix` / `példa` / `egyéni`. Direktívák: `:::evidence A`, `:::individual`, `:::protocol`, `:::task`, `:::summary`.
- Modul-fejléc (YAML): `id, title, title_en, level, disciplines, version, status, sources, estimated_pages`.
- Ábrák: forrás a `figures/src/` (Python/Vega), kimenet `figures/svg/`; színek csak a `design/tokens/` értékeiből.
- Betűtípus: csak OFL-licencű (IBM Plex / Inter), vendorozva a `design/fonts/` alatt.
