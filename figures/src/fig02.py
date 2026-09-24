#!/usr/bin/env python3
"""A 02 (Edzéselmélet) modul ábrái. Futtatás: python3 figures/src/fig02.py → figures/svg/02-*.svg
Adatok: data/sources.yaml kulcsai a függvények docstringjében; a „szerkesztői/szimuláció” jelű részek levezetések."""
import math
from figlib import SVG, C, S, ST, scale

BLUE, ORANGE, GREEN, INK, INK2, MUTED, HAIR, BASE = S["1"], S["2"], S["3"], C["ink"], C["ink-2"], C["muted"], C["hairline"], C["baseline"]
DEEP = C["brand-deep"]
YELLOW = S["4"]


def fmt(x, d=0):
    return (f"{x:.{d}f}").replace(".", ",")


# 1 ---------------------------------------------------------------
def forma_vs_terheles():
    """silva-oliveira-2024-pol-meta (TT SMD −0,01 CI −0,28–0,25; VO2peak SMD 0,24 CI 0,01–0,48),
    sylta-2016-hit-periodization (3 kar, 5–10 % javulás, nincs különbség — sematikus oszlopok)."""
    W, H = 560, 230
    svg = SVG(W, H)
    # bal: forest
    bx0, bx1 = 70, 300
    def X(s): return scale(s, -0.6, 0.8, bx0, bx1)
    y0 = 150
    svg.line(X(0), 45, X(0), y0, BASE, 1)
    for s in (-0.4, -0.2, 0.2, 0.4, 0.6):
        svg.line(X(s), 45, X(s), y0, HAIR, 1)
    for s in (-0.4, 0, 0.4):
        svg.text(X(s), y0 + 14, fmt(s, 1).replace("-", "−"), 8.5, MUTED, "middle")
    rows = [("időfutam-teljesítmény", -0.01, -0.28, 0.25, MUTED), ("VO2max", 0.24, 0.01, 0.48, BLUE)]
    for i, (lab, m, lo, hi, col) in enumerate(rows):
        y = 70 + i * 40
        svg.line(X(lo), y, X(hi), y, col, 2)
        svg.line(X(lo), y - 4, X(lo), y + 4, col, 2); svg.line(X(hi), y - 4, X(hi), y + 4, col, 2)
        svg.circle(X(m), y, 4.5, col)
        svg.text(bx0, y - 12, lab + f" · SMD {fmt(m,2).replace('-','−')}", 8.5, INK2)
    svg.text((bx0 + bx1) / 2, 26, "polarizált vs. többi eloszlás (17 vizsgálat, n = 437)", 9, INK2, "middle", 600)
    svg.text((bx0 + bx1) / 2, y0 + 30, "← többi jobb · polarizált jobb →", 8, MUTED, "middle")
    svg.text(X(0.02), 58, "0", 8, MUTED)
    # jobb: sylta
    cx0 = 370
    def Y2(p): return scale(p, 0, 12, 170, 60)
    labs = ["növekvő HIT", "csökkenő HIT", "vegyes HIT"]
    vals = [7.5, 7.5, 7.5]
    for i, (lab, v) in enumerate(zip(labs, vals)):
        x = cx0 + i * 56
        svg.rect(x, Y2(v), 38, 170 - Y2(v), BLUE, rx=3, opacity=0.85)
        svg.text(x + 19, Y2(v) - 5, "5–10 %", 8, INK, "middle", 600)
        svg.text(x + 19, 183, lab, 7.5, INK2, "middle")
    svg.line(cx0 - 10, 170, cx0 + 3 * 56, 170, BASE, 1)
    svg.text(cx0 + 84, 26, "azonos terhelés, három elrendezés", 9, INK2, "middle", 600)
    svg.text(cx0 + 84, 40, "(n = 63 kerékpáros, 12 hét): nincs különbség", 8, MUTED, "middle")
    svg.text(cx0 + 84, 205, "javulás sematikusan — a pontos számok karonként nem közöltek", 7, MUTED, "middle")
    return svg.write("02-forma-vs-terheles.svg")


