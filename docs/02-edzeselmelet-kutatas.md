# 02 · Edzéselmélet ultrára — kutatási összefoglaló (v0.1, 2026-09-24)

## Hogyan készült

Négy párhuzamos kutatóügynök, tizenegy kérdés (Q1–Q11), 92 új forrás (A: 26, B: 23, C: 21, D: 24; két kulcsot — `bosquet-2007-taper-meta`, `ronnestad-2014-strength-review` — két csomag egyszerre definiált, az első maradt) a `data/sources.yaml`-ban `02:` előtagú kérdéskulccsal; a forrástár így 429 tételes. A fokozatok az új tételeknél: A 33, B 14, C 45; 61 ellenőrzött DOI-val. A 03-as tényellenőrzés tanulságai beépítve a briefekbe: a forrástár `grade` mezője a mérce, összefűzött tartomány két forrásból tilos, hatásméret mellé konfidencia-intervallum, populáció (sport, edzettség, nem) mindig kiírva. A meglévő durability-, HRV-, alvás- és RED-S-kulcsokra az ügynökök csak hivatkoztak. A nyers kimenetek: `data/raw/02-A…D-sources.yaml` és `-evidence.md`; a bizonyíték-térképek teljes szövege e dokumentum második felében. Kérdésfelosztás: A = Q1 intenzitás-eloszlás, Q2 volumen vs. intenzitás, Q3 hosszú edzés és back-to-back; B = Q4 periodizáció, Q5 tapering, Q6 erősítés; C = Q7 terhelésmutatók, Q8 HRV és készenlét, Q9 túledzés és betegség; D = Q10 versenyzői konvergencia, Q11 feltörekvő irányok.

Keretszabály (Attila döntése): a modul elveket és bizonyítékot tanít, konkrét heti terv-sablont csak keretként ad, és minden feladatnál ott az „az edződdel egyeztetve”.

## A modul tíz kulcsállítása (a bizonyíték-térkép sűrítménye)

1. **Az összterhelés és a konzisztencia az elsődleges — az eloszlás és a periodizációs forma másodlagos.** A legnagyobb TID-meta (17 vizsgálat, n = 437) időfutam-teljesítményre nulla különbséget ad a modellek között (SMD −0,01; CI −0,28–0,25); a legnagyobb terhelés-kiegyenlített kerékpáros RCT-ben (n = 63, 12 hét) a HIT-elrendezés semmilyen adaptációs különbséget nem hozott; a hobbifutó-RCT-ben mindkét eloszlás javított, a különbség nem szignifikáns. [silva-oliveira-2024-pol-meta A; sylta-2016-hit-periodization A; munoz-2014-recreational A]
2. **Z1-dominancia + kevés tudatos minőség.** Az elit session-alapon ~80/20 (pulzus-idő szerint 75/8/17); az idő-alapú ~90/10 szerkesztői becslés; edzett kerékpáros vizsgálatok (7,5–11,7 h/hét — pont a célközönség sávja!) ~80 % Z1; a kis RCT-k polarizált-fölénye (kerékpáros: PPO +8 vs. +3 %) és az elit piramis-gyakorlata a session/idő-számolással és a fázissal békíthető. Ultrán a Z1–Z2 egyben versenyspecifikus. Kalkulátor-sávok: 6–8 h/hét: Z1 75–80 %; 8–12 h: 80–85 %; 12–15+ h: 85–90 %. [seiler-kjerland-2006 B; galan-rioja-2023-cyclist-tid-sr A; neal-2013-polarized-cyclists A; mateo-march-2025-worldtour B]
3. **A volumen belépőjegy, nem rangsoroló.** A 720 km-es RAAM-kvalifikáción (n = 76) a befejezést a heti edzésóra (r = 0,44) és -táv (r = 0,37) jósolta; egy 600 km-es versenyen (28 befutó) a befutók 3 havi volumene nem rangsorolt (r² = 0,000) — két külön vizsgálat; futóknál a könnyű volumen a legerősebb szint-prediktor (r ≥ 0,75). Óraszám-horgonyok: edzői 10–15 h/hét 320+ km-re, elit 15–20 h; amatőr TCR-teljesítés ~9–11 h/héttel is dokumentált (n = 1). [knechtle-2011-finishers-720km B; knechtle-2009-anthropometry-600km B; casado-2019-easyruns B; towers-2024-trainingweek C; houston-tcr-training C] {férfi}
4. **A fáradtságállóság (durability) az edzés-oldali fő cél — és volumen-függő.** Profi U23-aknál a VT1 alatti edzésidő korrelált a fáradt-teljesítmény javulásával (r = 0,43); a romlást az intenzitás hajtja, nem a kJ; egyetlen terhelésmutató sem jelezte előre az adaptációt, az LT1 alatti volumen a zsíranyagcsere-javulással függött össze. A HIIT időhatékonyan emeli a VO2max-ot (+1,2 ml/kg/perc többlet), de a többórás teljesítménymegtartáshoz a Z1-Z2 volumen kell — kevés órából élőnek mindkettő. [spragg-2022-durability-training B; voet-2025-durability-training B; sanchez-jimenez-2025-durability-sr A; milanovic-2015-hiit-meta A]
5. **A hosszú edzés és a back-to-back a felkészülés gerince — kontrollált bizonyíték nélkül, egybehangzó gyakorlattal.** A 4–10 órás edzés hozama a versenyspecifikus fáradt állapot, a zsíranyagcsere, az ülés-tűrés és a bél-, felszerelés-, fej-gyakorlás; back-to-back RCT nincs, minden edző használja (rajt előtti 4–8 hét); a brevet-sorozat (200→300→400→600) kész progresszió, a 600-as az alvás-főpróba; a leghosszabb blokk többnapos versenyre 2–4 napos főpróba ~4 héttel a rajt előtt, nem egyetlen extrém táv. Éjszakai menetgyakorlás igen; szándékos alvásmegvonás-edzés nem (36 h ébrenlét −11 % kimerülési idő, a kockázat valós). [rutberg-cts-multiday C; apidura-2018-ultratraining C; pbp-2027-rules C; martin-1981-sleep-rpe A; craven-2022-akut A]
6. **A periodizáció-forma alig számít, a szerkezet a logisztikáé.** Blokk-meta: kicsi, bizonytalan előny nagyon gyenge irodalomból (VO2max SMD 0,40; PEDro 3,7/10); fordított periodizáció nem jobb; a Kiely-kritika szerint a merev séma helyett az élet-összterhelésre reagáló rugalmas tervezés indokolt. Ami marad: 16–24 hét, 3+1 (vagy 2+1) hetes blokkok, terhelés-csúcs 4–6 héttel a rajt előtt, heti ≥1 pihenőnap — a pihenőhét kihagyása a leggyakrabban bevallott hiba. [molmen-2019-block-meta A; gonzalez-rave-2022-reverse A; kiely-2018-periodization-critique C; grandgeorge-t2m-season C; towers-2024-trainingweek C]
7. **Tapering: 2 hét, −41–60 % volumen, az intenzitás és a gyakoriság marad** (ES 0,72 ± 0,36; tipikus nyereség ~3 % rövid teljesítményen); többnapos ultrára a gyakorlat 2–3 hét, enyhébb lejtéssel, az utolsó napokban alvás-prioritással — ultra-taper vizsgálat nincs, a fő hozadék ott a frissesség, a glikogén és a betegség-kockázat. A feltöltés +~1 kg tömege glikogén + víz, nem zsír (kapcsolat a 03 modullal). [bosquet-2007-taper-meta A; mujika-2003-taper-bases C; shiose-2016-carboload-water A; white-ridefar-trainingplan C]
8. **Erősítés: heti 2 nehéz alkalom a felkészülésben, heti 1 fenntartó a szezonban — és a haszon éppen ultra-releváns.** 12 hét láberősítés után a 185 perc tekerést követő 5 perces teljesítmény +8 % (a friss nem változott); nőknél is működik; az interferencia-félelem alaptalan (erő SMD −0,06); a gazdaságosság-narratívát a 2025-ös kerékpáros meta nem erősíti meg. Nyak (Shermer), kéz, törzs: mért protokoll nincs, a törzsfáradás mérhetően rontja a hajtás-mechanikát (+54 % térd-kitérés), a konszenzus a core + húzó-tartó munka és a pozíció-gyakorlás. [ronnestad-2011-strength-185min A; vikmoen-2016-female-cyclists A; schumann-2022-concurrent-meta A; llanos-lagos-2025-hst-cyclists-meta A; abt-2007-core-cycling B; dotwatcher-shermers-roundtable C]
9. **A terhelésmutató iránymutató, nem cél.** TSS = óra × IF² × 100 (plafon 100/óra; ultra-alap Z2 ≈ 31–56 TSS/h); CTL/ATL/TSB a Banister-modell leegyszerűsítése, populációs időállandókkal; >6 órás edzésre és többnapos terhelésre sehol nem validált, a hosszú Z1-t alulárazza; sRPE (perc × CR-10) eszköz nélkül is konzisztens; egyénileg kalibrált belső mutató (iTRIMP r = 0,81) veri a gyárit; a rámpa-sáv (heti +3–8 CTL) edzői heurisztika; az ACWR számsávja („0,8–1,3”) nem tanítható tényként — az elv (ne ugorj hirtelen) marad. [foster-2001-session-rpe A; sanders-2017-load-cyclists B; clarke-2013-banister-model C; friel-ramp-rate C; impellizzeri-2020-acwr C]
10. **A szubjektív jel veri az objektívet — a HRV trendként hasznos, parancsként nem.** Kerékpáros 8 napos terepvizsgálatban egyetlen objektív napi mutató sem jelezte egyénileg a túlterhelést, a fáradtság + edzéskészség kérdőív a 3. napon 78 %-os pontossággal igen; a HRV-vezérelt RCT-k „ugyanaz vagy jobb, kevesebb intenzív edzésből” (meta csoportszinten null); a mérés: reggeli rMSSD, 7 napos gördülő átlag; a betegség és az alkohol nagyobb kilengés, mint az edzés; a magas HRV túlterhelésnél is nőhet. Túledzés: a romló alvás korai jel (F-OR: alvásidő −7,9 %, felső légúti fertőzés 67 vs. 11 %); láz és „nyak alatti” tünet = tilos edzeni; teljesítményesésnél az energia-audit (RED-S) megelőzi a túledzés-diagnózist. [tenhaaf-2017-for-prediction B; javaloyes-2019-hrv-cycling A; medellin-2020-hrv-meta A; plews-2013-hrv-monitoring C; altini-2021-hrv-freeliving B; bellenger-2016-hrv-meta A; hausswirth-2014-sleep-illness A; stellingwerff-2021-ots-reds C]

**Hőblokk és feltörekvő (Q11):** a melegadaptáció 6–14 nap alatt kiépül (plazmatérfogat, korábbi izzadás, alacsonyabb RPE), ~2,3–2,6 %/nap ütemben cseng le, az újra-indukció 8–12× gyorsabb — a hőblokk a taperrel átfedésben időzítendő; elit kerékpárosoknál 5 hét heti 5×50 perc hőedzés +2,4–2,6 % hemoglobin-tömeget adott mérsékelt klímára is („olcsó magaslat”); az LHTL-magaslat nagy hatása amatőrnek elérhetetlen dózisú. Minimál-dózis: az állóképesség 15 hétig megőrizhető heti 2, intenzitást tartó edzéssel (−33–66 % volumen) — munka-csúcsidőszakra. BET (agyi állóképesség-edzés): +11–17 % kimerülési idő két kerékpáros RCT-ben, de egyetlen kutatócsoporttól, ultra-formátum és női adat nélkül — feltörekvő jel. AI-edzéstervezők: nulla független validáció. [tyler-2016-heatadapt-meta A; daanen-2018-hadecay-meta A; ronnestad-2022-heat-hbmass A; feng-2023-hypoxia-nma A; spiering-2021-minimaldose A; staiano-2023-bet-cyclists A; paine-2026-ai-coaching C]

**Versenyzői konvergencia (Q10, 10 témasor):** egybevágó: hétvégi back-to-back hosszú, heti 1–2 minőség, 3+1 blokk, heti ≥1 pihenőnap, 1–2 (RAAM-nál 1–3) hét taper „sosem lehetsz túl friss” zárással, brevet-lépcső kezdőknek, core mindenkinél. Eltérő: a leghosszabb edzés (White: „4–6 óra fölött nincs élettani többlet” vs. Hughes 2/3–3/4 versenytáv vs. Barth 400–1000 km-es próbák), a minimális óraszám (CTS 4–6 h/hét vs. Towers „12 alatt nem optimális”), és a strukturált intervallos (Towers, Barth, CTS, Ibbett) vs. strukturálatlan volumen-modell (Wilcox az odatekerést, Sehili a futárkodást nevezi edzésnek) — mindkettő győztest termelt; a közös nevező az összterhelés és a konzisztencia. [white-ridefar-trainingplan C; comeau-2017-raam-training C; towers-2024-trainingweek C; pulford-2026-timecrunched C; barth-tcr-trainingpeaks-plan C; wilcox-expeditionportal C; sehili-roadcc-2023 C; lenhard-apidura-audax C]

## Ellentmondások, amiket a modulnak explicit módon kezelnie kell

- **E1 — Polarizált-fölény (kis RCT-k) vs. meta-null vs. elit piramis-gyakorlat.** Feloldás: a Z1-dominancia és a kevés tudatos minőség a közös mag; a session- vs. idő-alapú számolás és a fázis magyarázza a címke-vitát — a modul nem címkét, hanem arányt tanít.
- **E2 — A HIIT időhatékony (VO2max) vs. a durability volumen-függő.** Mindkettő kell: minimális minőség a plafonra, minden megmaradt óra Z1–Z2; a hétköznapi volument a hétvégi hosszú pótolja.
- **E3 — „4–6 óra fölött nincs élettani haszon” (White) vs. a hosszú edzés primátusa (RAAM-iskola, Hughes) és a durability-irodalom.** A modul kimondja: a kérdés méretlen; a hosszú edzés nem-élettani hozama (bél, ülés, felszerelés, fej) önálló indok, a 4–6 óra feletti élettani többlet nyitott.
- **E4 — Blokk-periodizáció: Rønnestad-fölény vs. gyenge meta vs. Sylta-null.** Az összvolumen és a konzisztencia az elsődleges; a HIT-blokk munka melletti amatőrnek logisztikai minta, nem kötelező forma.
- **E5 — A taper-paraméterek átvitele ultrára:** a meta az intenzitás megtartását írja elő, de ultrán az „intenzitás” maga a hosszú edzés; a modul a 2–3 hetes, enyhébb lejtésű ultra-tapert tanítja, jelölve, hogy kontrollált adat nincs.
- **E6 — Erő-gazdaságosság narratíva vs. 2025-ös meta.** A fő haszon nem a gazdaságosság, hanem a fáradt-állapotú teljesítmény és az elfáradás-késleltetés.
- **E7 — ACWR: „kritikus prediktor” (Gabbett) vs. „statisztikai műtermék” (Impellizzeri).** Az elv (fokozatos progresszió) tanítható, a számsáv nem.
- **E8 — HRV: egyedi RCT-k előnye vs. meta-null; „magas HRV = jó” vs. Bellenger.** A konzisztens lelet: ugyanaz vagy jobb eredmény kevesebb intenzív edzésből — a HRV a kemény napok időzítője, nem teljesítmény-fokozó; a magas érték is lehet túlterhelés-jel.
- **E9 — J-görbe (nagy volumen → több fertőzés) vs. immun-újraértelmezés.** A tünet-klaszterek valósak, a mechanizmus vitatott; a védekezés (alvás, energia, higiénia, progresszió) mindkét olvasatban ugyanaz.
- **E10 — A volumen prediktor (befejezés) vs. nem rangsoroló (befutók között).** A modul kettéválasztja a célt: a befejezéshez volumen, a helyezéshez a szerkezet, a durability és a 08-as logisztika.
- **E11 — Strukturált vs. strukturálatlan modell.** Nem tudományos vita, hanem életforma-kérdés: mindkettő győztest termelt; a döntő az összterhelés, a konzisztencia és hogy melyik tartható fenn az életed mellett.

