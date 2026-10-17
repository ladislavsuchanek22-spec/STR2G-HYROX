"""Generátor landing pages pro trhy (EN/UK, CZ, SK, DE, PL, FR).

Volá ho i18n/build.py. Obsah je v i18n/pages_content.py.
Styly, fonty a měřicí skript (cookies, Meta Pixel, GA4, Google Ads) se berou z index.html,
takže podstránky vypadají i měří stejně jako hlavní stránka.
"""
import json
import re
from html import escape
from pathlib import Path

from pages_content import T, SLUGS, HOME, LOCALE, COUNTRY, PROGRAMS, PLAN_PICKS, price

BASE = "https://str2g.com"
LANG_LABEL = {"en": "EN", "cs": "CZ", "sk": "SK", "de": "DE", "pl": "PL", "fr": "FR"}
ORDER = ["en", "cs", "sk", "de", "pl", "fr"]
NET = {  # weby STR2G v patičce podle jazyka
    "en": [("https://hyrox-prague.eu/en/", "HYROX Prague"), ("https://hyroxtrainingclub.cz/en/", "HYROX Training Club"),
           ("https://formfactorygames.cz/en/", "Form Factory Games"), ("https://www.ladislavsuchanek.cz/", "Ladislav Suchánek")],
}
NET["cs"] = [("https://hyrox-prague.eu/", "HYROX Prague"), ("https://hyroxtrainingclub.cz/", "HYROX Training Club"),
             ("https://formfactorygames.cz/", "Form Factory Games"), ("https://www.ladislavsuchanek.cz/", "Ladislav Suchánek")]
NET["sk"] = NET["cs"]
NET["de"] = [("https://hyrox-prague.eu/de/", "HYROX Prague"), ("https://hyroxtrainingclub.cz/de/", "HYROX Training Club"),
             ("https://formfactorygames.cz/de/", "Form Factory Games"), ("https://www.ladislavsuchanek.cz/", "Ladislav Suchánek")]
NET["pl"] = [("https://hyrox-prague.eu/pl/", "HYROX Prague"), ("https://hyroxtrainingclub.cz/pl/", "HYROX Training Club"),
             ("https://formfactorygames.cz/pl/", "Form Factory Games"), ("https://www.ladislavsuchanek.cz/", "Ladislav Suchánek")]
NET["fr"] = NET["en"]

EXTRA_CSS = """
.lp-hero{min-height:min(78vh,720px)}
.crumbs{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.crumbs a{color:var(--muted);text-decoration:none}.crumbs a:hover{color:var(--accent)}
.lp-list{list-style:none;margin:0;padding:0;display:grid;gap:12px;max-width:820px}
.lp-list li{position:relative;padding-left:26px;font-size:17px;line-height:1.55}
.lp-list li::before{content:"";position:absolute;left:0;top:.62em;width:12px;height:2px;background:var(--accent)}
.lp-list b{color:var(--fg)}
.lp-p{max-width:820px;font-size:17px;line-height:1.6;color:var(--muted);margin:0 0 22px}
.lp-p a,.lp-note a{color:var(--accent)}
.lp-table{width:100%;max-width:980px;border-collapse:collapse;font-size:16px}
.lp-table th{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);text-align:left;padding:0 14px 10px 0;border-bottom:2px solid var(--accent)}
.lp-table td{overflow-wrap:anywhere;padding:14px 14px 14px 0;border-bottom:1px solid var(--line);vertical-align:top}
.lp-table td:first-child{font-family:var(--display);font-style:italic;font-weight:800;font-size:22px;text-transform:uppercase;width:70px}
.lp-table td:last-child{color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
.phase{min-width:0;border-top:3px solid var(--accent);background:var(--panel,#0f0f0e);padding:20px}
.phase small{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.phase h3{overflow-wrap:break-word;hyphens:auto;font-family:var(--display);font-style:italic;font-weight:800;font-size:28px;text-transform:uppercase;margin:6px 0 8px;line-height:1}
.phase p{color:var(--muted);font-size:15px;margin:0}
.lp-note{font-family:var(--mono);font-size:12px;color:var(--muted);margin-top:18px;max-width:820px;line-height:1.6}
.lp-quote{margin:28px 0 0;max-width:820px;border-left:3px solid var(--accent);padding:6px 0 6px 20px}
.lp-quote blockquote{margin:0 0 10px;font-size:19px;line-height:1.5}
.lp-quote figcaption{font-family:var(--mono);font-size:12px;color:var(--muted)}
.lp-offer{margin-top:28px;max-width:520px}
.lp-steps{counter-reset:s;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.lp-steps li{counter-increment:s;background:var(--panel,#0f0f0e);border:1px solid var(--line);padding:20px;font-size:15.5px;line-height:1.5}
.lp-steps li::before{content:counter(s,decimal-leading-zero);display:block;font-family:var(--display);font-style:italic;font-weight:900;font-size:40px;color:var(--accent);line-height:1;margin-bottom:10px}
.guides{display:flex;flex-wrap:wrap;gap:8px 20px;margin:0 0 18px;padding:0 0 18px;border-bottom:1px solid var(--line)}
.guides a{color:var(--fg);text-decoration:none;font-weight:500}.guides a:hover,.guides a[aria-current]{color:var(--accent)}
@media (max-width:980px){.phases{grid-template-columns:1fr 1fr}.lp-steps{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.lp-hero h1{font-size:clamp(40px,11vw,60px)}.shead h2{font-size:clamp(34px,9.5vw,44px)}}
@media (max-width:620px){.phases,.lp-steps{grid-template-columns:1fr}.lp-table td:first-child{width:48px;font-size:18px}.lp-table{font-size:15px}}
"""


