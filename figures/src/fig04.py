#!/usr/bin/env python3
"""A 04 (Alvás) modul ábrái. Futtatás: python3 figures/src/fig04.py → figures/svg/04-*.svg
Adatok: data/sources.yaml kulcsai szerint (lásd a függvényekben)."""
import math
from figlib import SVG, C, S, ST, hgrid, scale

BLUE, ORANGE, INK, INK2, MUTED, HAIR, BASE = S["1"], S["2"], C["ink"], C["ink-2"], C["muted"], C["hairline"], C["baseline"]
DEEP = C["brand-deep"]


def egy_ejszaka():
    """craven-2022-akut (meta), roberts-2019-cycling (TT +10 %), temesi-2013-central (TTE −7,5 %)."""
    rows = [  # felirat, becslés %, alsó, felső, forrás-jelleg
        ("Állóképesség (összesített, 959 fő)", -5.55, -8.12, -2.99, "meta"),
        ("Robbanékonyság (összesített)", -6.26, -9.10, -3.41, "meta"),
        ("Erő (összesített)", -2.85, -4.47, -1.23, "meta"),
        ("Technikai készség (9 vizsgálat)", -20.9, -27.0, -14.9, "meta"),
        ("Kerékpáros időfutam ideje (13 fő)", +10.0, None, None, "cyc"),
        ("Kitartás kimerülésig, kerékpár (12 fő)", -7.5, None, None, "cyc"),
    ]
    W, H = 560, 272
    svg = SVG(W, H)
    x0, x1 = 250, 540
    vmin, vmax = -30, 15
    def X(v): return scale(v, vmin, vmax, x0, x1)
    ticks = [-30, -20, -10, 0, 10]
    for t in ticks:
        svg.line(X(t), 18, X(t), 210, HAIR if t else BASE, 1)
        svg.text(X(t), 226, f"{t:+d} %" if t else "0", 9.5, MUTED, "middle")
    svg.text((x0 + x1) / 2, 244, "változás egy éjszaka alvásmegvonás után", 9.5, INK2, "middle")
    bh, gap = 20, 11
    for i, (lab, v, lo, hi, kind) in enumerate(rows):
        y = 24 + i * (bh + gap)
        col = BLUE if kind == "meta" else ORANGE
        xa, xb = sorted([X(0), X(v)])
        svg.rect(xa, y, xb - xa, bh, col, rx=3)
        if lo is not None:
            svg.line(X(lo), y + bh / 2, X(hi), y + bh / 2, INK, 1.4)
            svg.line(X(lo), y + 4, X(lo), y + bh - 4, INK, 1.4); svg.line(X(hi), y + 4, X(hi), y + bh - 4, INK, 1.4)
        svg.text(x0 - 8, y + bh / 2 + 3.5, lab, 9.5, INK2, "end")
        # az érték a nulla vonal túloldalán, így soha nem ütközik a sávval vagy a felirattal
        lx = X(0) + (6 if v < 0 else -6)
        svg.text(lx, y + bh / 2 + 3.5, f"{v:+.1f} %".replace(".", ","), 9.5, INK, "start" if v < 0 else "end", 600)
    # legenda
    svg.rect(x0 - 200, 256, 10, 10, BLUE, rx=2); svg.text(x0 - 186, 265, "sok vizsgálat összesítése (vonal: bizonytalansági tartomány)", 8.5, INK2)
    svg.rect(x0 + 110, 256, 10, 10, ORANGE, rx=2); svg.text(x0 + 124, 265, "kerékpáros laborvizsgálat", 8.5, INK2)
    return svg.write("04-egy-ejszaka-hatas.svg")


