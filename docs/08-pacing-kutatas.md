# 08 · Pacing és versenystratégia — kutatási összefoglaló (v0.1, 2026-09-19)

## Hogyan készült

Négy párhuzamos kutatóügynök, tizenegy kérdés (Q1–Q11), 113 új forrás (A: 20, B: 44, C: 44, D: 5) a `data/sources.yaml`-ban `08:` előtagú kérdéskulccsal; a pilot tanulságaként minden kulcsszámhoz a forrás eredeti mondata (`quote` mező). DOI csak ott, ahol kiadói/Crossref oldalon látható volt (56 tétel); a többinél `doi: null` és megjegyzés. Meglévő 04-es forrásokra (RAF-vizsgálat, Ridefar, Hayden, Wilcox, Strasser stb.) az ügynökök csak hivatkoztak. A nyers kimenetek: `data/raw/08-A…D-sources.yaml` és `-evidence.md`; a bizonyíték-térképek teljes szövege e dokumentum második felében.

## A modul tíz kulcsállítása (a bizonyíték-térkép sűrítménye)

1. **Ultrán a fenntartható intenzitás alacsony, és a hosszal esik:** 24 órás elit csúcs 210–272 W (2,8–3,5 W/kg, az FTP ~55–70 %-a); szóló RAAM 1,8–2,1 W/kg (141–170 W, NP ~160 W); 14 napos TCR ~109 W (1,5 W/kg). Folyamatos 24 óra alatt a watt −37 %, a pulzus −22 %; pihenőkkel tagolva (váltó, 75 h) csak −12 %. [rothschild-2021-ultracyclist B; knechtle-2015-24h-road B; schumacher-2011-raam B; brayson-2019-tcr B]
2. **Mindenki lassul (pozitív tempó); a kérdés a lassulás mértéke és ingadozása.** 24 órás futáson a tempó ingadozása (CV) és a táv r = −0,64; a saját átlaghoz képest gyors rajt r = −0,58 az összteljesítménnyel (n = 501). Kerékpáron csak n = 1 esetek és a RAAM-mezőny leíró adata: a top 3 abszolút értékben gyorsabban rajtol és tovább tartja — ez a nagyobb kapacitás tünete, nem stratégia. [inoue-2019-24h-pacing B; bossi-2017-24h-running B; heidenfelder-2016-raam-pacing B; neumayr-2004-rata B]
3. **A fáradtságállóság (durability) az intenzitástól függ, nem a kJ-tól:** 2 óra CP alatti munka után a CP −9 %, a W′ már 80 perc után esik; 60 g/h szénhidrát a CP-esést megszünteti; ~2000 kJ <70 % CP alatti munka után profiknál nincs esés, 5×8 perc CP fölött igen. Egyéni szórás <1–32 %. [clark-2019-cp-dynamics A; spragg-2024-intensity A; spragg-2023-durability A; jones-2024-resilience C]
4. **A pulzus többnapos versenyen három irányba „csal”:** hőségben felfelé (valós: VO2max −19 % 35 °C-on), többnapos terhelésnél lefelé (azonos wattnál napról napra alacsonyabb, 94 bpm-es plató; HRmax is csúszik), TCR végén ismét felfelé (U-alak, R² 0,63). Ezért a pulzuszóna önmagában nem tempóvezérlő eszköz ultrán. [wingo-2005-cvdrift A; schumacher-2011-raam B; fesseler-2026-raam58 B; brayson-2019-tcr B]
5. **Az RPE alváshiány és energiadeficit után felfelé csal a pulzus és a VO2 nélkül; az RPE:pulzus arány érzékenyebb jel, mint a nyers pulzus; a HRV reggeli szűrő, nem tempó-jel** (túlterhelésnél is nőhet). Gyakorlati szintézis: watt = a leadott munka mérésére; pulzus = 1–2. napi túlrajtolás és hőség jelzésére; RPE:pulzus = alváshiány/energia; HRV = reggeli szűrő. [martin-1981-sleep-rpe A; roberts-2019-cycling A; bellenger-2016-hrv-meta A]
6. **Mozgáshányad: a teljes TCR-mezőny ~50 %, a felső harmad 70–76 %, az élmezőny ~78 % (első 24 óra ~100 %); Tour Divide rekorderek <25 % álló idő, középmezőny ~38 %; PBP-n ~74 %.** Az álló idő nagyobbik fele nem alvás (Bartholmoes: 60 h-ból 15–30 h alvás; 1216 km-en 31 megállás × 36 perc). [white-2016-ridefar-method C; evans-2022-bikeradar-bartholmoes B; mckenzie-dotwatcher-tcr12-briefing-2026 B; toone-2016-pbp-southern B; giuliani-2023-morton-tourdivide B]
7. **Időköltségvetés: napok = táv / (mozgósebesség × napi mozgásóra); egy óra plusz mozgás ≡ v/h km/h sebesség.** TCR-középmezőnyben (22 km/h, 12,5 h) 4000 km-en +1 km/h = −15 h, +1 h mozgás = −26 h, −30 perc álló idő = −13 h; +1 km/h síkon +13 W-ot kíván (150→163 W). A középmezőny szűk keresztmetszete a logisztika, az élé a sebesség. [ridefar-time-efficiency C; white-2016-ridefar-method C; martin-1998-model A (levezetés)]
8. **Alvás–sebesség: mért „km/óra alvás” kerékpáron nincs.** A modell szerint 1 óra alvás ≈ 0,8–0,85 × mozgósebesség ≈ 20–22 km; a mezőnyszintű „több alvás = lassabb” (RAF R² 0,66) a pályán töltött idő műterméke; személyen belül a kevesebb alvás rontja a reakcióidőt és az álmosságot (5,3 h/nap alatt halmozódik). A 2020 utáni TCR-győztesek 3–4 h/éj sávban konvergálnak. [hurdiel-2026-raf B; guilherme-2026-ultra A; mckenzie-dotwatcher-tcr-2026 C; gemperle-apidura-2026 C]
9. **Energia mint tempóplafon:** terepen 52–57 g szénhidrát/óra a bevitel (az ajánlott 90 g/h ~60 %-a), napi deficit 1500–3100 kcal; a fenntartható bevitel ~2,5× alapanyagcsere; zsírból ~290 kcal/h → a „tüzelőanyag-plafon” 550–650 kcal/h ≈ 130–165 W tartósan — egybevág a mért ultra-átlagokkal. [geesmann-2014-1230km B; black-2012-384km B; thurber-2019-alimentary B; maunder-2018-mfo B]
10. **A sebesség fizikája terhelt bringán:** CdA 0,25 (aerobar, csupasz) → 0,31–0,35 (hoods, jól pakolt táskák, mért) → 0,40 (terhelt alap) → 0,42–0,48 (táskatartó); Crr 0,003–0,005 aszfalt, 0,006–0,008 érdes/4 évszakos, 0,008–0,015 murva; 150 W síkon 85 kg-mal 32,4 / 29,2 / 28,1 km/h (CdA 0,25 / 0,35 / 0,40); 1 kg ≈ 30–40 perc a 3900 km-es TCR-en; −0,8 % légsűrűség és −0,6 % teljesítmény 100 méterenként. [martin-1998-model A; frank-2021-tailfin-aero B; grappe-1997-obree B; brr-test-method B; white-2016-ridefar-resistance C]

**Versenyzői konvergencia (Q10, 9 témasor):** a különbséget a mozgáshányad adja, nem a sebesség (Ride Far ≥80 %, CTS 94 %, Hughes ≤5 perc/óra, Allegaert „könnyebb menni, mint újraindulni”); rajttempó a saját fenntartható átlaghoz képest konzervatív, miközben az élboly az első 24 órát frissen, alvás nélkül használja ki (600+ km); hőségben ritmuseltolás (hajnali rajt, éjfélig tekerés, a legmelegebb órákban tudatos lassítás + hűtés-megállás), nem nappali alvás; „bad patch”: feldarabolás és nem-döntés („20 percig meg tudod csinálni?”, „éjjel sose adj fel”). Eltérés: alvásadag (Wilcox/Hayden/Gemperle 3–4 h vs. Sehili „nem áll meg”, RAAM 1–1,5 h) és napi távcél (Ride Far számszerű +5 % tartalék vs. Hayden folyamatcél).

## Ellentmondások, amiket a modulnak explicit módon kezelnie kell

- **E1 — „Lassan rajtolj” vs. „a győztesek gyorsan rajtolnak”.** Futáson a legjobbak a saját átlagukhoz képest lassan kezdenek; RAAM/PBP-n az élboly abszolút értékben gyorsabb. Feloldás: relatív vs. abszolút rajtsebesség — a mérce mindig a saját fenntartható átlag; a gyors rajt szelekció, nem recept.
- **E2 — Mozgásidő dönt vs. mozgósebesség dönt.** TCR-él: 26,0 vs. 26,2 km/h, +2 h mozgás nyert; Tour Divide: Morton 30 % állással 34 órával verte Hall <25 %-át, mert 20,5 vs. ≤17 km/h-val mozgott. Feloldás: ha a sebességkülönbség >10 %, az többet ér, mint 5–10 pont mozgáshányad; 1 %-on belül a mozgásidő dönt. A modul „melyik a szűk keresztmetszet?” kérdésként tanítja.
- **E3 — Pulzus-drift kettős természete** (hőségben valós intenzitás-emelkedés, többnapos versenyen lefelé csúszás, TCR végén felfelé): ugyanaz a mutató három irányba csal — ezért a modul mutatónként adja meg, mikor mire jó.
- **E4 — Alvás keresztmetszetben vs. személyen belül** (mint a 04-ben): csak a személyen belüli irány használható ok-okozatként; a mezőnyszintű korreláció a pályán töltött idő függvénye.
- **E5 — Éjszakai tekerés hőség ellen vs. éjszakai wattveszteség** (RAAM-váltó: nappal 212 W, éjjel 189 W): 35 °C felett a délutáni veszteség (labor −17 % / −6,5 %) nagyobb; 25–30 °C-nál a csere nem biztos — a hőmérsékleti küszöb nem ismert.
- **E6 — Dehidráció: laborban lineáris kár, terepen 4 %-ig nincs** (önszabályozott tempónál a szervezet a tempóban fizeti meg); és **HRV „magas = jó” vs. paraszimpatikus túlsúly** (túlterhelésnél is nő).
- **E7 — Aerobar-nyereség szórása** (ΔCdA 0,014–0,057 m² forrástól és referenciahelyzettől függően) és **táskatartó-hátrány** (0,025 vs. 0,07–0,10 m²): a modul sávot ad, és saját mérésre (Chung-módszer) buzdít.

## Bizonyítékhiányok (ahol a modul csak „legjobb becslést” adhat)

- Nincs kontrollált összehasonlítás egyenletes / pozitív / változó tempóstratégia között 6 óránál hosszabb kerékpáros eseményen; a „túl gyors rajt ára” számszerűen csak futásból van.
- Nincs watt- vs. pulzus- vs. RPE-vezérelt tempózást összehasonlító vizsgálat ultrán; RPE-adat többnapos kerékpáros versenyről nincs.
- Napról napra bontott watt-görbe szólóversenyről nem publikált; PBP 1200 km-ről semmilyen fiziológiai terepadat; női ultrakerékpáros intenzitásadat nincs.
- Nincs mért „km/óra alvás”; nincs lektorált tracker-elemzés az álló idő összetevőiről (navigáció, mechanika, ellenőrzőpont időköltsége forrás nélkül).
- Nincs mért Crr laza murvára / Tour Divide-felületre; nincs CdA-mérés aerobaros és teljesen táskázott bringára; a Martin-modell 15–25 km/h-n, terhelten, fáradtan nem validált.
- Nincs ultrakerékpáros terepvizsgálat nappali pihenő vs. hűtéssel áttekerés hőségben; a szélablak csak heurisztika.
- Minden durability-vizsgálat ≤4 órás; a többnapos „átvitt CP-esés” mérése nem létezik; validált többnapos érkezésbecslő (alvás + megállás + durability + időjárás) nincs.

