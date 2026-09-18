# 08. modul – Pacing és versenystratégia – C csomag: bizonyíték-térkép (Q3, Q4, Q6)

Készült: 2026-09-18/19. Új forrásdefiníciók: `data/raw/08-C-sources.yaml` (27 tétel: 2 A, 15 B, 10 C; 5 DOI Crossrefen ellenőrizve). Meglévő, itt csak hivatkozott kulcsok: `ridefar-time-efficiency`, `raceacrossseries-sleeprule`, `hurdiel-2026-raf`, `bikepacking-ultraguide-2019`, `brayson-2019-tcr` (08-A), `hyldahl-2024-tourdivide` (08-A), `mckenzie-dotwatcher-tcr-2026`, `halfwayanywhere-tourdivide-2024`, `cyclecharts-pbp-2023`, `storbeck-2019-pbp-speeds`, `homer-bikepacking-tourdivide-2026` (08-B).
Fokozat: A = meta-analízis/RCT/validált fizikai modell; B = terepvizsgálat, tracking-elemzés, mért CdA/Crr; C = narratív, edzői/versenyzői, közösségi kalkulátor; D = feltörekvő. A "derived" jelölésű számok saját számítások a forrás adataiból vagy a Martin-modellből (`scratchpad/model.py`, `budget.py`), nem idézetek.

---

## Q3 — Mozgó és álló idő: mozgáshányad, az álló idő összetevői, élmezőny vs középmezőny

### Számszerű állítások

1. **A TCR teljes mezőnyének mozgáshányada a 24 órára vetítve ~50%: a 2015-ös TCR-en a versenyzők átlagosan 12 óra 10 percet tekertek naponta, ezért a Ridefar-modell a tekerési időt egyszerűen megduplázza célidővé.** Ugyanezt adja ki n=1-en Brayson TCR5-esete: 3978,7 km / 23,1 km/h = 172 h tekerés 14 nap (336 h) alatt → 51% (derived). [white-2016-ridefar-method C; brayson-2019-tcr B]

2. **Az élmezőny mozgáshányada 70–78%, a napi mozgásidő 17–18,5 óra: Bartholmoes (TCRNo8, 6. hely) 183,7 h mozgás / 241,85 h eltelt = 76%, ~60 h álló idő 10 nap alatt; Long (TCRNo11) 21 km/h × 316,9 h → 70%, 17,0 h/nap mozgás; Gemperle (TCRNo12) 7 nap alatt 3422,9 km 25,97 km/h-val → ~78% (derived).** A nyitó 24 órában az élmezőny gyakorlatilag nem áll meg: a top 10 5–31 perc tracker-rögzített álló időt mutatott, 646–665 km-rel. [evans-2022-bikeradar-bartholmoes B; long-2025-tcr11 B; mckenzie-dotwatcher-tcr12-briefing-2026 B; mckenzie-dotwatcher-tcr-2026 C]

3. **Az álló idő NAGYOBBIK fele nem alvás.** Bartholmoes: ~60 h álló időből 1,5–3 h/éj alvás = 15–30 h, tehát 30–45 h (3–4,5 h/nap) bolt, evés, egyéb (derived). Toone 1216 km-es randonneur-adatsora: 18,6 h álló idő = 7 h alvás + 9,15 h nem-alvás, 31 megállás átlag 36 perc. Morton (Tour Divide-útvonal): ~30% álló idő, ebből 6 h/éj alvás ≈ 25%, egyéb ~5% (derived). [evans-2022-bikeradar-bartholmoes B; toone-2016-pbp-southern B; giuliani-2023-morton-tourdivide B]

4. **Tour Divide: a rekorderek 25% alatt állnak, a középmezőny ~38%-ot.** Hall (2016) és Bartholmoes (2023) tracker szerint <25% álló idő; Morton (2023, önkéntes 12 h/48 h pihenőszabállyal) ~30%; egy 19 nap 17 órás középmezőnyös befutó 14 h 49 min tekerés / 24 h = 62% mozgás, 15 km/h mozgósebesség. [giuliani-2023-morton-tourdivide B; halfwayanywhere-tourdivide-2024 C; hyldahl-2024-tourdivide B (16,8 h/nap tekerés)]

