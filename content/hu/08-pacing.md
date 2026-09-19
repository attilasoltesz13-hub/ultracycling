---
id: "08"
title: "Pacing és versenystratégia"
title_en: "Pacing and race strategy"
level: alap-halado-elit
disciplines: [onellato, kiseros, brevet, 24h]
version: 0.1
status: ellenorzott-vazlat
research: docs/08-pacing-kutatas.md
sources: data/sources.yaml
estimated_pages: 14
---

:::page type=modulnyito level=alap disc=all
# 08 · Pacing és versenystratégia

Egy ultraversenyt nem az nyer, aki a leggyorsabban teker, hanem aki a legkevesebbet veszít: a rajtnál, a megállásoknál, a hegyen, az éjszakában és a saját fejében. Ez a modul azt tanítja meg, hogyan oszd be az erődet és az idődet több napra úgy, hogy a harmadik napon is legyen miből tekerni — és hogyan számold ki előre, mi visz a célig a legtöbbet: a plusz kilométer/óra, a plusz mozgásóra vagy a rövidebb megállás.

**A modul végére tudni fogod:**

1. miért lassul mindenki, és mi választja el a jó lassulást a rossztól;
2. mennyit visz el a túl gyors rajt, és miért nem a watt, hanem az intenzitás dönti el, mennyi marad másnapra;
3. hogyan számolod ki a versenyidődet a sebességből, a napi mozgásidőből és az alvásból — és melyik a szűk keresztmetszet a te szintednél;
4. mit mutat a pulzus, a teljesítménymérő és az érzés egy többnapos versenyen, és mikor csal mindegyik;
5. hogyan tervezed a napot hőségben, hidegben, esőben és szélben;
6. miben értenek egyet a rutinos versenyzők, és mit kell magadon bemérned.

**Szint:** Alap (2–3., 5., 9. oldal, összefoglaló) → Haladó (4., 6–8., 10–12.) → Elit (13.). **Szakág:** mind a négy; az önellátó többnapos versenyekre a legtöbb adat, a brevet-időlimitet és a 24 órás formátumot külön jelöljük. **Időigény:** kb. 60 perc olvasás + a feladatok. **Előfeltétel:** a 04. modul (alvás) — az alvás–sebesség átváltás onnan folytatódik.
:::

:::page type=fogalom level=alap disc=all
## Ultrán mindenki lassul — a kérdés az, mennyit és hogyan

A tempó nem egy szám, hanem három: mennyivel indulsz, mennyit veszítesz belőle, és mennyit ingadozol közben.

:::figure src=figures/svg/08-intenzitas-tavolsag.svg caption="1. ábra · Mért átlagos leadott teljesítmény a verseny hosszának függvényében: 24 órás szóló rekordok (210–272 W, 2,8–3,5 W/kg), szóló RAAM (141–170 W, 1,8–2,1 W/kg), önellátó 14 napos TCR (109 W, 1,5 W/kg). Egyedi esetek, nem mezőnyátlagok; a pulzus ugyanebben a sorrendben 121–136 → 94–117 → 111–158/perc (a TCR-esetben U-alak)." ev=B
:::

**A fenntartható intenzitás alacsony, és a hosszal esik.** Egy elit 24 órás szóló csúcs 210–250 W mérve (elit közlés szerint 272 W-ig), 121–136-os átlagpulzussal; ez az egyórás küszöbteljesítmény (FTP) kb. 55–70 %-a (edzői közlés). [@rothschild-2021-ultracyclist; @knechtle-2015-24h-road; @knechtle-2019-24h-track; @strasser-inscyd-2022] {ev:B} Szóló RAAM-on ugyanez 141–170 W (1,8–2,1 W/kg), a normalizált teljesítmény (az ingadozó watt élettani „átlaga”) 160 W körül — egy hatszoros győztes ezt a saját skáláján „regeneráló tekerésnek” nevezi. [@schumacher-2011-raam; @strasser-power2max-2018; @strasser-pez-2019] {ev:B} Egy 14 napos, önellátó Transcontinentalon a napi átlag 109 W, 1,5 W/kg: a mozgásidő nagy része nagyon alacsony intenzitású. [@brayson-2019-tcr] {ev:B}

**Mindenki lassul.** Négy óránál hosszabb eseményre nincs bizonyítottan „optimális” tempóstratégia; a jól edzettek jellemzően pozitív tempóval haladnak, vagyis a vége lassabb, mint az eleje. [@abbiss-2008-pacing] {ev:C} Folyamatos 24 óra alatt egy elit esetben a leadott teljesítmény 37 %-kal, a pulzus 22 %-kal esett; ha a terhelést pihenők tagolják (kétfős váltó, 75 óra tekerés), ugyanannál a versenyzőnél az esés csak 12 %. [@rothschild-2021-ultracyclist] {ev:B} A RAAM teljes mezőnye lassul, de az első három gyorsabban rajtol, nagyobb csúcsot ér el, és tovább tartja, mielőtt lassulna. [@heidenfelder-2016-raam-pacing] {ev:B}

**Az „egyenletes tempó” a valóságban a kevésbé lassuló tempó.** 24 órás futáson nem a lassulás ténye, hanem az ingadozása jósolta a teljesítményt: a jobbaknál a sebesség relatív ingadozása (szórás/átlag) 21,5 %, a gyengébbeknél 27 %; a megtett táv és az ingadozás között közepes–erős a negatív összefüggés (r = −0,47…−0,64). [@inoue-2019-24h-pacing; @deusch-2021-timelimited] {ev:B} Ez futóadat — kerékpáron csak egyedi esetek vannak, de az elv ugyanaz: a stabil, kicsit alacsonyabb tempó többet hoz, mint a hullámzó magasabb.

**Egyenletes sebesség ≠ egyenletes teljesítmény.** Terepen, szélben az egyenletes sebességhez változó teljesítmény kell: modellen a lejtővel és széllel párhuzamosan ±10 %-kal változtatott watt azonos átlagteljesítmény mellett időt nyer (40 km-en 26–126 másodpercet). [@atkinson-2007-variable-power] {ev:A} Ultrán az elv marad (a légellenállás a sebesség köbével nő), a többórás ingadozás ára viszont nincs mérve.

:::you
**Fogadd el** előre, hogy lassulni fogsz, és a tervet erre írd: a második nap tempója nem „gyengeség”, hanem a terv része. **Mérd** a lassulást, ne érezd: a napi átlagteljesítmény és a mozgósebesség változása mondja meg, jól osztottad-e be az erődet — az érzés (9. oldal) hazudik. {fix}
:::
:::

:::page type=adat level=alap disc=all
## A túl gyors rajt ára: a második félben többet veszítesz, mint amennyit az elsőben nyertél

A mérce mindig a saját fenntartható átlagod — nem az, aki melletted rajtol.

:::figure src=figures/svg/08-24h-lecsenges.svg caption="2. ábra · Balra: egy elit versenyző teljesítménye és pulzusa folyamatos 24 óra alatt (−37 % és −22 %), a 24 órás pályarekord négy fázisával (0–4. óra tartás, 4–9. óra a legnagyobb esés, 9–22. óra plató, hajrá). Jobbra: 501 futó 24 órás pályafutásán a saját átlaghoz képest gyors első 2 óra kevesebb megtett távval járt (r = −0,58). Sematikus ábra a közölt adatok alapján." ev=B
:::

