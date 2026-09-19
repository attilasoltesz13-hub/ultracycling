#!/usr/bin/env python3
"""Kísérőoldal (statikus) — ugyanabból a modul-Markdownból, mint a PDF (build/render.py értelmezője).

Használat:  python3 build/site.py [content/hu/04-alvas.md ...]
Kimenet:    dist/site/  (index.html, hu/<modul>/, hu/eszkozok/<eszköz>/, assets/)
            file:// alól is működik: nincs fetch, minden adat a lapba írva; külső függőség nincs.
"""
import re, sys, json, html, random, shutil
from pathlib import Path
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import Module, SOURCES, ev_svg, tag_html, level_svg, DISC_ICONS, ICONS, GRADE_LABEL, LEVEL_HU, TYPE_HU, ROOT  # noqa: E402

OUT = ROOT / "dist/site"
WEB = ROOT / "web"
SITE_TITLE = "Hosszú távon"
DISC_HU = {"onellato": "önellátó", "kiseros": "kísérős", "brevet": "brevet", "24h": "24 órás"}
# eszközök: (kulcs, cím, leírás, modul, adatfájl a data/tools alatt vagy None)
TOOLS = [("alvasterv", "Alvásterv-kalkulátor", "Rajtidőből a 17. és 24. ébrenléti óra, mélypont, éjszakai blokkok, mozgáshányad; a 04 modul sablonja kitölthetően.", "04", "alvasterv.yaml"),
         ("kronotipus", "Kronotípus-kérdőív", "Öt kérdés (rMEQ-alapú): korai, köztes vagy késői típus — a kalkulátor ebből tolja el a mélypontot.", "04", None),
         ("idokoltsegvetes", "Időköltségvetés-kalkulátor", "Táv, sebesség, alvás, álló idő → napok és a három kar; fizikai réteg (CdA, Crr, lejtés, szél, magasság); a 08 modul versenyterv-sablonja.", "08", "idokoltsegvetes.yaml")]
MODULES_NAV = [("04-alvas", "04 · Alvás"), ("08-pacing", "08 · Pacing")]


def shell(title, body, rel, nav_on="", extra_head="", scripts=()):
    nav = [("index.html", "Kezdőlap", "home")] + [(f"hu/{slug}/", t, slug[:2]) for slug, t in MODULES_NAV] + [("index.html#eszkozok", "Eszközök", "tools")]
    navh = "".join(f'<a href="{rel}{h}"{" class=on" if k == nav_on else ""}>{t}</a>' for h, t, k in nav)
    sc = "".join(f'<script src="{rel}assets/{s}"></script>' for s in scripts)
    return (f'<!DOCTYPE html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{html.escape(title)} · {SITE_TITLE}</title><link rel="stylesheet" href="{rel}assets/tokens.css"><link rel="stylesheet" href="{rel}assets/web.css">{extra_head}</head>'
            f'<body><header class="site-head"><div class="in"><a class="brand" href="{rel}index.html">{SITE_TITLE}<small>Az ultrakerékpározás tudománya és gyakorlata · vázlat v0.1</small></a><nav>{navh}</nav></div></header>'
            f'{body}<footer class="site-foot"><div class="in">Hosszú távon · kísérőoldal, vázlat v0.1 · A tartalom oktatási célú, nem helyettesíti az orvosi tanácsot; közúton a KRESZ és a zéró tolerancia érvényes. '
            f'A böngésző csak a saját gépeden tárol adatot (kvíz, kérdőív, sablon); szerverre semmi nem megy.</div></footer>{sc}</body></html>')