## Bizonyítékhiányok (ahol a modul csak „legjobb becslést” adhat)

- Nincs egyetlen RCT sem ultra-kimenettel (>4 óra teljesítmény) — sem TID-re, sem volumenre, sem periodizációra, sem taperre, sem erősítésre; minden A-fokozatú adat ≤12 hetes, perc–órás labor-kimenet.
- Nincs publikált felmérés a TCR- vagy bármely önellátó ultra-mezőny edzésóráiról; a legjobb közelítés a 720 km-es kvalifikáció kohorsza (egynapos formátum). Az óraszám-ajánlások edzői keretszámok.
- Back-to-back hosszú napok adaptációs többlete méretlen; a „leghosszabb edzés a versenytáv X %-a” szabályra semmilyen adat; a 4–10 órás edzés dózis-válasza (3 vs. 5 vs. 8 óra) összehasonlítatlan.
- A TSS/CTL-modell 6 óránál hosszabb edzésre és többnapos terhelésre nem validált; a rámpa-sávra nincs lektorált bizonyíték; sRPE-kalibráció >6 órás edzésre nincs.
- HRV-vezérlés ultratávra vagy Z2-blokkra nem tesztelt; Whoop/Garmin readiness-pontszámok független validációja nincs; nő-specifikus (ciklus-korrigált) protokoll nincs.
- Amatőr, munka melletti OTS/NFOR-prevalencia ismeretlen; ultrakerékpáros betegség-incidencia felkészülés alatt méretlen; a „nyak-szabály” prospektíven nem validált; a krónikus alváshiány melletti edzés adaptációs ára méretlen (csak akut adat).
- Nyak-, kéz-, ülőgumó-specifikus erősítő protokoll ultrán nem létezik; kar-comb aszimmetria bikepacking-terhelésnél méretlen; erősítés többnapos teljesítményre méretlen.
- Hőprotokoll többnapos önellátó terepen nem tesztelt; a hőedzés × alváshiány × energiahiány interakció ismeretlen; BET-nek nincs ultra- és nő-adata; AI-tervezőkre nulla független validáció.
- A női adat az egész modulban alulreprezentált (kivétel: vikmoen-2016; a HRV-ciklushatás jelzett, nem kezelt) — a {férfi} jel itt is sokszor kell majd.
- Nem sikerült megnyitni: Knechtle 2012 (PBP vs. RAAM összehasonlítás), a Voet-korrelációk teljes listája, Plews 2013 teljes szöveg, Banister-eredeti, Strasser TCR-interjú (Cyclist, 403), Hayden edzés-videó (csak YouTube).

## Feltörekvő irányok (a modul „feltörekvő” jelével)

Durability mint önálló edzéscél (mérési módszertan kész, intervenciós RCT nincs; edzői kJ-küszöbös protokollok terjednek); hőedzés mint „olcsó magaslat” (Hb-tömeg +2,4–2,6 %); többdimenziós terhelés-modellek a TSS helyett; rugalmas, élet-terheléshez igazított periodizáció (Kiely nyomán, HRV-/készenlét-vezérléssel); BET; minimál-dózis fenntartó protokollok; OTS–RED-S egyesített szűrés (energia-audit először); AI-adaptív tervezés human-in-the-loop irányban. [hunter-2025-durability-methods A; pulford-2026-durability-cts C; ronnestad-2022-heat-hbmass A; voet-2025-durability-training B; kiely-2018-periodization-critique C; staiano-2023-bet-cyclists A; spiering-2021-minimaldose A; stellingwerff-2021-ots-reds C]

## Döntést igénylő pontok (Attila) — döntve 2026-09-24

Attila válaszai: 1 mindkét eszköz a leírt rétegekkel; 2 a három Mérd be magad feladat elfogadva; 3 HRV protokoll-oldal a döntési szabályokkal, wearable-pontszám {ev:D}; 4 ACWR-elv igen, számsáv lábjegyzetben; 5 hőblokk teljes protokoll-oldal; 6 éjszakai menetgyakorlás igen, szándékos alvásmegvonás-edzés nem; 7 strukturált vs. strukturálatlan a konvergencia-oldalon döntési kerettel (nem vita-oldal); 8 a tíz kulcsállítás elfogadva.

- [x] **A két web-eszköz rétegei.** (1) *Terhelés-kalkulátor:* heti órák zónánként → TSS (vagy sRPE eszköz nélkül) → CTL/ATL/TSB-szimuláció rámpa-figyelmeztetéssel (3–5 / 5–8 / ≤10 sáv), többnapos esemény terhelés-becslése (heti 2–3×), durability-teszt kiértékelő (friss vs. fáradt 20 perc, %-esés sávokkal). (2) *Ütemterv-generátor:* versenydátum + heti időkeret + formátum → fázisok visszafelé (taper 10–21 nap → csúcs/specifikus a −6…−3. héten back-to-back-kel és 2–4 napos főpróbával → építés 2+1/3+1 blokkokban → alap), brevet-naptár (200→300→400→600, a 600-as legkésőbb −4…−6. hét), opcionális hőblokk a taper alatt, erősítés-napok. Minden kimenet „keret — az edződdel egyeztetve” jellel. Jó így?
- [x] **„Mérd be magad” feladatok.** Javaslat: (1) saját zónák terepi bemérése (20 perces teszt + beszédteszt az LT1-re), (2) 4 hetes sRPE + reggeli készenlét-napló (a tenhaaf-kérdőív két kérdésével), (3) a durability-teszt a 08-ból hivatkozva, itt a kJ-célokkal (1000–2500 kJ előmunka). Elfogadod?
- [x] **HRV-oldal.** Javaslat: protokoll-oldal a döntési szabályokkal (mikor cseréld az intenzív edzést Z1-re), a wearable readiness-pontszámok {ev:D} jellel; a „nem kell hozzá eszköz” alternatíva (reggeli pulzus + kérdőív) egyenrangúan. OK?
- [x] **ACWR és rámpa.** Javaslat: az elv tanítása + a rámpa-sáv `{példa}` jellel, az ACWR-számsáv kihagyása (csak lábjegyzetben, miért nem). OK?
- [x] **Hőblokk.** Javaslat: teljes protokoll-oldal (nem csak feltörekvő), mert három A-fokozatú meta támogatja, és a nyári ultrákra (RACA, TCR) közvetlenül releváns: 6–14 nap, időzítés a taperrel átfedésben, fenntartó szabály. OK?
- [x] **Éjszakai edzés vs. alvásmegvonás.** A modul álláspontja: éjszakai menetgyakorlás igen (világítás, navigáció, hideg), szándékos alvásmegvonás-edzés nem — azt a 600-as brevet adja kontrollált keretben. Elfogadod?
- [x] **Strukturált vs. strukturálatlan.** Javaslat: nem vita-oldal (nem tudományos vita), hanem a konvergencia-oldal kiemelt sora + egy döntési keret („melyik tartható fenn az életed mellett”). Vagy legyen mégis vita-oldal, mint a keto?
- [x] A tíz kulcsállítást elfogadod a modul gerincének?

## Validálás (v0.1 tényellenőrzés, 2026-09-24)

Független tényellenőrzés (`docs/02-tenyellenorzes.md`): 44 tétel (3 magas, 5 közepes, 36 alacsony), mind átvezetve a modulba és az ábrákba. Örökölt hibák, itt javítva: a 3. kulcsállítás a 720 km-es (n = 76) és a 600 km-es (n = 28) Knechtle-vizsgálatot egy eseménnyé vonta össze — az r² = 0,000 a 600 km-es befutóké; a 2. kulcsállítás „idő-alapon ~90/10”-e a seiler-2010 notes szerkesztői becslése, a seiler-kjerland mért adata 75/8/17 (session-cél szerint); a modul a spragg-2024-et a „kJ tolja a görbét” állításhoz citálta, holott épp az ellenkezőjét méri (a jó kulcs a clark-2019); az ultra-versenyintenzitás 55–70 % FTP (a 08. modul szerint), nem 50–70; a ronnestad-2014-strength-review a D csomagban A-nak volt jelölve, a forrástár szerint C. Tanulság-megerősítés: a forrástár `grade` mezője a mérce; két vizsgálat száma nem vonható össze egy mondatba az n-ek jelölése nélkül; az ábrák sematikus paneljeit a caption-ben is jelölni kell.

---

# Bizonyíték-térképek kérdésenként (a négy ügynök nyers kimenete, változatlanul)


## Csomag A

Q1: intenzitás-eloszlás (polarizált / piramis / küszöb) · Q2: volumen vs. intenzitás · Q3: hosszú edzés és back-to-back
Készült: 2026-09-24. Kulcsok: /home/claude/ultra/data/raw/02-A-sources.yaml + data/sources.yaml (meglévő tár).

---

## Q1 — Intenzitás-eloszlás: polarizált vs. piramis vs. küszöb

1. **A 3-zónás modell horgonya a két szellőzési küszöb: Z1 = VT1 alatt (≈ ≤2 mM laktát), Z2 = VT1–VT2 között (≈2–4 mM), Z3 = VT2 felett.** Elit junior sífutóknál a pulzus-idő eloszlás 75±3% / 8±3% / 17±4% volt, a laktátmérések 71%-a ≤2,0 mM [seiler-kjerland-2006 B; seiler-2010-bestpractice C].
2. **Az elit „best practice" session-alapon ~80/20: a session-ök ~80%-a alacsony intenzitású, ~20%-a kemény; idő-alapon ugyanez inkább ~90/10.** A küszöb körüli középzóna nagy stresszt ad viszonylag kis többlet-adaptációért [seiler-2010-bestpractice C; seiler-kjerland-2006 B].
3. **A legnagyobb TID-RCT-ben (48 jól edzett sportoló, 9 hét) a polarizált csoport nyert minden kulcsváltozóban: VO2peak +11,7% (+6,8 ml/kg/perc, p<0,001), kimerülési idő +17,4%, csúcsteljesítmény +5,1%; a küszöb- és a nagy-volumen-csoport érdemben nem javult** [stoggl-2014-polarized-rct A].
4. **Kerékpáros-specifikus RCT (12 edzett kerékpáros, ~6–10 h/hét, 2×6 hét cross-over): polarizált (80/0/20) vs. küszöb (57/43/0) azonos edzésidőnél — PPO +8±2% vs. +3±1%, laktátküszöb +9±3% vs. +2±4%, nagy intenzitású kapacitás +85±14% vs. +37±14% a polarizált javára (p<0,05)** [neal-2013-polarized-cyclists A].
5. **Meta-szinten a kép kimenet-függő: VO2peak-re kis polarizált-előny (SMD=0,24; 95% CI 0,01–0,48; 17 vizsgálat, n=437), de időfutam-teljesítményre NINCS különbség a TID-modellek közt (SMD=-0,01; CI -0,28–0,25)** [silva-oliveira-2024-pol-meta A]. A korai, 3 RCT-s meta még közepes POL-előnyt mért időfutamra (ES=-0,66; CI -1,17 – -0,15), de PEDro 4–5/10 minőségű vizsgálatokból [rosenblat-2019-pol-thr-meta A].
6. **Amatőr, alacsony óraszámú adat: 30 hobbifutó, 10 hét, ~77/3/20 vs. ~46/35/19 — mindkét csoport javult 10 km-en, a polarizált 5,0%, a küszöb 3,6% (~41 s különbség), a csoportkülönbség nem szignifikáns** [munoz-2014-recreational A]. Vagyis amatőr szinten a polarizált „legalább olyan jó", de fölénye nem bizonyított.
7. **A szekvencia többet számít, mint az egyetlen „legjobb" eloszlás: 60 jól edzett futónál (16 hét) a piramis→polarizált váltás adta a legnagyobb javulást (~3,0% VO2max, ~1,5% 5 km-es idő)** [filipas-2022-pyr-pol A].
8. **Edzett kerékpárosok vizsgálataiban (7 tanulmány, n=161, heti 7,5–11,7 óra!) 8–12 hetes távon egyik periodizációs/TID-modell sem bizonyítottan jobb a másiknál** — a vizsgált óraszám pont a célközönség sávja [galan-rioja-2023-cyclist-tid-sr A].
9. **A profi gyakorlat nem polarizált, hanem piramis + progresszív intenzifikáció: 28 World Tour-kerékpáros szezonelemzésében a volumen fázisról fázisra nőtt, az eloszlás piramis mintázatú, a magas intenzitás aránya a versenyek felé nőtt (p≤0,001)** [mateo-march-2025-worldtour B].
10. **Ultra-transzfer tézis: mivel az ultra-versenyintenzitás Z1–Z2 (FTP 50–70%-a), a Z1-dominancia egyben versenyspecifikus edzés is; a Z3-minőség szerepe a fittségi plafon (VO2max, küszöb) emelése — az eloszlás-vita a teljes terhelés és a konzisztencia mögött másodlagos** [silva-oliveira-2024-pol-meta A; galan-rioja-2023-cyclist-tid-sr A; spragg-2022-durability-training B].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q1):** Nincs egyetlen RCT sem, amely TID-modelleket ULTRA-állóképességi (>4 h) kimeneten hasonlítana össze; a meták kimenetei 5 km–40 km időfutamok és VO2peak [silva-oliveira-2024-pol-meta A; rosenblat-2019-pol-thr-meta A]. Heti 6–8 órás KERÉKPÁROS mintán TID-RCT nem került elő (keresések: "polarized training recreational cyclists low volume RCT", "training intensity distribution amateur cyclists"); a legjobb közelítés a hobbi-futó adat [munoz-2014-recreational A] és a 7,5–11,7 h/hét kerékpáros áttekintés [galan-rioja-2023-cyclist-tid-sr A]. Női adat mindenhol alulreprezentált.

**ELLENTMONDÁS (Q1):** (1) Stöggl–Sperlich és Neal RCT-i egyértelmű polarizált-fölényt mérnek [stoggl-2014-polarized-rct A; neal-2013-polarized-cyclists A], míg a 2024-es nagy meta időfutamra nullhatást [silva-oliveira-2024-pol-meta A], és a Burnley–Bearden–Jones vitacikk szerint „a polarizált edzést az elit valójában ritkán gyakorolja, és nincs érdemi bizonyíték, hogy hatékonyabb más modelleknél" [burnley-2022-pol-debate C]. (2) A megfigyelt elit gyakorlat (piramis, [mateo-march-2025-worldtour B]) és a kis RCT-k polarizált-fölénye közti feszültséget részben a session- vs. idő-alapú számolás és a definíciós káosz magyarázza [burnley-2022-pol-debate C; seiler-kjerland-2006 B]. A modul ajánlott tanítása: „Z1-dominancia + kevés, tudatos minőség" — a címke (polarizált vs. piramis) mellékes.