**Futáson mérhető a rajt ára.** 501 versenyző 24 órás pályafutásán az első két óra saját átlaghoz viszonyított sebessége és az összes megtett táv között közepes negatív összefüggés volt (r = −0,58): a leggyorsabb csoport alacsonyabb *relatív* intenzitással indult, és egyenletesebben futott, mint a leglassabb. [@bossi-2017-24h-running] {ev:B} 100 km-en a legjobbak az első harminc kilométeren a saját átlaguk alatt futnak, a végén fölötte; a klasszikus adat szerint a leggyorsabbak a teljes távon a kezdősebességük 15 %-án belül maradtak, és kb. 50 km-ig tartották a kezdő tempót. [@renfree-2016-100km; @lambert-2004-100km] {ev:B}

**Kerékpáron az élettani lenyomat ugyanez.** Tíz elit versenyzőnél egy 525 km-es alpesi ultrán az átlagpulzus a maximum 86 %-áról indult és 66 %-án végzett (−23 %), nagyjából 10 %-ot esve tízóránként; az idő fele a maximális pulzus 70 %-a alatt telt. [@neumayr-2004-rata] {ev:B} A 24 órás rekordokon a sebesség körről körre esik (r = −0,73…−0,79 a megtett távval), és a legnagyobb esés a 4. és 9. óra közé esik — oda, ahol az első órák ára megérkezik. [@knechtle-2015-24h-road; @knechtle-2019-24h-track] {ev:B}

**Az abszolút gyors rajt a jobb versenyzők tulajdonsága, nem receptje.** A RAAM első három helyezettje gyorsabban rajtol és tovább tartja; a Paris–Brest–Paris 2023-as adatai szerint az időn belül célba érők első szakasza is gyorsabb volt, mint a kiesőké. [@heidenfelder-2016-raam-pacing; @cyclecharts-pbp-2023] {ev:B} Ez szelekció: aki nagyobb kapacitással és jobb fáradtságállósággal (4. oldal) rajtol, az abszolút értékben gyorsabb, a saját átlagához képest mégis mérsékelt. A „lassan rajtolj” tehát így pontos: *a saját fenntartható átlagod alatt* indulj.

**Egy önellenőrző szabály.** Az érzett erőkifejtés (mennyire érzed nehéznek a munkát) szorozva a hátralévő távolság hányadával: ha a rajt utáni órákban — amikor még majdnem az egész táv hátravan — az érzés már „közepes” fölött jár, a lassulás kikényszerül. [@dekoning-2011-hazard; @tucker-2009-anticipatory] {ev:A} Ultrán ez a legegyszerűbb fék: az első napon a „könnyű” az egyetlen elfogadható válasz.

:::you
**Írd be** a tervedbe az első nap plafonját wattban vagy pulzusban (9. oldal), és ne az ellenfelek, hanem a saját fenntartható átlagod alatt indulj. **Számítsd bele**, hogy a 4–9. óra a fizetés ideje: ott ne legyen technikás, forgalmas vagy hosszú emelkedős szakasz, ha választhatsz. {fix}
:::
:::

:::page type=fogalom level=halado disc=all
## Fáradtságállóság: nem a kilojoule dönt, hanem az intenzitás — és a bél

Ami két óra után marad belőled, azt nem a megtett munka mennyisége, hanem a módja határozza meg.

:::figure size=short src=figures/svg/08-durability.svg caption="3. ábra · A tartósan fenntartható legnagyobb teljesítmény (kritikus teljesítmény, CP) frissen és két óra közepesen kemény tekerés után: 260 → 236 W (−9 %) placebóval, 254 W óránként 60 g szénhidráttal; a görbék a mért CP és W′ értékekből számolva. A rövid, robbanékony tartalék (W′) már 80 perc után esik, és a szénhidrát azon nem segít. 16 fő, kontrollált laborvizsgálat." ev=A
:::

**A görbe lejjebb tolódik.** Két óra közepesen kemény (a fenntartható szint alatti) tekerés után a kritikus teljesítmény — a tartósan fenntartható legnagyobb teljesítmény — 9 %-kal esett (260 → 236 W), a rövid robbanékony tartalék (W′) már 80 perc után 18-ról 15 kJ-ra. Óránként 60 g szénhidrát a kritikus teljesítmény esését megszüntette (254 W), a tartalékét nem. [@clark-2019-cp-dynamics] {ev:A} Az egyéni szórás óriási: 1 % alatti és 32 %-os esés is előfordul. [@jones-2024-resilience] {ev:C}

**Az intenzitás számít, nem a mennyiség.** Profi kerékpárosoknál kb. 2000 kJ, a fenntartható szint 70 %-a alatt végzett munka után a 12 perces teljesítmény és a kritikus teljesítmény nem esett; 5×8 perc a fenntartható szint fölött — kevesebb összmunkával — a sprint- és a 3 perces teljesítményt igen. [@spragg-2024-intensity] {ev:A} 21 vizsgálat összesítése ugyanezt mondja, és versenystratégiai következtetést von le: a fenntartható szint feletti percek a drágák, nem a kilojoule-ok. [@sanchez-jimenez-2025-durability-sr] {ev:A} Aki alacsony intenzitáson kevesebb szénhidrátot éget és hatékonyabban teker, kevesebbet veszít. [@spragg-2023-durability] {ev:A}

**A fáradtságállóságot a pulzus nem mutatja.** Amatőröknél 1000 kJ munka után a sikeresebb versenyzők 20 perces teljesítménye 6,5 %-kal, a kevésbé sikereseké 12,5 %-kal esett — a pulzusválaszban nem volt különbség. [@barsumyan-2025-durability-amateur] {ev:A} Ezért a teljesítménymérő a leadott munka egyetlen közvetlen mérője, a pihent FTP-re számolt zónák viszont a tizedik óra után már más állapotot jelölnek. [@maunder-2021-durability] {ev:C} Minden ilyen vizsgálat 2–4 órás; a versenyen belül, napról napra átvitt esést senki nem mérte (egy 16 napos Tour Divide előtt–után a maximális oxigénfelvétel nem változott). [@hunter-2025-durability-methods; @hyldahl-2024-tourdivide] {ev:C}

**A másik plafon a bél.** Terepen az ultrakerékpárosok óránként 52–57 g szénhidrátot visznek be (az ajánlott 90 g/h kb. 60 %-a), a második félben ez tovább esik; a napi hiány 1500–3100 kcal még váltóban és 1230 km-es nonstop versenyen is. [@geesmann-2014-1230km; @black-2012-384km; @hulton-2010-raam-energy] {ev:B} A tartósan fenntartható energia*bevitel* kb. 2,5-szerese az alapanyagcserének (a nyugalmi napi energiaigénynek), az esemény hosszától függetlenül; e fölött a raktárak fogynak. [@thurber-2019-alimentary] {ev:B} Edzett sportoló zsírból kb. 290 kcal-t tud óránként — a felszívott szénhidráttal együtt 550–650 kcal/óra a „tüzelőanyag-plafon”, ami 130–165 W tartós teljesítménynek felel meg (saját levezetés, ±30 %). [@maunder-2018-mfo; @jeukendrup-2014-personalized] {ev:C} Ez egybevág a mért ultra-átlagokkal (2. oldal): hosszú távon a bél és a raktár szabja meg a tempót, nem a láb (részletek: 03. modul).

:::you
**Tartsd** a fenntartható szint alatt a hegyeket is: a plusz percek a csúcson többe kerülnek, mint amennyit a kilojoule mutat. **Egyél** az első órától: a szénhidrát a fenntartható teljesítményt védi. **Mérd be** a saját fáradt teljesítményedet (13. oldal): az egyéni szórás túl nagy ahhoz, hogy más számát használd. {egyéni}
:::
:::

:::page type=adat level=alap disc=all
## Az idő matematikája: sebesség × mozgásidő × napok — és hol a szűk keresztmetszet

Egy plusz óra mozgás minden nap ugyanannyit ér, mint egy bizonyos plusz sebesség: a te szintedtől függ, melyik az olcsóbb.

