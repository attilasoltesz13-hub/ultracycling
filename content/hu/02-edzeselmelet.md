---
id: "02"
title: "Edzéselmélet ultrára"
title_en: "Training for ultras"
level: alap-halado-elit
disciplines: [onellato, kiseros, brevet, 24h]
version: 0.1
status: ellenorzott-vazlat
research: docs/02-edzeselmelet-kutatas.md
sources: data/sources.yaml
estimated_pages: 18
---

:::page type=modulnyito level=alap disc=all
# 02 · Edzéselmélet ultrára

A 08. modul megmutatta, mi dönt a versenyen; a 03., hogy miből megy a motor. Ez a modul arról szól, hogyan épül fel a motor — heti 6–15 órából, munka mellett. A jó hír: az edzéstudomány legnagyobb vitái (polarizált vagy piramis? blokk vagy lineáris?) a te szintedről nézve mellékesek, mert a mérések szerint az összterhelés és a konzisztencia dönt, nem a címke. A rossz hír: ultra-kimenettel egyetlen kontrollált edzésvizsgálat sincs — ezért ez a modul mondja ki a legtöbbször, hogy „a bizonyíték rövid távú, az átvitel becslés”.

**Egy keret az egész modulhoz:** ez a fejezet elveket és bizonyítékot tanít; a konkrét heti terved az edződdel közösen készül. Minden sablon és kalkulátor-kimenet keret, nem parancs. {fix}

**A modul végére tudni fogod:**

1. mitől lesz fittség: mennyit számít az óraszám, az intenzitás-eloszlás és a forma;
2. mit ad a hosszú edzés és a back-to-back, amit semmi más — és hol a határa;
3. hogyan épül fel 16–24 hét a versenydátumtól visszafelé, brevet-naptárral;
4. mennyit és hogyan erősíts, hogy a harmadik napon is tartson a törzsed és a nyakad;
5. mit mérnek a terhelésmutatók (TSS, CTL) és a HRV — és mikor csalnak;
6. hogyan ismered fel időben a túledzést és a betegséget, és mikor tilos edzeni;
7. hogyan férnek bele az órák a munka mellé — és mit adhat egy hőblokk.

**Szint:** Alap (2–4., 12–13., összefoglaló) → Haladó (5–11., 14–16.) → Elit (17.). **Szakág:** mind a négy; a brevet-naptár az önellátó és brevet-felkészülés gerince. **Időigény:** kb. 70 perc olvasás + a feladatok. **Előfeltétel:** a 08. modul 4. oldala (fáradtságállóság) és a 04. modul (alvás). **Jelölés:** ahol az adat csak férfiaktól származik, a {férfi} jel mutatja.
:::

:::page type=adat level=alap disc=all
## Amiből a fittség lesz: az összterhelés és a konzisztencia — a forma másodlagos

A legnagyobb, legtisztább vizsgálatok újra és újra ugyanazt mérik: ha a terhelés ugyanannyi, a szerkezet címkéje alig változtat az eredményen.

:::figure src=figures/svg/02-forma-vs-terheles.svg caption="1. ábra · Balra: a legnagyobb intenzitás-eloszlás meta-analízis (17 vizsgálat, n = 437) — időfutam-teljesítményre a modellek közti különbség nulla (SMD −0,01), a VO2max-ra kicsi polarizált-előny (SMD 0,24). Jobbra: a legnagyobb terhelés-kiegyenlített kerékpáros RCT (n = 63, 12 hét) — három HIT-elrendezés, azonos összterhelés, azonos 5–10 %-os javulás mindhárom csoportban. n = 437 / 63, férfi többség." ev=A
:::

**A meták nullát adnak a címkére.** Az intenzitás-eloszlás modelljei (polarizált, piramis, küszöb) között időfutam-teljesítményben nincs különbség (17 vizsgálat, standardizált átlagkülönbség −0,01; 95 %-os konfidencia-intervallum, CI: −0,28–0,25); a maximális oxigénfelvételre kicsi polarizált-előny mérhető (SMD 0,24). [@silva-oliveira-2024-pol-meta] {ev:A} A legnagyobb kerékpáros RCT-ben (63 jól edzett versenyző, 12 hét, azonos összterhelésű, de eltérő elrendezésű intervall-programok) minden csoport 5–10 %-ot javult, a formák között semmilyen különbség nem volt. [@sylta-2016-hit-periodization] {ev:A} A blokk-periodizáció meta-előnye kicsi és nagyon gyenge irodalomból jön (a módszertani minőség a PEDro-skálán 3,7/10); a fordított periodizáció sem jobb a többinél. [@molmen-2019-block-meta; @gonzalez-rave-2022-reverse] {ev:A}

**Ahol mégis van jel, kis vizsgálatból jön.** Egy 48 fős RCT-ben (randomizált, kontrollált vizsgálat) a polarizált csoport nyert minden változóban (+11,7 % VO2peak); 12 edzett férfi kerékpárosnál (6–10 h/hét!) a polarizált 80/0/20 a küszöb-eloszlást verte (csúcsteljesítmény +8 vs. +3 %). [@stoggl-2014-polarized-rct; @neal-2013-polarized-cyclists] {ev:A} {férfi} A profi (férfi) mezőny közben nem polarizáltan, hanem piramis-mintázatban edz, a verseny felé növelt minőséggel; egy vitacikk szerint a polarizált fölényre „nincs érdemi bizonyíték”. [@mateo-march-2025-worldtour; @burnley-2022-pol-debate] {ev:B} {férfi} (a vitacikk C) A feloldás a 3. oldalon: a közös mag a Z1-dominancia és a kevés tudatos minőség — a címke mellékes.

**Amit ebből a te szinteden tanítani érdemes.** Sorrendben: (1) a heti órák összege és a kihagyás-mentesség; (2) a Z1-dominancia; (3) heti 1–2 tudatos minőség; (4) minden más — forma, app, eszköz — ezek után jön. A merev periodizációs séma helyett az élet-összterhelésre (munka, alvás, család) reagáló rugalmas tervezés a modern irány. [@kiely-2018-periodization-critique] {ev:C} Egy szekvencia-vizsgálat szerint a sorrend többet számít, mint az „egyetlen legjobb” eloszlás: a piramis→polarizált váltás adta a legnagyobb javulást. [@filipas-2022-pyr-pol] {ev:A}

**A modul őszinteségi záradéka.** Egyetlen edzésvizsgálat sincs ultra-kimenettel (4 óránál hosszabb teljesítménnyel): minden A-fokozatú adat legfeljebb néhány hónapos (4–16 hetes), perc–órás labor-kimenet. Az átvitel a 08. modul mért versenyintenzitására (az FTP 55–70 %-a) következtetés, nem mérés. {ev:C}

:::you
**Előbb a naptárt rendezd, aztán a tervet:** a kihagyott hetek többe kerülnek, mint a rossz eloszlás. **Ne válts** formát/appot/módszert a szezon közepén az újdonság kedvéért — a mérések szerint nem ott van a különbség. {fix}
:::
:::

:::page type=fogalom level=alap disc=all
## Zónák és eloszlás: az órák nagyja könnyű, a minőség kevés és tudatos

Három zóna elég: Z1 az első szellőzési küszöb (VT1, laktát-alapon LT1) alatt — beszélgetős tempó; Z2 a két küszöb között — tempós; Z3 a második küszöb (VT2) fölött — kemény.

:::figure src=figures/svg/02-eloszlas.svg caption="2. ábra · Balra: az elit állóképességi gyakorlat session-alapon (~80/20) és idő-alapon (~90 % Z1 — becslés) — ugyanaz a hét kétféle számolással. Jobbra: a modul kalkulátor-sávjai heti óraszám szerint (6–8 h: Z1 75–80 %; 8–12 h: 80–85 %; 12–15+ h: 85–90 %) — kis óraszámnál a heti 1–2 minőségi edzés aránylag nagyobb szeletet visz. Szerkesztői sávok elit megfigyelésből és RCT-kből." ev=B
:::

**A horgony az elit gyakorlat.** Elit állóképességi sportolóknál a session-ök ~80 %-a könnyű (pulzus-idő szerint 75/8/17 % a három zóna; a laktátmérések 71 %-a ≤2,0 mmol/l); idő-alapon számolva az eloszlás még Z1-túlsúlyosabb, nagyjából 90/10 (szerkesztői becslés, C) — a session- és idő-számolás keveredése a „polarizált-vita” egyik fele. [@seiler-kjerland-2006; @seiler-2010-bestpractice] {ev:B} Edzett kerékpáros vizsgálatokban (heti 7,5–11,7 óra — pont a te sávod) ~80 % Z1 a jellemző, és 8–12 hetes távon egyik modell sem bizonyítottan jobb. [@galan-rioja-2023-cyclist-tid-sr] {ev:A}