5. **A sebesség és a mozgáshányad szétválasztható, és az élen gyakran a mozgásidő dönt, nem a sebesség.** TCRNo12: Chatelet 26,21 vs Gemperle 25,97 km/h, de Gemperle ~2 órával többet mozgott 7 nap alatt és vezetett. Tour Divide 2024: Leveika "hasonló mozgótempóval, következetesen kevesebb alvással" nyert. FORDÍTOTT példák (több pihenő, de gyorsabb mozgás nyer): Morton ~5 ponttal többet állt Hallnál, mégis ~34 órával gyorsabb (derived: 20,5 vs ≤17,1 km/h mozgósebesség); SRMR 2019: Sliacan >52 h pihenővel (≈30%) nyert Wilcox 30 h-ja (≈16%) ellen, mert >13,8 vs ~11,1 km/h-val mozgott (derived). [mckenzie-dotwatcher-tcr-2026 C; horanyi-2024-leveika-tourdivide C; giuliani-2023-morton-tourdivide B; adn-2019-srmr C]

6. **Élmezőny vs középmezőny TCR-en számokban: 480–494 km/nap (Strasser 2022, Gemperle 2026) vs 252–267 km/nap medián (2013–2016); top 25% ≥300, top 5% >350 km/nap.** Mozgósebesség: 26–28,75 km/h (élmezőny, tracker) vs 21–23,5 km/h (felső harmad) vs ~23 km/h (Brayson, középmezőny 2017, alacsonyabb mozgáshányaddal). A középmezőnyben tehát a mozgáshányad (50–60%) a nagyobb különbség, a sebesség csak 3–5 km/h. [white-2017-tcr-results B; evans-2022-bikeradar-bartholmoes B; mckenzie-dotwatcher-tcr12-briefing-2026 B; brayson-2019-tcr B]

7. **Randonneur-tempó (PBP 90 h): a 1200 km-es mérés 73,7% mozgáshányadot, 23,3 km/h mozgó- és 17,2 km/h eltelt-átlagot adott; PBP-n 2–3 óra alvás/éj a tipikus stratégia, 83 h 50 min célidővel.** A 90 órás limit 13,33 km/h eltelt-átlagot követel. [toone-2016-pbp-southern B; storbeck-2019-pbp-speeds C; cyclecharts-pbp-2023 C; rusa-acp-control-times C]

8. **Szervezői mutató: a Race Across Series "Wakefulness Made Good" fogalma szerint hosszú formátumokon a versenyidő 8–20%-a jut alvásra; a Race Across France mért alvása 228 ± 107 perc/24 h (≈16%).** Ez az alvás-hányad, nem a teljes álló idő – az álló idő ennek 1,5–2-szerese (3. pont). [raceacrossseries-sleeprule C; hurdiel-2026-raf B]

9. **Gyakorlati célérték: 80% mozgáshányad az ébren töltött időre (12 óra a 15-ből, 3 óra megállás), 75–85% a tipikus tartomány, <70% "túrázás"; a gyorsabbak 16–18 órás mozgásidő-stratégiát terveznek 4–6 óra alvással.** [ridefar-time-efficiency C; bikepacking-ultraguide-2019 C]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q3)
- Nincs lektorált, tracker-alapú elemzés az önellátó versenyek álló idejének összetevőiről (bolt/evés/mechanika/navigáció/CP/fotó); minden bontás n=1 versenyzői adat vagy sajtó. Navigációs hiba, mechanika, ellenőrzőpont és social media időköltségére számszerű forrás NINCS (Ridefar csak "sok időt lehet veszíteni").
- A "moving time" fogalma forrásonként más: a Strava a lassú mozgást/rövid megállást is mozgásnak veszi, a tracker a pont-időközökből becsül – a mozgáshányadok ±3–5 pontos hibával hasonlíthatók.
- Transibérica- és Race Across France-tracking-elemzést mozgáshányaddal nem találtam (csak alvási szabályt és alvásmérést).
- A TCR-medián (252–267 km/nap) 2016-os adat; a 2020-as évek mezőnyére frissített medián nincs publikálva.

