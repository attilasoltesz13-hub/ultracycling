#!/usr/bin/env python3
"""A 08 (Pacing) modul ábrái. Futtatás: python3 figures/src/fig08.py → figures/svg/08-*.svg
Adatok: data/sources.yaml kulcsai szerint (a függvényekben); a „levezetés” jelű számok a Martin-modellből vagy a képletből."""
import math
from figlib import SVG, C, S, ST, scale

BLUE, ORANGE, GREEN, INK, INK2, MUTED, HAIR, BASE = S["1"], S["2"], S["3"], C["ink"], C["ink-2"], C["muted"], C["hairline"], C["baseline"]
DEEP = C["brand-deep"]
GRAY = C["baseline"]


def fmt(x, d=0):
    return (f"{x:.{d}f}").replace(".", ",")


# ---------- fizika (Martin 1998): sebesség adott teljesítményre
def speed(P, cda, crr=0.005, m=85.0, grade=0.0, rho=1.2, wind=0.0, eta=0.976):
    g = 9.81
    th = math.atan(grade)
    def power(v):
        return (0.5 * rho * cda * (v + wind) ** 2 * v + crr * m * g * math.cos(th) * v + m * g * math.sin(th) * v) / eta
    lo, hi = 0.0, 30.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if power(mid) < P: lo = mid
        else: hi = mid
    return (lo + hi) / 2 * 3.6


