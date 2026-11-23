"""Build /cs/, /sk/, /de/, /pl/, /fr/ from the English index.html + market landing pages (i18n/pages.py) + sitemap.xml.

Run from the repo root:  python3 i18n/build.py
Edit index.html (English) and the i18n/*.json files, then re-run.
"""
import json, re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
# Programy a ceny z appky Strong Coach: stáhnout dřív, než se načte pages_content (ten z nich bere ceny)
import app_store
_APP_DATA, _APP_SRC = app_store.sync()
print(f"app_store: {len(_APP_DATA)} programů z appky ({_APP_SRC}); chybí: {app_store.missing(_APP_DATA) or 'nic'}")
from pages_content import T as PT, SLUGS, price
import pages

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://str2g.com"
LANGS = {"cs": "cs_CZ", "sk": "sk_SK", "de": "de_DE", "pl": "pl_PL", "fr": "fr_FR", "es": "es_ES", "it": "it_IT", "nl": "nl_NL"}
# Other STR2G websites: English URL in the source -> per-language path
XLINKS = {u: {"cs": "/", "sk": "/", "de": "/de/", "pl": "/pl/", "fr": "/en/", "es": "/en/", "it": "/en/", "nl": "/en/"} for u in (
    "https://hyroxtrainingclub.cz/en/", "https://formfactorygames.cz/en/")}
XLINKS["https://www.ladislavsuchanek.cz/en/"] = {"cs": "/", "sk": "/", "de": "/de/", "pl": "/pl/", "fr": "/en/", "es": "/en/", "it": "/en/", "nl": "/en/"}
XLINKS["https://hyrox-prague.eu/"] = {"cs": "/cs/", "sk": "/cs/", "de": "/de/", "pl": "/pl/", "fr": "/", "es": "/", "it": "/", "nl": "/"}
XLINKS["https://riahrusovska.cz/en/"] = {l: ("/" if l in ("cs", "sk") else "/en/") for l in ("cs", "sk", "de", "pl", "fr", "es", "it", "nl")}
XLINKS["https://strongertogether.cz/en/"] = {l: ("/" if l in ("cs", "sk") else "/en/") for l in ("cs", "sk", "de", "pl", "fr", "es", "it", "nl")}
XLINKS["https://xenomczech.cz/en/"] = {l: ("/" if l in ("cs", "sk") else "/en/") for l in ("cs", "sk", "de", "pl", "fr", "es", "it", "nl")}
ATTRS = ("alt", "aria-label", "content", "title")

# Newsletter okno: i18n/newsletter.html je zdroj, do index.html se vždy přepíše aktuální verze
import re as _re
import re
_idx = ROOT / "index.html"
_nl = (ROOT / "i18n" / "newsletter.html").read_text(encoding="utf-8").rstrip("\n")
_html = _idx.read_text(encoding="utf-8")
_html = _re.sub(r"<!--STR2G_NEWSLETTER-->.*?<!--/STR2G_NEWSLETTER-->", lambda m: _nl, _html, count=1, flags=_re.S)
# Ukázkový týden zdarma: i18n/freeweek.html je zdroj, stejně jako newsletter
_fw = (ROOT / "i18n" / "freeweek.html").read_text(encoding="utf-8").rstrip("\n")
_html = _re.sub(r"<!--STR2G_FREEWEEK-->.*?<!--/STR2G_FREEWEEK-->", lambda m: _fw, _html, count=1, flags=_re.S)
# Odkazy na zveřejněné průvodce (i18n/guides.py) do patičky homepage
import sys as _sys; _sys.path.insert(0, str(ROOT / "i18n"))
import guides as _guides
_html = _re.sub(r"<!--STR2G_GUIDES-->.*?<!--/STR2G_GUIDES-->", lambda m: "<!--STR2G_GUIDES-->" + _guides.nav("en") + "<!--/STR2G_GUIDES-->", _html, count=1, flags=_re.S)
# Tlačítka koupit + ceny na hlavní stránce podle appky (odkaz na vlastní storefront místo Strivee)
from pages_content import PROGRAMS as _P
def _fmt(n): return f"{n:,}"
for _pid in app_store.APP_IDS:
    if _pid not in _P: continue
    _sid, _czk, _mon, _name = _P[_pid]
    _html = re.sub(r'href="https://train\.strivee\.app/payment/[A-Za-z0-9]+" target="_blank" rel="noopener" (data-program="%s") data-value="\d+"' % re.escape(_name),
                   lambda m: f'href="{app_store.buy_url(_pid)}" {m.group(1)} data-value="{_czk}"', _html)
    _html = re.sub(r'(href="%s" data-program="[^"]*") data-value="\d+"' % re.escape(app_store.buy_url(_pid)), lambda m: f'{m.group(1)} data-value="{_czk}"', _html)
    _html = re.sub(r'(id="%s">.*?<div class="price"><b>)CZK [\d,]+(</b>.*?data-czk=")\d+(")' % _pid,
                   lambda m: f'{m.group(1)}CZK {_fmt(_czk)}{m.group(2)}{_czk}{m.group(3)}', _html, count=1, flags=re.S)