# 2 ---------------------------------------------------------------
def eloszlas():
    """seiler-kjerland-2006 (idő-alapon ~90/10; session ~80/20), kalkulátor-sávok (szerkesztői, A csomag Q1)."""
    W, H = 560, 240
    svg = SVG(W, H)
    def stack(x, y, w, parts, labels=False):
        cx = x
        cols = [BLUE, YELLOW, ST["serious"]]
        total = sum(parts)
        for p, col in zip(parts, cols):
            pw = w * p / total
            svg.rect(cx, y, pw, 20, col, opacity=0.85)
            if pw > 26: svg.text(cx + pw / 2, y + 14, f"{p} %", 8, "#fff", "middle", 600)
            cx += pw
    # bal
    svg.text(60, 26, "az elit hete kétféle számolással", 9, INK2, "start", 600)
    svg.text(60, 52, "idő-alapon", 8.5, INK2); stack(140, 40, 170, [90, 6, 4])
    svg.text(60, 82, "session-alapon", 8.5, INK2); stack(140, 70, 170, [80, 0, 20])
    # jobb: sávok
    svg.text(354, 26, "kalkulátor-sávok heti óraszámra", 9, INK2, "start", 600)
    rows = [("6–8 h/hét", [77, 13, 10]), ("8–12 h/hét", [82, 10, 8]), ("12–15+ h/hét", [88, 7, 5])]
    for i, (lab, parts) in enumerate(rows):
        y = 52 + i * 34
        svg.text(430, y - 3, lab, 8, INK2, "start", 600)
        stack(354, y, 186, parts)
    # legend
    for i, (col, lab) in enumerate([(BLUE, "Z1 — könnyű (VT1 alatt)"), (YELLOW, "Z2 — tempó"), (ST["serious"], "Z3 — kemény (VT2 fölött)")]):
        svg.rect(60 + i * 172, 150, 10, 10, col, rx=2, opacity=0.85); svg.text(74 + i * 172, 159, lab, 8, INK2)
    svg.text(60, 190, "kis óraszámnál a heti 1–2 minőségi edzés aránylag nagyobb szelet;", 8.5, INK2)
    svg.text(60, 203, "12+ óránál a többlet gyakorlatilag mind Z1 — a Z3 abszolút mennyisége nem nő tovább.", 8.5, INK2)
    svg.text(60, 224, "Idő-alapú arányok; session-alapon a Z3 magasabbnak látszik. Szerkesztői sávok (C).", 7.5, MUTED)
    return svg.write("02-eloszlas.svg")


# 3 ---------------------------------------------------------------
def volumen():
    """knechtle-2011-finishers-720km (r=0,44 óra; 0,37 táv), knechtle-2009 (befutók r²=0,000);
    horgonyok: pulford-2026 (4–6), houston (9–11), tatt-boundary (10–15), towers (15–20)."""
    W, H = 560, 230
    svg = SVG(W, H)
    # bal: korrelációk
    bx0 = 200
    def X(r): return scale(r, 0, 0.6, bx0, 330)
    rows = [("befejezés ~ heti edzésóra (720 km, n = 76)", 0.44, BLUE), ("befejezés ~ heti edzéstáv (720 km)", 0.37, BLUE), ("helyezés ~ 3 havi volumen (600 km, 28 befutó)", 0.0, ST["serious"])]
    for i, (lab, r, col) in enumerate(rows):
        y = 50 + i * 40
        svg.text(bx0 - 8, y + 4, lab, 8.5, INK2, "end")
        if r > 0:
            svg.rect(bx0, y - 7, X(r) - bx0, 14, col, rx=2, opacity=0.9)
            svg.text(X(r) + 5, y + 4, "r = " + fmt(r, 2), 8.5, INK, "start", 600)
        else:
            svg.text(bx0 + 4, y + 4, "r² = 0,000 — semmi", 8.5, ST["critical"], "start", 600)
    svg.text(180, 24, "két kvalifikációs verseny (férfi)", 9, INK2, "middle", 600)
    svg.line(bx0, 36, bx0, 165, BASE, 1)
    # jobb: óraszám-horgonyok
    cx0, cx1 = 400, 545
    def Y(h): return scale(h, 0, 22, 195, 40)
    for h in (5, 10, 15, 20):
        svg.line(cx0 - 4, Y(h), cx1, Y(h), HAIR, 1); svg.text(cx0 - 8, Y(h) + 3, f"{h} h", 8, MUTED, "end")
    pts = [("CTS time-crunched", 5, MUTED), ("amatőr TCR-teljesítő", 10, BLUE), ("edzői minimum 320+ km-re", 12.5, BLUE), ("elit-közeli sáv", 17.5, ORANGE)]
    for i, (lab, h, col) in enumerate(pts):
        y = Y(h)
        svg.circle(cx0 + 14, y, 4.5, col)
        svg.text(cx0 + 24, y + 3, lab, 7.8, INK2)
    svg.text((cx0 + cx1) / 2, 24, "óraszám-horgonyok (edzői/versenyzői)", 9, INK2, "middle", 600)
    svg.text(60, 218, "A volumen belépőjegy a célba éréshez — a befutók rangsorát már nem az órák adják.", 8.5, INK2)
    return svg.write("02-volumen.svg")


