#!/usr/bin/env python3
"""A 03 (Táplálkozás és hidratálás) modul ábrái. Futtatás: python3 figures/src/fig03.py → figures/svg/03-*.svg
Adatok: data/sources.yaml kulcsai szerint (a függvények docstringjében); a „levezetés” jelű számok képletből."""
import math
from figlib import SVG, C, S, ST, scale

BLUE, ORANGE, GREEN, INK, INK2, MUTED, HAIR, BASE = S["1"], S["2"], S["3"], C["ink"], C["ink-2"], C["muted"], C["hairline"], C["baseline"]
DEEP = C["brand-deep"]
YELLOW = S["4"]


def fmt(x, d=0):
    return (f"{x:.{d}f}").replace(".", ",")


def legend(svg, x, y, items, gap=150):
    for i, (col, lab) in enumerate(items):
        svg.rect(x + i * gap, y - 7, 10, 10, col, rx=2)
        svg.text(x + i * gap + 15, y + 2, lab, 8.5, INK2)


# 1 ---------------------------------------------------------------
def energiamerleg():
    """enqvist-2010 (24 h: 18 050 forgalom / 8450 bevitel; 6 nap: 80 000 → 13 300/nap), geesmann-2014 (1230 km, 43 h: 25 303 / 19 749 → napi 14 100 / 11 000, levezetés),
    hulton-2010 (RAAM-váltó DLW: 6420 forgalom / 4918 bevitel per fő per nap), hyldahl-2024 (Tour Divide: energiaegyensúly az első 9 napon, DLW)."""
    rows = [("24 órás ultra (n = 9)", 18050, 8450, "47 %"), ("1230 km nonstop, napi (n = 14)", 14100, 11000, "78 %"),
            ("RAAM 4 fős váltó, fő/nap (DLW)", 6420, 4918, "77 %"), ("6 napos kalandverseny, napi (n = 6)", 12600, None, "bevitel nem közölt"),
            ("Tour Divide, 1–9. nap (n = 1, DLW)", None, None, "energiaegyensúly")]
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1 = 215, 530
    def X(k): return scale(k, 0, 20000, x0, x1)
    for k in (5000, 10000, 15000, 20000):
        svg.line(X(k), 28, X(k), 208, HAIR, 1); svg.text(X(k), 220, f"{k // 1000} 000", 8.5, MUTED, "middle")
    svg.text((x0 + x1) / 2, 236, "kcal / nap", 9, INK2, "middle")
    for i, (lab, tee, ei, note) in enumerate(rows):
        y = 36 + i * 36
        svg.text(x0 - 8, y + 12, lab, 8.5, INK2, "end")
        if tee:
            svg.rect(x0, y, X(tee) - x0, 11, BLUE, rx=2, opacity=0.9)
            svg.text(X(tee) + 4, y + 9, f"{tee:,}".replace(",", " "), 8, INK, "start", 600)
        if ei:
            svg.rect(x0, y + 13, X(ei) - x0, 11, ORANGE, rx=2, opacity=0.9)
            svg.text(X(ei) + 4, y + 22, f"{ei:,} · {note}".replace(",", " "), 8, INK, "start", 600)
        elif tee:
            svg.text(x0 + 2, y + 22, note, 8, MUTED, "start")
        else:
            svg.text(x0 + 4, y + 15, note, 8.5, GREEN, "start", 600)
    legend(svg, x0, 20, [(BLUE, "mért / becsült forgalom"), (ORANGE, "bevitel")], 170)
    return svg.write("03-energiamerleg.svg")