def eberseg():
    """limdinges-2010-pvt: Hedges g (negatív = romlás)."""
    rows = [
        ("Figyelmi reakcióidő-teszt — kihagyott válaszok", -0.762),
        ("Figyelmi reakcióidő-teszt — reakcióidő", -0.732),
        ("Munkamemória — pontosság", -0.555),
        ("Összetett figyelem — pontosság", -0.479),
        ("Feldolgozási sebesség", -0.30),
        ("Következtetés, „gondolkodás”", -0.125),
    ]
    W, H = 560, 230
    svg = SVG(W, H)
    x0, x1 = 268, 540
    def X(v): return scale(-v, 0, 0.9, x0, x1)
    for t in [0, 0.3, 0.6, 0.9]:
        svg.line(X(-t), 18, X(-t), 190, HAIR if t else BASE, 1)
        svg.text(X(-t), 206, f"{t:.1f}".replace(".", ","), 9.5, MUTED, "middle")
    svg.text((x0 + x1) / 2, 224, "a romlás mértéke (összesített hatásméret, 70 közlemény, 1533 fő) →", 9.5, INK2, "middle")
    bh, gap = 20, 8
    for i, (lab, g) in enumerate(rows):
        y = 22 + i * (bh + gap)
        col = DEEP if i < 2 else (BLUE if i < 4 else S["1"])
        op = 1 if i < 2 else (0.75 if i < 4 else 0.5)
        svg.rect(x0, y, X(g) - x0, bh, col, rx=3, opacity=op)
        svg.text(x0 - 8, y + bh / 2 + 3.5, lab, 9.5, INK2, "end")
        svg.text(X(g) + 6, y + bh / 2 + 3.5, f"{-g:.2f}".replace(".", ","), 9.5, INK, "start", 600)
    return svg.write("04-eberseg-vs-gondolkodas.svg")


def kuszob():
    """Bal: dawson-1997-alcohol + williamson-2000-alcohol (0,74 %/óra, 17 h ≈ 0,05 %, 24 h ≈ 0,10 %).
    Jobb: tefft-2018-crash esélyhányadosok (log skála)."""
    W, H = 560, 250
    svg = SVG(W, H)
    # ---- bal panel: ébren töltött óra → véralkohol-egyenérték (‰)
    lx0, lx1, ly0, ly1 = 48, 268, 200, 30
    def LX(h): return scale(h, 8, 28, lx0, lx1)
    def LY(p): return scale(p, 0, 1.2, ly0, ly1)
    for p in [0, 0.5, 1.0]:
        svg.line(lx0, LY(p), lx1, LY(p), HAIR if p else BASE, 1)
        svg.text(lx0 - 6, LY(p) + 3.5, f"{p:.1f} ‰".replace(".", ","), 9, MUTED, "end")
    for h in [10, 17, 24]:
        svg.text(LX(h), 216, f"{h} h", 9, MUTED, "middle")
    svg.text((lx0 + lx1) / 2, 234, "ébren töltött órák", 9.5, INK2, "middle")
    # lineáris közelítés 10–26 h: 0 → ~1,15 ‰ (0,74 %/h teljesítményromlás ≈ BAC-egyenérték)
    svg.path(f"M{LX(10):.1f} {LY(0):.1f} L{LX(17):.1f} {LY(0.5):.1f} L{LX(24):.1f} {LY(1.0):.1f} L{LX(26):.1f} {LY(1.14):.1f}", BLUE, 2.4)
    for h, p, lab in [(17, 0.5, "17 h ≈ 0,5 ‰"), (24, 1.0, "24 h ≈ 1 ‰")]:
        svg.line(LX(h), LY(p), LX(h), ly0, DEEP, 1, dash="3 3")
        svg.circle(LX(h), LY(p), 4.5, C["paper"], DEEP, 2.4)
        svg.text(LX(h) - 8, LY(p) - 8, lab, 9.5, DEEP, "end", 600)
    svg.rect(LX(17), ly1, LX(28) - LX(17), ly0 - ly1, ST["warning"], opacity=0.08)
    svg.text(LX(27.6), ly0 - 8, "figyelem-zóna", 8.5, "#8a6100", "end", 600)
    # ---- jobb panel: baleset-okozás esélye (OR), log skála
    rx0, rx1, ry0, ry1 = 340, 540, 200, 44
    data = [("7–9 h", 1.0, None, None), ("6 h", 1.3, 1.04, 1.7), ("5 h", 1.9, 1.1, 3.2), ("4 h", 2.9, 1.4, 6.2), ("< 4 h", 15.1, 4.2, 54.4)]
    def RY(v): return scale(math.log10(v), math.log10(0.7), math.log10(60), ry0, ry1)
    for v in [1, 3, 10, 30]:
        svg.line(rx0, RY(v), rx1, RY(v), BASE if v == 1 else HAIR, 1)
        svg.text(rx0 - 6, RY(v) + 3.5, f"{v}×", 9, MUTED, "end")
    bw = 26
    for i, (lab, v, lo, hi) in enumerate(data):
        x = rx0 + 14 + i * 40
        col = BASE if v == 1 else (ST["critical"] if v > 10 else BLUE)
        svg.rect(x, RY(v), bw, ry0 - RY(v), col, rx=3)
        if lo:
            svg.line(x + bw / 2, RY(lo), x + bw / 2, RY(hi), INK, 1.4)
            svg.line(x + bw / 2 - 4, RY(lo), x + bw / 2 + 4, RY(lo), INK, 1.4); svg.line(x + bw / 2 - 4, RY(hi), x + bw / 2 + 4, RY(hi), INK, 1.4)
        svg.text(x + bw / 2, 216, lab, 9, MUTED, "middle")
        svg.text(x + bw / 2, RY(v) - 6 if not hi else RY(hi) - 6, f"{v:.1f}×".replace(".", ",") if v != 1 else "1×", 9, INK, "middle", 600)
    svg.text((rx0 + rx1) / 2, 234, "alvás az előző 24 órában", 9.5, INK2, "middle")
    svg.text(rx0, 18, "baleset-okozás esélye (6845 baleset)", 9.5, INK2, "start", 600)
    svg.text(lx0, 18, "teljesítményromlás véralkohol-egyenértékben", 9.5, INK2, "start", 600)
    return svg.write("04-biztonsagi-kuszob.svg")