def extract(src):
    tracking = (Path(__file__).resolve().parent / "tracking.html").read_text(encoding="utf-8").rstrip("\n")
    style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
    fonts = re.search(r'<link rel="stylesheet" href="(https://fonts.googleapis.com[^"]+)"', src).group(1)
    verify = re.findall(r'<meta name="google-site-verification" content="[^"]+">', src)
    icons = "\n".join(re.findall(r'<link rel="(?:icon|apple-touch-icon|manifest)"[^>]*>', src))
    return tracking, style, fonts, "\n".join(verify), icons


def price_html(lang, pid):
    sid, czk, monthly, _ = PROGRAMS[pid]
    main, fx = price(lang, czk)
    u = T[lang]["ui"]
    period = u["per_month"] if monthly else u["one_time"]
    fx_html = f'<em class="fx">{fx}</em>' if fx else ""
    return f'<div class="price"><b>{main}</b><span>{period}</span>{fx_html}</div>'


def card(lang, pid, kind):
    sid, czk, monthly, pname = PROGRAMS[pid]
    u = T[lang]["ui"]
    btn = u["start_btn"] if monthly else u["buy_btn"]
    name = T[lang]["names"].get(pid, pname)
    return (f'<article class="card"><div class="kind">{escape(kind)}</div><h4>{escape(name)}</h4>{price_html(lang, pid)}'
            f'<div class="actions"><a class="btn btn-gold" href="https://train.strivee.app/payment/{sid}" target="_blank" rel="noopener" '
            f'data-program="{escape(pname)}" data-value="{czk}">{btn}</a>'
            f'<a class="btn btn-ghost" href="https://train.strivee.app/program/{sid}" target="_blank" rel="noopener">{u["details"]}</a></div></article>')


def faq_html(lang, faq):
    u = T[lang]["ui"]
    items = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faq)
    return f'''<section id="faq">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">FAQ</p><h2 class="display"><span>{u["faq_h"][0]} <span class="gold">{u["faq_h"][1]}</span></span></h2></div>
    <div class="faq">{items}</div>
  </div>
</section>'''


def shead(eyebrow, h2):
    return f'<div class="shead"><p class="eyebrow">{escape(eyebrow)}</p><h2 class="display"><span>{h2}</span></h2></div>'


