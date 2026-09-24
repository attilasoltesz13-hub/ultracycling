# Kísérőoldal (statikus)

Ugyanabból a modul-Markdownból készül, mint a PDF (`build/render.py` értelmezője), `build/site.py` írja a `dist/site/` mappába.

    python3 build/site.py                # minden: content/hu/04-alvas.md → dist/site/
    open dist/site/index.html            # file:// alól is működik, szerver nem kell

Részek:

- `web.css` — webes stíluslap a közös tokenekre (`design/tokens/tokens.css`) építve; a jelek (bizonyíték-ikon, fix/példa/egyéni) ugyanazok, mint a PDF-ben.
- `js/site.js` — tartalomjegyzék-kiemelés, szintszűrő (alap/haladó/elit), `localStorage` segéd.
- `js/kviz.js` — önellenőrző kvíz; kérdések: `data/quiz/<modul>.yaml` (a build keveri a válaszokat, determinisztikusan).
- `js/alvasterv.js` + `templates/alvasterv.html` — alvásterv-kalkulátor és a 12. oldal sablonja; paraméterek: `data/tools/alvasterv.yaml`.
- `js/kronotipus.js` + `templates/kronotipus.html` — rMEQ-alapú kronotípus-kérdőív (forrás: `adan-1991-rmeq`).
- `js/idokoltsegvetes.js` + `templates/idokoltsegvetes.html` — időköltségvetés-kalkulátor (08); paraméterek: `data/tools/idokoltsegvetes.yaml`.
- `js/etetesiterv.js` + `templates/etetesiterv.html` — etetési és hidratálási terv (03): energia · folyadék és nátrium · koffein, a 16. oldal sablonja; paraméterek: `data/tools/etetesiterv.yaml`.
- `js/terheles.js` + `templates/terheles.html` — terhelés-kalkulátor (02): zónaórák → TSS/sRPE, CTL-szimuláció, fáradt-teljesítmény kiértékelő; paraméterek: `data/tools/terheles.yaml`.
- `js/utemterv.js` + `templates/utemterv.html` — felkészülési ütemterv-generátor (02): fázisok visszafelé a versenydátumtól, brevet-lépcső, hőblokk; paraméterek: `data/tools/utemterv.yaml`.

Adat csak a böngészőben marad (`localStorage`: `ht.level`, `ht.kviz.<modul>`, `ht.kronotipus`, `ht.alvasterv`, `ht.idokoltsegvetes`, `ht.etetesiterv`, `ht.terheles`, `ht.utemterv`, `ht.sablon.<modul>`). Külső függőség, betöltés hálózatról nincs; a betűk a `dist/site/assets/fonts` mappából jönnek.

GitHub Pages: a `dist/site/` tartalma tehető a `gh-pages` ágra vagy egy Actions-lépés futtathatja a buildet (`.nojekyll` benne van).

## GitHub Pages

`.github/workflows/pages.yml`: minden `main`-re érkező push után a workflow lefuttatja a `build/site.py`-t és a `dist/site` mappát teszi közzé. Egyszeri beállítás a GitHubon: Settings → Pages → Source: **GitHub Actions**. Publikus repónál ingyenes.