## Feltörekvő irányok (a modul „feltörekvő” jelével)

Egyéni durability-profilozás („fáradt CP”) a %FTP helyett; intenzitás-súlyozott terhelésszámítás versenyen belül; folyamatos többcsatornás verseny-monitorozás (CGM, watt, pulzus, alvás) valós idejű tempó- és etetéskorrekcióval; valós idejű maghő-alapú pacing (CORE — trendjelző, nem küszöb: az adatpontok 45–51 %-a 0,3 °C-on belül); gépi tanulásos érkezésbecslés (n = 1, MAE 6,6 perc); tracker-adattudomány (DotWatcher álló idő-statisztikák) mint a jövő nyilvános adatforrása; Hazard Score (RPE × hátralévő hányad) ultrára kalibrálva.

## Döntést igénylő pontok (Attila)

- [ ] **Kalkulátor köre.** A modul webes eszköze időköltségvetés-kalkulátor lenne (táv, mozgósebesség, alvás, egyéb álló idő → napok; érzékenység: +1 km/h vs. +1 h mozgás vs. −30 perc állás), presetekkel (TCR-középmezőny, felső harmad, él; Tour Divide; PBP 90 h a kontrollzárási sebességekkel), és opcionális fizikai réteggel (watt → sebesség a Martin-modellből: CdA, Crr, tömeg, lejtés, szél, magasság). Kérdés: a fizikai réteg is ebbe a modulba kerüljön, vagy a 09 Felszerelés modul eszköze legyen (ott a CdA/Crr választás a téma)?
- [ ] **Saját adat.** A modul példái közé beleférne a te TCR-célod: 4000 km, saját mozgósebesség és alvásterv → napok — csak ha szeretnéd; a szöveg enélkül is teljes.
- [ ] **Hőség-küszöb.** Az E5 ellentmondásnál a modul „35 °C felett ritmuseltolás, alatta egyéni” szabályt adna, jelölve, hogy a küszöb nem mért. Elfogadható?
- [ ] **Durability-teszt mint feladat.** A 15. oldali „mérd be magad” része lenne egy 2 órás CP alatti előterhelés utáni 20 perces teszt (fáradt FTP %). Ez edzésbe illesztendő — Nándival egyeztetendő később, de a leírás bekerülhet most?
- [ ] Elfogadod-e a tíz kulcsállítást mint a modul gerincét?

---

# Bizonyíték-térképek kérdésenként (a négy ügynök nyers kimenete, változatlanul)


## Csomag A

Készült: 2026-09-18. Új forrásdefiníciók: `data/raw/08-A-sources.yaml` (32 tétel). A meglévő forrástárból hivatkozott, itt nem újradefiniált kulcsok: `roberts-2019-cycling`, `hurdiel-2026-raf`, `lahart-2013-raam`, `nedelec-2022-camaron`, `ridefar-time-efficiency`, `strasser-pez-2019`.
Fokozat: A = meta-analízis/RCT/kontrollált labor; B = terepvizsgálat, esettanulmány mért adattal; C = narratív áttekintés, edzői/versenyzői közlés; D = feltörekvő.

---

## Q1 — Mért intenzitás többnapos és 24 órás ultrakerékpáros versenyeken; durability

### Számszerű állítások

1. **A 24 órás szóló csúcsteljesítmény elit szinten 210–272 W (2,8–3,5 W/kg), ~121–136/perc átlagpulzussal, és ez az FTP ~55–70%-a.** Rothschild esettanulmánya: 861,6 km, 210 W (2,8 W/kg), 121 bpm; Knechtle 2015-ös országúti rekord 896 km, 250,2 W; a 2019-es pályarekord 941,9 km, 214,5 ± 23,7 W; Strasser 2021-es 1026 km-es rekordja edzői közlés szerint 272 W / 136 bpm, 400 W-os FTP-hez képest ~68%. [rothschild-2021-ultracyclist B; knechtle-2015-24h-road B; knechtle-2019-24h-track B; strasser-inscyd-2022 C]

2. **Folyamatos 24 órán belül a teljesítmény 30–40%-kal, a pulzus ~20%-kal csökken, lineáris vagy négyfázisú lefutással.** Rothschild: -37% teljesítmény, -22% pulzus 24 óra alatt. Knechtle 2015: a sebesség és a watt körről körre lineárisan esett (r = -0,79 / -0,85). Knechtle 2019: 0–4. óra stabil, 4–9. óra a legnagyobb esés, 9–22. óra plató, utolsó 2 óra hajrá. [rothschild-2021-ultracyclist B; knechtle-2015-24h-road B; knechtle-2019-24h-track B]

3. **Többnapos szóló RAAM-on az átlagos leadott teljesítmény 1,8–2,1 W/kg (141–170 W), a normalizált teljesítmény ~160 W, a pulzus 94–120/perc – azaz a pihent LT/aerob küszöb környéke vagy alatta.** Schumacher befutója (10 nap 23 óra): 141 ± 76 W (1,8 W/kg), 117 ± 14 bpm, LT 2,37 W/kg. Strasser (8 nap 1 óra): NP 162 W, TSS 3173; interjúban "160/170 W átlag, ami nálam regeneráló tekerés", FTP 5 W/kg. A 2026-os 58 éves RAAM-eset: tekerés alatti pulzus 94 bpm-es platóra süllyedt. [schumacher-2011-raam B; strasser-power2max-2018 C; strasser-pez-2019 C; fesseler-2026-raam58 B]

4. **Self-supported (TCR) 14 napos versenyen a napi átlagteljesítmény ~109 W (~1,5 W/kg), 23,1 km/h, 247 perc alvás/nap – a mozgásidő nagy része nagyon alacsony intenzitású.** [brayson-2019-tcr B] Kontraszt: napi alvással futó szakaszversenyen (Transalp, 8 nap) az átlagpulzus 85,4% HRmax, a versenyidő 36%-a a magas zónákban – tehát a "többnapos" önmagában nem mondja meg az intenzitást, a nap közötti alvás dönt. [wirnitzer-2008-transalp B]

5. **Váltós RAAM-ban (2 és 4 fős) az intenzitás 2,3–2,8 W/kg, 186–214 W, a laktátminimum-teljesítmény 69–85%-a; 2 fős váltóban 75 óra tekerés alatt csak 12% a teljesítményesés (vs. 37% a folyamatos 24 órán).** Nappal 212 W, éjjel 189 W (p < 0,001). [manunzio-2016-raam-team B; rothschild-2021-ultracyclist B; lahart-2013-raam B]

6. **Az elsőnapi túlrajtolás elit ultrakerékpárosoknál is mérhető: a HRátlag/HRmax a rajtnál 0,86, a végén 0,66 (-23%), ~10% csökkenés 10 óránként; az "ultraendurance küszöb" ~68–70% HRmax.** 10 elit férfi, Race Across the Alps (525 km, 27 óra): 53% <70% HRmax, 25% 70–80%, 19% 80–90%, 3% >90%. [neumayr-2004-rata B]

7. **A RAAM-mezőny 2010–2014 adatai szerint mindenki pozitív pacinget mutat, de a top 3 gyorsabban rajtol, magasabb csúcsteljesítményt ér el és tovább tartja, mielőtt lassul.** [heidenfelder-2016-raam-pacing B] Ezzel összhangban a pacing-szakirodalom szerint >4 órás eseményekre "optimális" stratégia nincs bizonyítva; a jól edzettek jellemzően pozitív pacinget alkalmaznak. [abbiss-2008-pacing C]

8. **Durability: 2 óra CP alatti ("heavy") kerékpározás után a kritikus teljesítmény ~9–10%-kal esik (260 → 236 W), a W' már 80 perc után (17,9 → 14,7 kJ, 2 óra után 13,8 kJ); 60 g/h szénhidrát a CP-esést megszünteti (254 W), a W'-ét nem.** Az egyéni CP-esés <1% és ~32% között szór. [clark-2019-cp-dynamics A; jones-2024-resilience C]

9. **A durability-t a korábbi munka intenzitása, nem a kJ-mennyisége határozza meg: ~2000 kJ <70% CP alatti munka után a CP és a 12 perces teljesítmény nem esett profiknál, míg 5×8 perc 105–110% CP után a 3 perces és a sprintteljesítmény igen.** [spragg-2024-intensity A] Aki alacsony intenzitáson kevesebb szénhidrátot éget és hatékonyabb, kevesebbet veszít a CP-jéből (ΔCP vs. CHO-oxidáció 200 W-on r = -0,70; vs. bruttó hatásfok r = 0,87; VT1 r = 0,75–0,83). [spragg-2023-durability A]

10. **Amatőröknél 1000 kJ munka után a sikeres versenyzők 20 perces teljesítménye 6,5%-kal, a kevésbé sikereseké 12,5%-kal esett – a pulzusválasz nem különbözött.** [barsumyan-2025-durability-amateur A] Ultratávon a lecsengés nem feltétlenül centrális: Tour Divide után (16 nap, 16,8 óra/nap) a VO2max és a maximális teljesítmény nem változott, miközben a mitokondriális és endotél-funkció romlott. [hyldahl-2024-tourdivide B]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q1)
- Nincs lektorált, teljesítménymérős adat a **Transcontinental Race-ről** egyetlen eseten (Brayson) kívül, **Tour Divide-ról** verseny alatti W/pulzus nincs (Hyldahl csak pre/post), **Paris-Brest-Paris 1200 km-ről** semmilyen fiziológiai terepvizsgálatot nem találtam.
- Minden ultra-esettanulmány **n = 1–10, férfi**; női ultrakerékpáros intenzitásadat lektorált forrásban nincs (Heidenfelder közli, hogy a nők lassabbak, de W-adatot nem).
- A **napról napra csökkenő teljesítmény** számszerű görbéje többnapos szólóversenyen sehol nincs publikálva; csak összesített százalékok (Rothschild -12% 6,5 nap alatt váltóban; Strasser ">250 W" első nap → NP 162 W) és pulzusgörbék (Brayson U-alak, Fesseler 94 bpm plató).
- A **durability** vizsgálatok mind 2 órás vagy 1000–2000 kJ-os laborprotokollok profikkal/amatőrökkel; ultra-időtartamra (10–100×) extrapoláció, ezt a módszertani áttekintés is korlátként rögzíti. [hunter-2025-durability-methods C]
- A Strasser-számok (162 W NP, 272 W 24 h, 160/170 W átlag) gyártói/edzői/interjú-közlések, nem lektoráltak. [strasser-power2max-2018 C; strasser-inscyd-2022 C; strasser-pez-2019 C]

### ELLENTMONDÁS (Q1)
- **"Lassan rajtolj" vs. "a győztesek gyorsan rajtolnak".** Neumayr adatai (0,86 HRmax a rajtnál, majd -23%) és a 24 órás rekordok lineáris lecsengése a túlrajtolás fiziológiai árát mutatják, Heidenfelder viszont azt találta, hogy a RAAM top 3 gyorsabban és nagyobb teljesítménnyel rajtolt, és tovább tartotta. Feloldás: a gyors rajt a nagyobb kapacitás és a jobb durability tünete (Spragg, Barsumyan), nem stratégiai ok – a "pozitív pacing" leíró, nem előíró. [neumayr-2004-rata B; heidenfelder-2016-raam-pacing B; barsumyan-2025-durability-amateur A]
- **Alvásminimalizálás vs. rendszeres pihenő.** Schumacher befutója 45 óra alvással (5 óra/nap) 10 nap 23 óra alatt ért célba, Strasser 14 óra teljes szünettel 8 nap alatt; a szerzők "egyformán sikeres" alternatívának nevezik a sok alvást, de a két eset teljesítményszintje összemérhetetlen (63 vs. ~80+ ml/kg/perc VO2max-tartomány, 141 vs. 162+ W). [schumacher-2011-raam B; strasser-power2max-2018 C]
- **Folyamatos vs. szakaszos terhelés lecsengése.** Ugyanaz a sportoló 24 órán -37%, 6,5 napos váltóban -12% – a "napról napra esik a watt" tézis a pihenőkkel tagolt formátumban gyengébb, mint a folyamatosban. [rothschild-2021-ultracyclist B]