# 4 ---------------------------------------------------------------
def durability_edzes():
    """spragg-2022-durability-training (VT1 alatti idő ~ fáradt-teljesítmény javulás, r=0,43 — sematikus szórásdiagram),
    ronnestad-2011-strength-185min (371→400 W; kontroll változatlan)."""
    W, H = 560, 235
    svg = SVG(W, H)
    # bal: szórás sematikus
    bx0, bx1, by0, by1 = 60, 280, 180, 50
    import random
    random.seed(7)
    svg.line(bx0, by0, bx1, by0, BASE, 1); svg.line(bx0, by0, bx0, by1, BASE, 1)
    for i in range(14):
        x = random.uniform(0.05, 0.95); noise = random.gauss(0, 0.18)
        y = min(0.95, max(0.05, x * 0.5 + 0.25 + noise))
        svg.circle(scale(x, 0, 1, bx0 + 8, bx1 - 8), scale(y, 0, 1, by0 - 8, by1 + 8), 3.5, BLUE, opacity=0.8)
    svg.line(scale(0.06, 0, 1, bx0, bx1), scale(0.28, 0, 1, by0, by1), scale(0.95, 0, 1, bx0, bx1), scale(0.72, 0, 1, by0, by1), DEEP, 2)
    svg.text((bx0 + bx1) / 2, 26, "VT1 alatti edzésidő és a fáradt-teljesítmény", 9, INK2, "middle", 600)
    svg.text((bx0 + bx1) / 2, 40, "javulása (U23 profik, r = 0,43 — sematikus)", 8, MUTED, "middle")
    svg.text((bx0 + bx1) / 2, by0 + 16, "Z1-edzésidő →", 8.5, INK2, "middle")
    svg.text(bx0 - 40, (by0 + by1) / 2, "Δ fáradt watt →", 8.5, MUTED, "middle", rotate=-90)
    # jobb: strength
    cx0 = 360
    def Y(w): return scale(w, 340, 420, 180, 50)
    bars = [("erősítés előtt", 371, MUTED), ("12 hét után", 400, ORANGE), ("kontroll", 372, HAIR)]
    for i, (lab, w, col) in enumerate(bars):
        x = cx0 + i * 56
        svg.rect(x, Y(w), 40, 180 - Y(w), col, rx=3, opacity=0.95)
        svg.text(x + 20, Y(w) - 5, f"{w} W", 8.5, INK, "middle", 600)
        svg.text(x + 20, 193, lab, 7.5, INK2, "middle")
    svg.line(cx0 - 8, 180, cx0 + 3 * 56, 180, BASE, 1)
    svg.text(cx0 + 80, 26, "5 perces watt 185 perc tekerés után", 9, INK2, "middle", 600)
    svg.text(cx0 + 80, 40, "(heti 2 nehéz láberősítés, n = 20 férfi)", 8, MUTED, "middle")
    svg.text(cx0 + 80, 208, "+8 % fáradtan — frissen nem változott", 8.5, ORANGE, "middle", 600)
    svg.text(cx0 + 80, 221, "(a tengely 340 W-nál kezdődik)", 7, MUTED, "middle")
    return svg.write("02-durability-edzes.svg")