def raf():
    """hurdiel-2026-raf: 2. ábra (óránkénti halmozott alvás, percben, ábráról leolvasva) és 1. ábra regressziója."""
    hours = list(range(21, 24)) + list(range(0, 21))
    mins = [1000, 1800, 3500, 6200, 7000, 7300, 6800, 5200, 3000, 1000, 600, 300, 250, 200, 150, 200, 350, 600, 450, 300, 250, 200, 300, 200]
    W, H = 560, 250
    svg = SVG(W, H)
    lx0, lx1, ly0, ly1 = 44, 300, 200, 30
    n = len(hours); bw = (lx1 - lx0) / n
    def LY(v): return scale(v, 0, 8000, ly0, ly1)
    svg.rect(lx0, ly1, bw * 10, ly0 - ly1, BLUE, opacity=0.06)  # 21–06 éjszaka
    for v in [0, 4000, 8000]:
        svg.line(lx0, LY(v), lx1, LY(v), BASE if v == 0 else HAIR, 1)
        svg.text(lx0 - 5, LY(v) + 3.5, f"{v // 1000} e. perc" if v else "0", 9, MUTED, "end")
    for i, (h, m) in enumerate(zip(hours, mins)):
        x = lx0 + i * bw
        col = DEEP if 0 <= h <= 3 else BLUE
        svg.rect(x + 1, LY(m), bw - 2, ly0 - LY(m), col, rx=1.5, opacity=1 if 0 <= h <= 3 else 0.55)
        if h % 3 == 0:
            svg.text(x + bw / 2, 216, f"{h:02d}", 9, MUTED, "middle")
    svg.text((lx0 + lx1) / 2, 234, "napszak (óra) — 23 versenyző összes alvása", 9.5, INK2, "middle")
    svg.text(lx0, 18, "mikor alszanak", 9.5, INK2, "start", 600)
    svg.text(lx0 + bw * 1.5, ly1 + 12, "éjszaka", 8.5, DEEP, "start", 600)
    # ---- jobb: helyezés vs átlagos napi alvás (regressziós egyenes + sáv, sematikus)
    rx0, rx1, ry0, ry1 = 352, 540, 200, 30
    def RX(m): return scale(m, 80, 320, rx0, rx1)
    def RY(r): return scale(r, 0, 100, ry0, ry1)
    for r in [0, 25, 50, 75, 100]:
        svg.line(rx0, RY(r), rx1, RY(r), BASE if r == 0 else HAIR, 1)
        svg.text(rx0 - 5, RY(r) + 3.5, f"{r}." if r else "1.", 9, MUTED, "end")
    for m in [100, 200, 300]:
        svg.text(RX(m), 216, f"{m}", 9, MUTED, "middle")
    svg.text((rx0 + rx1) / 2, 234, "átlagos alvás percben / 24 óra", 9.5, INK2, "middle")
    # sáv (95 % CI sematikusan) és egyenes y = −22,03 + 0,33x
    def reg(m): return -22.03 + 0.33 * m
    pts = [(RX(m), RY(reg(m))) for m in (95, 306)]
    band = f"M{RX(95):.1f} {RY(reg(95)-14):.1f} L{RX(306):.1f} {RY(reg(306)-8):.1f} L{RX(306):.1f} {RY(reg(306)+8):.1f} L{RX(95):.1f} {RY(reg(95)+14):.1f} Z"
    svg.path(band, "none", 0, fill=BLUE, opacity=0.12)
    svg.path(f"M{pts[0][0]:.1f} {pts[0][1]:.1f} L{pts[1][0]:.1f} {pts[1][1]:.1f}", DEEP, 2.4)
    # néhány sematikus pont az ábra mintázatát követve
    for m, r in [(95, 4), (105, 8), (135, 42), (145, 19), (165, 30), (185, 57), (215, 27), (225, 53), (235, 48), (245, 70), (255, 35), (265, 95), (275, 72), (285, 78), (290, 62), (300, 38), (306, 75)]:
        svg.circle(RX(m), RY(r), 3.2, C["paper"], BLUE, 1.6)
    svg.text(rx0, 18, "helyezés és napi alvás", 9.5, INK2, "start", 600)
    svg.text(RX(84), RY(97), "hátsó mezőny: ~300 perc / nap", 8.5, MUTED, "start", 600)
    svg.text(RX(120), RY(2), "élmezőny: ~100 perc / nap", 8.5, DEEP, "start", 600)
    return svg.write("04-race-across-france.svg")