---

## Q7 — Mi szabályozza jól a tempót többnapos terhelés alatt: watt, pulzus, RPE, RPE:pulzus, HRV

### Számszerű állítások

1. **Többnapos ultrán a pulzus azonos wattnál napról napra csökken, ezért a pulzuszóna-tartás "lefelé csal" (több wattot kényszerít ki).** Schumacher RAAM-esete: szegmensenként stabil teljesítmény mellett szignifikánsan eső átlagpulzus; Fesseler: tekerés alatti pulzus 94 bpm-es platóra süllyedt, a W:pulzus arány a 7. napig esett; Neumayr: -10% HRátlag/HRmax minden 10 órában; Rothschild: -22% pulzus 24 óra alatt. [schumacher-2011-raam B; fesseler-2026-raam58 B; neumayr-2004-rata B; rothschild-2021-ultracyclist B]

2. **A pulzus 14 napos self-supported versenyen nem monoton: U-alakú (R² = 0,63), az 5. napon 111 bpm minimum, ~7. nap fordulópont, a 14. napon 158 bpm – a verseny végén emelkedő pulzus kronotróp zavar, nem "több erő".** [brayson-2019-tcr B] Halmozódó fáradtságnál a csúcspulzus is lejjebb csúszik (182 → 176 bpm 3 hét túlterhelés után), a HRR +8 bpm-mel gyorsul. [aubry-2015-overreaching-hrr A]

3. **Hőségben a pulzusdrift NEM hamis jel: 45 perc alatt 35 °C-ban a pulzus +12% (151 → 169), a VO2max -19% (4,4 → 3,6 l/perc) – a relatív intenzitás valóban nő, a watt-tartás a csaló.** [wingo-2005-cvdrift A] Elit kerékpárosok 32 °C-on önszabályozva 6,5%-kal kevesebb wattot választanak azonos végbélhőmérséklet mellett. [tatterson-2000-heat A]

4. **Kiszáradásnál a maghő- és pulzusemelkedés, valamint a verőtérfogat-esés arányos a testtömeg-veszteséggel (1,1–4,2%; r = 0,98 a maghőre).** [montain-1992-dehydration A] Ugyanakkor kültéri önszabályozott időfutamon 2,2 ± 1,0% (max. 4%) kiszáradás nem rontotta a teljesítményt (+0,06%), a szomjúság szerinti ivás +5,2%-kal jobb, mint az alatta maradó ivás. [goulet-2011-dehydration-meta A]

5. **Alváshiány után az RPE "felfelé csal", a pulzus és a VO2 nem mozdul: 36 óra ébrenlét után a kimerülésig tartó idő -11%, az RPE szignifikánsan nagyobb, a pulzus és az anyagcsere változatlan.** [martin-1981-sleep-rpe A] Kerékpáron egy éjszaka teljes alvásmegvonás után az időfutam -10%, és az RPE:átlagpulzus arány nő – az arány érzékenyebb, mint a nyers pulzus. [roberts-2019-cycling A]

6. **Energiadeficit után a fenntartható tempó (CP) ténylegesen lejjebb tolódik, és ezt a szénhidrát visszaadja: 2 óra után -9% CP placebóval, 60 g/h CHO-val nincs esés.** [clark-2019-cp-dynamics A] RAAM alatt a vércukor napi 0,92 mg/dl-rel csökkent, 21 169 kcal deficit mellett; a monitorozás valós idejű tempó/etetés-korrekciót tett lehetővé. [fesseler-2026-raam58 B]

7. **A HRV többnapos versenyen a napi terhelést tükrözi (RPE r = 0,46; TRIMP r = 0,60), de napi teljes alvással nem halmozódik; amatőröknél 3 nap után 24 óra alatt sem áll helyre.** [barrero-2019-tdf-hrv B; swart-2023-mtb-hrv B] A nyugalmi HRV a pozitív adaptációnál (RMSSD SMD 0,58) és a túlterhelésnél (SMD 0,26) is nőhet, ezért önmagában nem különbözteti meg a jó és rossz állapotot; a pulzusgyorsulás csökkenése (SMD -0,48) a jobb fáradtságjel. [bellenger-2016-hrv-meta A]

8. **A durability-különbséget a pulzus nem mutatja: 1000 kJ után 6,5% vs. 12,5% teljesítményesés azonos pulzusválasz mellett.** [barsumyan-2025-durability-amateur A] Ezért a teljesítménymérő a leadott munka egyetlen közvetlen mérője; a pihent FTP-re számolt zónák viszont a 10. óra után más fiziológiai állapotot jelölnek. [maunder-2021-durability C; jones-2024-resilience C]

9. **Az RPE a legintegráltabb jel (hő, glikogén, alvás együtt), az anticipatív szabályozás modellje szerint a tempó RPE-vezérelt csökkenése védő mechanizmus.** [tucker-2009-anticipatory C] Az edzői "aerob szétcsatolódás" (Pw:Hr) heurisztika: <5% jó, 5–10% fáradtság, >10% aerob küszöb feletti terhelés – edzésdiagnosztika, verseny alatt a drift természetes. [friel-decoupling-tp C]

10. **Gyakorlati szintézis a forrásokból (nem egyetlen vizsgálat eredménye):** watt = a leadott munka mérésére (napi célok, hegyek plafonja); pulzus = korai (1–2. nap) túlrajtolás és hőség/kiszáradás jelzésére felfelé, később már csak "lefelé csal"; RPE:pulzus arány = alváshiány és energiadeficit jelzője; HRV = reggeli szűrő, nem tempó-jel. [schumacher-2011-raam B; wingo-2005-cvdrift A; roberts-2019-cycling A; bellenger-2016-hrv-meta A]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q7)
- **Nincs olyan vizsgálat, amely ultrakerékpáron összehasonlítaná a watt-, pulzus- vagy RPE-vezérelt tempózást** (RCT vagy keresztezett terep). Minden ajánlás labor-mechanizmusokból (2 óra, 45 perc) és n = 1 esetleírásokból van összerakva.
- **RPE-adat többnapos kerékpáros versenyről** gyakorlatilag nincs; a hurdiel-2026-raf álmossági/kognitív adatokat ad, nem RPE-t. [hurdiel-2026-raf B]
- **A csökkenő HRmax versenyközi mérése** nincs; az Aubry-féle 6 bpm-es esés edzési túlterhelésből származik (triatlon).
- **Alváshiány + kiszáradás + hőség együttes hatása** a pulzusra és RPE-re nem vizsgált; a Goulet-féle "szomjúságra igyál" 2–3 órás időfutamokból jön, alváshiányos szomjúságérzet-tompulásra nincs forrás.
- **HRV verseny közben** (nem reggeli nyugalmi) ultrán nincs adat; a Barrero/Swart adatok szakaszversenyekről származnak.
- A Friel-féle 5%-os decoupling-küszöb nem validált.

### ELLENTMONDÁS (Q7)
- **A pulzusdrift kettős természete.** Rövid távon/hőségben a felfelé drift valós intenzitás-emelkedést jelez (Wingo: VO2max -19%), többnapos versenyen viszont a domináns jelenség a lefelé csúszó pulzus (Schumacher, Fesseler, Neumayr, Aubry), a TCR-esetben pedig a végén ismét felfelé (Brayson). Ugyanaz a mutató három különböző irányba "csal" a verseny különböző szakaszaiban – ez a fő ok, amiért a pulzus önmagában nem alkalmas több napos tempóvezérlésre. [wingo-2005-cvdrift A; schumacher-2011-raam B; brayson-2019-tcr B]
- **Dehidráció: laborban lineáris kár, terepen 4%-ig nincs kár.** Montain (kontrollált, 2 óra, melegben) vs. Goulet (kültéri, önszabályozott TT). A feloldás a szabályozás módja: önszabályozott tempónál a szervezet a dehidráció árát a tempóban fizeti meg, nem "romlik" a teljesítmény a kitűzött watthoz képest. [montain-1992-dehydration A; goulet-2011-dehydration-meta A]
- **HRV: "magas = jó" vs. paraszimpatikus túlsúly.** Bellenger meta-analízise szerint a nyugalmi RMSSD túlterhelésnél is nő; Aubry szerint a gyorsabb HRR a funkcionális túledzés jele. Az ultrán mért "jó HRV" tehát félreolvasható. [bellenger-2016-hrv-meta A; aubry-2015-overreaching-hrr A]

---

## Feltörekvő irányok (D-szintű, figyelni érdemes)
- **Folyamatos többcsatornás verseny-monitorozás** (CGM-glükóz, pulzus, watt, alvás, izomtónus) valós idejű tempó- és etetéskorrekcióval – a 2026-os RAAM-eset feasibility-szintű bizonyíték. [fesseler-2026-raam58 B]
- **Egyéni durability-tesztelés** (fáradt CP / ΔCP, 1000–2000 kJ utáni 12–20 perces teszt) mint ultra-tempóterv alapja; a <1–32%-os egyéni szórás miatt "% FTP" helyett "fáradt CP %" lehet a jövő mértéke. [jones-2024-resilience C; spragg-2023-durability A; hunter-2025-durability-methods C]
- **Szénhidrátbevitel mint a CP védelme** (60 g/h laborban, 105–116 g/h Strasser 24 órás rekordján) – a pacing és a táplálkozás összekapcsolása. [clark-2019-cp-dynamics A; strasser-inscyd-2022 C]
- **Pulzusgyorsulás / HRR mint fáradtságjel** a nyugalmi HRV helyett – edzésadat, versenyen nem tesztelt. [bellenger-2016-hrv-meta A; aubry-2015-overreaching-hrr A]
- A Brayson-féle **késői pulzusemelkedés** gyakorisága más versenyzőknél nyitott kérdés (a szerzők maguk jelölik kutatási iránynak). [brayson-2019-tcr B]

## Nem sikerült megnyitni (ezért nem szerepel, vagy csak absztrakt-szinten)
- **Périard és mtsai 2011**, "Cardiovascular strain impairs prolonged self-paced exercise in the heat", Exp Physiol 96(2):134-144, DOI 10.1113/expphysiol.2010.054213 (Crossrefen látva) – Wiley/PubMed/Semantic Scholar mind blokkolt; számokat nem tudtam idézni, ezért kimaradt.
- **Wingo, Ganio, Cureton 2012**, "Cardiovascular drift during heat stress: implications for exercise prescription", Exerc Sport Sci Rev 40(2):88-94 (DOI Crossrefen látva) – absztrakt nem elérhető (LWW 402, ResearchGate 403); helyette a 2005-ös MSSE-vizsgálat szerepel.
- **Coyle & González-Alonso 2001** (ESSR, kardiovaszkuláris drift klasszikus áttekintés) – nem próbáltam tovább, mert az LWW 402-t ad; helyette Montain 1992 + Wingo 2005.
- **Bescós és mtsai 2012**, "High energy deficit in an ultraendurance athlete in a 24-hour ultracycling race" (PMC3310508) – PMC reCAPTCHA; kimaradt.
- **Van Erp, Sanders, Lamberts 2021** (durability profi országúti versenyeken, MSSE) – LWW blokk; a Spragg-cikkek fedik.
- **PubMed** oldalak a legtöbb esetben üres metaadatot adtak vissza (csak a rothschild-2021 nyílt meg); **Europe PMC REST** és **Semantic Scholar API** tartósan 429-et adott; **Crossref** működött.
- Tour Divide / TCR / PBP teljesítménymérős, lektorált terepadatot a fentieken túl nem találtam (keresés: "Transcontinental Race power", "Tour Divide physiological", "Paris-Brest-Paris heart rate").

## Csomag B