# 5 ---------------------------------------------------------------
def felkeszules():
    """Ütemterv-fázisok visszafelé (B/D csomag kalkulátor-blokkjai; edzői keret-szintézis, C)."""
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1, y = 40, 530, 62
    def X(w): return scale(w, -20, 0, x0, x1)  # hét a rajtig
    phases = [(-20, -11, "alap", BLUE, 0.35), (-11, -6, "építés (2+1 / 3+1)", BLUE, 0.6), (-6, -2.5, "specifikus csúcs", ORANGE, 0.75), (-2.5, 0, "taper (10–21 nap)", GREEN, 0.6)]
    for a, b, lab, col, op in phases:
        svg.rect(X(a), y - 24, X(b) - X(a), 48, col, rx=4, opacity=op * 0.5)
        svg.text((X(a) + X(b)) / 2, y + 3, lab, 8.5, INK, "middle", 600)
    for w in range(-20, 1, 2):
        svg.line(X(w), y + 26, X(w), y + 31, BASE, 1)
        svg.text(X(w), y + 43, f"{w}" if w else "rajt", 7.5, MUTED, "middle")
    svg.text(X(-16), y + 58, "hét a versenydátumig", 8.5, INK2, "middle")
    # jelölők — külön sorokban, vezetővonallal lefelé
    marks = [(-5, "600-as brevet (legkésőbb −4…−6. hét)", BLUE), (-4.5, "terhelés-csúcs (−4…−6. hét)", ORANGE), (-4, "2–4 napos főpróba", DEEP), (-1.6, "utolsó hosszú (−10–14. nap)", GREEN), (-1.1, "hőblokk (opció, 10–14 nap)", ST["serious"])]
    ly = y + 66
    for i, (w, lab, col) in enumerate(marks):
        yy = ly + i * 15
        svg.line(X(w), y + 24, X(w), yy - 4, col, 1.1, dash="3 2")
        svg.circle(X(w), yy - 4, 2.6, col)
        anchor = "end" if w < -3 else "end"
        svg.text(X(w) - 6, yy, lab, 7.8, INK2, "end")
    # brevet lépcső alul
    by = 228
    for i, (w, d) in enumerate([(-14, "200"), (-11, "300"), (-8, "400"), (-5, "600")]):
        svg.rect(X(w) - 16, by - 12, 32, 16, BLUE, rx=3, opacity=0.25 + i * 0.15)
        svg.text(X(w), by, d, 8, INK, "middle", 600)
    svg.text(x0, by, "brevet-lépcső:", 8.5, INK2)
    svg.text(x0, 24, "a felkészülés visszafelé tervezve (16–24 hét; edzői keret, C) — az ütemterv-generátor ezt tölti ki dátumokkal", 9, INK2, "start", 600)
    return svg.write("02-felkeszules.svg")


# 6 ---------------------------------------------------------------
def taper():
    """bosquet-2007-taper-meta (2 hét, −41–60 %, ES 0,72±0,36; intenzitás-csökkentés ES 0,33; gyakoriság ES 0,35)."""
    W, H = 560, 210
    svg = SVG(W, H)
    bx0 = 260
    def X(e): return scale(e, 0, 1.2, bx0, 520)
    rows = [("2 hét, −41–60 % volumen,\nintenzitás + gyakoriság marad", 0.72, 0.36, GREEN),
            ("intenzitás is csökkentve", 0.33, 0.0, ST["serious"]),
            ("csak gyakoriság csökkentve", 0.35, 0.0, YELLOW)]
    for i, (lab, e, sd, col) in enumerate(rows):
        y = 60 + i * 42
        for j, l in enumerate(lab.split("\n")):
            svg.text(bx0 - 10, y - 4 + j * 11, l, 8, INK2, "end")
        if sd:
            svg.line(X(max(0, e - sd)), y, X(e + sd), y, col, 2)
            svg.line(X(e - sd), y - 4, X(e - sd), y + 4, col, 2); svg.line(X(e + sd), y - 4, X(e + sd), y + 4, col, 2)
        svg.circle(X(e), y, 4.5, col)
        svg.text(X(e + sd) + 8, y + 3, "ES " + fmt(e, 2), 8.5, INK, "start", 600)
    for e in (0, 0.4, 0.8, 1.2):
        svg.line(X(e), 40, X(e), 185, HAIR, 1); svg.text(X(e), 198, fmt(e, 1), 8, MUTED, "middle")
    svg.text((bx0 + 520) / 2, 26, "taper-stratégiák hatásmérete (27 vizsgálat)", 9, INK2, "middle", 600)
    svg.text(40, 60, "tipikus nyereség ~3 %", 9, INK, "start", 600)
    svg.text(40, 74, "(0,5–6 %) — rövid, intenzív", 8, INK2)
    svg.text(40, 86, "teljesítményen mérve;", 8, INK2)
    svg.text(40, 98, "ultra-taper vizsgálat nincs.", 8, INK2)
    svg.text(40, 124, "Ultra-fordítás: 2–3 hét,", 8.5, INK2, "start", 600)
    svg.text(40, 136, "enyhébb lejtés, utolsó hosszú", 8, INK2)
    svg.text(40, 148, "a −10–14. napon, alvás-prioritás.", 8, INK2)
    return svg.write("02-taper.svg")