**Miért Z1-dominancia ultrára?** Három ok. A versenyintenzitásod maga Z1–Z2 (az FTP 55–70 %-a — 08. modul) — a Z1-óra egyben versenyspecifikus edzés. A fáradtságállósággal a Z1-volumen függ össze (5. oldal). És a küszöb körüli középzóna nagy stresszt ad viszonylag kis többlet-adaptációért — a „mindig kicsit tempósan” a legdrágább rossz szokás. [@seiler-2010-bestpractice; @spragg-2022-durability-training] {ev:C}

**Miért kell mégis minőség?** A heti 1–2 kemény edzés tartja a plafont (VO2max, küszöb), amiből a tartós teljesítmény százalékolódik: a nagy intenzitású intervall-edzés (HIIT) időhatékonyan emeli a VO2max-ot (meta: +5,5 ml/kg/perc, a folyamatos edzésnél +1,2-vel több), és az ultra-edzői konszenzus is heti 1–2 minőséget tart („a csak hosszú-lassú edzéstől csak lassan-sokáig menni leszel jó”). [@milanovic-2015-hiit-meta; @apidura-2018-ultratraining] {ev:A}

**A kalkulátor-sávok** (idő-alapon; szerkesztői összeállítás a fenti forrásokból): 6–8 h/hét → Z1 75–80 %, Z2 10–15 %, Z3 8–12 % (heti 1 intervall + 1 tempó); 8–12 h → 80–85 / 8–12 / 6–10 % (1–2 minőség + 1 hosszú); 12–15+ h → 85–90 / 5–10 / 4–6 % — a többlet-óra gyakorlatilag mind Z1-be megy, a Z3 abszolút mennyisége nem nő tovább. {példa} Fázis szerint: alapozásban piramis-jellegű (több Z2), a specifikus fázisban polarizáltabb vagy még Z1-dominánsabb. [@filipas-2022-pyr-pol; @mateo-march-2025-worldtour] {ev:C}

:::you
**Tedd lassabbá a könnyű napokat és keményebbé a keveset:** a leggyakoribb amatőr hiba a szürke középzónában töltött mindennap. **Számold** időben, ne edzésszámban az arányt — session-alapon becsapod magad. {fix} A saját küszöbeid bemérése: 17. oldal, 1. teszt. {egyéni}
:::
:::

:::page type=adat level=alap disc=all
## Volumen: belépőjegy a célba éréshez — de a befutók között már nem rangsorol

A heti óraszám dönti el, hogy célba érsz-e; hogy hányadikként, azt már a szerkezet, a fáradtságállóság és a 08. modul logisztikája.

:::figure src=figures/svg/02-volumen.svg caption="3. ábra · Balra: egy 720 km-es kvalifikáción (n = 76) a befejezést a heti edzésóra (r = 0,44) és edzéstáv (r = 0,37) jósolta; egy 600 km-es versenyen (28 befutó) a befutók 3 havi volumene semmit (r² = 0,000). Jobbra: óraszám-horgonyok (edzői/versenyzői közlések, C) — CTS „time-crunched” 4–6 h/hét, amatőr TCR-teljesítő ~9–11 h, edzői ajánlás 320+ km-re 10–15 h, elit-közeli 15–20 h. Férfi adat." ev=B
:::

**A terepadat.** A 720 km-es RAAM-kvalifikáción (n = 76) a befejezést a heti edzésóra (r = 0,44 — közepes együttjárás), az edzéstáv (r = 0,37) és az edzéssebesség jelezte előre; egy 600 km-es versenyen (28 befutó) viszont a befutók 3 havi edzésvolumene egyáltalán nem jósolta a versenysebességet (r² = 0,000 — az r² a megmagyarázott hányad). [@knechtle-2011-finishers-720km; @knechtle-2009-anthropometry-600km] {ev:B} {férfi} Futóknál a könnyű futás volumene a legerősebb szint-prediktor (r ≥ 0,75). [@casado-2019-easyruns] {ev:B} {férfi} A tanulság kettős: a célba éréshez órák kellenek; a helyezéshez a 3., 5. és 7. oldal (eloszlás, fáradtságállóság, szerkezet) és a 08. modul.

**Mennyi óra „elég”?** Mért küszöb nincs — csak horgonyok. Edzői keretszám: 320+ km-es eseményre minimum 10–15 h/hét, 16–20 hét alatt felépítve; elit-közeli ultrásnak 15–20 h a kényelmes sáv, és a „12 alatt nem optimális” vélemény is él; közben egy amatőr TCR-teljesítő ~9–11 h/hetes alapozással végigment, a CTS pedig 4–6 h/hétből is fenntartható fejlődést tanít. [@tatt-boundary-ultraguide; @towers-2024-trainingweek; @houston-tcr-training; @pulford-2026-timecrunched] {ev:C} A White-féle gyakorlati minimum a befejezéshez: ~2 W/kg tartósan + havi 500–1000 km télen, 1000–1500 km szezonban. [@white-ridefar-trainingplan] {ev:C} A modul álláspontja: **a befejezéshez a 8–12 h/hét sáv reális minimum többnapos versenyre; a helyezési célhoz 12+**; és a szám kevesebbet mond, mint a kihagyás-mentesség. {példa}

**A rangsort nem az órák adják.** Az élmezőnyben a 15–20 órás strukturált hét (Towers) és a strukturálatlan volumen-modell (Wilcox az odatekerést, Sehili a futárkodást nevezi edzésének) egyaránt győztest termelt — a közös bennük az évek óta halmozott, kihagyás nélküli összterhelés. [@towers-2024-trainingweek; @wilcox-expeditionportal; @sehili-roadcc-2023] {ev:C} A döntési keret a 15. oldalon.

:::you
**Számold ki** a ténylegesen vállalható heti órád (munka, család, alvás után), és **arra** tervezz — a papíron szép 15 órás terv, amiből 8 lesz, rosszabb, mint a becsületes 10. **Az ingázás óra**: a leghatékonyabb rejtett volumenforrás. [@white-ridefar-trainingplan] {példa}
:::
:::

:::page type=adat level=halado disc=all
## Fáradtságállóság mint edzéscél: a Z1-volumen építi, és az erősítés védi

A 08. modul megmutatta, hogy ultrán a fáradt teljesítmény dönt; itt az a kérdés, mitől javul.

:::figure src=figures/svg/02-durability-edzes.svg caption="4. ábra · Balra: profi U23 kerékpárosoknál az első szellőzési küszöb alatti edzésidő korrelált a fáradt-állapotú teljesítmény javulásával (r = 0,43, p = 0,018). Jobbra: 12 hét heti 2 nehéz láberősítés után a 185 perc tekerést követő 5 perces maximális teljesítmény 371-ről 400 W-ra nőtt (+8 %), a kontrollcsoporté nem változott. Férfi adat." ev=B
:::

**A volumen-oldal.** Profi U23-aknál az első küszöb alatti edzésidő korrelált a fáradt-teljesítmény későbbi javulásával (r = 0,43) — az edzésjellemzők közül a legtisztább jel (mellette a polarizáltabb eloszlás felé mozdulás járt még javulással). [@spragg-2022-durability-training] {ev:B} {férfi} A romlást az előzetes munka intenzitása hajtja, nem a kJ (08. modul). [@sanchez-jimenez-2025-durability-sr] {ev:A} 8 hetes blokkban egyetlen terhelésmutató (TSS, sRPE, TRIMP — pulzus-alapú terhelés-pontszám) sem jelezte előre az adaptációt; az első laktátküszöb (LT1, ~az első szellőzési küszöb) alatti volumen viszont a zsíranyagcsere javulásával függött össze (n = 10, megfigyelés). [@voet-2025-durability-training] {ev:B} A zsíranyagcsere edzhető — a hosszú, alacsony intenzitású munka a fő inger [@maunder-2018-mfo] {ev:B} —, és az alacsony glikogénnel végzett edzés a zsíroxidációt javítja, a teljesítményt bizonyítottan nem. [@gejl-2021-trainlow-meta] {ev:A}

**Az erő-oldal.** 12 hét heti 2 nehéz láberősítés után a 185 perc tekerést követő 5 perces teljesítmény +8 % (371 → 400 W), a hosszú tekerés alatt kisebb oxigénigény, pulzus és érzett erőkifejtés — a friss teljesítmény nem változott, a fáradt igen. [@ronnestad-2011-strength-185min] {ev:A} {férfi} Ez az ultra-releváns haszon, és a 9. oldal erősítés-protokolljának fő indoka.