:::figure src=figures/svg/08-idokoltsegvetes.svg caption="4. ábra · Mennyi órát nyer a célidőn egy 4000 km-es versenyen +1 km/h mozgósebesség, +1 óra napi mozgásidő és −30 perc napi álló idő, három szintre: TCR-középmezőny (22 km/h, 12,5 h/nap), TCR-élmezőny (26 km/h, 19 h/nap) és Tour Divide-középmezőny (15 km/h, 14,8 h/nap). Levezetés a képletből; a bemeneti számok tracker- és esettanulmány-adatok." ev=C
:::

**A képlet.** Napok = táv / (mozgósebesség × napi mozgásóra); a napi mozgásóra = 24 − alvás − egyéb álló idő. A Ridefar példája: 15 ébren töltött óra, 85 %-os mozgáshányad, 24 km/h → 306 km/nap; 75 %-nál 270 km/nap — a különbség 4000 km-en másfél nap. [@ridefar-time-efficiency] {ev:C} A képlet szorzatos, ezért egy óra plusz napi mozgás pontosan annyit ér, mint sebesség/mozgásóra km/h: TCR-középmezőnyben (22 km/h, 12,5 h) 1,76 km/h, az élen (26 km/h, 19 h) 1,37 km/h, a Tour Divide közepén (15 km/h, 14,8 h) 1,01 km/h. [@white-2016-ridefar-method; @mckenzie-dotwatcher-tcr-2026; @halfwayanywhere-tourdivide-2024] {ev:C}

**Érzékenység.** 4000 km, 22 km/h, 12,5 óra mozgás naponta = 275 km/nap, 14,5 nap. +1 km/h → −15 óra; +1 óra mozgás (akár egy óra kevesebb alvás, akár egy óra kevesebb egyéb állás) → −26 óra; −30 perc álló idő → −13 óra. Az élen (8 nap) ugyanez −7, −10, −5 óra; a Tour Divide közepén (18 nap) +1 km/h és +1 óra egyaránt kb. −27 óra, −30 perc állás −14. {ev:C} A +1 km/h síkon, 29 km/h körül 150 W-ról 163 W-ot kíván (+9 %; lassabb, terhelt tempónál kevesebbet, hegyen többet), az egy óra mozgás viszont „csak” logisztika. [@martin-1998-model; @white-2016-ridefar-method] {ev:C}

**A szűk keresztmetszet.** Két ellentétes példa: a TCR 12. kiadásának hetedik napján az első kettő mozgósebessége 26,0 és 26,2 km/h volt, és az vezetett, aki két órával többet volt mozgásban. [@mckenzie-dotwatcher-tcr-2026] {ev:C} A Tour Divide útvonalán viszont egy profi 30 % álló idővel 34 órával volt gyorsabb a versenyrekordnál, amelyet 25 % alatti álló idővel állítottak fel — mert 17 helyett 20,5 km/h-val mozgott (levezetés; nem hivatalos verseny). [@giuliani-2023-morton-tourdivide] {ev:C} A szabály: ha a mozgósebességben 10 %-nál nagyobb a különbség, az többet ér, mint 5–10 pont mozgáshányad; ha a sebességek egy százalékon belül vannak, a mozgásidő dönt. {példa}

**Mit jelent ez a szintedre.** A középmezőny szűk keresztmetszete a logisztika: a mozgáshányad 50–60 %, a sebességkülönbség csak 3–5 km/h a felső harmadhoz képest (6. oldal). Az élmezőny már 19–23 órát mozog naponta; ott csak a sebesség és az alvás minősége marad. A Ridefar saját számai szerint a legjobb felszerelés-optimalizálás a 2016-os TCR-en összesen 15–20 óra (saját összegzés) — a napi plusz egy óra mozgás 26. [@white-2016-ridefar-method; @white-2016-ridefar-resistance; @ridefar-time-efficiency] {ev:C}

:::you
**Számold ki** a következő versenyedre a három számot (kalkulátor a kísérőoldalon): mennyit ér nálad +1 km/h, +1 óra mozgás, −30 perc állás. **Válaszd** azt, amelyik a legolcsóbb: 60 % alatti mozgáshányadnál szinte mindig a megállások; 80 % fölött már a sebesség és a fizika (8. oldal). {fix}
:::
:::

:::page type=adat level=halado disc=onellato,brevet
## Mozgó és álló idő terepen: a különbséget a megállás adja, nem a sebesség

Az álló idő nagyobbik fele nem alvás — hanem bolt, evés, töltés, fotó, tétovázás.

:::figure src=figures/svg/08-mozgashanyad.svg caption="5. ábra · Egy versenynap felosztása mozgásra, alvásra és egyéb megállásra: TCR teljes mezőny (2015), TCR felső harmad (2022, 6. hely), TCR-élmezőny (2026, első 7 nap), Tour Divide-középmezőny (2024), Tour Divide-rekord (2016, <25 % állás) és PBP-tempójú 1200 km (2016). Tracker- és esettanulmány-adatok; az alvás/egyéb bontás részben levezetés (az egyéb a maradékból számolva)." ev=B
:::

**Mozgáshányad szintenként.** A 2015-ös TCR teljes mezőnye naponta átlagosan 12 óra 10 percet tekert, azaz a 24 óra felét; egy 2017-es középmezőnyös eset 3979 km / 23,1 km/h = 172 óra tekerés 14 nap alatt, szintén 51 % (levezetés). [@white-2016-ridefar-method; @brayson-2019-tcr] {ev:C} A felső harmad 70–76 %: egy 6. helyezett 183,7 óra mozgás 241,9 óra alatt (18,4 óra/nap), kb. 60 óra állással tíz nap alatt. [@evans-2022-bikeradar-bartholmoes; @long-2025-tcr11] {ev:B} Az élmezőny hét napra kb. 78 % (levezetés), és az első 24 órában a legjobb tíz mindössze 5–31 percet állt, az első négy 646–665 km-t tett meg. [@mckenzie-dotwatcher-tcr-2026; @mckenzie-2026-tcr12-frozen] {ev:B} Tour Divide-on a rekorderek 25 % alatt állnak, a középmezőny 38 % körül (egy blog, n = 1); egy PBP-tempójú 1216 km-es tekerésen 74 %. [@giuliani-2023-morton-tourdivide; @halfwayanywhere-tourdivide-2024; @toone-2016-pbp-southern] {ev:B}

**Mi van az álló időben.** A 6. helyezett kb. 60 órás álló idejéből éjszakánként 1,5–3 óra alvás, azaz 15–30 óra — a maradék 30–45 óra, naponta 3–4,5 óra, bolt, evés és egyéb. [@evans-2022-bikeradar-bartholmoes] {ev:B} Az 1216 km-es adatsor még pontosabb: 18,6 óra álló időből csak 7 óra volt alvás, a nem-alvás megállás legalább 9,2 óra (31 megállás, átlagosan 36 perc); a tervezettnél 2,5 órával több állás csak az eszközök töltése miatt. [@toone-2016-pbp-southern] {ev:B} A navigációs hiba, a mechanika és az ellenőrzőpontok időköltségére nincs mért adat — a versenyzői források csak annyit mondanak, hogy itt „sok időt lehet veszíteni”. [@ridefar-time-efficiency; @hayden-sleeping-guide]

