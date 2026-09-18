// Mintaoldalak — Typst motor
// Fordítás: typst compile --root . --font-path design/fonts --input font=plex build/samples/samples.typ dist/samples/samples-typst-plex.pdf
#let font-choice = sys.inputs.at("font", default: "plex")
#let sans = if font-choice == "inter" { "Inter" } else { "IBM Plex Sans" }
#let display = if font-choice == "inter" { "Inter Display" } else { "IBM Plex Sans" }
#let mono = "IBM Plex Mono"

// ---- tokenek (design/tokens/tokens.json) ----
#let paper = rgb("#fcfcfb"); #let plane = rgb("#f4f4f1")
#let ink = rgb("#0b0b0b"); #let ink2 = rgb("#52514e"); #let muted = rgb("#898781")
#let hairline = rgb("#e1e0d9"); #let baseline = rgb("#c3c2b7")
#let brand = rgb("#184f95"); #let brand-deep = rgb("#0d366b"); #let accent = rgb("#eb6834")
#let ev-col = (A: rgb("#0d366b"), B: rgb("#256abf"), C: rgb("#5598e7"), D: rgb("#86b6ef"))
#let t-fix = brand; #let t-ex = muted; #let t-ind = accent
#let critical = rgb("#d03b3b"); #let warning = rgb("#fab219")

#set page(paper: "a4", margin: (top: 16mm, right: 16mm, bottom: 18mm, left: 28mm), fill: paper,
  footer: context [
    #line(length: 100%, stroke: 0.2mm + hairline)
    #v(-2mm)
    #set text(7.5pt, muted)
    #grid(columns: (1fr, auto, 1fr), align: (left, center, right),
      [04 · Alvás, fáradtság, kognitív teljesítmény], [Hosszú távon · minta v0.1],
      text(font: mono, ink2)[04 – #counter(page).display(n => if n < 10 { "0" + str(n) } else { str(n) })])
  ])
#set text(font: sans, size: 10.5pt, fill: ink, lang: "hu")
#set par(leading: 0.62em, justify: false)
#show heading.where(level: 1): it => block(below: 3mm)[#text(font: display, 24pt, weight: 700, fill: brand-deep, tracking: -0.01em)[#it.body]]
#show heading.where(level: 3): it => block(below: 1.5mm)[#text(10.5pt, weight: 600, fill: ink2, tracking: 0.06em)[#upper(it.body)]]