**Amit még nem tudunk.** A fáradtságállóságot célzottan javító edzésmódszerre nincs RCT — a mérési módszertan kész (friss vs. fáradt teljesítményprofil), az intervenciós vizsgálat hiányzik; az edzői protokollok (minőségi szakasz 1000–2500 kJ előmunka után) plauzibilis extrapolációk. [@hunter-2025-durability-methods; @pulford-2026-durability-cts] {ev:C} A saját fáradt-teszted: 08. modul 13. oldal, a kJ-célokkal a 17. oldalon.

:::you
**A hosszú edzésed vége a legértékesebb szakasz:** a specifikus fázisban tegyél a 3–4. óra utánra tempót vagy intervallt — fáradt izomzattal edzed azt, amit a verseny kér (edzői gyakorlat, méretlen). {példa} **Ne hagyd ki** az erősítést azért, mert „nem fér bele”: a 9. oldal minimál-protokollja heti 30–40 perc. {fix}
:::
:::

:::page type=protokoll level=halado disc=all
## A hosszú edzés és a back-to-back: a felkészülés gerince — bizonyíték nélkül, teljes egyetértéssel

Amit a 6–10 órás edzés és a két egymást követő hosszú nap ad, azt semmi rövidebb nem pótolja — de ezt méréssel senki nem támasztotta alá, csak az egybehangzó gyakorlat.

:::protocol
1. **Mit ad a hosszú edzés.** Élettanilag: a versenyspecifikus fáradt állapot maga (két óra közepesen kemény munka után a tartós teljesítmény mérhetően esik — 08. modul 4. oldal) és a zsíranyagcsere-inger. Nem-élettanilag — és ez önálló indok —: ülés-tűrés, a bél edzése (03. modul), felszerelés-teszt, fejben-tartás. [@clark-2019-cp-dynamics; @maunder-2018-mfo; @jeukendrup-2017-trainingthegut] {ev:A} A 4–6 óra feletti élettani többlet vitatott (White szerint nincs; a durability-irodalom és a RAAM-iskola szerint épp az a lényeg) — a kérdés méretlen, a nem-élettani hozam viszont vitathatatlanul csak hosszú úton gyakorolható. [@white-ridefar-trainingplan; @comeau-2017-raam-training] {ev:C}
2. **Back-to-back: két egymást követő hosszú nap.** Kontrollált vizsgálat nincs; gyakorlatilag minden ultra-edző és versenyző használja a rajt előtti 4–8 hétben („a második-harmadik napi azonos szintű teljesítés képességét edzed”). Amatőr léptékben 2 × 5–8 óra; időhiányban „stacked” változat: este 3 óra + másnap reggel 90 perc. [@rutberg-cts-multiday; @apidura-2018-ultratraining; @towers-2024-trainingweek; @mcquarrie-tec-zone3] {ev:C} {példa}
3. **A progresszió.** A hosszú edzés 4–6 órától épül 10+ óráig; többnapos versenyre a csúcs nem egyetlen extrém táv, hanem egy 2–4 napos főpróba-túra ~4 héttel a rajt előtt, napi 10+ óra nyeregidővel — felszerelés-, alvás- és etetés-teszttel egyben. [@tatt-boundary-ultraguide; @apidura-2018-ultratraining; @white-ridefar-multiday] {ev:C} {példa}
4. **A brevet-sorozat a kész gerinc.** A 200→300→400→600 km-es lépcső beépített progresszió (PBP-kvalifikációnál kötelező Super Randonneur sorozat); a 600-as az első valódi alvás-stratégia-főpróba — legkésőbb 4–6 héttel a célverseny előtt. [@pbp-2027-rules; @lenhard-apidura-audax; @tatt-boundary-pbp] {ev:C} {fix}
5. **Éjszaka: menetgyakorlás igen, alvásmegvonás-edzés nem.** Az éjszakai tekerés gyakorlása (világítás, navigáció, hideg, éjszakai evés) a felkészülés része. A szándékos alvásmegvonásos edzés viszont nem: 36 óra ébrenlét −11 % kimerülési idő és felfelé csaló érzett erőkifejtés, a baleseti kockázat valós, „alváshiányra edzeni” nem lehet (04. modul) — az ellenőrzött főpróbát a 600-as brevet adja. [@martin-1981-sleep-rpe; @craven-2022-akut; @poussel-2015-utmb-sleep] {ev:A} {fix}
:::

A „leghosszabb edzés a versenytáv X %-a” szabályra nincs mért adat; a 4–10 órás edzés dózis-válaszát (3 vs. 5 vs. 8 óra) senki nem hasonlította össze.

:::you
**Védd a hétvégi hosszút mindenáron** — a hétköznap rugalmas, a gerinc nem. **Tervezz** a szezonba legalább egy 2–4 napos főpróbát: az dönti el, hogy a felszerelésed, az ülésed és az etetésed versenyérett-e, nem a heti átlag. {fix}
:::
:::

:::page type=adat level=halado disc=all
## A felkészülés szerkezete: 16–24 hét visszafelé a versenydátumtól

A periodizáció-forma alig számít; a szerkezet értelme a logisztika — hogy a csúcsterhelés, a főpróba és a pihenés a jó helyre essen.

:::figure src=figures/svg/02-felkeszules.svg caption="5. ábra · A felkészülés fázisai visszafelé a versenydátumtól (16–24 hét): tapering 10–21 nap ← specifikus fázis a −6…−3. héten (leghosszabb edzés, back-to-back, 2–4 napos főpróba, opcionális hőblokk) ← építés 2+1/3+1 hetes blokkokban ← alap. A brevet-lépcső (200→300→400→600) a specifikus fázisra illesztve, a 600-as legkésőbb a −4…−6. héten. Edzői keret-szintézis (C) — az ütemterv-generátor ezt tölti ki." ev=C
:::

**A fázisok** (edzői keret-szintézis; a formák közti különbséget a mérések nem támasztják alá — 2. oldal): **alap** (ami a 16–24 hétből marad): Z1-domináns volumenépítés, +10–15 %/hét, minden 3–4. hét könnyű; **építés** (6–8 hét): a minőség fölfelé, a hosszú edzés 4–6 → 8–10 óra; **specifikus** (a rajt előtti 6–3. hét): terhelés-csúcs 4–6 héttel a rajt előtt, back-to-back hétvégék, 2–4 napos főpróba, éjszakai gyakorlás; **tapering** (10–21 nap): 8. oldal. [@grandgeorge-t2m-season; @vanderlinden-wuca-1224; @comeau-2017-raam-training; @tatt-boundary-ultraguide] {ev:C} {példa}

**A blokk-ritmus.** 3 terhelő hét + 1 könnyű (vagy 2+1 nagyobb terhelésnél), heti legalább 1 teljes pihenőnap — a pihenőhét kihagyása a leggyakrabban bevallott hiba (egy elit versenyző 7 hetes szünet nélküli blokkját nevezi a legnagyobb tévedésének). [@towers-2024-trainingweek; @pulford-2026-timecrunched] {ev:C} {fix} Rövid HIT-blokk (1 hét 5 kemény edzés + 3 hét heti 1 minőséggel) edzett kerékpárosnál működik, és munka mellett logisztikailag vonzó minta — kis vizsgálat, óvatosan. [@ronnestad-2014-block-cyclists] {ev:A}

**Két fő verseny egy szezonban.** A versenyzői gyakorlat 6–8 hét teljes regenerációt tart két nagy esemény között — évi 2–3 fő verseny fér bele; lektorált adat nincs. [@vanderlinden-wuca-1224] {ev:C} A minimális felkészülési idő előélettől függ, tipikusan ~6 hónap dedikált munka; a 6 hónapos össz-volumen a mezőnyben 2 000-től 20 000+ km-ig szór. [@white-ridefar-trainingplan] {ev:C}

**Munka-csúcsidőszakra: minimál-dózis.** Az állóképesség akár 15 hétig megőrizhető heti 2, intenzitást megtartó edzéssel (−33–66 % volumen), az erő heti 1-gyel — projekthajrá vagy családi csúcs idején a bázis nem vész el, ha a kevés megmaradt edzés nem lassú, hanem kevés és élénk. [@spiering-2021-minimaldose] {ev:A} {példa}