Kérdések: **Q2** tempóstratégia ultra-távon · **Q5** alvás–sebesség átváltás · **Q8** energiabevitel mint tempókorlát
Készült: 2026-09-18. Forrástár: `raw/08-B-sources.yaml` (24 új kulcs) + hivatkozott kulcsok a `data/sources.yaml`-ból és a `raw/08-A-sources.yaml`-ból.
Jelölés: [kulcs FOKOZAT; megjegyzés]. A = meta/RCT/kontrollált labor; B = terepvizsgálat mért adattal; C = narratív/edzői/versenyzői; D = feltörekvő.
Analógia-jelölés: (FUTÁS) / (VITORLÁZÁS) / (TÚRA) – nem kerékpáros adat.

---

## Q2 – Tempóstratégia ultra-távon (egyenletes vs. változó, pozitív/negatív split, a túl gyors rajt ára)

1. **Ultra-távon a mezőny gyakorlatilag mindig pozitív tempóval (lassulva) halad; az „egyenletes” stratégia a valóságban a „kevésbé lassuló” stratégiát jelenti.** Az Abbiss–Laursen-tipológia szerint a >4 órás eseményekre az optimális stratégia ismeretlen, a jól edzettek jellemzően pozitív pacinget mutatnak [abbiss-2008-pacing C]. 24 órás országúti kerékpár-rekordon a sebesség körről körre lineárisan esett (r = -0,79 távolság vs. sebesség), pályán négyfázisú (tartás → 4–9. órában esés → plató → hajrá) [knechtle-2015-24h-road B; knechtle-2019-24h-track B; n=1]. RAAM-on a szólómezőny sebessége minden időállomáson csökkent [heidenfelder-2016-raam-pacing B; absztrakt].

2. **A tempó ingadozása – nem a lassulás ténye – jósolja a teljesítményt: a nagyobb variációs együttható (CV) kevesebb megtett távot jelent.** 24 órás futáson a jó teljesítményű férfiak CV-je 21,5 ± 4,8%, a gyengébbeké 27,2 ± 3,0%; az összes táv és a CV között r = -0,64 (férfi), -0,47 (nő), a jelentős sebességcsökkenések számával r = -0,47/-0,61 [inoue-2019-24h-pacing B; (FUTÁS) n=51]. 937 futónál a CV a formátum hosszával nő (6 h 0,12 → 12 h 0,18 → 24 h 0,22), és a gyorsabbaknál kisebb (r = -0,47 – -0,64) [deusch-2021-timelimited B; (FUTÁS)].

3. **A túl gyors rajt mérhető ára: aki a saját átlagához képest gyorsan kezd, kevesebbet tesz meg 24 óra alatt.** 501 futónál az első 2 óra normalizált sebessége és az összteljesítmény között r = -0,58 (p < 0,001); a leggyorsabb csoport (180,5 km) alacsonyabb relatív intenzitással indult, mint a leglassabb (97,2 km) [bossi-2017-24h-running B; (FUTÁS)]. 100 km-en a legjobbak az első három 10 km-es szakaszon szignifikánsan alacsonyabb RELATÍV sebességgel futnak, a végén magasabbal [renfree-2016-100km B; (FUTÁS) absztrakt]. A klasszikus 100 km-es adat: a leggyorsabbak a kezdősebesség 15%-án belül maradtak és ~50 km-ig tartották a tempót, a leglassabbak 1,4 ± 0,7 m/s-ot lassultak az A csoport 0,5 ± 0,2 m/s-ával szemben [lambert-2004-100km B; (FUTÁS) n=67].

4. **Kerékpáros terepen az abszolút gyors rajt viszont a jobb versenyzők tulajdonsága – a „relatív” és az „abszolút” rajtsebességet szét kell választani.** A RAAM top 3 gyorsabban és nagyobb teljesítménnyel rajtolt, magasabb csúcsot ért el és tovább tartotta, mielőtt lassult [heidenfelder-2016-raam-pacing B]. PBP 2023-on a 84/90 órás csoportban az időn belül célba érők 1. szakaszos medián sebessége magasabb volt, mint a DNF/időn túlieké [cyclecharts-pbp-2023 C; kontroll-idők, nem lektorált]. Elit RATA-mezőnyben azonban a rajt 0,86 HRmax-ról 0,66-ra esett – a túl magas abszolút rajtintenzitás fiziológiai lenyomata [neumayr-2004-rata B].

5. **A „gyorsabb = egyenletesebb” összefüggés nem lineáris: a mezőny alja is egyenletes, a közép a legingadozóbb.** Spartathlonon (n=2598) a leglassabb ÉS a leggyorsabb csoport kisebb sebességváltozást mutatott, mint a két középső (p < 0,01); mindenki lassult az első 7 ellenőrzőpontig, majd a cél felé gyorsított (fordított J) [knechtle-2022-spartathlon B; (FUTÁS)]. A fordított J (utolsó órák gyorsulása) 24 órás futáson is megjelenik, de az utolsó óra sebessége nem függ össze a végeredménnyel (r = 0,03) [bossi-2017-24h-running B].

6. **Terepen (domb, szél) a változó teljesítmény – nem a változó sebesség – az optimum: a lejtővel/széllel párhuzamos ±10% W azonos átlagteljesítménynél időt nyer.** 40 km-es modellben 126 s (±10% lejtő), 51 s (±4,4 m/s szél), 26 s (sík) [atkinson-2007-variable-power A; modell, DOI nem ellenőrizve]. Ultrára az elv (légellenállás ∝ v³) átvihető, a ±10% W-ingadozás órákon át tartó költsége nem modellezett.

7. **A tempóváltoztatás szabályozója az RPE × hátralévő távolság-hányad („Hazard Score”): 3 fölött a lassulás gyakorlatilag kikényszerül.** [dekoning-2011-hazard A; rövid laborfutamok]. Az ultrán ez önellenőrző szabály: ha a rajt utáni órákban (hátralévő hányad ≈ 1) az RPE már 3 fölött van, a pozitív split elkerülhetetlen – ugyanez a kerete az anticipatív szabályozásnak [tucker-2009-anticipatory C].

8. **Többnapos versenyen a napi távolság lecsengése kisebb, mint a folyamatos 24 órásé, mert a pihenő „visszaállít”.** Ugyanannál az elit versenyzőnél 24 órás szóló: -37% teljesítmény; RAAM 2 fős váltóban 75 óra alatt: -12% [rothschild-2021-ultracyclist B; n=1]. TCR-en (14 nap) a napi táv 140–410 km között szórt, átlag 109 W [brayson-2019-tcr B; n=1]. TCR No12 első 7 napján az élen ~489 km/nap, ~26 km/h mozgósebesség; a napi táv versenyzőnként ±100–185 km-t ingadozott [mckenzie-dotwatcher-tcr-2026 C]. Tour Divide 2026 5. napján az éllovas 438 km / 16 h 27 min, majd >6 óra megállás [homer-bikepacking-tourdivide-2026 C].

9. **Brevet-mezőnyben (PBP) a bruttó sebesség hét évtizede 15–16 km/h, a leggyorsabbaké 23–28 km/h – a különbség döntően a megállási időből fakad, nem a mozgósebességből.** Átlagidő 1948: 78:37 (15,6 km/h), 1975: 73:10, 2019: ~78 h; leggyorsabb 1948: 51:15, 2015: 42:26 [storbeck-2019-pbp-speeds C]. Kontrollonkénti sebesség-lecsengést egyik forrás sem közöl számmal.

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q2)
- **Nincs kontrollált összehasonlítás** (RCT vagy keresztezett terep) egyenletes vs. pozitív vs. változó stratégia között 6 óránál hosszabb kerékpáros eseményen; minden kerékpáros adat n=1 esettanulmány [knechtle-2015/2019, rothschild-2021, brayson-2019, schumacher-2011] vagy leíró mezőnyelemzés absztraktból [heidenfelder-2016]. A 2008-as Abbiss–Laursen-hiány lényegében ma is fennáll.
- A „túl gyors rajt ára” számszerűen csak futásból van (r = -0,58; 15%-os sáv; 0,5 vs 1,4 m/s) – kerékpárra csak az elv vihető át.
- 24 órás kerékpárversenyek szakaszsebesség-lecsengése mezőnyszinten (nem rekordkísérlet) nem publikált; PBP kontrollonkénti sebességprofil szintén nincs (a cyclecharts csak az 1. szakaszt és a hosszú megállásokat elemzi).
- TCR/Tour Divide/RAAM napi táv-alakulása csak tracker-alapú, nem lektorált kommentárokból; nincs nyilvános, tisztított adatsor.
- A változó-teljesítmény modellek (Atkinson 2007) 40 km-esek; a többórás W-ingadozás glikogén-/izomkár-költsége nincs mérve.

### ELLENTMONDÁS (Q2)
- **Relatív vs. abszolút rajt:** futáson a legjobbak a saját átlagukhoz képest lassan kezdenek [bossi-2017; renfree-2016; lambert-2004], a RAAM top 3 és a PBP-befutók viszont abszolút értékben gyorsabban rajtolnak [heidenfelder-2016; cyclecharts-pbp-2023]. Feloldás: a gyors rajt a felkészültség jele (szelekció), nem stratégia; a mérce mindig a saját fenntartható átlag.
- **Lineáris vs. U-alakú** „gyorsabb = egyenletesebb”: Inoue/Deusch lineáris, Spartathlon U-alak (a leglassabbak is egyenletesek, mert a cut-offhoz igazodnak) [knechtle-2022-spartathlon].
- **Egyenletes sebesség vs. egyenletes teljesítmény:** a pacing-irodalom „even pacing”-je sebességre vonatkozik, a modellek szerint terepen az egyenletes SEBESSÉG változó TELJESÍTMÉNYT kíván [atkinson-2007] – a tankönyvben a kettőt nem szabad összemosni.

---

## Q5 – Alvás–sebesség átváltás számszerűen

1. **A gyakorlati modell: napi táv = ébren töltött óra × mozgáshányad × mozgósebesség; az alvás az ébrenléti órákat, nem a sebességet csökkenti közvetlenül.** 15 ébren töltött óra, 24 km/h és 85% mozgáshányad → 306 km/nap; 75% → 270 km/nap; a versenytartomány 75–85% [ridefar-time-efficiency C]. Egy órányi extra alvás ebben a modellben 0,8–0,85 × mozgósebesség km-t „ér” (24 km/h-nál ≈ 20 km; 26 km/h-nál ≈ 22 km) – **ez modellszámítás, nem mérés**.

2. **Az élen a különbséget a mozgásidő adja, nem a sebesség.** TCR No12, 7. nap: 25,97 vs. 26,21 km/h mozgósebesség, de a vezető „majdnem két órával többet volt mozgásban” → ≈50 km ≈ a teljes előny [mckenzie-dotwatcher-tcr-2026 C; tracker-becslés]. Középmezőnyben fordítva: egy Tour Divide-befutó 14 h 49 min tekerés / 18 h 12 min versenyidő naponta (≈81% mozgáshányad) 221 km/nap-ot adott ~15 km/h-val; ugyanennyi mozgásidő 20 km/h-val ~300 km/nap lenne [halfwayanywhere-tourdivide-2024 C; n=1].

3. **Keresztmetszetben a többet alvó versenyző lassabb – de ez a „pályán töltött idő” műterméke, nem az alvás oksági hatása.** Race Across France 2024: helyezés = -22,03 + 0,33 × alvásperc, R² = 0,655 (~100 perc → ~5. hely, ~300 perc → ~75. hely), az alvásidő a versenyidővel R² = 0,83 [hurdiel-2026-raf B; teljes szöveg]. Ultrafutás: kumulált alvás vs. célidő r = 0,44 (n=1154) [kishi-2024-ultramarathon B], r = 0,44–0,48 a 36 órán túli versenyeken [martin-2018-habits B]; 326 km-en a gyorsabbak 1,8 h, a lassabbak 9,0 h aludtak (73,6 vs. 88,5 h befutó) [bianchi-2022-200mile-case B; (FUTÁS) n=4]. Szisztematikus szintézis: 16 vizsgálat, 1389 sportoló, a gyorsabbak kevesebbet vagy egyáltalán nem aludtak [guilherme-2026-ultra A; konfundált].