**KALKULÁTOR-PARAMÉTEREK (Q1) — zónaarány-ajánlás heti óraszám-sávokra (idő-alapú, 3-zónás modell):**
- Elvi horgony: elit idő-alapú eloszlás ~88–92% Z1 [seiler-kjerland-2006 B]; edzett kerékpáros vizsgálatok: ~80% Z1 [galan-rioja-2023-cyclist-tid-sr A]; ultra-versenyző gyakorlat: 80/20–90/10 [towers-ultra-training C].
- **6–8 h/hét:** Z1 75–80% / Z2 10–15% / Z3 8–12%; heti 1 minőségi (Z3-intervall) + 1 tempó/sweet spot edzés, a többi Z1 — kis óraszámnál a heti 1-2 intenzív edzés aránylag nagyobb szeletet vihet [neal-2013-polarized-cyclists A; munoz-2014-recreational A; milanovic-2015-hiit-meta A].
- **8–12 h/hét:** Z1 80–85% / Z2 8–12% / Z3 6–10%; heti 1-2 minőség + 1 hosszú Z1-Z2 [galan-rioja-2023-cyclist-tid-sr A; tatt-boundary-ultraguide C].
- **12–15+ h/hét:** Z1 85–90% / Z2 5–10% / Z3 4-6%; a többlet-óra gyakorlatilag mind Z1-be megy (a Z3 abszolút mennyisége nem nő tovább) [seiler-2010-bestpractice C; mateo-march-2025-worldtour B; towers-ultra-training C].
- Fázis-moduláció: alapozásban piramis-jellegű (több Z2-tempó), specifikus fázisban vagy polarizáltabb, vagy ultra-specifikusan még Z1-dominánsabb [filipas-2022-pyr-pol A; mateo-march-2025-worldtour B]. Megjegyzés a kalkulátorba: „az arányok idő-alapúak; session-alapon a Z3-arány magasabbnak látszik".

---

## Q2 — Volumen vs. intenzitás; time-crunched; durability-edzés

1. **A volumen a legerősebb ismert teljesítmény-prediktor hosszútávon: 85 futó retrospektív adatában a könnyű futás volumene r≥0,75 (p<0,001) korrelált a versenyszinttel, az összvolumen a variancia ≥57%-át magyarázta (R²≥0,57); a tempófutás r=0,68, a hosszú-intervall csak r=0,22** [casado-2019-easyruns B].
2. **VO2max-ra viszont az intenzitás időhatékony: meta-analízisben (28 vizsgálat, n=723) a HIIT +5,5 ml/kg/perc (±1,2), a folyamatos edzés +4,9 (±1,4); a HIIT többlete mindössze 1,2 ml/kg/perc (±0,9)** — a time-crunched logika (kevés óra + minőség) VO2max-oldala valós [milanovic-2015-hiit-meta A].
3. **A time-crunched megközelítés ultra-korlátja: a HIIT-meták kimenete VO2max, nem többórás teljesítmény; a fáradtságállósághoz (durability) az alacsony intenzitású volumen kell.** Profi U23 kerékpárosoknál a VT1 ALATTI edzésidő korrelált a fáradt állapotú teljesítmény javulásával (r=0,43, p=0,018), és a polarizáltabb eloszlás felé mozdulás is a fáradt-teljesítmény későbbi javulásával járt [spragg-2022-durability-training B; milanovic-2015-hiit-meta A].
4. **A durability önálló, negyedik teljesítmény-dimenzió: 2 h heavy-intenzitású tekerés után a CP átlagosan ~10%-ot esik, egyéni szórással <1%–32% között** — ultrán ez a szórás dönt, nem a friss FTP [jones-2023-resilience C; clark-2019-cp-dynamics A]. Amatőröknél a „sikeresek" 20 perces teljesítménye 1000 kJ munka után csak 6,5%-ot esett, a kevésbé sikereseké 12,5%-ot [barsumyan-2025-durability-amateur A].
5. **A durability-romlást elsősorban az előzetes munka INTENZITÁSA hajtja, nem a mennyisége** — ultrán a Z1-Z2 versenytempó ezért is „védi" a teljesítményt, és az edzésben a hosszú Z1-Z2 munka a specifikus inger [sanchez-jimenez-2025-durability-sr A; spragg-2024-intensity A].
6. **Egyetlen terhelés-mutató (TSS, sRPE, TRIMP, kJ) önmagában nem jelzi előre az adaptációt: 10 félprofi kerékpáros 8 hetes blokkjában egyik mutató sem korrelált a friss/fáradt teljesítmény-javulással; a szénhidrát-oxidáció változása viszont az LT1 alatti volumennel függött össze** [voet-2025-durability-training B].
7. **Ultra-cél óraszám-horgonyok (edzői/versenyzői közlések):** 320+ km-es eseményre minimum 10–15 h/hét, 16–20 hét alatt felépítve [tatt-boundary-ultraguide C]; elit-közeli ultra-versenyzőnek 15–20 h/hét a „sweet spot" [towers-ultra-training C]; ugyanakkor egy amatőr TCR-teljesítő alapozása ~240 km (~9–11 h)/hét volt ~6 hónapon át — a CÉLBAÉRÉS a 8–12 h/hét sávból is reális [houston-tcr-training C; brayson-2019-tcr B].
8. **Edzett kerékpáros RCT-k tipikus vizsgált volumene 7,5–11,7 h/hét** — a sportélettani evidenciabázis nagy része tehát épp a célközönség óraszámán született, csak nem ultra-kimenettel [galan-rioja-2023-cyclist-tid-sr A].
9. **A terhelés-emelés biztonságos üteme: CTL-rámpa ~5–8 pont/hét a legtöbb sportolónak; 10 felett csak rövid ideig (≤1 hét)** [friel-ctl-ramp C]. A pihenőhetek kihagyása (2×7 hetes blokk regeneráció nélkül) versenyzői esettanulmányban közel krónikus fáradtsághoz vezetett [towers-ultra-training C].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q2):** (1) Kerékpáros dózis-válasz görbe (heti óra → többórás teljesítmény) prospektív vizsgálatból nem került elő; a Casado-adat futó és retrospektív [casado-2019-easyruns B]. Keresések: "training volume dose response cyclists performance hours per week", "durability cyclists training volume low-intensity". (2) A „mennyi óra kell TCR/PBP/1000 km teljesítéséhez" kérdésre csak n=1 versenyzői közlések és edzői keretszámok vannak [houston-tcr-training C; tatt-boundary-ultraguide C; towers-ultra-training C] — szisztematikus felmérés (pl. TCR-mezőny edzésóráiról) nincs. (3) A time-crunched (Carmichael-féle) programok saját, lektorált validálása ultra-távra hiányzik; a HIIT-helyettesítés bizonyítéka VO2max-ra szól [milanovic-2015-hiit-meta A]. (4) A durability edzhetőségére RCT nincs, csak megfigyelés [spragg-2022-durability-training B; voet-2025-durability-training B] és narratív hipotézis [jones-2023-resilience C].

**ELLENTMONDÁS (Q2):** A HIIT-meta szerint az intenzitás időhatékonyan pótolja a volument (VO2max-ra) [milanovic-2015-hiit-meta A], miközben a durability-irodalom szerint épp az LT1/VT1 alatti volumen az, ami a több-órás teljesítménymegtartással függ össze [spragg-2022-durability-training B; voet-2025-durability-training B; casado-2019-easyruns B]. Feloldás a modulban: a kevés órából élő ultrásnak mindkettő kell — minimális minőség a plafon (VO2max/FTP) tartására, és minden megmaradt óra Z1-Z2, mert a versenyspecifikus adaptáció (zsíranyagcsere, durability) volumen-függő; a hiányzó hétköznapi volument a hétvégi hosszú + back-to-back pótolja (Q3).

**KALKULÁTOR-PARAMÉTEREK (Q2) — terhelés-kalkulátor:**
- **TSS** = időtartam(h) × IF² × 100, ahol IF = NP/FTP (Coggan-keret; iparági sztenderd, lektorált validálás korlátos) [friel-ctl-ramp C; voet-2025-durability-training B — több mutató együttes használata ajánlott].
- **sRPE-terhelés** = időtartam (perc) × session-RPE (CR-10, 0–10) — eszköz nélküli alternatíva; ebből monotónia = napi terhelések átlaga/szórása, strain = heti terhelés × monotónia [foster-2001-srpe B].
- **CTL** = 42 napos, **ATL** = 7 napos exponenciálisan súlyozott TSS/nap átlag; **TSB** = CTL−ATL (PMC-modell). Rámpa-értékek: kezdő 3–5, haladó 5–8, rövid csúcsblokk ≤10 CTL-pont/hét [friel-ctl-ramp C].
- Heti mikro-struktúra: 3 hét progresszív terhelés (+10–15%/hét időtartamban) + 1 könnyebb hét [tatt-boundary-ultraguide C]; TRIMP/LuTRIMP pulzus-alapú alternatíva sRPE hiányában (Banister-elv, a voet-2025 vizsgálatban is használt mutató) [voet-2025-durability-training B].
- Többnapos esemény terhelés-becslése: a normál HETI edzésterhelés 2–3-szorosa órában/TSS-ben [rutberg-cts-multiday C].
- Figyelmeztetés a kalkulátorba: „egyetlen mutató nem jelzi előre az adaptációt — a TSS/CTL iránymutató, nem cél" [voet-2025-durability-training B].

---

## Q3 — A hosszú edzés, a back-to-back és a felkészülési gerinc

1. **Amit a 4–10 órás edzés ad, és a rövid nem: a versenyspecifikus fáradt-állapot maga.** A power-duration görbe lefelé tolódása (durability-teszt) tipikusan 1500–2000 kJ előzetes munka után mérhető — amatőrnek ez 2–3+ óra; a 20 perces teljesítmény már 1000 kJ után 6,5–12,5%-ot esik [spragg-2024-intensity A; barsumyan-2025-durability-amateur A; clark-2019-cp-dynamics A].
2. **A zsíranyagcsere-kapacitás (MFO ~0,53±0,16 g/perc edzetteknél, Fatmax ~56±8% VO2max) edzéssel nő, és a hosszú, alacsony intenzitású munka a fő ingere; Ironman-mezőnyben az MFO r=0,35-tel korrelált a versenyidővel** [maunder-2018-mfo B; maunder-2021-durability C]. Alacsony glikogénnel végzett edzés (train-low) meta-szinten javítja a zsíroxidációt, de teljesítmény-előnye nem bizonyított [gejl-2021-trainlow-meta A].
3. **A hosszú edzés nem-élettani hozama önálló indok: ülés-tűrés, táplálkozás-gyakorlás (a bél edzhető), felszerelés- és fejben-tartás — ezek csak többórás terhelésen gyakorolhatók** [jeukendrup-2017-trainingthegut C; rothschild-2021-ultracyclist B; apidura-ultra-training C].
4. **Back-to-back: közvetlen RCT nincs, az edzői konszenzus és az elit gyakorlat egybehangzó.** „Kötelező back-to-back edzésblokkokat építeni — a második-harmadik napi azonos szintű teljesítés képességét edzed" [rutberg-cts-multiday C]; „a hétvége a hosszú, back-to-back napoké" (Hammond) [apidura-ultra-training C]; „hétvégi back-to-back hosszú edzések a kumulatív fáradtság gyakorlására" [tatt-boundary-ultraguide C].
5. **A tömbösítés elve kontrollált bizonyítékkal bír (HIT-oldalon): 4 hetes blokk-periodizáció (1 hét 5 HIT-edzés + 3 könnyű hét) a hagyományos elosztásnál jobb: Wmax +4,6±3,7% (ES=1,34), 4 mM-teljesítmény +2,1±2,8% (ES=0,85), míg a tradicionális csoport nem javult** — a koncentrált inger + regeneráció minta a hosszú-napokra analógiaként vihető át [ronnestad-2014-block A].
6. **Éjszakai/alvásmegvonásos gyakorló edzés: az érv mellette a szubjektív fáradtság-kezelés gyakorlása, ellene az akut kockázat.** 36 óra alvásmegvonás a kimerülésig tartó időt átlag 11%-kal rövidítette (egyéni szórás <5%-tól 15–40%-ig), az RPE-t emelte, miközben a pulzus és a VO2 nem változott; a mikroalvás/baleseti kockázat éjjel nő — a modul ajánlása: éjszakai menetgyakorlás igen (világítás, navigáció, hideg), szándékos alvásmegvonásos edzés nem, azt a 400/600-as brevet „főpróbája" adja kontrollált keretben [martin-1981-sleep-rpe A; craven-2022-akut A; poussel-2015-utmb-sleep B; ridefar-sleepdep C].
7. **A brevet-sorozat (200-300-400-600) intézményesített progressziós gerinc: a PBP-nevezés feltétele a teljes Super Randonneur sorozat a versenyévben; hosszabb brevet helyettesíthet rövidebbet** — a 600-as egyben az első valódi alvás-stratégia-teszt [pbp-2027-rules C; brayson-2019-tcr B].
8. **A leghosszabb edzés hossza: az edzői ökölszabályok 10+ órás csúcs-edzésig progresszív építkezést adnak (4–6 órától), nem a versenytáv lemásolását.** „Tévhit, hogy hetente irdatlan távokat kell menni — néha igen" (Hammond); Ibbett a nagy esemény előtt ~1 hónappal 4 napos többnapos főpróbát tart; egy amatőr TCR-teljesítő leghosszabb egynapos edzése ~440 km (audax-dupla) volt [tatt-boundary-ultraguide C; apidura-ultra-training C; houston-tcr-training C].
9. **Tapering: 2 hét, exponenciálisan 41–60%-os volumencsökkentés, intenzitás és gyakoriság megtartásával (ES=0,72±0,36, p<0,001); intenzitás-csökkentés rontja a hatást (ES=0,33)** — ultrára fordítva: a hosszú edzések rövidülnek, a megszokott heti ritmus és a kevés minőség marad [bosquet-2007-taper-meta A]. Versenyzői gyakorlat: taper ~2–3 héttel a rajt előtt [houston-tcr-training C].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q3):** (1) Back-to-back hosszú napok adaptációs többletére nincs kontrollált vizsgálat állóképességi sportban (keresések: "consecutive days prolonged exercise training adaptation back-to-back", "block training long duration rides") — a bizonyíték edzői konszenzus + HIT-blokk-analógia [rutberg-cts-multiday C; ronnestad-2014-block A]. (2) A „leghosszabb edzés a versenytáv X%-a" szabályra semmilyen mért adat nincs, csak gyakorlat. (3) A 4–10 órás edzés dózis-válaszát (3 vs. 5 vs. 8 óra) senki nem hasonlította össze kontrolláltan; a zsíranyagcsere-érv indirekt [maunder-2018-mfo B; gejl-2021-trainlow-meta A]. (4) Az ülés-tűrés/nyereggél alkalmazkodás edzés-válaszáról nincs lektorált adat (csak sérülés-epidemiológia, más modul).

**ELLENTMONDÁS (Q3):** (1) Ibbett: „a csak-hosszú-lassú edzéstől csak lassan-sokáig menni leszel jó" [apidura-ultra-training C] vs. a durability-irodalom Z1-volumen-pártisága [spragg-2022-durability-training B] — feloldás: a hosszú Z1 a specifikus alap, de a fittségi plafont kevés minőség tartja (Q1-Q2 szintézissel egyező). (2) A tapering-meta az intenzitás megtartását írja elő [bosquet-2007-taper-meta A], ultrán viszont a „intenzitás" maga a hosszú edzés — a paraméterek átvitele értelmezést igényel, ultra-specifikus taper-vizsgálat nincs. (3) Az alvásmegvonásos gyakorlóedzést egyes versenyzők hasznosnak tartják [ridefar-sleepdep C], a laboradat szerint a kockázat/haszon arány rossz [craven-2022-akut A; martin-1981-sleep-rpe A].

