# 03 · Táplálkozás és hidratálás — kutatási összefoglaló (v0.1, 2026-09-23)

## Hogyan készült

Négy párhuzamos kutatóügynök, tizenegy kérdés (Q1–Q11), 134 új forrás (A: 31, B: 32, C: 32, D: 40; egy átfedő kulcs, `baker-2016-sweat-normative`, a B és D csomagban egyszerre) a `data/sources.yaml`-ban `03:` előtagú kérdéskulccsal; a forrástár így 336 tételes. Minden kulcsszámhoz a forrás eredeti mondata (`quote` mező); DOI csak ott, ahol kiadói/Crossref/OpenAlex oldalon látható volt (113 tétel), a többinél `doi: null` és megjegyzés. A fokozatok: A 53, B 46, C 33, D 2. A meglévő 04-es és 08-as forrásokra (Thurber, Hulton, Geesmann, Black, Purcell, Hyldahl, Fesseler, Strasser, Hayden, Wilcox, Sehili, Ridefar, DotWatcher) az ügynökök csak hivatkoztak. A nyers kimenetek: `data/raw/03-A…D-sources.yaml` és `-evidence.md`; a bizonyíték-térképek teljes szövege e dokumentum második felében. Kérdésfelosztás: A = Q1 szénhidrát-bevitel és felszívódási plafon, Q2 energiamérleg többnapos versenyen, Q3 zsíradaptáció-vita; B = Q4 a bél edzése és GI-panaszok, Q5 hidratálás és nátrium; C = Q6 koffein, egyéb szerek, NSAID, Q8 hőség/hideg/magasság, Q9 verseny előtti és utáni táplálkozás, RED-S; D = Q7 boltból táplálkozás, Q10 versenyzői konvergencia, Q11 feltörekvő irányok.

Két figyelmeztetés a 08-as tényellenőrzés tanulságából: a kalóriasűrűség-lista (chips ~5,3 kcal/g stb.) a D csomagban **nem ellenőrzött címkeadat** (USDA/Open Food Facts a proxy miatt nem nyílt meg) — a végleges szövegbe csak ellenőrzés után; és több kulcsszám csak absztraktból származik (jelölve: *absztraktból*), például Del Coso 2016 hatásmérete (perc) hiányzik.

## A modul tíz kulcsállítása (a bizonyíték-térkép sűrítménye)

1. **Az óránként hasznosítható szénhidrátnak plafonja van, és a plafon a keveréktől függ:** egyféle cukorból (glükóz/maltodextrin) ~60–75 g/h ég el, akármennyit viszünk be; glükóz+fruktóz keverékkel (2:1 – 1:0,8) 84–100 g/h. 120 g/h bevitelnél a hasznosulás 72–75 %, és a forma (ital, gél, rágó) nem számít. A 120 g/h nem kíméli a glikogént a 90-hez képest — a többlet haszna (kisebb izomkárosodás, jobb ökonómia) más úton jön, mechanizmusa nyitott. [jeukendrup-2006-ultra-exo A; podlogar-2022-120vs90 A; hearris-2022-120-formats A; ravikanti-2025-marathoners-120 A; morton-2026-metabolism-medals A]
2. **A terepen mért bevitel ultrakerékpáron 52–59 g/h, óriási egyéni szórással (13–126 g/h), és a verseny második felében csökken** (1230 km-en 618 km után szignifikánsan). Az elit 24 órás rekordon 105–116 g/h is megy — de ez folyékony, stábbal adagolt, edzett bél. A magasabb energiabevitel rövidebb versenyidővel járt (r² = 0,28, 384 km) — megfigyelés, nem ok-okozat. [geesmann-2014-1230km B; black-2012-384km B; martinez-2025-mallorca312 B; strasser-inscyd-2022 B]
3. **A deficit a norma, nem a hiba:** a forgalom 24 órán ~750 kcal/h, 2 napos nonstopon ~590, 6+ naposon ~500 kcal/h (PAL 4–7); a bevitel ennek 36–78 %-a; a tartósan felszívható bevitel populációs plafonja ~2,4× alapanyagcsere (egyéni kerékpáros esetekben 4×-ig). Egy 43 órás verseny után a tesztoszteron −67 %, IGF-1 −45 %, leptin −79 % — 12 óra pihenés után is. A tolerálható deficit küszöbe nem ismert; a két végpont: energiaegyensúly-közeli Tour Divide (VO2max változatlan) és −25 % testtömeg (VO2max −20 %). [enqvist-2010-adventure-racing B; thurber-2019-alimentary B; hyldahl-2024-tourdivide B; geesmann-2017-hormone-suppression B; stroud-1997-antarctic B; best-2023-cocodona-dlw B]
4. **A zsíradaptáció megemeli a zsírégetést (0,5–0,7 → 1,2–1,5 g/perc), de nem javítja a teljesítményt:** a meta-analízisek semlegesek, magas intenzitáson elit szinten reprodukálhatóan ront (ökonómia), ultrás 50–65 %-os intenzitáson kontrollált adat nincs. A zsíradaptált sportoló is profitál a szénhidrátból. Vegyes étrenden a zsír ~290 kcal/h-t fedez, a többit (600 kcal/h forgalomnál ~78 g/h) szénhidrátból kell hozni. [volek-2016-faster B; burke-2017-supernova A; burke-2020-supernova2 A; cao-2021-keto-meta A; gawelczyk-2026-lchf-aerobic-sr A; carpenter-2025-keto-cho-feeding A; maunder-2018-mfo B]
5. **A gyomor-bél panasz ultrán a szabály: futóknál 65–96 %, kerékpárosoknál ~38 % (312 km), profi kerékpárosoknál 7 %.** A hő önmagában 12-szeresére emeli a tünetek súlyosságát, az ibuprofen megduplázza a bélsérülést; a hányinger a feladás vezető oka; ultrán a **kevés** folyadék előzi meg a hányingert (5,9 vs. 10,9 ml/kg/h). Gyógyszer (ondanszetron) nem segít. [stuempfle-2015-wser-gi B; martinez-2025-mallorca312 B; pfeiffer-2012-gi-endurance-events B; snipe-2018-heat-gi A; vanwijck-2012-ibuprofen A; stuempfle-2013-racediet-gi B; pasternak-2021-ondansetron A]
6. **A bél edzhető, és ez az egyik legjobban bizonyított beavatkozás a modulban:** két hét napi 90 g/h-s „bélkihívás” a tüneteket 60–63 %-kal csökkenti, a felszívódási zavart felére, a teljesítményt 4–5 %-kal javítja (két RCT + szisztematikus áttekintés). Verseny előtt 1–3 nap rost/FODMAP-szegény menü a nyugalmi tüneteket csökkenti. [costa-2017-guttraining A; miall-2018-gutchallenge A; martinez-2023-guttraining-sr A; lis-2018-lowfodmap A]
7. **Hidratálás: a túlivás ultrán gyakoribb baj, mint a kiszáradás.** Mért bevitel 0,39–0,58 l/h; 387 km-en a célba érők 39 %-a ≤135 mmol/l vér-nátriummal, csak 11 % dehidrált; a hyponatraemia küszöbe ~168 ml/kg/nap összbevitel; a testtömeg-gyarapodás OR 4,2. Önszabályozott kültéri terhelésen 2–4 % tömegvesztés nem ront, a szomjúság szerinti ivás jobb, mint az alatta maradó. Többnapos ultrán a mérleg félrevezet: stabil tömeg mellett +2 l visszatartott víz, ödéma az 5. napon. [black-2014-387km-fluid B; armstrong-2017-eh-cycling B; almond-2005-boston-eah B; goulet-2011-dehydration-meta A; gauckler-2024-ultracycling-fluid B; geesmann-2014-1230km B]
8. **Nátrium: az egyéni izzadás-nátrium 410–1630 mg/l (átlag ~830), az óránkénti veszteség ~1,2 g; a pótlásra egyetlen terep-RCT mutat teljesítményelőnyt (félironman, ~460 mg/h), görcs ellen és hyponatraemia ellen nem véd** (a nátriumbevitel nem különbözött a hyponatraemiások és a többiek között; a görcsölők sóbevitele azonos). Az izzadásteszt-alapú 100 %-os pótlás 5 órás hőségfutáson sem változtatta a folyadékegyensúlyt. Ajánlott alap 300–600 mg/h, ital 230–690 mg/l. [baker-2016-sweat-normative B; barnes-2019-sweat-by-sport B; delcoso-2016-salt-halfironman A; hoffman-2015-sodium-eah-wser B; hoffman-2015-cramping-wser B; mccubbin-2024-sodium-personalized A; veniamakis-2022-sodium-review C]
9. **Koffein: 1–3 mg/kg elég, az ismételt kis adag ugyanannyit ér, mint az egy nagy (+3 %), a terepi bevitel 24 órán ~2 mg/kg; az ára az alvás:** −45 perc alvásidő, 107 mg-ot ≥8,8 órával, 217 mg-ot ≥13 órával a tervezett alvás előtt kell bevenni; 200 mg közvetlenül egy 15–30 perces alvás előtt („koffein-alvás”) javítja az éberséget. Genotípus-teszt nem indokolt. **NSAID verseny alatt: ne** — ibuprofen 400 mg/4 h esetén akut vesekárosodás 52 % vs. 34 % (NNH 5,5), hyponatraemia-kapcsolat, maratonon 5× több nemkívánatos esemény; az ártalom feltételes (dehidráció + hőség + hosszú terhelés + ismételt adag). Nitrát, bikarbonát, kreatin, ketonészter ultrán nem hasznos. [guest-2021-issn-caffeine A; cox-2002-caffeine-protocols A; bescos-2012-24h-relay B; gardiner-2023-caffeine A; centofanti-2020-caffeinenap A; filtness-2026-caffeinenap A; grgic-2021-cyp1a2-sr A; lipman-2017-ibuprofen-aki A; kuster-2013-analgesics-marathon B; wharam-2006-nsaid-eah-ironman B; senefeld-2020-nitrate-meta A; brooks-2022-ketone-meta A]
10. **Hőségben és hidegben a rendszer más:** hőségben a gyomorürülést a maghő + kiszáradás lassítja (r = −0,76), az étvágy csökken, a jégkása (7,5 g/kg) −0,66 °C maghőt és +19 % kimerülési időt ad, a hűtés összesen +6,7 % (meta); hidegben az étvágy elvileg nő, terepen mégis „nincs éhség, nincs idő enni” (+200 kcal/h versenyzői becslés, 5000–7000 kcal/nap), a 2026-os TCR nyitónapján −1…−3 °C-ban az élboly 5–31 perc álló időt engedett meg. Magasságban a bevitel mérsékelten csökken (SMD −0,50), európai hágókon ritkán tényező. [neufer-1989-gastric-heat A; shorten-2009-heat-appetite A; siegel-2010-ice-slurry A; bongers-2015-cooling-meta A; charlot-2017-hot-cold-review C; smid-2025-cold-nutrition C; tuft-7mesh-winter-tips C; mckenzie-2026-tcr12-frozen B; matu-2018-hypoxia-appetite-meta A]

**Verseny előtt és után (Q9):** feltöltéshez egy pihenőnap 10 g/kg szénhidráttal elég (95 → 180 mmol/kg izomglikogén 24 h alatt; a 2–3. nap nem ad többet); rajt előtt 1–4 g/kg 1–4 órával; a teljes raktár 6–10 óra tekerést fedez, többnapos versenyen a feltöltés a deficit *kezdetét* tolja ki. Regeneráció: fehérje 1,8–2,2 g/kg/nap 4–5 adagban + 30–40 g kazein este, az első 48 óra fehérje + szénhidrát + alvás; teljes helyreállás ~6 nap (UTMB-adat, futó). RED-S: férfi országúti kerékpárosok 44 %-ánál alacsony csontsűrűség, krónikus alacsony energia-elérhetőség → alacsonyabb tesztoszteron; a felkészülési LEA-t ki kell zárni (verseny alatti akut deficit ≠ RED-S). Labor a felkészülés elején: ferritin, D-vitamin. [bussau-2002-1day-loading A; thomas-2016-joint-position A; jager-2017-issn-protein A; baron-2022-utmb-recovery B; mountjoy-2023-ioc-reds A; keay-2018-male-cyclists-lea B]

**Versenyzői konvergencia (Q7 + Q10, 11 témasor):** önellátón, brevet-en és 24 órán az ökölszabály 200–300 kcal/h szilárd, boltos étel „minden órában, éhség előtt, időzítővel”; kísérős RAAM-on a stáb 500–550 kcal/h-t etet folyékonyan, és a 3–4. naptól a stáb dönt; brevet-kontrollon meleg étel <10 perc alatt, a kalória 1/3–1/2-e italból; 24 órás box: banán 86,5 %, energiaszelet 50 %, sajt 43 %, kóla 54 %, 1,3 étkezés/óra, két leülős étkezés. Konvergens: az édes korán elfárad, „sós fordulat” (chips, sajt, kenyér, dió); semmi romlandó, semmi új; hányingerre lassíts + kortyolj + kóla + folyékonyra váltás; POI-terv (benzinkút a leghatékonyabb, nyitvatartás, tartalék étel). Eltérés: leülős étkezés (Mäkipää/Dickson) vs. „a biciklin eszem” (Sehili, Allegaert 9 h 38 perc összes megállás 8 nap alatt); csak szomj szerint (Hughes) vs. tervezett folyadék + nátrium (PH/CTS). [white-ridefar-food C; rutberg-pulford-cts-ultra-2025 C; hughes-rbr-showstoppers-2019 C; barnett-2017-raam-toone B; strasser-datasport-2019 C; dickson-rusa-pbp C; chlibkova-2014-24h-mtb B; lwcoaching-2008-24h-solo C; hayden-tcr6-story B; wilcox-adventurecycling-2022 C; sehili-rawcycling-atlas C; blow-ph-ultra-2021 C]

## Ellentmondások, amiket a modulnak explicit módon kezelnie kell

- **E1 — Izotópos plafon vs. „két óra alatt csak a fele hasznosul”.** A 13C-mérések 1,5–1,7 g/perc csúcsot mutatnak 120 g/h-nál; Noakes és Prins szerint 2 óra alatt a bevitt szénhidrát ≤50 %-a ég el. Feloldás: a hasznosulás a 2–3. órától éri el a platót — ultrán éppen ez a tartomány számít, az első két óra alacsony hatásfoka a raktárból megy.
- **E2 — ISSN 30–50 g/h vs. ACSM 90 g/h vs. 120 g/h iskola.** Három nagyságrend ugyanarra a kérdésre. Az ISSN futásra szól (GI-korlát), a 120 a 2–3 órás laborból és rövid terepből jön, a 90 az általános ajánlás. A modul sávot tanít: 60–90 g/h alap, a mért ultra-terep 52–59; >90 csak edzett béllel és stáb/folyékony formátumban; a 120 g/h többnapos hatékonysága **nem bizonyított** (a 2026-os irányelv-revízió is kimondja).
- **E3 — Alimentáris plafon 2,4× BMR vs. Tour Divide ~4× BMR energiaegyensúlyban.** A plafon populációs átlag, nem egyéni korlát; a kerékpár (ülő helyzet, nincs rázkódás) többet enged, mint a futás; alvással tagolt tempón fedezhető, nonstop versenytempón nem.
- **E4 — Tervezett ivás (≥2 % ront) vs. szomjúság (2–4 % nem ront; hyponatraemia-megelőzés).** Feloldás: rövid/meleg/intenzív = tervezett, felső határral; ultra = szomjúság + „ne hízz” + padló 6–8 ml/kg/h (a kevés folyadék hányingert hoz). „A többet ivók gyorsabbak” (24 h MTB) és „a több folyadék hyponatraemiát okoz” nem ellentmondás: a kockázat a bevitel/izzadás arány, nem az abszolút bevitel.
- **E5 — Só gyorsít (Del Coso) vs. só nem véd, nem görcsöl (Hoffman).** Különböző kérdések: 5–6 órás meleg verseny teljesítménye vs. 30 órás hyponatraemia/görcs. Ultrán a sóbevitel értelme a nátriumesés mérséklése és az étvágy, nem a görcs-prevenció.
- **E6 — Koffein ergogén vs. alvásromboló, és CYP1A2 (CC genotípusnál 4 mg/kg +13,7 % rontás egy vizsgálatban) vs. 17 tanulmány áttekintése (kicsi, inkonzisztens).** Ultrán az alvásminőség a nagyobb tét → időzítés, nem adag; a genotípus nem döntő, az egyéni teszt edzésen az.
- **E7 — NSAID-ártalom (AKI, GI, hyponatraemia) vs. euhidrált 24 órás naproxen ártalmatlan.** Az ártalom feltételes: dehidráció + hőség + hosszú terhelés + ismételt adag — a modul ezért nem tiltással, hanem a feltételekkel tanítja.
- **E8 — Keto „egy hét után helyreáll” (SR) vs. Burke 3–3,5 hét után elit szinten reprodukálhatóan rosszabb.** Intenzitásfüggő; a FASTER 20 hónapos adaptáltjai csak zsíroxidációban különböztek, teljesítményt nem mértek. A könyv nem választ tábort: ultrás intenzitáson nincs kontrollált adat, a meta semleges.
- **E9 — Ízfáradás: versenyzői konszenzus (édes → sós) vs. labor (4 óra alatt az édes ital preferenciája nőtt).** A labor 4 óra, nem edzett nők, egyetlen ital; a versenyzői beszámolók 20–200 órás monotóniáról szólnak — nem ugyanazt mérik.
- **E10 — CGM: „glükóz ↔ sebesség” (Ishihara) vs. „nincs élettani indok” (Helleputte, Riddell).** Korreláció ≠ vezérlőjel; a késői stressz-hiperglikémia (a glükóz a célig *nő* futóultrán) félrevezethet. A modul a CGM-et trend- és hipoglikémia-jelzőként, nem üzemanyagszint-mérőként mutatja.
- **E11 — Hidrogél: Rowe (+2,1 %, futás) vs. két SR (nincs előny, kerékpáros vizsgálatok negatívak).** Ultrára nem bizonyított; feltörekvő jel.

## Bizonyítékhiányok (ahol a modul csak „legjobb becslést” adhat)

- Nincs izotópos vagy teljesítmény-vizsgálat 120 g/h-ról 6 óránál hosszabb vagy többnapos terhelésen; a leghosszabb kontrollált mérés 5 óra (90 g/h). Bevitel–teljesítmény kapcsolat ultrakerékpáron csak megfigyeléses (r² = 0,28).
- Szóló RAAM/TCR kettős jelölt vizes forgalom-mérés nincs; a tolerálható deficit küszöbére nincs dózis–válasz vizsgálat; izomvesztés kerékpáros ultrán (DXA) n = 1–2; immun- és döntéshozatali adat sportolónál nincs (csak katonai modell).
- Ultrakerékpáros (>12 h, RAAM, TCR, 24 h) GI-tünet-prevalencia lektorált felmérésben nincs; kerékpáros gut-training RCT nincs (mindkét RCT futó); többnapos „bél-fáradás” csak futásból ismert.
- Kerékpáros ultrán (>12 h) mért izzadásráta nincs — csak bevitel és testtömeg; hőmérséklet-függő izzadásráta-tábla kerékpárosoknak csak modell vagy szerkesztői összeállítás; a szomjúság megbízhatósága alváshiányban nem vizsgált; női ultrakerékpáros hidratálási adat n = 5.
- Nátriumpótlás teljesítményhatása: egy 5–6 órás triatlon-RCT (hatásméret az absztraktban nincs); ultrán RCT nincs.
- Koffein: nincs RCT >6 órás vagy többnapos kerékpáros eseményen, csak egy 24 órás megfigyelés (n = 8); koffein-megvonás hatása ultrán nincs. NSAID-használati arány ultrakerékpáron ismeretlen (minden vese/GI/EAH-adat futó, triatlon, kalandverseny).
- Zsíradaptált ultrakerékpáros esettanulmány lektorált folyóiratban nincs; >4 órás keto-teljesítményteszt nincs (leghosszabb 100 km).
- Jégkása/belső hűtés >3 órán nincs vizsgálva; hideg étvágy-adat hidegvíz-immerzióból; hideg kalóriaszorzó kerékpáros ultrán n = 1.
- Feltöltés többnapos ultrán: nincs RCT; CK-lefutás kerékpáron nem dokumentált; regeneráció többnapos *kerékpáros* ultra után egyetlen követéses vizsgálat sincs; RED-S ultrakerékpárosoknál nincs adat.
- Nincs mért (napló + DLW) adat arról, hogy önellátó versenyen mit és mennyit esznek boltból — a lista interjúkból áll (C); ízfáradás lektorált vizsgálata ultrán nincs; meleg étel–morál sportolói adat nincs (csak katonai); kalóriasűrűség-adatok nem ellenőrzöttek.
- Nem sikerült megnyitni: Rüst/Knechtle 2012 (Swiss Cycling Marathon, 720 km, nulla hyponatraemia — csak a C csomag OpenAlex-absztraktja), Talanian & Spriet 2016, Sawka 2007 ACSM, Costill 1971, Kolbinger/Bartholmoes/Gemperle/Allegaert étkezési interjúk (Casquette/Cyclist 403), „Septuagenarians approach 4× BMR during RAAM” (IJSPP 2022).