4. **Személyen belül viszont a kevesebb alvás rontja a másnapi reakcióidőt és álmosságot – az egyetlen „sebesség-jellegű” személyen belüli szám egy n=1 futóeset: +1 óra alvás ≈ +0,5 km/h átlagsebesség (866 km-es Transpyrenea).** [guilherme-2026-ultra A → Biorci-esettanulmány, MÁSODLAGOS; az eredeti nem nyílt meg]. RAF: napi <5,29 h alvásnál az álmosság napról napra nőtt, a kevesebb alvás lassabb reakcióidővel járt [hurdiel-2026-raf B]. Laborból: a 30 percnél hosszabb terhelés romlik jobban alvásmegvonás után (SMD -0,52) [lopes-2023-endurance A], ébren töltött óránként -0,36–0,55%/h [craven-2022-akut A], a mérsékelt intenzitású munka romlik, a 20 perces időfutam nem [gattoni-2025-recovery A].

5. **A verseny alatti alvás tipikus mennyisége kerékpáron: 95–306 perc/24 h (RAF, 5–8 nap) [hurdiel-2026-raf B]; 247 perc/nap (TCR, 14 nap) [brayson-2019-tcr B]; ~5 h/nap szóló RAAM-befutónál, 45 h alvás 11 nap alatt [schumacher-2011-raam B]; 2,4 h/24 h alatt RAAM-váltóban, a 6 órás pihenőben ~3× annyi tényleges alvás, mint a 3 órásban [lahart-2013-raam B]; 5:13 h/éjszaka 24 napos, 432 km/nap teljesítménynél [nedelec-2022-camaron B].** A RAAM-győztesek 6–15 óra összalvással 7–11 nap alatt [raam-sleepcom-2022 C].

6. **A hosszú (≥3 h) megállás hiánya brevet-en DNF-fel jár együtt.** PBP 2023: a DNF/időn túli versenyzők 43%-a nem rögzített 3 óránál hosszabb megállást, a befutóknak csak 14%-a; a befutók messzebb jutottak az első hosszú megálló előtt [cyclecharts-pbp-2023 C]. Ok-okozat nem bizonyított (aki bajban van, nem ér oda az alvásig).

7. **Verseny ELŐTTI alvásnyújtás a leginkább „ingyen” sebesség: UTMB-n az alvásidőt megnövelők gyorsabban értek célba, mint az alvásmegvonásra „edzők” (p = 0,026)** [poussel-2015-utmb-sleep B; (FUTÁS) másodlagos idézet]. Ezzel szemben 200+ mérföldön a verseny előtti éjjel <7 h alvás jósolta a felső kvartilist – valószínűleg zavaró változó [lynch-2025-200mile B].

8. **Edzői/versenyzői ökölszabályok: 4 napnál rövidebb eseményen min. ~1,5 h/éjszaka, hosszabbon átlag ~3 h; „bölcsebb túl sokat aludni és gyorsan tekerni”** [hayden-sleeping-guide C]; elit: 2–3 órás blokk + power napek, középmezőny 4–6 h/éjszaka [ridefar-sleeping C]; 16–18 h mozgásidő → 4–6 h alvás [bikepacking-ultraguide-2019 C]; TCR-győztes ~4 h/éjszaka [kolbinger-euronews-2019 C].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q5)
- **Nincs mért „km/óra alvás” átváltás kerékpáron.** Minden szám vagy keresztmetszeti korreláció (RAF, Kishi, Martin, Bianchi), vagy modell (Ridefar), vagy n=1 futóeset (Biorci +0,5 km/h/óra, csak másodlagosan). Egy személyen belüli, napról napra vezetett alvás → másnapi mozgósebesség/mozgáshányad elemzés (tracker + aktigráf) hiányzik – ez lenne a tankönyv „alvás-egyenletének” tényleges alapja.
- A mozgáshányad-modell a bolti/evési/alvási megállásokat együtt kezeli; az alvás „megtérülése” (pihenés utáni magasabb mozgósebesség, kevesebb navigációs hiba) nincs számszerűsítve – Hayden „sleep drunk” eltévedés-példája anekdota.
- A RAF-vizsgálat saját ábráját a szerzők ellentétesen értelmezik (több alvás = jobb helyezés) [hurdiel-2026-raf notes]; a DotWatcher-recepció ezt vette át [dotwatcher-moresleep-2026 D; fizetőfal].
- Stampi 99 vitorlázós terepvizsgálata (polifázisos alvás és helyezés) – a DOI ellenőrizve, de az absztrakt egyik elérhető oldalon sem nyílt meg, ezért számai nem idézhetők.
- Alvásmennyiség és DNF kapcsolata kerékpáron nincs vizsgálva (a PBP-adat csak „hosszú megállás”, nem alvás).

### ELLENTMONDÁS (Q5)
- **Keresztmetszet vs. személyen belül:** a mezőnyszintű „több alvás = lassabb” [hurdiel-2026-raf; kishi-2024; bianchi-2022; guilherme-2026] szemben a személyen belüli „kevesebb alvás = rosszabb reakcióidő/álmosság, alacsonyabb sebesség” [hurdiel-2026-raf személyen belüli elemzés; guilherme-2026 Biorci-sor]. A tankönyvben csak a személyen belüli irány használható ok-okozatként.
- **Verseny előtti alvás:** UTMB-n a nyújtás gyorsít [poussel-2015], 200+ mérföldön a rövidebb alvás jár jobb helyezéssel [lynch-2025] – mindkettő önbevallás, konfundált.
- **Elit gyakorlat vs. tudomány:** a győztesek 1,5–4 h/éjszaka [raam-sleepcom-2022; kolbinger-2019; mckenzie-2026], a laborirodalom szerint már egy éjszaka alvásvesztés -5,5% állóképesség [craven-2022] – a feloldás a durability-plafon: az ultrán a fenntartható intenzitás olyan alacsony (1,5–2,7 W/kg) [brayson-2019; schumacher-2011], hogy a -5%-os kapacitásesés kevésbé korlátoz, mint az elvesztett mozgásóra.

---

## Q8 – Energiabevitel mint tempókorlát (rövid, a 03 modul témája)

1. **Felszívódási plafon: egyetlen CHO-forrásból ~60 g/h (1–1,1 g/perc exogén oxidáció), glükóz+fruktózból ~90 g/h ajánlás 2,5 óra fölött; 120 g/h-nál az exogén oxidáció tovább nő, a teljesítményelőny bizonytalan.** [jeukendrup-2014-personalized C; podlogar-2022-newhorizons C; 2–3 órás labor, edzett kerékpárosok]. Az ajánlás testtömegtől és edzettségtől független [jeukendrup-2014].

2. **Terepen az ultrakerékpárosok a plafon 55–65%-át viszik be, és a második félben tovább esik.** 1230 km/43 h: 57,1 ± 17,7 g CHO/h, 618 km után szignifikáns csökkenés; folyadék 392 ml/h [geesmann-2014-1230km B; n=14, absztrakt]. 384 km/16 h: 52 g CHO/h, 18,7 MJ bevitel a 25,5 MJ igényre; a nagyobb bevitel rövidebb idővel járt (p = 0,023, r² = 0,283) [black-2012-384km B; n=18, absztrakt]. ISSN (futás): 150–400 kcal/h, 30–50 g CHO/h; a bevitel a forgalom 36–53%-a [tiller-2019-issn-ultra C].

3. **Napi deficit többnapos ultrán: 1500–3000+ kcal/nap még váltóban és csoportos versenyen is.** RAAM 4 fős váltó (DLW): 6420 kcal/nap forgalom, 4918 bevitel, 1503 kcal/nap deficit [hulton-2010-raam-energy B; absztrakt-tükör]. 1230 km: 25 303 – 19 749 ≈ 5500 kcal / 43 h (≈3100 kcal/nap) [geesmann-2014-1230km B]. Szóló RAAM, 58 év: becsült összdeficit 21 169 kcal / 11 nap (≈1900 kcal/nap), -2,3 kg [fesseler-2026-raam58 B; absztrakt]. Tour Divide 16 nap: az első 9 napban energiaegyensúly DLW-vel, testtömeg változatlan [hyldahl-2024-tourdivide B; n=1].

4. **Metabolikus plafon: a fenntartható energiaBEVITEL ~2,5× BMR (2,36 ± 0,59×), az esemény hosszától független; e fölött a raktárak fogynak.** RAUSA-futók: 1. hét 6202 kcal/nap (3,76× BMR) → utolsó hét 4906 (2,81×), 140 napos átlag 3,11×; TdF 4–5× BMR csak 23 napig [thurber-2019-alimentary B]. Ultrakerékpáron 1–2 hét alatt 4–5× BMR a norma → a deficit tervezendő, nem hiba.

5. **A bél a szűk keresztmetszet, nem az izom: ha a nap felében nem tekersz, a bevitel 3,7–4,1× BMR forgalomnál is egyensúlyban tartható.** 30 napos, 155 → 118 km/nap kanadai átkelés (DLW): PAL 3,71–4,11, stabil testtömeg [purcell-2025-canada B; n=2, nem verseny]. Versenytempónál (16+ h nyereg) az evésre/emésztésre jutó idő és az étvágy (éjszaka, hő) a korlát.

6. **Zsíroxidáció: edzett állóképességi sportolónál MFO 0,53 ± 0,16 g/perc (0,40–0,67), Fatmax 56 ± 8% VO2max → ≈290 kcal/h zsírból (saját átszámítás).** Edzéssel az MFO nő, a Fatmax-intenzitás nem; Ironmanon MFO–idő r = 0,35 [maunder-2018-mfo B]. Következmény a tempóra: ~300 kcal/h zsír + ~250–350 kcal/h felszívott CHO ≈ 550–650 kcal/h fenntartható „üzemanyag-plafon” → 20–22% mechanikai hatásfoknál ≈ 130–165 W tartós – egybevág a mért ultra-átlagokkal (109 W TCR, 141 W RAAM, 210–250 W 24 h-n glikogénből is) [brayson-2019-tcr; schumacher-2011-raam; knechtle-2015-24h-road; rothschild-2021-ultracyclist B].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q8)
- 120 g/h fenntarthatósága 6+ órán át, illetve több napon át: nincs adat (a 120 g/h vizsgálatok 2–3 órásak).
- Szóló RAAM/TCR kettős jelölt vizes energiaforgalma: csak n=1 esetek [hyldahl-2024; fesseler-2026 becsült]; a Knechtle 2005 RAAM-energiaforgalom esetleírás nem nyílt meg.
- „Bél edzése” (gut training) ultra-specifikus bizonyítéka: csak rövid távú labor (Jeukendrup 2014 említi), ultrakerékpáros terepen nincs.
- A „metabolikus plafon → fenntartható W” láncolat (6. pont) saját levezetés: hatásfok, zsír/CHO arány és egyéni MFO nélkül ±30%-os hibasáv.

### ELLENTMONDÁS (Q8)
- **2,5× BMR plafon [thurber-2019] vs. 3,7–4,1× BMR egyensúlyban [purcell-2025]:** feloldás – a plafon a bevitelre vonatkozik ÉS az evésre fordítható időtől függ; a Thurber-adatbázis futó/expedíciós események, ahol a mozgás a nap nagy részét kitölti. Ultrakerékpáron a 24 h-s nonstop formátum Thurber, a 8–10 h/nap túra Purcell felé húz.
- **„Több bevitel = gyorsabb” [black-2012] vs. fordított ok-okozat:** aki bírja a tempót (alacsonyabb relatív intenzitás), tud enni; a magas intenzitás önmagában csökkenti a felszívódást – megfigyeléses adat, irány nem bizonyított.
- **90 g/h ajánlás [jeukendrup-2014] vs. 52–57 g/h terepi valóság [black-2012; geesmann-2014] vs. 30–50 g/h ISSN-futó ajánlás [tiller-2019]:** a kerékpáros ultra a kettő között; a tankönyvi cél 60–80 g/h reális, 90+ g/h csak edzett béllel és 24 h alatt.

---