# 2 ---------------------------------------------------------------
def cho_plafon():
    """jeukendrup-2006-ultra-exo (90 g/h glükóz: 1,24; 2:1: 1,40 g/perc), podlogar-2022-120vs90 (120 g/h 0,8:1: 1,51), hearris-2022-120-formats (1,56–1,66),
    ravikanti-2025 (120 g/h 1:1 elit futók: 1,68), morton-2026 (publikált csúcs 1,60–1,75). Görbék sematikusak."""
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1, y0, y1 = 60, 380, 195, 30
    def X(g): return scale(g, 0, 140, x0, x1)
    def Y(v): return scale(v, 0, 2.0, y0, y1)
    for v in (0.5, 1.0, 1.5, 2.0):
        svg.line(x0, Y(v), x1, Y(v), HAIR, 1); svg.text(x0 - 5, Y(v) + 3.5, fmt(v, 1), 8.5, MUTED, "end")
    for g in (0, 30, 60, 90, 120):
        svg.line(X(g), y0, X(g), y0 + 4, BASE, 1); svg.text(X(g), y0 + 15, f"{g}", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.text((x0 + x1) / 2, y0 + 30, "bevitt szénhidrát, g/óra", 9, INK2, "middle")
    svg.text(x0 - 44, (y0 + y1) / 2, "elégetett külső CH, g/perc →", 9, MUTED, "middle", rotate=-90)
    # 100 % hasznosulás vonal
    svg.line(X(0), Y(0), X(105), Y(1.75), HAIR, 1, dash="3 3")
    svg.text(X(107), Y(1.75) + 3, "100 %", 7.5, MUTED)
    def curve(plateau, col, eff=1.0):
        pts = []
        for i in range(0, 141, 2):
            v = min(i / 60 * eff, plateau)
            v = plateau * (1 - math.exp(-(i / 60) * eff / plateau * 1.6)) if i else 0
            pts.append(f"{X(i):.1f} {Y(v):.1f}")
        svg.path("M" + " L".join(pts), col, 2.4)
    curve(1.15, BLUE)
    curve(1.62, ORANGE)
    pts = [(90, 1.24, BLUE, "90 g/h csak glükóz: 1,24", 8, 26, "start"), (90, 1.40, ORANGE, "90 g/h 2:1: 1,40", -8, -6, "end"),
           (120, 1.51, ORANGE, "", 0, 0, "start"), (120, 1.62, ORANGE, "", 0, 0, "start"), (120, 1.68, DEEP, "120 g/h (1:0,8 – 1:1): 1,51–1,68", -8, -8, "end")]
    for g, v, col, lab, dx, dy, anc in pts:
        svg.circle(X(g), Y(v), 4.5, col, "#fff", 1.5)
        if lab: svg.text(X(g) + dx, Y(v) + dy, lab, 8, INK2, anc)
    svg.text(X(52), Y(0.62), "egy kapu (csak glükóz): plató 1,0–1,25 g/perc = 60–75 g/h", 8.5, BLUE, "start", 600)
    svg.text(X(2), Y(1.62) - 32, "két kapu (glükóz + fruktóz): 1,4–1,7 g/perc = 84–100 g/h", 8.5, ORANGE, "start", 600)
    # jobb: hatásfok
    bx = 470
    svg.text(bx, 40, "hasznosulás a 3. órától", 9, INK2, "middle", 600)
    for i, (lab, e, col) in enumerate((("≤90 g/h, 2:1", 80, BLUE), ("120 g/h, 1:0,8", 73, ORANGE), ("első 2 óra", 50, MUTED))):
        y = 60 + i * 42
        svg.rect(bx - 45, y, 90 * e / 100, 14, col, rx=2, opacity=0.85)
        svg.text(bx - 45, y - 4, lab + (" (vitairat)" if e == 50 else ""), 8, INK2)
        svg.text(bx - 45 + 90 * e / 100 + 4, y + 11, f"~{e} %", 8, INK, "start", 600)
    return svg.write("03-cho-plafon.svg")


# 3 ---------------------------------------------------------------
def terepi_bevitel():
    """geesmann-2014 (57 ± 18 g/h), black-2012 (52), martinez-2025-mallorca312 (59,2), bescos-2012 (~39 váltóidőre), strasser-inscyd-2022 (105–116),
    thomas-2016 (60–90 sáv), tiller-2019 (30–50), futó ultratrail egyéni 22–126 (arribalzaga-2021)."""
    W, H = 560, 240
    svg = SVG(W, H)
    x0, x1, y0, y1 = 60, 540, 185, 30
    def Y(g): return scale(g, 0, 130, y0, y1)
    for g in (30, 60, 90, 120):
        svg.line(x0, Y(g), x1, Y(g), HAIR, 1); svg.text(x0 - 5, Y(g) + 3.5, f"{g}", 8.5, MUTED, "end")
    svg.rect(x0, Y(90), x1 - x0, Y(60) - Y(90), GREEN, opacity=0.10)
    svg.text(x0 + 4, Y(75) + 3, "ajánlott alap", 8.5, GREEN, "start", 600); svg.text(x0 + 4, Y(75) + 14, "60–90 g/h", 8.5, GREEN, "start", 600)
    svg.rect(x0, Y(50), x1 - x0, Y(30) - Y(50), YELLOW, opacity=0.08)
    svg.text(x0 + 4, Y(40) + 3, "ultrafutó-", 8, INK2, "start"); svg.text(x0 + 4, Y(40) + 13, "állásfoglalás 30–50", 8, INK2, "start")
    bars = [("1230 km nonstop\n(n = 14)", 57, 18, BLUE), ("384 km\n(n = 18)", 52, 0, BLUE), ("Mallorca 312\n(n = 138)", 59, 0, BLUE),
            ("8 fős váltó,\neltelt órára", 39, 0, MUTED), ("elit 24 h rekord\n(n = 1, közlés)", 110, 0, ORANGE)]
    bw = 48
    for i, (lab, g, sd, col) in enumerate(bars):
        x = x0 + 120 + i * 84
        svg.rect(x, Y(g), bw, y0 - Y(g), col, rx=3, opacity=0.9)
        if sd:
            svg.line(x + bw / 2, Y(g - sd), x + bw / 2, Y(g + sd), INK, 1.2)
            svg.line(x + bw / 2 - 5, Y(g + sd), x + bw / 2 + 5, Y(g + sd), INK, 1.2)
            svg.line(x + bw / 2 - 5, Y(g - sd), x + bw / 2 + 5, Y(g - sd), INK, 1.2)
        svg.text(x + bw / 2, Y(g + (sd or 0)) - 5, ("105–116" if i == 4 else fmt(g)) + " g/h", 8.5, INK, "middle", 600)
        for j, l in enumerate(lab.split("\n")):
            svg.text(x + bw / 2, y0 + 13 + j * 11, l, 8, INK2, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.text(x0 - 44, (y0 + y1) / 2, "szénhidrát g/óra →", 9, MUTED, "middle", rotate=-90)
    svg.text(x0, 18, "mért óránkénti szénhidrát-bevitel ultrakerékpáron; egyéni szórás futóultrán 22–126 g/h", 9.5, INK2, "start", 600)
    return svg.write("03-terepi-bevitel.svg")


# 4 ---------------------------------------------------------------
def zsiradaptacio():
    """randell-2017 (MFO 0,59, 0,17–1,27), maunder-2018 (0,53), volek-2016 (1,54 vs 0,67), burke-2017 (1,57), cao-2021 (TTE SMD −0,13, CI −0,66–0,40),
    burke-2017 (10 km: HCHO +6,6 %, LCHF −1,6 %), burke-2020 (HCHO −4,8 %, LCHF +2,3 %), mcswiney-2018 (100 km: −4,07 vs −1,13 perc, n.s.)."""
    W, H = 560, 230
    svg = SVG(W, H)
    # bal: zsírégetés
    x0, x1, y0, y1 = 55, 250, 180, 35
    def Y(v): return scale(v, 0, 1.8, y0, y1)
    for v in (0.5, 1.0, 1.5):
        svg.line(x0, Y(v), x1, Y(v), HAIR, 1); svg.text(x0 - 5, Y(v) + 3.5, fmt(v, 1), 8.5, MUTED, "end")
    bars = [("sportolói\nátlag", 0.59, 0.17, 1.27, BLUE), ("edzett\nállóképességi", 0.53, None, None, BLUE), ("vegyes,\nFASTER", 0.67, None, None, BLUE), ("keto\nadaptált", 1.54, 1.2, 1.57, ORANGE)]
    for i, (lab, v, lo, hi, col) in enumerate(bars):
        x = x0 + 12 + i * 47
        svg.rect(x, Y(v), 30, y0 - Y(v), col, rx=3, opacity=0.9)
        if lo:
            svg.line(x + 15, Y(lo), x + 15, Y(hi), INK, 1.2)
        svg.text(x + 15, Y(hi if hi else v) - 5, fmt(v, 2), 8, INK, "middle", 600)
        for j, l in enumerate(lab.split("\n")):
            svg.text(x + 15, y0 + 12 + j * 10, l, 7.5, INK2, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.text(x0, 20, "zsírégetés csúcsa, g/perc", 9, INK2, "start", 600)
    # jobb: teljesítmény
    bx0, bx1 = 330, 540
    def X(p): return scale(p, -8, 8, bx0, bx1)
    svg.line(X(0), 40, X(0), 155, BASE, 1)
    for p in (-6, -3, 3, 6):
        svg.line(X(p), 40, X(p), 155, HAIR, 1); svg.text(X(p), 165 - 8, f"{p:+d} %", 8, MUTED, "middle")
    svg.text((bx0 + bx1) / 2, 20, "teljesítmény-változás, keto vs. szénhidrát", 9, INK2, "middle", 600)
    rows = [("elit gyaloglók, 3 hét, 10 km (2017): keto", -1.6, ORANGE), ("… ugyanott szénhidrát", 6.6, BLUE),
            ("elit gyaloglók, 3,5 hét, 10 000 m (2020): keto", -2.3, ORANGE), ("… ugyanott szénhidrát", 4.8, BLUE)]
    for i, (lab, v, col) in enumerate(rows):
        y = 56 + i * 26
        svg.rect(min(X(0), X(v)), y - 5, abs(X(v) - X(0)), 10, col, rx=2, opacity=0.9)
        svg.text(bx0, y - 8, lab, 7.5, INK2)
        svg.text(X(v) + (4 if v > 0 else -4), y + 3, f"{v:+.1f} %".replace(".", ","), 7.5, INK, "start" if v > 0 else "end", 600)
    svg.text(bx0, 172, "meta-analízis, kimerülésig tartó idő: semleges", 7.5, INK2, "start", 600)
    svg.text(bx0, 183, "(SMD −0,13; CI −0,66 … 0,40)", 7.5, MUTED)
    svg.text(bx0, 197, "100 km kerékpár, 12 hét keto: nem szignifikáns;", 7.5, INK2, "start", 600)
    svg.text(bx0, 208, "a W/kg-javulást a −5,9 kg tömegvesztés adja", 7.5, MUTED)
    svg.text(bx0, 40, "+ = jobb (2020: időváltozásból átszámolva)", 7.5, MUTED)
    return svg.write("03-zsiradaptacio.svg")


# 5 ---------------------------------------------------------------
def gi_panasz():
    """stuempfle-2015-wser-gi (96 % bármely, 60 % hányinger), pfeiffer-2012 (Ironman súlyos 31 %, profi kerékpár 7 %), martinez-2025-mallorca312 (38,4 %, 13,8 % súlyos),
    snipe-2018 (I-FABP +127 % vs +432 %), vanwijck-2012 (352 / 507 / 474 / 875 pg/ml)."""
    W, H = 560, 240
    svg = SVG(W, H)
    x0, x1 = 150, 300
    rows = [("161 km ultrafutás, bármely tünet", 96, BLUE), ("… ebből hányinger", 60, BLUE), ("Ironman, súlyos tünet", 31, BLUE),
            ("312 km amatőr kerékpár, bármely", 38, ORANGE), ("… közepes / súlyos", 14, ORANGE), ("profi kerékpáros, súlyos", 7, ORANGE)]
    def X(p): return scale(p, 0, 100, x0, x1)
    for i, (lab, p, col) in enumerate(rows):
        y = 40 + i * 26
        svg.text(x0 - 6, y + 10, lab, 8, INK2, "end")
        svg.rect(x0, y, X(p) - x0, 13, col, rx=2, opacity=0.9)
        svg.text(X(p) + 4, y + 10, f"{p} %", 8.5, INK, "start", 600)
    svg.text(x0, 24, "gyomor-bél panasz gyakorisága", 9, INK2, "start", 600)
    # jobb: I-FABP
    bx = 380
    def Y(v): return scale(v, 0, 900, 200, 60)
    bars = [("nyugalom", 352, MUTED), ("ibuprofen\nnyugalomban", 507, MUTED), ("2 h kerékpár", 474, BLUE), ("kerékpár +\nibuprofen", 875, ST["critical"])]
    for i, (lab, v, col) in enumerate(bars):
        x = bx + i * 44 - 20
        svg.rect(x, Y(v), 30, 200 - Y(v), col, rx=3, opacity=0.9)
        svg.text(x + 15, Y(v) - 4, f"{v}", 8, INK, "middle", 600)
        for j, l in enumerate(lab.split("\n")):
            svg.text(x + 15, 212 + j * 10, l, 7.2, INK2, "middle")
    svg.line(bx - 25, 200, bx + 160, 200, BASE, 1)
    svg.text(bx + 65, 24, "bélsérülés jele (I-FABP, pg/ml)", 9, INK2, "middle", 600)
    svg.text(bx + 65, 38, "hő 35 °C: +432 % (22 °C: +127 %)", 8, ST["serious"], "middle", 600)
    return svg.write("03-gi-panasz.svg")


# 6 ---------------------------------------------------------------
def hidratalas():
    """geesmann-2014 (0,39 l/h), chlibkova-2014 (0,49 / 0,55 l/h; −2,0 / −1,3 kg), black-2014 (0,58 l/h; 39 % ≤135; 11 % dehidrált),
    armstrong-2017 (R² = 0,45; küszöb ~168 ml/kg; két EAH ~190 ml/kg, 130 mmol/l). A jobb panel sematikus."""
    W, H = 560, 240
    svg = SVG(W, H)
    # bal: bevitel
    x0, y0, y1 = 45, 185, 50
    def Y(v): return scale(v, 0, 0.8, y0, y1)
    bars = [("1230 km", 0.39, "stabil"), ("24 h MTB (1)", 0.49, "−2,0 kg"), ("24 h MTB (2)", 0.55, "−1,3 kg"), ("387 km", 0.58, "11 % dehidr.")]
    for i, (lab, v, note) in enumerate(bars):
        x = x0 + i * 42
        svg.rect(x, Y(v), 30, y0 - Y(v), BLUE, rx=3, opacity=0.9)
        svg.text(x + 15, Y(v) - 4, fmt(v, 2), 8, INK, "middle", 600)
        for j, l in enumerate(lab.split("\n")):
            svg.text(x + 15, y0 + 12 + j * 9, l, 7, INK2, "middle")
        svg.text(x + 15, y0 + 30, note, 6.8, MUTED, "middle")
    svg.line(x0 - 5, y0, x0 + 170, y0, BASE, 1)
    svg.text(x0, 28, "folyadékbevitel, l/óra", 9, INK2, "start", 600)
    # közép: 387 km
    cx, cy, r = 265, 120, 42
    def arc(a0, a1, col):
        a0r, a1r = math.radians(a0 - 90), math.radians(a1 - 90)
        x1_, y1_ = cx + r * math.cos(a0r), cy + r * math.sin(a0r)
        x2_, y2_ = cx + r * math.cos(a1r), cy + r * math.sin(a1r)
        large = 1 if a1 - a0 > 180 else 0
        svg.path(f"M{cx},{cy} L{x1_:.1f},{y1_:.1f} A{r},{r} 0 {large} 1 {x2_:.1f},{y2_:.1f} Z", "#fff", 1.5, fill=col)
    arc(0, 140, ST["serious"]); arc(140, 180, ORANGE); arc(180, 360, HAIR)
    svg.text(cx, 28, "387 km, célba érők (n = 18)", 9, INK2, "middle", 600)
    svg.rect(cx - 55, 178, 9, 9, ST["serious"], rx=2); svg.text(cx - 42, 186, "39 % hígult (≤135 mmol/l)", 8, INK2)
    svg.rect(cx - 55, 194, 9, 9, ORANGE, rx=2); svg.text(cx - 42, 202, "11 % mérsékelten kiszáradt", 8, INK2)
    svg.rect(cx - 55, 210, 9, 9, HAIR, rx=2); svg.text(cx - 42, 218, "50 % normál", 8, INK2)
    # jobb: Na vs bevitel
    bx0, bx1, by0, by1 = 380, 540, 185, 50
    def X(v): return scale(v, 60, 220, bx0, bx1)
    def YY(na): return scale(na, 125, 150, by0, by1)
    for na in (130, 135, 140, 145):
        svg.line(bx0, YY(na), bx1, YY(na), HAIR, 1); svg.text(bx0 - 4, YY(na) + 3, f"{na}", 7.5, MUTED, "end")
    for v in (80, 120, 160, 200):
        svg.text(X(v), by0 + 12, f"{v}", 7.5, MUTED, "middle")
    svg.line(bx0, by0, bx1, by0, BASE, 1)
    svg.line(X(70), YY(143), X(205), YY(132), BLUE, 2)
    svg.rect(bx0, YY(135), bx1 - bx0, by0 - YY(135), ST["serious"], opacity=0.08)
    svg.line(X(168), by1, X(168), by0, ST["critical"], 1.2, dash="4 3")
    svg.text(X(168) - 3, by1 + 9, "~168 ml/kg", 7.5, ST["critical"], "end", 600)
    for v, na in ((188, 130), (193, 130)):
        svg.circle(X(v), YY(na), 4, ST["critical"], "#fff", 1.2)
    svg.text((bx0 + bx1) / 2, 28, "164 km hőségtúra: vér-Na és az ivott folyadék", 8.5, INK2, "middle", 600)
    svg.text((bx0 + bx1) / 2, 40, "ml/kg/nap (R² = 0,45, n = 33, sematikus)", 7.5, MUTED, "middle")
    svg.text((bx0 + bx1) / 2, by0 + 24, "összes folyadék, ml/kg", 8, INK2, "middle")
    return svg.write("03-hidratalas.svg")


# 7 ---------------------------------------------------------------
def izzadas_natrium():
    """baker-2016-sweat-normative (egésztest [Na+] 35,9 ± 10,4 mmol/l, 18,2–70,8 → ~830 (410–1630) mg/l; n = 506), barnes-2019 (1190 ± 640 mg/h).
    A haranggörbe normális eloszlás a közölt átlaggal és szórással (sematikus)."""
    W, H = 560, 200
    svg = SVG(W, H)
    x0, x1, y0, y1 = 50, 540, 130, 30
    mu, sd = 830, 240
    def X(v): return scale(v, 200, 1800, x0, x1)
    bands = [(200, 500, "alacsony", GREEN), (500, 1000, "közepes", BLUE), (1000, 1500, "magas", YELLOW), (1500, 1800, "nagyon magas", ST["serious"])]
    for a, b, lab, col in bands:
        svg.rect(X(a), y1, X(b) - X(a), y0 - y1, col, opacity=0.10)
        svg.text((X(a) + X(b)) / 2, y0 + 28, lab, 8.5, INK2, "middle", 600)
    pts = []
    for i in range(0, 161):
        v = 200 + i * 10
        d = math.exp(-0.5 * ((v - mu) / sd) ** 2)
        pts.append(f"{X(v):.1f} {scale(d, 0, 1, y0, y1 + 10):.1f}")
    svg.path("M" + " L".join(pts), BLUE, 2.2)
    for v in (400, 800, 1200, 1600):
        svg.line(X(v), y0, X(v), y0 + 4, BASE, 1); svg.text(X(v), y0 + 15, f"{v}", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.line(X(830), y1 + 10, X(830), y0, INK, 1, dash="3 3")
    svg.text(X(830) + 5, y1 + 18, "átlag ~830 mg/l", 8.5, INK, "start", 600)
    svg.line(X(410), y0 - 6, X(1630), y0 - 6, INK2, 1.2)
    svg.text(X(410), y0 - 10, "410", 7.5, INK2, "middle"); svg.text(X(1630), y0 - 10, "1630 mg/l", 7.5, INK2, "middle")
    svg.text(x0, 18, "izzadás nátriumtartalma, mg/l (506 sportoló, egésztestre korrigálva)", 9.5, INK2, "start", 600)
    svg.text(x0, 178, "óránkénti veszteség = izzadásráta (l/h) × koncentráció (mg/l); állóképességi átlag ~1190 ± 640 mg/h  ·  1 g só = 393 mg nátrium", 8.5, INK2, "start")
    return svg.write("03-izzadas-natrium.svg")


# 8 ---------------------------------------------------------------
def koffein_alvas():
    """gardiner-2023 (107 mg ≥ 8,8 h; 217 mg ≥ 13,2 h; −45 perc TST), filtness-2026 (255 mg hatás 15–45 perc csúcs, 60–75 perc lecsengés), centofanti-2020 (200 mg + 30 perc)."""
    W, H = 560, 200
    svg = SVG(W, H)
    x0, x1, y = 40, 330, 100
    def X(h): return scale(h, 16, 0, x0, x1)
    svg.line(x0, y, x1, y, BASE, 1.5)
    for h in (16, 12, 8, 4, 0):
        svg.line(X(h), y - 4, X(h), y + 4, BASE, 1); svg.text(X(h), y + 18, f"{h} h" if h else "alvás", 8.5, MUTED, "middle")
    svg.rect(X(16), y - 30, X(13.2) - X(16), 12, GREEN, rx=2, opacity=0.5)
    svg.rect(X(16), y - 14, X(8.8) - X(16), 12, GREEN, rx=2, opacity=0.5)
    svg.rect(X(13.2), y - 30, X(0) - X(13.2), 12, ST["serious"], rx=2, opacity=0.35)
    svg.rect(X(8.8), y - 14, X(0) - X(8.8), 12, ST["serious"], rx=2, opacity=0.35)
    svg.text(X(16), y - 34, "217 mg (erős kávé vagy két koffeines gél): ≥ 13 órával az alvás előtt", 8, INK2)
    svg.text(X(16), y - 18 + 30, "", 8, INK2)
    svg.text(X(13.2) + 3, y - 21, "217 mg itt már rontja", 7.5, ST["critical"], "start", 600)
    svg.text(X(8.8) + 3, y - 5, "107 mg itt már rontja", 7.5, ST["critical"], "start", 600)
    svg.text(X(16), y + 40, "107 mg (egy kávé): ≥ 8,8 órával az alvás előtt", 8, INK2)
    svg.text(X(16), y + 54, "átlagos hatás: −45 perc alvásidő, −7 % hatékonyság, +9 perc elalvás (meta-analízis)", 8, MUTED)
    svg.text(x0, 30, "utolsó koffein a tervezett alvás előtt", 9.5, INK2, "start", 600)
    # jobb: koffein-alvás
    bx0, bx1, by0, by1 = 380, 540, 150, 50
    def BX(m): return scale(m, 0, 90, bx0, bx1)
    for m in (0, 30, 60, 90):
        svg.line(BX(m), by0, BX(m), by0 + 4, BASE, 1); svg.text(BX(m), by0 + 14, f"{m}", 8, MUTED, "middle")
    svg.line(bx0, by0, bx1, by0, BASE, 1)
    svg.rect(BX(0), by1, BX(20) - BX(0), by0 - by1, BLUE, opacity=0.10)  # 15–30 perces alvás (sematikus)
    svg.text(BX(10), by1 + 10, "alvás", 7.5, BLUE, "middle", 600)
    pts = []
    for i in range(0, 91):
        m = i
        v = (1 - math.exp(-m / 10)) / (1 + math.exp((m - 58) / 9))
        pts.append(f"{BX(m):.1f} {scale(v, 0, 1, by0, by1 + 8):.1f}")
    svg.path("M" + " L".join(pts), ORANGE, 2.2)
    svg.text((bx0 + bx1) / 2, 30, "koffein-alvás: 200 mg a 15–30 perces", 8.5, INK2, "middle", 600)
    svg.text((bx0 + bx1) / 2, 42, "alvás elején; hatás 15–45 perc, lecseng 60–75-re", 7.5, MUTED, "middle")
    svg.text((bx0 + bx1) / 2, by0 + 26, "perc a bevétel után", 8, INK2, "middle")
    return svg.write("03-koffein-alvas.svg")


# 9 ---------------------------------------------------------------
def kaloriasuruseg():
    """cimkeadat-kaloriasuruseg-2026 (kcal/100 g), chlibkova-2014-24h-mtb (box-etetés gyakoriság: banán 86,5 %, szelet 50 %, sajt 43 %, kóla 54 %)."""
    rows = [("földimogyoró", 609, ""), ("chips", 544, ""), ("tejcsokoládé", 535, ""), ("Snickers", 491, "24 h box: energiaszelet 50 %"), ("keksz", 483, ""),
            ("trappista sajt", 381, "24 h box: 43 %"), ("gumicukor", 340, ""), ("fehér kenyér", 255, ""), ("pizza, kebab (becslés)", 250, "nem ellenőrzött"),
            ("jégkrém", 164, ""), ("banán", 95, "24 h box: 87 %"), ("tej (2,8 %)", 62, ""), ("kóla (100 ml)", 44, "24 h box: 54 %")]
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1 = 150, 360
    def X(k): return scale(k, 0, 650, x0, x1)
    for i, (lab, k, note) in enumerate(rows):
        y = 26 + i * 16.5
        col = ORANGE if k >= 400 else (BLUE if k >= 200 else MUTED)
        if "becslés" in lab: col = HAIR
        svg.text(x0 - 6, y + 9, lab, 8, INK2, "end")
        svg.rect(x0, y, X(k) - x0, 11, col, rx=2, opacity=0.9)
        svg.text(X(k) + 4, y + 9, f"{k}" + (f"  ·  {note}" if note else ""), 8, INK, "start", 600 if not note else 400)
    svg.line(x0, 22, x0, 26 + 13 * 16.5, BASE, 1)
    svg.text(x0 - 6, 16, "kcal / 100 g", 9, INK2, "end", 600)
    svg.rect(x0 + 175, 8, 9, 9, ORANGE, rx=2); svg.text(x0 + 188, 16, "sűrű (≥4 kcal/g)", 8, INK2)
    svg.rect(x0 + 290, 8, 9, 9, BLUE, rx=2); svg.text(x0 + 303, 16, "közepes (2–4)", 8, INK2)
    svg.rect(x0 + 375, 8, 9, 9, MUTED, rx=2); svg.text(x0 + 388, 16, "híg (<2)", 8, INK2)
    return svg.write("03-kaloriasuruseg.svg")


# 10 --------------------------------------------------------------
def feltoltes():
    """bussau-2002 (95 → 180 mmol/kg 24 h alatt, 2–3. nap plató), levezetés: raktár 2000–2400 kcal / (250–400 kcal/h CH-égetés) = 5–10 óra."""
    W, H = 560, 210
    svg = SVG(W, H)
    x0, x1, y0, y1 = 55, 240, 160, 40
    def X(d): return scale(d, 0, 3, x0, x1)
    def Y(g): return scale(g, 0, 200, y0, y1)
    for g in (50, 100, 150, 200):
        svg.line(x0, Y(g), x1, Y(g), HAIR, 1); svg.text(x0 - 5, Y(g) + 3.5, f"{g}", 8.5, MUTED, "end")
    for d in (0, 1, 2, 3):
        svg.line(X(d), y0, X(d), y0 + 4, BASE, 1); svg.text(X(d), y0 + 15, f"{d}. nap", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.path(f"M{X(0):.1f} {Y(95):.1f} C {X(0.4):.1f} {Y(160):.1f}, {X(0.7):.1f} {Y(178):.1f}, {X(1):.1f} {Y(180):.1f} L{X(2):.1f} {Y(180):.1f} L{X(3):.1f} {Y(180):.1f}", BLUE, 2.4)
    for d, g in ((0, 95), (1, 180), (2, 180), (3, 180)):
        svg.circle(X(d), Y(g), 4, BLUE, "#fff", 1.5)
    svg.text(X(0) + 6, Y(95) + 14, "95", 8.5, INK, "start", 600)
    svg.text(X(1), Y(180) - 8, "180 — egy nap után teli, a 2–3. nap nem ad többet", 7.5, INK, "start", 600)
    svg.text(x0, 22, "izomglikogén, mmol/kg (pihenő + 10 g/kg/nap, n = 8)", 9, INK2, "start", 600)
    # jobb
    bx0, bx1, by0, by1 = 345, 460, 160, 40
    def BX(k): return scale(k, 200, 450, bx0, bx1)
    def BY(h): return scale(h, 0, 12, by0, by1)
    for h in (4, 8, 12):
        svg.line(bx0, BY(h), bx1, BY(h), HAIR, 1); svg.text(bx0 - 5, BY(h) + 3.5, f"{h} h", 8.5, MUTED, "end")
    for k in (250, 300, 350, 400):
        svg.line(BX(k), by0, BX(k), by0 + 4, BASE, 1); svg.text(BX(k), by0 + 15, f"{k}", 8.5, MUTED, "middle")
    svg.line(bx0, by0, bx1, by0, BASE, 1)
    for store, col, lab in ((2400, ORANGE, "600 g"), (2000, BLUE, "500 g")):
        pts = [f"{BX(k):.1f} {BY(store / k):.1f}" for k in range(220, 431, 5)]
        svg.path("M" + " L".join(pts), col, 2.2)
        svg.text(BX(430) + 4, BY(store / 430) + 3, lab + " (≈" + fmt(store) + " kcal)", 8, col, "start", 600)
    svg.text((bx0 + bx1) / 2, 22, "hány óra tekerést fedez a teli raktár", 9, INK2, "middle", 600)
    svg.text((bx0 + bx1) / 2, by0 + 30, "szénhidrát-égetés, kcal/óra", 8.5, INK2, "middle")
    return svg.write("03-feltoltes.svg")


if __name__ == "__main__":
    for f in (energiamerleg, cho_plafon, terepi_bevitel, zsiradaptacio, gi_panasz, hidratalas, izzadas_natrium, koffein_alvas, kaloriasuruseg, feltoltes):
        print("wrote", f().name)