def intenzitas_tavolsag():
    """rothschild-2021 (210 W 24 h; 203 W váltó), knechtle-2019 (214,5 W), strasser-inscyd-2022 (272 W, C),
    schumacher-2011 (141 W RAAM), strasser-power2max-2018 (NP 162 W, C), brayson-2019 (109 W TCR 14 nap)."""
    pts = [  # felirat, tartam (óra, log), W, W/kg, fokozat
        ("24 h szóló, 861 km", 24, 210, "2,8", "B"),
        ("24 h pálya, 942 km", 24, 214.5, "2,8", "B"),
        ("24 h, 1026 km (edzői közlés)", 24, 272, "3,5", "C"),
        ("RAAM 2 fős váltó (75 h)", 154, 203, "2,7", "B"),
        ("RAAM szóló, 8 nap (NP, gyártói közlés)", 193, 162, "2,1", "C"),
        ("RAAM szóló, 11 nap", 263, 141, "1,8", "B"),
        ("TCR önellátó, 14 nap", 336, 109, "1,5", "B"),
    ]
    W, H = 560, 262
    svg = SVG(W, H)
    x0, x1, y0, y1 = 60, 540, 200, 30
    def X(h): return scale(math.log10(h), math.log10(18), math.log10(420), x0, x1)
    def Y(w): return scale(w, 80, 300, y0, y1)  # noqa
    for w in range(100, 301, 50):
        svg.line(x0, Y(w), x1, Y(w), HAIR, 1); svg.text(x0 - 6, Y(w) + 3.5, f"{w} W", 9, MUTED, "end")
    for h, lab in ((24, "24 óra"), (72, "3 nap"), (168, "7 nap"), (336, "14 nap")):
        svg.line(X(h), y0, X(h), y0 + 5, BASE, 1); svg.text(X(h), y0 + 17, lab, 9, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.text((x0 + x1) / 2, y0 + 34, "a verseny hossza (logaritmikus skála)", 9.5, INK2, "middle")
    svg.text(x0 - 46, (y0 + y1) / 2, "átlagteljesítmény →", 9, MUTED, "middle", rotate=-90)
    offs = {0: (9, 12), 1: (9, -8), 2: (9, 4), 3: (-9, 15), 4: (-9, -8), 5: (-9, 15), 6: (-9, 14)}
    for i, (lab, h, w, wkg, gr) in enumerate(pts):
        col = BLUE if gr == "B" else ORANGE
        svg.circle(X(h), Y(w), 5, col, "#fff", 1.5)
        dx, dy = offs[i]
        anchor = "start" if dx > 0 else "end"
        svg.text(X(h) + dx, Y(w) + dy, f"{lab} · {fmt(w)} W · {wkg} W/kg", 8.5, INK2, anchor)
    svg.circle(x0 + 6, 246, 4, BLUE); svg.text(x0 + 15, 249, "terepvizsgálat, mért", 8.5, INK2)
    svg.circle(x0 + 170, 246, 4, ORANGE); svg.text(x0 + 179, 249, "edzői / gyártói közlés", 8.5, INK2)
    return svg.write("08-intenzitas-tavolsag.svg")


def lecsenges_24h():
    """Bal: rothschild-2021 (−37 % W, −22 % HR 24 h alatt), fázisok knechtle-2019. Jobb: bossi-2017 (r = −0,58, n = 501) — sematikus."""
    W, H = 560, 250
    svg = SVG(W, H)
    # bal panel
    x0, x1, y0, y1 = 48, 300, 190, 30
    def X(h): return scale(h, 0, 24, x0, x1)
    def Y(p): return scale(p, 50, 110, y0, y1)
    for p in (60, 80, 100):
        svg.line(x0, Y(p), x1, Y(p), HAIR, 1); svg.text(x0 - 5, Y(p) + 3.5, f"{p} %", 8.5, MUTED, "end")
    for h in (0, 4, 9, 22, 24):
        svg.line(X(h), y0, X(h), y0 + 4, BASE, 1); svg.text(X(h), y0 + 15, f"{h} h", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    # fázisok
    svg.rect(X(4), y1, X(9) - X(4), y0 - y1, ORANGE, opacity=0.08)
    svg.text(X(6.5), y1 + 12, "4–9. óra: a legnagyobb esés", 8, INK2, "middle", 600)
    # teljesítmény: 100 → 63 (négyfázisú), pulzus: 100 → 78
    pw = [(0, 100), (4, 97), (9, 78), (22, 68), (24, 63)]
    hr = [(0, 100), (4, 96), (9, 86), (22, 79), (24, 78)]
    svg.path("M" + " L".join(f"{X(h):.1f} {Y(v):.1f}" for h, v in pw), BLUE, 2.4)
    svg.path("M" + " L".join(f"{X(h):.1f} {Y(v):.1f}" for h, v in hr), ORANGE, 2.4)
    svg.text(X(13), Y(72), "teljesítmény −37 %", 9, BLUE, "start", 600)
    svg.text(X(13), Y(86), "pulzus −22 %", 9, ORANGE, "start", 600)
    svg.text(x0, 18, "24 óra folyamatosan — a rajt %-ában (elit versenyző, n = 1)", 9.5, INK2, "start", 600)
    svg.text((x0 + x1) / 2, y0 + 30, "ébren töltött óra a rajttól", 9, INK2, "middle")
    # jobb panel: relatív rajtsebesség vs táv (sematikus szórásdiagram + trend)
    rx0, rx1, ry0, ry1 = 350, 540, 190, 30
    def RX(v): return scale(v, 0.95, 1.35, rx0, rx1)
    def RY(d): return scale(d, 80, 200, ry0, ry1)
    for d in (100, 150, 200):
        svg.line(rx0, RY(d), rx1, RY(d), HAIR, 1); svg.text(rx0 - 5, RY(d) + 3.5, f"{d} km", 8.5, MUTED, "end")
    for v in (1.0, 1.1, 1.2, 1.3):
        svg.line(RX(v), ry0, RX(v), ry0 + 4, BASE, 1); svg.text(RX(v), ry0 + 15, fmt(v, 1) + "×", 8.5, MUTED, "middle")
    svg.line(rx0, ry0, rx1, ry0, BASE, 1)
    import random
    rnd = random.Random(8)
    for _ in range(60):
        v = 0.98 + rnd.random() * 0.34
        d = 205 - (v - 0.98) * 260 + rnd.gauss(0, 14)
        d = max(85, min(198, d))
        svg.circle(RX(v), RY(d), 2.6, BLUE, opacity=0.45)
    svg.line(RX(0.98), RY(198), RX(1.32), RY(112), ORANGE, 2.2)
    svg.text(rx0, 18, "első 2 óra a saját átlaghoz képest (501 futó)", 9.5, INK2, "start", 600)
    svg.text((rx0 + rx1) / 2, ry0 + 30, "rajt-tempó / saját átlag", 9, INK2, "middle")
    svg.text(rx1, RY(190), "r = −0,58", 9.5, ORANGE, "end", 600)
    svg.text(rx0 + 4, ry1 + 14, "sematikus", 8, MUTED, "start")
    return svg.write("08-24h-lecsenges.svg")


def durability():
    """clark-2019-cp-dynamics: CP 260 → 236 W (2 h), 254 W CHO-val; W′ 17,9 → 14,7 (80 min) → 13,8 kJ (2 h)."""
    W, H = 560, 240
    svg = SVG(W, H)
    x0, x1, y0, y1 = 60, 330, 190, 30
    def X(t): return scale(math.log10(t), math.log10(1), math.log10(60), x0, x1)
    def Y(p): return scale(p, 200, 420, y0, y1)
    for p in (240, 280, 320, 360, 400):
        svg.line(x0, Y(p), x1, Y(p), HAIR, 1); svg.text(x0 - 5, Y(p) + 3.5, f"{p} W", 8.5, MUTED, "end")
    for t, lab in ((1, "1"), (3, "3"), (10, "10"), (30, "30"), (60, "60 perc")):
        svg.line(X(t), y0, X(t), y0 + 4, BASE, 1); svg.text(X(t), y0 + 15, lab, 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.text((x0 + x1) / 2, y0 + 30, "tartam (logaritmikus)", 9, INK2, "middle")
    def curve(cp, wp_kj, col, dash=None):
        pts = []
        for i in range(0, 121):
            t = 10 ** (i / 120 * math.log10(60))
            p = cp + wp_kj * 1000 / (t * 60)
            pts.append(f"{X(t):.1f} {Y(min(p, 420)):.1f}")
        svg.path("M" + " L".join(pts), col, 2.2, dash=dash)
    curve(260, 17.9, BLUE)
    curve(236, 13.8, ORANGE)
    curve(254, 13.5, GREEN, dash="5 3")
    for i, (lab, col) in enumerate((("frissen: CP 260 W", BLUE), ("2 h + 60 g/h CHO: CP 254 W", GREEN), ("2 h után: CP 236 W (−9 %)", ORANGE))):
        svg.line(X(6), 44 + i * 14, X(9), 44 + i * 14, col, 2.2, dash=("5 3" if col == GREEN else None))
        svg.text(X(9.6), 47 + i * 14, lab, 8.5, col, "start", 600)
    svg.text(x0, 18, "teljesítmény–tartam görbe (16 fő, labor)", 9.5, INK2, "start", 600)
    # jobb: W′ oszlopok
    bx = 430
    def BY(k): return scale(k, 0, 20, 190, 60)
    vals = [("frissen", 17.9, BLUE), ("80 perc", 14.7, ORANGE), ("2 óra", 13.8, ORANGE), ("2 h + CHO", 13.5, GREEN)]
    for i, (lab, k, col) in enumerate(vals):
        x = bx + i * 30 - 45
        svg.rect(x, BY(k), 22, 190 - BY(k), col, rx=2, opacity=0.9)
        svg.text(x + 11, BY(k) - 4, fmt(k, 1), 8.5, INK, "middle", 600)
        svg.text(x + 11, 203, lab, 7.5, INK2, "middle")
    svg.line(bx - 50, 190, bx + 80, 190, BASE, 1)
    svg.text(bx + 15, 18, "rövid tartalék (W′), kJ", 9.5, INK2, "middle", 600)
    svg.text(bx + 15, 32, "a szénhidrát ezen nem segít", 8.5, MUTED, "middle")
    return svg.write("08-durability.svg")


def idokoltsegvetes():
    """Levezetés: T = D/(v·h); Δ órák 4000 km-re. Presetek: white-2016-ridefar-method, evans-2022-bikeradar-bartholmoes,
    mckenzie-dotwatcher-tcr-2026, halfwayanywhere-tourdivide-2024 (C/B)."""
    D = 4000
    presets = [("TCR-középmezőny\n22 km/h · 12,5 h/nap", 22, 12.5, 4000), ("TCR-élmezőny\n26 km/h · 19 h/nap", 26, 19, 4000),
               ("Tour Divide-középmezőny\n15 km/h · 14,8 h/nap", 15, 14.8, 4000)]
    levers = [("+1 km/h", BLUE), ("+1 óra mozgás/nap", DEEP), ("−30 perc állás/nap", ORANGE)]
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1 = 40, 540
    gw = (x1 - x0) / 3
    def T(v, h): return D / (v * h) * 24
    ymax = 32
    y0, y1 = 190, 40
    def Y(val): return scale(val, 0, ymax, y0, y1)
    for t in (0, 10, 20, 30):
        svg.line(x0, Y(t), x1, Y(t), HAIR if t else BASE, 1); svg.text(x0 - 5, Y(t) + 3.5, f"{t} h", 8.5, MUTED, "end")
    for gi, (lab, v, h, dist) in enumerate(presets):
        base = T(v, h)
        vals = [base - T(v + 1, h), base - T(v, h + 1), base - T(v, h + 0.5)]
        gx = x0 + gi * gw + 18
        for li, ((ll, col), val) in enumerate(zip(levers, vals)):
            x = gx + li * 46
            svg.rect(x, Y(val), 34, y0 - Y(val), col, rx=2)
            svg.text(x + 17, Y(val) - 4, fmt(val), 9, INK, "middle", 600)
        l1, l2 = lab.split("\n")
        svg.text(gx + 60, y0 + 15, l1, 9, INK2, "middle", 600)
        svg.text(gx + 60, y0 + 27, l2 + f" · {fmt(base / 24, 1)} nap", 8.5, MUTED, "middle")
    svg.text(x0, 18, "órányi nyereség a célidőn, 4000 km-en", 9.5, INK2, "start", 600)
    for i, (ll, col) in enumerate(levers):
        svg.rect(x0 + i * 165, 230, 10, 10, col, rx=2); svg.text(x0 + i * 165 + 14, 239, ll, 8.5, INK2)
    return svg.write("08-idokoltsegvetes.svg")


def mozgashanyad():
    """Napfelosztás (óra): mozgás / alvás / egyéb. white-2016-ridefar-method (TCR mezőny 12,2 h), evans-2022 (18,4 h mozgás, 1,5–3 h alvás),
    mckenzie-dotwatcher-tcr-2026 (~78 %), halfwayanywhere-2024 (14,8 h, 62 %), giuliani-2023 (Hall <25 % állás), toone-2016 (74 %, 7 h alvás/70 h)."""
    rows = [  # felirat, mozgás, alvás, egyéb (óra/24)
        ("TCR teljes mezőny (2015)", 12.2, 5.0, 6.8, "levezetés: alvás/egyéb becslés"),
        ("TCR felső harmad (2022, 6. hely)", 18.4, 2.2, 3.4, ""),
        ("TCR élmezőny (2026, első 7 nap)", 18.7, 3.5, 1.8, "levezetés"),
        ("Tour Divide középmezőny (2024)", 14.8, 6.0, 3.2, "levezetés: alvás/egyéb becslés"),
        ("Tour Divide rekord (2016, Hall)", 18.2, 4.0, 1.8, "levezetés: <25 % állás"),
        ("1216 km PBP-tempóban (2016)", 17.7, 2.4, 3.9, "mért bontás"),
    ]
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1 = 232, 540
    def X(h): return scale(h, 0, 24, x0, x1)
    for h in (0, 6, 12, 18, 24):
        svg.line(X(h), 18, X(h), 200, HAIR if h else BASE, 1); svg.text(X(h), 214, f"{h} h", 8.5, MUTED, "middle")
    bh, gap = 22, 8
    for i, (lab, mv, sl, ot, note) in enumerate(rows):
        y = 22 + i * (bh + gap)
        svg.rect(X(0), y, X(mv) - X(0), bh, BLUE, rx=2)
        svg.rect(X(mv), y, X(mv + sl) - X(mv), bh, DEEP, rx=0, opacity=0.9)
        svg.rect(X(mv + sl), y, X(24) - X(mv + sl), bh, ORANGE, rx=2, opacity=0.8)
        svg.text(X(mv / 2), y + bh / 2 + 3.5, f"{fmt(mv / 24 * 100)} %", 9, "#fff", "middle", 600)
        svg.text(x0 - 8, y + bh / 2 + 3.5, lab, 9, INK2, "end")
    svg.text(x0, 236, "", 8)
    svg.rect(x0, 228, 10, 10, BLUE, rx=2); svg.text(x0 + 14, 237, "mozgás", 8.5, INK2)
    svg.rect(x0 + 70, 228, 10, 10, DEEP, rx=2); svg.text(x0 + 84, 237, "alvás", 8.5, INK2)
    svg.rect(x0 + 130, 228, 10, 10, ORANGE, rx=2); svg.text(x0 + 144, 237, "egyéb megállás (bolt, evés, töltés, egyéb)", 8.5, INK2)
    return svg.write("08-mozgashanyad.svg")


def alvas_km():
    """Modell: táv = (24 − alvás) × 0,8 × v (ridefar-time-efficiency). Jobb: hurdiel-2026-raf helyezés = −22,03 + 0,33 × alvásperc."""
    W, H = 560, 250
    svg = SVG(W, H)
    x0, x1, y0, y1 = 52, 320, 190, 30
    def X(s): return scale(s, 0, 8, x0, x1)
    def Y(d): return scale(d, 200, 500, y0, y1)
    for d in (200, 300, 400, 500):
        svg.line(x0, Y(d), x1, Y(d), HAIR, 1); svg.text(x0 - 5, Y(d) + 3.5, f"{d} km", 8.5, MUTED, "end")
    for s in (0, 2, 4, 6, 8):
        svg.line(X(s), y0, X(s), y0 + 4, BASE, 1); svg.text(X(s), y0 + 15, f"{s} h", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    for v, col in ((26, DEEP), (24, BLUE), (20, S["4"])):
        pts = [f"{X(s):.1f} {Y((24 - s) * 0.8 * v):.1f}" for s in (0, 8)]
        svg.path("M" + " L".join(pts), col, 2.2)
        svg.text(X(8) + 4, Y((24 - 8) * 0.8 * v) + 3, f"{v} km/h", 8.5, col, "start", 600)
    svg.rect(X(3), y1, X(4) - X(3), y0 - y1, BLUE, opacity=0.08)
    svg.text(X(3.5), y1 + 12, "3–4 h: 2020 utáni győztesek", 8, INK2, "middle", 600)
    svg.text(x0, 18, "napi táv az alvás függvényében (modell, 80 % mozgáshányad)", 9.5, INK2, "start", 600)
    svg.text((x0 + x1) / 2, y0 + 30, "alvás óra / 24 h", 9, INK2, "middle")
    svg.text(X(0.3), Y(232), "1 óra alvás ≈ 0,8 × sebesség km", 8.5, INK2, "start")
    # jobb: RAF
    rx0, rx1, ry0, ry1 = 380, 540, 190, 30
    def RX(m): return scale(m, 60, 320, rx0, rx1)
    def RY(r): return scale(r, 0, 90, ry1, ry0)
    for r in (0, 30, 60, 90):
        svg.line(rx0, RY(r), rx1, RY(r), HAIR, 1); svg.text(rx0 - 5, RY(r) + 3.5, f"{r}.", 8.5, MUTED, "end")
    for m in (100, 200, 300):
        svg.line(RX(m), ry0, RX(m), ry0 + 4, BASE, 1); svg.text(RX(m), ry0 + 15, f"{m}", 8.5, MUTED, "middle")
    svg.line(rx0, ry0, rx1, ry0, BASE, 1)
    import random
    rnd = random.Random(3)
    for _ in range(23):
        m = 95 + rnd.random() * 211
        r = -22.03 + 0.33 * m + rnd.gauss(0, 12)
        r = max(1, min(88, r))
        svg.circle(RX(m), RY(r), 3, ORANGE, opacity=0.7)
    svg.line(RX(80), RY(-22.03 + 0.33 * 80), RX(310), RY(-22.03 + 0.33 * 310), INK2, 1.6, dash="4 3")
    svg.text(rx0, 18, "mezőny: alvás és helyezés (RAF 2024)", 9.5, INK2, "start", 600)
    svg.text((rx0 + rx1) / 2, ry0 + 30, "alvás perc / nap · helyezés", 9, INK2, "middle")
    svg.text(rx0 + 4, ry1 + 14, "sematikus — nem tanács", 8, MUTED, "start")
    return svg.write("08-alvas-km.svg")


def sebesseg_fizika():
    """martin-1998-model; CdA tartományok frank-2021, grappe-1997, white-2016-ridefar-aero; Crr 0,005. Levezetés."""
    W, H = 560, 262
    svg = SVG(W, H)
    x0, x1, y0, y1 = 52, 330, 200, 30
    def X(p): return scale(p, 80, 260, x0, x1)
    def Y(v): return scale(v, 18, 40, y0, y1)
    for v in (20, 25, 30, 35, 40):
        svg.line(x0, Y(v), x1, Y(v), HAIR, 1); svg.text(x0 - 5, Y(v) + 3.5, f"{v} km/h", 8.5, MUTED, "end")
    for p in (100, 150, 200, 250):
        svg.line(X(p), y0, X(p), y0 + 4, BASE, 1); svg.text(X(p), y0 + 15, f"{p} W", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.line(X(150), y0, X(150), y1, ORANGE, 1, dash="3 3")
    for cda, col, lab in ((0.25, DEEP, "CdA 0,25 — aerobar, minimális csomag"), (0.35, BLUE, "CdA 0,35 — felsőfogás, jól pakolt táskák"), (0.40, S["4"], "CdA 0,40 — terhelt alapérték")):
        pts = [f"{X(p):.1f} {Y(speed(p, cda)):.1f}" for p in range(80, 261, 10)]
        svg.path("M" + " L".join(pts), col, 2.2)
        v150 = speed(150, cda)
        svg.circle(X(150), Y(v150), 3.5, col, "#fff", 1.2)
        if cda == 0.25: svg.text(X(150) - 7, Y(v150) - 3, f"{fmt(v150, 1)}", 8.5, col, "end", 600)
        elif cda == 0.35: svg.text(X(150) + 7, Y(v150) - 4, f"{fmt(v150, 1)}", 8.5, col, "start", 600)
        else: svg.text(X(150) + 7, Y(v150) + 11, f"{fmt(v150, 1)}", 8.5, col, "start", 600)
    svg.text(x0, 18, "síkon, 85 kg, Crr 0,005, szélcsend (Martin-modell)", 9.5, INK2, "start", 600)
    svg.text((x0 + x1) / 2, y0 + 30, "leadott teljesítmény", 9, INK2, "middle")
    # jobb: emelkedő 150 W, CdA 0,35
    rx = 380
    svg.text(rx + 80, 18, "150 W emelkedőn (CdA 0,35)", 9.5, INK2, "middle", 600)
    grades = [0, 2, 4, 6, 8, 10]
    def BY(v): return scale(v, 0, 32, 200, 50)
    for i, g in enumerate(grades):
        v = speed(150, 0.35, grade=g / 100)
        x = rx + i * 27
        svg.rect(x, BY(v), 20, 200 - BY(v), BLUE if g else DEEP, rx=2, opacity=0.9)
        svg.text(x + 10, BY(v) - 4, fmt(v, 1), 8, INK, "middle", 600)
        svg.text(x + 10, 213, f"{g} %", 8, INK2, "middle")
    svg.line(rx - 6, 200, rx + 165, 200, BASE, 1)
    svg.text(rx + 80, 228, "km/h · lejtés", 8.5, MUTED, "middle")
    legend = [(DEEP, "CdA 0,25 aerobar, minimális csomag"), (BLUE, "CdA 0,35 felsőfogás, jól pakolt táskák"), (S["4"], "CdA 0,40 terhelt alapérték")]
    for i, (col, lab) in enumerate(legend):
        svg.rect(x0 + i * 175, 246, 10, 10, col, rx=2); svg.text(x0 + i * 175 + 14, 255, lab, 8, INK2)
    return svg.write("08-sebesseg-fizika.svg")


def pulzus_napok():
    """Sematikus: wingo-2005 (+12 % 45 perc, hőség), schumacher-2011/fesseler-2026/neumayr-2004 (lefelé), brayson-2019 (U: 111 → 158)."""
    W, H = 560, 230
    svg = SVG(W, H)
    x0, x1, y0, y1 = 52, 540, 180, 30
    def X(d): return scale(d, 0, 14, x0, x1)
    def Y(p): return scale(p, 60, 130, y0, y1)
    for p in (70, 85, 100, 115, 130):
        svg.line(x0, Y(p), x1, Y(p), HAIR, 1); svg.text(x0 - 5, Y(p) + 3.5, f"{p} %", 8.5, MUTED, "end")
    for d in range(0, 15, 2):
        svg.line(X(d), y0, X(d), y0 + 4, BASE, 1); svg.text(X(d), y0 + 15, f"{d}. nap" if d else "rajt", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.line(x0, Y(100), x1, Y(100), BASE, 1, dash="3 3")
    # hőség-drift az első napon
    svg.path(f"M{X(0):.1f} {Y(100):.1f} L{X(0.6):.1f} {Y(112):.1f}", ORANGE, 2.4)
    svg.text(X(0.7), Y(114), "hőségben 45 perc alatt +12 % (valós)", 8.5, ORANGE, "start", 600)
    # többnapos lefelé
    pts = [(0.6, 100), (2, 92), (4, 84), (5, 80), (7, 78), (9, 77)]
    svg.path("M" + " L".join(f"{X(d):.1f} {Y(p):.1f}" for d, p in pts), BLUE, 2.4)
    svg.text(X(2.2), Y(67), "többnapos: azonos wattnál napról napra lejjebb (csal)", 8.5, BLUE, "start", 600)
    # U-alak vége
    pts2 = [(9, 77), (11, 84), (13, 100), (14, 112)]
    svg.path("M" + " L".join(f"{X(d):.1f} {Y(p):.1f}" for d, p in pts2), ST["critical"], 2.4, dash="5 3")
    svg.text(X(10.5), Y(104), "TCR vége: ismét felfelé (kimerülés)", 8.5, ST["critical"], "start", 600)
    svg.text(x0, 18, "pulzus azonos leadott teljesítménynél, a rajt %-ában — sematikus", 9.5, INK2, "start", 600)
    svg.text((x0 + x1) / 2, y0 + 30, "a verseny napja", 9, INK2, "middle")
    return svg.write("08-pulzus-napok.svg")


def homerseklet():
    """galloway-1997-temperature: 70 % VO2max kimerülésig, 4 pont (10,5 °C 93,5 min; 30,5 °C 51,6 min; 4 és 21 °C rövidebb — a pontos értékük a szövegben nem idézett)."""
    W, H = 560, 220
    svg = SVG(W, H)
    x0, x1, y0, y1 = 60, 540, 170, 30
    def X(t): return scale(t, 0, 35, x0, x1)
    def Y(m): return scale(m, 40, 100, y0, y1)
    for m in (50, 70, 90):
        svg.line(x0, Y(m), x1, Y(m), HAIR, 1); svg.text(x0 - 5, Y(m) + 3.5, f"{m} perc", 8.5, MUTED, "end")
    for t in (0, 5, 10, 15, 20, 25, 30, 35):
        svg.line(X(t), y0, X(t), y0 + 4, BASE, 1); svg.text(X(t), y0 + 15, f"{t} °C", 8.5, MUTED, "middle")
    svg.line(x0, y0, x1, y0, BASE, 1)
    svg.rect(X(10), y1, X(20) - X(10), y0 - y1, GREEN, opacity=0.08)
    svg.text(X(15), y0 - 8, "olcsó kilométer", 8.5, INK2, "middle", 600)
    svg.rect(X(30), y1, X(35) - X(30), y0 - y1, ST["critical"], opacity=0.08)
    svg.rect(X(0), y1, X(5) - X(0), y0 - y1, BLUE, opacity=0.08)
    # fordított U: sematikus, a két mért pont pontos
    pts = [(4.0, 80), (10.5, 93.5), (21.0, 80), (30.5, 51.6)]  # a 4 és 21 °C-os érték becsült
    path = []
    for i in range(0, 101):
        t = 2 + i / 100 * 30
        # sima interpoláció a pontokon át (Catmull-Rom helyett egyszerű parabola-illesztés két szakaszban)
        if t <= 10.5: m = 93.5 - (93.5 - 80) * ((10.5 - t) / 6.9) ** 2
        else: m = 93.5 - (93.5 - 51.6) * ((t - 10.5) / 20) ** 1.6
        path.append(f"{X(t):.1f} {Y(m):.1f}")
    svg.path("M" + " L".join(path), BLUE, 2.4)
    for t, m, lab in ((10.5, 93.5, "10,5 °C · 93,5 perc"), (30.5, 51.6, "30,5 °C · 51,6 perc")):
        svg.circle(X(t), Y(m), 4.5, BLUE, "#fff", 1.5)
        svg.text(X(t) + 8, Y(m) + (3 if t > 20 else -6), lab, 8.5, INK, "start", 600)
    for t in (4.0, 21.0):
        svg.circle(X(t), Y(80), 4, "#fff", BLUE, 1.5)  # becsült helyű pontok: üres jelölő
    svg.text(X(4.0) + 8, Y(80) + 12, "4 °C: rövidebb, mint 11 °C-on (érték becsült)", 8.5, INK2, "start")
    svg.text(x0, 18, "kimerülésig tartó tekerés a kimerülési teljesítmény 70 %-án (8 férfi) — a köztes pontok sematikusak", 9.5, INK2, "start", 600)
    svg.text((x0 + x1) / 2, y0 + 30, "levegő-hőmérséklet", 9, INK2, "middle")
    return svg.write("08-homerseklet.svg")


if __name__ == "__main__":
    for f in (intenzitas_tavolsag, lecsenges_24h, durability, idokoltsegvetes, mozgashanyad, alvas_km, sebesseg_fizika, pulzus_napok, homerseklet):
        print("wrote", f().name)