class WebModule(Module):
    """A PDF-értelmezőre épülő webes kimenet: szakaszok, linkelt hivatkozások, oldalszám-hivatkozások horgonyként."""

    def __init__(self, path):
        super().__init__(path)
        self.pages = [(b[1], b[2]) for b in self.parse_blocks(self.body) if b[0] == "page"]
        for _, body in self.pages:
            self.inline(body)  # hivatkozás-sorrend, mint a PDF-ben
        self.titles = []

    def post(self, h):
        h = re.sub(r'<sup class="cite">([\d, ]+)</sup>',
                   lambda m: '<sup class="cite">' + ", ".join(f'<a href="#ref-{n.strip()}">{n.strip()}</a>' for n in m.group(1).split(",")) + "</sup>", h)
        h = re.sub(r"(?<![\w\-])(\d{1,2})\. oldal", lambda m: f'<a class="pref" href="#p-{int(m.group(1)):02d}">{m.group(1)}. oldal</a>', h)
        h = re.sub(r"(\d{1,2})\. oldali", lambda m: f'<a class="pref" href="#p-{int(m.group(1)):02d}">{m.group(1)}. oldali</a>', h)
        h = h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
        return h

    def section(self, attrs, body, idx, quiz_html=""):
        a = dict(re.findall(r"(\w+)=(\S+)", attrs))
        ptype, level, disc = a.get("type", "fogalom"), a.get("level", "alap"), a.get("disc", "all")
        discs = list(DISC_ICONS) if disc == "all" else disc.split(",")
        parts, title = [], ""
        for b in self.parse_blocks(body):
            if b[0] == "md":
                h = self.md(b[1])
                if not title:
                    m = re.search(r"<h[12]>(.*?)</h[12]>", h, re.S)
                    if m:
                        title = m.group(1); h = h.replace(m.group(0), "", 1)
                        if ptype != "forrasok":
                            h = re.sub(r"^\s*<p>(.*?)</p>", r'<p class="lede">\1</p>', h, count=1, flags=re.S)
                parts.append(h)
            elif b[0] == "figure":
                parts.append(self.figure_html(b[1]))
            elif b[0] == "you":
                parts.append(f'<div class="box you"><h3>Mit jelent neked</h3>{self.md(b[2])}</div>')
            elif b[0] == "protocol":
                parts.append(self.protocol_html(b[2]))
            elif b[0] == "references":
                parts.append(self.references_web())
        self.titles.append((idx, title, level, ptype))
        content = self.post("\n".join(parts))
        if ptype == "feladat" and quiz_html:
            content += quiz_html
        if ptype == "osszefoglalo":
            mine = [t for t in TOOLS if t[3] == self.meta["id"]]
            links = " · ".join(f'<a href="../eszkozok/{k}/">{t}</a>' for k, t, *_ in mine) + ' · <a href="#quiz">önellenőrző kvíz</a>'
            content = re.sub(r"<p>QR → kísérőoldal: .*?</p>", f'<p><b>Eszközök:</b> {links}.</p>', content, flags=re.S)
        mod = self.meta["id"]
        if ptype == "modulnyito":
            return (f'<section class="hero" id="p-{idx:02d}"><div class="wrap"><div class="modnum">{mod}</div><div class="kicker">{SITE_TITLE} · {mod}. modul</div>'
                    f'<h1>{title}</h1>{content}</div></section>')
        kicker = (f'<div class="kicker"><span class="n">{mod} – {idx:02d}</span><b>{TYPE_HU.get(ptype, ptype)}</b><span class="lvl" title="szint">{level_svg(level)} {LEVEL_HU.get(level, level)}</span>'
                  f'<span class="disc" title="{", ".join(DISC_HU.get(d, d) for d in discs)}">{"".join(DISC_ICONS[d] for d in discs if d in DISC_ICONS)}</span></div>')
        return f'<section class="pg {ptype}" id="p-{idx:02d}" data-level="{level}" data-type="{ptype}">{kicker}<h2>{title}</h2>{content}</section>'

    def references_web(self):
        rows = []
        for i, k in enumerate(self.cite_order, 1):
            s = SOURCES[k]
            au = s.get("authors") or []
            au = ", ".join(a for a in au[:3] if a) + (" et al." if len(au) > 3 else "")
            cred = f" — {html.escape(s['credential'])}" if s.get("credential") else ""
            venue = html.escape(str(s.get("venue") or ""))
            link = ""
            if s.get("doi"):
                link = f' <a href="https://doi.org/{s["doi"]}" rel="noopener">doi:{s["doi"]}</a>'
            elif s.get("url"):
                link = f' <a href="{html.escape(s["url"])}" rel="noopener">link</a>'
            rows.append(f'<div class="ref" id="ref-{i}"><b>{i}.</b> {html.escape(au)} ({s.get("year")}). {html.escape(str(s.get("title")))}. <i>{venue}</i>.{link}{cred} '
                        f'{ev_svg(s["grade"])} <span class="key">{k}</span></div>')
        return f'<div class="refs">{"".join(rows)}</div>'

    def legend(self):
        evs = "".join(f"<span>{ev_svg(g)} {GRADE_LABEL[g]}</span>" for g in "ABCD")
        tags = "".join(tag_html(k) for k in ("fix", "példa", "egyéni"))
        return f'<div class="legend"><span>Bizonyíték:</span>{evs}<span style="margin-left:auto">Sablon:</span>{tags}</div>'

    def render_site(self, quiz):
        quiz_html = ""
        if quiz:
            quiz_html = ('<h3 id="quiz-h">Ellenőrizd magad — interaktív változat</h3><div class="quiz" id="quiz"></div>')
        secs = [self.section(a, b, i + 1, quiz_html) for i, (a, b) in enumerate(self.pages)]
        hero, rest = secs[0], secs[1:]
        if not any('class="refs"' in x for x in secs):
            rest.append(f'<section class="pg forrasok" id="p-forrasok" data-level="alap" data-type="forrasok"><div class="kicker"><span class="n">{self.meta["id"]} – források</span><b>Források</b></div>'
                        f'<h2>A modul {len(self.cite_order)} forrása</h2><p class="lede">Számozás a szövegbeli felső indexek szerint; a könyvben a közös irodalomjegyzékben ugyanezzel a számozással.</p>{self.references_web()}</section>')
            self.titles.append((len(self.pages) + 1, "Források", "alap", "forrasok"))
        toc = "".join(f'<li data-level="{lv}"><a href="#p-{"forrasok" if pt == "forrasok" and i > len(self.pages) else f"{i:02d}"}"><span class="n">{"§" if i > len(self.pages) else f"{i:02d}"}</span>{re.sub("<.*?>", "", t)}</a></li>' for i, t, lv, pt in self.titles[1:])
        tools = "".join(f'<li><a href="../eszkozok/{k}/">{t}</a></li>' for k, t, _, mod, _f in TOOLS if mod == self.meta["id"])
        chips = "".join(f'<button class="chip" data-level="{l}">{level_svg(l)}{LEVEL_HU[l]}</button>' for l in ("alap", "halado", "elit"))
        body = (f'{hero}<div class="wrap"><div class="layout"><aside class="toc"><ol>{toc}</ol><div class="tools"><b>Eszközök</b><ol>{tools}</ol></div></aside><main>'
                f'<div class="filters"><span class="lab">Szint:</span>{chips}<span class="lab" style="margin-left:8px">— a haladó az alapot is mutatja</span></div>{self.legend()}'
                + "".join(rest) + "</main></div></div>")
        quiz_js = f"<script>window.HT_QUIZ={json.dumps(quiz, ensure_ascii=False)};</script>" if quiz else ""
        return shell(f'{self.meta["id"]} · {self.meta["title"]}', body + quiz_js, "../../", nav_on=self.meta["id"], scripts=("site.js", "kviz.js"))


