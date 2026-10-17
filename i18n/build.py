"""Build /cs/, /sk/, /de/, /pl/, /fr/ from the English index.html + market landing pages (i18n/pages.py) + sitemap.xml.

Run from the repo root:  python3 i18n/build.py
Edit index.html (English) and the i18n/*.json files, then re-run.
"""
import json, re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pages_content import T as PT, SLUGS, price
import pages

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://str2g.com"
LANGS = {"cs": "cs_CZ", "sk": "sk_SK", "de": "de_DE", "pl": "pl_PL", "fr": "fr_FR", "es": "es_ES", "it": "it_IT", "nl": "nl_NL"}
# Other STR2G websites: English URL in the source -> per-language path
XLINKS = {u: {"cs": "/", "sk": "/", "de": "/de/", "pl": "/pl/", "fr": "/en/", "es": "/en/", "it": "/en/", "nl": "/en/"} for u in (
    "https://hyrox-prague.eu/en/", "https://hyroxtrainingclub.cz/en/", "https://formfactorygames.cz/en/")}
ATTRS = ("alt", "aria-label", "content", "title")

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
    missing = set()
    page_src = src.replace('<a href="/hyrox-training-plan/">HYROX training plan</a>', f'<a href="{SLUGS["plan"][lang]}">{PT[lang]["ui"]["plan_link"]}</a>', 1)
    page_src = page_src.replace('<a href="/online-hyrox-coach/">Online HYROX coach</a>', f'<a href="{SLUGS["coach"][lang]}">{PT[lang]["ui"]["coach_link"]}</a>', 1)
    out = translate_text(page_src, t, missing)
    def _fx(m, lang=lang):
        approx = price(lang, int(m.group(1)))[1]
        return f'<em class="fx">{approx}</em>' if approx else ""
    out = re.sub(r'<em class="fx" data-czk="(\d+)">[^<]*</em>', _fx, out)
    out = out.replace(TRACK_MARK, TRACK, 1)
    out = out.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    out = out.replace('content="en_GB"', f'content="{locale}"', 1)
    out = out.replace(f'<link rel="canonical" href="{BASE}/">', f'<link rel="canonical" href="{BASE}/{lang}/">', 1)
    out = out.replace(f'<meta property="og:url" content="{BASE}/">', f'<meta property="og:url" content="{BASE}/{lang}/">', 1)
    out = out.replace(' aria-current="page">EN<', '>EN<', 1)
    out = out.replace(f'hreflang="{lang}" lang="{lang}">', f'hreflang="{lang}" lang="{lang}" aria-current="page">', 1)
    out = re.sub(r'(src|content)="img/', r'\1="../img/', out)
    # links to the other STR2G websites -> same language
    for en_url, path in XLINKS.items():
        out = out.replace(f'href="{en_url}"', f'href="{en_url.rsplit("/en/", 1)[0]}{path[lang]}"')
    out = out.replace("'→ Our pick: '", json.dumps(t.get("__hint", "→ Our pick: "), ensure_ascii=False).replace('"', "'"))
    d = ROOT / lang
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(out, encoding="utf-8")
    print(f"{lang}: written, {len(missing)} untranslated text nodes")
    for m in sorted(missing):
        print("   ·", m[:90])


# ---- landing pages pro trhy + sitemap
pages.build(ROOT)
ALL = ["en", "cs", "sk", "de", "pl", "fr", "es", "it", "nl"]
HOMES = {l: (f"{BASE}/" if l == "en" else f"{BASE}/{l}/") for l in ALL}
LASTMOD = "2026-10-17"
def _entry(loc, alts):
    links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{u}"/>' for l, u in alts.items())
    links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{alts["en"]}"/>'
    return f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{LASTMOD}</lastmod>{links}\n  </url>"
entries = []
for group in (HOMES, {l: BASE + SLUGS["plan"][l] for l in ALL}, {l: BASE + SLUGS["coach"][l] for l in ALL}):
    for l in ALL:
        entries.append(_entry(group[l], group))
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n", encoding="utf-8")
print(f"sitemap.xml: {len(entries)} URLs")
