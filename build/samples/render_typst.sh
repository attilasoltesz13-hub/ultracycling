#!/usr/bin/env bash
# Mintaoldalak renderelése Typst motorral (typst >= 0.13 kell a PATH-on).
# Használat: build/samples/render_typst.sh [plex|inter|all]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"; mkdir -p dist/samples
fonts=${1:-all}; [ "$fonts" = all ] && fonts="plex inter"
for f in $fonts; do
  fam="IBM Plex Sans"; [ "$f" = inter ] && fam="Inter"
  # az SVG-ábrák betűtípus-helyőrzőjét a választott családra cseréljük egy ideiglenes másolatban
  tmp="$(mktemp -d)"; mkdir -p "$tmp/figures/svg"
  for s in figures/svg/*.svg; do sed "s/{{FONT}}/$fam/g" "$s" > "$tmp/figures/svg/$(basename "$s")"; done
  cp -r design build "$tmp/"
  typst compile --root "$tmp" --font-path design/fonts --input font="$f" "$tmp/build/samples/samples.typ" "dist/samples/samples-typst-$f.pdf"
  rm -rf "$tmp"; echo "wrote dist/samples/samples-typst-$f.pdf"
done