### ELLENTMONDÁS (Q3)
- "Az élen a mozgásidő dönt" (Gemperle/Leveika) vs "a mozgósebesség dönt" (Morton, Sliacan): mindkettő igaz, más feltétel mellett – ha a mozgósebesség-különbség >10%, az többet ér, mint 5–10 pont mozgáshányad; ha a sebességek 1%-on belül vannak (TCR-él), az egy-két órányi plusz mozgás dönt. A modulban explicit "melyik a szűk keresztmetszet" kérdésként kezelendő.
- A sajtó "moving pace" adata Leveikánál (8,6 mph) valójában eltelt-átlag (2700 mi / 314,3 h = 8,59 mph, derived) – a mozgósebesség ~18–19 km/h lehetett. [horanyi-2024-leveika-tourdivide C]

---

## Q4 — Időköltségvetés-modell: érkezési idő = táv / (mozgósebesség × napi mozgásidő)

### Számszerű állítások

1. **Alapképlet: napok = D / (v_mozgó × h_mozgás), ahol h_mozgás = 24 − alvás − egyéb álló idő; a Ridefar-példa 15 ébren töltött óra × 85% × 24 km/h = 306 km/nap, 75%-nál 270 km/nap (−36 km/nap, 4000 km-en >1,5 nap).** [ridefar-time-efficiency C]

2. **A képlet szorzatos, ezért a relatív érzékenység: ΔT/T ≈ −Δv/v − Δh/h. Egy óra plusz mozgásidő pontosan v/h km/h sebességnövelésnek felel meg (derived).** TCR-középmezőny (22 km/h, 12,5 h): 1 h = 1,76 km/h; TCR-él (26 km/h, 19 h): 1 h = 1,37 km/h; Tour Divide-középmezőny (15 km/h, 14,8 h): 1 h = 1,01 km/h; PBP (22 km/h, 16,5 h): 1 h = 1,33 km/h. [derived a budget.py-ból; alapszámok: white-2016-ridefar-method C, evans-2022-bikeradar-bartholmoes B, halfwayanywhere-tourdivide-2024 C]

3. **Érzékenységvizsgálat 4000 km-es TCR-középmezőnyre (22 km/h, 12,5 h/nap = 275 km/nap, 14,55 nap): +1 km/h → −15,2 h; +1 h mozgás (= −1 h alvás vagy −1 h egyéb állás) → −25,9 h; −30 min álló idő → −13,4 h; mindkettő → −39,9 h (derived).** Az élmezőnyben (26 km/h, 19 h, 8,1 nap): +1 km/h −7,2 h, +1 h −9,7 h, −30 min −5,0 h. Tour Divide-középmezőnyben (15 km/h, 14,8 h, 19,4 nap): +1 km/h −29,1 h ≈ +1 h −29,4 h – itt a kettő egyenértékű. [derived; brayson-2019-tcr B; hyldahl-2024-tourdivide B]

4. **+1 km/h síkon 150 W-ról ~163 W-ot (+9%) kíván (CdA 0,35, 85 kg, derived), míg +1 óra mozgás "csak" logisztika – ezért középmezőnyben az álló idő csökkentése a legolcsóbb gyorsulás; az élen viszont a mozgásidő már 19–23 h/nap, ott csak a sebesség (és az alvás minősége) marad.** [derived Martin-modellből: martin-1998-model A; white-2016-ridefar-method C]

5. **A Ridefar teljes-útvonal modellje szerint +40 W (+28%, 130 → 165 W) csak +3 km/h-t (+14%) ad – a sebesség a teljesítmény ~köbgyökével nő, tehát a teljesítmény-oldali érzékenység alacsony.** [white-2016-ridefar-method C; crouch-2017-aero-review A]

6. **Brevet-időlimit (ACP): zárás 15 km/h-val 600 km-ig (200 km 13 h 30, 600 km 40 h), 11,428 km/h-val 600–1000 km (1000 km 75 h), 13,333 km/h-val 1000–1300 km (1200 km 90 h); nyitás 34/32/30/28/26 km/h-val sávonként; első 60 km zárása 20 km/h + 1 h.** A modul kalkulátora ebből számol "utolsó pillanat" görbét. [rusa-acp-control-times C]

7. **Tervezőszámok TCR-re: medián 252–267 km/nap, top 25% ≥300, top 5% >350 km/nap (2013–2016); élmezőny 2022–2026: 480–494 km/nap.** Tour Divide: rekord 13 nap 2 h (333 km/nap), középmezőny ~221 km/nap 19,7 nap alatt; napi 438 km-es csúcsnap az élen. [white-2017-tcr-results B; evans-2022-bikeradar-bartholmoes B; horanyi-2024-leveika-tourdivide C; halfwayanywhere-tourdivide-2024 C; homer-bikepacking-tourdivide-2026 C]