def ul(items):
    return '<ul class="lp-list">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def schema(lang, kind, url, d):
    u = T[lang]["ui"]
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "STR2G HYROX", "item": BASE + HOME[lang]},
        {"@type": "ListItem", "position": 2, "name": u["plan_link"] if kind == "plan" else u["coach_link"], "item": url}]}
    area = [{"@type": "Country", "name": c} for c in COUNTRY[lang]]
    if kind == "plan":
        offers = {"@type": "AggregateOffer", "priceCurrency": "CZK", "lowPrice": "550", "highPrice": "3500", "offerCount": "9",
                  "url": BASE + HOME[lang] + "#programs"}
        stype = u["plan_link"]
    else:
        offers = {"@type": "Offer", "price": "3500", "priceCurrency": "CZK", "availability": "https://schema.org/InStock",
                  "url": "https://train.strivee.app/program/" + PROGRAMS["coaching"][0],
                  "priceSpecification": {"@type": "UnitPriceSpecification", "price": "3500", "priceCurrency": "CZK", "billingDuration": "P1M"}}
        stype = u["coach_link"]
    graph = [
        {"@type": "WebPage", "@id": url, "url": url, "name": d["title"], "description": d["desc"], "inLanguage": lang,
         "isPartOf": {"@id": BASE + "/#web"}, "about": {"@id": url + "#service"}},
        {"@type": "Service", "@id": url + "#service", "name": stype, "serviceType": stype, "description": d["desc"],
         "provider": {"@id": BASE + "/#org"}, "areaServed": area, "availableChannel": {"@type": "ServiceChannel", "serviceUrl": url},
         "offers": offers},
        crumbs,
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def page(lang, kind, parts):
    tracking, style, fonts, verify, icons = parts
    d = T[lang][kind]
    u = T[lang]["ui"]
    url = BASE + SLUGS[kind][lang]
    other = "coach" if kind == "plan" else "plan"
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{SLUGS[kind][l]}">' for l in ORDER) + \
        f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{SLUGS[kind]["en"]}">'
    langnav = "".join(
        f'<a href="{SLUGS[kind][l]}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{LANG_LABEL[l]}</a>' for l in ORDER)
    home = HOME[lang]

    head = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(d["title"])}</title>
<meta name="description" content="{escape(d["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#050505">
{verify}
<link rel="canonical" href="{url}">
{alts}
<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:site_name" content="STR2G HYROX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escape(d["title"])}">
<meta property="og:description" content="{escape(d["desc"])}">
<meta property="og:image" content="{BASE}/img/lada-ria-finish-line.jpg">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">{schema(lang, kind, url, d)}</script>
<style>{style}{EXTRA_CSS}</style>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="{home}" aria-label="STR2G HYROX"><img class="mark" src="/favicon.svg?v=2" alt="" width="34" height="34"><b>STR<span class="gold">2</span>G</b><small>{escape(u["plan_link"] if kind == "plan" else u["coach_link"])}</small></a>
    <div class="navlinks">
      <a class="txt" href="{home}#programs">{u["programs"]}</a>
      <a class="txt" href="{SLUGS[other][lang]}">{escape(u["coach_link"] if kind == "plan" else u["plan_link"])}</a>
      <nav class="lang" aria-label="{u["lang"]}">{langnav}</nav>
      <a class="btn btn-gold" href="#pick">{u["start"]}</a>
    </div>
  </div>
</nav>

<header class="hero lp-hero" id="top">
  <img class="hero-img" src="/img/lada-ria-finish-line.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">STR2G HYROX</a><span aria-hidden="true">/</span><span>{escape(u["plan_link"] if kind == "plan" else u["coach_link"])}</span></nav>
    <p class="eyebrow">{escape(d["eyebrow"])}</p>
    <h1 class="display">{escape(d["h1"][0])}<br><span class="gold">{escape(d["h1"][1])}</span></h1>
    <p class="lead">{escape(d["lead"])}</p>
    <div class="cta-row">
      <a class="btn btn-gold" href="#pick">{u["start"]}</a>
      <a class="btn btn-ghost" href="{SLUGS[other][lang]}">{escape(u["coach_link"] if kind == "plan" else u["plan_link"])}</a>
    </div>
  </div>
</header>
'''
    if kind == "plan":
        rows = "".join(f"<tr><td>{a}</td><td>{escape(b)}</td><td>{escape(c)}</td></tr>" for a, b, c in d["week"])
        phases = "".join(f'<div class="phase"><small>{escape(w)}</small><h3>{escape(n)}</h3><p>{escape(t)}</p></div>' for w, n, t in d["phases"])
        cards = "".join(card(lang, p, T[lang]["picks"][p]) for p in PLAN_PICKS)
        body = f'''
<section id="approach">
  <div class="wrap">
    {shead(u["plan_link"], escape(d["s1_h"]))}
    <p class="lp-p">{escape(d["s1_p"])}</p>
    {ul(d["s1_ul"])}
  </div>
</section>

<section id="week">
  <div class="wrap">
    {shead(u["plan_link"], escape(d["week_h"]))}
    <p class="lp-p">{escape(d["week_p"])}</p>
    <table class="lp-table"><thead><tr><th>{d["week_cols"][0]}</th><th>{d["week_cols"][1]}</th><th>{d["week_cols"][2]}</th></tr></thead><tbody>{rows}</tbody></table>
  </div>
</section>