def load_quiz(mod_id):
    p = ROOT / f"data/quiz/{mod_id}-alvas.yaml"
    cands = list((ROOT / "data/quiz").glob(f"{mod_id}-*.yaml"))
    if not cands:
        return None
    q = yaml.safe_load(cands[0].read_text())
    for i, item in enumerate(q["questions"]):  # determinisztikus keverés, a helyes válasz ne mindig az első legyen
        rnd = random.Random(1000 + i)
        order = list(range(len(item["options"]))); rnd.shuffle(order)
        item["options"] = [item["options"][j] for j in order]
        item["answer"] = order.index(item["answer"])
    return q


def tool_page(key, title, desc, mod, datafile):
    tpl = (WEB / f"templates/{key}.html").read_text()
    tpl = tpl.replace("{{ICON_FIX}}", ICONS["fix"]).replace("{{ICON_EX}}", ICONS["ex"]).replace("{{ICON_IND}}", ICONS["ind"])
    data = ""
    if datafile:
        p = yaml.safe_load((ROOT / "data/tools" / datafile).read_text())
        data = f"<script>window.HT_TOOL={json.dumps(p, ensure_ascii=False)};</script>"
    return shell(title, tpl + data, "../../../", nav_on="tools", scripts=("site.js", f"{key}.js"))