**Élmezőny és középmezőny számokban.** TCR-befutók középértéke (mediánja) 252–267 km/nap; a felső 25 %-hoz kb. 300, a felső 5 %-hoz 350 km/nap fölött; az élmezőny 2022–2026-ban 480–490 km/nap. [@white-2017-tcr-results; @evans-2022-bikeradar-bartholmoes; @mckenzie-dotwatcher-tcr-2026] {ev:B} A mozgósebesség közben csak 21–23,5 km/h (felső harmad) és 26–28,8 km/h (él) között szór: a középmezőnyben a mozgáshányad a nagy különbség, a sebesség a kicsi. A PBP mezőnyének bruttó sebessége hét évtizede 15–16 km/h, a leggyorsabbaké 23–28 — a különbség döntően a megállásokból jön. [@storbeck-2019-pbp-speeds] {ev:C} Brevet-en a hosszú megállás hiánya sem jó jel: a 2023-as PBP-n a kiesők 43 %-a nem rögzített 3 óránál hosszabb megállást, a befutóknak csak 14 %-a. [@cyclecharts-pbp-2023] {ev:C}

**Szervezői viszonyítás.** A Race Across sorozat „ébren töltött hasznos idő” fogalma szerint hosszú formátumon a versenyidő 8–20 %-a jut alvásra; a Race Across France mért alvása napi 228 perc (≈16 %) — az álló idő ennek másfél-kétszerese. [@raceacrossseries-sleeprule; @hurdiel-2026-raf] {ev:B}

:::you
**Mérd** egy hosszú edzésen vagy brevet-en a saját álló idődet és a bontását (13. oldal): amíg nem tudod, hova megy a napi 3–4 óra, nem tudod visszahozni. **Célozz** 80 %-os mozgáshányadot az ébren töltött időre (15 órából 12 mozgás); 75–85 % a versenytartomány, 70 % alatt túrázol. [@ridefar-time-efficiency] {példa}
:::
:::

:::page type=adat level=halado disc=onellato,kiseros
## Alvás mint sebesség: egy óra alvás kb. 20 kilométer — de nem a mezőny adatából derül ki

A 04. modul folytatása: ott az volt a kérdés, mennyit kell aludni; itt az, mibe kerül és mit hoz.

:::figure src=figures/svg/08-alvas-km.svg caption="6. ábra · Napi távolság az éjszakai alvás függvényében három mozgósebességnél (20, 24 és 26 km/h), 80 %-os mozgáshányaddal az ébren töltött időre: minden óra alvás kb. 0,8 × mozgósebesség kilométert visz el. Modellszámítás, nem mérés; a mezőnyszintű mérés (jobb oldali pontok: Race Across France 2024, alvás és helyezés) a pályán töltött időt tükrözi, nem az alvás hatását." ev=C
:::

**A modell.** Napi táv = ébren töltött óra × mozgáshányad × mozgósebesség; az alvás az ébrenléti órákat csökkenti, nem a sebességet. Egy óra alvás így 0,8–0,85 × mozgósebesség kilométert „ér”: 24 km/h-nál kb. 20, 26-nál 22 km. [@ridefar-time-efficiency] {ev:C} Ez számítás, nem mérés: kerékpáron nincs olyan vizsgálat, amely egy versenyzőnél napról napra vetette volna össze az alvást és a másnapi mozgósebességet.

**Amit a mezőny mutat, és amit nem.** A Race Across France 2024-es mezőnyében a több alvás rosszabb helyezéssel járt (a helyezés kétharmadát az alvásmennyiség „magyarázta”), ultrafutókon ugyanez r = 0,44 (n = 1154). [@hurdiel-2026-raf; @kishi-2024-ultramarathon] {ev:B} Ez a pályán töltött idő műterméke: aki gyorsabb, kevesebb éjszakát tölt el. Személyen belül az irány fordított: ugyanezeknél a versenyzőknél a kevesebb alvás lassabb reakcióidővel járt, és napi 5,3 óra alatt az álmosság napról napra nőtt. [@hurdiel-2026-raf] {ev:B} Az egyetlen „sebesség-jellegű” személyen belüli szám egy futóeset (+1 óra alvás ≈ +0,5 km/h), másodkézből, n = 1. [@guilherme-2026-ultra] {ev:C} Ok-okozatként csak a személyen belüli irány használható.

**Miért bírja az élmezőny 3–4 órával?** Laborban már egy éjszaka alvásvesztés −5,5 % állóképesség. [@craven-2022-akut] {ev:A} Az ultrán viszont a fenntartható intenzitás olyan alacsony (többnapos szólón 1,5–2,1 W/kg), hogy ez a kapacitásesés kevésbé korlátoz, mint az elvesztett mozgásóra. A 2019 utáni TCR-győztesek közül Kolbinger (~4 óra alvás) és Gemperle (~4 óra megállás éjszakánként) ugyanabba a sávba esik; Wilcox tétele („minél többet alszol, annál jobban mész”) és Hayden ~3 órája is ide mutat; a RAAM kísérőstábbal 1–1,5 órával megy, a „nem alvó” stílus a mezőnyben visszaszorul. [@kolbinger-euronews-2019; @gemperle-apidura-2026; @wilcox-rouleur-2024; @wilcox-roadman-2026; @hayden-sleeping-guide; @strasser-pez-2019; @sehili-breakaway] {ev:C}

**A verseny előtti alvás az „ingyen sebesség”.** UTMB-n azok értek gyorsabban célba, akik a verseny előtt növelték az alvásukat, nem azok, akik az alváshiányra „edzettek”. [@poussel-2015-utmb-sleep] {ev:B} A 04. modul 11. oldalának előtakarékolása ide is érvényes.

:::you
**Számold** az alvást a versenyidő részeként, ne veszteségként: a kalkulátor a napi távot adja alvásórára bontva. **Ne másold** az élmezőny alvásidejét — a saját sebességednél és mozgáshányadodnál más a legjobb pont, és a 04. modul jelei (mikroalvás, fejszámolás) felülírják a tervet. {fix}
:::
:::

:::page type=adat level=halado disc=all
## A sebesség fizikája terhelt bringán: mennyit ad 150 watt, és mi viszi el

A légellenállás a sebesség köbével nő; a csomag, a pozíció és a gumi többet változtat, mint a lábad.

:::figure size=short src=figures/svg/08-sebesseg-fizika.svg caption="7. ábra · Sebesség a leadott teljesítmény függvényében síkon, 85 kg össztömeggel, három légellenállási felülettel (CdA 0,25 aerobar és minimális csomag; 0,35 felsőfogás jól pakolt táskákkal; 0,40 terhelt alapérték), és ugyanez 150 W-on emelkedőn 2–10 %-os lejtésnél. Levezetés a terepen validált teljesítmény–sebesség modellből (Crr 0,005, szélcsend; emelkedőn CdA 0,35)." ev=C
:::

**A modell.** A teljesítmény–sebesség egyenlet terepen 2,7 W-os hibával, R² = 0,97-tel (a mért teljesítmény ingadozásának 97 %-át magyarázza) igazolt; a hajtás hatásfoka kb. 97,7 %. [@martin-1998-model] {ev:A} Síkon, versenysebességnél a légellenállás az ellenállás több mint 90 %-a; terhelt, lassabb bringán az aránya kisebb (terepkerékpáron 8–35 %), a gördülésé nő. [@crouch-2017-aero-review; @bertucci-2013-mtb-field; @white-2016-ridefar-resistance] {ev:B} Ellenőrző értékek (levezetés; Crr 0,005, szélcsend) 150 W-ra, síkon, 85 kg-mal: 32,4 / 29,2 / 28,1 km/h, ha a légellenállási felület (CdA) 0,25 / 0,35 / 0,40 m². Emelkedőn ugyanezzel a wattal (CdA 0,35): 2 % → 19,5, 4 % → 13,1, 6 % → 9,5, 8 % → 7,4 km/h. [@martin-1998-model] {ev:C}