#let kicker(body) = text(8.5pt, weight: 500, fill: muted, tracking: 0.1em)[#upper(body)]
#let lede(body) = block(below: 4mm, width: 150mm)[#text(11.5pt, ink2)[#body]]
#let caption(body) = text(7.5pt, muted)[#body]
#let small(body) = text(8.5pt, ink2)[#body]
#let ev(g) = box(baseline: 20%, inset: (x: 0.8mm), rect(width: 4.2mm, height: 4.2mm, radius: 0.8mm, fill: ev-col.at(g),
  stroke: if g == "D" { (paint: brand, thickness: 0.3mm, dash: "dashed") } else { none },
  align(center + horizon, text(6.5pt, weight: 600, fill: if g == "D" { ink } else { white })[#g])))
#let tag(kind) = {
  let (col, label, dash) = if kind == "fix" { (t-fix, "fix", "solid") } else if kind == "ex" { (t-ex, "példa", "dashed") } else { (t-ind, "egyéni", "solid") }
  box(baseline: 25%, rect(radius: 6mm, inset: (x: 1.6mm, y: 0.6mm), stroke: (paint: col, thickness: 0.35mm, dash: dash))[
    #box(circle(radius: 1mm, fill: if kind == "ex" { none } else { col }, stroke: 0.35mm + col)) #h(0.8mm) #text(7.5pt, col)[#label]])
}
#let status(col, label) = box(baseline: 20%)[#box(rect(width: 3mm, height: 3mm, radius: 0.6mm, fill: col)) #h(1mm) #text(8.5pt, weight: 600)[#label]]
#let you(body) = block(width: 100%, fill: white, stroke: (left: 1.2mm + accent, rest: 0.2mm + hairline), radius: (right: 1.5mm), inset: (x: 4mm, y: 3.5mm))[
  #text(10.5pt, weight: 600, fill: accent, tracking: 0.06em)[MIT JELENT NEKED] #v(1.5mm) #text(9.5pt)[#body]]
#let boxed(body) = block(width: 100%, fill: plane, stroke: 0.2mm + hairline, radius: 1.5mm, inset: (x: 4mm, y: 3.5mm))[#body]
#let sample-tag(body) = place(top + right, dy: -10mm, rect(stroke: 0.4mm + accent, radius: 1mm, inset: (x: 1.6mm, y: 0.6mm), text(7pt, accent, tracking: 0.12em)[#upper(body)]))
#let sidebar(level) = place(top + left, dx: -12mm, dy: 0mm, stack(dir: ttb, spacing: 2.5mm,
  ..range(level).map(_ => line(length: 5mm, stroke: 0.7mm + brand)),
  line(length: 4mm, stroke: 0.2mm + baseline),
  text(7pt, ink2)[önell.], text(7pt, ink2)[kísérős], text(7pt, ink2)[24h]))

// ============ 1. FOGALOM-OLDAL ============
#sample-tag[Mintaoldal · tartalom illusztratív]
#sidebar(3)
#kicker[#text(brand)[04 · Alvás, fáradtság, kognitív teljesítmény] · Fogalom · Alap]
= Két erő dönti el, mikor alszol el a nyeregben: az alvásnyomás és a belső óra
#lede[A fáradtság nem egyenletesen nő. Az ébren töltött órákkal halmozódó alvásnyomás és a napszakhoz kötött cirkadián ritmus összege adja az álmosságot — és a kettő hajnali 3 és 5 között találkozik.]

#grid(columns: (4fr, 2fr), column-gutter: 4mm, row-gutter: 4mm,
  [
    #image("../../figures/svg/04-ket-folyamat-modell.svg", width: 100%)
    #v(1mm)
    #caption[1. ábra · A két-folyamat modell sémája 48 órán át egy átalvott és egy áttekert éjszakával. Sematikus rajz, nem mért görbe. Forrás: Borbély-modell #ev("A")]
    #line(length: 100%, stroke: 0.2mm + hairline)
  ],
  [
    === Hogyan működik
    *S – alvásnyomás.* Minden ébren töltött órával nő, alvással ürül. Ha áttekersz egy éjszakát, a második nap eleve magasabb szintről indulsz.

    *C – belső óra.* Napszakhoz kötött hullám, függetlenül attól, mennyit aludtál. Mélypontja hajnali 3–5 óra között; a testhőmérséklet, a reakcióidő és az éberség itt a legrosszabb. #ev("A")

    *Az összeg számít.* A második éjszakán a magas S és a C-mélypont összeadódik: ez a mikroalvások, a hallucinációk és a rossz döntések ablaka. #ev("B")
  ],
  grid.cell(colspan: 2, you[*Tervezd* a napi rövid alvást a C-mélypont köré (kb. 02:30–05:00), nem oda, ahol „épp elfáradsz”: ugyanaz a 90 perc itt a legtöbbet ér. *Mérd* a saját mélypontodat: két-három éjszakai edzésen jegyezd fel, mikor a legrosszabb — a görbe fázisa egyénenként ±2 órát eltolódhat. #tag("ind")])
)

#pagebreak()
// ============ 2. ADAT-OLDAL ============
#sample-tag[Mintaoldal · számok illusztratívak]
#sidebar(2)
#kicker[#text(brand)[04 · Alvás, fáradtság, kognitív teljesítmény] · Adat · Haladó]
= Az éberség nem lassan kopik, hanem lépcsőben omlik: a figyelemkiesések az ébren töltött 18. óra után szaporodnak

#image("../../figures/svg/04-figyelemkiesesek.svg", width: 100%)
#caption[2. ábra · Figyelemkiesések (≥ 500 ms reakcióidő) száma egy 10 perces éberségi teszten az ébren töltött idő függvényében. *Illusztratív görbe a formátum bemutatására* — a kutatási fázisban a forrás mért adatsora kerül ide. Tervezett forrás: Dawson & Reid 1997, Nature #ev("B")]
#line(length: 100%, stroke: 0.2mm + hairline)
#v(2mm)
#grid(columns: (1fr, 1fr), column-gutter: 4mm,
  [
    #text(font: display, 56pt, weight: 700, fill: brand-deep, tracking: -0.02em)[17–19]#h(1mm)#text(12pt, weight: 500, fill: ink2)[óra ébren]
    #v(1mm)
    #small[ennyi után a reakcióidő és a figyelem romlása a 0,5 ‰-es véralkoholszinttel mérhető össze — a legtöbb országban ez a vezetési határ. #ev("B")]
    #v(1mm)
    #caption[Ez a szám gyakran idézett és a mintában tájékoztató jellegű; a végleges modulban a konkrét tanulmány és a konfidencia-tartomány szerepel.]
  ],
  you[*Kerüld*, hogy a 18. ébren töltött óra forgalmas útra vagy hosszú lejtőre essen; a rajtidő ismeretében ez előre kiszámolható. *Állítsd* be az első tervezett alvást legkésőbb 20–22 óra ébrenlét után #tag("ex") — hogy neked hol a küszöb, azt a 16. modul alvásmegvonásos próbatekerése mutatja meg. #tag("ind")]
)
#v(4mm)
=== Három szám, amit a végleges oldal a forrásból hoz #tag("ex")
#let stat(n, body) = boxed[#text(font: display, 30pt, weight: 700, fill: brand-deep, tracking: -0.02em)[#n] #v(1mm) #small[#body]]
#grid(columns: (1fr, 1fr, 1fr), column-gutter: 4mm,
  stat[≈ 2×][ennyivel több figyelemkiesés a 2. áttekert éjszaka hajnalán az elsőhöz képest #ev("B")],
  stat[20 perc][rövid alvás után mérhetően javul az éberség; a hatás 2–3 órán át tart #ev("A")],
  stat[03–05 h][a cirkadián mélypont — itt a legnagyobb a mikroalvás kockázata, alvástól függetlenül #ev("A")])

#pagebreak()
// ============ 3. PROTOKOLL-OLDAL ============
#sample-tag[Mintaoldal · protokoll illusztratív]
#sidebar(3)
#kicker[#text(brand)[04 · Alvás, fáradtság, kognitív teljesítmény] · Protokoll · Alap → Elit]
= Út menti szunyókálás: hat lépés, hogy 20 perc alvásból 3 óra tiszta fej legyen
#lede[A rövid alvás akkor hoz a legtöbbet, ha a jelekre indul, nem a kimerülésre, és ha az ébredés utáni tehetetlenséget is betervezed. A jelölések mutatják, mi általános szabály, mi példaérték és mi az, amit magadon kell bemérned.]

#let step(n, what, how, tags) = {
  line(length: 100%, stroke: 0.2mm + hairline)
  v(-1mm)
  grid(columns: (9mm, 1fr, 30mm), column-gutter: 3mm, inset: (y: 1.2mm),
    text(font: mono, 13pt, weight: 600, fill: brand)[#n],
    [#text(weight: 600)[#what] \ #text(9pt, ink2)[#how]],
    stack(dir: ttb, spacing: 1.2mm, ..tags))
}
#step("01", [Állj meg a második jelre], [Az első mikroalvás-jel (fejbiccentés, kihagyott kanyar, „hogy kerültem ide?”) után a következő biztonságos helyen megállsz — nem a harmadikra. Mikroalvás = azonnali stop.], (tag("fix"), status(critical, "biztonsági")))
#step("02", [Koffein a lefekvés előtt, nem utána], [100–200 mg (egy erős kávé vagy gél) közvetlenül alvás előtt: mire felébredsz, hatni kezd. Érzékeny gyomornál vagy este 22 után hagyd ki, ha a főalvást is tervezed.], (tag("ex"), ev("C")))
#step("03", [Időzítő 15–25 percre], [A rövid alvás nem éri el a mélyalvást, ezért könnyebb belőle felébredni. 30 perc fölött nő az alvási tehetetlenség kockázata. A saját optimumod a próbatekeréseken derül ki.], (tag("ind"), ev("A")))
#step("04", [Fekvő helyzet, meleg, sötét], [Buszmegálló, templomelőtér, benzinkút mosdója. Sapka, minden réteg fel, biciklit magadhoz kötve. Fény és hideg ellen szemmaszk és mentőfólia.], (tag("fix"), ev("C")))
#step("05", [Ébredés után 5 perc gyaloglás], [Ne ülj azonnal nyeregbe: az alvási tehetetlenség 5–15 percig rontja a reakcióidőt. Egyél, igyál, nézd meg az útvonalat — csak utána indulj.], (tag("fix"), ev("B")))
#step("06", [Két szunyókálás után főalvás], [Ha ugyanazon az éjszakán másodszor is kell, a harmadik jelnél már 90 perces alvás jön (egy teljes ciklus) — a rövid alvás nem pótolja a hiányt, csak áthidal.], (tag("ex"), status(warning, "figyelem")))
#v(1mm)
#grid(columns: (1fr, 1fr), column-gutter: 4mm,
  [
    === Döntési fa
    #set text(8.5pt)
    #table(columns: (1fr, 1.4fr), stroke: (x, y) => (bottom: (if y == 0 { 0.4mm + baseline } else { 0.2mm + hairline })), inset: 1.4mm,
      table.header([#text(weight: 600, ink2)[Jel]], [#text(weight: 600, ink2)[Teendő]]),
      [Ásítás, nehéz szemhéj], [Koffein, hideg víz, 10 perc állva — még nincs stop],
      [Kihagyott kanyar, „hol vagyok?”], [Következő biztonságos hely: 20 perc #tag("fix")],
      [Fejbiccentés, hallucináció], [#status(critical, "Azonnali stop"), 20–90 perc])
  ],
  you[*Mérd* be a 16. modul protokolljával, hogy 15, 20 vagy 25 perc után vagy-e a legtisztább — ezt a számot viszed a versenytervbe. *Írd* a Garminra emlékeztetőnek a jeleket: a fáradt agy nem ismeri fel őket magától.])
#v(1.5mm)
#line(length: 100%, stroke: 0.2mm + hairline)
#text(9pt, ink2)[*Ékezet- és számpróba:* Öt hűtőházból kértünk színhúst — árvíztűrő tükörfúrógép. #text(font: mono)[1 234,5 km · 03:47 · 2 340 m · 145 W · 6,8 W/kg] · #text(number-type: "lining")[0123456789] · ŐŰ őű ÁÉÍÓÖÚÜ áéíóöúü]