8. **A kereskedelmi/közösségi becslők (komoot, RWGPS, Best Bike Split) MOZGÁSIDŐT adnak, nem célidőt: a komoot "only calculates your time moving"; a BBS 2–3%-os pontossága időfutamra, pontos teljesítmény- és időjárás-bemenet mellett érvényes.** Ultrán a célidő-hiba főleg az álló időből és a teljesítmény többnapos eséséből jön, nem a fizikából. [komoot-fitness-hub C; bestbikesplit-tt-accuracy C]

### KALKULÁTOR-PARAMÉTEREK (Q4)
- **Képlet:** `T_nap = D / (v_mozgó × h_mozgás)`; `h_mozgás = 24 − t_alvás − t_egyéb`; `T_óra = 24 × T_nap`. Mozgáshányad `f = h_mozgás / 24`.
- **Érzékenység:** `∂T/∂v = −T/v`, `∂T/∂h = −T/h`; egyenérték: `1 h mozgás ≡ (v/h) km/h`.
- **Alapértékek (preset):**
  - TCR középmezőny: v 21–23 km/h, h 12–13 h (f 0,50–0,55), alvás 4–5 h, egyéb 6–7 h → 260–300 km/nap [white-2016-ridefar-method C; brayson-2019-tcr B; white-2017-tcr-results B]
  - TCR felső harmad: v 21–23,5, h 17–18,5 (f 0,70–0,76), alvás 1,5–3 h, egyéb 3–4,5 h → 360–425 km/nap [evans-2022-bikeradar-bartholmoes B; long-2025-tcr11 B]
  - TCR élmezőny (7 nap): v 26–26,2, h ~19 (f ~0,78) → 480–490 km/nap; első 24 h: f ≈ 0,98–1,0 [mckenzie-dotwatcher-tcr-2026 C; mckenzie-dotwatcher-tcr12-briefing-2026 B]
  - Tour Divide középmezőny: v ~15, h ~14,8 (f 0,62) → ~221 km/nap; élmezőny: f ≥0,75, v ~17–18 (derived) → 310–335 km/nap [halfwayanywhere-tourdivide-2024 C; giuliani-2023-morton-tourdivide B; hyldahl-2024-tourdivide B]
  - PBP/1200 km brevet: v 22–23, f ~0,74, alvás 2–3 h/éj → 80–84 h; limit 90 h = 13,33 km/h eltelt-átlag [toone-2016-pbp-southern B; rusa-acp-control-times C]
- **Alvás-hányad szervezői referencia:** versenyidő 8–20%-a (WMG) [raceacrossseries-sleeprule C]; mért: 228 ± 107 perc/24 h [hurdiel-2026-raf B].
- **Brevet-kontrollidő:** zárás-sebességek 15 / 15 / 15 / 11,428 / 13,333 km/h a 0–200 / 200–400 / 400–600 / 600–1000 / 1000–1300 km sávokra; nyitás 34 / 32 / 30 / 28 / 26 km/h; sávonként összegezve [rusa-acp-control-times C].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q4)
- Publikált, validált "időköltségvetés-kalkulátor" ultrára NINCS: a Ridefar time-efficiency modell és a Tour Divide "miles per day" tervezés közösségi ökölszabály; a Ridefar TCR-modellje a legközelebbi (célidő = 2 × tekerési idő), de a 2015-ös mezőnyre kalibrált.
- A napi mozgósebesség többnapos esése (durability, 08-A) nincs beépítve egyetlen közösségi kalkulátorba sem; Brayson és Bartholmoes adatai napi bontásban nem hozzáférhetők.
- Tour Divide "miles per day" tervezőket (spreadsheet/planner) konkrét képlettel nem találtam; a versenyzői recapok (Long 2024) csak napi távokat adnak.