## Feltörekvő irányok
- **Személyen belüli alvás→sebesség modellezés tracker + aktigráf adatból** (RAF-típusú vizsgálat kiterjesztése mozgósebességre/mozgáshányadra) – ez adná a hiányzó „km/óra alvás” számot. [hurdiel-2026-raf B nyomán; D]
- **Folyamatos többcsatornás monitorozás (CGM, pulzus, teljesítmény, alvás) valós idejű tempó- és etetéskorrekcióhoz** [fesseler-2026-raam58 B; n=1, D-szintű alkalmazás].
- **Hazard Score / RPE-alapú önszabályozó szabályok ultrára adaptálva** (RPE × hátralévő hányad küszöbök 6+ órás eseményre nem kalibráltak) [dekoning-2011-hazard A → D].
- **Tracker-alapú tömeges pacing-elemzés (TCR/TD/PBP)**: a DotWatcher és cyclecharts-típusú elemzések adatai lektorált feldolgozás nélkül – nyitott lehetőség egy 24 h-s / brevet kontrollonkénti lecsengés-adatbázisra [mckenzie-dotwatcher-tcr-2026; cyclecharts-pbp-2023 C].
- **120 g/h + hidrogél/„gut training” ultrán** [podlogar-2022 C; D].
- **Fordított J tempó és a „hajrá-tartalék” tudatos tervezése** (utolsó 2 óra nem korrelál a végeredménnyel → a tartalék inkább biztonsági, mint teljesítménytényező) [bossi-2017; knechtle-2022 B].

## Nem sikerült megnyitni
- **Stampi C. (1989) Polyphasic sleep strategies improve prolonged sustained performance: a field study on 99 sailors. Work & Stress 3(1):41-55, DOI 10.1080/02678378908256879** – DOI Crossref-en ellenőrizve, absztrakt (T&F 403, PsycNet robots, Semantic Scholar üres) nem elérhető → számai nem idézhetők.
- **Biorci et al. – Transpyrenea 866 km, n=1 alvás–átlagsebesség esettanulmány** (a guilherme-2026-ultra 33. hivatkozása) – a hivatkozásjegyzék az MDPI-oldal csonkolt betöltése miatt nem nyílt meg; csak másodlagosan idézve.
- **Poussel 2015 (UTMB alvásstratégia)** – kiadói absztrakt (T&F 403, PubMed CAPTCHA, ResearchGate 429); számok másodlagos forrásból (kishi-2024, Nikolaidis 2023).
- **Hulton 2010, Geesmann 2014, Black 2012, Atkinson 2007** – kiadói oldal 403, Crossref/Europe PMC 429 a munkamenet második felében; absztraktok repozitóriumi/tükör-oldalról, DOI nem ellenőrizve.
- **Knechtle B. et al. (2005) Energy turnover at the Race Across AMerica (RAAM) – a case report, Int J Sports Med** – csak ResearchGate „Request PDF”.
- **Bescós R. et al. (2012) High energy deficit in an ultraendurance athlete in a 24-hour ultracycling race** – PMC3310508 CAPTCHA, PubMed CAPTCHA.
- **Brager A.J. et al. (2020) Earlier shift in race pacing can predict future performance during a single-effort ultramarathon under sleep deprivation, Sleep Science** – DOAJ-absztrakt megnyílt (a 100 mérföldes befutók korábban lassultak, mint a DNF-esek), PMC teljes szöveg CAPTCHA; számok nélkül a térképbe nem került.
- **Escape Collective „How the Tour Divide was won” (2023)** – megnyílt, de napi táv/alvás számot nem tartalmaz (Joe Nation: „300 km és 4–5 óra alvás/nap az első héten” célkitűzés).
- **Wells & Marwood (2016) Effects of power variation on cycle performance during simulated hilly time-trials, EJSS** – Wiley 403.
- **DotWatcher „More Sleep = Higher Race Ranking?” (2026)** – fizetőfal (lásd dotwatcher-moresleep-2026 D a meglévő tárban).

## Csomag C

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

## Csomag D

Készült: 2026-09-18/19. Új forrásdefiníciók: `data/raw/08-D-sources.yaml` (30 tétel). A meglévő forrástárból (`data/sources.yaml`) hivatkozott, itt nem újradefiniált kulcsok – az idézeteket az URL újranyitásával nyertem ki: `hayden-sleeping-guide`, `allegaert-apidura-2016`, `wilcox-rouleur-2024`, `wilcox-roadman-2026`, `sehili-breakaway`, `strasser-pez-2019`, `ridefar-time-efficiency`, `kolbinger-euronews-2019`, `hall-bikepacking-2016`. A 08-A/08-B csomagból hivatkozott kulcsok: `manunzio-2016-raam-team`, `heidenfelder-2016-raam-pacing`, `neumayr-2004-rata`, `tatterson-2000-heat`, `spragg-2023-durability`, `spragg-2024-intensity`, `hunter-2025-durability-methods`, `jones-2024-resilience`, `barsumyan-2025-durability-amateur`, `clark-2019-cp-dynamics`, `mckenzie-dotwatcher-tcr-2026`, `storbeck-2019-pbp-speeds`, `strasser-inscyd-2022`, `atkinson-2007-variable-power`, `brayson-2019-tcr`, `cyclecharts-pbp-2023`.
Fokozat: A = meta-analízis/RCT/kontrollált labor; B = terepvizsgálat, tracking-elemzés mért adattal; C = narratív áttekintés, edzői/versenyzői tapasztalat; D = feltörekvő, nem validált.

---

## Q9 — Napszak- és időjárás-stratégia: hőség, hideg, eső, szél a napi tervben

1. **Hőségben az önszabályozott teljesítmény mérhetően esik – rövid terhelésen 40 °C-on ~17%-kal kevesebb munka, 32 °C-on 30 perces időfutamon ~6,5%-kal kisebb átlagteljesítmény –, és a munkaráta csökkentése nem hiba, hanem a testhőmérséklet szabályozásának viselkedéses eszköze.** A konszenzus-ajánlás ezért a rajtidő időjárás szerinti ütemezését, hosszabb hűtési szüneteket és verseny közbeni belső hűtést (jégkása) javasol. Ultrán az abszolút intenzitás (FTP 55–70%-a, többnapos versenyen ~1,8–2,1 W/kg) jóval alacsonyabb, így a hőtermelés kisebb – a százalékok nem vihetők át egy az egyben, az irány igen. [periard-2021-heat-review C; racinais-2015-heat-consensus C; tatterson-2000-heat A]

2. **A teljesítőképesség a hőmérséklet függvényében fordított U: 70% VO2max-on kimerülésig 10,5 °C-on 93,5 ± 6,2 perc, 30,5 °C-on 51,6 ± 3,7 perc, és 4 °C-on is rövidebb, mint 11 °C-on; maratonon az optimum 3,8–9,9 °C, felette négyzetes lassulás és több feladó.** Gyakorlati fordítás: a 10–20 °C-os reggel/este az „olcsó kilométer", a 30 °C feletti délután és a 0–5 °C-os hajnali leereszkedés egyaránt a „drága sáv". [galloway-1997-temperature A; elhelou-2012-marathon-weather B]

3. **Hideg esőben ugyanaz a sebesség többe kerül: 5 °C-on esőszimuláció mellett a nyelőcső- és bőrhőmérséklet alacsonyabb, a VO2 és a laktát magasabb volt, mint száraz kontrollban** – vagyis esőben a tempót nem a watt, hanem a hőháztartás korlátozza, és az átöltözésre/melegedésre fordított álló idő nem veszteség, hanem befektetés. [ito-2013-rain-cold A] Versenyzői oldalról az eső elsősorban morált rombol: Broadwith LEJOG-rekordján a skót esőben „minden pozitivitást kivertek belőlem". [broadwith-cyclingweekly-2018 C]

4. **A versenyzői gyakorlatban a hőség kezelése nem „nappali alvás", hanem a napi ritmus eltolása: hajnal előtti indulás, éjfélig tekerés, a legmelegebb órákban tudatos lassítás és hűtés-megállók.** Walker (All Points North): a hajnal előtti rajt nyáron azért előnyös, mert a déli hőség előtt le lehet tudni a távot; Shaw: pihenő 22:00-ig, nyeregben 02:00 előtt; Muller (24 h vb): „During the hottest part of the day I slowed myself down … not trying to push through when my body wouldn't allow", és körönként megállt jégzoknit cserélni; a Ride Far: „Riding more at night and resting more during the day can obviously help to avoid extreme heat." [dotwatcher-nightstarts-roundtable C; muller-precisionhydration-2017 C; ridefar-schedule C] Kísérős RAAM-on a sivatagot inkább áttekerik hűtéssel (fagylalt, jég), nappali pihenőről egyik RAAM-forrás sem beszél. [baloh-nduranz-2024 C; goldstein-cbc-2021 C]

5. **Az éjszakai tekerés nem ingyenes: mért adaton (2 fős RAAM-váltó) nappal 212 W, éjjel 189 W (p < 0,001), azaz ~11%-kal alacsonyabb teljesítmény** – a hőség elkerülése és az éjszakai wattveszteség (cirkadián mélypont, látás, kialvatlanság) között kell átváltani; Muller a leghidegebb/legsötétebb órákra (02–04 h) és napkeltére időzíti a koffeint. [manunzio-2016-raam-team B; muller-precisionhydration-2017 C] Britton (edző) szerint a kialvatlan versenyzőnél „slower reaction times, poorer decision making, higher levels of risk taking" – az éjszakai tempó kockázati ára az alvás-modulban részletezett. [dotwatcher-nightstarts-roundtable C]

6. **Szél: a versenyzői heurisztika szerint „Winds tend to decrease when the sun goes down", ezért a szeles/sík szakaszt érdemes éjszakára tenni; az előrejelzést útvonalválasztásba építik (több változat a navigációs eszközön, a helyszínen a melegebb/szárazabb/kevésbé szeles opció).** Ez meteorológiailag a nappali termikus szélre igaz, frontális szélre nem – lektorált ultra-adat nincs. [ridefar-schedule C; ridefar-route-planning C] A változó teljesítmény szél/lejtő szerinti optimalizálását modellen (40 km) igazolták, órákra/napokra nem. [atkinson-2007-variable-power B]

