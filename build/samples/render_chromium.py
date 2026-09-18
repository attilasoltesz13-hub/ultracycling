#!/usr/bin/env python3
"""Mintaoldalak renderelése PDF-be Chromium print motorral (Playwright).

Használat:  python3 build/samples/render_chromium.py [plex|inter|all]
Kimenet:    dist/samples/samples-chromium-<font>.pdf
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "build" / "samples" / "samples.html"
OUT = ROOT / "dist" / "samples"
OUT.mkdir(parents=True, exist_ok=True)

fonts = sys.argv[1:] or ["all"]
if fonts == ["all"]:
    fonts = ["plex", "inter"]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for font in fonts:
        page = browser.new_page()
        page.goto(SRC.as_uri())
        page.evaluate(f"document.documentElement.dataset.font = '{font}'")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        target = OUT / f"samples-chromium-{font}.pdf"
        page.pdf(path=str(target), format="A4", print_background=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                 prefer_css_page_size=True)
        print("wrote", target.relative_to(ROOT))
        page.close()
    browser.close()