:::you
**Írd be először** a versenydátumot, a főpróbát (−4 hét), a 600-ast (−4…−6 hét) és a pihenőhetek dátumát — a többi e köré épül (az ütemterv-generátor a kísérőoldalon kitölti). **Egyeztesd az edződdel**, és hagyd, hogy az élet-terhelésed (munka, alvás) felülírja a papírt: a rugalmas terv a modern ajánlás, nem a merev séma. {fix}
:::
:::

:::page type=protokoll level=halado disc=all
## Tapering: két hét, fele volumen, a minőség marad — „sosem lehetsz túl friss”

A forma az utolsó két hétben már nem épül, csak előhívódik; a cél a frissesség, a teli raktár és az egészség.

:::figure size=short src=figures/svg/02-taper.svg caption="6. ábra · A tapering-meta (27 vizsgálat): a legnagyobb hatást a 2 hetes, exponenciálisan −41–60 % volumenű, intenzitást és gyakoriságot megtartó taper adja (össz-hatásméret 0,72 ± 0,36); az intenzitás csökkentése a hatás felét viszi el (0,33). Tipikus nyereség ~3 % (0,5–6) — rövid teljesítményen mérve; ultra-taper vizsgálat nincs." ev=A
:::

:::protocol
1. **Az alapreceptet meta adja:** 2 hét, a volumen exponenciális csökkentése átlagosan 41–60 %-kal, az intenzitás és az edzésgyakoriság megtartásával (hatásméret 0,72; az intenzitás-csökkentő taper 0,33-ra esik). [@bosquet-2007-taper-meta] {ev:A} A tipikus nyereség ~3 % (0,5–6) rövid teljesítményen — áttekintés szerint. [@mujika-2003-taper-bases] {ev:C} {fix}
2. **Ultra-fordítás.** Többnapos versenyre a gyakorlat 2–3 hét, enyhébb lejtéssel: a hosszú edzések rövidülnek (a leghosszabb ~10–14 nappal a rajt előtt), a heti ritmus és heti 1–2 rövid, élénk edzés marad, az utolsó napok fő feladata az alvás — „sosem lehetsz túl friss”. [@grandgeorge-t2m-season; @white-ridefar-trainingplan; @apidura-2018-ultratraining; @rutberg-cts-taper] {ev:C} {példa} Ultra-taper vizsgálat nincs; a fő hozadék itt valószínűleg nem a ~3 %, hanem az alvás-tartalék (04. modul), a glikogén és a betegség-kockázat csökkenése.
3. **A mérleg nőni fog — hagyd.** A feltöltéssel (03. modul) +~1 kg jön: glikogén és víz, nem zsír (72 órás, 12 g/kg feltöltésnél a testvíz +0,9 kg, a többlet az izomban). [@shiose-2016-carboload-water] {ev:A} {fix}
4. **Ami még a taperbe tartozik:** az utolsó nehéz erősítés ~7–10 nappal a rajt előtt (9. oldal); a felszerelés és a logisztika lezárása 2–3 héttel a rajt előtt — az utolsó hét ne szervizről szóljon; opcionális hőblokk (14. oldal) a taperrel átfedésben. [@white-ridefar-trainingplan] {ev:C} {példa}
5. **Amit ne:** új étel, új fekvés, új felszerelés, „még egy utolsó nagy edzés” — az utolsó héten a fittséged már adott („ami van, azzal versenyzel”), csak rontani tudsz rajta. [@rutberg-cts-taper] {ev:C} {fix}
:::

:::you
**Számolj vissza:** utolsó hosszú a −10–14. napon, utolsó nehéz erősítés a −7–10. napon, logisztika-zárás a −14–21. napon. **A viszketegséget** (túl sok energia, „edzenem kéne”) vedd jó jelnek — pont ez a cél. {példa}
:::
:::

:::page type=protokoll level=halado disc=all
## Erősítés: heti kétszer nehéz a felkészülésben, egyszer fenntartó a szezonban — a fáradt teljesítményért

Az erősítés nem a sprintedért van: a 185. perc utáni wattodért, a törzsedért és a nyakadért.

:::figure size=short src=figures/svg/02-erosites.svg caption="7. ábra · Balra: 12 hét heti 2 nehéz láberősítés után az 5 perces maximális teljesítmény 185 perc tekerés után +8 % (371 → 400 W), frissen változatlan — a haszon a fáradt állapotban jelentkezik (n = 20 férfi). Jobbra: 32 perc törzs-fárasztás után a térd frontális kitérése +54 % (15,1° → 23,3°) — a törzs-állóképesség a parazita-mozgás elleni védelem (n = 15)." ev=A
:::

:::protocol
1. **Mit tud, mit nem.** A kerékpáros meta szerint a nehéz erősítés (≥80 % 1RM — az egyszer kinyomható maximum 80 %-a) javítja a VO2max-ot és a teljesítményt; a gazdaságosság-narratívát nem erősíti meg. [@llanos-lagos-2025-hst-cyclists-meta] {ev:A} A valódi ultra-haszon a fáradt-állapotú teljesítmény (+8 % 185 perc után); nőknél is igazolt (jobb 40 perces teljesítmény). [@ronnestad-2011-strength-185min; @vikmoen-2016-female-cyclists] {ev:A}
2. **Az interferencia-félelem alaptalan.** Az egyidejű aerob + erőedzés nem rontja az erőt (SMD −0,06) és az izomnövekedést (hipertrófia, −0,01); csak az explozív erő érzékeny — ezért az erősítés külön napra vagy az aerob edzéstől ≥3 órára kerüljön. [@schumann-2022-concurrent-meta] {ev:A} {fix}
3. **A protokoll.** Felkészülésben heti 2 alkalom, 4 gyakorlat-kategória, 3 sorozat, 4–10 ismétléses nehéz súly, teljes pihenőkkel: (1) csípő/térd-domináns (guggolás, lábtolás, kitörés); (2) csípőfeszítő-lánc (felhúzás-variáns, híd); (3) törzs anti-mozgás (plank-variánsok, oldaltámasz); (4) húzó + nyak-váll tartóizmok (evezés, lapocka). A láb-protokoll a mért vizsgálaté; a törzs/húzó-kategóriák szerkesztői kiterjesztés a törzsfáradás-adatból. [@ronnestad-2011-strength-185min; @abt-2007-core-cycling] {ev:C} {példa} Időhiányban: heti 1 alkalom, izomcsoportonként ≥4 sorozat, szuperszettekkel 30–40 perc — a heti össztérfogat számít, nem az elosztás. [@iversen-2021-notimetolift] {ev:C} {példa}
4. **Szezonban: heti 1 fenntartó alkalom elég** — 13 héten át megőrizte az erőt és a 40 perces teljesítmény-előnyt; az utolsó nehéz alkalom ~7–10 nappal a rajt előtt. [@ronnestad-2010-inseason-maintenance] {ev:A} {fix}
5. **Nyak, kéz, ülőgumó.** Mért protokoll nincs (a Shermer-nyak a 07. modul témája); a konszenzus: a törzs- és húzó-munka mellé nyak-mozgásminta (áll-betűrés), pozíció-gyakorlás a versenyfelszereléssel, mikro-szünetek az első kilométertől. A törzsfáradás mérhetően rontja a hajtás-mechanikát — a core nem kozmetika. [@dotwatcher-shermers-roundtable; @abt-2007-core-cycling] {ev:C} {példa}
:::

Erősítés-vizsgálat többnapos ultra-kimenettel nincs; a leghosszabb mérés 185 + 5 perc.

:::you
**Kezdd az alapozásban** — az izomláz-hetek férjenek a télbe. **Soha ne hagyd el teljesen** a szezonban: a heti egy fenntartó alkalom olcsó, az újrakezdés drága. {fix} Terhelést és gyakorlat-kiválasztást az edződdel. {egyéni}
:::
:::

:::page type=fogalom level=halado disc=all
## Terhelésmutatók: a TSS iránymutató, nem cél — és 6 óra fölött senki nem validálta

Egy szám sosem írja le a terhelést; kettő-három együtt már használható műszerfal.

:::figure src=figures/svg/02-terheles.svg caption="8. ábra · Balra: óránkénti TSS zónánként (a képlet determinisztikus következménye): Z1 ~25–30, ultra-alap Z2 ~31–56, tempó ~58–81, küszöb ~83–100 (plafon 100/óra) — az ultraverseny-intenzitás 25–49 TSS/h. Jobbra: példa CTL-görbe 16 hetes felkészülésre heti +5 pontos rámpával, 3+1-es blokkokkal és taperrel (szimuláció — a kalkulátor ezt rajzolja a te számaidból)." ev=C
:::