7. **Hideg nyitószakasz tracker-adaton (TCR No.12, 2026): az első éjjel 1 → −1 °C (egy fejegységen −3 °C), a kumulált top 10 mégis csak 5–31 perc álló időt mutatott, a legjobb nyitónapi mozgósebesség 28,75 km/h; a hideg egy versenyzőnél extra nyújtás-megállásokat kényszerített ki.** Az élboly tehát a hideget ruházattal és nem megállással kezeli; a mezőny ugyanabban a versenyben téli hajnalból görög nyárba tart – a napi terv időjárás-függő újratervezése a TCR-ben strukturális. [mckenzie-2026-tcr12-frozen B]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q9)
- **Nincs ultrakerékpáros terepvizsgálat**, amely a nappali pihenő + éjszakai tekerés stratégiát összevetné a „hűtéssel áttekerni" stratégiával; minden hőség-szám rövid (15–90 perces) laborterhelésből vagy maratonból származik.
- A „szélablak" (éjszakai szélcsend) állítás versenyzői heurisztika; szélsebesség–napi táv összefüggést tracker-adaton senki nem elemzett.
- Eső hatása az álló időre (átöltözés, menedék) és a bivakminőségre nincs számszerűsítve; csak morál-anekdota (Broadwith) és felszerelési tanács (Hager: „clearly under-equipped").
- RAAM sivatagi hőségtaktika (Strasser, Baloh, Goldstein) csak interjú-parafrázisokban; a stáb hűtési protokolljáról (jég, mennyiség, gyakoriság) nyilvános, hivatkozható crew-guide-ot nem találtam.
- A hőségben kialakuló hidratációs/görcs-problémák tempóköltsége (Baloh: „lower the tempo … increased hydration and waited") n=1 anekdota.

### ELLENTMONDÁS (Q9)
- **Éjszakai tekerés hőség ellen vs. éjszakai wattveszteség:** a Ride Far és a szervezői kerekasztal a hőség elkerülésére az éjszakát ajánlja [ridefar-schedule; dotwatcher-nightstarts-roundtable], a mért RAAM-váltó adat szerint éjjel ~11%-kal kisebb a leadott teljesítmény [manunzio-2016-raam-team]. Feloldás: a 35 °C feletti délután vesztesége (labor: 17% / 6,5%) nagyobb, mint az éjszakai; 25–30 °C-nál viszont nem biztos, hogy megéri a cserét – a hőmérsékleti küszöb nem ismert.
- **Optimális hőmérséklet:** futáson 4–10 °C [elhelou-2012-marathon-weather], kerékpáron laborban ~11 °C, és 4 °C már rosszabb [galloway-1997-temperature] – a menetszél miatt a kerékpáros optimum feljebb tolódik, a hideg hajnali leereszkedés viszont a labornál is hidegebb effektív hőmérsékletet jelent.
- **„Sose adj fel éjjel" [ridefar-schedule] vs. Britton kockázati figyelmeztetése**: a döntés-halasztás mentálisan védő, a kialvatlan éjszakai tekerés viszont biztonsági kockázat – a tankönyvben a kettőt a „megállni igen, feladni nem" formulával lehet összeegyeztetni.

---

## Q10 — Konvergencia: versenyzők, edzők, stábok, szervezői elemzések

### KONVERGENCIA-MÁTRIX

| Téma | Egybevágó tapasztalat [kulcsok] | Eltérő gyakorlat [kulcsok] | Amitől függ |
|---|---|---|---|
| **Rajttempó** | „Túl korán túl sok" mindig visszaüt: Muller „overdoing it early on will almost always come back to bite you later"; CTS: plafon a laktátküszöb ~65%-án a rajttól, „you can lose more time in the second half than you can possibly gain in the first half"; Hughes: tervezett sebesség 0,5–1,0 mph-val az edzésszint alatt; Graham: „keep enough in the tank to look after themselves the next day" [muller-precisionhydration-2017; rutberg-cts-2016; hughes-rbr-2015; evans-bikeradar-2024] | Az élboly abszolút értékben gyorsan indul és nem áll meg: TCR top 10 első nap 5–31 perc állás, 600+ km az első 24 órában; Wilcox: „never really at max capacity except for maybe at the beginning when all the gaps are established"; Sehili: „giving 100% all the time"; Gemperle „all-in" az elejétől; Baloh viszont Strassert követve begörcsölt [mckenzie-2026-tcr12-frozen; ridefar-schedule; evans-bikeradar-2024; sehili-breakaway; gemperle-apidura-2026; baloh-infinity-2020] | Saját fenntartható átlaghoz mérve mindenki „lassan" indul; a győzelemért versenyzők az első napot frissen, alvás nélkül használják ki – a középmezőnynek ez nem másolható |
| **Napi távcél és alakulása** | Élboly: ≥600 km első 24 h, majd 400–450 km/nap; 300 km/nap = rajtolók felső 20%-a; 240–280 = mezőnyközép; +5% tartalék betervezése; a frissesség az első napokon a legnagyobb [ridefar-schedule; hager-transiberica-2022 (297 km/nap, 18. hely)] | Hayden elutasítja a merev „X km/nap" tervet („on the third day, when it rains crazy … what do you think will happen?"), helyette „amennyit csak tudok"; Bialek: a terv helyszíntől, időjárástól, közérzettől függ [hayden-confidence-realistic; bialek-cyclite-2024] | Számszerű terv a logisztikához (szállás, bolt), folyamatcél a morálhoz; időlimit nélküli önellátón a rugalmas, RAAM/brevet szintidős formátumban a számszerű terv dominál |
| **Mozgáshányad-cél** | A különbséget a megállás, nem a sebesség adja: Ride Far ≥80% (1 óra állás / 4 óra mozgás); CTS-eset 94,4%; Hughes ≤5 perc/óra (~92%); Allegaert: „It's easier to keep going than it is to rest and then have to leave again"; Hager tudatosan csökkentette az álló időt; TCR-élboly: 5–31 perc/nap [ridefar-time-efficiency; rutberg-cts-2016; hughes-rbr-2015; allegaert-apidura-2016; hager-transiberica-2022; mckenzie-2026-tcr12-frozen] | Brevet: Storbeck PBP-n 57 h nyeregben / 30 h kívül (≈65%), ebből csak 10 h alvás – a kontrollok viszik az időt [storbeck-2019-pbp-lessons]; Muller a hőségben körönként megállt jégzokniért, „worth it" [muller-precisionhydration-2017] | Formátum (önellátó vs. kontroll-kötött), hőség (hűtés-megállás), esemény hossza (egynapos 90%+, többnapos 80–85%) |
| **Mikor állsz meg és mennyi időre** | Több okot gyűjts egy megállásra („not stop until you have multiple reasons"); kontrollon időzítő (30 perc + 10–15); a szunyókálás „trükk", amitől az agy azt hiszi, aludt [ridefar-time-efficiency; storbeck-2019-pbp-lessons; baloh-nduranz-2024] | Alvásadag: Gemperle 4 h/éj következetesen; Wilcox „about four hours a night" hetes versenyen, rekordkísérleten 6–7 h; Hayden 1,5 h (<4 nap) / ~3 h (>4 nap); Kolbinger ~4 h, de „I could have slept less"; Sehili nem áll meg, „if I stopped, the others would either catch me or get away"; RAAM: Strasser 1 h/éj, Baloh 1,5 h, Goldstein 3 h → 1,5 h a végére [gemperle-apidura-2026; wilcox-roadman-2026; wilcox-rouleur-2024; hayden-sleeping-guide; kolbinger-euronews-2019; sehili-breakaway; strasser-pez-2019; baloh-nduranz-2024; goldstein-cbc-2021] | Versenyhossz (rövid = kevesebb alvás), kísérős vs. önellátó (RAAM 1–1,5 h, TCR 3–4 h), ellenfél helyzete (Sehili), hőség (hűtés-megállás) |
| **Hegyi vs. sík tempó** | Emelkedőn magasabb, síkon alacsonyabb watt, de mindkettő „kontrollált": Broadwith 220 W sík / 280 W hegy (FTP 55% / 70%) az első 24 órában; Strasser könnyű Tarmac hegyre, Shiv síkra; 2–3 órás emelkedőn nem lehet enni (előre töltés) [broadwith-cyclingweekly-2018; strasser-pez-2019; baloh-nduranz-2024] | A CP feletti csúcsok drágábbak, mint a kJ mutatja – az élettani irodalom a hegyi „követem a többieket" ellen szól [sanchez-jimenez-2025-durability-sr; spragg-2024-intensity] | Terep-profil és a versenyző W/kg-ja; a +25–30% hegyi watt a kísérős, sík-domináns rekordokból jön, alpesi TCR-re számszerű forrás nincs |
| **Éjszakai tempó** | Éjjel a teljesítmény esik (RAAM-váltó: 212 → 189 W); a legnehezebb sáv „the darkest and coldest hours of the night (generally 2am to 4am)" és a napkelte utáni óra, a koffeint erre időzítik; éjjel inkább főútra váltanak [manunzio-2016-raam-team; muller-precisionhydration-2017; ridefar-route-planning] | Sehili és az első napi TCR-élboly átteker; Shaw inkább 22:00-kor fekszik és 02:00-kor indul; Baloh a cikk parafrázisa szerint élvezi az éjszaka nyugalmát [sehili-breakaway; dotwatcher-nightstarts-roundtable; baloh-nduranz-2024] | Kronotípus, hőség (éjszaka hűvösebb), forgalom, közvilágítás; kísérős versenyen a stáb figyelése teszi biztonságossá |
| **„Bad patch" kezelése** | Feldarabolás és nem-döntés: „Can you do it for 20 minutes?" (Broadwith); „Never scratch at night" (Ride Far); önbeszéd a negatív spirál ellen (Muller); a kilométereket rossz időben is sikerként keretezni (Hayden); a teljesítmény javulása az utolsó harmadban húzta ki Hagert; Wilcox: „the hard moments won't last forever" [broadwith-cyclingweekly-2018; ridefar-schedule; muller-precisionhydration-2017; hayden-confidence-realistic; hager-transiberica-2022] | Sehili nem nézi a trackert, mert rontja a hangulatát; Hall a saját korábbi splitjei ellen versenyez („racing against the splits"); Baloh görcsnél lassít és iszik, vár [sehili-breakaway; hall-bikepacking-2016; baloh-infinity-2020] | Ok szerint: élettani (hidratáció, energia) → lassíts és tölts; mentális → rövid egység, alvás; a tracker-nézés egyénileg motivál vagy demoralizál |
| **Terv rugalmassága / adat vs. érzés** | A terv viszonyítási alap, nem parancs: „having the plan allows me to track how I'm doing" (Ride Far); Bialek a testére hallgat; Hall: kísérlet bizonytalan kimenettel [ridefar-schedule; bialek-cyclite-2024; hall-bikepacking-2016] | CTS és Broadwith wattplafonnal versenyez (IF 0,60–0,65; 220/280 W); Strasser 160/170 W „recovery ride"-szintje mért; Muller a hőségedzésekből tudta, mit nem szabad túllépni [rutberg-cts-2016; broadwith-cyclingweekly-2018; strasser-pez-2019; muller-precisionhydration-2017] | Kísérős/egynapos formátumban a wattplafon működik; többnapos önellátón az RPE és az alvás-állapot felülírja (lásd 08-A Q7) |
| **Alvás mint sebesség** | „The more you sleep, the better you perform" (Wilcox); Hayden: bölcsebb túl sokat aludni és gyorsan tekerni; Gemperle 4 h/éj a tempó tartásáért; DotWatcher-elemzés: több alvás – jobb helyezés [wilcox-rouleur-2024; hayden-sleeping-guide; gemperle-apidura-2026; dotwatcher-moresleep-2026] | Sehili („the man who doesn't sleep"); Kolbinger „I could have slept less"; RAAM 1 h/éj (Strasser) [sehili-breakaway; kolbinger-euronews-2019; strasser-pez-2019] | Versenyhossz és formátum: 4 napnál hosszabb önellátón konvergál a 3–4 h; RAAM-on a stáb teszi lehetővé az 1–1,5 h-t; a „nem alvó" stílus 2020 óta a mezőnyben visszaszorul (08-B Q5) |

### Szakágankénti eltérések
- **Önellátó bikepacking (TCR, Transibérica, Tour Divide):** az első 24 óra alvás nélkül, 600+ km az élen, utána beálló 400–450 km/nap és 3–4 h/éj alvás; a mozgáshányad (80–85%, élen 95%+) a fő különbségtevő, a mozgósebesség a mezőnyben szűk sávban szór [ridefar-schedule; ridefar-time-efficiency; mckenzie-2026-tcr12-frozen; mckenzie-dotwatcher-tcr-2026; brayson-2019-tcr]. A hőséget a napi ritmus eltolásával kezelik, nem nappali alvással [dotwatcher-nightstarts-roundtable].
- **Kísérős RAAM:** alvás 1–1,5 h/24 h (Strasser, Baloh), a végén tovább csökkentve (Goldstein 3 → 1,5 h); intenzitás „recovery ride" szint (160/170 W); a sivatagot hűtéssel tekerik át; a stáb a biztonsági és döntési tartalék (hallucináció-figyelés, alvásprotokoll) [strasser-pez-2019; baloh-nduranz-2024; goldstein-cbc-2021; raam-sleepcom-2022]. A rajt itt is gyorsabb az élen [heidenfelder-2016-raam-pacing].
- **Brevet / PBP (időlimit):** a kontrollok viszik az időt (Storbeck: 30 h a 87-ből), az első éjszakai alvás a 90 órás csoportban a szintidőt veszélyezteti; edzői tanács negatív split és ≤5 perc/óra állás; a mezőny bruttó sebessége hét évtizede 15–16 km/h [storbeck-2019-pbp-lessons; hughes-rbr-2015; storbeck-2019-pbp-speeds; cyclecharts-pbp-2023].
- **24 órás pálya-/időfutam:** wattplafon (FTP 55–70%), hőségben tudatos lassítás és körönkénti hűtés-megállás, koffein 02–04 h-ra, az utolsó óra kontrollálva; a brit hagyomány a rekordkísérletekben 220/280 W-os sík/hegy plafonnal él [muller-precisionhydration-2017; broadwith-cyclingweekly-2018; strasser-inscyd-2022].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q10)
- Kristof Allegaert, Mike Hall, Fiona Kolbinger, Ulrich Bartholmoes és Christoph Fuhrbach esetében a nyitható interjúk **nem tartalmaznak számszerű pacing-adatot** (watt, km/nap, alvásóra) – csak elvi mondatokat; Fuhrbachtól egyetlen használható interjút sem találtam. Adam Bialek interjúja pacing-számot nem közöl.
- Edzői oldalon a **RAAM-specifikus CTS-cikk, Hunter Allen ultra-cikke és Dean Golich anyagai nem voltak elérhetők**; a CTS-elvek egy 200 mérföldes gravel-esetből származnak.
- **RAAM crew-guide** (stáb-protokoll: alvásablak, hűtés, tempóvisszajelzés) nyilvános, hivatkozható formában nem került elő.
- A brit 24 órás időfutam-hagyomány (Andy Wilkinson-vonal) pacing-tanácsa csak Broadwith rekordkísérletén és a 2013-as Cycling Weekly-cikken keresztül dokumentált; utóbbi táplálkozásról szól, tempóról nem.
- Több versenyzői „idézet" (Baloh nduranz, Goldstein CBC, Gemperle Apidura) szerkesztői parafrázis – a tankönyvben nem idézőjeles formában használandó.

### ELLENTMONDÁS (Q10)
- **Negatív split (Hughes, edző) vs. pozitív split mindenkinél (tracker):** Hughes rövidebb (100–200 mérföld) eseményre ad tanácsot; többnapos versenyen a 08-B csomag szerint mindenki pozitív pacinget mutat – a negatív split ultrán a „saját átlaghoz képest lassú első nap" értelmében marad érvényes.
- **Merev napi táv (Ride Far) vs. folyamatcél (Hayden):** a két győztes-szintű forrás ellentétes; a különbség inkább a cél funkciója (logisztika vs. morál), mint a gyakorlat.
- **Alvás ≈ sebesség (Wilcox, Hayden, Gemperle) vs. „aludhattam volna kevesebbet" (Kolbinger) és „nem állok meg" (Sehili):** a versenyhossz, a mezőny és a saját alvásigény dönt; a 2020 utáni győztesek (Gemperle, Bartholmoes) a 3–4 órás sávban konvergálnak.

---

## Q11 — Feltörekvő: durability a pacingben, gépi tanulásos idő-/tempóbecslés, valós idejű hőterhelés

1. **A durability-irodalom (2023–2025) pacing-üzenete: nem a kJ, hanem az intenzitás dönti el, mennyit veszítesz a későbbi teljesítményből – a kritikus teljesítmény feletti erőfeszítések kevesebb összmunkával is nagyobb esést okoznak.** 21 vizsgálat szisztematikus áttekintése; a szerzők explicit versenystratégiai következtetést vonnak le (intenzitás-specifikus terhelésszámítás). [sanchez-jimenez-2025-durability-sr A; spragg-2024-intensity A; spragg-2023-durability A]

2. **De a CP alatti tartományon belül (mérsékelt vs. nehéz) 60–90 perces, munkával kiegyenlített terhelés után a durability nem különbözött: a rámpa-csúcsteljesítmény 412,6 → 380,2 ill. 374,8 W, a W' esett, a VO2max/küszöbök/gazdaságosság nem.** Ultrára: a „hegyen egyenletes watt" szabály a CP feletti csúcsok ellen szól, a heavy-domain „kényelmesen erős" tekerés ára rövid távon nem mutatható ki – hosszabb terhelésre a szerzők is további kutatást kérnek. [evans-2025-durability-domain A; clark-2019-cp-dynamics A]

3. **A durability mérési módszertana még nem egységes (mit mérünk: CP, MMP, küszöb, RPE:pulzus; mennyi előmunka után), ezért a „fatigue resistance" mint pacing-bemenet ma még egyedi profilozást igényel, nem normát.** Amatőröknél 1000 kJ után a sikeresebbek 6,5%, a kevésbé sikeresek 12,5% 20 perces esést mutattak – az egyéni szórás az, amit egy tempóbecslőnek tudnia kellene. [hunter-2025-durability-methods C; jones-2024-resilience C; barsumyan-2025-durability-amateur A]

4. **A kereskedelmi tempó-/érkezésbecslők fizikai modellek fáradtság-tag nélkül: a Best Bike Split aerodinamika–gördülés–lejtés–szél–watt alapon mérföldenkénti wattcélt ad, a gyártó 2–3% időpontosságot állít helyes bemenetek mellett** – alvást, megállást, durability-t nem modellez, így többnapos ultrára csak szakaszszintű (egy etap, egy hegy) tervezésre alkalmas. [bestbikesplit-tt-plan D]

5. **A gépi tanulásos idő-előrejelzés első nyilvános kerékpáros munkái n=1 vagy konferencia-absztrakt szintűek: egy amatőr 96 menetéből Lasso-regresszió MAE 6,60 perc, R² 0,922; a fitnesz-mutatók 14%-kal javítják a topológia-alapú becslést; időjárás-bemenet még nincs.** A Ghent/Antwerp csoport egyénre szabott fitnesz–fáradtság és küszöbbecslést ígér, de a „fekete doboz" és a zajos adat korlátját maga nevezi meg. [aguilera-2025-race-time-ml D; boone-2023-jsc-ml D]

6. **Tracker-alapú versenyelemzés (DotWatcher) ma a legközelebb áll a „többnapos érkezésbecsléshez": mozgósebesség, álló idő és napi táv alapján a szerkesztők projekciót adnak, de a módszertan nem publikált és részben fizetőfal mögött van.** A 2026-os TCR-nyitónapon a kumulált top 10 álló ideje 5–31 perc, a legjobb mozgósebesség 28,75 km/h – ez a nyers bemenet, amelyből egy modell dolgozhatna. [mckenzie-2026-tcr12-frozen B; mckenzie-dotwatcher-tcr-2026 C; dotwatcher-moresleep-2026 C]

7. **Valós idejű hőterhelés-alapú pacing: a CORE-szenzort 2024-ben 10 WorldTour-csapat használja, a gyártó „5% teljesítményvesztés / 1 °C maghő" állítással; edzői esetleírásban a versenyző pulzus + maghő alapján vett vissza a wattból és folyamatos hűtéssel tartotta stabilan a maghőt.** A független validálás azonban gyenge: rektális referenciához képest az adatpontok csak 45–51%-a volt 0,3 °C-on belül, szisztematikus +0,23 ± 0,35 °C eltéréssel – a szenzor trendjelzőnek használható, abszolút „lassíts 39 °C-nál" küszöbre nem. [cyclingnews-core-2024 D; martinez-freespeed-core-2023 D; verdel-2021-core-validity A]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q11)
- Egyetlen durability-vizsgálat sem 4 óránál hosszabb vagy többnapos; az ultra-durability (napról napra átvitt CP-esés) mérése nem létezik.
- Nincs publikált, validált többnapos érkezési-idő modell (alvás + megállás + durability + időjárás); a Strava/Komoot idő-becslők belső módszertanáról ellenőrizhető forrás nem került elő.
- A CORE gyártói „5%/°C" állítás hivatkozás nélküli; ultratávon (alacsony intenzitás, hosszú expozíció) a hőterhelés–teljesítmény görbe nem ismert.
- A DotWatcher-projekciók módszertana nem nyilvános.