def banking():
    """arnal-2015-extension (juginovic-2026-banking összefoglalása): ~16 vs ~8 kihagyott válasz a megvonás alatt;
    regeneráció után ~280 vs ~258 ms reakcióidő."""
    W, H = 560, 230
    svg = SVG(W, H)
    x0, y0, y1 = 60, 190, 40
    def Y(v): return scale(v, 0, 20, y0, y1)
    for v in [0, 5, 10, 15, 20]:
        svg.line(x0, Y(v), 300, Y(v), BASE if v == 0 else HAIR, 1)
        svg.text(x0 - 6, Y(v) + 3.5, str(v), 9, MUTED, "end")
    bars = [("szokásos alvás\n(8,2 óra/éj)", 16, BASE), ("nyújtott alvás\n(9,8 óra/éj, 6 éjszaka)", 8, DEEP)]
    for i, (lab, v, col) in enumerate(bars):
        x = x0 + 40 + i * 110
        svg.rect(x, Y(v), 60, y0 - Y(v), col, rx=3)
        svg.text(x + 30, Y(v) - 6, f"~{v}", 10.5, INK, "middle", 600)
        for j, l in enumerate(lab.split("\n")):
            svg.text(x + 30, 208 + j * 12, l, 8.8, INK2, "middle")
    svg.text(x0, 24, "kihagyott válaszok az átvirrasztott éjszaka alatt (14 fő)", 9.5, INK2, "start", 600)
    # jobb: reakcióidő a regeneráció után
    rx0, ry0, ry1 = 380, 190, 40
    def RY(v): return scale(v, 240, 290, ry0, ry1)
    for v in [240, 260, 280]:
        svg.line(rx0, RY(v), 540, RY(v), BASE if v == 240 else HAIR, 1)
        svg.text(rx0 - 6, RY(v) + 3.5, f"{v}", 9, MUTED, "end")
    for i, (v, col) in enumerate([(280, BASE), (258, DEEP)]):
        x = rx0 + 20 + i * 70
        svg.rect(x, RY(v), 44, ry0 - RY(v), col, rx=3)
        svg.text(x + 22, RY(v) - 6, f"~{v} ms", 9.5, INK, "middle", 600)
    svg.text(rx0 + 42, 208, "szokásos", 8.8, INK2, "middle"); svg.text(rx0 + 112, 208, "nyújtott", 8.8, INK2, "middle")
    svg.text(rx0, 24, "reakcióidő egy pihenőéjszaka után", 9.5, INK2, "start", 600)
    return svg.write("04-sleep-banking.svg")