## Feltörekvő irányok (a modul „feltörekvő” jelével)

CGM mint napi trend- és éjszakai hipoglikémia-jelző (RAW-váltó 91 vs. 115 mg/dl, TBR 9,15 %; RAAM −0,92 mg/dl/nap), nem etetés-vezérlő; ketonészter (akut g = 0,136, GI-panasz gyakoribb, a „regenerációs” EPO-hatás nyitott); ≥100 g/h + hidrogél többnapos glikogén-visszatöltésre (hipotézis); egyéni exogén-oxidációs mérés (13C) a szénhidrát-cél személyre szabására; kültéri izzadásráta-modell (sweatratecalculator.com, egyenlet nem publikált) és hordozható izzadás-szenzorok; copeptin/NT-proBNP mint többnapos „túltöltöttség” marker (n = 13); cisztatin C mint terepi vesemarker; koffein-alvás mikrociklus (15 perces alvás + 200 mg) terepi validálás nélkül; probiotikum legfeljebb GI-tünet-mérséklő (g = −0,62, p = 0,05); AI-etetéstervezők validálatlanok (R² ~0,5). [skroce-2026-cgm-records B; fesseler-2026-raam58 B; helleputte-2025-cgm-review C; brooks-2022-ketone-meta A; li-2026-hydrogel-review A; wilson-2025-highcarb-review C; jay-2024-sweat-prediction-outdoor B; gauckler-2024-ultracycling-fluid B; colombini-2012-giro-ck B; aitkenhead-2025-supplements-gut A; wang-2025-ml-supplement D]

## Döntést igénylő pontok (Attila)

- [ ] **Web-eszköz köre.** Javaslat: egy „Etetési és hidratálási terv” kalkulátor három réteggel — (1) energia: BMR × PAL (formátum-preset: 24 h / 2 napos nonstop / többnapos önellátó / kísérős), bevitel-cél kcal/h és g CH/h (60–90 sáv, formátum-plafon), napi deficit és „hány nap tartható”; (2) folyadék + nátrium: izzadásráta-sáv hőmérséklet szerint (szerkesztői tábla, C-jelöléssel) vagy saját mérés, óránkénti minimum (6–8 ml/kg) és maximum (≤ izzadásráta, ≤168 ml/kg/nap), nátrium 300–600 mg/h alap ± egyéni izzadás-Na; (3) koffein-adagoló: mg/kg, ismételt adag, utolsó adag időpontja a tervezett alvás előtt (8,8 h / 13 h szabály), „koffein-alvás” opció. Alternatíva: csak (1)+(2), a koffein a 04 alváseszközbe kerül.
- [ ] **120 g/h álláspont.** Javaslat: a könyv 60–90 g/h-t tanít alapnak, a 90 fölötti sávot „edzett bél + folyékony/stáb formátum + saját teszt” feltételekkel, a 120-at „nem bizonyított többnapos versenyen” jellel. Alternatíva: a 120-at csak a feltörekvő oldalon említeni.
- [ ] **Keto/zsíradaptáció: külön „vita” oldal** (mint a 08-ban a pulzus-drift), vagy egy bekezdés a „miből megy az ultra” oldalon? Javaslat: egy vita-oldal, mert a téma a versenyzői közbeszédben súlyos, a bizonyíték pedig világos (semleges).
- [ ] **NSAID-figyelmeztetés erőssége.** Javaslat: piros keretes „verseny alatt ne” protokoll-blokk a feltételekkel (kiszáradás + hőség + ismételt adag) és a paracetamol-alternatíva „forrás nélkül, kérdezd meg az orvosod” jelöléssel. Alternatíva: enyhébb, csak a feltételeket tanító megfogalmazás.
- [ ] **Bél-edzés protokoll mint a modul „Mérd be magad” feladata** (2 hét napi 90 g/h edzésen, tünetnapló) — a 08-as durability-teszt párja. Elfogadod? Nándival később.
- [ ] **Izzadásteszt: otthoni mérleg-módszer leírása** (előtte/utána tömeg + bevitel − vizelet) belekerüljön feladatként, vagy csak hivatkozás a modellre? Javaslat: belekerül, mert az egyéni izzadásráta a kalkulátor bemenete.
- [ ] **Boltos kalóriasűrűség-táblázat:** ellenőrzöm címkeadatból (magyar bolti termékek, saját ellenőrzés) és belekerül „példa” jelöléssel, vagy kimarad? Javaslat: 10–12 tétel, ellenőrzés után, `{példa}` jellel.
- [ ] **Női adat:** a modulban külön jelezzük, ahol az adat csak férfi (hormonok, RED-S férfi-hiány, hidratálás n = 5 nő)? Javaslat: igen, egységes „férfi adat” jellel — ez a többi modulra is szabály lenne.
- [ ] **Szakági bontás:** a versenyzői konvergencia-táblát (önellátó / kísérős / brevet / 24 h) a modul saját oldalaként (mint a 08-ban), vagy a mezőben `disc=` szűrővel? Javaslat: saját oldal + a protokollok disc-jelölve.
- [ ] A tíz kulcsállítást elfogadod a modul gerincének?


---

# Bizonyíték-térképek kérdésenként (a négy ügynök nyers kimenete, változatlanul)


## Csomag A

Q1 szénhidrát-bevitel ultrán · Q2 energiamérleg többnapos versenyen · Q3 zsíradaptáció / metabolikus rugalmasság
Készült: 2026-09-23. Forrásfájl: `data/raw/03-A-sources.yaml` (31 új tétel) + hivatkozott meglévő kulcsok (`data/sources.yaml`, 03-B/C/D).
Fokozat: A meta/SR/RCT/kontrollált labor/konszenzus · B terep/megfigyelés/esettanulmány mért adattal · C narratív/edzői/gyártói · D feltörekvő.
Jelölés: „absztraktból” = a szám csak absztraktból; „másodlagos” = áttekintés idézi.

---

## Q1 — Szénhidrát-bevitel ultrán: exogén oxidáció, felszívódási plafon, 120 g/h, terepi bevitel, GI

1. **Egyetlen transzporterű (glükóz/maltodextrin) forrásból az exogén oxidáció ~1,0–1,25 g/perc-en (60–75 g/h) tetőzik, akárhány grammot viszünk be.** 8 edzett kerékpáros, 5 h, 58% VO2max, 90 g/h csak-glükóz: plató 120 perc után, csúcs 1,24 ± 0,04 g/perc [jeukendrup-2006-ultra-exo A]; áttekintés: 1–1,1 g/perc [podlogar-2022-newhorizons C; jeukendrup-2014-personalized C].
2. **Glükóz+fruktóz (2:1 – 1:0,8) keverékkel a plafon 1,4–1,7 g/perc-re (84–100 g/h) emelkedik.** 5 h kerékpár, 2:1, 90 g/h: 1,40 ± 0,08 g/perc [jeukendrup-2006-ultra-exo A]; 3 h kerékpár, 120 g/h, 0,8:1: 1,51 ± 0,22 g/perc a 120–180. percben [podlogar-2022-120vs90 A]; 3 h kerékpár, 120 g/h 1:0,8, ital/gél/rágó: csúcs 1,56–1,66 g/perc, hatásfok 72–75% [hearris-2022-120-formats A]; 2 h futás elit maratonisták, 120 g/h 1:1: 1,68 ± 0,16 g/perc [ravikanti-2025-marathoners-120 A]. A 2026-os irányelv-revízió szerint a publikált csúcs 1,60–1,75 g/perc (96–105 g/h), 2,0–2,4 g/perc bevitelnél [morton-2026-metabolism-medals A].
3. **A 120 g/h nem „kíméli” az endogén glikogént a 90 g/h-hoz képest – csak a teljes CHO-oxidációt emeli.** Endogén CHO-oxidáció 2,15 vs 2,20 g/perc (p=0,786) 120 vs 90 g/h mellett [podlogar-2022-120vs90 A]; a profi mezőny áttekintésében egy vizsgálatban a 112,5 g/h inkább NÖVELTE a máj- és izomglikogén-felhasználást a 90 g/h-hoz képest (másodlagos) [wilson-2025-highcarb-review C]. Ellenben elit futóknál a 120 g/h 8,1 ml O2/kg/km-rel javította a futóökonómiát [ravikanti-2025-marathoners-120 A].
4. **A forma (folyadék / gél / zselés rágó / vegyes) nem befolyásolja az exogén oxidációt 120 g/h-nál – a mennyiség és az arány számít.** 9 edzett férfi, mind a négy formában 1,56–1,66 g/perc, GI-panasz minimális, kapacitásteszt azonos [hearris-2022-120-formats A].
5. **A többszörös transzportálható CHO teljesítményelőnye 2,5–3 órás terhelésen 1–9%, és a bevitel mértékével nő.** 14 vizsgálat: fruktóz:glükóz 0,5–1:1, 1,3–2,4 g/perc → átlagteljesítmény +1–9% (95% CI 0–19); ≥1,7 g/perc-nél 4–9%, alacsonyabbnál 1–3%; optimum 0,8:1 arány 1,5–1,8 g/perc [rowlands-2015-fructose-glucose A]. 61 vizsgálat (679 alany) 82%-a mutatott szignifikáns CHO-előnyt; >2 h-nál a mechanizmus a >90 g/h szállítás [stellingwerff-2014-cho-sr A].
6. **Hivatalos ajánlás: >2,5–3 h terhelésre 90 g/h-ig többszörös transzportálható CHO; a 2026-os revízió edzett sportolóknál 120 g/h-ra emelné a felső határt, de a terepen látott 120–200 g/h hatékonyságát „a jelenlegi tudomány nem támasztja alá”.** [thomas-2016-joint-position A; morton-2026-metabolism-medals A]. ISSN egynapos ultrára: 150–400 kcal/h, CHO 30–50 g/h [tiller-2019-issn-ultra C].
7. **Terepen a 120 g/h elviselhető ÉS csökkenti a másnapi izomkárosodást – edzett bélnél, futóknál.** Hegyi maraton (42 km, 4000 m), 60/90/120 g/h (n=6/7/7): belső terhelés 3805 vs 4688/4692 AU (p=0,019); 24 h-s CK-emelkedés 156% vs 976% (60 g/h), LDH 8,5 vs 46,7%, GOT 27 vs 162%; versenyidő nem különbözött (p=0,871) [viribay-2020-120-mountain A]. Az egynapos ultratrail-SR (8 vizsgálat): két vizsgálat a 120 g/h-t kisebb belső terheléssel és EIMD-vel kötötte össze [arribalzaga-2021-ultratrail-sr A].
8. **A ténylegesen mért terepi bevitel ultrán jellemzően 50–65 g/h, hatalmas egyéni szórással (13–126 g/h), és a verseny második felében csökken.** Kerékpár: 1230 km nonstop, n=14: 57,1 ± 17,7 g/h, 618 km után szignifikáns csökkenés [geesmann-2014-1230km B]; 384 km, n=18: 52 g/h, a magasabb energiabevitel rövidebb versenyidővel járt (p=0,023, r²=0,28) [black-2012-384km B]; 24 h váltó, n=8: 943 g CHO/24 h (~39 g/h a váltó-időre vetítve) [bescos-2012-24h-relay B]; Mallorca 312, n=138: 59,2 g/h [martinez-2025-mallorca312 B]. Futás: ultratrail 22–126 g/h, a többség nem éri el a 90 g/h-t [arribalzaga-2021-ultratrail-sr A]; 12–24 h-s versenyeken 30–66 g/h (másodlagos) [morton-2026-metabolism-medals A]; 63 g/h átlag, 13–105 g/h egyéni tartomány, >50% nem visz be 30 g/h-nál többet (másodlagos) [ishihara-2026-glucose-phases C]. Rekord-szintű kivétel: Strasser 24 h-s rekordján 116 g/h az első 12 h-ban, ~105 g/h a 24 h-ra [strasser-inscyd-2022 C].
9. **GI-tünet ultrán a szabály, nem a kivétel: futóknál 65–85%, kerékpárosoknál ~40%; és a többnapos versenyen a GI-tünet mérhetően csökkenti a bevitelt.** MSUM 85%, 24 h 73%; többnaposon a tünetesek futás közbeni CHO-bevitele −8 g/h (p<0,01), 24 h-n a tünet nem változtatta a bevitelt [costa-2016-ultra-gis-intake B]; ultratrail 65–82% [arribalzaga-2021-ultratrail-sr A]; Mallorca 312: 38,4% a versenyen, a bevitel és a tünet között NINCS összefüggés – a nyugalmi GI-tünet és a rajt előtti idegesség jósol [martinez-2025-mallorca312 B]. Elit futóknál a hányinger/teltség/görcs csúcsa a 120 g/h-nál a legnagyobb [ravikanti-2025-marathoners-120 A].
10. **A bél edzhető: ismételt CHO-etetés a bélpanaszt 26–47%-kal, a CHO-malabszorpciót 45–54%-kal csökkenti (8 vizsgálat).** [martinez-2023-guttraining-sr A]. A 120 g/h-s terepvizsgálatok résztvevői mind előzetes bél-edzésen estek át [viribay-2020-120-mountain A].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q1)
- **120 g/h 6+ órán át vagy több napon:** nincs lektorált izotópos vagy teljesítmény-vizsgálat. A leghosszabb kontrollált exogén-oxidációs mérés 5 h (90 g/h) [jeukendrup-2006-ultra-exo A]; a 120 g/h-s labor-vizsgálatok 2–3 órásak [podlogar-2022-120vs90; hearris-2022-120-formats; ravikanti-2025-marathoners-120]; a terepi 120 g/h ~4–5 órás hegyi maraton [viribay-2020-120-mountain]. A 2026-os revízió maga is kimondja, hogy a >90 g/h hatékonysága nem bizonyított [morton-2026-metabolism-medals A]. Keresés: „120 g/h carbohydrate ultra-endurance 24-hour multi-day tolerance” (WebSearch, 2026-09-23) – csak áttekintéseket és blogokat adott. Egyetlen több napos, ~105 g/h-s adat versenyzői közlés (n=1, 24 h) [strasser-inscyd-2022 C].
- **Bevitel–teljesítmény kapcsolat ultrakerékpáron:** csak megfigyeléses korreláció (r²=0,28, 384 km) [black-2012-384km B]; RCT nincs.
- **Kerékpáros GI-adatok ultrán:** egyetlen kérdőíves vizsgálat (312 km) [martinez-2025-mallorca312 B]; a többnapos kerékpáros GI-„fáradás” (bevitel napról napra csökken) csak futásból ismert [costa-2016-ultra-gis-intake B].
- **Ajánlások:** ACSM/ISSN egyike sem ad külön dózist >6 órás vagy többnapos kerékpáros eseményre; az ISSN-ultra állásfoglalás futásra szól és 30–50 g/h-t mond [tiller-2019-issn-ultra C] – ez ellentmond a 90 g/h-s általános ajánlásnak.

### ELLENTMONDÁS (Q1)
- **Izotópos plafon vs. „2 órás hasznosulás” érv:** a 13C-vizsgálatok 1,5–1,7 g/perc csúcsot mérnek 120 g/h-nál [podlogar-2022-120vs90 A; hearris-2022-120-formats A; ravikanti-2025-marathoners-120 A], Noakes & Prins szerint viszont 2 óra alatt a bevitt CHO legfeljebb ~50%-a oxidálódik (144 g/h-nál is csak ~68,5 g/h) és 53–70% a bélben marad [noakes-2025-sub2h-critique C]. Feloldás ultrára: az exogén oxidáció 2–3 óra után éri el a platót, a 2 órás átlag alábecsül; a hatásfok (72–75%) a 3. órától érvényes.
- **Glikogén-kímélés:** a 120 g/h nem csökkenti az endogén oxidációt [podlogar-2022-120vs90 A], a magasabb dózis akár növelheti a glikogén-felhasználást (másodlagos) [wilson-2025-highcarb-review C] – mégis kisebb izomkárosodást és jobb ökonómiát mérnek [viribay-2020-120-mountain A; ravikanti-2025-marathoners-120 A]. A mechanizmus nyitott.
- **GI-tünet és bevitel:** futóknál a magasabb dózis több tünettel jár [ravikanti-2025-marathoners-120 A], kerékpárosoknál nincs kapcsolat [martinez-2025-mallorca312 B]; ultratrailen a tünet inkább magasság/környezet/sebesség függvénye [arribalzaga-2021-ultratrail-sr A].
- **ISSN 30–50 g/h vs. ACSM 90 g/h vs. 120 g/h iskola** – három nagyságrend ugyanarra a kérdésre; az ISSN futás-specifikus (GI-korlát), a 120 g/h labor- és rövid-terep alapú.

### KALKULÁTOR-PARAMÉTEREK (Q1 – óránkénti CHO-cél)
- Időtartam-alapú alaptartomány (ACSM/Jeukendrup): 1–2,5 h: 30–60 g/h; >2,5–3 h: 60–90 g/h többszörös transzportálható CHO [thomas-2016-joint-position A; jeukendrup-2014-personalized C]. Edzett, bél-edzett sportoló felső határa: 120 g/h [morton-2026-metabolism-medals A].
- Egy-transzporteres plafon: ~60–75 g/h oxidáció (1,0–1,25 g/perc) [jeukendrup-2006-ultra-exo A]; glükóz:fruktóz 2:1 → ~84 g/h (1,4 g/perc) 90 g/h bevitelnél [jeukendrup-2006-ultra-exo A]; 1:0,8 → ~90–100 g/h oxidáció 120 g/h bevitelnél, hatásfok 0,72–0,75 [hearris-2022-120-formats A; podlogar-2022-120vs90 A].
- Képlet: oxidált exogén CHO (g/h) ≈ bevitel × hatásfok, ahol hatásfok ≈ 0,80 (≤90 g/h, 2:1) ill. 0,72–0,75 (120 g/h, 1:0,8) – csak a 3. órától; az első 2 órában ~0,5 [noakes-2025-sub2h-critique C].
- Ultra-terepi „reális” tartomány kerékpáron: 50–65 g/h (mért átlagok) [geesmann-2014-1230km B; black-2012-384km B; martinez-2025-mallorca312 B]; cél többnapos versenyen: 60–90 g/h fenntartva, a verseny második felében várható 20–30%-os csökkenéssel [geesmann-2014-1230km B].
- Energiában: 60 g/h ≈ 240 kcal/h; 90 g/h ≈ 360 kcal/h; 120 g/h ≈ 480 kcal/h (4 kcal/g). Ez a 24 h-s forgalom (~500–750 kcal/h) 30–65%-a [enqvist-2010-adventure-racing B].

---

## Q2 — Energiamérleg többnapos versenyen: forgalom, deficit, alimentáris plafon, testösszetétel, hormonok, döntéshozatal