### ELLENTMONDÁS (Q4)
- "A sebesség a fő kar" (fizikai kalkulátorok, Ridefar Bike-sorozat: köpeny 7 h, aero 5 h, tömeg 40 perc/kg) vs "a mozgásidő a fő kar" (time-efficiency, tracking): a Ridefar saját számai szerint a legjobb felszerelés-optimalizálás összesen ~15–20 óra a 2016-os TCR-en, míg napi +1 óra mozgás ~26 óra a középmezőnyben – a két Ridefar-sorozat egymás mellett olvasva egyértelművé teszi, hogy a középmezőny szűk keresztmetszete a logisztika. [white-2016-ridefar-method C; white-2016-ridefar-resistance C; ridefar-time-efficiency C]

---

## Q6 — A sebesség fizikája terhelt ultrakerékpáron

### Számszerű állítások

1. **A Martin-modell (P = [½ρ·CdA·v_lég²·v + Crr·m·g·cosθ·v + m·g·sinθ·v + csapágy + gyorsítás] / η) terepen R² = 0,97-tel, 2,7 W standard hibával validált; η ≈ 0,977; szélcsatorna-CdA 0,255–0,269 m² (0–15° yaw), Crr = 0,0032 (magas nyomású köpeny).** [martin-1998-model A]

2. **Síkon a légellenállás az ellenállás >90%-a versenysebességnél, a teljesítmény 56–96%-a lejtéstől függően; terhelt, lassabb (15–25 km/h) bringán ez 60–80%-ra esik, a gördülés 10–35%-ra nő (MTB-terepen 8–35% aero).** [crouch-2017-aero-review A; bertucci-2013-mtb-field B; white-2016-ridefar-resistance C]

3. **CdA pozíció szerint (versenyző, táska nélkül): felsőfogás 0,299 → alsófogás 0,276 (−7,8%) → aerobar 0,262 (−12,4%) → Obree 0,216 (−27,8%) m²; szélcsatorna-átlagok: tops/hoods → drops −15–20%, TT-pozíció −30–35%.** [grappe-1997-obree B; crouch-2017-aero-review A]

4. **Terhelt bikepacking-bringa mért CdA-ja (hoods, Chung-módszer): csupasz bringa 0,329, jól pakolt (AeroPack + aero kormánytáska) 0,315, 14 l nyeregtáska 0,334, kormányhenger + hátsó 0,346 m²; a leggyorsabb–leglassabb különbség 7,5 perc 180 km-en 200 W-nál.** MTB-s ülő pozícióban 0,357 ± 0,023 m². A Ridefar terhelt-bikepacker alapértéke 0,40 m², Groeskamp "amatőr" alapértéke szintén 0,4. [frank-2021-tailfin-aero B; bertucci-2013-mtb-field B; white-2016-ridefar-aero C; groeskamp-2017-incline-wind C]

5. **Aerobar nyeresége: szélcsatornában 31,3 W 35 km/h-n hoods-hoz képest (derived ΔCdA ≈ 0,057 m²); a Ridefar konzervatív becslése −0,03 m² drops-hoz képest (+0,7 km/h 150 W-on), nettó csak ~40 perc a 3900 km-es TCR-en a plusz súly és a részleges használat miatt; tops → aerobar összesen +1,7 km/h.** Táskatartós rendszer vs bikepacking-táska: −6,5% (egy pár), −7,9% (két pár) sebesség 200 W-on. [branston-2023-windtunnel B; white-2016-ridefar-aero C; denham-2016-panniers-velodrome B]

6. **Gördülési ellenállás: jó országúti köpeny dobon Crr ≈ 0,003–0,0035, gravel-köpenyek 35–45 mm alacsony nyomáson 11,4–18 W/kerék 28,8 km/h-n (derived Crr 0,0034–0,0054 a dobon); a valós út a dobérték ~kétszerese 85 kg-ra (két kerék); felület: aszfalt < fű ≈ murva << homok (4,5–15×); MTB-terepen a Crr 2–3× az országútié (másodlagos).** Nyomás: 60 vs 100 psi +20–40% Crr; "4 évszakos" köpeny +40% Crr = −0,6 km/h, +5 h a TCR-en. [brr-test-method B; steyn-2014-mtb-surfaces B; bertucci-2013-mtb-field B; white-2016-ridefar-resistance C]