_idx.write_text(_html, encoding="utf-8")

src = (ROOT / "index.html").read_text(encoding="utf-8")

# Tracking snippet (i18n/tracking.html) is copied verbatim into every language,
# never run through the translator.
TRACK = (ROOT / "i18n" / "tracking.html").read_text(encoding="utf-8").rstrip("\n")
TRACK_MARK = "<!--STR2G_TRACKING-->"
assert TRACK in src, "index.html must contain i18n/tracking.html right after <meta charset>"
src = src.replace(TRACK, TRACK_MARK, 1)


def translate_text(html, t, missing):
    parts = re.split(r"(<[^>]+>)", html)
    raw = 0
    for i, p in enumerate(parts):
        if p.startswith("<"):
            tag = p[1:].split()[0].split(">")[0].lower() if len(p) > 1 else ""
            if tag in ("script", "style"):
                raw += 1
            elif tag in ("/script", "/style"):
                raw -= 1
            # attributes
            def attr_sub(m):
                v = m.group(2)
                return f'{m.group(1)}="{t[v]}"' if v in t else m.group(0)
            parts[i] = re.sub(r'\b(%s)="([^"]*)"' % "|".join(ATTRS), attr_sub, p)
            continue
        if raw or not p.strip():
            continue
        core = p.strip()
        if core in t:
            lead = p[: len(p) - len(p.lstrip())]
            trail = p[len(p.rstrip()):]
            val = t[core]
            if val[:1] in ".,;:!?":
                lead = ""
            parts[i] = lead + val + trail
        elif re.search(r"[A-Za-z]{3}", core):
            missing.add(core)
    return "".join(parts)


for lang, locale in LANGS.items():
    t = json.loads((ROOT / "i18n" / f"{lang}.json").read_text(encoding="utf-8"))
    from programs_content import HOME_EXTRA
    t.update(HOME_EXTRA.get(lang, {}))
    missing = set()
    page_src = src.replace('<a href="/hyrox-training-plan/">HYROX training plan</a>', f'<a href="{SLUGS["plan"][lang]}">{PT[lang]["ui"]["plan_link"]}</a>', 1)
    page_src = page_src.replace('<a href="/online-hyrox-coach/">Online HYROX coach</a>', f'<a href="{SLUGS["coach"][lang]}">{PT[lang]["ui"]["coach_link"]}</a>', 1)
    # Odkazy "Details" na vlastní stránky programů: CS má svoje stránky, ostatní jazyky zatím vedou na Strivee
    from programs_content import PSLUGS, PROG_LANGS
    from pages_content import PROGRAMS
    from app_store import buy_url
    page_src = page_src.replace('<a class="btn btn-ghost" href="/online-hyrox-coach/">Details</a>',
                                f'<a class="btn btn-ghost" href="{SLUGS["coach"][lang]}">Details</a>', 1)
    for _pid, _sl in PSLUGS.items():
        if lang in PROG_LANGS:
            _new = f'href="{_sl[lang]}"'
        else:
            _new = f'href="{buy_url(_pid)}"'
        page_src = page_src.replace(f'href="{_sl["en"]}"', _new)
    # 12-Week Advanced má zatím texty jen v EN a CS
    if lang not in PROG_LANGS:
        page_src = re.sub(r"[ \t]*<!--ADV-->.*?<!--/ADV-->\n?", "", page_src, flags=re.S)
        page_src = page_src.replace('<div class="grid two" id="race-grid">', '<div class="grid" id="race-grid">', 1)
    out = translate_text(page_src, t, missing)
    def _fx(m, lang=lang):
        approx = price(lang, int(m.group(1)))[1]
        return f'<em class="fx">{approx}</em>' if approx else ""
    out = re.sub(r'<em class="fx" data-czk="(\d+)">[^<]*</em>', _fx, out)
    out = out.replace(TRACK_MARK, TRACK, 1)
    if lang in ("cs", "sk"):
        out = out.replace('<a href="/privacy/">', '<a href="/cs/ochrana-osobnich-udaju/">', 1)
        out = out.replace('<a href="/terms/">', '<a href="/cs/obchodni-podminky/">', 1)
    out = out.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    out = out.replace('content="en_GB"', f'content="{locale}"', 1)
    out = out.replace(f'<link rel="canonical" href="{BASE}/">', f'<link rel="canonical" href="{BASE}/{lang}/">', 1)
    out = out.replace(f'<meta property="og:url" content="{BASE}/">', f'<meta property="og:url" content="{BASE}/{lang}/">', 1)
    out = out.replace(' aria-current="page">EN<', '>EN<', 1)
    out = out.replace(f'hreflang="{lang}" lang="{lang}">', f'hreflang="{lang}" lang="{lang}" aria-current="page">', 1)
    out = re.sub(r'(src|content)="img/', r'\1="../img/', out)
    # links to the other STR2G websites -> same language
    for en_url, path in XLINKS.items():
        out = out.replace(f'href="{en_url}"', f'href="{(en_url.rsplit("/en/", 1)[0] if "/en/" in en_url else en_url.rstrip("/"))}{path[lang]}"')
    out = out.replace("'→ Our pick: '", json.dumps(t.get("__hint", "→ Our pick: "), ensure_ascii=False).replace('"', "'"))
    d = ROOT / lang
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(out, encoding="utf-8")
    print(f"{lang}: written, {len(missing)} untranslated text nodes")
    for m in sorted(missing):
        print("   ·", m[:90])