# 7 ---------------------------------------------------------------
def erosites():
    """ronnestad-2011-strength-185min (371→400 W fáradtan; frissen nincs változás), abt-2007-core-cycling (térd frontális 15,1→23,3°)."""
    W, H = 560, 210
    svg = SVG(W, H)
    # bal: ismét a strength — más nézet: friss vs fáradt
    bx0 = 70
    def Y(w): return scale(w, 340, 420, 165, 45)
    groups = [("frissen", [(370, MUTED), (373, MUTED)]), ("185 perc után", [(371, MUTED), (400, ORANGE)])]
    labels = ["előtte", "12 hét erősítés után"]
    x = bx0
    for glab, bars in groups:
        for i, (w, col) in enumerate(bars):
            svg.rect(x, Y(w), 34, 165 - Y(w), col, rx=3, opacity=0.95)
            svg.text(x + 17, Y(w) - 4, f"{w}", 8, INK, "middle", 600)
            x += 40
        svg.text(x - 42, 179, glab, 8, INK2, "middle")
        x += 26
    svg.line(bx0 - 8, 165, x - 20, 165, BASE, 1)
    svg.rect(bx0, 190, 9, 9, MUTED, rx=2); svg.text(bx0 + 13, 198, "előtte", 8, INK2)
    svg.rect(bx0 + 70, 190, 9, 9, ORANGE, rx=2); svg.text(bx0 + 84, 198, "12 hét heti 2 erősítés után", 8, INK2)
    svg.text(bx0 + 90, 212, "frissen nincs szignifikáns változás (sematikus); a tengely 340 W-nál kezdődik", 7, MUTED, "middle")
    svg.text(bx0 + 90, 26, "5 perces watt (n = 20 férfi)", 9, INK2, "middle", 600)
    # jobb: core
    cx0 = 380
    def Y2(d): return scale(d, 0, 28, 165, 55)
    for i, (lab, d, col) in enumerate([("pihent törzs", 15.1, BLUE), ("fárasztott törzs", 23.3, ST["serious"])]):
        xx = cx0 + i * 72
        svg.rect(xx, Y2(d), 44, 165 - Y2(d), col, rx=3, opacity=0.9)
        svg.text(xx + 22, Y2(d) - 4, fmt(d, 1) + "°", 8.5, INK, "middle", 600)
        svg.text(xx + 22, 179, lab, 7.8, INK2, "middle")
    svg.line(cx0 - 8, 165, cx0 + 150, 165, BASE, 1)
    svg.text(cx0 + 66, 26, "a térd frontális kitérése", 9, INK2, "middle", 600)
    svg.text(cx0 + 66, 40, "hajtás közben (n = 15): +54 %", 8, MUTED, "middle")
    svg.text(cx0 + 66, 198, "a törzsfáradás parazita-mozgást ad", 7.8, INK2, "middle")
    return svg.write("02-erosites.svg")