def kronotipus():
    """facerchilds-2015-chronotype: csúcs ideje és csúcs–mélypont különbség kronotípusonként."""
    W, H = 560, 200
    svg = SVG(W, H)
    x0, x1 = 60, 400
    def X(h): return scale(h, 6, 24, x0, x1)
    y = 120
    svg.line(x0, y, x1, y, BASE, 1.2)
    for h in range(6, 25, 3):
        svg.line(X(h), y - 4, X(h), y + 4, BASE, 1)
        svg.text(X(h), y + 18, f"{h:02d}:00", 9, MUTED, "middle")
    svg.text((x0 + x1) / 2, y + 36, "a nap órája — mikor vagy a csúcson", 9.5, INK2, "middle")
    rows = [("korai (28 %)", 12 + 11 / 60, 7.6, S["4"]), ("köztes (48 %)", 15 + 49 / 60, 10.0, BLUE), ("késői (24 %)", 19 + 40 / 60, 26.2, DEEP)]
    for i, (lab, h, amp, col) in enumerate(rows):
        yy = y - 28 - i * 26
        svg.line(X(h), yy, X(h), y, col, 1.2, dash="3 3")
        svg.circle(X(h), yy, 7, col)
        svg.text(X(h) + 12, yy + 3.5, f"{lab} · csúcs {int(h):02d}:{int(round((h % 1) * 60)):02d}", 9.5, INK, "start", 600)
    # jobb: amplitúdó
    rx0 = 440
    def RY(v): return scale(v, 0, 30, 130, 30)
    for i, (lab, h, amp, col) in enumerate(rows):
        x = rx0 + i * 34
        svg.rect(x, RY(amp), 26, 130 - RY(amp), col, rx=3)
        svg.text(x + 13, RY(amp) - 6, f"{amp:.0f} %" if amp > 9 else f"{amp:.1f} %".replace(".", ","), 9.5, INK, "middle", 600)
    svg.line(rx0, 130, rx0 + 100, 130, BASE, 1)
    svg.text(rx0 + 50, 150, "csúcs–mélypont különbség", 9, INK2, "middle")
    svg.text(rx0 + 50, 163, "a napon belül", 9, INK2, "middle")
    svg.text(x0, 18, "121 versenysportoló · a csúcs időpontja több mint 7 órával tolódik", 9.5, INK2, "start", 600)
    return svg.write("04-kronotipus.svg")


def regeneracio():
    """kishi-2024 (rebound 9,9 h), fachan-2026 (töredezett 1–4. éjszaka), baron-2022 (~6 nap), raam-sleepcom-2022 (4–7 nap ritmus)."""
    W, H = 560, 150
    svg = SVG(W, H)
    x0, x1, y = 50, 540, 84
    def X(d): return scale(d, 0, 8, x0, x1)
    svg.line(x0, y, x1, y, BASE, 1.2)
    for d in range(0, 9):
        svg.line(X(d), y - 4, X(d), y + 4, BASE, 1)
        svg.text(X(d), y + 18, "cél" if d == 0 else f"{d}. nap", 9, MUTED, "middle")
    # sávok
    svg.rect(X(0), 30, X(1) - X(0), 14, DEEP, rx=2); svg.text(X(1) + 5, 40.5, "alvás-visszapótlás az 1. napon (~10 óra)", 8.5, DEEP, "start", 600)
    svg.rect(X(1), 50, X(4.5) - X(1), 14, BLUE, rx=2, opacity=0.85); svg.text(X(2.75), 60.5, "töredezett éjszakák, több ébredés", 8.5, "#fff", "middle", 600)
    svg.rect(X(0), 66, X(6) - X(0), 8, ORANGE, rx=2, opacity=0.5); svg.text(X(6) + 5, 73, "szubjektív helyreállás ~6 nap", 8.5, INK2, "start", 600)
    svg.rect(X(0), y + 26, X(1) - X(0), 12, ST["critical"], rx=2); svg.text(X(1) + 5, y + 35, "ne vezess", 8.5, ST["critical"], "start", 600)
    svg.text(x0, 18, "a célba érés utáni hét (futóversenyek terepadatai és versenyzői tapasztalat)", 9.5, INK2, "start", 600)
    return svg.write("04-regeneracio.svg")