# ---- landing pages pro trhy + sitemap
pages.build(ROOT)

# ---- zásady ochrany osobních údajů
import privacy
_tr_parts = pages.extract(src.replace(TRACK_MARK, TRACK, 1))
_tr, _st, _fonts, _ver, _icons = _tr_parts
privacy.build(ROOT, TRACK, _fonts, _icons)
import terms
terms.build(ROOT, TRACK, _fonts, _icons)

# ---- storefront: statický obsah a strukturovaná data z appky (pro vyhledávače)
import storefront_static
storefront_static.build(ROOT)
ALL = ["en", "cs", "sk", "de", "pl", "fr", "es", "it", "nl"]
HOMES = {l: (f"{BASE}/" if l == "en" else f"{BASE}/{l}/") for l in ALL}
LASTMOD = "2026-10-23"
def _entry(loc, alts):
    links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{u}"/>' for l, u in alts.items())
    links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{alts["en"]}"/>'
    return f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{LASTMOD}</lastmod>{links}\n  </url>"
entries = []
for group in (HOMES, {l: BASE + SLUGS["plan"][l] for l in ALL}, {l: BASE + SLUGS["coach"][l] for l in ALL}):
    for l in ALL:
        entries.append(_entry(group[l], group))

# ---- samostatné stránky programů (zatím EN + CS)
import programs
from programs_content import PSLUGS as _PS, PROG_LANGS as _PL, PROG_ORDER as _PO
programs.build(ROOT, _tr_parts)
for _pid in _PO:
    group = {l: BASE + _PS[_pid][l] for l in _PL}
    for l in _PL:
        entries.append(_entry(group[l], group))
# ---- rozcestník programů /programs/ a /cs/programy/ (cíl: „HYROX training programs“)
import hub
_hub = hub.build(ROOT, _tr_parts)
for l in _hub:
    entries.append(_entry(_hub[l], _hub))
# ---- anglické průvodce (i18n/guides.py), koncepty (draft) se negenerují
import guides
for _u in guides.build(ROOT, _tr_parts):
    entries.append(_entry(_u, {"en": _u}))
entries.append(f"  <url>\n    <loc>{BASE}/storefront/</loc>\n    <lastmod>{LASTMOD}</lastmod>\n  </url>")
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n", encoding="utf-8")
print(f"sitemap.xml: {len(entries)} URLs")

# ---- FAQPage strukturovaná data (Google + AI vyhledávače)
import faq_ld
faq_ld.apply(ROOT)

# ---- Google Merchant produktový feed (/feed.xml CZ, /feed-en.xml EN)
import feed
feed.build(ROOT)