# 8 ---------------------------------------------------------------
def terheles():
    """TSS/h sávok (IF²×100, determinisztikus), CTL-szimuláció (42/7 napos EWMA, heti +5 rámpa, 3+1, taper — levezetés)."""
    W, H = 560, 240
    svg = SVG(W, H)
    # bal: TSS/h sávok
    bx0 = 150
    rows = [("Z1 könnyű, alsó", 25, 30, BLUE), ("Z1–Z2 ultra-alap", 31, 56, GREEN), ("Z2 tempó", 58, 81, YELLOW), ("Z3 küszöb", 83, 100, ST["serious"]), ("ultraverseny-\nintenzitás", 30, 49, DEEP)]
    def X(t): return scale(t, 0, 110, bx0, 300)
    for i, (lab, lo, hi, col) in enumerate(rows):
        y = 48 + i * 32
        for j, l in enumerate(lab.split("\n")):
            svg.text(bx0 - 8, y + 3 + j * 10 - (5 if "\n" in lab else 0), l, 8, INK2, "end")
        svg.rect(X(lo), y - 7, X(hi) - X(lo), 14, col, rx=3, opacity=0.85)
        svg.text(X(hi) + 5, y + 3, f"{lo}–{hi}", 8, INK, "start", 600)
    svg.line(X(100), 40, X(100), 205, BASE, 1, dash="4 3")
    svg.text(X(100), 222, "plafon: 100 TSS/óra", 7.5, MUTED, "middle")
    svg.text(190, 26, "TSS / óra zónánként", 9, INK2, "middle", 600)
    # jobb: CTL szimuláció
    cx0, cx1, cy0, cy1 = 360, 540, 190, 60
    weeks = 16
    ctl = 45.0; pts = []; day = 0
    tss_week = 450
    import math as m
    for w in range(weeks):
        light = (w % 4 == 3)
        taperw = (w >= weeks - 2)
        wt = tss_week * (0.55 if light else 1.0) * (0.5 if taperw else 1.0)
        for d in range(7):
            daily = wt / 7
            ctl = ctl + (daily - ctl) / 42
            day += 1
            pts.append((day, ctl))
        if not light and not taperw: tss_week += 35  # ~ +5 CTL/hét közelítés
    def PX(d): return scale(d, 0, weeks * 7, cx0, cx1)
    def PY(c): return scale(c, 40, 90, cy0, cy1)
    for c in (50, 70, 90):
        svg.line(cx0, PY(c), cx1, PY(c), HAIR, 1); svg.text(cx0 - 5, PY(c) + 3, f"{c}", 8, MUTED, "end")
    svg.path("M" + " L".join(f"{PX(d):.1f} {PY(min(90, c)):.1f}" for d, c in pts), BLUE, 2.2)
    svg.line(cx0, cy0, cx1, cy0, BASE, 1)
    for w in (0, 4, 8, 12, 16):
        svg.text(PX(w * 7), cy0 + 13, f"{w}. hét", 7.5, MUTED, "middle")
    svg.rect(PX((weeks - 2) * 7), cy1, PX(weeks * 7) - PX((weeks - 2) * 7), cy0 - cy1, GREEN, opacity=0.12)
    svg.text(PX((weeks - 1) * 7), cy1 + 12, "taper", 7.5, GREEN, "middle", 600)
    svg.text((cx0 + cx1) / 2, 26, "példa CTL-görbe (szimuláció):", 9, INK2, "middle", 600)
    svg.text((cx0 + cx1) / 2, 40, "heti ~+5 pont, 3+1 blokkok, 2 hét taper", 8, MUTED, "middle")
    svg.text((cx0 + cx1) / 2, 222, "a kalkulátor ezt rajzolja a te számaidból", 7.5, MUTED, "middle")
    return svg.write("02-terheles.svg")