1. **A fenntartható energiaBEVITEL plafonja ~2,5×BMR (2,36 ± 0,59×BMR), az esemény hosszától függetlenül; ami efölött van, testraktárból jön.** RAUSA (140 nap): 1. hét 3,76×BMR, utolsó hét 2,81×, átlag 3,11×; a Tour de France 4–5×BMR-je legfeljebb ~23 napig tartható [thurber-2019-alimentary B].
2. **Napokig tartó eseményeken a mért forgalom 4–7×BMR; minél hosszabb az esemény, annál alacsonyabb a PAL.** DLW: Cocodona 250 (402 km futás, n=5) PAL 4,34–6,94; Arizona Trail FKT (1315 km) 5,63; DLW-ultrák között az esemény hossza és a PAL inverz kapcsolata r²=0,68 [best-2023-cocodona-dlw B]. Tour de France (n=4, DLW): 4,3–5,3×BMR [westerterp-1986-tdf-dlw B]; 30 napos, 4300 km-es kanadai átkelés (n=2, DLW): PAL 3,7–4,1 [purcell-2025-canada B].
3. **Kerékpáros ultrák mért/becsült forgalma: 24 h ~750 kcal/h; 2 napos nonstop ~600 kcal/h; 6+ napos ~500 kcal/h; RAAM-váltó ~6400 kcal/nap DLW-vel.** 24 h vegyes ultra (n=9): 18 050 ± 2390 kcal (750 ± 100 kcal/h); 6 napos kalandverseny (n=6): 80 000 ± 18 000 kcal (500 ± 100 kcal/h) [enqvist-2010-adventure-racing B]; 1230 km / ~43 h (n=14): 25 303 ± 2436 kcal (~590 kcal/h) [geesmann-2014-1230km B]; RAAM 4 fős váltó (DLW): 43 401 kcal/6,5 nap [hulton-2010-raam-energy B]; szóló RAAM esettanulmány becslése 17 965 kcal/nap (valószínű túlbecslés) [knechtle-2005-raam-case B].
4. **A verseny alatti bevitel a forgalom 36–55%-a; a deficit a norma.** Cocodona-győztes: igény 53%-a bevitelből (ennek 85,6%-a CHO), 47% testtömeg-katabolizmus [best-2023-cocodona-dlw B]; 24 h: bevitel 8450 ± 1160 kcal (47%), deficit 9590 ± 770 kcal [enqvist-2010-adventure-racing B]; 1230 km: bevitel 19 749 vs forgalom 25 303 kcal (78%) [geesmann-2014-1230km B]; 384 km: 4470 vs 6100 kcal (73%) [black-2012-384km B]; szóló RAAM: 9612 kcal/nap bevitel (a legmagasabb publikált) [knechtle-2005-raam-case B]; ISSN: ultrázók a forgalom 36–53%-át viszik be [tiller-2019-issn-ultra C]. Egyéni tartomány egy 43 órás versenyen: −11 859 kcal deficittől +3593 kcal többletig [geesmann-2017-hormone-suppression B].
5. **Az önbevallott bevitel a verseny előrehaladtával egyre jobban alábecsül a DLW-hez képest (+13%, +21%, +35% az egymást követő heteken).** [westerterp-1986-tdf-dlw B]. A pulzusalapú forgalombecslés az oxigénpulzus-drift miatt korrekció nélkül 5–10%-kal alábecsül 12 h után [enqvist-2010-adventure-racing B].
6. **Többnapos kerékpáros ultrán a testtömeg-vesztés 2–5 kg; a zsírvesztés 24–48 h alatt ~1–1,5 kg; a bőrredő/BIA a láb-ödéma miatt megbízhatatlan.** Szóló RAAM (9,7 nap): −5 kg [knechtle-2005-raam-case B]; RAAM 58 éves (11 nap): −2,3 kg, becsült deficit 21 169 kcal [fesseler-2026-raam58 B]; 1000 km/48 h: zsír −1 kg, a legnagyobb ütem a 12–24. órában, BIA/bőrredő a folyadék-felhalmozódást tömegként méri [knechtle-2011-1000km-bodycomp B]; 24 h: −2,3 kg testtömeg, −1,5 kg zsír, izomglikogén −60% [enqvist-2010-adventure-racing B]; Tour Divide 16 nap: testtömeg stabil, zsír csökkent, láb-izomtömeg nőtt [hyldahl-2024-tourdivide B]; 30 nap Kanada: −2,3 kg zsír, +1,4 kg zsírmentes tömeg [purcell-2025-canada B].
7. **Mennyi deficit tolerálható? Mérhető adat: energiaegyensúly-közeli többnapos teljesítés mellett a VO2max és a max. teljesítmény nem változik; 25%-os tömegvesztés mellett a VO2max −20%, az izomerő −56%.** Tour Divide: VO2max és Wmax változatlan, DLW szerint az első 9 napban energiaegyensúly [hyldahl-2024-tourdivide B]; Antarktisz 95 nap, bevitel 21,3 MJ/nap vs forgalom 29–38 MJ/nap (csúcs 44,6–48,7 MJ/nap), >25% tömegvesztés → VO2max 53,6→41,2 és 58,1→46,0 ml/kg/perc, izomerő −55,8%-ig, izomenzimek −63%-ig, hipoglikémia [stroud-1997-antarctic B]. Köztes tartományra (5–15% tömegvesztés) nincs kontrollált adat.
8. **Egyetlen ~43 órás kerékpáros ultra után a tesztoszteron −67%, IGF-1 −45%, leptin −79%, és 12 h pihenés után is elnyomott; a deficit mértéke arányos az IGF-1-eséssel (r=0,65).** [geesmann-2017-hormone-suppression B]. 161 km futás után tesztoszteron, LH, SHBG csökken, kortizol emelkedik, a T:C arány és a CK a 2. napon is kóros [kupchak-2014-wser-hormones B].
9. **RED-S keret: egészségi EA-küszöb ≤30 kcal/kg FFM/nap (férfiaknál ~9–25); a napok–hetek hosszú „adaptálható LEA” megkülönböztetendő a „problémás LEA”-tól.** [mountjoy-2023-ioc-reds A]. Kerékpárosoknál (n=50, országúti): alacsony ágyéki csontsűrűség 44%-nál, krónikus LEA → alacsonyabb tesztoszteron [keay-2018-male-cyclists-lea B].
10. **Energiadeficit + alváshiány mellett a kockázatvállalás nő és az önkontroll csökken; a vigilancia és hangulat romlása viszont az energiaegyensúlytól független.** 72 h szimulált művelet, n=10, 43% deficit: kockázatvállalás ↑ (p=0,047), önkontroll ↓ (p=0,021); vigilancia-lapszusok és munkamemória mindkét karon romlott [beckner-2023-susops-deficit A].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q2)
- **Szóló RAAM / TCR DLW-mérés:** nincs. A RAAM DLW-adat 4 fős váltóé [hulton-2010-raam-energy B]; a Tour Divide (n=1) [hyldahl-2024-tourdivide B] és a kanadai átkelés (n=2) [purcell-2025-canada B] az egyetlen szóló kerékpáros DLW; a TCR-ről csak pulzus/teljesítmény-adat van [brayson-2019-tcr B]. A „Septuagenarians approach 4× BMR during RAAM” (IJSPP 2022, DLW, idős RAAM-csapat) cikket nem sikerült megnyitni (403/429) – lásd „Nem sikerült megnyitni”.
- **Tolerálható deficit küszöbe:** nincs dózis–válasz vizsgálat; a két végpont (egyensúly → változatlan VO2max; −25% tömeg → −20% VO2max) között csak esetleírás.
- **Izomvesztés kerékpáros ultrán:** a mérési módszerek (BIA, bőrredő) a folyadékretenció miatt hibásak [knechtle-2011-1000km-bodycomp B]; DXA/NMR-alapú többnapos kerékpáros adat csak n=1–2 [hyldahl-2024-tourdivide; purcell-2025-canada].
- **Immunrendszer többnapos kerékpáros deficitben:** nem találtunk ultrakerékpáros immun-vizsgálatot energiamérleg-méréssel (keresés: „ultra-endurance race energy deficit immune testosterone cortisol cycling”); a hormonadatok egyeseménysek (≤43 h) [geesmann-2017-hormone-suppression B].
- **Döntéshozatal:** csak katonai modell (72 h, 4500 kcal/nap) [beckner-2023-susops-deficit A]; sportolói adat nincs.

### ELLENTMONDÁS (Q2)
- **Becsült vs mért deficit:** a szóló RAAM esettanulmány 83 526 kcal-os becsült deficitje ~11 kg zsírnak felelne meg, a mért tömegvesztés 5 kg [knechtle-2005-raam-case B]; a DLW-mérések (Tour Divide, Kanada) energiaegyensúly-közeli állapotot mutatnak [hyldahl-2024-tourdivide B; purcell-2025-canada B]. A pulzus/teljesítmény-alapú becslések ultrán szisztematikusan túlbecsülik a deficitet, a naplózott bevitel pedig alábecsül [westerterp-1986-tdf-dlw B].
- **Alimentáris plafon 2,5×BMR vs. 4×BMR-es bevitel Tour Divide-on:** a Tour Divide-versenyző az első 9 napon energiaegyensúlyban volt ~4×BMR mellett [hyldahl-2024-tourdivide B], ami meghaladja a Thurber-féle 2,36×BMR bevitel-plafont [thurber-2019-alimentary B]; a kanadai átkelők PAL 3,7–4,1 mellett 30 napig tartották a tömegüket [purcell-2025-canada B]. A plafon tehát populációs átlag, nem egyéni korlát; a kerékpár (ülő pozíció, rázkódás nélkül) magasabb bevitelt enged, mint a futás.
- **Hormonelnyomás = deficit vagy = terhelés?** Geesmann szerint a tesztoszteron/leptin-esés az éhezéséhez hasonló, de csak az IGF-1 korrelált a deficittel [geesmann-2017-hormone-suppression B]; a válasz nem választható szét.

### KALKULÁTOR-PARAMÉTEREK (Q2 – napi energiamérleg többnapos versenyen)
- BMR: Mifflin-St Jeor vagy mért; férfi 70–80 kg-nál ~1700–1900 kcal/nap (általános egyenlet, nem forrásadat).
- Forgalom (TEE) = BMR × PAL. PAL-tartományok mért adatokból: 24 h nonstop: ~750 kcal/h → ~9–10×BMR aznap [enqvist-2010-adventure-racing B]; 2 napos nonstop kerékpár: ~590 kcal/h [geesmann-2014-1230km B]; 6–16 napos: PAL 3,7–5,6 [best-2023-cocodona-dlw B; hyldahl-2024-tourdivide B; westerterp-1986-tdf-dlw B]; 30 napos: PAL 3,7–4,1 [purcell-2025-canada B]; >30 nap: konvergál 2,5–3×BMR-re [thurber-2019-alimentary B].
- Bevitel-plafon: 2,4 ± 0,6×BMR populációs átlag [thurber-2019-alimentary B]; egyéni felső értékek kerékpáron 4×BMR-ig (n=1–2) [hyldahl-2024-tourdivide B; purcell-2025-canada B]; legmagasabb publikált szóló RAAM-bevitel 9612 kcal/nap ≈ 400 kcal/h [knechtle-2005-raam-case B].
- Deficit → tömeg: 1 kg zsír ≈ 7000–7700 kcal (általános); a mért 1 kg zsírvesztés 48 h alatt ≈ 150 kcal/h nettó zsírmobilizáció [knechtle-2011-1000km-bodycomp B]. Első 24–48 h tömegvesztésének nagy része víz/glikogén (izomglikogén −60%) [enqvist-2010-adventure-racing B].
- Figyelmeztető küszöb: EA <30 kcal/kg FFM/nap (nő) / ~9–25 (férfi) napok–hetek távon „adaptálható”, hónapok távon „problémás” [mountjoy-2023-ioc-reds A]; verseny alatti akut deficit ≠ RED-S, de a felkészülési LEA-t ki kell zárni [keay-2018-male-cyclists-lea B].

---

## Q3 — Zsíradaptáció és a „metabolikus rugalmasság” vita

1. **Hosszú távú ketogén adaptáció a zsíroxidáció csúcsát ~1,5 g/perc-re emeli (vegyes étrenden 0,5–0,7 g/perc), és a csúcs magasabb intenzitásra tolódik.** FASTER: LC 1,54 ± 0,18 vs HC 0,67 ± 0,14 g/perc, csúcs 70,3 vs 54,9% VO2max; 3 h futás alatt 1,21 vs 0,76 g/perc [volek-2016-faster B]; elit gyaloglók 3 hét LCHF: csúcs 1,57 ± 0,32 g/perc [burke-2017-supernova A]; 0,6→1,3 g/perc [burke-2020-supernova2 A]; 30/30 vizsgálat +28% – +200% [gawelczyk-2026-lchf-aerobic-sr A].
2. **Vegyes étrenden az MFO normatív értéke 0,5–0,6 g/perc, de az egyéni tartomány 0,17–1,27 g/perc; a Fatmax ~50–56% VO2max.** 1121 sportoló: MFO 0,59 ± 0,18 g/perc (0,17–1,27), Fatmax 49,3 ± 14,8% VO2max, férfi 0,61 vs nő 0,50 [randell-2017-mfo-athletes B]; edzett állóképességi: 0,53 ± 0,16 g/perc, Fatmax 56 ± 8%; edzéssel az MFO nő, a Fatmax nem; Ironman-idő és MFO r=0,35 [maunder-2018-mfo B].
3. **Magas intenzitáson (≥80–90% VO2max) a LCHF rontja az ökonómiát és a teljesítményt – két független elit kohorszban reprodukálva.** 10 km gyaloglás: HCHO +6,6%, PCHO +5,3%, LCHF −1,6% [burke-2017-supernova A]; 10 000 m: HCHO −4,8% (134 s), LCHF +2,3% (86 s lassabb, p<0,001), nincs „rebound” 2,5 hét CHO-visszatöltés után sem [burke-2020-supernova2 A]. SR: a szubmaximális ökonómia a legérzékenyebb, a vizsgálatok 50%-ában romlott [gawelczyk-2026-lchf-aerobic-sr A].
4. **Meta-analízisek: a keto nem javítja és összességében nem is rontja a VO2max-ot és a kimerülésig tartó időt – az RER csökken, a teljesítmény nem változik.** VO2max SMD −0,06 (CI −0,36–0,25), TTE SMD −0,13 (CI −0,66–0,40), RER SMD −1,81 [cao-2021-keto-meta A]; 33 vizsgálat/409 fő: VO2max megmaradt 50%, javult 11%; TTE megmaradt 69%; ≤7 napon belül romlás, >1 hét után fenntartott/javult [gawelczyk-2026-lchf-aerobic-sr A].
5. **A leghosszabb kerékpáros keto-teszt (100 km TT, 12 hét): nem szignifikáns különbség, a W/kg-javulás nagyrészt a −5,9 kg tömegvesztésből.** 100 km: LCKD −4,07 vs HC −1,13 perc (p=0,057); testtömeg −5,9 vs −0,8 kg; kritikus teljesítmény +1,4 vs −0,7 W/kg (p=0,047) [mcswiney-2018-keto-cyclists B].
6. **Krónikusan (8+ hónap) LCHF-adaptált kerékpárosok nem kompenzálnak több glükoneogenezissel: az endogén glükóztermelés alacsonyabb (6,0 vs 7,8 mg/kg/perc), a glükoneogenezis azonos (2,8 vs 2,5).** [webster-2016-lchf-gluconeogenesis B]. A FASTER-ben az izomglikogén-felhasználás (~64%) és -visszatöltés a két csoportban azonos volt – a keto nem „kímél” glikogént 3 h-s futáson [volek-2016-faster B].
7. **„Train low” periodizáció: mitokondriális jelátvitel igen, teljesítmény nem – 9 vizsgálat meta-analízise semleges (SMD 0,17; CI −0,15–0,49; p=0,29).** [gejl-2021-trainlow-meta A]. A periodizált CHO-kar a Burke-vizsgálatokban a HCHO-hoz hasonlóan javult (+5,3%; +2,2% trend) – nem rosszabb, de nem is jobb [burke-2017-supernova A; burke-2020-supernova2 A].
8. **A zsíradaptált sportoló is profitál a CHO-ból: 25 hónapos keto után egy 60 g-os edzés előtti CHO-bolusz javította a 16,1 km-es időfutamot; a 2 napos töltés önmagában nem.** n=13, zsíroxidáció placebónál 0,60–0,74 g/perc [carpenter-2025-keto-cho-feeding A]. Ez a „metabolikus rugalmasság” gyakorlati tartalma: a két üzemanyag nem kizáró.
9. **Esetsorozat: 10 hét keto → −4 kg, zsíroxidáció +41% (0,6→0,8 g/perc), de TTE −2 perc, csúcsteljesítmény −18 W; minden résztvevő jobb közérzetet jelentett.** [zinn-2017-nz-keto-pilot B] – a szubjektív és az objektív hatás elválik.
10. **Ultrás relevancia számokban:** 1,2–1,5 g/perc zsíroxidáció ≈ 650–810 kcal/h – ez fedezné a többnapos ultra ~500–600 kcal/h forgalmát [enqvist-2010-adventure-racing B; geesmann-2014-1230km B]; vegyes étrenden 0,5–0,6 g/perc ≈ 270–320 kcal/h [maunder-2018-mfo B; randell-2017-mfo-athletes B], a különbözetet CHO-ból kell fedezni. Az ökonómia-romlás (több O2 ugyanahhoz a sebességhez) ultrán is költség, de a hegyi szakaszokon a tömegvesztés (−5,9 kg) [mcswiney-2018-keto-cyclists B] valós előny lehet.

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q3)
- **Ultrakerékpáros zsíradaptált esettanulmány lektorált folyóiratban:** nem találtunk. Keresések (WebSearch, 2026-09-23): „ketogenic OR low-carbohydrate ultra-endurance cyclist case study race”, „low-carbohydrate ultra-cyclist Race Across America OR Transcontinental case study metabolic” – csak FASTER (futók, labor), Zinn 2017 (vegyes), McSwiney 2018 (100 km) és blogok. Az ultrás terepadatok (Q3) tehát futó-laborra és rövid kerékpáros tesztekre korlátozódnak.
- **>4 órás keto-teljesítményteszt:** nincs; a leghosszabb 100 km (~3 h) [mcswiney-2018-keto-cyclists B] és a 3 h-s laborfutás teljesítménymérés nélkül [volek-2016-faster B].
- **Adaptáció hossza:** a Burke-vizsgálatok 3–3,5 hetesek [burke-2017-supernova; burke-2020-supernova2]; a hosszú távú (8+ hónap) adatok keresztmetszetiek, önszelektáltak [volek-2016-faster B; webster-2016-lchf-gluconeogenesis B].
- **Zsíroxidáció edzhetősége mint önálló kimenet:** az MFO edzéssel nő [maunder-2018-mfo B], de a variancia >50%-a megmagyarázatlan [randell-2017-mfo-athletes B]; dózis–válasz edzésprotokoll nincs.
- **GI-hatás keto-n ultrán:** nincs adat.

### ELLENTMONDÁS (Q3)
- **„Rövid adaptáció” érv:** Gawelczyk 2026 szerint >1 hét után a teljesítmény helyreáll [gawelczyk-2026-lchf-aerobic-sr A], Burke 3–3,5 hét után reprodukálhatóan rosszabb teljesítményt mér elit szinten [burke-2017-supernova A; burke-2020-supernova2 A]; a FASTER 20 hónapos adaptáltjai viszont csak zsíroxidációban különböztek, teljesítményt nem mértek [volek-2016-faster B]. Feloldás: intenzitás-függő – ≥80% VO2max-on a LCHF ökonómia-vesztése mérhető, ultrás 50–65%-on nincs kontrollált adat.
- **Zsíroxidáció mértéke hosszú távú keto-n:** FASTER 1,54 g/perc (elit ultrafutók) [volek-2016-faster B] vs 0,60–0,74 g/perc rekreációs, 25 hónapos keto-sportolóknál időfutam alatt [carpenter-2025-keto-cho-feeding A] – az edzettség és az intenzitás (TT vs. 64% VO2max) magyarázza; a „1,5 g/perc” nem általánosítható.
- **Keto → W/kg:** McSwiney javulása [mcswiney-2018-keto-cyclists B] vs Zinn romlása [zinn-2017-nz-keto-pilot B] vs meta semleges [cao-2021-keto-meta A] – a tömegvesztés és a tesztintenzitás a moderátor.
- **Noakes-iskola:** a fat-max 0,7–0,9 g/perc mellett „nem kell exogén CHO” a sub-2h maratonhoz [noakes-2025-sub2h-critique C] vs. a 120 g/h-nál mért ökonómia-javulás [ravikanti-2025-marathoners-120 A].

### KALKULÁTOR-PARAMÉTEREK (Q3 – zsír/CHO részarány ultrás intenzitáson)
- Zsíroxidáció energia-egyenértéke: 1 g zsír ≈ 9 kcal → MFO (g/perc) × 540 = kcal/h zsírból. Vegyes étrend, edzett: 0,53 g/perc ≈ 290 kcal/h [maunder-2018-mfo B]; sportolói átlag 0,59 (0,17–1,27) [randell-2017-mfo-athletes B]; keto-adaptált elit: 1,2–1,5 g/perc ≈ 650–810 kcal/h [volek-2016-faster B].
- Fatmax-intenzitás: 49–56% VO2max (edzett 56 ± 8%) [randell-2017-mfo-athletes B; maunder-2018-mfo B]; keto-adaptáltnál 70% VO2max [volek-2016-faster B].
- Ultrás forgalom fedezete: 500–750 kcal/h [enqvist-2010-adventure-racing B] − zsírból (fent) = CHO-igény; pl. 600 − 290 = ~310 kcal/h ≈ 78 g CHO/h endogén+exogén; exogénből max ~90–100 g/h [hearris-2022-120-formats A].
- Ökonómia-büntetés LCHF-en magas intenzitáson: O2-költség nem javult az edzés ellenére (HCHO/PCHO: −2,5– −7%) [burke-2017-supernova A]; ultrás intenzitásra nincs szám – ne extrapoláljuk.