### ELLENTMONDÁS (Q11)
- **Intenzitás számít (Sánchez-Jiménez, Spragg 2024) vs. „a tartomány nem számít" (Evans 2025):** Evans a CP alatti két tartományt hasonlította rövid terhelésen, a másik kettő a CP feletti munkát – a határ a CP-nél húzódik, nem a mérsékelt/nehéz között.
- **CORE mint pacing-eszköz (gyártó, edzők) vs. validálási hiány (Verdel):** a gyakorlat megelőzte a bizonyítékot; újabb firmware-re a 2021-es validálás nem vonatkozik, de újabb független validálás sem került elő.

---

## Feltörekvő irányok (D-szintű, figyelni érdemes)
- **Intenzitás-súlyozott terhelésszámítás versenyen belül** („CP feletti percek" mint a durability fő prediktora) – a következő lépés a több napra átvitt hatás mérése [sanchez-jimenez-2025-durability-sr; evans-2025-durability-domain].
- **Egyénre szabott ML-fáradtságbecslés viselhető szenzorokból** (HR, HRV, watt, magasság) – jelenleg absztrakt/n=1 szint; időjárás-API és több sportoló a bejelentett következő lépés [boone-2023-jsc-ml; aguilera-2025-race-time-ml].
- **Fizikai + fáradtsági hibrid tempóbecslő** – a Best Bike Split-típusú modellek durability-taggal és alvás/megállás-blokkokkal; ilyen termék vagy közlemény nem került elő [bestbikesplit-tt-plan].
- **Valós idejű hőterhelés-index a pacingben** – gyakorlat (WorldTour, triatlon-edzők) megelőzi a validálást; ultrán az alacsony intenzitású, hosszú expozíció külön validálást igényel [cyclingnews-core-2024; martinez-freespeed-core-2023; verdel-2021-core-validity].
- **Tracker-adattudomány** – a DotWatcher mozgásidő/álló idő/alvás–helyezés elemzései a legjobb nyilvános ultra-adatforrás; nyílt, tisztított adatsor és lektorált elemzés hiányzik [mckenzie-2026-tcr12-frozen; dotwatcher-moresleep-2026].

## Nem sikerült megnyitni (ezért nem szerepel a forrástárban, vagy csak másodkézből)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4602249 (Racinais 2015, PMC-tükör) – reCAPTCHA; a Citadel-tükör PDF-ből dolgoztam.
- https://pubmed.ncbi.nlm.nih.gov/23371827/ (Ito 2013) – reCAPTCHA; az Europe PMC REST-válaszból dolgoztam.
- https://onlinelibrary.wiley.com/doi/10.1002/ejsc.70039 (Evans 2025) – 403; Crossref API adta a metaadatot és absztraktot.
- https://www.ebi.ac.uk/europepmc/... (Evans 2025 keresés) – 429 (rate limit) többszöri próbálkozásra.
- https://www.cyclist.co.uk/in-depth/fiona-kolbinger-cyclist – 403.
- https://www.rouleur.cc/performance/beating-the-heat-tour-de-france-core – 403.
- https://coachpav.com/cycling-technique-tactics/mastering-the-art-of-pacing-in-ultra-cycling-races/ – 401.
- https://dotwatcher.substack.com/p/tour-divide-2026-3500km-in-and-the – megnyílt, de a projekció módszertana fizetőfal mögött.
- https://www.apidura.com/journal/on-winning-robin-gemperles-preparation-for-tcrno10/ – megnyílt, de a cikk törzse nem töltődött be (csak bevezető).
- https://dotwatcher.substack.com/ (kezdőlap) – nem adott cikklistát; az /archive oldal igen.
- Megnyílt, de pacing-tartalom nélkül, ezért nem vettem fel: welovecycling.com Strasser-interjú (2017), stories.strava.com Bartholmoes Tour Divide (2023), supernova-lights.com Bartholmoes és Kolbinger cikkek, en.brujulabike.com Gemperle-bringa, apidura.com „Rediscovering racing spirit" (Carlsson), progravelmagazine „Just a little bit further", cyclingweekly.com 24 h TT „How to get through" (2013 – táplálkozás), roadbikerider.com „Good pacing starts with holding back" (Ric Stern, rövid távra).
- Nem található nyitható formában: CTS RAAM-specifikus pacing-cikk; Hunter Allen ultra-cikk; Dean Golich RAAM-anyag; RAAM crew guide; Christoph Fuhrbach interjú; Andy Wilkinson pacing-tanács; Strava/Komoot idő-becslő módszertan.