def home(modules):
    cards = []
    for m in modules:
        cards.append(f'<a class="card" href="hu/{m["slug"]}/"><div class="k">{m["id"]}. modul · {m["pages"]} oldal</div><h2>{html.escape(m["title"])}</h2><p>{html.escape(m["lede"])}</p></a>')
    cards.append('<div class="card soon"><div class="k">hamarosan</div><h2>További 17 modul</h2><p>Élettan, edzés, táplálkozás, felszerelés, navigáció, mentális oldal, sablonok — a 04 modul a pilot, a többi ugyanezen a pályán készül.</p></div>')
    tools = "".join(f'<a class="card" href="hu/eszkozok/{k}/"><div class="k">eszköz · {mod}. modul</div><h2>{t}</h2><p>{d}</p></a>' for k, t, d, mod, _f in TOOLS)
    body = (f'<div class="wrap home-hero"><div class="kicker">Ultrakerékpáros oktatóanyag · vázlat v0.1</div><h1>{SITE_TITLE}</h1>'
            '<p class="sub">Az ultrakerékpározás tudománya és gyakorlata — önállóan feldolgozható modulok, a legfrissebb kutatásokból és a rutinos versenyzők egybevágó tapasztalatából. '
            'A PDF a tananyag; ez az oldal a hozzá tartozó eszközök és a webes olvasat.</p>'
            f'<div class="cards">{"".join(cards)}</div><h2 id="eszkozok" style="margin-top:24px">Eszközök</h2><div class="cards">{tools}</div>'
            '<p class="note">Jelölések a teljes anyagban: négysávos bizonyíték-ikon (összesített kutatás · terepvizsgálat · szakmai tapasztalat · feltörekvő), és minden sablonelemnél <span class="t fix">'
            + ICONS["fix"] + 'fix</span> <span class="t ex">' + ICONS["ex"] + 'példa</span> <span class="t ind">' + ICONS["ind"] + 'egyéni</span>.</p></div>')
    return shell("Kezdőlap", body, "", nav_on="home", scripts=("site.js",))


def build(paths):
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets/fonts").mkdir(parents=True)
    shutil.copy(ROOT / "design/tokens/tokens.css", OUT / "assets/tokens.css")
    shutil.copy(WEB / "web.css", OUT / "assets/web.css")
    for f in (ROOT / "design/fonts").glob("*.ttf"):
        shutil.copy(f, OUT / "assets/fonts" / f.name)
    for f in (WEB / "js").glob("*.js"):
        shutil.copy(f, OUT / "assets" / f.name)
    modules = []
    for p in paths:
        m = WebModule(p)
        quiz = load_quiz(m.meta["id"])
        out = OUT / "hu" / Path(p).stem
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(m.render_site(quiz))
        lede = re.sub("<.*?>", "", m.md(m.pages[0][1]).split("</p>")[0].split("<p>")[-1]) if m.pages else ""
        modules.append({"id": m.meta["id"], "slug": Path(p).stem, "title": m.meta["title"], "pages": len(m.pages), "lede": (lede.split(". ")[0] + ".") if len(lede) > 220 else lede})
        print("wrote", (out / "index.html").relative_to(ROOT), f"({len(m.pages)} szakasz, {len(m.cite_order)} hivatkozás)")
    for k, t, d, mod, datafile in TOOLS:
        out = OUT / "hu/eszkozok" / k
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(tool_page(k, t, d, mod, datafile))
        print("wrote", (out / "index.html").relative_to(ROOT))
    (OUT / "index.html").write_text(home(modules))
    (OUT / ".nojekyll").write_text("")
    print("wrote", (OUT / "index.html").relative_to(ROOT))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")] or [f"content/hu/{slug}.md" for slug, _ in MODULES_NAV]
    build([ROOT / a for a in args])