**Légellenállási felület (CdA) — a pozíció és a csomag.** Aerobar, csupasz bringa: 0,25–0,27; alsófogás vagy aerobar közepes csomaggal: 0,28–0,30; felsőfogás jól pakolt táskákkal, mérve: 0,315–0,334 (kormányhengerrel 0,346); felsőfogás kormányhengerrel, bő ruhával, terepkerékpáros pozíció: 0,36–0,40; táskatartós rendszer: 0,42–0,48 (−6,5–7,9 % sebesség). [@grappe-1997-obree; @frank-2021-tailfin-aero; @denham-2016-panniers-velodrome; @white-2016-ridefar-aero] {ev:B} A jól pakolt és a rosszul pakolt bikepacking-bringa között 180 km-en 7,5 perc volt 200 W-nál. [@frank-2021-tailfin-aero] {ev:B} Az aerobar nyeresége forrástól függően 0,014–0,057 m² — a modul 0,02–0,05 sávot ad, és saját mérésre biztat. [@grappe-1997-obree; @branston-2023-windtunnel; @white-2016-ridefar-aero] {ev:B}

**Gördülési ellenállás (Crr) — a gumi és a felület.** Jó országúti gumi sima aszfalton 0,003–0,005; érdes vagy nedves út, „négy évszakos” védett gumi, alacsony nyomás 0,006–0,008 (+40 % Crr ≈ −0,6 km/h, +5 óra a TCR-en); tömör murva, földút 0,008–0,015; homok az aszfalt 4,5–15-szöröse (mért terepkerékpáros adat); laza murvára, mosott Tour Divide-szakaszra mért kerékpáros Crr nincs. [@brr-test-method; @steyn-2014-mtb-surfaces; @white-2016-ridefar-resistance] {ev:B} Crr 0,005 → 0,012 ugyanazon a bringán 28,1 → 24,7 km/h 150 W-on.

**Tömeg, magasság, szél.** Egy kilogramm a 3900 km-es, 55 000 m szintes TCR-en 30–40 perc; 100 méter szint kb. 5 perc 150 W-on 85 kg-mal (fel és le együtt, sík úthoz képest). [@white-2016-ridefar-resistance; @martin-1998-model] {ev:C} 100 méterenként a levegő 0,8 %-kal ritkul (síkon gyorsít), a leadható teljesítmény 0,6 %-kal esik (emelkedőn ez marad); 1000 méteren ez −5 %. [@white-2016-ridefar-resistance; @bassett-1999-hour-records] {ev:C} 10 km/h szembeszél 29,2 → 23,5 km/h-ra lassít 150 W-nál; a Ridefar-modell átlag 10 km/h véletlen irányú szele −0,5 km/h a szélcsendhez képest; oldalszélben a hatásos légellenállási felület nő (a sebességek levezetések). [@isvan-2015-wind-yaw; @white-2016-ridefar-resistance] {ev:C} A Mont Ventoux 7,3 %-os emelkedője terhelt bringán nagyjából 56 km/h-s szembeszélnek felel meg. [@groeskamp-2017-incline-wind] {ev:C}

:::you
**Ne a wattot növeld, hanem a CdA-t és a Crr-t csökkentsd:** +40 W (+28 %) a Ridefar modelljében csak +3 km/h, míg a jól pakolt bringa, az aerobar és a gyors gumi együtt 1–2 km/h ugyanazon a lábon. [@white-2016-ridefar-method] {példa} **Használd** a kalkulátort a saját tömegeddel és CdA-becsléseddel — a becslők (Komoot, Best Bike Split) mozgásidőt adnak, nem célidőt. [@komoot-fitness-hub; @bestbikesplit-tt-accuracy] {egyéni}
:::
:::

:::page type=protokoll level=alap disc=all
## Mit nézz a kormányon: a watt a munkát méri, a pulzus háromfelé csal, az érzés integrál

Egy többnapos versenyen ugyanaz a mutató a verseny más-más szakaszában más irányba hazudik.

:::figure size=short src=figures/svg/08-pulzus-napok.svg caption="8. ábra · A pulzus viselkedése azonos leadott teljesítménynél: hőségben 45 perc alatt +12 % (a relatív terhelés valóban nő); többnapos versenyen napról napra lefelé csúszik (RAAM: 94/perc plató; TCR: 111/perc minimum az 5. napon); egy 14 napos TCR végén ismét emelkedik (U-alak). Öt vizsgálat sematikus egyesítése." ev=B
:::

:::protocol
1. **Watt: az első nap plafonja.** A leadott munka egyetlen közvetlen mérője; a fáradtságállóság-különbséget a pulzus nem mutatja. [@barsumyan-2025-durability-amateur] {ev:A} 24 órás formátumon az FTP 55–70 %-a; többnapos versenyen a versenyátlag 1,5–2,1 W/kg — az első nap plafonja feljebb lehet, de a saját fenntartható átlag alatt, hegyen is. [@rothschild-2021-ultracyclist; @schumacher-2011-raam] {példa} A pihent zónák a tizedik óra után mást jelentenek (13. oldal). {egyéni}
2. **Pulzus: az első két napon felfelé figyeld, utána lefelé csal.** Hőségben a felfelé drift valós: 35 °C-on 45 perc alatt +12 % pulzus, −19 % maximális oxigénfelvétel azonos wattnál — ilyenkor a watt-tartás a hiba. [@wingo-2005-cvdrift; @tatterson-2000-heat] {ev:A} Többnapos versenyen a pulzus azonos wattnál napról napra csökken (RAAM: 94-es plató; alpesi ultra: −10 % tízóránként) — a zóna tartása egyre több wattot kényszerít ki. [@fesseler-2026-raam58; @neumayr-2004-rata; @aubry-2015-overreaching-hrr] {ev:B} Egy 14 napos TCR végén ismét emelkedett (111 → 158/perc): a szerzők szerint szabályozási zavar, nem több erő. [@brayson-2019-tcr] {ev:B} {fix}
3. **Érzés: alvás- és energiahiány után felfelé csal — és ez a jó jel.** 36 óra ébrenlét után az érzett erőkifejtés nő, a pulzus és az oxigénfelvétel nem; a kimerülésig tartó idő −11 %. [@martin-1981-sleep-rpe] {ev:A} Az érzés/pulzus arány érzékenyebb, mint a nyers pulzus. [@roberts-2019-cycling] {ev:A} Ha ugyanaz a watt változatlan pulzusnál egyre nehezebb: aludj vagy egyél. {fix}
4. **Kiszáradás: a szomjúság szerint, órás minimummal.** Laborban 1–4 % testtömegvesztés arányosan emeli a maghőt és a pulzust; kültéri, önszabályozott időfutamon 2–4 % nem rontott. [@montain-1992-dehydration; @goulet-2011-dehydration-meta] {ev:A} {példa}
5. **Pulzusvariabilitás: reggeli szűrő, nem tempó-jel.** A napi terhelést tükrözi, de a „magas = jó” olvasat csal: túlterhelésnél is nőhet. [@bellenger-2016-hrv-meta; @barrero-2019-tdf-hrv] {ev:A} Versenyen ne nézd. Az edzői „szétcsatolódás” (watt:pulzus arány romlása, 5 % alatt jó) edzésdiagnosztika, versenyen a drift természetes. [@friel-decoupling-tp] {ev:C} {példa}
:::

Ultrán senki nem hasonlította össze a watt-, pulzus- és érzésvezérelt tempózást; a fentiek labor-mechanizmusokból és egyedi esetekből állnak össze. [@abbiss-2008-pacing]

:::you
**Írd** a kormányra: 1. nap watt-plafon; hőségben pulzus; 2. naptól watt + érzés/pulzus arány. **Ne** a pulzuszónát tartsd a harmadik napon — az egyre több wattot kér, pont amikor a legkevesebb van. {fix}
:::
:::