**A képletek.** TSS = óra × IF² × 100, ahol IF = NP/FTP (az NP a normalizált teljesítmény, az ingadozó watt élettani átlaga; 1 óra FTP-n = 100 pont, óránként ennél több nem szerezhető); CTL = 42 napos, ATL = 7 napos exponenciálisan súlyozott TSS-átlag, TSB = CTL − ATL. A modell a Banister-féle impulzus-válasz keret leegyszerűsítése, populációs időállandókkal — egyéni kalibrálás nélkül az előrejelző ereje gyenge. [@trainingpeaks-tss-explainer; @clarke-2013-banister-model] {ev:C} Eszköz nélkül a session-RPE ugyanezt tudja: perc × érzett erőkifejtés (0–10) — pulzus- és wattmérő nélkül is konzisztens terhelésmutató. [@foster-2001-session-rpe] {ev:A}

**Egyénre kalibrálva jobb.** Versenykerékpárosoknál a terhelésmutatók és a fittségváltozás korrelációja r = 0,54–0,81 — a legjobb az egyénileg kalibrált belső mutató (iTRIMP r = 0,81), a TSS r = 0,75: a friss FTP-re kalibrálás többet ér, mint a mutató márkája. [@sanders-2017-load-cyclists] {ev:B} {férfi}

**Hol csal ultrás edzésen.** Az IF²-súlyozás a hosszú Z1–Z2 munkát „olcsónak” árazza (IF 0,6 → 36 TSS/h), miközben a 6+ órás edzés valós költsége (glikogénürülés, fáradtságállóság-romlás) nem-lineárisan nő; az NP lökésszerű terepen felfelé torzít; és a modellt 6 óránál hosszabb edzésen vagy többnapos terhelésen soha senki nem validálta. A session-RPE hosszú edzésen a végállapotot súlyozza, alváshiányban pedig maga az RPE is felfelé csal. [@spragg-2023-durability; @martin-1981-sleep-rpe] {ev:C} Ezért: „egyetlen mutató nem jelzi előre az adaptációt — a TSS/CTL iránymutató, nem cél”. [@voet-2025-durability-training] {ev:B}

**Rámpa és a hirtelen ugrás.** Friel heurisztikája: heti +5–8 CTL-pont a legtöbbeknek, +10 legfeljebb egy hétig; munka melletti amatőrnek a +3–5 a szerkesztői ajánlásunk — lektorált validáció egyikre sincs. [@friel-ramp-rate] {ev:C} {példa} Az elv mögötte szilárd: a sérülés- és betegség-kockázatot a terhelés hirtelen megugrása emeli (IOC-konszenzus). Az akut:krónikus terhelésarány (ACWR) számsávját („0,8–1,3 az édes zóna”) viszont nem tanítjuk tényként: a módszertani kritika szerint statisztikai műtermék, oksági bizonyíték nélkül — az elv marad, a küszöbszám nem. [@schwellnus-2016-ioc-illness; @impellizzeri-2020-acwr] {ev:C} {fix}

:::you
**Válassz egy műszerfalat és maradj rajta:** TSS + sRPE (vagy sRPE egyedül, ha nincs wattmérő), heti összeg + a 7 napos trend. **A hosszú edzés napján** ne a TSS-t nézd, hanem az órát és a kJ-t: a 8 órás Z1-edzés a legfontosabb edzésed, akkor is, ha a szám kevésnek mutatja. {fix} Többnapos főpróba-hét: a normál heti terhelés 2–3-szorosa — utána kötelező könnyű hét. [@rutberg-cts-multiday] {példa}
:::
:::

:::page type=protokoll level=halado disc=all
## HRV és készenlét: a kemény napok időzítője — trendként, nem parancsként

A pulzusvariabilitás nem teljesítmény-fokozó, hanem döntéstámogató: ugyanazt az eredményt hozza kevesebb intenzív edzésből.

:::figure size=short src=figures/svg/02-hrv.svg caption="9. ábra · Balra: HRV-vezérelt edzés RCT-kben — kerékpárosoknál +5,1 % csúcsteljesítmény és +7,3 % 40 perces időfutam a stagnáló kontrollal szemben, futóknál kevesebb intenzív edzésből (13,2 vs. 17,7) nagyobb javulás; a 8 RCT-s meta csoportszinten nullát ad. Jobbra: eszköz-validitás EKG-referenciával — app + mellkaspánt 4,1 %, okosgyűrű 6,8 % hiba, kamerás mérés használhatatlan (112 %). n = 17–40 / 28 175 felhasználó." ev=A
:::

:::protocol
1. **Mit mond a bizonyíték.** Kerékpáros RCT: a HRV-vezérelt csoport javult (+5,1 % csúcsteljesítmény), az előre írt terv szerint edző nem; futóknál kevesebb intenzív edzésből több javulás; a meta csoportszinten nullát ad. A konzisztens lelet: „ugyanaz vagy jobb, kevesebb kemény napból, sosem rosszabb”. [@javaloyes-2019-hrv-cycling; @vesterinen-2016-hrv-rct; @medellin-2020-hrv-meta] {ev:A}
2. **A mérés.** Reggel, ébredés után, azonos testhelyzetben, rMSSD (a pulzusvariabilitás nyugalmi mutatója); és soha nem a napi érték, hanem a 7 napos gördülő átlag a saját normálsávodhoz képest — a napi szám zajos. [@plews-2013-hrv-monitoring] {ev:C} {fix} Eszköz: mellkaspánt + app vagy jó okosgyűrű (hiba 4–7 %); az abszolút értékek eszközök között nem összevethetők, csak a saját trended számít. [@stone-2021-wearable-validity] {ev:B}
3. **A döntési szabályok.** Gördülő átlag a sávban → terv szerint; egy rossz nap semmit nem ír felül. A sáv alatt → az intenzív edzést cseréld Z1-re vagy pihenőre — a volumen mehet, az intenzitás nem. Egyedi mélypont gyanús kontextussal (alkohol, torokfájás, rossz éjszaka, stressz) → először az okot kezeld: a betegség és az alkohol nagyobb kilengés, mint az edzés (28 175 felhasználó). [@vesterinen-2016-hrv-rct; @altini-2021-hrv-freeliving] {ev:B} {fix}
4. **A csapda: a magas HRV nem mindig jó.** Túlterhelésnél a nyugalmi rMSSD inkább nő (meta: SMD 0,26) — szokatlanul magas érték nagy blokkban, romló teljesítménnyel: az is túlterhelés-jel. [@bellenger-2016-hrv-meta] {ev:A} A wearable „készenléti pontszámok” zárt algoritmusok, független validáció nélkül. {ev:D}
5. **Eszköz nélkül.** Reggeli nyugalmi pulzus + két kérdés (mennyire vagy fáradt? mennyire volnál kész ma keményen edzeni?) hasonló döntéstámogatást ad — a 12. oldal terepvizsgálatában épp a kérdőív működött, az objektív mutatók nem. [@tenhaaf-2017-for-prediction] {ev:B} {példa}
:::

HRV-vezérlés ultratávra nem tesztelt; a ciklusfázis mozgatja az rMSSD-t, nő-specifikus protokoll nincs.

:::you
**Mérj 4 hétig** beavatkozás nélkül — az a normálsávod (17. oldal, 2. teszt). Utána a szabály egyszerű: rossz trend = a kemény napot told, a könnyűt tartsd. **Ne vegyél** műszert emiatt: a pulzus + két kérdés ingyen van. {egyéni}
:::
:::

:::page type=protokoll level=alap disc=all
## Túledzés és betegség: a kérdőív veri a műszert, a romló alvás az első jel — és lázzal tilos

A túledzés elcsúszott spirál, a betegség pedig nem balszerencse, hanem terhelés-menedzsment.

:::figure size=short src=figures/svg/02-tuledzes.svg caption="10. ábra · Balra: a túlterhelés kontinuuma (funkcionális túlterhelés → nem-funkcionális → túledzés) az időskálával. Jobbra: a korai jelek — 8 napos kerékpáros terepvizsgálatban a fáradtság + edzéskészség kérdőív a 3. napon 78 %-os pontossággal jelezte a túlterhelést, egyetlen objektív napi mutató sem; 6 hetes túlterhelésben az alvásidő −7,9 %, a felső légúti fertőzés 67 % (kontroll: 11 %)." ev=A
:::