---

## Feltörekvő irányok (D / korai C)
- **Egyénre szabott CHO-adagolás exogén oxidáció mérésével** (13C-lehelet-teszt alapján „személyes plafon”) – a 2026-os revízió és a peloton-áttekintés is javasolja, validált protokoll még nincs [morton-2026-metabolism-medals A; wilson-2025-highcarb-review C].
- **CGM-vezérelt üzemanyagozás ultrán:** háromfázisú glükóz-dinamika, késői emelkedések, amit a bevitel nem magyaráz; kerékpáros ultrán nem validált [ishihara-2026-glucose-phases C].
- **≥100–120 g/h többnapos versenyen mint napi energiamérleg-eszköz** (nem aznapi teljesítmény-előny): a verseny alatti CHO erősen korrelál a napi összbevitellel a profi mezőnyben – ultrára hipotézis [wilson-2025-highcarb-review C].
- **Bél-edzés többnapos „bél-fáradás” ellen:** a gut training 1–4 hetes protokollokon igazolt [martinez-2023-guttraining-sr A], a napról napra romló GI-tünet/bevitel (MSUM) [costa-2016-ultra-gis-intake B] ellen nem vizsgált.
- **Stratégiai CHO-visszavezetés zsíradaptáltaknál** (60 g bolusz) mint „hibrid” stratégia [carpenter-2025-keto-cho-feeding A] – ultrán teszteletlen.
- **Deficit és döntéshozatal:** a katonai SUSOPS-modell (kockázatvállalás ↑ deficitben) [beckner-2023-susops-deficit A] ultrás átvitele (self-supported versenyek, forgalomban való döntések) nyitott kutatási kérdés.

## Nem sikerült megnyitni (2026-09-23)
- journals.physiology.org (J Appl Physiol) teljes szöveg: 403 – Ravikanti 2025, Hearris 2022, Jeukendrup 2006, Westerterp 1986 → Crossref / Europe PMC / OpenAlex / repozitórium absztraktból.
- jandonline.org és ScienceDirect (ACSM 2016 J Acad Nutr Diet): 403/404 → 03-C `thomas-2016-joint-position` kulcsra hivatkozunk.
- journals.humankinetics.com: 403; pubmed.ncbi.nlm.nih.gov: 429 – „Septuagenarians Approach 4 Times the Basal Metabolic Rate During Race Across America” (IJSPP 2022; DLW, idős RAAM-csapat) – NEM került be, pedig kerékpáros DLW-adat.
- tandfonline.com (Knechtle 2011 Res Sports Med; Enqvist 2010 J Sports Sci; Zinn 2017): 403 → OpenAlex DOI-rekord / Springer-tükör.
- physoc.onlinelibrary.wiley.com (Burke 2017; Webster 2016; Burke 2021 „future of elite endurance sport?”): 403 → OpenAlex; Burke 2021 áttekintés kimaradt.
- api.crossref.org: 429 több lekérés után (Stellingwerff 2014 és Jeukendrup 2006 még sikerült); Europe PMC REST: 429 az első lekérés után (Ravikanti-absztrakt sikerült); api.openalex.org keresés (search/filter): 429, a DOI-végpont működött; link.springer.com: időszakos 429 (Zinn 2017 másodszorra sikerült).
- Stroud 1993 (Arktisz DLW) és Westerterp/Saris 1989 abszolút MJ/nap-értékei: nem keresve tovább; a Tour de France-adat csak BMR-többszörösként szerepel.
- Nem talált (keresés után): ultrakerékpáros keto/LCHF esettanulmány; szóló RAAM/TCR DLW; 120 g/h >6 h vagy többnapos kontrollált vizsgálat.

## Csomag B

**Q4: a bél edzése és a gyomor-bél panaszok · Q5: hidratálás és nátrium (kalkulátor-paraméterekkel)**
Készült: 2026-09-23. Forrásfájl: `data/raw/03-B-sources.yaml` (32 új tétel). Meglévő kulcsok (`data/sources.yaml`) csak hivatkozva.
Jelölés: [kulcs FOKOZAT]. A = meta/SR/RCT/kontrollált labor/konszenzus; B = terep/megfigyelés mért adattal; C = narratív review, edzői/versenyzői tapasztalat; D = feltörekvő.
Megjegyzés: a legtöbb absztrakt az OpenAlex rekonstrukciójából származik (kiadói oldalak 403/429); a számok absztrakt-szintűek, a végleges szövegbe teljes szöveg ellenőrzése után.

---

## Q4 — A bél edzése és a gyomor-bél panaszok

### Gyakoriság ultra-eseményeken

1. **Egy 161 km-es ultrafutáson gyakorlatilag mindenki (96%) tapasztal GI-tünetet, és a hányinger a feladás vezető oka.** Western States, n=272: bármely GI-tünet 96,0%; szelesség 65,9%, böfögés 61,3%, hányinger 60,3%. A célba érők 43,9%-ánál a GI-tünet rontotta a teljesítményt (ebből hányinger 86%); a feladók 35,6%-a a GI-panasz miatt adta fel (hányinger 90,5%). A tünetek a legmelegebb szakaszon tetőztek. [stuempfle-2015-wser-gi B]

2. **A "súlyos" GI-tünet gyakorisága az esemény hosszával nő: 4% maratonon, 14% félironmanen, ~31% Ironmanen – de a profi kerékpárosoknál csak 7%.** n=221, hat esemény; a kerékpáros alcsoportok (100/150 km amatőr, profi szakaszverseny) a legalacsonyabb tünetarányúak, CHO-bevitelük is a legkisebb (35±26 g/h vs. IM 62–71 g/h). A GI-előzmény a legerősebb prediktor. [pfeiffer-2012-gi-endurance-events B]

3. **Amatőr hosszútávú kerékpárversenyen (Mallorca 312: 167–312 km) a résztvevők 38,4%-a jelez GI-tünetet verseny közben, 13,8% közepes/súlyosat – edzésen csak 22–26%.** n=138 (utólagos minta); szelesség 25,4%, böfögés 23,2%, puffadás 15,2%. Bevitel 59,2 g CHO/h, ~500 ml/h, ~285 kcal/h. **A bevitel és a tünetek között nem volt összefüggés**; a nyugalmi GI-tünetek és a rajt előtti idegesség jelezte előre. [martinez-2025-mallorca312 B]

4. **Állóképességi sportolók 30–50%-a rendszeresen GI-panaszos; futóknál gyakoribb, mint kerékpárosoknál (rázkódás).** [deoliveira-2014-gi-complaints C; jeukendrup-2017-trainingthegut C]

5. **Ultrakerékpáros (RAAM, TCR, 24 h) GI-tünet-prevalenciáról nincs lektorált felmérés.** Keresések: "gastrointestinal symptoms ultra-cycling", "nausea Race Across America", "GI ultra-endurance cycling 24-hour", "Transcontinental Race nutrition gastrointestinal" – csak a Mallorca 312 (≤14 h) és a hyponatraemia-vizsgálatok (Chlíbková 24 h MTB; Black 387 km) adnak kerékpáros terepet, tünetadat nélkül. A könyvben a RAAM-beszámolók (Strasser: folyékony táplálás; l. strasser-* kulcsok) csak C-szintű tapasztalat.

### Okok (mechanizmus)

6. **A GI-zavar küszöbe: ≥2 óra 60% VO2max-on, edzettségtől függetlenül; intenzitással és tartammal nő a bélsérülés, a permeabilitás, romlik a gyomorürülés és a felszívódás.** Két ág: keringési (splanchnikus vérátáramlás-csökkenés → epithel-sérülés → endotoxin) és neuroendokrin (gyomorürülés/tranzit lassul). Hő és futó mozgásforma súlyosbít. [costa-2017-eigs-review A] Maximális terhelésen a splanchnikus vérátáramlás akár 80%-kal csökken. [deoliveira-2014-gi-complaints C]

7. **A hő önmagában ~3,4-szeresére emeli a bélsérülés-markert és ~12-szeresére a GI-tünet-súlyosságot ugyanannál a terhelésnél.** n=10, 2 h 60% VO2max: 35 °C vs. 22 °C → I-FABP +432% vs. +127%; maghő +2,4 vs. +1,4 °C; tünet-incidencia 90% vs. 70%; súlyosság 720 vs. 58 pont (p=0,008). [snipe-2018-heat-gi A]

8. **Az ibuprofen (2×400 mg) kerékpározás közben megduplázza a vékonybél-sérülést és nyolcszorozza a permeabilitást.** n=9, kerékpár-ergométer: I-FABP csúcs 875 (ibuprofen+kerékpár) vs. 474 (kerékpár) vs. 507 (ibuprofen nyugalomban) vs. 352 pg/ml; laktulóz/ramnóz 0,08 vs. 0,04 vs. 0,05 vs. 0,01. [vanwijck-2012-ibuprofen A]

9. **Dehidráció, >500 mOsm/l ital, rost, zsír, fehérje, fruktóz-túlsúly és NSAID a klasszikus rizikólista; a felső GI-tünet a CHO-bevitellel korrelál (r=0,37–0,51), de a magasabb CHO jobb Ironman-időt is ad.** [deoliveira-2014-gi-complaints C; pfeiffer-2012-gi-endurance-events B]

10. **Ultrán a kevés folyadék ELŐZI MEG a hányingert, nem követi: a GI-panaszmentesek 10,9 vs. a panaszosak 5,9 ml/kg/h-t ittak (p=0,001), és több zsírt ettek (0,06 vs. 0,03 g/kg/h).** n=15, Javelina 161 km; asszociáció, nem okság. 75 kg-ra: ~820 vs. ~440 ml/h. [stuempfle-2013-racediet-gi B]

### A bél edzésének protokolljai és bizonyítéka

11. **Két hét napi "bélkihívás" edzés közben (90 g CHO/h, 2:1 glükóz:fruktóz) 60–63%-kal csökkenti a GI-tüneteket és 4–5%-kal javítja a futóteljesítményt.** n=25, RCT: gél -60% (p=0,008), étel -63% (p=0,046), placebo nem; kilégzett H2-csúcs (felszívódási zavar) 6 vs. 9 vs. 12 ppm; 1 h távteszt +5,2% / +4,3% / -2,1%. [costa-2017-guttraining A]

12. **Ugyanez placebo-kontrollal, vakon (n=18): kevesebb bél-diszkomfort (p=0,012), összes tünet (p=0,009), hányinger (p=0,05); H2-csúcs 6±3 vs. 13±6 ppm; 1 h futótáv 11,7→12,3 km (+5%).** Az "etetési tolerancia" (mennyit tud lenyelni) nem változott – a zavaró érzet és a felszívódás igen. [miall-2018-gutchallenge A]

13. **Öt gut-training stratégia: magas napi CHO (28 nap 8,5 vs. 5,3 g/kg/nap → nagyobb exogén CHO-oxidáció kerékpárosoknál), CHO-bevitel edzés közben, gyomortérfogat-edzés, verseny-szimuláció, kevert CHO.** 3 napi 400 g glükóz a gyomor fél-ürülési idejét 29,1→20,7 percre gyorsítja. [jeukendrup-2017-trainingthegut C]

14. **A 2025-ös szisztematikus áttekintés (29 vizsgálat) szerint a gut-training "ígéretes", az ajánlás szerinti CHO-bevitel kevesebb tünettel jár, a low-FODMAP segíthet, a hidrogél nem ad előnyt, a probiotikum vegyes.** [mlinaric-2025-gi-strategies-sr A]

15. **6 napos low-FODMAP diéta a napi GI-tüneteket csökkenti (AUC -13,4; p=0,003), az edzés KÖZBENI tüneteket nem.** n=11, futók. Gyakorlatban: a verseny előtti 1–3 nap rost/FODMAP-szegény menü. [lis-2018-lowfodmap A]

### Mi működik terepen: folyékony vs. szilárd, valódi étel vs. gél, hidrogél

16. **Kerékpárosoknál 80 g/h-n az ital és a gél egyenértékű, a szelet (bar) -3,9% csúcsteljesítményt és több hányingert/teltséget/görcsöt ad tempós tekerésen.** n=12, 140 perc + rámpateszt: ital 370, gél 376, szelet 362, vegyes 368 W. [guillochon-2017-format-cycling A] – Ultra-intenzitáson (50–60% FTP) a szilárd étel toleranciája jobb (l. 10. pont, zsír), ezért a könyv ajánlása: tempós/meleg szakasz = folyékony/gél, lassú/hűvös/éjszakai = valódi étel. Ez utóbbi C-szintű következtetés.

17. **Hidrogél: egy futó-RCT-ben 2,1%-kal gyorsabb az 5 km-es időfutam és kevesebb GI-tünet a sima oldatnál (90 g/h), de a szisztematikus áttekintés szerint összességében nincs előny.** [rowe-2022-hydrogel A vs. mlinaric-2025-gi-strategies-sr A] – kerékpáros vizsgálatokban (a review szerint) nem volt előny.

### Hányinger kezelése

18. **Ondanszetron (4 mg, max. 4 adag) nem javította a hányingert ultrafutáson (p=0,26).** n=31 használó, kettős vak. Gyógyszeres kezelésre nincs pozitív bizonyíték. [pasternak-2021-ondansetron A]

19. **Ami a terepadatokból következik: több folyadék (≥8–10 ml/kg/h), némi zsír, lassítás/hő-csökkentés (a tünetek a legmelegebb szakaszon tetőznek), NSAID kerülése.** [stuempfle-2013-racediet-gi B; stuempfle-2015-wser-gi B; snipe-2018-heat-gi A; vanwijck-2012-ibuprofen A] – "lassíts, hűtsd magad, kortyolj" – az összefűzés szerkesztői (C).

### PROTOKOLL-PARAMÉTEREK (gut training – a könyv gyakorlati blokkjához)
- Időtartam: **2 hét**, napi; edzés közben ≥90 perc (a vizsgálatokban 2 h 60% VO2max). [costa-2017-guttraining A; miall-2018-gutchallenge A]
- Dózis: **90 g CHO/h** (30 g / 20 perc), 2:1 glükóz:fruktóz, 10% w/v; étel-formában is működik (63% tünetcsökkenés). [costa-2017-guttraining A]
- Napi háttér: 8,5 g CHO/kg/nap 28 napig → nagyobb exogén oxidáció (kerékpárosok). [jeukendrup-2017-trainingthegut C, Cox 2010 nyomán]
- Várható hatás: -60% GI-tünet, +4–5% teljesítmény (futás, 1 h); felszívódási zavar felére. Az adaptáció 4 hét feletti időskálájáról nincs adat.
- Verseny előtt 1–3 nap: low-FODMAP/rostszegény. [lis-2018-lowfodmap A]
- Verseny alatt: hő + intenzitás + NSAID = a három legerősebb "GI-szorzó"; ital <500 mOsm/l. [snipe-2018-heat-gi A; vanwijck-2012-ibuprofen A; deoliveira-2014-gi-complaints C]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q4)
- Minden gut-training RCT futókon, laborban, 2 hét, n=18–25; kerékpáros gut-training RCT nincs (keresés: "gut training cyclists randomized", "repetitive gut-challenge cycling").
- Ultrakerékpáros GI-prevalencia (>12 h) nem mért (l. 5. pont). A RAAM/TCR "folyékony táplálás" gyakorlata versenyzői tapasztalat.
- Hányinger-kezelés: egyetlen gyógyszeres RCT (negatív); gyömbér, lassítás, hűtés ultrán nem vizsgált.
- A hidrogél-vizsgálatok rövidek (2–3 h), 90 g/h-n; többnapos, alváshiányos állapotra semmi.
- Mechanikai rázkódás (gravel, MTB) vs. országút GI-hatása kerékpáron nem mért.

### ELLENTMONDÁS (Q4)
- **Hidrogél**: Rowe 2022 (+2,1%, kevesebb tünet, futás) vs. Mlinaric 2025 SR ("nincs előny", kerékpáros vizsgálatok negatívak). Valószínű magyarázat: sport (rázkódás), intenzitás és termék-különbség; ultrára nem bizonyított.
- **CHO és tünet**: Pfeiffer: több CHO → több felső GI-tünet ÉS jobb idő; Martínez: 59 g/h-n nincs összefüggés; gut-training: a magas CHO edzi a belet. Feloldás: a tünet a bevitel × edzettség × körülmény szorzata, nem a bevitel önmagában.
- **Zsír**: klasszikus rizikófaktor (de Oliveira) vs. ultrán a több zsír kevesebb hányingerrel jár (Stuempfle 2013). Intenzitásfüggő.

---

## Q5 — Hidratálás és nátrium

### Izzadásveszteség és izzadás-nátrium egyéni tartománya

1. **Az izzadásráta sportolóknál 1,21±0,68 l/h, de az egyéni tartomány 0,26–5,73 l/h (15,3±6,8; 3,3–69,7 ml/kg/h); az egésztest izzadás-[Na+] 35,9±10,4 (18,2–70,8) mmol/l = ~830 (410–1630) mg/l.** n=506 (kerékpár/futás/triatlon + csapatsportok), 15–50 °C, alkar-tapasz (nyers 43,6±18,2; 12,6–104,8 mmol/l), egésztestre regresszióval korrigálva. [baker-2016-sweat-normative B]

2. **Állóképességi sportolók (kerékpár/futás/triatlon) izzadásrátája 1,28±0,57 l/h, óránkénti nátriumvesztesége 51,7±27,8 mmol/h (≈1190±640 mg/h).** n=1303 sportoló, sportági bontás; csapatsportoké 0,8–0,95 l/h. [barnes-2019-sweat-by-sport B]

3. **Tipikus tartomány: izzadásráta 0,5–2,0 l/h (ritkán >3), lokális [Na+] 10–90, egésztest 10–70 mmol/l; a tapasz túlbecsli az egésztest-értéket; az intenzitás és a hő emeli, a hőakklimatizáció korábban indítja az izzadást.** [baker-2017-sweat-methodology C]

### Ultrakerékpáros terepadatok: folyadékbevitel és testtömeg

4. **24 órás MTB-ultrán a kerékpárosok 0,49±0,15 és 0,55±0,19 l/h-t isznak, testtömegük -2,0 kg (2,7%) és -1,3 kg (1,9%); a többet ivók jobban helyeztek (p=0,04; 0,01).** n=27 MTB-s; többnapos MTB 0,43 l/h, 1. szakasz -2,1%. [chlibkova-2014-24h-mtb-eah B]

5. **387 km-es országúti versenyen 0,58 l/h a bevitel; a célban 39% (7/18) ≤135 mmol/l vér-Na, csak 11% (2/18) mérsékelten dehidrált – a versenyzők mégis a kiszáradástól féltek.** [black-2014-387km-fluid B]

6. **1230 km-es nonstop (≈43 h): 392±85 ml/h, a második félben csökkenő bevitel; a hidráltság a verseny alatt stabil.** [geesmann-2014-1230km B – meglévő kulcs] RAAM-szóló, 11 nap: -2,3 kg. [fesseler-2026-raam58 B – meglévő]

7. **Hat napos önellátó ultrán (1205 km, 19 417 m) a testtömeg stabil (-0,26%), de a testvíz +1,98 l, a plazmatérfogat +18,9%, NT-proBNP +298 ng/l, copeptin +38 pg/ml, szérum-Na +1,8 mmol/l; arc/szemhéj-ödéma az 5. napon tetőzik.** n=13. **A mérleg többnapos ultrán félrevezet**: a zsír/glikogén-vesztést visszatartott víz és só "pótolja" (RAAS+AVP). [gauckler-2024-ultracycling-fluid B]

8. **164 km-es hőségtúrán (34 °C) az EAH-küszöb ~168 ml folyadék/kg összbevitel; a két hyponatraemiás (130 mmol/l) ~190 ml/kg-ot ivott (≈1,4 l/h), az egyik +4,3% testtömeggel, a másik ±0-val.** n=33; szérum-Na vs. összbevitel R²=0,45, vs. Na-bevitel R²=0,28, vs. testtömeg-változás R²=0,22; Na-változás tartománya +6 – -11 mmol/l. [armstrong-2017-eh-cycling B]

### Szomjúság szerinti vs. tervezett ivás

9. **Kültéri, önszabályozott kerékpározáson 2,2% (akár 4%) testtömeg-veszteség nem ront, a szomjúság szerinti ivás jobb, mint az alatta maradó (+5,2%).** [goulet-2011-dehydration-meta A – meglévő kulcs, csak hivatkozás] Labor: a maghő-, pulzusemelkedés arányos a kiszáradással (r=0,98). [montain-1992-dehydration A – meglévő]

10. **Az ellenállásfoglalás: ≥2% testtömeg-vesztés rontja a hőszabályozást és (meleg, hosszú, intenzív terhelésen) a teljesítményt; >90 perc, meleg, magas izzadásráta esetén tervezett ivás, de "soha ne igyál annyit, hogy hízz".** [kenefick-2018-drinking-strategies C]

