# Stílusguide — Hosszú távon

Verzió 0.2 (2026-09-18). A tokenek gépi forrása: `tokens/tokens.json` és `tokens/tokens.css`. PDF-motor: HTML + CSS → Chromium print (döntés 2026-09-18), így a PDF és a weboldal ugyanazokat a tokeneket és komponenseket használja. Ez a dokumentum a szabályokat és a szándékot rögzíti; az értékeket a tokenfájlok.

## 1. Alapelv

Az anyag tanítási stílusa két könyvtípus ötvözete: **interaktív-vizuális** (ábra és feladat tanít, nem a folyószöveg) és **gyakorlati-útmutató** (minden tudás cselekvésre fordítva). Ebből három tervezési szabály következik.

1. **Egy oldal, egy gondolat.** Minden oldal egy állítást, egy mechanizmust vagy egy eljárást hordoz; a cím maga az állítás, nem téma-megnevezés („A második éjszaka a fordulópont”, nem „Alvásmegvonás”).
2. **Minden oldalon vizuális horgony.** Ábra, diagram, séma, táblázat vagy nagy szám; folyószöveg legfeljebb 90–120 szó oldalanként.
3. **Minden ábra mellett „mit jelent neked” doboz.** A tudás közvetlen következménye: mit mérj, mit állíts be, mit csinálj másképp a következő edzésen.

## 2. Vizuális nyelv

Adatvizualizációs stílus: sok fehér tér, egy márkaszín (éjszakai kék) és egy kiemelő szín (hajnal-narancs), recesszív rács és tengelyek, vékony vonalak. Semmi dekoráció, ami nem hordoz információt. A képek (saját és szabad felhasználású fotók) hangulati és példa-szerepben jelennek meg, teljes szélességű sávként vagy oldalsávban, sosem szöveg mögött.

**Paletta.** Felület `#fcfcfb`, tinta `#0b0b0b`, márka `#184f95`, mély kék `#0d366b`, kiemelő `#eb6834`. A diagram-sorozatok rögzített sorrendű, validált kategorikus palettát használnak (tokens: `series`); szekvenciális skálához egyhangú kék ramp; divergálóhoz kék–szürke–piros. Státuszszínek (jó / figyelem / komoly / kritikus) csak biztonsági küszöbökhöz, mindig ikon és felirat mellett.

**Tipográfia.** Inter (szöveg), Inter Display (címek) és IBM Plex Mono (számok, kód) — mind OFL-licencű, a `fonts/` alatt vendorozva. Döntés 2026-09-18, a mintaoldalak alapján (a másik jelölt az IBM Plex Sans volt). Számok táblázatban és tengelyen `tabular-nums`, hero számoknál proporcionális. Betűméret-skála: display 34 pt, H1 24 pt, H2 16 pt, szöveg 10,5 pt, kis szöveg 8,5 pt, képaláírás 7,5 pt, hero szám 56 pt.

**Oldal.** Álló A4, margók 16 / 16 / 18 / 16 mm, 6 oszlopos rács 4 mm hézaggal, bal oldalsáv 8 mm a szint- és szakág-ikonoknak. Lábléc: modulszám · modulcím · oldalszám. Címlapon verzió és dátum.

## 3. Jelrendszer

**Bizonyíték-fokozat.** Nem betűjel, hanem négysávos jelerősség-ikon az állítás mellett: 4 kitöltött sáv = RCT / meta-analízis (A, `#0d366b`), 3 = terepvizsgálat, megfigyelés (B, `#256abf`), 2 = szakmai (edzői / versenyzői) konszenzus (C, `#5598e7`), 1 = feltörekvő, nem validált (D, `#86b6ef`, a sávok szaggatott kerettel). A kitöltött sávok száma hordozza a jelentést, a szín csak támogat, így fekete-fehérben is olvasható. Minden oldal láblécében jelmagyarázat; a forrásjegyzékben a betűjel (A–D) marad a hivatkozások mellett.

**Sablonelemek.** Három jel, a keret és az ikon hordozza a jelentést, a szín másodlagos:

| Jel | Jelentés | Megjelenés |
| --- | --- | --- |
| fix | bizonyítékok alapján általánosan érvényes | tömör kék keret, tű-ikon + szó |
| példa | szemléltető érték, nem előírás | szaggatott szürke keret, ceruza-ikon + szó |
| egyéni | csak saját teszttel beállítható | narancs keret, személy-ikon + szó |

**Szint és szakág.** Oldalsáv-ikonok: Alap / Haladó / Elit (egy, két, három vonal); önellátó (táska), kísérős (autó), brevet (bélyegző), 24h (óra). Az oldal csak azokat mutatja, amelyekre az adott tartalom vonatkozik.

**QR-kód.** Ott, ahol a kísérőoldalon interaktív változat (kalkulátor, teszt) van; a lábléc fölött, 14 mm, rövid felirattal.

## 4. Oldaltípusok

Nyolc ismétlődő sablon; egy modul ezekből épül: modulnyitó → fogalom- és adat-oldalak → konvergencia-oldal → protokoll- és sablon-oldalak → feladat-oldal → összefoglaló. A pilotban három készül el mintaként: fogalom, adat, protokoll.

| Oldaltípus | Rács | Kötelező elemek |
| --- | --- | --- |
| Modulnyitó | teljes oldal, mély kék mező | modulszám, cím, 3–5 tanulási cél, szint, szakág, időigény |
| Fogalom | 4 + 2 oszlop | ábra vagy séma, 3–6 mondat, bizonyíték-jel, „mit jelent neked” doboz |
| Adat | 6 oszlop diagram, alatta 3 + 3 | egy diagram, forrás és fokozat, kulcsszám, „mit jelent neked” |
| Konvergencia | mátrix | egybevágó / eltérő tapasztalatok, egyéni tényezők oszlopa |
| Protokoll | 6 oszlop lépéslista | számozott lépések, fix / példa / egyéni jelek, döntési fa vagy időszalag |
| Sablon | táblázat | kitölthető mezők, jelölések, QR a webes változathoz |
| Feladat | 3 + 3 | mérési utasítás, kérdések, eredmény helye |
| Összefoglaló | 2 × 3 kártya | kulcsállítások fokozattal, számok, QR |

## 5. Diagramok

A dataviz-szabályok kötelezőek: egy tengely (soha dupla y-tengely), vékony jelek, recesszív rács, legenda 2+ sorozatnál és közvetlen felirat legfeljebb 4-nél, szín sosem hordoz egyedül jelentést. Sorozatszínek rögzített sorrendben; szekvenciális = egy hue világostól sötétig; státuszszínek csak küszöbökhöz. Minden diagram forrása a `figures/src/` alatt, kimenet SVG a `figures/svg/` alatt; a PDF és a web ugyanazt az SVG-t használja.

## 6. Nyelv és hang

Tegeződő, közvetlen, pontos. Rövid mondatok, számok mértékegységgel. Szakkifejezés első előfordulásakor zárójelben az angol megfelelő. Nincs motivációs töltelék; a „mit jelent neked” doboz mindig felszólító módban kezdődik (Mérd, Állítsd, Tervezd, Kerüld).
