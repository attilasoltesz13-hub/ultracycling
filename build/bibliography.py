#!/usr/bin/env python3
"""Közös irodalomjegyzék a könyv végére: minden modul hivatkozásai, modulonként, a modulon belüli számozással.

Használat:  python3 build/bibliography.py [--draft]   → dist/irodalomjegyzek.pdf
A modulok a content/hu/NN-*.md fájlok sorszám szerint; a számozás megegyezik a modulszövegben lévő felső indexekkel.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import render
from render import Module, ROOT, fit_pages


def main():
    mods = sorted(p for p in (ROOT / "content/hu").glob("[0-9][0-9]-*.md") if p.stem != "00-hasznalati-utmutato")
    pages = []
    for p in mods:
        m = Module(p)
        body_pages = [(b[1], b[2]) for b in m.parse_blocks(m.body) if b[0] == "page"]
        for _, body in body_pages:
            m.inline(body)
        keys = m.cite_order
        if not keys:
            continue
        chunks, start = [], 1
        first, rest = keys[:m.REFS_FIRST], keys[m.REFS_FIRST:]
        chunks.append((first, 1)); start = len(first) + 1
        while rest:
            c, rest = rest[:m.REFS_PAGE], rest[m.REFS_PAGE:]
            chunks.append((c, start)); start += len(c)
        for i, (chunk, st) in enumerate(chunks):
            title = f"Irodalomjegyzék · {m.meta['id']}. modul — {m.meta['title']}" + (" (folytatás)" if i else "")
            pages.append((m, f"## {title}\n\n:::refchunk {st}\n:::\n", (chunk, st)))
    total = len(pages)
    htmls = [m.page_html("type=forrasok level=alap disc=all", body, i + 1, total, refchunk=rc) for i, (m, body, rc) in enumerate(pages)]
    head = ('<!DOCTYPE html><html lang="hu"><head><meta charset="utf-8"><title>Irodalomjegyzék</title>'
            '<link rel="stylesheet" href="../design/tokens/tokens.css"><link rel="stylesheet" href="../design/print.css"></head><body>')
    out = ROOT / "dist/irodalomjegyzek.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(head + "\n".join(htmls) + "</body></html>")
    pdf = ROOT / "dist/irodalomjegyzek.pdf"
    for line in fit_pages(out, pdf):
        print(line)
    print("wrote", pdf.relative_to(ROOT), f"({total} oldal, {len(mods)} modul)")


if __name__ == "__main__":
    main()
