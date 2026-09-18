"""Kis SVG-rajzoló segédkönyvtár a tokenek szerint (design/tokens/tokens.json).

Egyszerű, determinisztikus SVG-t ír: rács, tengely, oszlop, vonal, pont, szöveg.
A betűtípus-helyőrző {{FONT}} marad az SVG-ben; a build cseréli (Inter).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOK = json.loads((ROOT / "design/tokens/tokens.json").read_text())
C = {k: (v["value"] if isinstance(v, dict) and "value" in v else v) for k, v in TOK["color"].items()}
S = TOK["color"]["series"]; ST = TOK["color"]["status"]
FONT = "{{FONT}}"


class SVG:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def rect(self, x, y, w, h, fill, rx=0, opacity=1, stroke=None, sw=0, dash=None):
        extra = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        if dash: extra += f' stroke-dasharray="{dash}"'
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" fill-opacity="{opacity}"{extra}/>')

    def line(self, x1, y1, x2, y2, stroke, sw=1, dash=None, cap="round"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')

    def path(self, d, stroke, sw=2, fill="none", dash=None, opacity=1):
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" opacity="{opacity}"{dd}/>')

    def circle(self, cx, cy, r, fill, stroke=None, sw=0):
        extra = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}"{extra}/>')

    def text(self, x, y, s, size=10, fill=None, anchor="start", weight=400, rotate=None, family=None):
        fill = fill or C["muted"]
        rot = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
        fam = f' font-family="{family}"' if family else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{fam}{rot}>{s}</text>')

    def write(self, name):
        out = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">\n'
               + "\n".join(self.parts) + "\n</svg>\n")
        p = ROOT / "figures/svg" / name
        p.write_text(out)
        return p


def hgrid(svg, x0, x1, ys, color=None):
    for y in ys:
        svg.line(x0, y, x1, y, color or C["hairline"], 1)


def scale(v, v0, v1, p0, p1):
    return p0 + (v - v0) * (p1 - p0) / (v1 - v0)