# 9 ---------------------------------------------------------------
def hrv():
    """javaloyes-2019 (+5,1 % PPO, +7,3 % 40 perc TT), vesterinen-2016 (13,2 vs 17,7 intenzív edzés), medellin-2020 (meta null),
    stone-2021 (MAPE 4,10 / 6,84 / 112 %)."""
    W, H = 560, 220
    svg = SVG(W, H)
    # bal: RCT-k
    bx0 = 180
    def X(p): return scale(p, 0, 8, bx0, 320)
    rows = [("kerékpár: csúcsteljesítmény", 5.1, BLUE), ("kerékpár: 40 perces időfutam", 7.3, BLUE), ("futó: 3000 m (kevesebb", 2.1, GREEN)]
    for i, (lab, p, col) in enumerate(rows):
        y = 56 + i * 34
        svg.text(bx0 - 8, y + 3, lab, 8, INK2, "end")
        svg.rect(bx0, y - 7, X(p) - bx0, 14, col, rx=2, opacity=0.9)
        svg.text(X(p) + 5, y + 3, "+" + fmt(p, 1) + " %", 8.5, INK, "start", 600)
    svg.text(bx0 - 8, 56 + 2 * 34 + 15, "intenzív edzésből)", 8, INK2, "end")
    svg.text(180, 26, "HRV-vezérelt edzés RCT-k (kontroll: stagnált)", 9, INK2, "middle", 600)
    svg.text(180, 185, "a 8 RCT-s meta csoportszinten: nulla különbség —", 8.5, INK2, "middle")
    svg.text(180, 198, "„ugyanaz vagy jobb, kevesebb kemény napból”", 8.5, INK2, "middle", 600)
    # jobb: eszköz-validitás
    cx0 = 380
    def Y(m): return scale(math.log10(m), math.log10(2), math.log10(150), 170, 55)
    bars = [("app +\nmellkaspánt", 4.1, GREEN), ("okosgyűrű", 6.84, YELLOW), ("kamerás\nmérés", 112, ST["critical"])]
    for i, (lab, m, col) in enumerate(bars):
        x = cx0 + i * 56
        svg.rect(x, Y(m), 38, 170 - Y(m), col, rx=3, opacity=0.9)
        svg.text(x + 19, Y(m) - 4, fmt(m, 1) + " %", 8, INK, "middle", 600)
        for j, l in enumerate(lab.split("\n")):
            svg.text(x + 19, 183 + j * 10, l, 7.3, INK2, "middle")
    svg.line(cx0 - 8, 170, cx0 + 3 * 56, 170, BASE, 1)
    svg.text(cx0 + 80, 26, "rMSSD-hiba EKG-hoz képest", 9, INK2, "middle", 600)
    svg.text(cx0 + 80, 40, "(log skála; n = 5, 148 mérés) — a saját trend számít", 8, MUTED, "middle")
    return svg.write("02-hrv.svg")


# 10 --------------------------------------------------------------
def tuledzes():
    """meeusen-2013 (FOR/NFOR/OTS), tenhaaf-2017 (kérdőív 78 % a 3. napon; objektív: semmi), hausswirth-2014 (alvás −7,9 %; URTI 67 vs 11 %)."""
    W, H = 560, 220
    svg = SVG(W, H)
    # bal: kontinuum
    y = 70
    stages = [("terhelés", 60, GREEN, "napok"), ("FOR", 150, YELLOW, "napok–hetek"), ("NFOR", 250, ST["serious"], "hetek–hónapok"), ("OTS", 360, ST["critical"], "hónapok")]
    prev = 40
    for lab, xw, col, t in stages:
        svg.rect(prev, y - 18, xw - prev + 60, 36, col, rx=4, opacity=0.35)
        svg.text((prev + xw + 60) / 2, y - 26, "", 8, INK2, "middle")
        svg.text((prev + xw + 60) / 2, y + 3, lab, 9, INK, "middle", 600)
        svg.text((prev + xw + 60) / 2, y + 30, t, 7.3, MUTED, "middle")
        prev = xw + 64
    svg.text(40, 30, "a túlterhelés kontinuuma (konszenzus): a visszaút minden lépéssel hosszabb", 9, INK2, "start", 600)
    # jobb/alsó: korai jelek
    rows = [("kérdőív (fáradtság + edzéskészség), 3. nap", "78 % pontosság", GREEN),
            ("objektív napi mutatók (pulzus, hőmérséklet)", "egyénileg: semmi", ST["critical"]),
            ("alvásidő 6 hét túlterhelésben", "−7,9 %", ST["serious"]),
            ("felső légúti fertőzés (túlterheltek vs. kontroll)", "67 % vs. 11 %", ST["serious"])]
    for i, (lab, val, col) in enumerate(rows):
        yy = 130 + i * 22
        svg.circle(52, yy - 3, 3.5, col)
        svg.text(64, yy, lab, 8.5, INK2)
        svg.text(520, yy, val, 8.5, INK, "end", 600)
    svg.text(40, 112, "a korai jelek — mi működik", 9, INK2, "start", 600)
    return svg.write("02-tuledzes.svg")