:::page type=protokoll level=halado disc=all
## Napszak és időjárás: a hőséget nem alvással, hanem ritmuseltolással kezeled

A 10–20 °C-os reggel és este az olcsó kilométer; a 30 °C feletti délután és a 0–5 °C-os hajnali leereszkedés a drága — maratonon az optimum 3,8–9,9 °C, fölötte négyzetesen nő a lassulás és a feladók aránya. [@elhelou-2012-marathon-weather] {ev:B}

:::figure size=short src=figures/svg/08-homerseklet.svg caption="9. ábra · Kimerülésig tartó tekerés ideje a levegő hőmérsékletének függvényében a maximális oxigénfelvétel 70 %-án (8 férfi, laborvizsgálat): fordított U, 10,5 °C-on a leghosszabb (93,5 perc), 30,5 °C-on a legrövidebb (51,6 perc), 4 °C-on rövidebb, mint 11 °C-on; a 4 és 21 °C-os pont helye sematikus. Maratonon az optimum 3,8–9,9 °C. A kerékpáros optimum a menetszél miatt feljebb tolódik." ev=A
:::

:::protocol
1. **Hőségben a lassítás nem hiba, hanem a test hűtése.** 32 °C-on 30 perces időfutamon −6,5 % teljesítmény (kontrollált vizsgálat), 40 °C-on rövid terhelésen 17 %-kal kevesebb munka (áttekintés); a konszenzus időjárás szerinti rajtidőt, hűtési szüneteket és belső hűtést (jégkása) javasol. [@tatterson-2000-heat; @periard-2021-heat-review; @racinais-2015-heat-consensus] {ev:A} Ultrán a hőtermelés kisebb — az irány vihető át, a százalék nem.
2. **35 °C fölött told el a napot, alatta egyéni.** A versenyzői gyakorlat nem nappali alvás, hanem ritmuseltolás: hajnal előtti indulás, éjfélig tekerés, a legmelegebb órákban lassítás és rövid hűtés-megállók. [@dotwatcher-nightstarts-roundtable; @muller-precisionhydration-2017; @ridefar-schedule] {ev:C} A küszöb nem mért. {példa} {egyéni}
3. **Az éjszaka nem ingyenes.** Egy elit versenyzőnél 2 fős RAAM-váltóban nappal 212, éjjel 189 W (−11 %) ugyanazon a versenyen; a legnehezebb sáv 02–04 óra és a napkelte utáni óra — ide a koffein. [@rothschild-2021-ultracyclist; @muller-precisionhydration-2017] {ev:B} A kockázati ár a 04. modulban: „megállni igen, feladni nem”. {fix}
4. **Hidegben és esőben a hőháztartás korlátoz, nem a watt.** 5 °C-on esőben (futószalagon, n = 7) azonos sebességnél magasabb az oxigénfelvétel és a laktát (a vér tejsavszintje, az intenzitás jele), alacsonyabb a maghő; a hajnali leereszkedés menetszélben a labor 4 °C-ánál is hidegebb. [@ito-2013-rain-cold; @galloway-1997-temperature] {ev:A} Az átöltözés befektetés — a TCR 2026 fagyos nyitóéjszakáját (−1 … −3 °C) az élboly ruházattal, nem megállással kezelte. [@mckenzie-2026-tcr12-frozen] {ev:B} {példa}
5. **Szél: éjszakára a sík, szeles szakasz.** A versenyzői heurisztika szerint a szél naplementekor csökken — a nappali termikus szélre igaz, frontálisra nem. [@ridefar-schedule; @ridefar-route-planning] {ev:C} Mért ultra-adat nincs. {példa}
6. **Kísérős versenyen a sivatagot áttekerik.** RAAM-on a stáb hűtéssel viszi át a versenyzőt; nappali pihenőről egyik forrás sem beszél. [@baloh-nduranz-2024; @goldstein-cbc-2021] {ev:C}
:::

:::you
**Tervezd** a napot a hőmérséklet-görbére: nehéz emelkedő és technikás szakasz a 10–20 °C-os sávba, sík és szeles az éjszakába, a 35 °C feletti órákba lassítás és hűtés. **Vidd** az eső-réteget akkor is, ha a rajt meleg. {fix}
:::
:::

:::page type=konvergencia level=halado disc=all
## Amiben a rutinos versenyzők egyetértenek — és amiben nem

Több mint húsz versenyzői, edzői, stábos és szervezői forrás. Ahol egyetértenek, az bevehető a tervedbe; ahol nem, ott a formátum vagy egyéni tényező dönt. {ev:C}

| Téma | Egybevágó tapasztalat | Eltérő gyakorlat | Amitől függ |
| --- | --- | --- | --- |
| **Rajttempó** | „Túl korán túl sok” mindig visszaüt; plafon a küszöb ~65 %-án; a második félben többet veszíthetsz, mint amennyit az elsőben nyersz [@muller-precisionhydration-2017; @rutberg-cts-2016; @hughes-rbr-2015] | Az élboly abszolút értékben gyorsan indul és nem áll meg: első nap 600+ km, 5–31 perc állás; „soha nem maximumon, kivéve az elején” [@mckenzie-2026-tcr12-frozen; @evans-bikeradar-2024; @gemperle-apidura-2026] | A saját átlaghoz mérve mindenki lassan indul; az élboly az első napot frissen használja ki — a középmezőnynek nem másolható {egyéni} |
| **Napi távcél** | Élboly 400–450 km/nap az első nap után; 300 km/nap a felső ötöd; 240–280 a közép; +5 % tartalék [@ridefar-schedule; @hager-transiberica-2022] | Hayden elutasítja a merev „X km/nap” tervet („a harmadik napon, esőben mi lesz vele?”), helyette folyamatcél; Bialek a közérzethez igazít [@hayden-confidence-realistic; @bialek-cyclite-2024] | Számszerű terv a logisztikához, folyamatcél a morálhoz; szintidős formátumban számszerű |
| **Mozgáshányad** | A különbséget a megállás adja: Ride Far ≥80 % (az ébren töltött időre); edzői eset 94 %, „óránként legfeljebb 5 perc” (eltelt időre); „könnyebb menni, mint megállni és újraindulni” [@ridefar-time-efficiency; @rutberg-cts-2016; @hughes-rbr-2015; @allegaert-apidura-2016] | Brevet: PBP-n 57 óra nyeregben, 30 óra kívül (≈65 % az eltelt időre), ebből csak 10 óra alvás — a kontrollok viszik az időt; hőségben a körönkénti hűtés-megállás „megérte” [@storbeck-2019-pbp-lessons; @muller-precisionhydration-2017] | Formátum (önellátó vs. kontroll-kötött), hőség, hossz (egynapos 90 %+, többnapos 80–85 %) |
| **Megállás: mikor, mennyi** | Több ok gyűljön össze egy megállásra; kontrollon időzítő (30 + 10–15 perc) [@ridefar-time-efficiency; @storbeck-2019-pbp-lessons] | Alvásadag: Gemperle 4 h megállás/éj; Wilcox ~4 h; Hayden 1,5 h (<4 nap) / ~3 h; Kolbinger ~4 h, „aludhattam volna kevesebbet”; Sehili nem áll meg; RAAM 1–1,5 h [@gemperle-apidura-2026; @wilcox-roadman-2026; @hayden-sleeping-guide; @kolbinger-euronews-2019; @sehili-breakaway; @strasser-pez-2019] | Versenyhossz, kísérős vs. önellátó, az ellenfél helyzete {egyéni} |
| **Hegy és sík** | Emelkedőn magasabb, síkon alacsonyabb watt, de mindkettő kontrollált: rekordkísérleten 220 W sík / 280 W hegy (az FTP 55 / 70 %-a); hosszú emelkedő előtt előre töltés, mert fent nem lehet enni [@broadwith-cyclingweekly-2018; @strasser-pez-2019; @baloh-nduranz-2024] | A fenntartható szint feletti csúcsok drágábbak, mint a kilojoule mutatja — az élettan a hegyi „követem a többieket” ellen szól [@sanchez-jimenez-2025-durability-sr; @spragg-2024-intensity] | Terepprofil és W/kg; a +25–30 % hegyi watt sík-domináns rekordokból jön, alpesi ultrára számszerű forrás nincs |
| **Éjszaka** | Éjjel esik a teljesítmény (212 → 189 W, n = 1); a legnehezebb 02–04 óra és a napkelte utáni óra, ide a koffein; éjjel inkább főútra [@rothschild-2021-ultracyclist; @muller-precisionhydration-2017; @ridefar-route-planning] | Sehili és az első napi élboly átteker; Shaw 22:00-kor fekszik, 02:00-kor indul [@sehili-breakaway; @dotwatcher-nightstarts-roundtable] | Kronotípus (04. modul), hőség, forgalom; kísérős versenyen a stáb figyelése |
| **Rossz szakasz** | Feldarabolás és nem-döntés: „húsz percig meg tudod csinálni?”; „éjjel sose adj fel”; a kilométer rossz időben is siker [@broadwith-cyclingweekly-2018; @ridefar-schedule; @hayden-confidence-realistic; @hager-transiberica-2022] | Sehili nem nézi a trackert; Hall a saját korábbi részidői ellen versenyez; Baloh görcsnél lassít, iszik, vár [@sehili-breakaway; @hall-bikepacking-2016; @baloh-infinity-2020] | Élettani ok → lassíts és tölts; mentális → rövid egység, alvás; a tracker egyénileg motivál vagy demoralizál {egyéni} |
| **Alvás mint sebesség** | „Minél többet alszol, annál jobban mész”; bölcsebb túl sokat aludni és gyorsan tekerni; 4 h megállás/éj a tempó tartásáért [@wilcox-rouleur-2024; @wilcox-roadman-2026; @hayden-sleeping-guide; @gemperle-apidura-2026] | „Az ember, aki nem alszik”; „aludhattam volna kevesebbet”; RAAM 1 h/éj [@sehili-breakaway; @kolbinger-euronews-2019; @strasser-pez-2019] | Versenyhossz és formátum: 4 napnál hosszabb önellátón konvergál a 3–4 h; a „nem alvó” stílus 2020 óta visszaszorul |

