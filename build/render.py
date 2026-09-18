#!/usr/bin/env python3
"""Modul-Markdown → HTML → PDF (Chromium print, Playwright).

Használat:  python3 build/render.py content/hu/04-alvas.md [--html-only] [--draft]
Kimenet:    dist/<modul>.html és dist/<modul>.pdf; túlcsordulási jelentés a stdout-on.

Direktívák (design/styleguide.md 7. pont): :::page … :::, :::you, :::protocol, :::figure src= caption= ev=,
:::references; inline {ev:A}, {fix} {példa} {egyéni}, [@kulcs; @kulcs].
"""
import re, sys, json, html
from pathlib import Path
import yaml, markdown

ROOT = Path(__file__).resolve().parents[1]
TOK = json.loads((ROOT / "design/tokens/tokens.json").read_text())
SOURCES = yaml.safe_load((ROOT / "data/sources.yaml").read_text())["sources"]
DRAFT = "--draft" in sys.argv

GRADE_LABEL = {"A": "összesített kutatás", "B": "terepvizsgálat", "C": "szakmai tapasztalat", "D": "feltörekvő"}
LEVEL_HU = {"alap": "Alap", "halado": "Haladó", "elit": "Elit"}
TYPE_HU = {"modulnyito": "Modulnyitó", "fogalom": "Fogalom", "adat": "Adat", "konvergencia": "Tapasztalat", "protokoll": "Protokoll",
           "sablon": "Sablon", "feladat": "Feladat", "osszefoglalo": "Összefoglaló", "forrasok": "Források"}
ICONS = {
    "fix": '<svg viewBox="0 0 24 24"><path d="M12 3v6l4 5H8l4-5zM12 14v7M6 21h12"/></svg>',
    "ex": '<svg viewBox="0 0 24 24"><path d="M4 20l4-1 11-11-3-3L5 16zM13 6l3 3"/></svg>',
    "ind": '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
}
DISC_ICONS = {
    "onellato": '<svg viewBox="0 0 24 24" fill="none" stroke="#52514e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8h12l1 12H5zM9 8V6a3 3 0 0 1 6 0v2"/></svg>',
    "kiseros": '<svg viewBox="0 0 24 24" fill="none" stroke="#52514e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14l2-5h12l2 5v4H4zM7 18v2M17 18v2"/><circle cx="8" cy="15.5" r="1"/><circle cx="16" cy="15.5" r="1"/></svg>',
    "brevet": '<svg viewBox="0 0 24 24" fill="none" stroke="#52514e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="10" width="14" height="9" rx="1.5"/><path d="M9 10V6h6v4M8 19v2M16 19v2"/></svg>',
    "24h": '<svg viewBox="0 0 24 24" fill="none" stroke="#52514e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg>',
}


def ev_svg(g):
    g = g.lower()
    return (f'<svg class="ev {g}" viewBox="0 0 26 18" aria-label="bizonyíték {g.upper()}"><rect x="0" y="12" width="5" height="6" rx="1"/>'
            f'<rect x="7" y="8" width="5" height="10" rx="1"/><rect x="14" y="4" width="5" height="14" rx="1"/><rect x="21" y="0" width="5" height="18" rx="1"/></svg>')


def tag_html(kind):
    k = {"fix": "fix", "példa": "ex", "egyéni": "ind"}[kind]
    return f'<span class="t {k}">{ICONS[k]}{kind}</span>'


def level_svg(level):
    n = {"alap": 1, "halado": 2, "elit": 3}[level]
    paths = {1: "M5 12h14", 2: "M5 9h14M5 15h14", 3: "M5 7h14M5 12h14M5 17h14"}[n]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="#184f95" stroke-width="2.2" stroke-linecap="round"><path d="{paths}"/></svg>'