def ket_folyamat():
    """Borbély-féle kétfolyamat-modell, sematikus. 48 óra: 1. éjszaka alvás, 2. éjszaka tekerés."""
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1, y0, y1 = 40, 540, 190, 40   # rajzterület
    def X(h): return scale(h, 0, 48, x0, x1)   # h = óra a 18:00-ás kezdettől
    # éjszakai sávok: 22–06 (4–12 h) és 46–54 → 28–36 h
    for a, b in ((4, 12), (28, 36)):
        svg.rect(X(a), y1, X(b) - X(a), y0 - y1, BLUE, opacity=0.07)
    # mélypont-sáv: 00–04 h → 6–10 h és 30–34 h (a 2. éjszakán jelölve)
    svg.rect(X(30), y1, X(34) - X(30), y0 - y1, DEEP, opacity=0.10)
    svg.line(x0, y0, x1, y0, BASE, 1)
    # S folyamat: 1. éjszaka alszik (esik), 2. éjszaka teker (tovább nő)
    # fent = nagyobb álmosság; alvás alatt (4–12 h) az S esik, utána 36 órán át nő
    svg.path(f"M{X(0):.1f} 118 L{X(4):.1f} 96 L{X(12):.1f} 168 L{X(28):.1f} 92 L{X(36):.1f} 66 L{X(48):.1f} 48", BLUE, 2.4)
    # C folyamat: szinusz, minimum ~09 h (03:00) és 33 h
    pts = []
    for i in range(0, 481):
        h = i / 10
        y = 118 - 30 * math.cos((h - 9) / 24 * 2 * math.pi)  # csúcs (legnagyobb álmosság) 03:00-kor, azaz h = 9 és 33
        pts.append(f"{X(h):.1f} {y:.1f}")
    svg.path("M" + " L".join(pts), ORANGE, 2.4)
    # x tengely: óraidő
    for h in range(0, 49, 6):
        clock = (18 + h) % 24
        svg.text(X(h), y0 + 16, f"{clock:02d}", 9, MUTED, "middle")
    svg.text(X(9), y0 + 32, "1. éjszaka — alszol", 9, INK2, "middle", 600)
    svg.text(X(33), y0 + 32, "2. éjszaka — tekersz", 9, INK2, "middle", 600)
    svg.text(x0 - 22, 111, "álmosság →", 9, MUTED, "middle", rotate=-90)
    # feliratok a rajzterületen kívül / üres helyen
    svg.text(X(15.5), 168, "S — alvásnyomás", 10, BLUE, "start", 600)
    svg.text(X(15.5), 180, "ébren nő, alvással ürül", 8.5, INK2, "start")
    svg.text(X(38), 160, "C — belső óra", 10, ORANGE, "start", 600)
    svg.text(X(38), 171, "napszakhoz kötött hullám", 8.5, INK2, "start")
    svg.rect(X(25), 20, X(39) - X(25), 15, DEEP, rx=3)
    svg.text(X(32), 31, "a kettő összeadódik: 00–04 h", 8.5, "#fff", "middle", 600)
    svg.line(X(32), 35, X(32), y1, DEEP, 1, dash="3 3")
    return svg.write("04-ket-folyamat-modell.svg")


if __name__ == "__main__":
    for f in (ket_folyamat, egy_ejszaka, eberseg, kuszob, raf, banking, kronotipus, regeneracio):
        print("wrote", f().name)