7. **Tömeg: 1 kg ≈ 30–40 perc tekerési idő a 3900 km / 55 000 m-es TCR-en (0,08 km/h/kg), laposabb úton 0,06 km/h/kg; −5 kg → +1,9% sebesség.** Derived (Martin-modell, 150 W, CdA 0,35): 6%-os emelkedőn 75 / 85 / 95 kg → 10,6 / 9,5 / 8,5 km/h; 100 m szint nettó (fel + le vs sík) +3,4 / +4,9 / +6,2 perc 3 / 5 / 8%-os lejtésnél 85 kg-mal – ez a "climbing per km" ökölszabály fizikai alapja (~5 perc / 100 m / 150 W). [white-2016-ridefar-resistance C; martin-1998-model A (derived)]

8. **Szél: a Ridefar-modell 0–20 km/h egyenletes eloszlású (átlag 10 km/h) szelet feltételez; szélcsend +0,5 km/h, 15 km/h átlagszél −0,9 km/h és +8,5 h a TCR-en.** Derived: 150 W, CdA 0,35: 10 km/h szembeszél 29,2 → 23,5 km/h; 10 km/h hátszél → 34,9 km/h. Oldalszélben a hatásos CdA nő (oldal/front arány μ ≈ 1,2; λ = cos²β + μ·sin²β), és a drag a négyzetes légsebesség tengelyirányú komponensével arányos. Emelkedő ↔ szembeszél átváltás: Mont Ventoux (7,3%) ≈ 56 km/h szembeszél. [white-2016-ridefar-resistance C; isvan-2015-wind-yaw B; groeskamp-2017-incline-wind C]

9. **Hőmérséklet és magasság: a légsűrűség −0,8%/100 m, a leadható teljesítmény −0,6%/100 m (1000 m: −5%, Furka-hágó: −16%); 5 °C-kal hidegebb levegő −0,2 km/h. Órarekordhoz az optimum 2000 m (nem akklimatizált) – 2500 m (akklimatizált).** Derived ISA-táblázat: ρ = 1,225 (0 m, 15 °C), 1,112 (1000 m), 1,007 (2000 m); +10 °C ≈ −3,5%; 150 W síkon 1,225 → 1,007 kg/m³: 29,1 → 30,8 km/h. Emelkedőn a sűrűség-előny eltűnik, a teljesítményvesztés marad. [white-2016-ridefar-resistance C; bassett-1999-hour-records B]

10. **Lejtőn a sebességet a CdA és a tömeg aránya szabja meg (derived: 150 W, 85 kg, −5%: ~55 km/h; −8%: ~68 km/h), a valós ultra-lejtősebesség ennek 60–80%-a fékezés/kanyar/éjszaka miatt – erre nincs mért forrás.** Az útvonal-becslők (komoot, RWGPS) mozgásidőt becsülnek; a BBS 2–3%-os pontossága TT-re érvényes. [komoot-fitness-hub C; bestbikesplit-tt-accuracy C]

### KALKULÁTOR-PARAMÉTEREK (Q6)
- **Egyenlet (Martin 1998 / Gribble):** `P = (1/η) · [ ½·ρ·CdA·(v + v_szél)²·v + Crr·m·g·cos(atan G)·v + m·g·sin(atan G)·v ]`; sebesség teljesítményből: harmadfokú egyenlet (Cardano) vagy felezés. `η = 0,976–0,98` (2–2,4% hajtásláncveszteség) [martin-1998-model A; gribble-power-speed C; groeskamp-2017-incline-wind C].
- **CdA (m²), rendszer = versenyző + terhelt bringa:**
  - 0,25–0,27: aerobar, kompakt versenyző, minimális táska (Martin-szélcsatorna 0,255–0,269; Grappe AP 0,262) [martin-1998-model A; grappe-1997-obree B]
  - 0,28–0,30: alsófogás / aerobar közepes táskázással (Grappe DP 0,276; Frank legjobb táskás 0,315 hoods-ban − aerobar 0,03–0,05) [grappe-1997-obree B; frank-2021-tailfin-aero B; white-2016-ridefar-aero C]
  - 0,31–0,35: hoods, jól pakolt bikepacking-táskák (Frank 0,315–0,346) [frank-2021-tailfin-aero B]
  - 0,36–0,40: felsőfogás, kormányhenger, bő ruha, MTB-pozíció (Bertucci 0,357; Ridefar alap 0,40) [bertucci-2013-mtb-field B; white-2016-ridefar-aero C]
  - 0,42–0,48: táskatartós rendszer (−6,5–7,9% sebesség ≈ +0,07–0,10 m² a Ridefar becslése szerint) [denham-2016-panniers-velodrome B; white-2016-ridefar-aero C]
  - Lépések: tops → hoods −0,03; hoods → drops −0,02; drops → aerobar −0,03 (Ridefar) … −0,057 (BikeRadar hoods → clip-on); feszes ruha −0,02; kormányhenger +0,02–0,03.