class Module:
    REFS_FIRST, REFS_PAGE = 21, 30

    def __init__(self, path):
        text = Path(path).read_text()
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        self.meta = yaml.safe_load(m.group(1))
        self.body = text[m.end():]
        self.cite_order = []  # kulcsok első előfordulás szerint

    # ---- inline jelek
    def inline(self, s):
        def cite(m):
            keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
            nums = []
            for k in keys:
                if k not in SOURCES:
                    raise SystemExit(f"ismeretlen hivatkozás: {k}")
                if k not in self.cite_order:
                    self.cite_order.append(k)
                nums.append(str(self.cite_order.index(k) + 1))
            return f'<sup class="cite">{", ".join(nums)}</sup>'
        s = re.sub(r"\[(@[^\]]+)\]", cite, s)
        s = re.sub(r"\{ev:([ABCD])\}", lambda m: ev_svg(m.group(1)), s)
        s = re.sub(r"\{(fix|példa|egyéni)\}", lambda m: tag_html(m.group(1)), s)
        return s

    def md(self, s):
        return markdown.markdown(self.inline(s), extensions=["tables", "sane_lists", "attr_list"])

    # ---- blokkok
    @staticmethod
    def parse_blocks(src):
        """Soralapú, egymásba ágyazható direktíva-feldolgozó. Visszaad: [("md", szöveg) | (név, attribútumok, belső szöveg)]."""
        out, buf, stack = [], [], []
        for line in src.split("\n"):
            m = re.match(r"^:::(\w+)(.*)$", line)
            if m and not stack:
                if "".join(buf).strip():
                    out.append(("md", "\n".join(buf)))
                buf = []; stack.append((m.group(1), m.group(2).strip())); inner = []
                continue
            if m and stack:
                stack.append((m.group(1), m.group(2).strip())); inner.append(line); continue
            if line.strip() == ":::" and stack:
                name, attrs = stack.pop()
                if stack:
                    inner.append(line)
                else:
                    out.append((name, attrs, "\n".join(inner)))
                continue
            (inner if stack else buf).append(line)
        if "".join(buf).strip():
            out.append(("md", "\n".join(buf)))
        return out

    def render_blocks(self, src, page_type):
        return self.parse_blocks(src)

    def figure_html(self, attrs, cls="figure"):
        a = dict(re.findall(r'(\w+)=("[^"]*"|\S+)', attrs))
        a = {k: v.strip('"') for k, v in a.items()}
        svg = (ROOT / a["src"]).read_text().split("?>", 1)[-1].strip().replace("{{FONT}}", "Inter")
        cap = self.inline(a.get("caption", ""))
        ev = ev_svg(a["ev"]) if a.get("ev") else ""
        if a.get("size") == "half":
            cls += " half"
        return f'<div class="{cls}">{svg}<p class="caption">{cap} {ev}</p></div>'

    def protocol_html(self, body):
        # számozott lista → ol.steps; a sor végi jelek (t, ev) a tags oszlopba
        items = re.findall(r"^\d+\.\s+(.*?)(?=^\d+\.\s|\Z)", body, re.S | re.M)
        lis = []
        for it in items:
            h = self.md(it.strip())
            h = re.sub(r"^<p>|</p>$", "", h.strip(), flags=re.S)
            tags = re.findall(r'<span class="t [^"]+">.*?</span>|<svg class="ev [abcd]".*?</svg>', h, re.S)
            for t in tags:
                h = h.replace(t, "", 1)
            h = re.sub(r"\s+([.,;])", r"\1", h)
            lis.append(f'<li><div class="body">{h}</div><div class="tags">{"".join(tags)}</div></li>')
        return f'<ol class="steps">{"".join(lis)}</ol>'

    def references_html(self, keys=None, start=1):
        rows = []
        for i, k in enumerate(keys or self.cite_order, start):
            s = SOURCES[k]
            au = s.get("authors") or []
            au = ", ".join(a for a in au[:3] if a) + (" et al." if len(au) > 3 else "")
            cred = f" — {html.escape(s['credential'])}" if s.get("credential") else ""
            venue = html.escape(str(s.get("venue") or ""))
            doi = f' doi:{s["doi"]}' if s.get("doi") else ""
            rows.append(f'<div class="ref"><b>{i}.</b> {html.escape(au)} ({s.get("year")}). {html.escape(str(s.get("title")))}. <i>{venue}</i>.{doi}{cred} {ev_svg(s["grade"])} <span class="key">{k}</span></div>')
        return f'<div class="refs">{"".join(rows)}</div>'

    # ---- oldal
    def page_html(self, attrs, body, idx, total, refchunk=None):
        a = dict(re.findall(r"(\w+)=(\S+)", attrs))
        ptype, level, disc = a.get("type", "fogalom"), a.get("level", "alap"), a.get("disc", "all")
        discs = list(DISC_ICONS) if disc == "all" else disc.split(",")
        blocks = self.render_blocks(body, ptype)
        parts = []
        title = ""
        for b in blocks:
            if b[0] == "md":
                h = self.md(b[1])
                # első h1/h2 = oldalcím; az azt követő első bekezdés = lede
                if not title:
                    m = re.search(r"<h[12]>(.*?)</h[12]>", h, re.S)
                    if m:
                        title = m.group(1)
                        h = h.replace(m.group(0), "", 1)
                        if ptype not in ("forrasok",):
                            h = re.sub(r"^\s*<p>(.*?)</p>", r'<p class="lede">\1</p>', h, count=1, flags=re.S)
                parts.append(h)
            elif b[0] == "figure":
                parts.append(self.figure_html(b[1]))
            elif b[0] == "you":
                parts.append(f'<div class="box you"><h3>Mit jelent neked</h3>{self.md(b[2])}</div>')
            elif b[0] == "protocol":
                parts.append(self.protocol_html(b[2]))
            elif b[0] == "refchunk":
                parts.append(self.references_html(*refchunk))
            elif b[0] == "references":
                parts.append(self.references_html(self.cite_order[:self.REFS_FIRST]))
        content = "\n".join(parts)
        mod = self.meta["id"]; mtitle = self.meta["title"]
        if ptype == "modulnyito":
            inner = (f'<div class="modnum">{mod}</div><div class="kicker">Hosszú távon · {mod}. modul</div><h1>{title}</h1>{content}')
            return f'<section class="page modulnyito">{inner}{self.footer(idx, total, dark=True)}</section>'
        # elrendezés: fogalom/adat → lede + ábra + kétoszlopos szöveg + you alul
        kicker = f'<div class="kicker"><b>{mod} · {mtitle}</b> &nbsp;·&nbsp; {TYPE_HU.get(ptype, ptype)} &nbsp;·&nbsp; {LEVEL_HU.get(level, level)}</div>'
        sidebar = f'<div class="sidebar">{level_svg(level)}<div class="sep"></div>{"".join(DISC_ICONS[d] for d in discs if d in DISC_ICONS)}</div>'
        layout = self.layout(ptype, parts, title)
        draft = '<div class="draft-tag">Vázlat v0.1</div>' if DRAFT else ""
        return f'<section class="page {ptype}" data-type="{ptype}">{draft}{sidebar}{kicker}<h1>{title}</h1>{layout}{self.legend()}{self.footer(idx, total)}</section>'

    @staticmethod
    def cols_with_tables(text):
        """A táblázatok teljes szélességben, a köztük lévő szöveg két oszlopban."""
        out = []
        for seg in re.split(r"(<table>.*?</table>)", text, flags=re.S):
            if not seg.strip():
                continue
            out.append(seg if seg.startswith("<table>") else f'<div class="cols2">{seg}</div>')
        return "".join(out)

    def layout(self, ptype, parts, title):
        you = [p for p in parts if 'class="box you"' in p]
        figs = [p for p in parts if p.startswith('<div class="figure')]
        rest = [p for p in parts if p not in you and p not in figs]
        text = "\n".join(rest)
        lede = ""
        m = re.match(r'\s*<p class="lede">.*?</p>', text, re.S)
        if m:
            lede, text = m.group(0), text[m.end():]
        if ptype in ("fogalom", "adat"):
            return f'{lede}{"".join(figs)}{self.cols_with_tables(text)}{"".join(you)}'
        if ptype == "protokoll":
            # a lépéslista teljes szélességben, a többi szöveg két oszlopban
            steps = re.findall(r'<ol class="steps">.*?</ol>', text, re.S)
            other = text
            for s_ in steps: other = other.replace(s_, "")
            return f'{lede}{"".join(figs)}{"".join(steps)}{self.cols_with_tables(other)}{"".join(you)}'
        if ptype == "feladat":
            return f'{lede}{self.cols_with_tables(text)}{"".join(you)}'
        if ptype == "forrasok":
            refs = re.findall(r'<div class="refs">.*?</div>\s*$', text, re.S)
            other = text
            for r in refs: other = other.replace(r, "")
            return f'{lede}<div class="cols2">{other}</div>{"".join(refs)}'
        return f'{lede}{"".join(figs)}{text}{"".join(you)}'

    def legend(self):
        evs = "".join(f"<span>{ev_svg(g)} {GRADE_LABEL[g]}</span>" for g in "ABCD")
        tags = "".join(tag_html(k) for k in ("fix", "példa", "egyéni"))
        return f'<div class="legend"><span>Bizonyíték:</span>{evs}<span style="margin-left:auto">Sablon:</span>{tags}</div>'

    def footer(self, idx, total, dark=False):
        return (f'<div class="footer"><span>{self.meta["id"]} · {self.meta["title"]}</span><span>Hosszú távon · v{self.meta.get("version", "0")}</span>'
                f'<span class="pg">{self.meta["id"]} – {idx:02d}</span></div>')

    def render(self):
        pages = [(b[1], b[2]) for b in self.parse_blocks(self.body) if b[0] == "page"]
        # két menet: az első a hivatkozás-sorrendet gyűjti (a források oldal a végén van)
        for attrs, body in pages:
            self.inline(body)
        extra = max(0, -(-(len(self.cite_order) - self.REFS_FIRST) // self.REFS_PAGE)) if len(self.cite_order) > self.REFS_FIRST else 0
        total = len(pages) + extra
        htmls = [self.page_html(a, b, i + 1, total) for i, (a, b) in enumerate(pages)]
        # hivatkozás-folytató oldalak
        rest = self.cite_order[self.REFS_FIRST:]
        n = len(pages)
        while rest:
            chunk, rest = rest[:self.REFS_PAGE], rest[self.REFS_PAGE:]
            start = len(self.cite_order) - len(rest) - len(chunk) + 1
            n += 1
            htmls.append(self.page_html("type=forrasok level=alap disc=all", f"## Források (folytatás)\n\n:::refchunk {start}\n:::\n", n, total, refchunk=(chunk, start)))
        head = (f'<!DOCTYPE html><html lang="hu"><head><meta charset="utf-8"><title>{self.meta["title"]}</title>'
                f'<link rel="stylesheet" href="../design/tokens/tokens.css"><link rel="stylesheet" href="../design/print.css"></head><body>')
        return head + "\n".join(htmls) + "</body></html>"


def fit_pages(html_path, pdf_path):
    """Chromiumban ellenőrzi a túlcsordulást; ha kell, compact/compact2/compact3 osztályt ad az oldalnak, majd PDF-et ír."""
    from playwright.sync_api import sync_playwright
    report = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto(Path(html_path).resolve().as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        js = """() => Array.from(document.querySelectorAll('.page')).map(pg => {
            const r = pg.getBoundingClientRect(); const limit = r.top + r.height - (pg.classList.contains('modulnyito') ? 90 : 90);
            let bottom = r.top; for (const el of pg.children) { if (['sidebar','footer','legend','draft-tag','modnum','meta'].some(c => el.classList.contains(c))) continue;
              const rr = el.getBoundingClientRect(); if (rr.bottom > bottom) bottom = rr.bottom; }
            return { over: Math.round(bottom - limit), cls: pg.className }; })"""
        for level in ("compact", "compact2", "compact3"):
            res = pg.evaluate(js)
            over = [i for i, r in enumerate(res) if r["over"] > 0]
            if not over: break
            for i in over:
                pg.evaluate(f"document.querySelectorAll('.page')[{i}].classList.remove('compact','compact2'); document.querySelectorAll('.page')[{i}].classList.add('{level}')")
            pg.wait_for_timeout(100)
        res = pg.evaluate(js)
        for i, r in enumerate(res):
            flag = "TÚLCSORDUL" if r["over"] > 0 else "ok"
            report.append(f"oldal {i+1:02d}: {flag:10s} {r['over']:+5d}px  [{r['cls']}]")
        pg.pdf(path=str(pdf_path), format="A4", print_background=True, prefer_css_page_size=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        b.close()
    return report


if __name__ == "__main__":
    src = Path([a for a in sys.argv[1:] if not a.startswith("--")][0])
    mod = Module(src)
    out_html = ROOT / "dist" / (src.stem + ".html")
    out_html.parent.mkdir(exist_ok=True)
    out_html.write_text(mod.render())
    print("wrote", out_html.relative_to(ROOT), f"({len(mod.cite_order)} hivatkozás)")
    if "--html-only" not in sys.argv:
        pdf = ROOT / "dist" / (src.stem + ".pdf")
        for line in fit_pages(out_html, pdf):
            print(line)
        print("wrote", pdf.relative_to(ROOT))
