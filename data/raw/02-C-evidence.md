# 02. modul – Edzéselmélet ultrára – C csomag bizonyíték-térkép
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