<section id="phases">
  <div class="wrap">
    {shead("12", escape(d["phases_h"]))}
    <div class="phases">{phases}</div>
    <p class="lp-p">{escape(d["phases_p"])}</p>
  </div>
</section>

<section id="pick">
  <div class="wrap">
    {shead(u["programs"], escape(d["pick_h"]))}
    <div class="grid">{cards}</div>
    <p class="lp-note">{escape(u["pay_note"])} <a href="{home}#programs">{escape(u["all_programs"])} →</a></p>
  </div>
</section>

<section id="mistakes">
  <div class="wrap">
    {shead("HYROX", escape(d["mistakes_h"]))}
    {ul([escape(m) for m in d["mistakes"]])}
  </div>
</section>
'''
    else:
        how = "".join(f"<li>{escape(x)}</li>" for x in d["how"])
        body = f'''
<section id="pick">
  <div class="wrap">
    {shead(u["coach_link"], escape(d["get_h"]))}
    {ul([escape(x) for x in d["get"]])}
    <div class="grid lp-offer">{card(lang, "coaching", "1:1")}</div>
    <p class="lp-note">{escape(u["pay_note"])}</p>
  </div>
</section>

<section id="how">
  <div class="wrap">
    {shead("1:1", escape(d["how_h"]))}
    <ol class="lp-steps">{how}</ol>
  </div>
</section>

<section id="vs">
  <div class="wrap">
    {shead(u["programs"], escape(d["vs_h"]))}
    <p class="lp-p">{escape(d["vs_p"])} <a href="{SLUGS["plan"][lang]}#pick">{escape(d["vs_link"])} →</a></p>
  </div>
</section>

<section id="coaches">
  <div class="wrap">
    {shead("STR2G", escape(d["coaches_h"]))}
    <p class="lp-p">{d["lada"]}</p>
    <p class="lp-p">{d["ria"]}</p>
    <p class="lp-p">{escape(d["raced"])}</p>
    <figure class="lp-quote"><blockquote>{escape(d["quote"])}</blockquote><figcaption>{escape(d["quote_who"])}</figcaption></figure>
  </div>
</section>
'''
    net = "".join(f'<li><a href="{h}" target="_blank" rel="noopener"><b>{escape(t)}</b></a></li>' for h, t in NET[lang])
    tail = f'''
{faq_html(lang, d["faq"])}

<section class="final">
  <img class="bgimg" src="/img/lada-ria-finish-line.webp" alt="" loading="lazy">
  <div class="wrap">
    <h2 class="display">{escape(u["cta"][0])}<br><span class="gold">{escape(u["cta"][1])}</span></h2>
    <p class="lead">{escape(u["cta_lead"])}</p>
    <div class="cta-row">
      <a class="btn btn-gold" href="#pick">{u["start"]}</a>
      <a class="btn btn-ghost" href="{home}#programs">{escape(u["cta_btn"])}</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <nav class="guides" aria-label="Guides"><a href="{SLUGS["plan"][lang]}"{" aria-current=\"page\"" if kind == "plan" else ""}>{escape(u["plan_link"])}</a><a href="{SLUGS["coach"][lang]}"{" aria-current=\"page\"" if kind == "coach" else ""}>{escape(u["coach_link"])}</a><a href="{home}#programs">{u["programs"]}</a></nav>
    <nav class="net" aria-label="STR2G"><p class="net-h">STR2G</p><ul>{net}</ul></nav>
    <div style="display:flex;align-items:center;gap:12px"><img loading="lazy" src="/favicon.svg?v=2" alt="" width="26" height="26" style="border:1px solid var(--line);border-radius:6px"><span>© 2026 STR2G · Stronger Together · Strivee</span></div>
    <div class="links">
      <a href="https://instagram.com/22segge_coach" target="_blank" rel="noopener">@22segge_coach</a>
      <a href="https://instagram.com/riahrusovskaofficial" target="_blank" rel="noopener">@riahrusovskaofficial</a>
      <a href="#" onclick="str2gConsentReset();return false;">Cookies</a>
    </div>
  </div>
</footer>
</body>
</html>
'''
    return head + body + tail


def build(root):
    src = (root / "index.html").read_text(encoding="utf-8")
    parts = extract(src)
    urls = []
    for kind in ("plan", "coach"):
        for lang in ORDER:
            path = SLUGS[kind][lang]
            out = root / path.strip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page(lang, kind, parts), encoding="utf-8")
            urls.append((kind, lang))
    print(f"landing pages: {len(urls)} written")
    return urls