:::protocol
1. **A kontinuum.** Funkcionális túlterhelés (FOR): szándékos, napok–hetek alatt megtérül. Nem-funkcionális (NFOR): hetek–hónapok stagnálás haszon nélkül. Túledzés (OTS): hónapok, több rendszer, pszichés tünetekkel; a diagnózis kizárásos, biomarker nincs. [@meeusen-2013-ots-consensus] {ev:A}
2. **A korai jelek — és melyik működik.** Kerékpáros terepvizsgálatban (8 nap, 1300 km) egyetlen objektív napi mutató sem jelezte egyénileg a túlterhelést; a fáradtság + edzéskészség kérdőív a 3. napon 78 %-os pontossággal igen. [@tenhaaf-2017-for-prediction] {ev:B} A pulzus-jel nem az emelkedés, hanem a lefelé csúszás (csúcspulzus −6/perc); a romló alvás a legkorábbi objektív kísérő: 6 hét túlterhelésben alvásidő −7,9 %, felső légúti fertőzés 67 % vs. 11 %. [@aubry-2015-overreaching-hrr; @hausswirth-2014-sleep-illness] {ev:A} {fix}
3. **Betegség-szabályok.** Láz és „nyak alatti” tünet (mellkasi köhögés, izomfájdalom, hasmenés) = edzés és verseny tilos — a lázas terhelés szívizomgyulladás-kockázat; „nyak feletti” (orrfolyás, torokkaparás) = könnyű edzés mehet; láz után fokozatos visszatérés. 6 óránál kevesebb alvás ~4–5× megfázás-esély vírus-expozíció után. [@walsh-2018-immune-recs; @schwellnus-2016-ioc-illness] {ev:C} {fix}
4. **A „sok edzés = gyenge immunrendszer” árnyaltabb.** Az újraértelmezés szerint az edzés utáni immunsejt-esés átrendeződés, nem szuppresszió; a tünet-klaszterek nagy blokkok körül mégis valósak — okok: kitettség, utazás (repülőút után 2–5× tünet), alváshiány, energiahiány. A védekezés mindkét olvasatban ugyanaz: alvás, energia, higiénia, progresszió. [@campbell-2018-immune-debunk; @walsh-2018-immune-recs] {ev:C}
5. **Mielőtt „túledzést” diagnosztizálsz: energia-audit.** Az OTS és a RED-S (relatív energiahiány — 03. modul 15. oldal) tünetei nagyban átfednek, és sok esetben az energiahiányt ki sem zárták — tartós teljesítményesésnél először az evésed nézd, aztán az alvásod (04. modul), és csak utána az edzéstervet. [@stellingwerff-2021-ots-reds; @mountjoy-2023-ioc-reds] {ev:C} {fix}
:::

Amatőr, munka melletti túledzés-előfordulásról nincs megbízható adat; a „nyak-szabály” konszenzus, prospektíven nem validált.

:::you
**Vezesd** a két kérdést (fáradtság, edzéskészség) a naplódban — 20 másodperc naponta, és ez a legjobb korai radarod. **Sose edz lázzal.** {fix}
:::
:::

:::page type=adat level=alap disc=all
## Edzés munka mellett: a kevés óra rangsora — és mit ér az ingázás

Heti 6–10 órából nem lesz elit felkészülés; célba érő igen — ha a kevés óra jó helyre megy.

**A rangsor kevés óránál** (a 2–5. oldal szintézise): (1) a hétvégi hosszú — ez nem alku tárgya; (2) heti 1–2 rövid minőség hétköznap (a HIIT időhatékonyan tartja a plafont); (3) minden további óra Z1, ahogy fér; (4) heti 1 erősítés (30–40 perces minimál-protokoll, 9. oldal); (5) a pihenőnap marad. [@milanovic-2015-hiit-meta; @pulford-2026-timecrunched] {ev:C} {példa} A CTS „time-crunched” iskolája szerint 4–6 h/hét is fenntartható fejlődés — de a time-crunched programok kimenete rövid teljesítmény: a többnapos versenyhez a hétvégi hosszú és a szezononkénti pár nagy blokk (főpróba, brevet) nem váltható ki intenzitással, mert a fáradtságállóság volumen-függő (5. oldal). [@pulford-2026-timecrunched; @spragg-2022-durability-training] {ev:C}

**Az ingázás a rejtett volumenforrás.** A strukturálatlan modell (odatekerés, futármunka, ingázás) az élmezőnyben is győztest termelt; White az ingázást tartja a leghatékonyabb óraforrásnak — napi 2 × 45 perc Z1 heti 7,5 óra, edzésidőn kívül. [@white-ridefar-trainingplan; @wilcox-expeditionportal; @sehili-roadcc-2023] {ev:C} {példa} Az időhiányos back-to-back változat: pénteken este 3 óra + szombat reggel 90 perc („stacked”). [@mcquarrie-tec-zone3] {ev:C}

**Az élet-terhelés is terhelés.** A merev séma helyett az össz-stresszre (munka, alvás, család) reagáló rugalmas tervezés a modern ajánlás; elégtelen alvás mellett a nagy edzésblokk a túledzés-spirál kezdete (12. oldal), és egy éjszaka alváshiány önmagában −5,5 % állóképesség. [@kiely-2018-periodization-critique; @craven-2022-akut] {ev:A} Munkacsúcsra: minimál-dózis (heti 2 rövid, élénk edzés — 7. oldal), nem „megpróbálom bepréselni”.

:::you
**Naptárral tervezz, ne kívánsággal:** heti órád = a hét 168 órája − alvás (7 × 7,5) − munka − család — ami marad, az az edzés, és a 04. modul szerint az alvásból lopni a legrosszabb üzlet. **Az ingázást** számold be a Z1-volumenbe. {fix}
:::
:::

:::page type=protokoll level=halado disc=all
## Hőblokk: hat–tizennégy nap melegadaptáció — a nyári ultrák legolcsóbb százalékai

A hőség elleni védelem edzhető, gyorsan kiépül, gyorsan lecseng — és mérsékelt klímára is ad valamit.

:::figure size=short src=figures/svg/02-hoblokk.svg caption="11. ábra · A hőadaptáció kinetikája: 6–14 nap alatt kiépül (plazmatérfogat nő, az izzadás korábban indul és több, azonos terhelésen kisebb pulzus és érzett erőkifejtés), majd naponta ~2,3–2,6 %-ot veszít — de az újra-indukció 8–12-szer gyorsabb. Elit kerékpárosoknál 5 hét heti 5×50 perc hőedzés +2,4–2,6 % hemoglobin-tömeget és +4,9 % teljesítményt adott mérsékelt klímában is. Meta-analízisek + RCT." ev=A
:::

:::protocol
1. **Mit ad.** 6–14 nap meleg környezeti edzés: a plazmatérfogat (a vér folyadék-része) nő, az izzadás korábban indul és bőségesebb, azonos terhelésen kisebb pulzus, maghő és érzett erőkifejtés — melegben mérhetően jobb teljesítmény; a konszenzus meleg versenyre kifejezetten ajánlja. [@tyler-2016-heatadapt-meta] {ev:A} [@racinais-2015-heat-consensus] {ev:C}
2. **A protokoll** (keret): 6–14 egymást követő nap, napi 50–90 perc Z1–Z2 melegben — nyáron délidőben, tavasszal réteges öltözettel vagy görgőn fűtött szobában; a maghő-emelkedés és az izzadás a cél, nem a szenvedés. {példa} Időzítés: a taperrel átfedésben — a volumen úgyis csökken, a hőadag belefér.
3. **A lecsengés-szabály.** Az adaptáció ~2,3–2,6 %/nap ütemben vész el (nagyjából 1 nap adaptáció-veszteség 2 hőmentes naponként), de az újra-indukció 8–12-szer gyorsabb — ha a blokk és a rajt közé hőmentes napok esnek, 2 naponta egy fenntartó hőexpozíció (a lecsengés-ütemből levezetett szabály, C), vagy rövid újra-indukció a rajt előtt. [@daanen-2018-hadecay-meta] {ev:A} {fix}
4. **„Olcsó magaslat”.** Elit kerékpárosoknál 5 hét, heti 5 × 50 perc hőedzés +2,4–2,6 % hemoglobin-tömeget (a vér összes oxigénszállító fehérjéje) és +4,9 % összesített teljesítményjavulást adott mérsékelt klímában is (kontroll +1,7 %), heti 3 fenntartó edzéssel megtartva. A valódi magaslat (LHTL) hatása nagyobb, de a dózis (hetek a hegyen) amatőrnek irreális. [@ronnestad-2022-heat-hbmass; @feng-2023-hypoxia-nma] {ev:A}
5. **Biztonság.** A hőedzés maga is terhelés: hidratálás a 03. modul szerint, a minőségi edzések nem hőben, alvásmegvonással és energiahiánnyal nem kombinálandó. Lázasan tilos (12. oldal). {fix}
:::