**KALKULÁTOR-PARAMÉTEREK (Q3) — felkészülési ütemterv-generátor (visszafelé a versenydátumtól):**
- **Teljes felkészülési táv:** 16–20 hét (minimum), ~6 hónap tipikus amatőr gyakorlat [tatt-boundary-ultraguide C; houston-tcr-training C].
- **Fázisok visszafelé:** taper 2 hét (1000 km felett 2–3 hét), volumen −41–60%, intenzitás/gyakoriság marad [bosquet-2007-taper-meta A; houston-tcr-training C] ← specifikus fázis 4–6 hét: leghosszabb edzés + back-to-back hétvégék + többnapos főpróba (~4 nap, a rajt előtt ~4 héttel) [apidura-ultra-training C; rutberg-cts-multiday C] ← építés 6–8 hét: piramis→polarizáltabb minőség + hosszú edzés progresszió 4–6 h-ról 10+ h-ra [filipas-2022-pyr-pol A; tatt-boundary-ultraguide C] ← alap: ami marad, Z1-domináns, +10–15%/hét, minden 4. hét könnyű [tatt-boundary-ultraguide C; friel-ctl-ramp C].
- **Brevet-naptár mint gerinc:** 200 → 300 → 400 → 600 km növekvő sorrendben a specifikus fázisra illesztve (PBP-kvalifikációnál kötelező, más ultrára ajánlott váz); a 600-as = alvás-stratégia főpróba, legkésőbb ~4–6 héttel a célverseny előtt [pbp-2027-rules C; apidura-ultra-training C].
- **Leghosszabb edzés:** cél 10+ óra egyhuzamban legalább egyszer; többnapos versenyre inkább back-to-back (2×6–8 h) és egy 3–4 napos mini-túra, mint egyetlen extrém táv [tatt-boundary-ultraguide C; apidura-ultra-training C; rutberg-cts-multiday C].
- **Terhelés-plafon:** CTL-rámpa ≤5–8/hét; többnapos főpróba hete ≤ a heti átlagterhelés 2–3-szorosa [friel-ctl-ramp C; rutberg-cts-multiday C].

---

## Feltörekvő irányok
- **Durability/reziliencia mint edzés-cél:** a „negyedik dimenzió" keret [jones-2023-resilience C] nyomán várhatók az első edzés-intervenciós vizsgálatok (mit javít a fáradt-állapotú CP-t: volumen, train-low, hosszú edzés végi minőség); most csak megfigyelés van [spragg-2022-durability-training B; voet-2025-durability-training B].
- **TID-kutatás módszertani fordulat:** a session- vs. idő-alapú számolás és a polarizációs index standardizálása a Burnley–Foster vita után [burnley-2022-pol-debate C]; várható, hogy a „piramis vs. polarizált" kérdést fázis-szekvencia kérdésként vizsgálják tovább [filipas-2022-pyr-pol A].
- **Egyszámos terhelésmutatók leváltása:** többdimenziós (zónaidő + kJ + sRPE) terhelés-modellek a TSS helyett [voet-2025-durability-training B].
- **Hosszú edzés végi minőség ("fatigued intervals"):** elit gyakorlatban terjed, kontrollált adat még nincs (keresés: "intervals after prolonged low-intensity ride training study" — nem került elő RCT).

## Nem sikerült megnyitni
- journals.humankinetics.com – Voet 2025 cikkoldal (403) → helyette OpenAlex-rekord (számok onnan, korrelációs együtthatók nélkül).
- api.crossref.org – 10.1519/JSC.0000000000002618 és 10.1249/MSS.0000000000002869 (429 rate-limit) → helyette OpenAlex-rekordok.
- journals.lww.com (Rosenblat teljes szöveg), tandfonline.com (Spragg 2023 EJSS teljes szöveg) – nem próbált közvetlen fetch a ismert 403-blokk miatt; absztrakt-szintű adatok OpenAlexből.
- Rønnestad 2014: a VO2max-változás OpenAlex-rekonstrukciója bizonytalan volt („10 ± 12%"), ezért a VO2max-számot nem használtuk, csak a Wmax- és ES-értékeket.

## Csomag B

Q4: periodizáció ultrára · Q5: tapering · Q6: erősítés
Készült: 2026-09-24. Hivatkozás: [kulcs FOKOZAT]. Új kulcsok: data/raw/02-B-sources.yaml; a többi a data/sources.yaml meglévő tétele.

---

## Q4 — Periodizáció ultrára

1. **Azonos össz-terhelés mellett a periodizációs forma alig változtat az adaptáción.** 63 jól edzett kerékpáros (VO2peak 61,3±5,8 ml/kg/perc), 12 hét, 24 azonos össz-terhelésű intervall-edzés növekvő, csökkenő vagy vegyes HIT-elrendezésben: minden csoport 5–10%-ot javult teljesítményben és VO2peak-ben, a modellek között semmilyen adaptációs különbség nem volt (p>0,05), a reagálók/nem-reagálók eloszlása is azonos [sylta-2016-hit-periodization A].
2. **A blokk-periodizáció fölénye a meta-analízisben kicsi és bizonytalan.** 20 vizsgálat: VO2max SMD=0,40 (95% CI 0,02–0,79), Wmax SMD=0,28 (95% CI 0,01–0,54) a blokk javára — de az átlagos módszertani minőség nagyon alacsony (PEDro 3,7/10), és a szerzők egyike maga a fő blokk-kutató [molmen-2019-block-meta A].
3. **Rövid HIT-blokk edzett kerékpárosnál működhet.** 4 hetes ciklus: 5 HIT-edzés az 1. héten + 3 könnyű hét (n=10) vs. elosztott heti 2 HIT (n=9), azonos volumen: a blokk-csoportban csúcsteljesítmény +4,6±3,7%, 4 mmol/l-teljesítmény +2,1±2,8%, VO2max +10±12% (p<0,05; ES 1,34/0,85/0,71), a hagyományosban nincs szignifikáns változás [ronnestad-2014-block-cyclists A]. Munka melletti amatőrnek egy „HIT-hét + 3 nyugodt hét" logisztikailag is vonzó minta (n=19, 4 hét — óvatos extrapoláció).
4. **A fordított periodizáció nem jobb a többinél.** Szisztematikus áttekintés (11 vizsgálat, 200 sportoló — úszás, futás, erő, triatlon; kerékpáros nincs): „reverse periodization is no more effective than other forms of periodization"; úszó 100 m-en mindkét modell 1–5%, futásban 2000–5000 m-en mindkettő ~2,4% javulás [gonzalez-rave-2022-reverse A].
5. **A periodizáció-elmélet alapfeltevései maguk is vitatottak.** Kiely lektorált kritikája szerint a Selye-stresszmodellre épített, hét évtizedes feltevések „largely unchallenged and unchanged" — a merev séma helyett az élet-összterhelésre (munka, alvás) reagáló rugalmas tervezés indokolt [kiely-2018-periodization-critique C]; a modern konszenzus a periodizációt integráltan (edzés+regeneráció+táplálkozás+pszichés készségek) értelmezi [mujika-2018-integrated-periodization C].
6. **Többnapos ultrára az edzői gyakorlat fázisokat használ, de a csúcsterhelést köti időponthoz: 4–6 héttel a rajt előtt.** Grandgeorge (TABR/RAAM-indulók edzője): a terhelés-csúcs a verseny előtt 4–6 héttel (30–42 nap adaptációs idő), 3+1 vagy 2+1 hetes mikrociklusok, heti 6 edzésnap + 1 pihenőnap [grandgeorge-t2m-season C]. 12/24 órás versenyre: ~4 hónap alapozás + ~2 hónap intenzitás-fázis + verseny-specifikus csúcs/taper [vanderlinden-wuca-1224 C].
7. **A felkészülés volumene tág sávban szór: 6 hónap alatt 2 000–20 000+ km.** Bikepacking-versenyre a tipikus tartomány „between 2,000 km and 20,000+ km in the six months leading up to the event" (Allegaert: 20 000+ km 7 hónap alatt); munka mellett heti helyett havi távcélok javasoltak [white-ridefar-training-plan C]. Viszonyítás: egy TCR-t teljesítő jól edzett amatőr versenyteljesítménye ~1,5 W/kg, 109±12 W napi átlag volt [brayson-2019-tcr B] — a cél-intenzitás alacsony, a korlát a tartósság.
8. **Két fő verseny egy szezonban: 6–8 hét regenerációs köz a versenyzői gyakorlat.** „Most of us need approximately six to eight weeks to recover completely" — ebből évi 2–3 fő verseny fér bele [vanderlinden-wuca-1224 C]. Lektorált vizsgálat ultrakerékpáros kettős csúcsformáról nincs (lásd HIÁNYZÓ).
9. **A brevet-naptár beépített táv-progressziót ad (200→300→400→600 km), de önmagában nem edzésterv.** A PBP-kvalifikációs Super Randonneur sorozat november–június 30. között teljesítendő; edzői tanács: a 600-ast nem szabad késő tavaszra hagyni; „Completing 200/300/400/600km brevets proves distances possible" — a többnapos versenyre külön felkészülés kell [tatt-boundary-pbp C].
10. **A minimális felkészülési idő tapasztalati becslés: előélettől függően „2 héttől 2 évig", tipikusan ~6 hónap dedikált edzés** [white-ridefar-training-plan C]. Lektorált küszöb-adat (mennyi edzés alatt nő meredeken a feladás/sérülés-kockázat) nincs.

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q4):**
- Periodizációs RCT többnapos ultrakerékpáros kimenettel nem létezik (keresve: "periodization ultra-endurance cycling RCT", "block periodization ultracycling", "training characteristics bikepacking race finishers"). Minden A-fokozatú adat ≤12 hetes, labor-kimenetű.
- A 16–24 hetes felkészülés szerkezetére kizárólag edzői/versenyzői forrás van [grandgeorge-t2m-season C; vanderlinden-wuca-1224 C; white-ridefar-training-plan C].
- Kettős csúcsforma (két fő verseny) ultra-kontextusban méretlen; a 6–8 hetes köz egyetlen versenyző tapasztalata.
- A „minimális hatásos felkészülés" (óra/km küszöb a teljesítéshez) publikált finisher-prediktor vizsgálattal nem támasztott; PBP/TCR-finisher edzés-jellemzőkről nem találtam lektorált tanulmányt (keresve: "Paris-Brest-Paris randonneurs training characteristics finishers study").

**ELLENTMONDÁS (Q4):**
- Blokk vs. hagyományos: a Rønnestad-vizsgálatok jelentős fölényt mutatnak [ronnestad-2014-block-cyclists A], a meta-analízis csak kis, bizonytalan hatást gyenge minőségű irodalomból [molmen-2019-block-meta A], a legnagyobb, terhelés-kiegyenlített RCT pedig semmilyen forma-hatást nem talál [sylta-2016-hit-periodization A]. Óvatos szintézis: az összvolumen és a konzisztencia az elsődleges, a forma másodlagos.
- „4–6 óránál hosszabb edzés nem ad pluszt" [white-ridefar-training-plan C] vs. a durability-irodalom, amely szerint a nagy edzésvolumen és a hosszú, fáradt állapotban végzett munka a fáradt-állapotbeli teljesítmény (ΔCP) fő meghatározója [spragg-2023-durability B; sanchez-jimenez-2025-durability-sr A] — a hosszú edzés hasznának kérdése nyitott.

**KALKULÁTOR-PARAMÉTEREK (ütemterv-generátor, Q4):**
- Visszafelé a versenydátumtól: taper 1–2 hét (többnaposnál 2–3 hét kezdete) [mujika-2003-taper-bases C; grandgeorge-t2m-season C; white-ridefar-training-plan C]; terhelés-csúcs a rajt előtt 4–6 héttel [grandgeorge-t2m-season C]; specifikus fázis (leghosszabb edzés/back-to-back, éjszakai/felszerelés-teszt) a rajt előtti 3–8. hét; építés: 2+1 vagy 3+1 hetes mikrociklusok; a maradék idő alapozás (min. ~8 hét, ha van) [grandgeorge-t2m-season C; vanderlinden-wuca-1224 C].
- 16 hetes minta: 6 hét alap + 6 hét építés + 2–3 hét specifikus csúcs + 1–2 hét taper; 24 hetesnél az alap nyúlik (10–12 hét). (Edzői keret-szintézis, C-fokozatú bemenetekből — a modulban „az edződdel egyeztetve" keretként.)
- Brevet-naptár: 200→300→400→600 km, 2–6 hetes közökkel, a 600-as legkésőbb ~6 héttel a fő verseny előtt (egyben leghosszabb főpróba); bukott kísérletre tartalék-időt hagyni [tatt-boundary-pbp C].
- Kísérős/24 órás versenyre: leghosszabb edzés = céltáv ~75%-a, 2 héttel a rajt előtt [vanderlinden-wuca-1224 C]; többnapos önellátóra ez NEM alkalmazandó — ott a leghosszabb blokk tipikusan 1–2 napos back-to-back főpróba a 3–6. héten a rajt előtt [white-ridefar-training-plan C; grandgeorge-t2m-season C].

---

## Q5 — Tapering

1. **A meta-analízis optimuma: 2 hét, exponenciális 41–60%-os volumencsökkentés, intenzitás és gyakoriság megtartva.** 27 beválogatott vizsgálat: ez a kombináció adta a legnagyobb hatást (össz-ES 0,72±0,36, p<0,001); intenzitás-megtartással ES 0,59±0,33; csak gyakoriság-csökkentés ES 0,35±0,17 [bosquet-2007-taper-meta A].
2. **A klasszikus taper-keret: 4–28 nap, volumen −60–90% (a taper végére), gyakoriság legfeljebb −20%, progresszív > lépcsős; tipikus teljesítménynyereség ~3% (0,5–6,0%)** [mujika-2003-taper-bases C].
3. **Ultra-adaptáció (edzői gyakorlat): 7–10 nap taper, a volumen erős csökkentésével, némi intenzitás megtartásával; az utolsó héten formát építeni már nem lehet.** „No matter where your conditioning is with one week to go, that's what you have to work with." [rutberg-cts-taper C] Többnapos ultrára a taper 2–3 héttel a rajt előtt indul, csökkentett volumen + megtartott/emelt intenzitás mellett [grandgeorge-t2m-season C].
4. **Az utolsó hosszú edzés időzítése: kísérős/fix-körös versenynél a leghosszabb (céltáv ~75%-a) 2 héttel a rajt előtt** [vanderlinden-wuca-1224 C]; **hagyományos versenyhétben szerdai 3–4 órás „szuperkompenzációs" tekerés** üríti a raktárakat a feltöltés előtt [rutberg-cts-taper C]; bikepacking-versenynél a szervizt/logisztikát 2–3 héttel a rajt előtt le kell zárni, a taper 1–2 hét, alvás-prioritással [white-ridefar-training-plan C].
5. **A taper alatti súlygyarapodás glikogén+víz, nem zsír.** 72 órás, 12 g/kg/nap szénhidrát-feltöltés után az izomglikogén 169,4±55,9 mmol/kg-ra nőtt (p<0,001), a teljes testvíz 39,3±3,2→40,2±3,0 kg (+~0,9 kg, p<0,05), a többlet intracelluláris és főleg a lábakban [shiose-2016-carboload-water A] — kapcsolat a 03-as modul feltöltési protokolljával; a rajt-előtti +1–2 kg normális és funkcionális.
6. **Kell-e klasszikus taper alacsony intenzitású többnapos versenyre? Közvetlen bizonyíték nincs; a mechanizmus-érv gyengébb hatást valószínűsít, a gyakorlat mégis taperel.** A taper-nyereség (~3%) rövid, intenzív erőfeszítéseken mért [bosquet-2007-taper-meta A; mujika-2003-taper-bases C]; többnapos, FTP 50–70%-án zajló versenyen a rajt-frissesség fő hozadéka inkább az alvás-tartalék, a glikogén-telítettség és a sérülés-/betegség-kockázat csökkentése — minden ultra-edzői forrás 1–3 hetes tapert ír elő [grandgeorge-t2m-season C; white-ridefar-training-plan C; rutberg-cts-taper C].
7. **A taper az integrált periodizáció része: a táplálkozást (feltöltés) és a pszichés felkészülést is a záró fázishoz kell igazítani** [mujika-2018-integrated-periodization C].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q5):**
- Nincs egyetlen kontrollált taper-vizsgálat sem többnapos ultra-állóképességi kimenettel (keresve: "taper ultraendurance cycling study", "tapering multiday race performance"); a 0,72-es ES rövidebb (perc–óra) teljesítményre vonatkozik, átvitele a 08-as modul intenzitás-világára (1,5–2,1 W/kg) igazolatlan.
- Az „utolsó hosszú edzés" időzítésére csak edzői/versenyzői forrás van; a TCR/RAAM-mezőny tényleges utolsó-heti edzésadatai publikálatlanok (a meglévő versenyzői források a verseny alatti adatokat közlik [brayson-2019-tcr B; rothschild-2021-ultracyclist B; hyldahl-2024-tourdivide B]).
- A taper alatti súlygyarapodás mértéke ultrás terep-adattal nem dokumentált; a Shiose-adat labor, n=8.