- **Crr:**
  - 0,003–0,0035: sima aszfalt/pálya, prémium köpeny, 6–8 bar (Martin 0,0032) [martin-1998-model A; brr-test-method B]
  - 0,004–0,0055: jó/átlagos aszfalt, 28–35 mm, valós felület (dob × ~1,3–1,6) [brr-test-method B; white-2016-ridefar-resistance C]
  - 0,006–0,008: érdes/nedves aszfalt, "4 évszakos"/defektvédett köpeny (+40%), alacsony nyomás (+20–40%) [white-2016-ridefar-resistance C]
  - 0,008–0,015: tömör murva, földút (út × 2–3, Bertucci másodlagos; fű ≈ murva, Steyn) [bertucci-2013-mtb-field B; steyn-2014-mtb-surfaces B]
  - 0,015–0,03+: laza murva, homok, mosott Tour Divide-szakasz – NINCS mért kerékpáros forrás; homok = aszfalt × 4,5–15 [steyn-2014-mtb-surfaces B]
- **Légsűrűség:** `ρ = p/(287,05·T_K)`, `p = 101325·(1 − 2,25577·10⁻⁵·h)^5,25588` (ISA); gyakorlati: −0,8%/100 m, −0,35%/°C [gribble-power-speed C; white-2016-ridefar-resistance C]. Teljesítménykorrekció magasságra: −0,6%/100 m (nem akklimatizált) [white-2016-ridefar-resistance C; bassett-1999-hour-records B].
- **Szél:** fejszél-komponens a (v + v_szél)² tagban; oldalszél: hatásos CdA × (cos²β + 1,2·sin²β) [isvan-2015-wind-yaw B]. Ultra-alapérték: átlag 10 km/h véletlen irányú szél ≈ −0,5 km/h szélcsendhez képest [white-2016-ridefar-resistance C].
- **Tömeg:** 85 kg alap (67 + 10 + 8) [white-2016-ridefar-method C]; érzékenység 0,06–0,08 km/h/kg, ~1 perc/100 km/kg [white-2016-ridefar-resistance C].
- **Ellenőrző értékek (derived, 85 kg, ρ 1,2, Crr 0,005, η 0,976, sík):** 150 W → 32,4 / 30,6 / 29,2 / 28,1 / 27,1 km/h CdA 0,25 / 0,30 / 0,35 / 0,40 / 0,45-nél; 100 W (CdA 0,35) 24,8; 200 W 32,7 km/h. Crr 0,005 → 0,012 (CdA 0,40): 28,1 → 24,7 km/h. 150 W emelkedőn (CdA 0,35, 85 kg): 2% 19,5; 4% 13,1; 6% 9,5; 8% 7,4; 10% 6,0 km/h.
- **Emelkedés-ökölszabály:** 100 m szint ≈ +5 perc 150 W-on 85 kg-mal (3–8%-os lejtésen +3,4…+6,2 perc, fel + le vs sík, derived); felső korlát m·g·h/(η·P) ≈ 9,5 perc / 100 m (lejtő-visszanyerés nélkül).

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q6)
- Nincs lektorált CdA-mérés aerobaros, TELJESEN táskázott ultra-bringára (Frank 2021 hoods-ban, aerobar nélkül; BikeRadar/Grappe táska nélkül) – a 0,28–0,32 m² tartomány két forrás kombinációja (derived).
- Nincs mért Crr laza murvára / Tour Divide-jellegű felületre kerékpáron; Bertucci abszolút számai a nem elérhető teljes szövegben, Steyn táblázata a 429-es ResearchGate-en; a Zwift-féle 0,012–0,014 játékparaméter (nem hivatkozott, D).
- A Martin-modell 20–40 km/h-n, sík, szélcsendes, pihent versenyzővel validált; 15–25 km/h-n, terhelten, fáradtan (változó pozíció, "lazuló" CdA) nincs validáció – a 2–3%-os BBS-pontosság ultrára át nem vihető.
- Az "impedancia" (érdes felületen a magas nyomás növeli a veszteséget, Silca 2014) csak grafikonban, számszerű Crr nélkül publikált.
- Lejtősebességre és éjszakai/kanyaros korrekcióra nincs terepadat.