**Szakágak.** *Önellátó:* első 24 óra alvás nélkül az élen, utána 400–450 km/nap és 3–4 óra alvás; a mozgáshányad a fő különbségtevő. *Kísérős RAAM:* 1–1,5 óra alvás, „regeneráló” intenzitás, sivatag hűtéssel, a stáb a döntési tartalék. *Brevet/PBP:* a kontrollok viszik az időt, az első éjszakai alvás a 90 órás csoportban a szintidőt veszélyezteti; óránként ≤5 perc állás. *24 órás pálya:* watt-plafon (FTP 55–70 %), hőségben lassítás és hűtés-megállás, koffein 02–04 órára. [@storbeck-2019-pbp-lessons; @hughes-rbr-2015; @muller-precisionhydration-2017; @raam-sleepcom-2022] {ev:C}

:::you
**Vedd át** azt, amiben egyetértenek (mozgáshányad, rajt a saját átlag alatt, feldarabolás), és **döntsd el** a formátumod szerint azt, amiben nem (alvásadag, távcél típusa). {egyéni}
:::
:::

:::page type=sablon level=halado disc=all
## Versenyterv-sablon: az időköltségvetés, amit a rajt előtt kitöltesz

Kitöltve egy oldal; a kísérőoldal kalkulátora a számokat és az érzékenységet kiszámolja.

| Mező | Mit írj be | Jelölés |
| --- | --- | --- |
| Verseny, táv, szint, felület | pl. 4000 km, 40 000 m, 90 % aszfalt | — |
| **Mozgósebesség** (saját, terhelt, edzésből) | pl. 22 km/h; a kalkulátor CdA/Crr/tömeg alapján ellenőrzi | {egyéni} |
| Napi alvás (04. modul) | pl. 3 óra/éj | {példa} |
| **Egyéb álló idő célja** (bolt, evés, töltés, egyéb) | pl. 3 óra/nap → mozgáshányad az ébren töltött időre 80 % | {példa} |
| Napi mozgásóra és napi táv | 24 − 3 − 3 = 18 óra × 22 km/h = 396 km/nap | — |
| **Célidő + 5 % tartalék** | 4000 / 396 = 10,1 nap → 10,6 nap | {példa} |
| A három kar nálad (+1 km/h · +1 h mozgás · −30 min állás) | pl. −11 h · −13 h · −7 h → a szűk keresztmetszet: ___ | {fix} |
| Első nap plafonja | pl. FTP 60 %-a wattban, vagy pulzus a max 75 %-a alatt; hegyen a fenntartható szint alatt | {példa} |
| Első 24 óra terve | ébren tekerve az első éjszakán csak akkor, ha a 04. modul jelei engedik; különben 1. éjszaka blokk | {egyéni} |
| Napi ritmus időjárásra | 35 °C fölött: hajnali indulás, déli lassítás, éjfélig; hideg hajnal: réteg, nem megállás | {példa} |
| Mutatók a kormányon | 1. nap watt-plafon; hőségben pulzus; 2. naptól watt + érzés/pulzus arány | {fix} |
| Brevet: kontrollzárás | 15 km/h 600 km-ig, 11,43 km/h 600–1000, 13,33 km/h 1000–1300; PBP 90 óra = 13,33 km/h bruttó | {fix} |
| Kísérős: ki dönt a tempóról és a megállásról | a stáb neve, a szabály (pl. „a 3. naptól a stáb”) | {fix} |
| Rossz szakasz szabálya | „20 percig”; éjjel nem adom fel; ok szerint: élettani → lassíts és tölts, mentális → egység, alvás | {fix} |

**Hogyan használd.** A fix mezők nem alku tárgyai; a példaértékek a te versenyhosszodra és szintedre igazítandók; az egyéni mezők csak a 13. oldal tesztjei után tölthetők ki felelősen. A sablon viszonyítási alap, nem parancs: „a terv attól jó, hogy látod, hol tartasz hozzá képest”. [@ridefar-schedule] {ev:C} A brevet-kontrollidők az ACP-szabályból jönnek. [@rusa-acp-control-times] {ev:C}

:::you
**Töltsd ki** a következő versenyedre, és **hasonlítsd össze** a kalkulátor három karjával: ha a „−30 perc állás” sor nagyobb számot ad, mint a „+1 km/h”, a felkészülésed következő hete a megállásokról szól, nem a wattról. {fix}
:::
:::

:::page type=feladat level=elit disc=all
## Mérd be magad: fáradt teljesítmény, saját mozgáshányad, saját légellenállás

A modul három egyéni száma teszttel derül ki; a részletes protokoll a 16. modulban.

**1. Fáradt teljesítmény (egy edzés, 3 óra).** Frissen: 20 perces időfutam-teszt (a szokásos FTP-teszted). Egy másik napon: 2 óra a fenntartható szint alatt (a küszöb 70–80 %-a), a szokásos versenyevéseddel, majd ugyanaz a 20 perces teszt. Az esés százaléka a te fáradtságállóságod: laborban evés nélkül 6–7 % volt a jó, 12 % a gyenge; szénhidráttal az esésnek ennél kisebbnek kell lennie — ha 10 % fölött esel, a versenytempódat lejjebb kell tenned (saját küszöb, nem mért). {egyéni} A szám csak a saját állapotodra és 2 órás előterhelésre érvényes — a többnapos átvitelt senki nem mérte. Edzéstervbe illesztendő; egyeztesd az edződdel. [@barsumyan-2025-durability-amateur; @clark-2019-cp-dynamics] {ev:A}