**ELLENTMONDÁS (Q5):**
- Volumencsökkentés mértéke: Bosquet-optimum 41–60% [bosquet-2007-taper-meta A] vs. Mujika-Padilla 60–90% [mujika-2003-taper-bases C] — az eltérés részben definíciós (átlagos vs. taper-végi csökkentés), a modulban 40–60%-os átlagos csökkentés a védhető ajánlás.
- Taper-hossz: 7–10 nap [rutberg-cts-taper C] vs. 2 hét [bosquet-2007-taper-meta A] vs. 2–3 hét többnapos ultrára [grandgeorge-t2m-season C] — hosszabb verseny → hosszabb, de enyhébb lejtésű taper a gyakorlat, kontrollált adat nélkül.

**KALKULÁTOR-PARAMÉTEREK (tapering, Q5):**
- Hossz: 10–14 nap (alap), többnapos önellátó versenynél 14–21 nap, enyhébb lejtéssel [bosquet-2007-taper-meta A; grandgeorge-t2m-season C; rutberg-cts-taper C].
- Volumen: átlagosan −40–60% a normál héthez képest, exponenciális/progresszív lefutással (utolsó hét: −50–70%) [bosquet-2007-taper-meta A; mujika-2003-taper-bases C].
- Intenzitás: megtartani (heti 1–2 rövid, élénk edzés marad); gyakoriság: legfeljebb −20% (edzésnapok száma nagyjából marad) [bosquet-2007-taper-meta A; mujika-2003-taper-bases C].
- Utolsó hosszú edzés: rajt előtt 10–14 nappal (többnapos self-supported), ill. versenyhét szerdáján 3–4 óra könnyű-tempós, feltöltés előtt [vanderlinden-wuca-1224 C; rutberg-cts-taper C].
- Várható hatás: +0,5–6% (tipikus ~3%) rövid teljesítményen — ultrára óvatos kommunikáció [mujika-2003-taper-bases C]; +~1 kg testtömeg a feltöltéstől: glikogén+víz [shiose-2016-carboload-water A].

---

## Q6 — Erősítés

1. **A friss kerékpáros-meta: a nehéz erősítés (≥80% 1RM, ≥3 hét) javítja a VO2max-ot (ES=0,353, p=0,012), az anaerob kapacitást (ES=0,560, p=0,024) és a teljesítményt (ES=0,463, p=0,016); a küszöb/gazdaságosság-mutatókat nem (p≥0,263).** 17 kontrollált vizsgálat, n=262 (60 nő); a bizonyosság alacsony [llanos-lagos-2025-hst-cyclists-meta A].
2. **Ultra-kulcsadat: az erősítés a FÁRADT állapotbeli teljesítményt javítja.** 12 hét heti 2 nehéz láberősítés után a 185 perc szubmaximális tekerést követő 5 perces all-out 371±9→400±13 W-ra nőtt (~+8%, p<0,05; kontroll: nincs változás), a hosszú tekerés alatt kisebb VO2, pulzus, laktát és RPE [ronnestad-2011-strength-185min A] — a durability-irodalom edzés-oldali párja [spragg-2023-durability B].
3. **Nőknél is működik: 11 hét erő+állóképesség jobb 40 perces teljesítményt, jobb frakcionális VO2max-kihasználást és gazdaságosságot adott, IIAX-IIX→IIA rost-átalakulással** (n=19; teljesítményjavulás vs. rost-átalakulás r=-0,63, vs. izomkeresztmetszet r=0,73) [vikmoen-2016-female-cyclists A].
4. **Az interferencia-félelem alaptalan: az egyidejű aerob+erő edzés a maximális erőt (SMD=-0,06, p=0,446) és a hipertrófiát (SMD=-0,01, p=0,919) nem rontja; csak az explozív erő csökken kissé (SMD=-0,28, p=0,007), főleg azonos edzésegységben** — külön napra vagy ≥3 órára szétválasztani [schumann-2022-concurrent-meta A].
5. **Dózis a felkészülésben: heti 2 nehéz alkalom; szezonban heti 1 fenntartó alkalom elég.** 12 hét heti 2 + 13 hét heti 1: a comb-keresztmetszet és erő megmaradt, a Wmax és a 40 perces all-out javult (p<0,05); a csak-állóképeséges kontroll stagnált (2×6 fő) [ronnestad-2010-inseason-maintenance A; ronnestad-2014-strength-review C].
6. **Minimális hatásos dózis időhiányban: heti ≥4 sorozat izomcsoportonként, 6–15 RM, több-ízületes gyakorlatokkal; a heti össz-volumen számít, nem az elosztás** — szuperszettekkel egy 30–40 perces heti alkalomba sűríthető [iversen-2021-notimetolift C].
7. **A törzsfáradás mérhetően rontja a hajtás-mechanikát: 32 perces törzs-fárasztás után a térd frontális mozgása +54,3% (15,1°→23,3°), a boka szagittális mozgása +48,3%** (n=15 versenyző kerékpáros; pedálerő változatlan) [abt-2007-core-cycling B] — többnapos nyeregidő mellett a törzs-állóképesség a parazita-mozgás és a túlterheléses panaszok elleni edzés-oldali védelem.
8. **Nyak (Shermer-nyak) megelőzésére nincs mért protokoll, a versenyzői-fizioterapeutás konszenzus: nyak-fej mozgásminta tanulása (fej-behúzás, áll-betűrés), mikro-szünetek „az első mérföldtől", pozíció-gyakorlás edzésen, kényelmi bike-fit** („Raise your pads and widen them… comfort is king") [dotwatcher-shermers-roundtable C]; a TCR-esettanulmány a többnapos statikus tartás terheléseit dokumentálja [brayson-2019-tcr B].
9. **Az erősítés helye a szezonban: a nehéz, fejlesztő blokk az alapozásra/építésre; a versenyidőszakban heti 1 fenntartó; a taperben az utolsó nehéz alkalom ~7–10 nappal a rajt előtt** (a fenntartó-vizsgálat + taper-elvek szintézise) [ronnestad-2010-inseason-maintenance A; ronnestad-2014-strength-review C; mujika-2003-taper-bases C].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q6):**
- Erősítés hatása TÖBBNAPOS ultra-teljesítményre méretlen; minden A-adat percek–órák teljesítményén nyugszik (leghosszabb: 185 perc + 5 perc [ronnestad-2011-strength-185min A]).
- Nyak-, kéz- (ulnáris/medián), ülőgumó-specifikus erősítő/tűrés-edzés kontrollált vizsgálata ultrakerékpárosokon nem létezik (keresve: "Shermer's neck prevention neck strengthening ultracycling RAAM", "handlebar palsy prevention training", "saddle pressure tolerance training") — csak tapasztalati ajánlás [dotwatcher-shermers-roundtable C]; a klinikai kép a 07-es modul területe.
- Kar-comb (felsőtest-alsótest) aszimmetria és bikepacking-terhelés kapcsolata: nem találtam vizsgálatot (keresve: "cycling upper body lower body strength imbalance ultra-endurance bikepacking asymmetry study" — a találatok bal-jobb pedálozás-aszimmetriáról vagy ülő életmódúak felsőtest-erejéről szólnak). A felsőtest-edzés ultra-indoklása közvetett (törzs/nyak-tartás, rázkódás-tűrés).
- A gazdaságosság-javulás kerékpárnál bizonytalan: a narratív irodalom állítja [ronnestad-2014-strength-review C], a 2025-ös meta nem erősíti meg (steady-state kimenetek p≥0,263) [llanos-lagos-2025-hst-cyclists-meta A].

**ELLENTMONDÁS (Q6):**
- Kerékpáros gazdaságosság: „heavy strength training shows superior benefits for cycling economy" [ronnestad-2014-strength-review C] vs. „No significant changes occurred in metabolic steady state (all p ≥ 0.263)" [llanos-lagos-2025-hst-cyclists-meta A]. A modulban: a fő haszon nem a gazdaságosság, hanem az elfáradás-késleltetés és a fáradt-állapotú teljesítmény [ronnestad-2011-strength-185min A].
- Minimális dózis: általános ajánlás heti ≥4 sorozat/izomcsoport [iversen-2021-notimetolift C] vs. a kerékpáros vizsgálatok heti 2×(4 gyakorlat×3 sorozat) protokolljai [ronnestad-2011-strength-185min A] — a „mennyi a minimum ultrásnak" pontos határa méretlen.

**KALKULÁTOR-PARAMÉTEREK (minimál-protokoll, Q6):**
- Gyakorlat-kategóriák: 1) csípő/térd-domináns több-ízületes (guggolás/lábtolás/kitörés), 2) csípőfeszítő-lánc (felhúzás-variáns/híd), 3) törzs anti-mozgás (plank-variánsok, oldaltámasz — a törzsfáradás-adat indoklásával [abt-2007-core-cycling B]), 4) húzó + nyak-váll tartóizmok (evezés, lapocka-munka; nyak-mozgásminta [dotwatcher-shermers-roundtable C]).
- Heti dózis felkészülésben: 2 alkalom, gyakorlatonként 3 sorozat, 4–10 RM (nehéz), teljes pihenőkkel [ronnestad-2011-strength-185min A; ronnestad-2014-strength-review C]; időhiányban: 1 alkalom/hét, izomcsoportonként ≥4 sorozat, 6–15 RM, szuperszettekkel ~30–40 perc [iversen-2021-notimetolift C].
- Szezonban: heti 1 fenntartó alkalom (a felkészülési terhelés ~felével is őrzi az erőt) [ronnestad-2010-inseason-maintenance A].
- Időzítés: állóképességi edzéstől külön napon vagy ≥3 óra távolságra (explozív-erő védelme) [schumann-2022-concurrent-meta A]; utolsó nehéz alkalom ~7–10 nappal a rajt előtt (taper-elv, C-szintű szintézis).

---