11. **A hyponatraemia-konszenzus vonala: igyál, ha szomjas vagy – ez a legindividualizáltabb stratégia; tüneti EAH kezelése 100 ml 3% NaCl 10 percenként.** [hewbutler-2017-eah-update C, a 2015-ös konszenzus (Clin J Sport Med 25:303) alapján]

### Hyponatraemia: előfordulás, kockázat, halálesetek

12. **EAH (<135 mmol/l) prevalencia: maraton 5–8%, Ironman 11% (n=1089), ultramaraton 67% (n=15, verseny közben), állóképességi kerékpárosok 6% (n=33), Boston maraton 13% (n=488; kritikus ≤120: 0,6%).** [hewbutler-2017-eah-update C; almond-2005-boston-eah B] Ultrán: WSER célba érők 6,6% [hoffman-2015-sodium-eah-wser B]; 24 h MTB 3,7%, 24 h futás 8,3%, többnapos MTB 7,1% [chlibkova-2014-24h-mtb-eah B]; 387 km kerékpár: 39% ≤135 [black-2014-387km-fluid B].

13. **Kockázati tényezők többváltozósan: testtömeg-gyarapodás OR 4,2 (2,2–8,2), >4 órás versenyidő OR 7,4 (2,9–23,1); egyváltozósan >3 l folyadék, női nem, alacsony BMI.** [almond-2005-boston-eah B] Konszenzus-lista: hipotóniás folyadék túlfogyasztása, hosszú tartam, NSAID (AVP-stimuláció), alacsony testtömeg. [hewbutler-2017-eah-update C]

14. **Halálesetek: igazolt EAH-halál középiskolás futballistáknál, katonánál, egy rendőrnél 19 km-es kerékpártúrán, egyetemistánál – nem a táv, hanem a túlivás öl.** [hewbutler-2017-eah-update C] Ultrakerékpáros EAH-halálesetről lektorált közlést nem találtam (keresés: "hyponatremia death ultracycling", "RAAM hyponatremia fatality", "cyclist died hyponatremia").

15. **30 órás ultrán a nátriumbevitel NEM különbözött a hyponatraemiás és normonatraemiás célba érők között (93,9% szedett sót); egy hyponatraemiás sem fogyott >4,3%-ot – a túlhidratálás az ok, nem a sóhiány.** [hoffman-2015-sodium-eah-wser B]

### Nátriumpótlás: teljesítmény és görcs

16. **Egyetlen terep-RCT mutat teljesítményelőnyt: félironmanen 113 mmol Na+ (≈2,6 g Na, ≈6,6 g só, ~20 mmol/h) → rövidebb versenyidő (p=0,04), magasabb szérum-Na (p=0,03), tendenciásan kisebb testtömeg-vesztés (p=0,09); izzadásveszteség azonos.** n=26; a különbség mértéke az absztraktban nem szerepel. [delcoso-2016-salt-halfironman A]

17. **Görcs: 161 km-en 26,8% görcsöl (+14,3% "közel-görcs"); a görcsölőknél magasabb a CK és gyakoribb a görcs-előzmény; testtömeg-változás, nátriumpótlás, Na-bevitel és szérum-Na NEM különbözik.** n=181 vérminta. [hoffman-2015-cramping-wser B] A nátrium–görcs kapcsolatra "nincs dokumentált tudományos bizonyíték". [veniamakis-2022-sodium-review C]

18. **Ajánlott nátriumbevitel hosszú terhelésen 300–600 mg/h; ital 10–30 mmol/l (230–690 mg/l); a nátrium mérsékli a vér-Na-esést, de túlivás mellett nem előzi meg az EAH-t.** [veniamakis-2022-sodium-review C; hoffman-2015-sodium-eah-wser B]

### Izzadásteszt módszerei

19. **Mérleg-módszer: ΔTesttömeg + bevitt folyadék − vizelet, korrigálva a légzési + metabolikus tömegveszteséggel (együtt 5–15%, több órán lényeges); a ruhában maradt izzadság 8–10% alábecslést ad. Tapasz: alkar-tapasz [Na+] → egésztest y = 0,57x + 11,05; a tapasz helyfüggően túlbecsül.** [baker-2017-sweat-methodology C; baker-2016-sweat-normative B]

20. **Alternatíva saját teszt helyett: validált kültéri kerékpáros izzadásráta-modell (sebesség/teljesítmény, testtömeg, hőmérséklet, páratartalom, szél, napsugárzás) a sweatratecalculator.com oldalon.** A validációs számok a rekonstruált absztraktban nem szerepelnek (kiadói oldal 403). [jay-2024-sweat-prediction-outdoor B]

### KALKULÁTOR-PARAMÉTEREK (Q5)

**A) Izzadásráta (l/h) – tartományok** (a horgonyszámok B-fokozatú adatbázisokból; a sávok hozzárendelése hőmérséklethez/intenzitáshoz szerkesztői összeállítás, C):
| Helyzet | Sáv | Forrás/horgony |
|---|---|---|
| Éjszaka/hűvös (<15 °C), ultra-intenzitás (50–60% FTP) | 0,3–0,6 l/h | ultrakerékpáros bevitel 0,39–0,58 l/h stabil hidráltság/enyhe fogyás mellett [geesmann-2014-1230km B; chlibkova-2014-24h-mtb-eah B; black-2014-387km-fluid B]; alsó tartomány [baker-2017-sweat-methodology C] |
| Mérsékelt (15–25 °C), ultra-intenzitás | 0,6–1,0 l/h | Baker-adatbázis átlag -1 SD…átlag (0,5–1,2) [baker-2016-sweat-normative B] |
| Meleg (25–32 °C) vagy tempós szakasz | 1,0–1,8 l/h | állóképességi átlag 1,28±0,57 [barnes-2019-sweat-by-sport B]; 34 °C-on ~1,4 l/h bevitel EAH-val [armstrong-2017-eh-cycling B] |
| Forró (>32 °C), napsütés, tempó | 1,8–2,5+ l/h | felső tartomány 2,0–3,0 [baker-2017-sweat-methodology C]; max. 5,73 [baker-2016-sweat-normative B] |
Egyéni mérés vagy modell (sweatratecalculator.com) felülírja a táblát. [jay-2024-sweat-prediction-outdoor B]

**B) Izzadás-nátrium (mg/l)**
- Egésztest: átlag ~830 mg/l (36 mmol/l), egyéni 410–1630 mg/l (18–71 mmol/l) [baker-2016-sweat-normative B]; tipikus 230–1610 mg/l (10–70 mmol/l) [baker-2017-sweat-methodology C]. Átváltás: 1 mmol Na = 23 mg; 1 g só (NaCl) = 393 mg Na.
- Kategóriák a kalkulátorhoz: alacsony <500, közepes 500–1000, magas 1000–1500, nagyon magas >1500 mg/l (szerkesztői felosztás a fenti tartományból, C).
- Óránkénti Na-veszteség = izzadásráta × [Na+]; állóképességi átlag ≈1190±640 mg/h [barnes-2019-sweat-by-sport B].

**C) Folyadék-szabályok ("óránkénti minimum/maximum")**
- Alsó jelzés: szomjúság [goulet-2011-dehydration-meta A; hewbutler-2017-eah-update C]; gyakorlati padló ultrán ~6–8 ml/kg/h (450–600 ml/h 75 kg-nál): ez alatt a hányinger-kockázat nőtt (5,9 vs. 10,9 ml/kg/h) [stuempfle-2013-racediet-gi B]; futó-konszenzus 450–750 ml/h [tiller-2019-issn-ultra A – meglévő].
- Felső korlát: ne hízz [kenefick-2018-drinking-strategies C; almond-2005-boston-eah B: hízás OR 4,2]; összbevitel <168 ml/kg egy napon belül (12,6 l / 75 kg) [armstrong-2017-eh-cycling B]; bevitel ≤ becsült izzadásráta.
- Elfogadható testtömeg-veszteség egy napon belül: 2% (konzervatív) – 4% (önszabályozott kerékpározás, hűvösben) [kenefick-2018-drinking-strategies C; goulet-2011-dehydration-meta A]; többnapos ultrán a mérleg nem hidráltsági mérő (visszatartott víz +2 l stabil tömeg mellett) [gauckler-2024-ultracycling-fluid B].

**D) Nátrium-szabályok**
- Pótlási alap: 300–600 mg Na/h; ital 230–690 mg/l [veniamakis-2022-sodium-review C]; magas izzadás-Na (>1000 mg/l) és meleg esetén az egyéni veszteség 50–80%-a (szerkesztői ajánlás, C; a teljes pótlás szükségességére nincs bizonyíték).
- Bizonyított hatás: félironmanen ~20 mmol/h (460 mg/h) → gyorsabb idő [delcoso-2016-salt-halfironman A]; ultrán teljesítmény- vagy görcs-hatás nem bizonyított [hoffman-2015-cramping-wser B; hoffman-2015-sodium-eah-wser B].
- A só nem véd a túlivás ellen: a nátriumbevitel nem különbözött EAH-sok és nem-EAH-sok között [hoffman-2015-sodium-eah-wser B].

### GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q5)
- Kerékpáros ultrán (>12 h) MÉRT izzadásráta nincs – csak bevitel és testtömeg (keresés: "sweat rate ultra-cycling 24 h", "sweat rate Race Across America", "sweat sodium ultra-endurance cyclists"). A Black 2014-tapaszadatok az absztraktban nincsenek számszerűsítve.
- Nátriumpótlás teljesítményhatása: egy 5–6 órás triatlon-RCT (hatásméret az absztraktban nem közölt); ultrán RCT nincs.
- Szomjúság megbízhatósága alváshiányban, 2–10 napos terhelésben: nincs adat (a Gauckler-vizsgálat mutatja a víz-visszatartást, de nem méri a szomjúságot).
- Hőmérséklet-függő izzadásráta-táblázat kerékpárosoknak: csak modell (Jay 2024, "proprietary") vagy adatbázis-átlag; a fenti tábla szerkesztői összeállítás.
- Női ultrakerékpáros hidratálási adat: Gauckler n=5 nő, Chlíbková külön nem bontja.

### ELLENTMONDÁS (Q5)
- **Tervezett ivás (Kenefick: ≥2% ront) vs. szomjúság (Goulet: 2–4% nem ront; Hew-Butler: EAH-megelőzés).** Feloldás a könyvben: rövid/meleg/intenzív = tervezett felső határral; ultra = szomjúság + "ne hízz" + padló 6–8 ml/kg/h. Goulet és Valenzuela kommentárt írt Kenefick cikkéhez (Sports Med 2018) – nem nyitottuk meg.
- **"Többet ivók gyorsabbak" (Chlíbková 24 h MTB [chlibkova-2014-24h-mtb-eah B]; 100 km futás r=-0,50 [knechtle-2011-100km-eah B]) vs. "a több folyadék EAH-t okoz" (Armstrong, Black).** Nem ellentmondás: a gyorsabbak többet izzadnak → többet isznak; a kockázat a bevitel/izzadás aránya, nem az abszolút bevitel.
- **Sópótlás gyorsít (Del Coso) vs. só nem véd, nem görcsöl (Hoffman).** Különböző kérdések: 5–6 órás meleg verseny teljesítménye vs. 30 órás EAH/görcs. Ultrán a sóbevitel értelme a Na-esés mérséklése és az étvágy, nem a görcs-prevenció.

---

## Feltörekvő irányok (D)
- Egésztest-izzadásráta-modellek kültéri kerékpározásra (Jay 2024) – validáció publikált, egyenlet nem; ultrán (alacsony intenzitás, éjszaka) nem validált.
- Viselhető izzadás-szenzorok (tapasz-alapú, valós idejű [Na+]) – nem kerestük szisztematikusan, ultrán nincs validáció.
- Copeptin/NT-proBNP mint többnapos "túltöltöttség" marker (Gauckler 2024) – első adat, n=13.
- Hidrogél ultra-dózisokon (>100 g/h, Strasser-féle 105–116 g/h) – csak versenyzői tapasztalat [strasser-inscyd-2022 C].
- Low-FODMAP versenymenü (gél/ital-összetétel) – Lis 2018 csak napi étrend.

## Nem sikerült megnyitni
- Springer: Rüst/Knechtle 2012 "No case of EAH in top male ultra-endurance cyclists: the Swiss Cycling Marathon" (10.1007/s00421-011-2024-y) – 429 rate-limit; OpenAlex absztrakt üres; ResearchGate 429. (Kerékpáros EAH-adat hiányzik emiatt – 720 km-es verseny.)
- Europe PMC REST (Del Coso 2016 teljes absztrakt) – 429; a hatásméret (perc) ezért hiányzik.
- cdnsciencepub.com (Costa 2017 gut-training) – 403; Wiley (Miall 2018; Del Coso 2016) – 403; T&F (Mlinaric 2025) – 403; Human Kinetics (Stuempfle 2013) – 403; journals.physiology.org (Jay 2024) – 403; kireports.org (Gauckler 2024) – 403 (ScienceDirect tükör nyílt meg); PubMed – reCAPTCHA. Ezeknél OpenAlex-rekonstrukció vagy Crossref az alap.
- Hoffman & Stuempfle 2015 cramping – springeropen redirect a rate-limitelt Springer-domainre; OpenAlex használva.
- Peters 1999 (runners/cyclists/triathletes GI-prevalencia) – rossz DOI-t adott a keresés, nem található meg ellenőrizhetően; kihagyva.

## Csomag C

**Kérdések:** Q6 (koffein és más szerek, NSAID), Q8 (hőség / hideg / magasság), Q9 (verseny előtti és utáni táplálkozás, RED-S)
**Forrásfájl:** `data/raw/03-C-sources.yaml` (32 új kulcs) + hivatkozott meglévő kulcsok a `data/sources.yaml`-ból.
**Készült:** 2026-09-23. Fokozat: A = meta/RCT/kontrollált labor/konszenzus; B = terep/megfigyelés/eset; C = narratív/edzői/gyártói; D = feltörekvő.

---

## Q6 — Koffein és más szerek ultrán; NSAID-kockázat

### Számszerű állítások

1. **A koffein hatásos adagja 3–6 mg/kg, de 1–3 mg/kg is mérhetően ergogén; 9 mg/kg felesleges és mellékhatásos.** Az ISSN-állásfoglalás szerint a leggyakoribb időzítés 60 perccel a terhelés előtt, és a koffein "a fáradtság felhalmozódásakor", hosszú terhelésnél a leghasznosabb. [guest-2021-issn-caffeine A]

2. **Ultrán az ismételt kis adag ugyanannyit ér, mint az egy nagy: 6×1 mg/kg 20 percenként +3,1%, egy 6 mg/kg adag +3,4%, kóla a végén (~1,5 mg/kg) +3,1% időfutam-javulás** (n=12 versenyző kerékpáros, 2 h + időfutam; a B-vizsgálatban a koffein önálló hatása +2,2%, 95% CI 0,5–3,8). [cox-2002-caffeine-protocols A]

3. **A koffein 20–24 órás versenyen ténylegesen kis mennyiségben kerül be: 142 ± 76 mg/24 h (~2 mg/kg) egy 24 órás váltóverseny 8 kerékpárosánál, és nem függött össze a teljesítménnyel.** [bescos-2012-24h-relay B] – ez az egyetlen kerékpáros terepadat mért koffeinbevitelről.

4. **A koffein alvásra gyakorolt hatása nagy: átlagosan −45 perc teljes alvásidő, −7% alváshatékonyság, +9 perc elalvási latencia; 107 mg-ot ≥8,8 órával, 217 mg-ot ≥13 órával a tervezett alvás előtt kell bevenni.** [gardiner-2023-caffeine A] Az ISSN is rögzíti, hogy objektív alvásmérésekben rontja a latenciát, a WASO-t, a hatékonyságot és az alvásidőt. [guest-2021-issn-caffeine A]

5. **A „koffein + rövid alvás” (200 mg közvetlenül egy 30 perces alvás előtt) éjszakai műszak-szimulációban javította az éberséget és a teljesítményt** [centofanti-2020-caffeinenap A]; 255 mg koffein a hatását 15–45 perc között éri el és 60–75 percre lecseng; a 30 perces alvás nem adott többet a 15 percesnél. [filtness-2026-caffeinenap A] → ultra-alkalmazás: a koffeint a bivakolás/pihenő *elején*, nem a végén.

6. **Genetikai érzékenység: 101 férfi kerékpárosnál a CYP1A2 AA genotípus 2 mg/kg-nál −4,8%, 4 mg/kg-nál −6,8% időt hozott; AC-nél semmi; CC-nél a 4 mg/kg +13,7%-kal RONTOTT (20,8 vs 18,3 perc, p=0,04).** [guest-2018-cyp1a2-cycling A] **De** 17 tanulmány áttekintésében csak 4 mutatott genotípus-különbséget, és azok kicsik/inkonzisztensek – rutin génteszt nem indokolt. [grgic-2021-cyp1a2-sr A]

7. **Tolerancia: 4 hét napi koffein toleranciát növelt az akut adagra (n=18 alacsony fogyasztó)** [guest-2021-issn-caffeine A, hivatkozott vizsgálatból] – a verseny előtti heti mérséklés élettanilag indokolt, de ultrán nem tesztelt.

8. **Nitrát: 80 RCT metaanalízisében a hatás összességében kicsi (d=0,17), jól edzett állóképességi sportolóknál (VO2max ≥65) nulla (d=0,02).** [senefeld-2020-nitrate-meta A] Ultra-távú vizsgálat nincs.

9. **Bikarbonát: a 30 mp–12 perces, nagy intenzitású feladatokra igazolt (0,2–0,3 g/kg, 60–180 perccel előtte), fő mellékhatása puffadás, hányinger, hányás, hasi fájdalom** – ultrán irreleváns és GI-kockázatos. [grgic-2021-issn-bicarbonate A]

10. **Kreatin: 28 nap 3 g/nap növelte az izom-kreatinfoszfátot és a plazmatérfogatot, ~10%-kal csökkentette a szubmaximális O2-fogyasztást, de egy 2 órás szimulált országúti versenyen nem javította a teljesítményt (n=12).** [hickner-2010-creatine-cycling A, absztrakt-parafrázis] Vízretenció (+1–2 kg) hegyi ultrán hátrány.

11. **NSAID – vese: ibuprofen 400 mg/4 h vs. placebo 80 km-es sivatagi ultrafutó-szakaszon (RCT, n=89): AKI 52% vs 34% (különbség 18%, 95% CI −4–41), súlyosabb fokozat ibuprofennél, NNH 5,5; az ultrafutók akár 75%-a használ NSAID-ot.** [lipman-2017-ibuprofen-aki A]

12. **NSAID – GI és kórház: 3913 maratonistából 49% vett be fájdalomcsillapítót; náluk ~5× több nemkívánatos esemény (kockázatkülönbség 13%), dózisfüggően; 9 kórházi felvétel (3 veseelégtelenség ibuprofen, 4 vérzés aszpirin, 2 infarktus) a szedők közül, 0 a kontrollból.** [kuster-2013-analgesics-marathon B]

13. **NSAID – hyponatraemia: 330 Ironman-indulónál 30% NSAID-használat; az NSAID összefüggött a hyponatraemia előfordulásával (p=0,0002), alacsonyabb plazma-Na (p=0,02); összincidencia 1,8%.** [wharam-2006-nsaid-eah-ironman B]

14. **Kerékpáron a CK/rhabdomyolízis-kockázat kisebb, mint futásnál: 113 cseh ultrázó közül a >10 000 U/l CK-t mutató 6 versenyző mind futó volt; a CK %-os emelkedése MTB-seknél kisebb; hyponatraemiásoknál nagyobb CK- és vizelet-kreatinin-emelkedés.** [chlibkova-2015-rhabdo-eah B] 48 órás kalandversenyen (n=20, 30% NSAID-használó) az NSAID-csoport mioglobinja alacsonyabb, de a versenyideje hosszabb volt. [wichardt-2011-nsaid-adventure B]

15. **Ellenpont: 24 órás naproxen (220 mg/8 h) euhidrált, mérsékelt intenzitású kerékpározásnál 35,7 °C-on sem GI-panaszt, sem teljesítményromlást nem okozott (n=11).** [emerson-2020-naproxen-heat A] → az ártalom a dehidráció + hőség + hosszú terhelés kombinációhoz kötött.