Hőprotokoll többnapos önellátó terepen nem tesztelt; minden adat labor és rövid teljesítmény.

:::you
**Ha a versenyed nyári** (RACA, TCR, PBP-nyár): tervezz 10–14 napos hőblokkot a taperbe, és a versenyen már ismerni fogod a saját izzadásrátádat is (03. modul 17. oldal). **Ha nem:** a heti 1–2 meleg edzés akkor is olcsó biztosítás a hőhullám ellen. {példa}
:::
:::

:::page type=konvergencia level=halado disc=all
## Amiben a rutinos ultrások és edzőik egyetértenek — és a nagy kettéválás

Több mint húsz edzői és versenyzői forrás. A tábla után a modul egyetlen igazi „melyik utat válaszd” döntése.

| Téma | Egybevágó tapasztalat | Eltérő gyakorlat | Amitől függ |
| --- | --- | --- | --- |
| **Heti óraszám** | Konzisztencia > csúcshetek; a források 12–20 h-t adnak, a modul 8–12 h-t tart reális minimumnak (4. oldal) [@towers-2024-trainingweek; @comeau-2017-raam-training] | CTS: 4–6 h is fenntartható fejlődés; Towers: 12 alatt „nem optimális” [@pulford-2026-timecrunched] | cél (befejezés vs. helyezés), időkeret, korábbi bázis {egyéni} |
| **Volumen szerepe** | Kell a befejezéshez (r = 0,44 a heti órával) [@knechtle-2011-finishers-720km] | Befutók között nem rangsorol (r² = 0,000) [@knechtle-2009-anthropometry-600km] | befejezés vs. helyezés |
| **Minőség** | Heti 1–2 kemény edzés ultrára is [@apidura-2018-ultratraining; @comeau-2017-raam-training] | Sehili: „a keménység többet ér, mint az FTP”; Wilcox strukturálatlan [@sehili-roadcc-2023; @wilcox-expeditionportal] | időkeret (kevés óra → több minőség), alkat |
| **Leghosszabb edzés** | Rendszeres hosszú kell; „a hét hosszúja fontosabb, mint az össz-volumen” [@comeau-2017-raam-training] | White: 4–6 h fölött nincs élettani többlet vs. Hughes 2/3–3/4 versenytáv vs. 400–1000 km-es próbák [@white-ridefar-trainingplan; @hughes-rbr-2015; @barth-tcr-trainingpeaks-plan] | a cél: élettan vs. felszerelés- és fej-teszt |
| **Back-to-back** | Mindenki használja a rajt előtti 4–8 hétben [@rutberg-cts-multiday; @towers-2024-trainingweek] | A cél eltér: csúcsterhelés (RAAM-iskola) vs. teszt (White) [@comeau-2017-raam-training; @white-ridefar-multiday] | első ultra (teszt) vs. rutinos (terhelés) |
| **Brevet-lépcső** | 200→600 kész progresszió kezdőknek [@lenhard-apidura-audax; @barth-tcr-trainingpeaks-plan] | Az elit kihagyja (odatekerés, futármunka) [@wilcox-expeditionportal; @sehili-roadcc-2023] | első vs. sokadik ultra, naptár |
| **Erősítés** | Core mindenkinél; nehéz munka ajánlott [@ronnestad-2014-strength-review; @apidura-2018-ultratraining] | Terjedelem: sérülésmegelőző minimum vs. rendszeres program [@wilcox-expeditionportal; @strasser-welovecycling-2017] | életkor, sérüléstörténet, idő {egyéni} |
| **Pihenő** | 3+1 blokk, heti ≥1 pihenőnap; a kihagyása a fő hiba [@towers-2024-trainingweek; @pulford-2026-timecrunched] | Strukturálatlan modellben nincs formális pihenőhét [@sehili-roadcc-2023] | monitorozás, élet-stressz |
| **Tapering** | 1–2 (RAAM-nál 1–3) hét, utolsó napok alvás; „sosem lehetsz túl friss” [@white-ridefar-trainingplan; @apidura-2018-ultratraining] | Teljes leállás vs. rövid élénkség megtartása [@comeau-2017-raam-training] | versenytáv, egyéni frissesség-érzet |
| **Terv jellege** | Realista napi kalkuláció kell a versenyre [@ridefar-schedule] | Hayden: a merev „X km/nap” a 3. napon összeomlik — folyamatcél [@hayden-confidence-realistic] | személyiség, időjárás-érzékenység |

**A nagy kettéválás: strukturált vagy strukturálatlan?** Mindkét út termelt győztest: a strukturált intervallos modell (Towers, Barth, CTS, Ibbett — terv, zónák, mérés) és a strukturálatlan volumen-modell (Wilcox Alaszkából a rajthoz tekert; Sehili futárévekre épít) egyaránt. [@towers-2024-trainingweek; @barth-tcr-trainingpeaks-plan; @wilcox-expeditionportal; @sehili-roadcc-2023] {ev:C} Nem tudományos vita — életforma-kérdés, és a döntési keret három kérdés: **(1) Melyik tartható fenn az életed mellett 6 hónapig kihagyás nélkül?** A konzisztencia az egyetlen, amiben minden adat egyetért. **(2) Van-e elég össz-órád strukturálatlanul?** A strukturálatlan modell nagy volumenre épül (futárkodás, ingázás, expedíció) — heti 8 óránál ez nem áll össze, ott a szerkezet pótolja a mennyiséget. **(3) Mit élvezel?** Amit utálsz, azt tavaszra abbahagyod. {példa} {egyéni}

:::you
**Vedd át** az egyetértést (hétvégi hosszú + back-to-back, heti 1–2 minőség, 3+1, pihenőnap, taper), és **válassz utat** a három kérdéssel — aztán maradj rajta a szezon végéig. {egyéni}
:::
:::

:::page type=sablon level=halado disc=all
## Felkészülési terv-sablon: amit a versenydátumból visszafelé kitöltesz

Kitöltve egy oldal; a kísérőoldal ütemterv-generátora a dátumokat, a terhelés-kalkulátor a heti számokat adja.

| Mező | Mit írj be | Jelölés |
| --- | --- | --- |
| Versenydátum, táv, formátum | pl. RACA1000, augusztus, önellátó | — |
| **Heti vállalható óra** (őszintén) | pl. 10 h (munka + család után); ingázás beszámítva | {egyéni} |
| Felkészülési hossz | 16–24 hét a rajtig; ebből alap = ami a többi után marad | {példa} |
| **Tapering** | 10–14 nap (többnapos versenyre 14–21), volumen −40–60 %, minőség és ritmus marad; utolsó hosszú a −10–14. napon | {fix} |
| **Specifikus fázis** (−6…−3. hét) | terhelés-csúcs a −4…−6. héten; back-to-back hétvégék; 2–4 napos főpróba a −4. héten; éjszakai gyakorlás | {példa} |
| Építés (6–8 hét) | hosszú edzés 4–6 → 8–10 óra; heti 1–2 minőség; 2+1 vagy 3+1 blokkok | {példa} |
| Brevet-naptár | 200 → 300 → 400 → 600, a 600-as legkésőbb a −4…−6. héten; tartalék-dátumokkal | {fix} |
| Zónaarány a sávodra | 6–8 h: Z1 75–80 %; 8–12 h: 80–85 %; 12–15+: 85–90 % | {példa} |
| **Rámpa és pihenő** | CTL +3–5 (haladó +5–8)/hét; minden 3–4. hét könnyű; heti ≥1 teljes pihenőnap | {példa} |
| Erősítés | alapozástól heti 2 nehéz (4 kategória × 3 sorozat), szezonban heti 1 fenntartó; utolsó nehéz a −7–10. napon | {fix} |
| Hőblokk (nyári verseny) | 10–14 nap a taperrel átfedésben; utána 2 naponta fenntartó hőexpozíció | {példa} |
| Monitorozás | sRPE-napló + fáradtság/edzéskészség kérdés naponta; HRV 7 napos trend (ha mérsz); heti tömeg | {példa} |
| Betegség-szabály | láz vagy nyak alatti tünet = tilos; nyak feletti = könnyű; láz után fokozatos | {fix} |
| Munkacsúcs-terv | minimál-dózis: heti 2 rövid, élénk edzés + heti 1 erő — a bázis 15 hétig kitart | {példa} |
| Két verseny esetén | 6–8 hét teljes regeneráció a kettő között | {példa} |