## Feltörekvő irányok
- **Durability mint edzés-cél:** a fáradt-állapotú kritikus teljesítmény (ΔCP) és meghatározói (volumen, intenzitás-eloszlás, zsír-oxidáció) körüli irodalom gyorsan nő [spragg-2023-durability B; sanchez-jimenez-2025-durability-sr A; evans-2025-durability-domain, hunter-2025-durability-methods a meglévő tárban] — a periodizáció-kérdést valószínűleg újrakeretezi („mennyi hosszú, fáradt munka kell").
- **Erősítés×durability:** a ronnestad-2011-strength-185min logikájának kiterjesztése többórás/többnapos kimenetekre — közvetlen ultra-vizsgálat még nincs.
- **Rugalmas (élet-terheléshez igazított) periodizáció** a Kiely-kritika nyomán: HRV-/készenlét-vezérelt tervezés amatőröknél (kapcsolódás: bellenger-2016-hrv-meta a meglévő tárban) — ultrás validáció hiányzik.
- **A 2025-ös kerékpáros erő-meta** [llanos-lagos-2025-hst-cyclists-meta A] a gazdaságosság-narratíva felülvizsgálatát jelzi; várható további, mechanizmus-tisztázó munka.

## Nem sikerült megnyitni
- journals.physiology.org (Shiose 2016 teljes szöveg) — 403; OpenAlex-absztraktból dolgoztam.
- coachpav.com (PBP-felkészülés) — 401; helyette boundarycycle.coach.
- pmc.ncbi.nlm.nih.gov (Llanos-Lagos 2025 teljes szöveg) — nem próbáltam a rendszeres 403 miatt; OpenAlex-absztrakt.
- api.crossref.org — egyszeri 429 (Rønnestad 2012/2014 blokk-cikk); OpenAlex-en pótolva.
- sportsmedicine-open.springeropen.com — cookie-átirányítás; link.springer.com-on megnyitva.

## Csomag C

Q7 (terhelésmutatók), Q8 (HRV és készenlét), Q9 (túledzés és betegség). Készült: 2026-09-24.
Fokozat: A/B/C/D a forrástár szerint. Új kulcsok: 02-C-sources.yaml; meglévők: data/sources.yaml.

---

## Q7 — Terhelésmutatók: TSS/IF/NP, CTL/ATL/TSB, sRPE, TRIMP, ramp-rate, ACWR

1. **A TSS-skála horgonya definíció szerint: 1 óra FTP-n = 100 pont, és óránként soha nem szerezhető 100-nál több.** A TSS = (idő_s × NP × IF)/(FTP × 3600) × 100, ahol IF = NP/FTP; 2 óra ~50 TSS/óra intenzitáson = 100 pont. [trainingpeaks-tss-explainer C]
2. **A PMC-modell (CTL/ATL/TSB) a Banister-féle impulzus-válasz modell leegyszerűsítése: a teljesítmény egy lassú "fittség" (~42 napos) és egy gyors "fáradtság" (~7 napos) exponenciális komponens különbsége.** A modell jól illeszthető egyéni adatokra, de az élettant absztrahálja, és az időállandók populációs átlagok — előrejelző ereje egyéni kalibrálás nélkül gyenge. [clarke-2013-banister-model C]
3. **A session-RPE (edzésidő perc × CR-10 RPE, 30 perccel az edzés után) teljesítménymérő és pulzusmérő nélkül is konzisztens terhelésmutató: a pulzuszóna-alapú pontszámmal „highly consistent" kapcsolatot adott, mozgásformától függetlenül.** [foster-2001-session-rpe A]
4. **Versenykerékpárosoknál a TSS és a jól kalibrált TRIMP-változatok hasonlóan követik az adaptációt: 10 hét alatt a terhelésmutatók és a fittségváltozás korrelációja r=0,54–0,81; a 8 perces időfutam-javulással iTRIMP r=0,81, TSS r=0,75, luTRIMP r=0,70 (n=15).** A "gyári" Banister/Edwards-TRIMP gyengébb — az egyéni kalibrálás (friss FTP, egyéni HR-laktát görbe) többet ér, mint a mutató márkája. [sanders-2017-load-cyclists B]
5. **Ramp-rate ökölszabály (edzői): heti 5–8 CTL-pont emelkedés „a legtöbbeknek megfelelő"; heti 10+ pont csak kivételes sportolóknak, legfeljebb ~1 hétig.** Nem validált vizsgálat, de a gyakorlatban legelterjedtebb számsáv. [friel-ramp-rate C]
6. **Az ACWR-koncepció alapja: a magas krónikus terhelés véd, a sérülést/megbetegedést a terhelés hirtelen megugrása hajtja; a javasolt „édes zóna" ~0,8–1,3, 1,5 felett emelkedő kockázat.** Csapatsport-adatokból származik, kerékpáros validáció nincs. [gabbett-2016-paradox C]
7. **Az ACWR módszertani kritikája: oksági bizonyíték nincs („no studies have even tried to estimate causal effects properly"), az arányképzés zajt és statisztikai műtermékeket ad, az édes zóna ábrája hibás.** A konkrét számküszöb nem védhető; a megőrzendő elv csak a fokozatos progresszió. [impellizzeri-2020-acwr C]
8. **Hol csal a TSS ultrás edzésen:** (a) az IF²-alapú súlyozás a hosszú Z1–Z2 munkát „olcsónak" árazza (IF 0,60 → 36 TSS/h), miközben a 6+ órás edzés valós élettani költsége (glikogénürülés, tartós fáradtság-ellenállás romlása) nem-lineárisan nő — a durability-irodalom szerint ~1500–2000 kJ munka után a küszöbök és a hatásfok mérhetően romlanak [spragg-2023-durability A; maunder-2021-durability C]; (b) az NP a lökésszerű terepen (hegyi, gravel) felfelé torzít, hosszú, egyenletes ultrán viszont az átlaghoz simul; (c) többnapos eseményen a napi 300–500 TSS a PMC-ben irreális CTL-ugrást generál, amit a modell 1 dimenziós fáradtságkomponense nem kezel. [trainingpeaks-tss-explainer C; clarke-2013-banister-model C]
9. **A session-RPE hosszú edzésen a végállapotot súlyozza (recency-torzítás), alváshiány mellett pedig az RPE maga is felfelé csal: 36 óra alvásmegvonás után ugyanaz a terhelés szignifikánsan nagyobb érzett erőkifejtést ad változatlan pulzus és VO2 mellett.** [martin-1981-sleep-rpe A; foster-2001-session-rpe A]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q7)
- Nincs publikált vizsgálat, amely a TSS/CTL-modellt 6 óránál hosszabb edzéseken vagy többnapos ultrakerékpáros terhelésen validálta volna (keresések: "training stress score validation ultra-endurance", "performance manager chronic training load validity cycling").
- A heti 5–8 pontos ramp-rate sávra nincs lektorált validáció — tisztán edzői heurisztika [friel-ramp-rate C].
- sRPE-szorzók nagyon hosszú (>6 h) alacsony intenzitású edzésre: nincs kalibrációs adat; a Foster-módszert jellemzően ≤2 órás edzéseken validálták.

### ELLENTMONDÁS (Q7)
- **Gabbett vs. Impellizzeri:** az ACWR mint sérülés-előrejelző „kritikus prediktor" [gabbett-2016-paradox C] vs. „nem oksági, statisztikai műtermék, elégtelen bizonyíték" [impellizzeri-2020-acwr C]. Az IOC 2016-os konszenzusa még ajánlotta az ACWR-monitorozást [schwellnus-2016-ioc-illness A] — a 2020 utáni módszertani irodalom visszavonulót fújt. Tankönyvi kezelés: az elv (ne ugorj hirtelen) marad, a számsáv nem tanítható tényként.
- **TSS vs. TRIMP:** Sanders-nél a TSS (külső terhelés) és az iTRIMP (belső) egyaránt erős, de a legjobb az individualizált belső mutató — miközben a gyakorlatban a legelterjedtebb (sima TSS) épp a legkevésbé egyénre szabott.

### KALKULÁTOR-PARAMÉTEREK (terhelés-kalkulátor)
- **Képletek:** IF = NP/FTP; TSS = t_óra × IF² × 100 (ekvivalens a hivatalos képlettel); hTSS/TRIMP alternatíva pulzusból; sRPE-terhelés = perc × CR-10 (0–10) érték [foster-2001-session-rpe A; trainingpeaks-tss-explainer C].
- **TSS/óra tipikus sávok zónánként (IF²×100 alapján, Coggan-zónák):** Z1 regeneráló (IF ~0,50–0,55) ≈ 25–30 TSS/h; Z2 állóképesség (IF 0,56–0,75) ≈ 31–56 TSS/h — tipikus ultra-alapozó 40–55 TSS/h; Z3 tempó (IF 0,76–0,90) ≈ 58–81 TSS/h; Z4 küszöb (IF 0,91–1,05) ≈ 83–110 → plafon 100 TSS/h; ultraverseny-intenzitás (FTP 50–70%-a) ≈ 25–49 TSS/h. [trainingpeaks-tss-explainer C — a plafon; a sávok a képlet determinisztikus következményei]
- **sRPE-szorzók (CR-10):** könnyű 2–3, közepes 4–5, kemény 6–7, nagyon kemény 8–9, maximális 10; heti terhelés = Σ(perc × RPE). [foster-2001-session-rpe A]
- **CTL/ATL/TSB:** CTL = 42 napos, ATL = 7 napos exponenciálisan súlyozott TSS-átlag; TSB = tegnapi CTL − tegnapi ATL. [clarke-2013-banister-model C]
- **Biztonságos rámpa:** alap heti +3–5 CTL-pont (munka melletti amatőr), agresszív +5–8, plafon +10 legfeljebb 1 hétig, utána regeneráló hét. [friel-ramp-rate C — edzői heurisztika, jelöld ekként]
- **Amatőr referenciasáv:** heti 6–15 óra, zömmel Z2 → heti ~300–700 TSS, fenntartható CTL ~45–90.

---

## Q8 — HRV és készenlét

1. **Kerékpáros RCT (n=17, 8 hét): a HRV-vezérelt csoport javult (csúcsteljesítmény +5,1%, küszöbteljesítmény +13,9%, 40 perces időfutam +7,3%), az előre írt terv szerint edző kontroll nem javult szignifikánsan.** [javaloyes-2019-hrv-cycling A]
2. **Futó RCT (n=40, 8 hét): a HRV-csoport kevesebb intenzív edzéssel (13,2±6,0 vs. 17,7±2,5) többet javult 3000 m-en (+2,1±2,0%, p=0,004 vs. +1,1±2,7%, p=0,118).** A haszon a kemény napok jobb időzítése, nem a több munka. [vesterinen-2016-hrv-rct A]
3. **Meta-analízis (8 RCT, n=190): csoportszinten NINCS szignifikáns különbség HRV-vezérelt és előre írt edzés között — VO2max MD=0,96 ml/kg/perc (95% CI −1,11–3,03), Wmax SMD=0,06 (−0,26–0,38), aerob teljesítmény SMD=0,14 (−0,22–0,51).** A HRV-vezérlés "nem rosszabb, néha jobb, sosem káros" összképet ad. [medellin-2020-hrv-meta A]
4. **Mérési protokoll: rMSSD, reggel ébredés után, azonos testhelyzetben (fekvő/ülő), és NAPI érték helyett 7 napos gördülő átlag — a napi rMSSD zaja miatt csak az átlagolt trend értelmezhető.** [plews-2013-hrv-monitoring C]
5. **Mit jelez valósan és mit nem (n=28 175 felhasználó, 9 millió mérés): a betegség (HR +6%, rMSSD −10%) és a sok alkohol (HR +6%, rMSSD −12%) nagyobb kilengést okoz, mint maga az edzés (HR 1,3%, rMSSD 4,6%); a menstruációs fázis is szisztematikusan mozgatja (rMSSD 3,2%).** A HRV érzékeny, de nem specifikus: alacsony érték először életmód-okot jelent, nem edzésparancsot. [altini-2021-hrv-freeliving B]
6. **A paraszimpatikus túlsúly csapdája: meta-analízis szerint a nyugalmi rMSSD túlterhelésnél is inkább NŐ (SMD 0,26), mint csökken — a magas HRV tehát nem mindig „jó jel", és a nyugalmi HRV alig különbözteti meg a pozitív adaptációt a túlterheléstől.** Elitben ismert a "HRV-telítődés" is (csökkenő HRV csökkenő nyugalmi pulzus mellett, ami nem fáradtság). [bellenger-2016-hrv-meta A; plews-2013-hrv-monitoring C]
7. **Wearable-validitás eszközfüggő: EKG-referenciával a HRV4Training app (rMSSD MAPE 4,10%, CCC 0,98) és az Oura gyűrű (6,84%, CCC 0,91) pontos, a kamera-alapú CameraHRV használhatatlan (MAPE 112%, CCC 0,04).** Abszolút értékek eszközök közt nem összevethetők — csak saját eszközön mért saját trend számít. [stone-2021-wearable-validity B]
8. **Többnapos verseny alatt a reggeli HRV nem használható a megszokott módon: amatőröknél már 3 napos szakaszverseny után sem tér vissza az autonóm egyensúly 24 óra alatt** [swart-2023-mtb-hrv B], **míg elit nőknél napi teljes alvás mellett a fáradtság nem halmozódott, és a HRV a verseny után 1 héttel állt vissza** [barrero-2019-tdf-hrv B].

### DÖNTÉSI SZABÁLYOK (HRV-alapú edzésmódosítás — a modul szövegébe)
- 7 napos gördülő rMSSD-átlag a saját normálsávban (pl. átlag ± legkisebb érdemi változás) → terv szerint edzhetsz, az aznapi egyszeri rossz érték önmagában nem ír felül semmit [plews-2013-hrv-monitoring C; javaloyes-2019-hrv-cycling A].
- Gördülő átlag a sáv alatt → az intenzív edzést cseréld Z1–Z2-re vagy pihenőre; a volumen mehet, az intenzitás nem [vesterinen-2016-hrv-rct A].
- Egyedi mélypont + gyanús kontextus (alkohol, kezdődő torokfájás, rossz éjszaka, nagy munkahelyi stressz) → először az okot kezeld; a HRV itt tünetjelző, nem edzésvezérlő [altini-2021-hrv-freeliving B].
- Szokatlanul MAGAS HRV nagy terhelésblokk közben + romló teljesítmény/hangulat → paraszimpatikus túlsúly gyanúja, ez is túlterhelés-jel lehet [bellenger-2016-hrv-meta A].
- HRV-eszköz nélkül: reggeli nyugalmi pulzus + fáradtság/készenlét-kérdőív hasonló döntéstámogatást ad [tenhaaf-2017-for-prediction B].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q8)
- Minden HRV-vezérelt RCT rövid (4–15 hét) és küszöb/VO2max-kimenetű; ultratáv-teljesítményre (>4 h) vagy nagy volumenű Z2-blokkokra HRV-vezérlést senki nem tesztelt (keresések: "HRV-guided training ultra-endurance", "heart rate variability guided long slow distance").
- Whoop és Garmin readiness-pontszámok (összetett, zárt algoritmusok) prediktív validitása edzésadaptációra: nincs független RCT; a Stone-vizsgálat Whoopot/Garmint nem is mért.
- Nő-specifikus HRV-vezérlési protokoll (ciklusfázis-korrekcióval): az Altini-adat jelzi a fázishatást, intervenciós vizsgálat nincs.

### ELLENTMONDÁS (Q8)
- **Egyedi RCT-k vs. meta-analízis:** Javaloyes és Vesterinen szignifikáns HRV-előnyt mutat, a Medellín-meta csoportszinten nullát [javaloyes-2019-hrv-cycling A; vesterinen-2016-hrv-rct A; medellin-2020-hrv-meta A]. Feloldás: kis, heterogén vizsgálatok; a konzisztens lelet nem a "több teljesítmény", hanem az "ugyanaz vagy jobb, kevesebb intenzív edzésből".
- **"Magas HRV = jó" narratíva vs. Bellenger-meta:** a fogyasztói appok kommunikációja szemben áll azzal, hogy a túlterhelés is emelheti az rMSSD-t [bellenger-2016-hrv-meta A].

---

## Q9 — Túledzés és betegség

1. **Definíciós kontinuum (ECSS-ACSM konszenzus): FOR = szándékos túlterhelés, átmeneti teljesítményesés, napok–hetek alatt szuperkompenzáció; NFOR = elhúzódó (hetek–hónapok) stagnálás/romlás haszon nélkül; OTS = hónapokig tartó, több rendszerre kiterjedő maladaptáció pszichés tünetekkel.** Diagnózis kizárásos; egyetlen megbízható biomarker sincs. [meeusen-2013-ots-consensus A]
2. **Korai jelek kerékpáron (n=15, 8 nap, 1300 km): egyetlen objektív napi mutató (nyugalmi pulzus, hőmérséklet) sem különítette el egyénileg a FOR-t az akut fáradtságtól; a fáradtság+edzéskészség kérdőív-kombináció viszont már a 3. napon 78%-os pontossággal (szenz. 79%, spec. 77%) előre jelezte.** A szubjektív monitor veri az objektívet. [tenhaaf-2017-for-prediction B]
3. **A pulzus-oldali korai jel nem az emelkedés, hanem a „lefelé csúszás": funkcionálisan túlterhelt triatlonistáknál a csúcspulzus 182±5-ről 176±6/percre esett, a terhelés utáni pulzus-visszaállás gyorsult (+8±5/perc), teljesítmény −2,1±0,8%.** [aubry-2015-overreaching-hrr A]
4. **Alvás mint korai jel és mint ár: 6 hetes túlterhelés alatt a funkcionálisan túledzettek alvásideje −7,9±6,7%, hatékonysága −1,6±0,7%; felső légúti fertőzés az F-OR csoport 67%-ánál vs. kontroll 11%.** A romló alvásminőség a túlterhelés egyik legkorábbi objektív kísérője, és a betegségkockázat-ugrással jár. [hausswirth-2014-sleep-illness A]
5. **A "J-görbe" (sok edzés = több fertőzés) vitatott: az edzés utáni immunsejt-szám-esés átrendeződés, nem szuppresszió; a nyál-IgA változásai nem jelölnek ki fertőzési ablakot; a megbízható bizonyíték az opportunista fertőzéskockázat-emelkedésre korlátozott.** A fertőzésklaszterek oka multifaktoriális: kitettség, utazás (2–5× URTI-tünet hosszú repülőút után), alváshiány, energiahiány. [campbell-2018-immune-debunk C; walsh-2018-immune-recs C]
6. **Nyál-IgA: abszolút értéke nem jelez (r=0,11 az URTI-vel), de az egyéni átlaghoz képesti 28%-os esés az URTI előtti 3 hétben, illetve a saját átlag 40%-a alá csökkenés valós kockázatjelző (n=38, 50 hét).** [neville-2008-siga B]
7. **Betegség-szabályok: lázzal és „nyak alatti" tünetekkel (mellkasi köhögés, izomfájdalom, GI-tünet) edzeni és versenyezni tilos; nyak feletti tüneteknél (orrfolyás, torokkaparás) csökkentett intenzitású edzés megengedhető; <6 óra alvás ~4–5-szörösére emeli a megfázás esélyét vírus-expozíció után.** Láz utáni fokozatos visszatérés; a lázas terhelés miokarditisz-kockázat. [walsh-2018-immune-recs C; schwellnus-2016-ioc-illness A]
8. **Az edzés–alvás–munka háromszög: 1 éjszakányi alvásvesztés önmagában −5,55% állóképesség-teljesítmény (95% CI −8,12–−2,99), és minden ébren töltött plusz óra −0,36%/h** [craven-2022-akut A]; **alváshiány mellett az RPE felfelé torzít változatlan élettani költség mellett** [martin-1981-sleep-rpe A]; **a konszenzus-ajánlás sportolónak 7–9+ óra** [walsh-2021-consensus C]. Elégtelen alvás mellett a nagy terhelésblokk a Hausswirth-lelet (romló alvás → F-OR → betegség) spirálját indítja el.
9. **RED-S kapcsolat: az OTS és a RED-S tünetei/útvonalai nagymértékben átfednek, és sok publikált „túledzés"-esetben az energiahiányt nem zárták ki — teljesítményesésnél az energia-elérhetőség auditja megelőzi a túledzés-diagnózist.** Kerékpáros-releváns háttér: versenyző férfi országútisok 44%-ánál alacsony csontsűrűség, krónikus LEA mellett alacsonyabb tesztoszteron és rosszabb teljesítmény [keay-2018-male-cyclists-lea B]; REDs-prevalencia becslés nők 23–79,5%, férfiak 15–70% [mountjoy-2023-ioc-reds A]. [stellingwerff-2021-ots-reds C]
10. **Terhelésmenedzsment-elv (IOC): a helytelen terhelésmenedzsment — hirtelen ugrások, zsúfolt naptár, pszichés stressz, utazás — az akut megbetegedés és az OTS szignifikáns kockázati tényezője; a monitorozás alapja wellness-mutatók (alvás, hangulat, fáradtság) + fokozatos progresszió.** [schwellnus-2016-ioc-illness A]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q9)
- OTS/NFOR-prevalencia amatőr, munka melletti állóképességi sportolóknál: nincs megbízható adat; a hivatkozott prevalencia-számok elit/junior mintákból származnak, a konszenzus maga is óvatos [meeusen-2013-ots-consensus A].
- Ultrakerékpáros-specifikus betegség-incidencia nagy volumenű felkészülés alatt: nem találtunk kohorszvizsgálatot (keresések: "illness incidence ultra-cycling training", "URTI bikepacking racers").
- A „nyak-szabály" (neck check) mint döntési algoritmus: konszenzusos edzői/orvosi gyakorlat, prospektív validáció nincs.
- Elégtelen alvás melletti KRÓNIKUS edzés adaptációs ára (hetek–hónapok): a Craven-meta csak akut (1 éjszakás) vesztést számszerűsít; hosszú távú "alváshiányos adaptáció" vizsgálat hiányzik.