# 11 --------------------------------------------------------------
def hoblokk():
    """tyler-2016 (6–14 nap indukció), daanen-2018 (lecsengés 2,3–2,6 %/nap; újra-indukció 8–12×), ronnestad-2022 (+2,4–2,6 % Hb, +4,9 % vs +1,7 %)."""
    W, H = 560, 210
    svg = SVG(W, H)
    x0, x1, y0, y1 = 55, 380, 165, 50
    def X(d): return scale(d, 0, 35, x0, x1)
    def Y(p): return scale(p, 0, 110, y0, y1)
    for p in (25, 50, 75, 100):
        svg.line(x0, Y(p), x1, Y(p), HAIR, 1); svg.text(x0 - 5, Y(p) + 3, f"{p} %", 8, MUTED, "end")
    for d in (0, 7, 14, 21, 28, 35):
        svg.line(X(d), y0, X(d), y0 + 4, BASE, 1); svg.text(X(d), y0 + 15, f"{d}", 8, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.text((x0 + x1) / 2, y0 + 30, "nap", 8.5, INK2, "middle")
    # görbe: indukció 0–12 nap 0→100, lecsengés 2,5 %/nap, újraindukció a 30. naptól gyors
    pts = []
    for i in range(0, 351):
        d = i / 10
        if d <= 12: v = 100 * (1 - math.exp(-d / 4.2))
        elif d <= 28: v = max(0, 100 * (1 - math.exp(-12 / 4.2)) - 2.5 * (d - 12) / 1 * 1)
        else: v = min(96, 55 + (d - 28) * 14)
        pts.append(f"{X(d):.1f} {Y(max(0, min(100, v))):.1f}")
    svg.path("M" + " L".join(pts), ORANGE, 2.4)
    svg.rect(X(0), y1, X(12) - X(0), y0 - y1, ORANGE, opacity=0.08)
    svg.text(X(6), y1 + 12, "indukció 6–14 nap", 8, INK2, "middle", 600)
    svg.text(X(20), Y(45), "lecsengés ~2,3–2,6 %/nap", 8, INK2, "middle")
    svg.rect(X(28), y1, X(31) - X(28), y0 - y1, GREEN, opacity=0.12)
    svg.text(X(29.5), y1 + 12, "újra-indukció", 7.5, GREEN, "middle", 600)
    svg.text(X(29.5), y1 + 22, "8–12× gyorsabb", 7.5, GREEN, "middle")
    svg.text(x0, 26, "a hőadaptáció kinetikája (meta-analízisek; a görbe sematikus)", 9, INK2, "start", 600)
    # jobb: Hb
    cx0 = 425
    def Y2(p): return scale(p, 0, 6, 165, 70)
    for i, (lab, p, col) in enumerate([("hőedzés", 4.9, ORANGE), ("kontroll", 1.7, MUTED)]):
        x = cx0 + i * 56
        svg.rect(x, Y2(p), 40, 165 - Y2(p), col, rx=3, opacity=0.9)
        svg.text(x + 20, Y2(p) - 4, "+" + fmt(p, 1) + " %", 8.5, INK, "middle", 600)
        svg.text(x + 20, 179, lab, 7.8, INK2, "middle")
    svg.line(cx0 - 8, 165, cx0 + 2 * 56 + 8, 165, BASE, 1)
    svg.text(cx0 + 48, 26, "teljesítmény 5 hét után", 8.5, INK2, "middle", 600)
    svg.text(cx0 + 48, 40, "mérsékelt klímában", 8, MUTED, "middle")
    svg.text(cx0 + 48, 54, "(elit kerékpárosok; Hb +2,4–2,6 %)", 7.3, MUTED, "middle")
    return svg.write("02-hoblokk.svg")


if __name__ == "__main__":
    for f in (forma_vs_terheles, eloszlas, volumen, durability_edzes, felkeszules, taper, erosites, terheles, hrv, tuledzes, hoblokk):
        print("wrote", f().name)