**Hogyan használd.** A fix mezők nem alku tárgyai; a példaértékek edzői keretszámok (C fokozat), a saját helyzetedre igazítandók; **a kitöltött sablon az edződdel közös munka végterméke, nem a helyettesítője.** Ultra-kimenetű kontrollvizsgálat egyik paraméter mögött sincs — a keret a rövid távú bizonyíték és az egybehangzó gyakorlat szintézise. {ev:C}

:::you
**Először a fix dátumokat** írd be (verseny, főpróba, 600-as, pihenőhetek), aztán töltsd fel a maradékot — és a naptárba, ne a fiókba. {fix}
:::
:::

:::page type=feladat level=elit disc=all
## Mérd be magad: a zónáid, a normálsávod és a fáradt wattod

A modul három egyéni száma teszttel derül ki; edzéstervbe illesztendő, az edződdel egyeztetve.

**1. A saját zónáid terepi bemérése (egy hét, két edzés).** Első edzés: 20 perces maximális teszt pihenten (a szokásos FTP-teszted; az átlagteljesítmény ~95 %-a ≈ FTP, pulzusból a 20 perces átlagpulzus ≈ küszöbpulzus) — ez adja a Z3 határát (VT2/FTP). Második edzés: beszédteszt a Z1-határra — az a tempó, ahol még folyamatosan, teljes mondatokban tudsz beszélni (az első szellőzési küszöb praktikus közelítése); jegyezd fel a hozzá tartozó pulzust és wattot. {egyéni} A kettő között van a Z2; a 3. oldal arányai ezekre a határokra vonatkoznak. A 20 perces teszt protokollja és hibái: 16. modul. {példa}

**2. A normálsávod (4 hét, napi 20 másodperc).** Négy héten át minden reggel: fáradtság (0–10), edzéskészség (0–10), nyugalmi pulzus (és rMSSD, ha mérsz — 7 napos gördülő átlagban nézve). A 4 hét átlaga ± a tipikus ingadozás a te normálsávod; ettől lefelé tartó 3+ napos trend = a 10–12. oldal szabályai lépnek életbe. A kérdőív-alap a kerékpáros terepvizsgálatból jön, ahol ez a kombináció 78 %-os pontossággal jelezte a túlterhelést — az objektív mutatók nem. [@tenhaaf-2017-for-prediction] {ev:B} {egyéni}

**3. A fáradt wattod kJ-célokkal (a 08. modul tesztjének edzés-változata).** Friss 20 perces teszt (1. feladat) vs. ugyanez 1000–1500 kJ (középhaladó) vagy 2000–2500 kJ (haladó) Z1–Z2 előmunka után, a szokásos versenyevéseddel. Az esés százaléka a fáradtságállóságod: 5 % alatt erős, 10 % fölött a hosszú Z1-volumen és az erősítés a következő blokk fókusza. [@pulford-2026-durability-cts; @highnorth-durability-guide] {ev:C} {egyéni} Évente 2–3-szor ismételve az edzésed leghosszabb visszajelzési hurka.

**Önellenőrzés — tíz kérdés, válasz nélkül ne lapozz:**

1. Mit mértek a nagy meták az intenzitás-eloszlás modelljeiről időfutam-teljesítményre — és mi az, ami tényleg számít?
2. Hány százalék Z1 való a te heti óraszámodhoz, és miért drága a „mindig kicsit tempósan”?
3. Mit jósol a heti edzésóra egy ultrán, és mit nem?
4. Mi az egyetlen edzésjellemző, ami a fáradt-teljesítmény javulásával korrelált — és mit ad hozzá az erősítés?
5. Mire való a back-to-back, és mi a 600-as brevet szerepe?
6. Mikorra essen a terhelés-csúcs és a főpróba a versenydátumhoz képest?
7. Mennyi volument vágj a taperben, és mi marad változatlan?
8. Miért „olcsó” a hosszú Z1-edzés TSS-ben, és miért nem baj ez?
9. Mikor cserélj intenzív edzést pihenőre a HRV-trend alapján — és mikor gyanús a szokatlanul magas HRV?
10. Milyen tünetekkel tilos edzeni, és mit auditálsz először tartós teljesítményesésnél?

:::you
**A 2. feladatot kezdd ma:** négy hét múlva lesz normálsávod, és az minden későbbi döntés alapja. Mindhárom teszt eredményét vidd az edződhöz. {fix}
:::
:::

:::page type=osszefoglalo level=alap disc=all
## A modul egy oldalon

| | |
| --- | --- |
| **Összterhelés + konzisztencia** {ev:A} · A nagy meták nullát adnak a formára; a kihagyott hét drágább, mint a rossz címke. Ultra-kimenetű RCT nincs. | **Zónák** {ev:B} · Z1-dominancia + heti 1–2 tudatos minőség (sávok: C); a középzóna a drága szokás. |
| **Volumen** {ev:B} · Belépőjegy (r = 0,44), nem rangsoroló (befutók közt r² = 0); 8–12 h/hét a reális minimum, helyezéshez 12+. | **Fáradtságállóság** {ev:B} · A Z1-volumen építi (r = 0,43), az erősítés védi (+8 % 185 perc után). |
| **Hosszú + back-to-back** {ev:C} · Méretlen, de egybehangzó: hétvégi gerinc, főpróba a −4. héten, 600-as brevet mint alvás-főpróba; alvásmegvonás-edzés: nem. | **Szerkezet** {ev:C} · 16–24 hét visszafelé; csúcs a −4…−6. héten; 3+1 blokk, heti ≥1 pihenőnap; munkacsúcsra minimál-dózis. |
| **Tapering** {ev:A} · 2 (ultrára 2–3) hét, volumen −40–60 %, minőség marad; +1 kg glikogén+víz normális. | **Erősítés** {ev:A} · Heti 2 nehéz felkészülésben, 1 fenntartó szezonban; a haszon a fáradt watt, a törzs, a nyak; időhiányban 30–40 perc/hét. |
| **Terhelésmutatók** {ev:C} · TSS/CTL iránymutató, nem cél; 6 h fölött nem validált; sRPE eszköz nélkül is jó; rámpa +3–8/hét (heurisztika); ACWR-számsáv: nem tény. | **HRV** {ev:A} · Ugyanaz vagy jobb, kevesebb kemény napból; 7 napos trend; magas HRV is lehet rossz jel; a kérdőív veri a műszert (terep: B). |
| **Túledzés, betegség** {ev:A} · Romló alvás az első jel (alvásidő −7,9 %, fertőzés 67 vs. 11 %); lázzal tilos (szabályok: C); előbb energia-audit. | **Hőblokk** {ev:A} · 6–14 nap a taperrel átfedésben; lecsengés ~2,5 %/nap, újra-indukció 8–12× gyorsabb; „olcsó magaslat” (+2,4–2,6 % Hb-tömeg). |

**Egyéni mezők:** zónahatárok · normálsáv (4 hetes napló) · fáradt watt kJ-célokkal · az őszinte heti óra. {egyéni} QR → kísérőoldal: terhelés-kalkulátor, ütemterv-generátor, sablon, kvíz.

**A három legerősebb bizonyíték:** a forma-null (nagy meták + a legnagyobb kerékpáros RCT), a tapering-recept (27 vizsgálat), az erősítés fáradt-teljesítmény-hatása (RCT). **A három leggyengébb:** az óraszám-ajánlások (edzői keretszám), a hosszú edzés és a back-to-back (méretlen), és az átvitel ultra-kimenetre — kontrollált ultra-edzésvizsgálat nem létezik. Minden terv-elem keret: az edződdel lesz belőle terv. {férfi} = csak férfi adat.

**Szószedet.** *Z1/Z2/Z3* — a két szellőzési küszöb kijelölte zónák. *FTP* — egyórás küszöbteljesítmény; *IF* — intenzitás az FTP arányában; *TSS* — óra × IF² × 100; *CTL/ATL/TSB* — 42/7 napos terhelés-átlag és különbségük. *sRPE* — perc × érzett erőkifejtés. *rMSSD* — a pulzusvariabilitás mutatója. *FOR/NFOR/OTS* — funkcionális/nem-funkcionális túlterhelés, túledzés. *Hőblokk* — több napos melegadaptációs szakasz.
{: .small }

**Bizonyíték-jelek (4 sávtól 1-ig):** összesített kutatás · terepvizsgálat · szakmai tapasztalat · feltörekvő (04. modul). A hivatkozások sorszáma modulon belüli; a teljes lista a könyv végi irodalomjegyzékben.
{: .small }
:::