### ELLENTMONDÁS (Q9)
- **J-görbe vita:** a klasszikus exercise-immunology (nagy volumen → nyitott ablak → több URTI; a Walsh-ajánlások is erre épülnek) vs. Campbell–Turner újraértelmezés (nincs valódi szuppresszió) [walsh-2018-immune-recs C; campbell-2018-immune-debunk C]. Gyakorlati közös nevező: a tünet-klaszterek nagy blokkok/versenyek körül valósak, a védekezés (alvás, energia, higiénia, terhelés-progresszió) mindkét olvasatban ugyanaz.
- **HRV mint túledzés-detektor:** a monitorozó-ipar ígérete vs. Bellenger-meta (a nyugalmi HRV alig változik túlterhelésnél, sőt nőhet) és ten Haaf (objektív mutatók egyénileg nem jeleztek, a kérdőív igen) [bellenger-2016-hrv-meta A; tenhaaf-2017-for-prediction B].
- **„Sportolók immunrendszere gyengébb" vs. adat:** nemzetközi szintű állóképességi sportolóknál KEVESEBB URTI-epizód, mint nemzeti szintűeknél nagy volumen mellett [walsh-2018-immune-recs C — a J-görbe S-görbévé hajlik a legedzettebbeknél].

---

## Feltörekvő irányok
- HRV-vezérelt edzés wearable-ökosisztémákban (éjszakai aggregált rMSSD + zárt readiness-algoritmusok): terjed, de független validáció nélkül [stone-2021-wearable-validity B; medellin-2020-hrv-meta A]. (D-szintű gyakorlat: Whoop/Garmin readiness-pontszám követése.)
- Durability/fáradtság-ellenállás mint terhelésmutató-korrekció: a TSS-t kJ-munka utáni küszöbromlással súlyozó megközelítések (Spragg, Maunder munkássága) — a "nem minden TSS egyenlő" formalizálása [spragg-2023-durability A; maunder-2021-durability C].
- OTS–REDs egyesített szűrési algoritmusok (energia-audit először) [stellingwerff-2021-ots-reds C].
- Nagy adatbázisú, címkézett szabadéletbeli HRV-elemzések (alkohol-, betegség-, ciklushatás számszerűsítése) [altini-2021-hrv-freeliving B].

## Nem sikerült megnyitni
- PubMed/PMC oldalak (403/CAPTCHA): a Foster 2001, ten Haaf 2017, Hausswirth 2014, Vesterinen 2016, Neville 2008 számai OpenAlex/Crossref-absztraktból származnak (jelölve).
- Plews 2013 teljes szöveg (Springer csak absztraktot adott): a "7 napos gördülő átlag" konkrét száma a kapcsolódó empirikus Plews-cikkekből ismert, itt az absztrakt "averaging techniques" megfogalmazása idézhető.
- humankinetics.com (IJSPP) teljes szövegek: csak OpenAlex-absztrakt szinten elérhetők.
- Banister eredeti (1975/1991 könyvfejezet): online nem elérhető; a modellt clarke-2013-banister-model közvetíti.

## Csomag D


Készült: 2026-09-24. Fokozatok: A/B/C/D a 02-D-sources.yaml és a data/sources.yaml `grade` mezői szerint.
Új kulcsok e csomagból; a meglévő forrástár kulcsai változatlan fokozattal hivatkozva.

---

## Q10 — Konvergencia: mit csinálnak a rutinos ultrakerékpárosok és edzőik?

**1. A publikus gyakorlati minimum a "befejezéshez" ~2 W/kg tartós teljesítmény és havi 500–1500 km edzésvolumen — a felkészülési össz-volumen 2000–20 000+ km a verseny előtti 6 hónapban.** White (Ride Far) szerint "averaging about 2 watts per kg for 12 hours of riding per day" elég a legtöbb bikepacking-verseny befejezéséhez; a havi km-cél télen 500–1000, tavasszal-nyáron 1000–1500 km [white-ridefar-trainingplan C]. Ez a 08-as modul mért versenyintenzitásával (1,5–2,1 W/kg többnapos versenyen) egybevág [brayson-2019-tcr B].

**2. Az elit skálája ettől 3–10× távolabb van: Strasser évi ~30 000 km-t, Allegaert ~20 000 km-t edz 7 hónap alatt, a "klasszikus" RAAM-felkészülés ~16 000 km 7–8 hónap alatt, 12–18 órás hetekkel az alapfázis végén.** "I do about 30,000 km of training per year" [strasser-welovecycling-2017 C]; "Accomplished RAAM riders typically ride about 10,000 miles in the 7-8 months preceding RAAM" [comeau-2017-raam-training C]; Allegaert-adat: [white-ridefar-trainingplan C]. Az elit példák a 6–15 órás amatőr sávra NEM másolhatók, csak a szerkezet elve vihető át.

**3. A heti szerkezetben a legerősebb konvergencia a hétvégi back-to-back hosszú edzés: gyakorlatilag minden edző és versenyző használja.** Towers: hétvégén "back-to-back 5+ órás" napok, heti 15–20 óra összvolumenben [towers-2024-trainingweek C]; Hammond: "Weekends are for riding long; back-to-back days" [apidura-2018-ultratraining C]; a RAAM-csúcsfázis hétvégéje 250+150 mérföld back-to-back vagy egyben 300 mérföld [comeau-2017-raam-training C]; időtakarékos változata a "stacked" edzés (este 3 h + reggel 90 perc intervall) [mcquarrie-tec-zone3 C].

**4. A "csak hosszú-lassú" ellen ugyancsak konvergens az edzői álláspont: heti 1–2 minőségi (küszöb/tempó/VO2max) edzés az ultra-felkészülésben is standard.** Ibbett: "By doing loads of really long, slow rides, you'll just become good at riding slowly for a long time!" [apidura-2018-ultratraining C]; az 1998-as RAAM-mezőny körkérdésének tanulsága: "more speed work" [comeau-2017-raam-training C]; Towers 80/20–90/10 eloszlást tart [towers-2024-trainingweek C]; a CTS heti 2 kemény napot horgonyoz [pulford-2026-timecrunched C]; a 20 hetes TCR-terv K3/küszöb/VO2max kombinációra épül [barth-tcr-trainingpeaks-plan C].

**5. A leghosszabb edzés kérdésében a tartomány edzésen 4–6 órától a 2/3–3/4 versenytávig, próbatúrán 400–1000 km-ig terjed.** White: "Rides longer than about 4-6 hours do not increase your physical capabilities" – a hosszabb út mentális/felszerelési teszt [white-ridefar-trainingplan C, white-ridefar-multiday C]; Hughes: a leghosszabb edzés a kulcsesemény 2/3–3/4-e (brevet-léptékben) [hughes-rbr-2015 C]; Barth TCR-terve 400, 600 és 1000 km-es teszttúrákat ír elő [barth-tcr-trainingpeaks-plan C]; Ibbett 4 napos túrát tesz ~1 hónappal a verseny elé, napi egész napos tekeréssel, ~6 óra alvással [apidura-2018-ultratraining C].

**6. A brevet-naptár (SR-sorozat: 200→300→400→600 km) a leggyakrabban ajánlott kész progressziós keret az első ultrához.** Lenhard (PBP-győztes): "If you are new to ultra-distance, I think it's the best way to do it" [lenhard-apidura-audax C]; a Barth-terv 400/600/1000 km-es próbái ugyanezt a lépcsőt követik [barth-tcr-trainingpeaks-plan C].

**7. Erősítés: a gyakorlat (core + nehéz súlyzós munka) egybevág a lektorált ajánlással, amely a nehéz erőedzést a kerékpáros gazdaságosság javítására ajánlja.** "Heavy strength training is recommended for improving cycling economy" [ronnestad-2014-strength-review A]; Hammond heti 2 erő- (nagy áttételes hegyi ismétlés) + 2 core-edzést végez [apidura-2018-ultratraining C]; Wilcox plank/fekvőtámasz/hát-munkát tart sérülésmegelőzésre ("a kerékpározás nagyon egyirányú") [wilcox-expeditionportal C]; Strasser a pálya-rekordhoz gimnasztikát és felsőtest-edzést adott hozzá [strasser-welovecycling-2017 C]; High North: 3–5×4–8 nehéz guggolás/felhúzás [highnorth-durability-guide C].

**8. Pihenőhét: a 3+1-es blokkszerkezet és a heti legalább 1 teljes pihenőnap a közös nevező; a kihagyása a leggyakrabban bevallott hiba.** Towers 4 hetes blokkokat használ (3 terhelő + 1 könnyű), és 7 hetes pihenő nélküli blokkjait nevezi legnagyobb hibájának [towers-2024-trainingweek C]; CTS: "Designate at least 1 day completely off the bike per week" [pulford-2026-timecrunched C]; a Barth-terv "gezielte Ruhewochen"-t ír elő [barth-tcr-trainingpeaks-plan C].

**9. Tapering: 1–2 hét visszavétel, az utolsó napokban szinte semmi — "sosem lehetsz túl friss".** White: 1–2 héttel a rajt előtt könnyítés, az utolsó napokban a fő feladat az alvás [white-ridefar-trainingplan C]; Hammond 1 héttel a rajt előtt teljesen leáll és "eszik sokat"; Ibbett: "You can never be too fresh" [apidura-2018-ultratraining C]; a RAAM-séma 1–3 hetes tapert ír, a hosszú edzés 100–150 mérföldre, a volumen ~600 mérföld/hóra esik [comeau-2017-raam-training C].

**10. Az amatőr terepadat: a 720 km-es RAAM-kvalifikáción a BEFEJEZÉST a heti edzésóra (r=0,44), edzéstáv (r=0,37) és edzéssebesség (r=-0,59) jelezte előre; a befutókon belül viszont a 3 havi edzésvolumen NEM jósolta a versenysebességet (r²=0,000).** [knechtle-2011-finishers-720km B; knechtle-2009-anthropometry-600km B] — a volumen "belépőjegy", nem rangsoroló; az étkezés a versenyidővel r=0,49–0,50-nel függött össze [knechtle-2011-finishers-720km B].

**11. A strukturálatlan "volumen-modell" (munka/ingázás/odatekerés mint edzés) az élmezőnyben is működő alternatíva.** Wilcox: "Both times, I rode to the start line from Alaska, so that was my training" [wilcox-expeditionportal C]; Sehili a párizsi futáréveket nevezi alapnak: "Couriering makes you mentally tough and physically fit" — pihenőnapon is 200 km [sehili-roadcc-2023 C]; White az ingázást a leghatékonyabb volumenforrásnak tartja [white-ridefar-trainingplan C].

### KONVERGENCIA-MÁTRIX

| Téma | Egybevágó (konvergens) | Eltérő (divergens) | Amitől függ |
|---|---|---|---|
| Heti óraszám (amatőr cél) | Konzisztencia > csúcshetek; a legtöbb forrás 8–20 h közé teszi a "rendes" ultra-felkészülést [towers-2024-trainingweek C; comeau-2017-raam-training C] | CTS szerint 4–6 h/hét is fenntartható fejlődés [pulford-2026-timecrunched C]; Towers szerint <12 h "nem optimális" [towers-2024-trainingweek C] | versenytáv és -típus; munka melletti időkeret; korábbi bázis |
| Volumen szerepe | Volumen kell a befejezéshez (r=0,44 heti órával) [knechtle-2011-finishers-720km B] | Befutók között a volumen nem rangsorol (r²=0,000) [knechtle-2009-anthropometry-600km B]; White: km-cél, Towers/Barth: óra+szerkezet | cél: befejezés vs. helyezés |
| Intenzitás / "speed work" | Heti 1–2 minőségi edzés kell [apidura-2018-ultratraining C; comeau-2017-raam-training C; towers-2024-trainingweek C; barth-tcr-trainingpeaks-plan C] | Sehili: "being tough as nails will [matter more] than FTP" [sehili-roadcc-2023 C]; Wilcox strukturálatlan [wilcox-expeditionportal C]; McQuarrie Z3-hangsúlya vs. 80/20 polarizált [mcquarrie-tec-zone3 C] | időkeret (kevés óra → több tempó), terep-jelleg, versenyző alkata |
| Leghosszabb edzés | Kell rendszeres hosszú edzés; "a hét hosszú edzése fontosabb, mint az össz-volumen" [comeau-2017-raam-training C] | White: 4–6 h fölött nincs élettani többlet [white-ridefar-trainingplan C] vs. Hughes 2/3–3/4 versenytáv [hughes-rbr-2015 C] vs. Barth 400–1000 km-es túrák [barth-tcr-trainingpeaks-plan C] | mi a cél: élettan vs. felszerelés-/mentális teszt; versenytáv |
| Back-to-back / többnapos | Mindenki használja a rajt előtti 4–8 hétben [apidura-2018-ultratraining C; comeau-2017-raam-training C; towers-2024-trainingweek C] | A cél eltér: fizikai csúcsterhelés (RAAM-séma) vs. kifejezetten mentál+felszerelés-teszt (White) [white-ridefar-multiday C] | tapasztalat: első ultrás inkább teszt, rutinos inkább terhelés |
| Brevet-naptár | SR-sorozat (200→600 km) mint kész progresszió kezdőknek [lenhard-apidura-audax C; barth-tcr-trainingpeaks-plan C] | Elit versenyzők kihagyják (Wilcox, Sehili odatekerés/futármunka) [wilcox-expeditionportal C; sehili-roadcc-2023 C] | első ultra vs. sokadik; naptári elérhetőség |
| Erősítés | Core mindenkinél; nehéz súlyzós munka ajánlott [ronnestad-2014-strength-review A; apidura-2018-ultratraining C; highnorth-durability-guide C] | Terjedelem/prioritás: Wilcoxnál csak sérülésmegelőző minimum [wilcox-expeditionportal C], Strassernél formátumfüggő kiegészítés [strasser-welovecycling-2017 C] | életkor, sérüléstörténet, időkeret |
| Pihenőhét / blokk | 3+1 blokk, heti ≥1 pihenőnap [towers-2024-trainingweek C; pulford-2026-timecrunched C; barth-tcr-trainingpeaks-plan C] | Strukturálatlan modellben nincs formális pihenőhét (Wilcox/Sehili) [wilcox-expeditionportal C; sehili-roadcc-2023 C] | terhelés-monitorozás elérhetősége, életstressz |
| Tapering | 1–2 (RAAM-nál 1–3) hét visszavétel, utolsó napok pihenés/alvás [white-ridefar-trainingplan C; apidura-2018-ultratraining C; comeau-2017-raam-training C] | Mérték: Hammond teljes leállás 1 héttel a rajt előtt vs. RAAM-séma rövid intenzitás megtartása (20–30 perc speed work) [comeau-2017-raam-training C] | versenytáv, egyéni frissesség-érzet |
| Napi ütemterv-cél a versenyen (a felkészülés tervezési vége) | Kell realista napi km-kalkuláció [ridefar-schedule C] | Hayden: a merev "X km/nap" terv a 3. napon összeomlik – folyamatcél kell [hayden-confidence-realistic C] | időjárás-érzékenység, személyiség |

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q10)
- **Nincs publikált kérdőíves/tracker-alapú felmérés a TCR- (vagy bármely önellátó ultra-) mezőny heti edzésóráiról.** Keresések: "Transcontinental race riders survey training hours per week questionnaire", "DotWatcher OR bikepacking.com survey 'hours per week' training Transcontinental" — csak egyedi interjúk és tapasztalati útmutatók kerültek elő. A legjobb közelítés a 720 km-es kvalifikációs verseny kohorsza [knechtle-2011-finishers-720km B], de az egynapos formátum.
- Az "Israel/UltraCoach" néven jelzett edzői forrást nem sikerült azonosítani (keresések: "UltraCoach Israel ultra cycling coaching", "coach Israel ultracycling RAAM Transcontinental") — csak ultrafutó-appok (ultracoach.eu, ultracoach.app) találhatók.
- A heti óraszámokra a legtöbb gyakorlati forrás nem ad számot (Barth-terv adatlapja, Wilcox, Sehili); a 15–20 h [towers-2024-trainingweek C] és a 4–6 h [pulford-2026-timecrunched C] közötti sávot semmilyen kontrollált adat nem rangsorolja ultra-kimenetre.
- A Knechtle-korrelációk abszolút heti óra/km átlagai a fizetős teljes szövegben vannak; az absztraktok csak r-értékeket adnak [knechtle-2011-finishers-720km B].