### KALKULÁTOR-PARAMÉTEREK (koffein-adagoló)
- **Egyszeri adag:** 1–3 mg/kg (ultra), max. 3–6 mg/kg egy kritikus szakaszra; 9 mg/kg tilos. [guest-2021-issn-caffeine A]
- **Ismételt adag:** ~1 mg/kg / 20 perc (labor) ≈ gyakorlatban 50–100 mg / 60–90 perc; kóla 5 ml/kg-onként ~1,5 mg/kg. [cox-2002-caffeine-protocols A]
- **Napi plafon:** nincs ultra-adat; a bescos-2012 terepátlag 2 mg/kg/24 h; általános biztonsági plafon 400 mg/nap (EFSA – itt nem ellenőrzött forrás, ne idézd számként).
- **Alvás-időablak:** tervezett alvás előtt ≥8,8 h (107 mg), ≥13,2 h (217 mg); gyakorlatban: az utolsó koffein a bivak előtti „koffein-nap”-nál, 200 mg közvetlenül a 15–30 perces alvás előtt, utána ~4–6 óra koffeinmentes. [gardiner-2023-caffeine A; centofanti-2020-caffeinenap A; filtness-2026-caffeinenap A]
- **Kezdő időzítés:** első adag nem a rajtnál, hanem a fáradtság felhalmozódásakor (labor: 80–100 perc után; ultrán: első éjszaka / 8–12 óra után) [guest-2021-issn-caffeine A; cox-2002 A]
- **NSAID-döntési szabály:** verseny alatt NSAID (ibuprofen, naproxen, diklofenak) NEM; ha elkerülhetetlen, csak euhidráltan, hőségcsúcson kívül, egyszeri adag; paracetamol a kevésbé veseterhelő alternatíva (erre itt nincs ellenőrzött forrás – jelöld). [lipman-2017 A; kuster-2013 B; wharam-2006 B; emerson-2020 A]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK
- Nincs RCT vagy kontrollált terepvizsgálat koffein-adagolásról >6 órás vagy többnapos kerékpáros eseményen (keresés: „ultra-cycling caffeine intake race field study Race Across America 24-hour ultra-endurance cyclists supplement use caffeine mg”; csak bescos-2012 megfigyeléses adat). A „ismételt kis adag vs. egy nagy” ultra-kontextusban a cox-2002 2,5 órás laboradat extrapolációja.
- Koffein-megvonás (fejfájás, fáradtság) hatása versenyteljesítményre ultrán: nincs forrás.
- NSAID ultrakerékpáron: minden vese/GI/EAH-adat futó, triatlon vagy kalandverseny; kerékpáros ultrán (RAAM, TCR) NSAID-használati arány ismeretlen.
- Nitrát, kreatin >4 órás eseményen: egyetlen vizsgálatot sem találtam (keresés: „dietary nitrate OR creatine supplementation ultra-endurance cycling OR ultramarathon randomized trial performance >4 hours”).
- Genotípus-vizsgálatok mind rövid időfutamon; a CC-csoport a guest-2018-ban ~8 fő.

### ELLENTMONDÁS
- **CYP1A2:** guest-2018 (CC genotípus rontás 13,7%) vs. grgic-2021 (a genotípus-hatás kicsi, inkonzisztens). Feloldás a tankönyvben: a genotípus nem döntő, az egyéni tesztelés edzésen az.
- **NSAID-ártalom:** lipman-2017/kuster-2013/wharam-2006 (AKI, GI, EAH kockázat) vs. emerson-2020 (naproxen euhidrált, rövid kerékpározásnál ártalmatlan) és wichardt-2011 (NSAID mellett alacsonyabb mioglobin). Feloldás: az ártalom feltételes – dehidráció + hőség + hosszú terhelés + ismételt adag.
- **Koffein ergogén vs. alvásromboló:** ugyanaz az adag, ami az éjszakai szakaszon +3% és éberség, a bivak alvását 45 perccel rövidíti. Ultrán az alvásminőség a nagyobb tét → időzítés, nem adag a kulcs.

---

## Q8 — Hőségben és hidegben evés-ivás; magasság

### Számszerű állítások

1. **Izzadási ráta állóképességi sportban 1,28 ± 0,57 l/h (1303 sportoló adatbázisa), nátriumveszteség 51,7 ± 27,8 mmol/h (~1,2 g Na/h); egyéni szélső érték 0,7–1,9+ l/h.** [barnes-2019-sweat-normative B] Hőségben, nagy teljesítménynél a 2 l/h reális, de ez nem 24 órás átlag.

2. **Ultrakerékpáron a 24 órás folyadékbevitel ~10,5 l (0,44 l/h átlag, váltó)** [bescos-2012-24h-relay B], **1230 km-en 392 ± 85 ml/h, a második félben csökkenő** [geesmann-2014-1230km B]; **720 km-en (n=65) −1,5 ± 1,7% testtömeg, ad libitum ivással nulla hyponatraemia** [rust-2012-swiss-cycling-marathon B].

3. **A dehidráció fiziológiai ára arányos: a maghő és a pulzus emelkedése lineáris a felhalmozott kiszáradással (r=0,98, 1,1–4,2% között, 2 h meleg)** [montain-1992-dehydration A], **de önszabályozott, kültéri terhelésen ~2% (max 4%) veszteségig nincs teljesítményromlás, és a szomjúság szerinti ivás +5,2%-kal jobb, mint az alatta maradó** [goulet-2011-dehydration-meta A].

4. **A gyomorürülést nem a meleg levegő, hanem a maghő + dehidráció lassítja: gyomorürülés vs. rektális hőmérséklet r=−0,76; 35 °C-on euhidráltan nem csökkent, 49 °C-on és 35 °C + −5% hypohidrációnál igen.** [neufer-1989-gastric-heat A] → hőségben a folyadék korán, kis adagokban, még a deficit előtt.

5. **Hőségben az étvágy csökken: 40 perc futás 36 °C-on után a kiadásra korrigált energiabevitel alacsonyabb (p=0,002), magasabb dobhártya-hőmérséklettel és PYY-szinttel összefüggésben (n=11)** [shorten-2009-heat-appetite A]; hidegvízben végzett terhelés után viszont 41–44%-kal (3666 ± 1910 kJ) magasabb a bevitel, más adatokban +74–171%. [charlot-2017-hot-cold-review C]

6. **Hűtés hőségben: 28 tanulmány metaanalízisében az előhűtés +5,7%, a terhelés alatti hűtés +9,9%, összesen +6,7% teljesítmény (ES 0,43; 323 fő).** [bongers-2015-cooling-meta A]

7. **Jégkása (7,5 g/kg, −1 °C) 0,66 °C-kal csökkenti a maghőt (hideg víz: 0,25 °C), és 34 °C-on +19% kimerülési időt ad (50,2 vs 40,7 perc), miközben a kimerüléskori maghő magasabb (39,36 vs 39,05 °C) – „hőtárolót nyit”.** [siegel-2010-ice-slurry A] 70 kg-ra ez ~500 g jégkása.

8. **Hőségben a munkaráta viselkedésesen csökken: 15 perc önszabályozott kerékpározás 40 °C-on ~17%-kal kevesebb munka, elit 30 perces időfutam 32 °C-on −6,5%** [periard-2021-heat-review C]; a konszenzus a belső hűtést (jégkása) versenyen alkalmazhatónak tartja. [racinais-2015-heat-consensus C]

9. **Hidegben az energiaigény 5000–7000 kcal/nap is lehet, a deficit a szükséglet 70%-áig nőhet, mert „nincs éhség, nincs idő enni”; hideg esőben azonos sebesség több O2-t és laktátot igényel (5 °C, 70% VO2max).** [smid-2025-cold-nutrition C; ito-2013-rain-cold A] Versenyzői becslés: hidegben +200 kcal/h. [tuft-7mesh-winter-tips C]

10. **Fagyott étel/ital kezelése (tapasztalati): tömlő/bladder a testhez közel, palack éjjel a hálózsákba, szigetelt palack, gélek a mezzsebben melegítve, forró tea/étel dideregéskor.** [tuft-7mesh-winter-tips C] A 2026-os TCR nyitónapján −1…−3 °C-ban az élboly 5–31 perc álló időt engedett meg – a hidegben az evés-ivás menet közben kell hogy működjön. [mckenzie-2026-tcr12-frozen B]

11. **Magasságban az energiabevitel mérsékelten csökken (SMD −0,50; 95% CI −0,85 – −0,15; 28 tanulmány), az étvágy és az acil-ghrelin csak „magas”, nem „mérsékelt” szimulált magasságon csökken.** [matu-2018-hypoxia-appetite-meta A] → európai hágókon (2000–2800 m) ez ritkán tényező; Colorado Trail / Silk Road (3500–4000 m+) igen.

12. **Többnapos hidegben (Tour Divide, 16 nap, 16,8 h/nap nyeregben) az első 9 napban energiaegyensúly volt tartható, a testtömeg nem változott** [hyldahl-2024-tourdivide B] – a hideg önmagában nem zárja ki a fedezett bevitelt, ha a szisztéma működik.

### KALKULÁTOR-PARAMÉTEREK (folyadék hőségben / kalória hidegben)
- **Izzadás-becslés:** SR = (m_előtt − m_után + bevitt folyadék − vizelet) / idő; alapérték 1,3 l/h (±0,6) meleg nappali szakaszra; éjszaka/hűvös 0,4–0,6 l/h. [barnes-2019 B; geesmann-2014 B; bescos-2012 B]
- **Célveszteség:** −1…−2% testtömeg/nap elfogadható, −4% felett teljesítmény- és hőterhelés-kockázat; szomjúság vezérelt ivás + időzített minimum hőségben. [goulet-2011 A; montain-1992 A; rust-2012 B]
- **Nátrium:** ~50 mmol/h (~1,2 g Na ≈ 3 g só) izzadási óránként állóképességi átlagon; egyéni ±50%. [barnes-2019 B]
- **Hűtés:** jégkása 5–7,5 g/kg (350–500 g) hőségcsúcs előtt/alatt; várható maghő-csökkenés ~0,5 °C. [siegel-2010 A; bongers-2015 A]
- **Hideg-kalória:** +10–20% (tapasztalati +200 kcal/h) a semleges alapigényhez; didergésnél lényegesen több, de ultrakerékpáron a didergés = megállás/menedék jel, nem tervezési paraméter. [smid-2025 C; tuft-7mesh C; ito-2013 A]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK
- Ultrakerékpáros izzadási ráta hőségben (l/h, 24+ óra) publikált mérése nincs; a barnes-2019 „endurance” kategória 1–2 órás mérés. Kerékpáros terepadatok (geesmann, bescos, rust) bevitelt, nem veszteséget mérnek.
- Jégkása/hideg ital ultrán (>3 óra) nincs vizsgálva; minden hűtési adat <1 órás labor.
- Hideg étvágy-adatok hidegvíz-immerzióból, nem kerékpározásból (charlot-2017).
- Hideg kalóriaszorzó (×BMR) kerékpáros ultrán: hyldahl-2024 (n=1) az egyetlen, és nem bontja hideg/meleg napokra.
- Magasság: sportolói, terhelés alatti bevitel-adat kevés; matu-2018 főleg nyugalmi hypoxia.

### ELLENTMONDÁS
- **Dehidráció:** montain-1992 (minden % kiszáradás mérhető élettani ár) vs. goulet-2011 (önszabályozott kültéri terhelésen 2–4%-ig nincs teljesítményromlás). Feloldás: hőterhelés/biztonság vs. teljesítmény külön; ultrán a többnapos kumulált deficit a kritikus, nem az órás %.
- **Jégkása:** siegel-2010 magasabb kimerüléskori maghő = teljesítmény-előny, de hőguta-kockázatot is jelenthet (a periard-2021 >40 °C maghő-küszöbe) – a belső hűtés nem helyettesíti a munkaráta-csökkentést.
- **Étvágy hidegben nő (charlot-2017) vs. hidegben „nincs éhség” (smid-2025):** a hidegvíz-immerziós ghrelin-válasz vs. a terepi, fáradt, időhiányos evés – a terep győz.

---

## Q9 — Verseny előtti és utáni táplálkozás

### Számszerű állítások

1. **Szénhidrát-feltöltés >90 perces eseményre: 36–48 órán át 10–12 g/kg/24 h; rajt előtti étkezés 1–4 g/kg CH 1–4 órával előtte; gyors visszatöltés 1–1,2 g/kg/h az első 4 órában.** [thomas-2016-joint-position A]

2. **Egy nap elég: pihenő + 10 g/kg/nap CH mellett az izomglikogén 95 → 180 mmol/kg nedves tömeg 24 óra alatt, a 2–3. napon nem nő tovább (n=8).** [bussau-2002-1day-loading A] → többnapos ultrára a 3 napos „hízlalás” felesleges; az utolsó 24–36 óra feltöltése elegendő.

3. **A feltöltésnek többnapos eseményen korlátozott értelme van: a teljes raktár (~500–600 g) 6–10 óra tekerést fedez, utána a bevitel dönt – 1230 km-en (43 h) a deficit ~5500 kcal, a CH-bevitel 57 g/h és 618 km után csökken** [geesmann-2014-1230km B]; **384 km-en (16 h) a magasabb energiabevitel rövidebb idővel járt (p=0,023)** [black-2012-384km B]; **RAAM-váltón 1503 kcal/nap deficit** [hulton-2010-raam-energy B]; **a fenntartható bevitel ~2,36 × BMR, ami felett a test raktárait éli fel** [thurber-2019-alimentary B].

4. **Az első nap teljes raktárral indulás mégis számít: a Tour Divide-on az első 9 nap energiaegyensúlyban telt, a testtömeg nem változott** [hyldahl-2024-tourdivide B]; **egy 11 napos szóló RAAM-on 21 169 kcal deficit, −2,3 kg, csökkenő vércukor (−0,92 mg/dl/nap)** [fesseler-2026-raam58 B] – a feltöltés a deficit *kezdetét* tolja ki.

5. **Rajt előtti étkezés gyakorlata: 1–4 g/kg CH 1–4 órával a rajt előtt, alacsony rost/zsír; hosszú eseményen nincs külön ultra-protokoll.** [thomas-2016-joint-position A; tiller-2019-issn-ultra C]

6. **Regeneráció fehérje: napi 1,4–2,0 g/kg (energia-megszorításban 2,3–3,1 g/kg FFM), adagonként 0,25 g/kg vagy 20–40 g, 3–4 óránként, lefekvés előtt 30–40 g kazein** [jager-2017-issn-protein A]; **0,25–0,3 g/kg (15–25 g) a terhelés utáni 0–2 órában** [thomas-2016 A]. Többnapos ultra után a felső sáv (1,8–2,2 g/kg) indokolt a CK/izomvesztés miatt.

7. **Alvás és regeneráció: UTMB (n=19) után a 2. éjszakán WASO-csúcs, amely az izomfájdalommal korrelált; szubjektív regeneráció az 5. napig romlott, teljes helyreállás ~6 nap.** [baron-2022-utmb-recovery B] → az első 48 óra: fehérje + CH + alvás elsőbbség, nem edzés.

8. **CK ultrán kerékpáron mérsékelt: 113 ultrázóból a >10 000 U/l CK-t mutató 6 versenyző mind futó; MTB-seknél kisebb %-os emelkedés** [chlibkova-2015-rhabdo-eah B]; **3 hetes Girón (n=9) a CK/AST a második félben emelkedett, és a CK-emelkedés a kreatinin-alapú GFR-becslést torzítja – cisztatin C pontosabb** [colombini-2012-giro-ck B]; 48 h kalandversenyen a mioglobin végig emelkedett (n=20) [wichardt-2011-nsaid-adventure B].

9. **Vas: vashiány a női sportolói kohorszok ~15–35%-ánál, férfiaknál ~5–11%; hepcidin-emelkedés a terhelés után gátolja a felszívódást** [sim-2019-iron-athlete C]; **ferritin aggályos tartomány <10–35 ng/ml (laborfüggő)** [thomas-2016 A].

10. **D-vitamin: elégséges >75 nmol/l, súlyos hiány <25, toxicitási aggály >180 nmol/l; 4000 NE/nap javította az erő regenerációját izomkárosító terhelés után; alacsony szint több felső légúti fertőzéssel jár; célérték 80–125 nmol/l.** [owens-2018-vitamin-d C; thomas-2016 A; smid-2025 C: 1500–2000 NE/nap hidegben]

11. **RED-S: a REDs „problémás (elhúzódó/súlyos) alacsony energia-elérhetőség okozta szindróma”; küszöb történetileg ≤30 kcal/kg FFM/nap (nők), férfiaknál ~9–25 is tolerálható; prevalencia nők 23–79,5%, férfiak 15–70%; a vizsgálatok csak 20%-a férfi.** [mountjoy-2023-ioc-reds A; thomas-2016 A]

12. **Kerékpáros-specifikus: 50 versenyző férfi országútis 44%-ánál alacsony ágyéki csontsűrűség (Z<−1); a 10 krónikus LEA-s alacsonyabb tesztoszteronnal (p=0,024); az edzésterhelés nőtt az FTP/kg-mal, de a LEA csont-, hormon- és teljesítmény-hátrányt adott.** [keay-2018-male-cyclists-lea B]

### KALKULÁTOR-PARAMÉTEREK (feltöltés / regeneráció)
- **Feltöltés (utolsó 24–36 h):** CH = 10 g/kg/nap (tartomány 8–12), pihenőnappal; 70 kg → 700 g CH/nap. [bussau-2002 A; thomas-2016 A]
- **Rajt előtti étkezés:** CH = 1–4 g/kg, 1–4 h előtte (70 kg: 70–280 g); minél közelebb, annál kevesebb. [thomas-2016 A]
- **Regeneráció, 0–4 h:** CH 1,0–1,2 g/kg/h + fehérje 0,3 g/kg; **napi (verseny utáni 3–7 nap):** fehérje 1,8–2,2 g/kg/nap 4–5 adagban, + 30–40 g kazein este; CH 5–8 g/kg/nap. [thomas-2016 A; jager-2017 A]
- **Energia-elérhetőség felkészülésben:** EA = (bevitel − edzés-kiadás) / FFM ≥ 30 kcal/kg FFM/nap (nők), férfiaknál sem tartósan 25 alatt; testtömeg-cél: max −0,5 kg/hét, versenyszezonban nem. [mountjoy-2023 A; keay-2018 B]
- **Labor a felkészülés elején (12–16 hét):** ferritin (<35 ng/ml: pótlás/orvos), 25(OH)D (cél 80–125 nmol/l), verseny után 48–72 h: CK + kreatinin/cisztatin C, ha tünet. [thomas-2016 A; owens-2018 C; colombini-2012 B]

### GYENGE / HIÁNYZÓ BIZONYÍTÉK
- Nincs RCT arról, hogy a szénhidrát-feltöltés javítja-e a többnapos ultra-kerékpáros teljesítményt; a „van-e értelme” érvelés glikogén-kinetikából (bussau) és deficit-terepadatokból (geesmann, hulton, fesseler) származik.
- Rajt előtti étkezés ultrán: nincs kontrollált vizsgálat; a thomas-2016 általános ajánlás.
- CK abszolút értékek (U/l) ultrakerékpáron az elérhető absztraktokban nincsenek (chlibkova, colombini); a lefutás (csúcs 24–48 h, normalizálás 5–7 nap) futóadatokból ismert, kerékpáron nem dokumentált.
- Regeneráció többnapos *kerékpáros* ultra után (alvás, hormonok, immun): egyetlen követéses vizsgálat sincs; baron-2022 (UTMB) és fachan-2026 (meglévő kulcs) futó.
- RED-S ultrakerékpárosoknál: keay-2018 országúti; ultra-populáción nincs adat.
- Vas/D-vitamin hatása ultra-teljesítményre: csak státusz-adatok, nem kimenet-vizsgálatok.

### ELLENTMONDÁS
- **Feltöltés:** thomas-2016 (36–48 h, 10–12 g/kg) vs. bussau-2002 (24 h elég) vs. a többnapos deficit-realitás (geesmann, fesseler): a tankönyvi feloldás „egy nap teljes feltöltés + az első 10 óra fegyelmezett bevitele”.
- **Energiaegyensúly többnapos eseményen:** hyldahl-2024 (9 napig egyensúly, testtömeg stabil) és purcell-2025 (30 nap, testtömeg stabil, PAL 3,7–4,1) vs. hulton-2010 / fesseler-2026 / thurber-2019 (deficit a norma, 2,36 × BMR plafon). Feloldás: alvással tagolt, „túrázó” tempón fedezhető; nonstop verseny-tempón nem.
- **D-vitamin és csont:** owens-2018 (nincs összefüggés 25(OH)D és csontsűrűség között sportolóknál) vs. a kerékpáros csontsűrűség-probléma (keay-2018, LEA) – a csont ügye ultrakerékpáron elsősorban energia-elérhetőség és terhelés-hiány, nem D-vitamin.

---

