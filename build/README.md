# Build

```
pip install playwright pyyaml markdown && playwright install chromium
python3 figures/src/fig04.py                       # ábrák → figures/svg/
python3 build/render.py content/hu/04-alvas.md     # → dist/04-alvas.html + .pdf (--draft: „Vázlat” címke; --html-only)
```

`render.py` a `design/styleguide.md` 7. pontja szerinti direktívákat dolgozza fel, a hivatkozásokat a `data/sources.yaml`-ből sorszámozza, a forrásjegyzéket automatikusan lapozza, és minden oldalon ellenőrzi a túlcsordulást (szükség esetén `compact` → `compact2` → `compact3` sűrítés; a jelentés a kimeneten). A `build/samples/` a pilot 0. lépésének mintaoldalait tartalmazza.