### ELLENTMONDÁS (Q10)
- **"4–6 óra fölött nincs élettani haszon"** [white-ridefar-trainingplan C] **vs. a hosszú edzés primátusa** ("total volume is less important than the long ride of the week" [comeau-2017-raam-training C]; Hughes 2/3–3/4 versenytáv [hughes-rbr-2015 C]) — és a durability-irodalom, amely szerint a releváns adaptációk épp nagy előzetes munka (>1500–2000 kJ) után jelentkeznek [sanchez-jimenez-2025-durability-sr A; spragg-2024-intensity A].
- **Volumen mint siker-prediktor** (befejezés: igen [knechtle-2011-finishers-720km B]) **vs. volumen mint rangsoroló** (nem [knechtle-2009-anthropometry-600km B]).
- **Strukturált intervallos modell** (Towers, Barth, CTS, Ibbett) **vs. strukturálatlan volumen-modell** (Wilcox, Sehili) — mindkettő győztest termelt; a döntő változó valószínűleg az össz-terhelés és a konzisztencia, nem a forma.
- **Minimális heti óraszám**: "12 óra alatt nem optimális" [towers-2024-trainingweek C] vs. "4–6 óra is működik" [pulford-2026-timecrunched C].

### KALKULÁTOR-PARAMÉTEREK (Q10 → felkészülési ütemterv-generátor)
- Fázisok visszafelé a versenydátumtól (RAAM-séma arányosítva): alap 4 hónap → sebesség 1–2 hónap → csúcs/specifikus 6 hét → taper 1–3 hét [comeau-2017-raam-training C]; rövidebb (20 hetes) keretben: kombinált blokkok + 2 "crash"-hét + pihenőhetek [barth-tcr-trainingpeaks-plan C].
- Blokk-szerkezet: 3 terhelő hét + 1 regeneráló hét; heti ≥1 teljes pihenőnap [towers-2024-trainingweek C; pulford-2026-timecrunched C].
- Leghosszabb edzés: alapfázisban 4–6 h [white-ridefar-trainingplan C]; brevet-léptékű célnál a versenytáv 2/3–3/4-e [hughes-rbr-2015 C]; hosszú önellátó versenynél 2–4 napos próbatúra ~4 héttel a rajt előtt [apidura-2018-ultratraining C], napi 10+ óra nyeregidővel, 80–90% mozgáshányaddal [white-ridefar-multiday C].
- Back-to-back csúcshétvége: a csúcsfázisban (rajt előtti 6 hét), pl. 2 egymást követő hosszú nap; RAAM-léptéknél 250+150 mérföld [comeau-2017-raam-training C]; amatőr léptékben 5+5 óra [towers-2024-trainingweek C].
- Brevet-naptár: SR-lépcső 200→300→400→600 km a szezonra elosztva, az utolsó nagy próba (600 km v. többnapos túra) ~4 héttel a rajt előtt [lenhard-apidura-audax C; apidura-2018-ultratraining C; barth-tcr-trainingpeaks-plan C].
- Tapering-paraméterek: hossz 1–2 hét (nagy volumenű felkészülésnél 1–3); volumen ~50–70%-os vágás analógiájára a hosszú edzés 160–240 km-re rövidül, intenzitás rövid (20–30 perc) formában megmarad [comeau-2017-raam-training C]; utolsó 2–3 nap: minimál tekerés, alvás-prioritás [white-ridefar-trainingplan C]; elvi háttér: volumen vágható 33–66%-kal, ha az intenzitás megmarad [spiering-2021-minimaldose A].
- Terhelés-kalkulátorhoz (heti órák + zónaarányok): "könnyű" edzés TSS ≈ CTL-érték -10–25%, "nehéz" ≈ CTL +50–100% [pulford-2026-timecrunched C]; durability-edzés kJ-céljai: középhaladó 1000–1500 kJ, haladó 2000–2500 kJ előmunka a minőségi szakasz előtt [pulford-2026-durability-cts C].

---

## Q11 — Feltörekvő módszerek

**1. Melegadaptáció: 6–14 nap meleg környezeti edzés mérhető élettani és teljesítmény-javulást ad melegben.** A metaanalízis tipikus indukciós protokollja "6-14 days of exercise in heated environments"; plazmatérfogat↑, izzadás korábban és többet, RPE↓ [tyler-2016-heatadapt-meta A]; a konszenzus-ajánlás szerint a versenyzőknek hőakklimatizáció javasolt a meleg versenyek előtt [racinais-2015-heat-consensus A].

**2. A hőadaptáció gyorsan lecseng: a pulzus-adaptáció ~2,3%/nap, a maghő-adaptáció ~2,6%/nap ütemben vész el, de az újra-indukció 8–12× gyorsabb.** [daanen-2018-hadecay-meta A] — gyakorlati következmény: a hőblokkot a rajt elé kell időzíteni (~1 nap adaptáció-vesztés 2 hőmentes naponként), vagy fenntartó expozíciókkal áthidalni.

**3. A hőedzés mérsékelt klímában is teljesítmény-előnyt adhat ("olcsó magaslat"): elit kerékpárosoknál 5 hét, heti 5×50 perc hőruhás/hőkamrás edzés +2,4–2,6% hemoglobin-tömeget és +4,9% (vs. +1,7% kontroll) összesített teljesítmény-javulást hozott, ami heti 3 fenntartó edzéssel megtartható.** [ronnestad-2022-heat-hbmass A].

**4. Hipoxiás edzés: a VO2max-ra a "live high–train low" a leghatásosabb (természetes LHTL SMD 1,04, 95% CI 0,47–1,61; 59 RCT, n=1821), az időszakos hipoxiás edzés (IHT) hatása jóval kisebb (SMD 0,36, CI 0,10–0,62).** [feng-2023-hypoxia-nma A] — ultra-amatőrnek az LHTL logisztikája (hetek magaslaton, "km·h" dózis 500–1415) irreális; a hőedzés hasonló hematológiai adaptációt ad olcsóbban [ronnestad-2022-heat-hbmass A].

**5. AI/adaptív edzéstervezők (TrainerRoad AT, Xert, JOIN, HumanGO, Vekta): kereskedelmi terjedés gyors, független, lektorált validáció nincs.** Szakértői vélemények szerint az AI "demokratizálja" az edzéstervezést, de a rekreációs versenyző túl-támaszkodhat rá, és LLM-alapú tanácsadás "lehetetlenül kemény edzéseket" is ajánlhat [paine-2026-ai-coaching C]. Keresések lektorált validációra ("TrainerRoad adaptive training validation peer-reviewed", "Xert validation study", "JOIN cycling app study peer-reviewed") — nem találtam publikált, független hatásvizsgálatot egyikre sem; az "AIRO" a keresések szerint aero-bikefit-platform, nem adaptív edzéstervező.

**6. Durability mint önálló edzéscél: a tesztelés módszertana lektorált (friss vs. fáradt teljesítmény-profil), de a durability-t JAVÍTÓ edzésmódszerekről nincs RCT — a gyakorlat plauzibilis extrapolációkkal dolgozik.** Módszertan: [hunter-2025-durability-methods A; maunder-2021-durability A]; az akut esést a előzetes munka intenzitása határozza meg leginkább [sanchez-jimenez-2025-durability-sr A; spragg-2024-intensity A]. Edzői protokollok: friss vs. 1000–2500 kJ utáni 20 perces teszt, sávok (elit 0–1%, átlagos 10–20% esés), intervall a hosszú edzés végén, sprint fáradt lábbal [pulford-2026-durability-cts C]; jó fáradástűrés: <5–8% esés; hosszú Z2 + kései intenzitás + alacsony kadenciájú Z3 + nehéz erőedzés [highnorth-durability-guide C].

**7. Minimál-dózis fenntartó edzés: az állóképesség akár 15 hétig fenntartható heti 2 edzéssel és 33–66%-os volumenvágással, az erő 32 hétig heti 1 edzéssel — ha az intenzitás megmarad.** "Exercise intensity seems to be the key variable for maintaining physical performance over time" [spiering-2021-minimaldose A] — munka melletti ultrásnak: projekthajtás/családi csúcsidőszak alatt a heti 2×13–26 perc intenzív ülés megőrzi a bázist.

**8. Brain endurance training (BET): kerékpárosokon 2 RCT-ben a 6 hetes, heti 5 alkalmas, edzés utáni/percenként nehezedő kognitív feladat +11,4–17,1% kimerülésig időt (vs. +2,8–3,4% kontroll) és +5,5% 20 perces TT-teljesítményt (vs. +1,6%) adott, csökkenő RPE mellett.** [staiano-2023-bet-cyclists A] — a mentálisfáradtság-tolerancia az ultra több-napos monotóniájában elvileg kulcstényező, de ultra-formátumú kimenetre nincs vizsgálat, és a heti 5×30–60 perc kognitív terhelés maga is jelentős dózis.

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q11)
- Hőprotokoll ultrakerékpáros terepadaptációval (többnapos, önellátó) nem publikált; minden adat labor/rövid teljesítmény [tyler-2016-heatadapt-meta A; ronnestad-2022-heat-hbmass A]. A hőedzés + többnapos alváshiány/energia-deficit interakciója ismeretlen.
- A Tyler-metaanalízis összesített hatásméret-számai a Crossref-kivonatban nem szerepeltek; csak protokoll-tartomány idézhető [tyler-2016-heatadapt-meta A].
- AI-tervezők: nulla publikált független validáció (keresőkifejezések a 5. pontban) — a állítások gyártói közlések.
- Durability-edzés: nincs olyan intervenciós vizsgálat, amely a "fáradt teljesítmény" javulását mérné edzésmódszer-RCT-ben; a sanchez-jimenez-2025-durability-sr csak az akut előterhelés hatását rendszerezi.
- BET: nincs nő-adat a hivatkozott kerékpáros RCT-kben, nincs ultra-formátumú (több órás/napos) kimenet, nincs terep-vizsgálat [staiano-2023-bet-cyclists A].
- Minimál-dózis: az adatok részben katonai/általános populációból; jól edzett sportolókra a szerzők szerint is kevés az adat [spiering-2021-minimaldose A].

### ELLENTMONDÁS (Q11)
- **Hipoxia vs. hőedzés mint "hematológiai boost"**: az LHTL nagy hatásmérete [feng-2023-hypoxia-nma A] a gyakorlatban az amatőr számára elérhetetlen dózisokhoz kötött, míg a hőedzés kis (+2,4–2,6% Hb-tömeg) de olcsón elérhető adaptációt ad [ronnestad-2022-heat-hbmass A] — a "melyik éri meg" kérdésre nincs közvetlen összehasonlító vizsgálat.
- **BET hatásmérete gyanúsan nagy** (TTE +17,1% 6 hét alatt jól edzetteknél) a szokásos edzés-intervenciókhoz képest — replikáció főleg ugyanattól a kutatócsoporttól (Staiano/Marcora); független megerősítés futóknál vegyes (Lima-Junior 2023, nem nyitottuk meg).
- **White "4–6 óra fölött nincs haszon"** [white-ridefar-trainingplan C] vs. a durability-gondolat, hogy a nagy előzetes munka utáni edzésszakasz maga az inger [pulford-2026-durability-cts C; highnorth-durability-guide C] — a gyakorlati tábor is megosztott.

### KALKULÁTOR-PARAMÉTEREK (Q11 → ütemterv-generátor kiegészítő modulok)
- Hőblokk: 6–14 nap [tyler-2016-heatadapt-meta A], közvetlenül a taperrel átfedésben a rajt előtti 1–2 hétre időzítve; lecsengés ~2,3–2,6%/nap → 2 naponta legalább 1 fenntartó hőexpozíció, vagy újra-indukció a rajt előtt (8–12× gyorsabb) [daanen-2018-hadecay-meta A]; fenntartó dózis-analógia: heti 3 hőedzés [ronnestad-2022-heat-hbmass A].
- Fenntartó (minimál-dózis) hetek a naptárban: heti 2 edzés, edzésenként ≥13–26 perc, intenzitás megtartva; max 15 hét állóképesség-megőrzés [spiering-2021-minimaldose A]; erő-fenntartás: heti 1 edzés, 1 sorozat/gyakorlat [spiering-2021-minimaldose A].
- Durability-teszt a terhelés-kalkulátorba: friss 20 perces teljesítmény vs. 1000–2500 kJ előmunka utáni 20 perces; kimenet: %-esés, sávok 0–1/1–5/5–10/10–20/20+% [pulford-2026-durability-cts C]; alternatív cél: <5–8% esés [highnorth-durability-guide C].

---

## Feltörekvő irányok
- Hőedzés mint hematológiai adaptációs eszköz mérsékelt klímára ("olcsó magaslat") — elit kerékpáros adatok után amatőr/ultra dozírozás-vizsgálatok várhatók [ronnestad-2022-heat-hbmass A].
- Durability mint edzéscél: a mérési módszertan most szilárdul [hunter-2025-durability-methods A]; a következő lépés az intervenciós RCT (edzésmódszer → fáradt-teljesítmény változás).
- BET és mentálisfáradtság-menedzsment ultra-kontextusban (alváshiány + monotónia) — jelenleg csak rövid-formátumú kerékpáros RCT-k [staiano-2023-bet-cyclists A].
- AI-adaptív tervezés: gyors termékfejlődés lektorált validáció nélkül; várható kutatási terület a "human-in-the-loop" edző+AI hibrid [paine-2026-ai-coaching C].
- Gyakorlati oldalon a durability-tudatos edzésszerkezet (kJ-küszöbhöz kötött kései intervallok) terjed az edzői protokollokban [pulford-2026-durability-cts C; highnorth-durability-guide C].

## Nem sikerült megnyitni
- cyclist.co.uk Strasser TCR-interjú (403) — https://www.cyclist.co.uk/in-depth/christoph-strasser-tcr-cyclist
- ZORA PDF (Knechtle 2012 PBP-vs-RAAM teljes szöveg; robots-tiltás) — a Sage-absztrakt és OpenAlex-rekonstrukció számok nélküli, ezért a 2012-es összehasonlító tanulmány nem került a forrástárba (csak a 2009/2011-es, számokkal idézhető Knechtle-cikkek).
- jsams.org Staiano-cikk kiadói oldala (403) — helyette a Birminghami Egyetem repozitóriumi PDF-je (megnyitva, teljes szöveg).
- Bonetti & Hopkins 2009 hipoxia-meta absztraktja (Crossref: nincs absztrakt; OpenAlex: abstract_inverted_index=null) — helyette feng-2023-hypoxia-nma (nyitott, számokkal).
- James Hayden "How I train for ultra races" (csak YouTube-videó; szöveges forrás nem került elő).