## Feltörekvő irányok (D)
- **Koffein-genotípus alapú személyre szabás** (CYP1A2/ADORA2A tesztek): a grgic-2021 szerint még nem indokolt; ultrán alvás-tolerancia lenne a releváns végpont – nem vizsgált.
- **Koffein + alvás-mikrociklus optimalizálás** ultrán (koffein-nap, 15 perces alvás): laborból (filtness-2026, centofanti-2020) átvitel, terepi validálás nélkül.
- **Cisztatin C mint terepi vesemarker** (colombini-2012) – ultra-orvosi ellátásban a kreatinin helyett; nem elterjedt.
- **Folyamatos glükózmonitor többnapos versenyen** (fesseler-2026): a napi 0,92 mg/dl vércukor-csökkenés mint bevitel-visszajelzés; nem validált intervenció.
- **Jégkása/belső hűtés hosszú eseményen** – minden adat <1 óra; ultra-specifikus protokoll nincs.
- **REDs férfi ultrázóknál** – az IOC 2023 szerint a férfi-adat hiányzik; ultrakerékpáros kohorsz nincs.

## Nem sikerült megnyitni
- Talanian & Spriet 2016, „Low and moderate doses of caffeine late in exercise improve performance in trained cyclists” (Appl Physiol Nutr Metab, DOI 10.1139/apnm-2016-0053): cdnsciencepub 403, Semantic Scholar 429; OpenAlex csak parafrázist adott (100 mg = 1,5 mg/kg és 200 mg = 2,9 mg/kg a 80. percben, mindkettő gyorsabb TT a placebónál) – számok nem idézhetők, nincs felvéve.
- Maughan et al. 2018 IOC-konszenzus étrend-kiegészítőkről (BJSM 52:439): az oldal megnyílt, de a 3. táblázat (nitrát/bikarbonát/kreatin adagok) nem volt kinyerhető – nem felvéve, az ISSN-állásfoglalások helyettesítik.
- Sawka et al. 2007 ACSM „Exercise and fluid replacement” (DOI 10.1249/mss.0b013e318029ba49): Crossref robots-tiltás, OpenAlex 404 – a barnes-2019 normatív adat helyettesíti.
- Costill et al. 1971 „Muscle glycogen utilization during prolonged exercise on successive days” (J Appl Physiol): OpenAlex-rekord absztrakt nélkül – nem felvéve.
- Bescós 2012 teljes szöveg (tandfonline 403, DOAJ 403): csak absztrakt (OpenAlex) – l/h és mg/kg számok az absztraktból.
- Wharam 2006 kiadói oldal (LWW/Ovid 402): absztrakt Europe PMC REST-ből.
- Guest 2018 kiadói oldal (LWW 402, PubMed CAPTCHA): absztrakt Europe PMC REST-ből.
- Europe PMC REST és link.springer.com időszakosan 429 (rate limit) – több Springer-forrás absztraktja OpenAlex/Semantic Scholar API-ból.

## Csomag D

**Kérdések:** Q7 (boltból táplálkozás és valódi étel), Q10 (konvergencia-mátrix), Q11 (feltörekvő)
**Készült:** 2026-09-23. Forrástár: `data/raw/03-D-sources.yaml` (40 új tétel) + hivatkozott meglévő kulcsok a `data/sources.yaml`-ból.
Fokozat: A = meta/SR/RCT/kontrollált labor/konszenzus; B = terep, megfigyelés, esettanulmány mért adattal; C = narratív, edzői/versenyzői, gyártói; D = feltörekvő, nem validált.
Jelölés: *absztraktból* = csak absztrakt/metaadat alapján; *másodlagos* = a szám nem az eredeti mérőtől származik; *parafrázis* = nem szó szerinti idézet.

---

## Q7 — Boltból táplálkozás és a valódi étel