### ELLENTMONDÁS (Q6)
- Aerobar-nyereség: −0,03 m² (Ridefar, konzervatív, TCR-nettó ~40 perc) vs −0,057 m² (BikeRadar szélcsatorna, 31 W/35 km/h) vs −4,6 pont (Grappe AP vs DP: −0,014 m²). A különbség a referenciahelyzettől (hoods vs drops) és az aerobar-kialakítástól függ; a modulban 0,02–0,05 m² sávot érdemes adni és mérésre (Chung-módszer) buzdítani.
- Táskatartó-hátrány: 0,07–0,10 m² (CyclingAbout velodrom-adatból) vs ~0,025 m² (GCN, Ridefar-idézet) – 4-szeres szórás, a kis mintás tesztek nem egyeztethetők.
- Magasság: a Ridefar szerint 1000 m-en −5% teljesítmény és −8% sűrűség (síkon nettó nyereség), Bassett szerint az optimum 2000–2500 m – de ez órarekordra (maximális aerob, akklimatizáció) vonatkozik; többnapos, alacsony intenzitású ultrán a magasság-teljesítmény görbe laposabb lehet (nincs adat).

---

## Feltörekvő irányok
- Tracker-alapú "stationary time" statisztika versenyzőnként (DotWatcher 2026-os briefingek már közlik az első napra) – ha a szervezők a teljes versenyre publikálnák, a Q3 első lektorálható adatbázisa lehetne. [mckenzie-dotwatcher-tcr12-briefing-2026 B]
- Chung-módszeres terepi CdA-mérés bikepacking-beállításokra (Frank 2021) – olcsó, reprodukálható; a modul "mérd meg a saját CdA-dat" feladatának alapja. [frank-2021-tailfin-aero B]
- Gépi tanulásos idő-előrejelzés útvonal-topológiából és edzésterhelésből (Aguilera Moreno 2025, arXiv 2601.00604: MAE 6,6 perc, R² 0,92, 96 rövid túrán) – ultrára nem validált, D fokozat, nem vettem fel forrásként.
- Oldalszél-korrekció (virtuális yaw, μ-arány) beépítése közösségi kalkulátorokba (Isvan 2015) – jelenleg csak a BBS és az Aerotune kezeli.

## Nem sikerült megnyitni
- Bertucci 2013 teljes szöveg / absztrakt kiadói oldalon (tandfonline 403, PubMed captcha, ResearchGate 429, Europe PMC REST 429) – absztrakt OpenAlex-rekonstrukcióból, DOI Crossrefen ellenőrizve.
- Bassett 1999 kiadói oldal (journals.lww.com 402) – absztrakt OpenAlex-ből, DOI Crossrefen ellenőrizve.
- Grappe 1997 kiadói oldal (tandfonline 403) – absztrakt OpenAlex-ből, DOI Crossrefen ellenőrizve.
- Steyn & Warnich 2014 Crr-táblázat (ResearchGate 429; AJOL csak absztrakt, cikk-DOI nélkül).
- Martin 1998 kiadói oldal (journals.humankinetics.com 403) – Utah-repozitóriumi szerzői PDF megnyitva, DOI Crossrefen ellenőrizve.
- trackleaders.com egyéni Tour Divide-előzmények (403) – a "miles per day" tervezőszámok csak sajtón/blogokon át.
- kreuzotter.de (TLS-hiba), diva-portal.org (robots/timeout), velo.outsideonline.com (redirect-hurok), ridefar.info /tire-rolling-resistance/ és /environmental-factors/ (404; a helyes URL-ek /rolling-resistance/ és /environmental/ megnyitva).
- Ride with GPS becslő dokumentációja számszerű tartalommal; Silca "Part 4B" számszerű Crr-adatai (csak grafikon).
- Crossref API a munkamenet egy részében 429 (WebFetch) és 403 (Bash-curl, proxy-tiltás); az Isvan 2015 és Groeskamp 2017 (JSC) DOI-kat ezért nem sikerült ellenőrizni → doi: null.