**2. Saját mozgáshányad (egy 300–600 km-es tekerés vagy brevet).** Tracker vagy óra bekapcsolva, minden megállásnál egy szó a jegyzetbe (bolt, WC, ruha, navigáció, fotó, tétovázás). Utána: mozgásidő / eltelt idő, és a megállások bontása percben. Amit keresel: a napi 3–4 órából mennyi a bolt és az evés (összevonható), mennyi a navigáció és a tétovázás (megszüntethető). {egyéni} Célérték 80 % az ébren töltött időre; 70 % alatt a következő verseny nem a wattról szól. [@ridefar-time-efficiency; @toone-2016-pbp-southern] {ev:C}

**3. Saját légellenállási felület (egy délelőtt, szélcsendben).** Egy 1–2 km-es, sík, forgalommentes kör, teljesítménymérővel, a versenyfelszereléssel: 5–6 kör egyenletes 150–200 W-on, aztán ugyanez a másik pozícióban (felsőfogás vs. aerobar) vagy csomagolással. A sebességből és a wattból a kalkulátor visszaszámolja a CdA-t; a két beállítás különbsége a te nyereséged. {egyéni} A módszer (Chung-féle „virtuális emelkedő”) egy hobbiversenyzőnél 8 beállítást különített el 0,315 és 0,346 m² között. [@frank-2021-tailfin-aero] {ev:B} Ha nem mérsz: 0,35 (felsőfogás, jól pakolva), 0,40 (kormányhenger, bő ruha) a becslés. {példa}

**Önellenőrzés — tíz kérdés, válasz nélkül ne lapozz:**

1. Miért nem „hiba” a lassulás egy ultrán — és mi az, ami valóban az?
2. Mekkora relatív rajtintenzitás járt a legtöbb megtett távval 24 órás futáson, és mi ebből a kerékpáros tanulság?
3. Mi dönti el, mennyi marad a kritikus teljesítményedből két óra után — és mi védi meg?
4. Egy óra plusz napi mozgásidő hány km/h sebességnek felel meg 22 km/h-nál és 12,5 órás mozgásidőnél?
5. A TCR-középmezőnyben mi a szűk keresztmetszet, és miért nem a watt?
6. Mennyi az álló idő nem-alvás része egy felső harmados TCR-en, és hova megy?
7. Hány kilométert „ér” egy óra alvás 24 km/h-nál — és miért nem a mezőny adatából derül ki?
8. Hogyan csal a pulzus hőségben, a harmadik napon és a verseny végén?
9. Mit csinál a rutinos versenyző 35 °C fölött, és mit nem?
10. Mennyivel lassít a rossz csomagolás vagy a védett gumi 150 W-on, és mennyi wattot kérne ugyanaz a különbség?

:::you
**Ne halaszd** a 2. tesztet: a következő brevet-ed erre tökéletes, és nem kerül semmibe. A 3. teszt egy délelőtt, és több km/h-t hozhat, mint egy hónap edzés. {fix}
:::
:::

:::page type=osszefoglalo level=alap disc=all
## A modul egy oldalon

| | |
| --- | --- |
| **Mindenki lassul** {ev:B} · 24 órás csúcs az FTP 55–70 %-a, RAAM 1,8–2,1 W/kg, TCR 1,5 W/kg. Folyamatos 24 óra: −37 % watt; pihenőkkel tagolva −12 %. A jó tempó a kevésbé ingadozó. | **A rajt ára** {ev:B} · Saját átlag fölötti első órák → kevesebb táv (r = −0,58, futás); pulzus 86 → 66 % max. A gyors rajt a jobb versenyzők *tünete*, nem receptje. |
| **Fáradtságállóság** {ev:A} · 2 óra után CP −9 %; szénhidrát (60 g/h) megvédi; az intenzitás dönt, nem a kJ; egyéni szórás 1–32 %. A bél plafonja 550–650 kcal/h ≈ 130–165 W. | **Az idő matematikája** {ev:C} · Napok = táv / (sebesség × mozgásóra). +1 óra mozgás ≡ sebesség/mozgásóra km/h. Középmezőny: a megállás; él: a sebesség. |
| **Mozgó és álló idő** {ev:B} · TCR mezőny 50 %, felső harmad 70–76 %, él 78 %; az álló idő nagyobb fele nem alvás (3–4,5 h/nap bolt, evés). | **Alvás mint sebesség** {ev:C} · 1 óra alvás ≈ 0,8 × mozgósebesség km (≈ 20 km). Mezőnyszinten „több alvás = lassabb” — műtermék; személyen belül a kevesebb alvás ront. |
| **A sebesség fizikája** {ev:C} · Validált modell, levezetett számok: 150 W síkon 32 / 29 / 28 km/h (CdA 0,25 / 0,35 / 0,40); védett gumi −0,6 km/h; 1 kg ≈ 30–40 perc a TCR-en. | **Mutatók** {ev:A} · Watt méri a munkát; pulzus hőségben fel (valós), több napon le (csal), a végén fel (zavar, nem erő); érzés/pulzus arány jelzi az alvás- és energiahiányt. |
| **Időjárás** {ev:A} · Fordított U: 10–20 °C olcsó, 30 °C+ és 0–5 °C drága; 35 °C fölött ritmuseltolás; éjjel −11 % watt (n = 1). | **Versenyzők** {ev:C} · Egyetértés: mozgáshányad ≥80 %, rajt a saját átlag alatt, feldarabolás. Eltérés: alvásadag (1–4 h), távcél típusa. |

**Egyéni mezők, amiket csak teszt tölt ki:** fáradt teljesítmény · mozgáshányad és az álló idő bontása · légellenállási felület · hőség-küszöb. {egyéni}

**A három legerősebb bizonyíték:** a fáradtságállóság intenzitásfüggése (kontrollált labor), a teljesítmény–sebesség modell (terepen validált), a hőmérséklet fordított U-ja. **A három leggyengébb:** a „km/óra alvás” átváltás (modell), a túl gyors rajt ára kerékpáron (futóadat és egyedi esetek), és minden, ami a harmadik napon túli fáradtságállóságról szól.

QR → kísérőoldal: időköltségvetés-kalkulátor, versenyterv-sablon, önellenőrző kvíz.

**Szószedet.** *Pozitív tempó* — a vége lassabb, mint az eleje. *Kritikus teljesítmény (CP)* — a tartósan fenntartható legnagyobb teljesítmény; *W′* — az e fölötti rövid tartalék. *FTP* — egyórás küszöbteljesítmény. *Fáradtságállóság (durability)* — mennyit veszítesz hosszú munka után. *Mozgáshányad* — mozgásidő / eltelt idő; „az ébren töltött időre” jelzéssel az alvás nélküli változat. *CdA* — légellenállási felület, m². *Crr* — a gördülési ellenállás együtthatója. *RPE* — érzett erőkifejtés. *HRV* — pulzusvariabilitás. *Normalizált teljesítmény* — az ingadozó watt „élettani átlaga”.
{: .small }

**Bizonyíték-jelek (4 sávtól 1-ig):** összesített kutatás · terepvizsgálat · szakmai tapasztalat · feltörekvő (részletesen: 04. modul). A hivatkozások sorszáma modulon belüli; a teljes lista a könyv végi irodalomjegyzékben és a kísérőoldalon.
{: .small }
:::