1. **A felszívható energia plafonja önellátó versenyen kb. 200–300 kcal/óra, azaz 4000–7000 kcal/nap – az égetés (6000–12 000 kcal/nap) alatt marad, a deficit tehát a norma.** A ridefar 200–300 kcal/h felszívási becslése és 6000–12 000 kcal/nap TCR-égetése [white-ridefar-food C]; a mért kerékpáros terepadatok ezt igazolják: 1230 km nonstop országúti ultrán 19 749 ± 4502 kcal bevitel vs. 25 303 ± 2436 kcal forgalom, 57,1 g CH/h [geesmann-2014-1230km B, *absztraktból*]; 384 km-en 4470 kcal bevitel a 6100 kcal igény ellen, 52 g CH/h [black-2012-384km B]; a RAAM-váltó 4918 kcal/nap bevitel, 1503 kcal/nap deficit [hulton-2010-raam-energy B]; a hosszú távon fenntartható bevitel 2,36 ± 0,59× BMR, az esemény hosszától függetlenül [thurber-2019-alimentary A]; ISSN egynapos ultrára 150–400 kcal/h, 30–50 g CH/h [tiller-2019-issn-ultra A].
2. **Az élmezőny önbevallott bevitele óriási szórást mutat: Allegaert ~3000 kcal/nap ~450 km/nap mellett (másodlagos), Hayden ~10 000 kcal/nap benzinkúti étel.** [white-ridefar-food C, *másodlagos*; hayden-tcr6-story B – „Consuming 10,000 calories of petrol station food daily is not good for you"]. Egyik sem mért adat; a mért Tour Divide-eset (16,8 h/nap nyeregben) az első 9 napban energiaegyensúlyt mutatott kettős jelölt vízzel [hyldahl-2024-tourdivide B].
3. **A boltos étel valós listája az élversenyzőknél: kóla, chips, tej + gabonapehely, fagylalt, McDonald's, kebab, spanyol tortilla, kenyér + sajt, hot dog, pizza, Haribo, Snickers.** Hayden: éjfélkor „pár liter kóla és chips", hajnali 2-kor McDonald's, „2 doboz gabonapehely és 4 liter tej", 6 fagylalt + kóla a hajrá előtt [hayden-tcr6-story B]; Wilcox: spanyol tortilla, olvadt fagylalt, tej/csokoládés tej, szendvics, hot dog, pizza, chips [wilcox-adventurecycling-2022 C]; Sehili Marokkóban: kenyér + krémsajt, otthonról hozott étel [sehili-rawcycling-atlas C]; Towers: Haribo és Snickers „csúf, de működik" [towers-substack-2026 C]; Baloh a sivatagban fagylaltot használ a hőség ellen [baloh-nduranz-2024 C]; Strasser önellátón: semmi romlandó, fehér kenyér és cukros szirup vízzel [strasser-cyclite-2025 C].
4. **A 24 órás box-etetésben a leggyakoribb ételek banán (86,5%), energiaszelet (50,0%), alma (43,2%) és sajt (43,2%); italban izotóniás (82,4%), víz (71,6%), kóla (54,1%), tea (51,4%); étkezés 30,6 ± 10,5 alkalom/24 h (1,3/óra), folyadék 0,5 ± 0,2 l/h; a bevitel éjjel és az utolsó szakaszban csökken.** [chlibkova-2014-24h-mtb B, n=74 szóló MTB]. Edzői gyakorlat ugyanerre: 250–300 kcal/h, kétszer leülős étkezés (18–20 h és 4–7 h), sózott krumplipüré éjjel, Pepsi a gyomorra [lwcoaching-2008-24h-solo C].
5. **Kísérős RAAM-on a stáb óránkénti folyékony protokollal 500–550 kcal/h-t etet – kétszerese az önellátó „plafonnak".** Strasser: óránként egy palack folyékony táp + egy palack elektrolit [strasser-cyclite-2025 C]; cél 12 000 kcal/nap ~15 000 égetés mellett, csak folyékony táppal (Ensure: 54% CH, 17% fehérje, 29% zsír) + akár 1 l/h CH-elektrolit ital [strasser-datasport-2019 C, önbevallás; 12 000 kcal / ~22 h ≈ 545 kcal/h saját számítás]; Toone-stáb: 300–400 kcal szilárd + 2 palack ital, „legalább 500 kcal/óra", ~8000 kcal/nap, kevés rost, emelkedő előtt szilárd CH, emelkedőn gél + folyadék, hőségben vissza folyékonyra [barnett-2017-raam-toone B]. 24 órás rekordon Strasser 116 g CH/h az első 12 órában, 105 g/h átlag [strasser-inscyd-2022 B].
6. **Brevet-kontrollon a bevált minta: meleg étel (omlett, püré, leves) gyorsan, a leves palackban tovább, megállás <10 perc, a kalória 1/3–1/2-e italból/sporttápból, mindig étel a kontrollok között.** [dickson-rusa-pbp C]; brevet-edzői ökölszabály 200–300 kcal minden órában, szomj szerinti ivás [hughes-rbr-showstoppers-2019 C; hughes-rbr-2015 C: óránként max 5 perc a nyeregből].
7. **Az édes-fáradás valós és korai: a boltos „sós fordulat" (chips, sajt, kenyér, dió) az élversenyzőknél konvergens.** Wilcox: „pretty tired of sweet stuff early on… looking for something savory… Amazing how far a bag of potato chips can get you!" [wilcox-adventurecycling-2022 C]; Sehili: „I crave salty food and nuts" [sehili-rawcycling-atlas C]; PH-dietetikus: az SSS (szenzoros-specifikus jóllakottság) mechanizmus, hivatkozott 2021-es vizsgálat szerint az első 60 percben édes, utána sós preferencia (*a vizsgálat nincs azonosítva*) [kelson-2023-ph-flavourfatigue C]; katonai adagoknál „Taste fatigue of sweets is common", a változatosság növeli a bevitelt [bakerfulco-1995-military-intake C].
8. **A meleg étel és a „leülős étkezés" morál- és bevitel-javító hatása versenyzői/edzői konszenzus, sportolói mérés nincs; a legközelebbi mért analóg a katonai terep: napi egy meleg étkezés növeli a tápanyagbevitelt.** Mäkipää/White: napi egy leülős étkezés táplálkozási és pszichés haszon; McDonald's = ismerős menü, gyors, forró, kalóriadús [white-ridefar-food C]; Hall „eat–sleep–eat" ciklus szállásnál [hall-bikepacking-2016 C]; Cyclite: „Warm meals at night aid digestion & comfort" [cyclite – nem vettük fel külön kulcsként, ld. GYENGE]; katonai: „Provision of at least one hot meal per day enhances nutrient intake" [bakerfulco-1995-military-intake C].
9. **A nagy kalóriadús boltos étkezés utáni azonnali tekerés és az ismeretlen termék a két tipikus GI-hiba.** Ridefar: az első energiaital 2 hét után 24 órára kidöntött egy versenyzőt; kalóriadús étel után azonnali tekerés = emésztési gond [white-ridefar-food C]; Strasser: semmi romlandó, semmi ismeretlen [strasser-cyclite-2025 C]; CTS/Hughes: „nothing new on race day" [rutberg-pulford-cts-ultra-2025 C; hughes-rbr-showstoppers-2019 C].
10. **A korai, magasabb bevitel a célba érés korrelátuma (futó-adat): célba érők 4,6 ± 1,7 vs. kiesők 2,5 ± 1,3 kcal/kg/h, CH 0,98 vs. 0,56 g/kg/h, Na 10,2 vs. 5,2 mg/kg/h, már az első 48 km-en.** [stuempfle-2011-ws100-diet B, n=16, *absztraktból*; 70 kg-ra 322 vs. 175 kcal/h saját számítás]. Kerékpáron ugyanez az irány: a magasabb energiabevitel rövidebb versenyidővel járt (p = 0,023) [black-2012-384km B].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q7)**
- Nincs mért (napló + kettős jelölt víz) adat arról, hogy önellátó bikepacking-versenyen MIT és MENNYIT esznek a versenyzők boltból; a lista kizárólag interjúkból áll (C). A meglévő kerékpáros mérések (geesmann, black, hulton, hyldahl, purcell) a bevitel mennyiségét adják, az élelmiszer-típust nem részletezik.
- „Ízfáradás" (flavour fatigue) ultra-állóképességi sportban: lektorált vizsgálatot nem találtam (keresés: „flavour fatigue ultra-endurance", „sensory-specific satiety prolonged exercise", „taste fatigue sweet ultramarathon"). A rendelkezésre álló laboradat (4×60 perc kerékpár, 20 nő) az édes ital preferenciájának NÖVEKEDÉSÉT mutatja [narukawa-2024-taste-cycling A] – lásd ELLENTMONDÁS.
- Meleg/hideg étel hatása a morálra sportolónál: nincs vizsgálat (keresés: „hot food morale ultra-endurance", „warm meal mood prolonged exercise"); csak katonai adagolási irodalom (C).
- Tápanyag-sűrűség (kcal/g) a tipikus boltos ételeknél: USDA FoodData Central és Open Food Facts lekérdezés a proxy (429/robots) miatt nem sikerült; a kalkulátor-blokk általános címkeadat, „nem ellenőrzött".
- Brevet-kontroll étkezésre csak régi, segítős PBP-tanács (Dickson, 2006) és edzői ökölszabály van; modern, mért kontroll-idő/bevitel adat nincs.
- Kolbinger, Bartholmoes, Gemperle, Allegaert étkezéséről közvetlen, idézhető forrást nem sikerült megnyitni (Casquette/Cyclist 403; ld. „Nem sikerült megnyitni"); Allegaert 3000 kcal/nap adata másodlagos (ridefar).

**ELLENTMONDÁS (Q7)**
- Felszívási plafon: ridefar/CTS/Hughes/LW 200–300 kcal/h [C] vs. kísérős RAAM 500–550 kcal/h folyékony protokoll [strasser-datasport-2019 C; barnett-2017-raam-toone B] és Strasser 24 órás 105–116 g CH/h (~420–460 kcal/h csak CH-ból) [strasser-inscyd-2022 B]. Feloldás: a 200–300 kcal/h a szilárd, boltos, önellátó (állva-evő) kontextus; folyékony, stáb-adagolt, alacsony intenzitású (RAAM ~150 W) formátumban tartósan magasabb tolerálható – de a mért RAAM-adatok (hulton váltó 4918 kcal/nap; fesseler szóló 21 169 kcal deficit) az önbevallott 12 000 kcal/nap alatt maradnak.
- Ízfáradás: versenyzői konszenzus (édes → sós váltás) vs. labor: 4 óra alatt az édes ital preferenciája nőtt [narukawa-2024-taste-cycling A]. Feloldás: a labor 4 óra, nem edzett nők, egyetlen ital; a versenyzői beszámolók 20–200 órás, monoton édes sportétel-terhelésről szólnak – a két adat nem ugyanazt méri.
- Leülős étkezés: Mäkipää/White (napi egy leülős étkezés) és Dickson (meleg étel kontrollon) vs. Sehili („I am not stopping for a comfortable meal, I eat on the bike") és Allegaert (8 nap alatt 9 h 38 perc összes megállás [allegaert-apidura-2016 C]). Amitől függ: helyezési cél (győzelem vs. befejezés), verseny hossza, ellátás sűrűsége.

**KALKULÁTOR-PARAMÉTEREK (Q7 – boltos ellátás)**
- Energiaigény: E_nap ≈ BMR × PAL, ultrán PAL 3,7–4,1 (30 napos kanadai átkelés, kettős jelölt víz) [purcell-2025-canada B]; RAAM-váltó 6420 kcal/nap forgalom [hulton-2010-raam-energy B]; tartós bevitel felső korlát ≈ 2,36 × BMR (≈ 4000–4500 kcal/nap 75 kg-os férfinál) [thurber-2019-alimentary A].
- Tervezhető bevitel: önellátó, szilárd: 200–300 kcal/h (tartomány 120–400) [white-ridefar-food C; rutberg-pulford-cts-ultra-2025 C; hughes-rbr-showstoppers-2019 C]; kísérős folyékony: 500 kcal/h [barnett-2017-raam-toone B; strasser-datasport-2019 C]; ISSN: 150–400 kcal/h, 30–50 g CH/h [tiller-2019-issn-ultra A]. Szénhidrát: mért ultra-terep 52–57 g/h [black-2012-384km B; geesmann-2014-1230km B], elit 24 h 105–116 g/h [strasser-inscyd-2022 B].
- Kalóriasűrűség (kcal/g) cipelendő ételekre: cél ≥ ~5,7 kcal/g (170 kcal/uncia); mogyoróvaj-pouch 5,9; mandula 5,9; Larabar 4,8; Pro Bar 4,6; Kind 5,1 [watts-2015-bikepacking-trailfood C, címkeadat]. Általános boltos ételek NAGYSÁGRENDJE (általános címkeadat, ebben a csomagban NEM ellenőrzött forrás – végleges szövegbe csak USDA/címke-ellenőrzés után): chips ~5,3; csokoládé/Snickers ~4,8–5,3; sós mogyoró ~6,0; Haribo ~3,4; keksz ~4,5–5,0; sajt ~3,5–4,0; fehér kenyér ~2,6; pizza/kebab ~2,3–2,7; fagylalt ~2,0; banán ~0,9; tej ~0,6; kóla ~0,42 kcal/g.
- Boltos megállás gyakorisága: F = E_bevitel_nap / (kcal cipelve egy vásárlásból); pl. 6000 kcal/nap, 1500 kcal/vásárlás → 4 bolt/nap; a nyitvatartás (mediterrán bolt 13–17 h zárva, este 19–20 h-ig nyit) és a „100 km-es élelem-sivatag" a korlát [white-ridefar-food C; dotwatcher-waypoints-2025 C]. Megállási költség: „óránként max 5 perc a nyeregből" [hughes-rbr-2015 C], kontroll <10 perc [dickson-rusa-pbp C], 24 h-nál 2×10–15 perc leülés [lwcoaching-2008-24h-solo C].
- Folyadék: 0,5 ± 0,2 l/h 24 órás MTB [chlibkova-2014-24h-mtb B]; 392 ± 85 ml/h 1230 km-en [geesmann-2014-1230km B]; 200–300 ml/h hideg – 1000+ ml/h hőség [blow-ph-ultra-2021 C]; 16 napos TCR: 5–11 l/nap [white-ridefar-food C, n=1].

---

## Q10 — Konvergencia: rutinos versenyzők, edzők, stábok gyakorlata

1. **Mennyiség: az edzői ökölszabályok 200–300 kcal/h és 60–90 g CH/h körül konvergálnak; a mért ultra-terep 52–57 g CH/h, az elit 24 h 105–116 g/h.** [rutberg-pulford-cts-ultra-2025 C; hughes-rbr-showstoppers-2019 C; blow-ph-ultra-2021 C; lwcoaching-2008-24h-solo C; black-2012-384km B; geesmann-2014-1230km B; strasser-inscyd-2022 B; tiller-2019-issn-ultra A].
2. **Ritmus: „minden órában", időzítővel, éhség előtt – a RAAM-stáb óránkénti palack-protokollja, a 24 h-s 1,3 étkezés/óra, a brevet „mielőtt éhes/szomjas vagy" ugyanaz az elv.** [strasser-cyclite-2025 C; chlibkova-2014-24h-mtb B; dickson-rusa-pbp C; hughes-rbr-showstoppers-2019 C; hayden-tcr6-story B – „if you're hungry, it's too late"].
3. **Front-loading: korán többet, mert a felszívás elöl a legjobb, nappal jobb, mint éjjel; a bevitel a rajt után a legmagasabb és éjjel/végén esik (mért).** [blow-ph-ultra-2021 C; chlibkova-2014-24h-mtb B; geesmann-2014-1230km B – a CH-bevitel 618 km után szignifikánsan csökkent; stuempfle-2011-ws100-diet B; towers-substack-2026 C – az első 24 órára gél/szelet magával].
4. **Hányinger kezelése: lassíts (bél-véráramlás), kortyolj vizet, kóla/Pepsi, savanyú/sós, folyékonyra váltás hőségben.** [rutberg-pulford-cts-ultra-2025 C; blow-ph-ultra-2021 C; lwcoaching-2008-24h-solo C; barnett-2017-raam-toone B; baloh-infinity-2020 C – görcsnél lassított, többet ivott, kivárta]. Mechanizmus: a felső GI-panasz korrelál a CH-bevitellel (r = 0,37–0,51), mégis a magasabb bevitel gyorsabb [pfeiffer-2012-gi-events B].
5. **Hasmenés/GI-katasztrófa megelőzése: semmi romlandó, semmi új, kevés rost, FODMAP-csökkentés opció, bél-edzés.** [strasser-cyclite-2025 C; barnett-2017-raam-toone B; blow-ph-ultra-2021 C; jeukendrup-2018-gssi-gut C; martinez-2023-guttraining-sr A].
6. **Ellátás útszakaszonként: POI-k (bolt, benzinkút, víz) a szintprofilra vetítve, benzinkút a leghatékonyabb, optimális boltméret, nyitvatartás, mindig tartalék étel.** [dotwatcher-waypoints-2025 C; towers-substack-2026 C; white-ridefar-food C; strasser-cyclite-2025 C; wilcox-adventurecycling-2022 C].
7. **Szakági különbség: kísérős RAAM = folyékony, stáb dönt („a csapat dönti el, mikor és mit egyen" [strasser-pez-2019 C]), 500 kcal/h; önellátó = boltos, szilárd, 200–300 kcal/h, sós fordulat; brevet = kontroll-étkezés + zsebétel; 24 h = box, banán/szelet/sajt, kóla, két leülős étkezés.** [barnett-2017-raam-toone B; strasser-datasport-2019 C; hayden-tcr6-story B; dickson-rusa-pbp C; chlibkova-2014-24h-mtb B; lwcoaching-2008-24h-solo C].
8. **A stáb átveszi a döntést, amikor a versenyző már nem tud a testére hallgatni (3–4. nap után).** [strasser-pez-2019 C; goldstein-cbc-2021 C – „egy ponton nem tudta, miért ül a biciklin"; baloh-nduranz-2024 C – 2–3 órás emelkedőn nem lehet enni, ezért előtte kell].

### KONVERGENCIA-MÁTRIX

| Téma | Egybevágó tapasztalat [kulcsok] | Eltérő gyakorlat [kulcsok] | Amitől függ |
|---|---|---|---|
| Óránkénti energia | 200–300 kcal/h önellátón/brevet-en/24 h-n [white-ridefar-food C; rutberg-pulford-cts-ultra-2025 C; hughes-rbr-showstoppers-2019 C; lwcoaching-2008-24h-solo C; tiller-2019-issn-ultra A] | Kísérős RAAM ≥500 kcal/h folyékonyan [barnett-2017-raam-toone B; strasser-datasport-2019 C]; Allegaert ~3000 kcal/nap (*másodlagos*) [white-ridefar-food C] | Formátum (stáb vs. bolt), szilárd vs. folyékony, intenzitás (RAAM ~150 W vs. 24 h 250–270 W), egyéni bél |
| Szénhidrát g/h | 60–90 g/h a kiindulás [blow-ph-ultra-2021 C; jeukendrup-2014-personalized A]; mért ultra-terep 52–57 g/h [black-2012-384km B; geesmann-2014-1230km B] | Strasser 24 h 105–116 g/h [strasser-inscyd-2022 B]; Towers 69 g/h 224 W-nál, 144 g/h 265 W-nál (egyéni modell) [towers-substack-2026 C]; 120 g/h nem bizonyítottan jobb 90-nél [wilson-2025-highcarb-review C] | Teljesítmény (W), verseny hossza, bél-edzettség, glükóz:fruktóz arány |
| Ritmus | Minden órában / 30–45 percenként, éhség előtt; időzítő [hughes-rbr-showstoppers-2019 C; strasser-cyclite-2025 C; chlibkova-2014-24h-mtb B; hayden-tcr6-story B] | Sehili: a biciklin eszik, nem áll meg [sehili-rawcycling-atlas C]; Mäkipää/Hall: napi egy leülős étkezés / eat–sleep–eat [white-ridefar-food C; hall-bikepacking-2016 C] | Helyezési cél, alvásstratégia (szállás vs. bivak), ellátás sűrűsége |
| Valódi étel vs. sportétel | Nagyon hosszú eseményen valódi étel kell (ízfáradás, éhség, morál) [blow-ph-ultra-2021 C; wilcox-adventurecycling-2022 C; kelson-2023-ph-flavourfatigue C]; szeletek/rizssütemény 3–4 óra után [rutberg-pulford-cts-ultra-2025 C] | Strasser RAAM: kizárólag folyékony táp, az első 3 napon „kényszer" [strasser-datasport-2019 C]; Toone: szilárd + folyékony vegyesen, hőségben folyékony [barnett-2017-raam-toone B] | Stáb megléte, hőség (folyékony), gyomor-tolerancia, verseny hossza |
| Sós/édes váltakozás | Az édes korán elfárad, sósat keresnek: chips, sajt, kenyér, dió [wilcox-adventurecycling-2022 C; sehili-rawcycling-atlas C; kelson-2023-ph-flavourfatigue C; bakerfulco-1995-military-intake C]; 24 h: sajt 43% + banán 87% [chlibkova-2014-24h-mtb B] | Labor: 4 óra alatt az édes ital preferenciája NŐTT [narukawa-2024-taste-cycling A]; Strasser: csoki és vanília íz végig „relish" [strasser-datasport-2019 C] | Időtartam (óra vs. nap), az ízkínálat monotonitása, egyéni preferencia |
| Meleg étel, leülős étkezés | Meleg étel/leülés = morál + bevitel [white-ridefar-food C; dickson-rusa-pbp C; lwcoaching-2008-24h-solo C; bakerfulco-1995-military-intake C] | Sehili/Allegaert: minimális megállás [sehili-rawcycling-atlas C; allegaert-apidura-2016 C] | Győzelmi cél vs. befejezés; hideg/eső (meleg étel értéke nő) |
| Hányinger | Lassíts, kortyolj vizet, kóla, folyékonyra váltás [rutberg-pulford-cts-ultra-2025 C; blow-ph-ultra-2021 C; lwcoaching-2008-24h-solo C; barnett-2017-raam-toone B] | Nincs ellentétes gyakorlat; a bevitel csökkentése vs. fenntartása (CTS: „calories are king") | Intenzitás, hőség, a hányinger oka (túletetés vs. alvásmegvonás vs. hő) |
| Hasmenés / GI-biztonság | Semmi romlandó, semmi új, kevés rost [strasser-cyclite-2025 C; barnett-2017-raam-toone B; hughes-rbr-showstoppers-2019 C]; bél-edzés edzésen [jeukendrup-2018-gssi-gut C; martinez-2023-guttraining-sr A] | Hayden/Wilcox: bármi, ami elérhető (McDonald's, hot dog, kebab) [hayden-tcr6-story B; wilcox-adventurecycling-2022 C]; FODMAP-csökkentés csak egyeseknek [blow-ph-ultra-2021 C] | Egyéni GI-előzmény (a tünetesek étvágya is csökken [martinez-2025-gutchallenge B]), a régió élelmiszer-biztonsága |
| Folyadék és nátrium | Szomj szerint + tudatos alap; 0,4–0,5 l/h mért [geesmann-2014-1230km B; chlibkova-2014-24h-mtb B]; Na ~500 mg/h átlag [rutberg-pulford-cts-ultra-2025 C] | Na 200–1500 mg/h egyénileg [blow-ph-ultra-2021 C]; Strasser akár 1 l/h [strasser-datasport-2019 C]; „csak szomj szerint" [hughes-rbr-showstoppers-2019 C] | Hőmérséklet, izzadás-Na (12,6–104,8 mmol/l tartomány [baker-2016-sweat-normative B]), stáb (mérhet) vs. bolt |
| Ellátás tervezése | POI-k szakaszonként, benzinkút, nyitvatartás, tartalék étel [dotwatcher-waypoints-2025 C; towers-substack-2026 C; white-ridefar-food C; strasser-cyclite-2025 C] | RAAM-stáb: nincs bolt, a követőautó a bolt [barnett-2017-raam-toone B]; brevet: kontroll-menza [dickson-rusa-pbp C] | Szakág; a régió boltsűrűsége (Marokkó: falvanként egy édességes bolt [sehili-rawcycling-atlas C]) |
| Döntéshozó | Az első napokban a versenyző, később a stáb/terv [strasser-pez-2019 C; goldstein-cbc-2021 C; pearson-ebr-2024 C (alvástervre)] | Önellátón nincs stáb: időzítő, előre írt terv [towers-substack-2026 C; bikepacking-ultraguide-2019 C] | Alvásdeficit mértéke, formátum |
| Koffein/kóla mint „üzemanyag" | Kóla/Pepsi és koffein éjjel, gyomorra is [hayden-tcr6-story B; lwcoaching-2008-24h-solo C; chlibkova-2014-24h-mtb B (kóla 54%); towers-substack-2026 C] | Sehili hétköznap koffeinmentes, hogy versenyen hasson [sehili-breakaway C] | Alvásstratégia, egyéni tolerancia |

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q10)**
- A konvergencia szinte teljes egészében C-fokozatú (edzői/versenyzői), az egyetlen B-szintű „gyakorlat"-adat a 74 fős 24 órás MTB-felmérés [chlibkova-2014-24h-mtb] és a Toone-stáb esettanulmánya.
- Nincs vizsgálat, amely önellátó bikepacking-versenyen összevetné a különböző etetési stratégiák (folyékony vs. boltos, sűrű kis vs. ritka nagy étkezés) teljesítményhatását.
- A „stáb dönt" protokollra (mikor veszi át a stáb a döntést, milyen jelek alapján) nincs írott, ellenőrizhető RAAM-stábkézikönyv a megnyitott forrásokban; Strasser és Goldstein interjú-szintű.
- Precision Hydration/Fuel és CTS anyagai gyártói/szolgáltatói érdekkel bírnak (elektrolit-termék, edzés-szolgáltatás).

**ELLENTMONDÁS (Q10)**
- „Csak szomj szerint" [hughes-rbr-showstoppers-2019 C] vs. „tervezett folyadék + nátrium, szomjjal kiegészítve" [blow-ph-ultra-2021 C; rutberg-pulford-cts-ultra-2025 C]. Mért terep: a folyadékbevitel és a sebesség között nincs összefüggés 24 órás MTB-n [chlibkova-2014-24h-mtb B]; az egyénre szabott Na-pótlás 5 órán nem javította a vízháztartást [mccubbin-2024-sodium-personalized A].
- „Több szénhidrát = gyorsabb, de több hányinger" [pfeiffer-2012-gi-events B] – ugyanaz az intézkedés két ellentétes hatással; a feloldás a bél-edzés [martinez-2023-guttraining-sr A: malabszorpció -45–54%].

**KALKULÁTOR-PARAMÉTEREK (Q10 – napi/útszakasz-terv)**
- Napi bevitel-cél: E_cél = óra_nyeregben × kcal/h_formátum + pihenő-étkezések; kcal/h_formátum = 200–300 (önellátó/brevet/24 h), 500 (kísérős folyékony). Ellenőrzés: E_cél ≤ 2,36 × BMR tartósan [thurber-2019-alimentary A] – e fölött a deficit raktárból megy.
- Szénhidrát-cél: 60–90 g/h alap; 90 g/h-ig glükóz:fruktóz ~2:1 [jeukendrup-2014-personalized A; towers-substack-2026 C]; >90 g/h csak bél-edzéssel és egyéni oxidációs mérés után [wilson-2025-highcarb-review C].
- Nátrium: alap 500 mg/h [rutberg-pulford-cts-ultra-2025 C], tartomány 200–1500 mg/h [blow-ph-ultra-2021 C]; egyéni Na-veszteség = izzadásráta (l/h) × izzadás-Na (mmol/l) × 23 mg/mmol; normatíva 43,6 ± 18,2 mmol/l és 1,21 ± 0,68 l/h [baker-2016-sweat-normative B].
- Bél-edzés: heti 1 magas CH-bevitelű edzés, 6–10 hét [jeukendrup-2018-gssi-gut C]; 2 hetes napi protokoll: malabszorpció -45–54%, bélkellemetlenség -26–47% [martinez-2023-guttraining-sr A].

---

## Q11 — Feltörekvő irányok

1. **CGM ultrán: a glükóz a nyeregben alacsonyabb, mint pihenőben (RAW-váltó: 91 ± 23 vs. 115 ± 25 mg/dl; TBR 9,15% vs. 1,23%), és szólóban napról napra csökken (RAAM: -0,92 mg/dl/nap).** [skroce-2026-cgm-records B; fesseler-2026-raam58 B].
2. **A CGM-érték ultrán nem „üzemanyagszint": futó-ultrán a glükóz a rajttól a célig 104 → 164 mg/dl-re NŐTT (stressz-hormonális), miközben a bevitel 16–53 g CH/h volt; a szakaszonkénti glükóz mégis korrelált a sebességgel.** [ishihara-2020-cgm-ultra B; ishihara-2026-glucose-phases C – háromfázisú modell, >50% nem eszik 30 g/h fölött].
3. **Szenzorpontosság edzés alatt elfogadható, de gyengébb (MARD <15%), időkéséssel; a CGM nem méri az izomglikogént; a „magasabb glükóz = jobb teljesítmény" állításra nincs bizonyíték; a vezető áttekintés szerint egészséges sportolónál a használat robusztus élettani indoka hiányzik.** [riddell-2025-gssi-cgm C; helleputte-2025-cgm-review C]. Normál napi ingadozás elit sportolónál: MAGE 36 ± 5, MODD 12,6 ± 1,8 mg/dl [bowler-2024-cgm-variability A]; a diéta GI-je a 24 órás átlagot nem változtatja (102 vs. 100 mg/dl) [hamilton-2025-gi-cgm A].
4. **Ketonészter: akut ergogén hatás nincs (8 RCT, n=80, g = 0,136; 95% CI -0,195–0,467), a GI-panasz gyakoribb; a krónikus „regenerációs" hatás (EPO +26% 3 hetes blokkban) nyitott kérdés; dózis 300–800 mg/kg.** [brooks-2022-ketone-meta A; sitko-2024-ketones-cycling C].
5. **120+ g/h: nincs egyértelmű bizonyíték, hogy 100–120 g/h a 60–90 g/h-nál jobb (King 2018: 90 g/h ~5%-kal jobb, n.s.; Viribay n=6–7/csoport); a valószínű haszon többnapos formátumban a napi összbevitel/glikogén-visszatöltés.** [wilson-2025-highcarb-review C; podlogar-2022-newhorizons A].
6. **Hidrogél: ≤70 g/h-nál nincs többlet, ≥90–180 g/h-nál következetesen magas exogén oxidáció; a teljesítményvizsgálatok többsége negatív; GI-tünet csökken vagy változatlan (főleg futásnál).** [li-2026-hydrogel-review A, 9 vizsgálat].
7. **Egyénre szabott nátrium: az izzadás-Na 12,6–104,8 mmol/l között szór (n=506), de az izzadásteszt-alapú 100%-os pótlás 5 órás, 30 °C-os ultrafutáson nem változtatta a folyadékegyensúlyt és hőterhelést (n=9, RCT) – csak a plazma-Na-t emelte.** [baker-2016-sweat-normative B; mccubbin-2024-sodium-personalized A].
8. **Probiotikum/bélflóra: a kiegészítők összhatása a GI-tünetekre n.s. (g = 0,42; p = 0,15); a probiotikum-alcsoport határértékű (g = -0,62; p = 0,05); teljesítményre semmi (p = 0,53); a terhelés az I-FABP-t +106%-kal emeli.** [aitkenhead-2025-supplements-gut A, 26 vizsgálat, n=495].
9. **Gut training: 2 hetes ismételt terhelés alatti etetéssel a CH-malabszorpció -45–54%, a bélkellemetlenség -26–47%; gyomorürülés és permeabilitás nem változik; ajánlás heti 1 magas CH-edzés 6–10 hétig.** [martinez-2023-guttraining-sr A; jeukendrup-2018-gssi-gut C]. A GI-tünetesek étvágya terhelés alatt alacsonyabb – korai jel [martinez-2025-gutchallenge B].
10. **AI-etetéstervezők: gyártói közlés, validáció nélkül (Fuelin „Smart Meals"); a lektorált ML-modell (evezés, 231 próba, szintetikus adatbővítés) R² = 0,53 és túlillesztett.** [endurancebiz-2025-fuelin-ai D; wang-2025-ml-supplement D].

**GYENGE / HIÁNYZÓ BIZONYÍTÉK (Q11)**
- Nincs RCT, amely CGM-vezérelt etetést hasonlítana össze terv-alapú etetéssel ultrán (keresés: „CGM-guided fueling randomized", „Supersapiens performance trial"). Supersapiens-specifikus vizsgálatot 2021–2026-ból nem találtam; a Skroce 2026 eset-sorozat Abbott Libre Sense (a Supersapiens szenzora) – gyártói kapcsolat lehetséges.
- Ketonészter többnapos ultrán (alvás, morál, regeneráció) – nincs adat; csak 1–3 hetes edzésblokk-vizsgálatok másodlagos idézése.
- 120 g/h és hidrogél ≥6 órás vagy többnapos protokollon – nincs vizsgálat; minden adat ≤3 órás labor.
- Izzadásteszt-alapú Na-terv kerékpáron és többnapos hőségben – nincs vizsgálat (a McCubbin RCT futás, 5 h).
- Probiotikum/„bélflóra-optimalizálás" ultrakerékpáron – semmi; a meta-analízis rövid laborterhelésekből áll.
- Gut training 2024–2026: az új adatok keresztmetszetiek (Martinez 2025), a 2 hetes protokoll (Costa 2017) régi; többnapos versenyre nincs.
- AI-tervezők: nulla lektorált validáció ultrakerékpárra.

**ELLENTMONDÁS (Q11)**
- CGM: Ishihara (glükóz ↔ sebesség pozitív korreláció, „practical to guarantee optimal carbohydrate intake") [ishihara-2020-cgm-ultra B] vs. Helleputte/Podlogar/Gonzalez (nincs bizonyíték, hogy konkrét glükózérték teljesítményt jósol; robusztus indok hiányzik) [helleputte-2025-cgm-review C] és Riddell („anecdotally… lack scientific evidence") [riddell-2025-gssi-cgm C]. Feloldás: korreláció ≠ vezérlőjel; a késői stressz-hiperglikémia [ishihara-2026-glucose-phases C] miatt a magas érték félrevezethet.
- Nátrium: a nagy egyéni szórás (Baker) az egyénre szabás érve, de az egyetlen RCT (McCubbin) nem talált élettani előnyt – a személyre szabott Na-terv ma inkább biztonsági (hyponatraemia-elkerülés), mint teljesítmény-eszköz.
- 120 g/h: a profi peloton gyakorlata (≥100 g/h) vs. a kísérletes bizonyíték hiánya [wilson-2025-highcarb-review C].

---

## Feltörekvő irányok (összefoglalva)
- CGM mint trend- és hipoglikémia-jelző szólóultrán (napi lecsengés, éjszakai TBR), nem mint etetés-vezérlő; szükséges: CGM-vezérelt vs. terv-alapú etetés RCT; multi-metabolit szenzorok [helleputte-2025-cgm-review; skroce-2026-cgm-records; fesseler-2026-raam58].
- Késői stressz-hiperglikémia ultrán (Ishihara 3. fázis) – kerékpáron nem vizsgált.
- Ketonészter mint alvás/regeneráció-modulátor többnapos formátumban – csak hipotézis (EPO-adat 3 hetes edzésből).
- ≥100 g/h + hidrogél többnapos glikogén-visszatöltésre (nem akut teljesítményre) – a Wilson-review hipotézise.
- Egyéni exogén-oxidációs mérés (13C) a CH-cél személyre szabására [wilson-2025-highcarb-review].
- Izzadásteszt: a Na-terv biztonsági eszköz; hordozható izzadás-szenzorok validációja folyamatban (nem nyitottuk meg).
- Probiotikum: legfeljebb GI-tünet-mérséklő; bélflóra–teljesítmény kapcsolat ultrán nem vizsgált.
- AI/ML etetéstervezők: kereskedelmi, validálatlan; a tudományos alap R² ~0,5-ös prediktív modell.

## Nem sikerült megnyitni
- link.springer.com (Helleputte 2025 teljes szöveg és PDF; Martinez 2023 SR teljes szöveg; SpringerPlus Chlíbková 2014) – HTTP 429 rate limit; helyette Crossref/OpenAlex/academia.edu-tükör.
- onlinelibrary.wiley.com (Hamilton 2025) – 403; helyette OpenAlex.
- journals.humankinetics.com (McCubbin 2024 teljes) – 403; helyette Crossref + OpenAlex.
- tandfonline.com (Narukawa 2024; Baker 2016) – 403; helyette OpenAlex (absztrakt részben parafrázis).
- pubmed / pmc.ncbi.nlm.nih.gov – üres oldal / reCAPTCHA.
- ebi.ac.uk Europe PMC REST, api.openalex.org (search endpoint), researchgate.net – 429.
- api.nal.usda.gov (FoodData Central) – 429; world.openfoodfacts.org – robots.txt tiltás (kalóriasűrűség-értékek ezért nem ellenőrzöttek).
- facebook.com (Strasser RAAM-táplálkozási poszt) – robots.txt tiltás; helyette Datasport- és Cyclite-interjú.
- casquette.co.uk, cyclist.co.uk (Kolbinger-interjúk) – 403.
- ridefar.info/rider/nutrition/ – 404 (a helyes oldal: /rider/strategy/food/, megnyitva).
