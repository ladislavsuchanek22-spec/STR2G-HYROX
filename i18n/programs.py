"""Generátor samostatných stránek programů (/programs/<program>/ a /cs/programy/<program>/).

Volá ho i18n/build.py. Obsah je v i18n/programs_content.py, ceny a Strivee ID v i18n/pages_content.py (PROGRAMS).
Styly, fonty a měřicí skript se berou z index.html stejně jako u landing pages (i18n/pages.py).
"""
import json
from html import escape
from pathlib import Path

from pages_content import PROGRAMS, HOME, LOCALE, price
from programs_content import PT, PSLUGS, PDATA, PROG_LANGS, PROG_ORDER
import pages

BASE = "https://str2g.com"
LANG_LABEL = {"en": "EN", "cs": "CZ"}

PROG_CSS = """
.lp-hero h1{font-size:clamp(52px,7.6vw,112px);hyphens:manual;overflow-wrap:normal}
@media (max-width:620px){.buybox .cta-row{width:100%}.buybox .cta-row .btn{flex:1 1 100%}}
.facts{display:grid;grid-template-columns:repeat(var(--cols,5),minmax(0,1fr));border-block:1px solid var(--line);margin-top:34px;max-width:980px}
.facts div{padding:14px 14px 14px 0;font-family:var(--mono);font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;line-height:1.35}
.facts div+div{padding-left:14px;border-left:1px solid var(--line)}
.facts strong{display:block;font-family:var(--display);font-style:italic;font-weight:800;font-size:30px;color:var(--fg);letter-spacing:0;line-height:1.05;margin-bottom:4px}
.facts .lvl strong{font-size:22px;line-height:1.1}
.fitgrid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:start}
.notfit{background:var(--panel);border:1px solid var(--line);padding:24px}
.notfit h3{font-family:var(--display);font-style:italic;font-weight:800;text-transform:uppercase;font-size:26px;margin:0 0 14px;line-height:1}
.notfit ul{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.notfit li{font-size:15.5px;line-height:1.5;color:var(--muted)}
.notfit a{display:inline-block;margin-top:4px;color:var(--accent);font-weight:500;text-decoration:none}
.notfit a:hover{text-decoration:underline}
.app{margin-top:28px;max-width:820px;border-top:1px solid var(--line);padding-top:22px}
.app h3{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:500;margin:0 0 12px}
.buybox{display:flex;flex-wrap:wrap;align-items:flex-end;gap:18px 32px;margin-top:30px}
.prog-nav{display:flex;flex-wrap:wrap;gap:8px 20px}
.prog-nav a{color:var(--fg);text-decoration:none;font-weight:500}.prog-nav a:hover,.prog-nav a[aria-current]{color:var(--accent)}
@media (max-width:980px){.facts{grid-template-columns:repeat(3,minmax(0,1fr))}.facts div:nth-child(3n+1){padding-left:0;border-left:0}.facts div:nth-child(n+4){border-top:1px solid var(--line)}.fitgrid{grid-template-columns:1fr;gap:28px}}
@media (max-width:620px){.facts{grid-template-columns:repeat(2,minmax(0,1fr))}.facts div:nth-child(odd){padding-left:0;border-left:0}.facts div:nth-child(even){padding-left:14px;border-left:1px solid var(--line)}.facts div:nth-child(n+3){border-top:1px solid var(--line)}.facts strong{font-size:26px}}
"""


def url_of(pid, lang):
    return PSLUGS[pid][lang]


def price_parts(lang, pid):
    sid, czk, monthly, _ = PROGRAMS[pid]
    main, fx = price(lang, czk)
    u = PT[lang]["ui"]
    period = u["monthly"] if monthly else (u["per_athlete"] if pid == "doubles" else u["one_time"])
    return main, period, fx


def price_html(lang, pid):
    main, period, fx = price_parts(lang, pid)
    fx_html = f'<em class="fx">{fx}</em>' if fx else ""
    return f'<div class="price"><b>{main}</b><span>{escape(period)}</span>{fx_html}</div>'


def buy_btn(lang, pid, cls="btn btn-gold"):
    sid, czk, monthly, pname = PROGRAMS[pid]
    u = PT[lang]["ui"]
    return (f'<a class="{cls}" href="https://train.strivee.app/payment/{sid}" target="_blank" rel="noopener" '
            f'data-program="{escape(pname)}" data-value="{czk}">{u["start"] if monthly else u["buy"]}</a>')


def related_card(lang, pid):
    u = PT[lang]["ui"]
    if pid == "coaching":
        sid, czk, monthly, pname = PROGRAMS["coaching"]
        main, fx = price(lang, czk)
        fx_html = f'<em class="fx">{fx}</em>' if fx else ""
        return (f'<article class="card"><div class="kind">{escape(u["coaching_kind"])}</div><h4>{escape(u["coaching_name"])}</h4>'
                f'<div class="price"><b>{main}</b><span>{escape(u["monthly"])}</span>{fx_html}</div>'
                f'<div class="actions"><a class="btn btn-ghost" href="{u["coaching_url"]}">{escape(u["see"])}</a></div></article>')
    p = PT[lang]["programs"][pid]
    return (f'<article class="card"><div class="kind">{escape(p["kind"])}</div><h4>{escape(p["name"])}</h4>{price_html(lang, pid)}'
            f'<p class="for">{escape(p["fit"][0])}</p>'
            f'<div class="actions"><a class="btn btn-ghost" href="{url_of(pid, lang)}">{escape(u["see"])}</a>{buy_btn(lang, pid)}</div></article>')


def link_to(lang, pid):
    """Odkaz z boxu 'Nesedí ti to' na jiný program."""
    u = PT[lang]["ui"]
    if pid == "coaching":
        return f'<a href="{u["coaching_url"]}">{escape(u["coaching_name"])} →</a>'
    return f'<a href="{url_of(pid, lang)}">{escape(PT[lang]["programs"][pid]["name"])} →</a>'


def schema(lang, pid, url, p, faq):
    sid, czk, monthly, pname = PROGRAMS[pid]
    u = PT[lang]["ui"]
    home = BASE + HOME[lang]
    offer = {"@type": "Offer", "price": str(czk), "priceCurrency": "CZK", "availability": "https://schema.org/InStock",
             "url": f"https://train.strivee.app/payment/{sid}", "seller": {"@id": BASE + "/#org"}}
    if monthly:
        offer["priceSpecification"] = {"@type": "UnitPriceSpecification", "price": str(czk), "priceCurrency": "CZK", "billingDuration": "P1M"}
    graph = [
        {"@type": "WebPage", "@id": url, "url": url, "name": p["title"], "description": p["desc"], "inLanguage": lang,
         "isPartOf": {"@id": BASE + "/#web"}, "about": {"@id": url + "#product"}},
        {"@type": "Product", "@id": url + "#product", "name": f"STR2G {pname}", "description": p["desc"],
         "brand": {"@type": "Brand", "name": "STR2G"}, "category": "Online HYROX training program",
         "image": f"{BASE}/img/{PDATA[pid]['img']}.jpg", "offers": offer},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "STR2G HYROX", "item": home},
            {"@type": "ListItem", "position": 2, "name": u["crumb_programs"], "item": home + "#programs"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def two(h):
    """('Who it's', 'for.') -> nadpis s druhou částí zlatě"""
    return f'{escape(h[0])} <span class="gold">{escape(h[1])}</span>'


def footer_programs(lang, current=None):
    """Řádek odkazů na všechny programy (patička programů, plánu i 1:1 stránky)."""
    links = "".join(
        f'<a href="{url_of(pid, lang)}"{" aria-current=\"page\"" if pid == current else ""}>{escape(PT[lang]["programs"][pid]["name"])}</a>'
        for pid in PROG_ORDER)
    return f'<nav class="prog-nav guides" aria-label="{escape(PT[lang]["ui"]["programs"])}">{links}</nav>'


def page(lang, pid, parts):
    tracking, style, fonts, verify, icons = parts
    u = PT[lang]["ui"]
    p = PT[lang]["programs"][pid]
    d = PDATA[pid]
    url = BASE + url_of(pid, lang)
    home = HOME[lang]
    faq = p["faq"] + u.get("extra_faq", [])
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{url_of(pid, l)}">' for l in PROG_LANGS) + \
        f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{url_of(pid, "en")}">'
    langnav = "".join(
        f'<a href="{url_of(pid, l)}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{LANG_LABEL[l]}</a>' for l in PROG_LANGS)
    img = d["img"]
    main, period, fx = price_parts(lang, pid)

    facts = [f'<div><strong>{d["days"]}</strong>{escape(u["f_days"])}</div>',
             f'<div><strong>{d["mins"]}</strong>{escape(u["f_mins"])}</div>',
             f'<div><strong>{d["sess"]}</strong>{escape(u["f_sess"])}</div>']
    if d["weeks"]:
        facts.append(f'<div><strong>{d["weeks"]}</strong>{escape(u["f_weeks"])}</div>')
    facts.append(f'<div class="lvl"><strong>{escape(p["level"])}</strong>{escape(u["f_level"])}</div>')
    facts_html = f'<div class="facts" style="--cols:{len(facts)}">' + "".join(facts) + "</div>"

    head = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(p["title"])}</title>
<meta name="description" content="{escape(p["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#050505">
{verify}
<link rel="canonical" href="{url}">
{alts}
<meta property="og:type" content="product">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:site_name" content="STR2G HYROX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escape(p["title"])}">
<meta property="og:description" content="{escape(p["desc"])}">
<meta property="og:image" content="{BASE}/img/{img}.jpg">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">{schema(lang, pid, url, p, faq)}</script>
<style>{style}{pages.EXTRA_CSS}{PROG_CSS}</style>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="{home}" aria-label="STR2G HYROX"><img class="mark" src="/favicon.svg?v=2" alt="" width="34" height="34"><b>STR<span class="gold">2</span>G</b><small>{escape(p["name"])}</small></a>
    <div class="navlinks">
      <a class="txt" href="{home}#programs">{u["programs"]}</a>
      <a class="txt" href="{u["plan_url"]}">{escape(u["plan_link"])}</a>
      <nav class="lang" aria-label="{u["lang"]}">{langnav}</nav>
      {buy_btn(lang, pid)}
    </div>
  </div>
</nav>

<header class="hero lp-hero" id="top">
  <img class="hero-img" src="/img/{img}.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">STR2G HYROX</a><span aria-hidden="true">/</span><a href="{home}#programs">{escape(u["crumb_programs"])}</a><span aria-hidden="true">/</span><span>{escape(p["name"])}</span></nav>
    <p class="eyebrow">{escape(p["kind"])}</p>
    <h1 class="display">{escape(p["h1"][0])}<br><span class="gold">{escape(p["h1"][1])}</span></h1>
    <p class="lead">{escape(p["lead"])}</p>
    <div class="buybox">
      {price_html(lang, pid)}
      <div class="cta-row" style="margin-top:0">
        {buy_btn(lang, pid)}
        <a class="btn btn-ghost" href="{u["plan_url"]}#pick">{escape(u["compare"])}</a>
      </div>
    </div>
    {facts_html}
  </div>
</header>
'''
    fit = "".join(f"<li>{escape(x)}</li>" for x in p["fit"])
    notfit = "".join(f"<li>{escape(t)}<br>{link_to(lang, alt)}</li>" for t, alt in p["notfit"])
    inside = "".join(f"<li>{escape(x)}</li>" for x in p["inside"])
    app = "".join(f"<li>{escape(x)}</li>" for x in u["app"])
    rows = "".join(f"<tr><td>{escape(a)}</td><td>{escape(b)}</td><td>{escape(c)}</td></tr>" for a, b, c in p["week"])
    week_h = p.get("week_h", u["week_h"])
    week_note = p.get("week_note", u["week_note"])

    body = f'''
<section id="fit">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(p["name"])}</p><h2 class="display"><span class="num">01</span><span>{two(u["fit_h"])}</span></h2></div>
    <div class="fitgrid">
      <ul class="lp-list">{fit}</ul>
      <aside class="notfit"><h3>{escape(u["notfit_h"])}</h3><ul>{notfit}</ul></aside>
    </div>
  </div>
</section>

<section id="inside">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(p["name"])}</p><h2 class="display"><span class="num">02</span><span>{two(u["inside_h"])}</span></h2></div>
    <ul class="lp-list">{inside}</ul>
    <div class="app"><h3>{escape(u["app_h"])}</h3><ul class="lp-list">{app}</ul></div>
  </div>
</section>

<section id="week">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(p["name"])}</p><h2 class="display"><span class="num">03</span><span>{two(week_h)}</span></h2></div>
    <table class="lp-table"><thead><tr><th>{u["week_cols"][0]}</th><th>{u["week_cols"][1]}</th><th>{u["week_cols"][2]}</th></tr></thead><tbody>{rows}</tbody></table>
    <p class="lp-note">{escape(week_note)}</p>
  </div>
</section>
'''
    body += f'''
<section id="coaches">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">STR2G</p><h2 class="display"><span>{two(u["coaches_h"])}</span></h2></div>
    <p class="lp-p">{u["lada"]}</p>
    <p class="lp-p">{u["ria"]}</p>
    <p class="lp-p">{escape(u["raced"])}</p>
  </div>
</section>
'''
    faq_items = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faq)
    related = "".join(related_card(lang, r) for r in d["related"])
    net = "".join(f'<li><a href="{h}" target="_blank" rel="noopener"><b>{escape(t)}</b></a></li>' for h, t in pages.NET[lang])
    tail = f'''
<section id="faq">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">FAQ</p><h2 class="display"><span>{two(u["faq_h"])}</span></h2></div>
    <div class="faq">{faq_items}</div>
  </div>
</section>

<section id="related">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(u["programs"])}</p><h2 class="display"><span>{two(u["related_h"])}</span></h2></div>
    <div class="grid">{related}</div>
    <p class="lp-note">{escape(u["pay_note"])} <a href="{u["plan_url"]}#pick">{escape(u["compare"])} →</a></p>
  </div>
</section>

<section class="final">
  <img class="bgimg" src="/img/{img}.webp" alt="" loading="lazy">
  <div class="wrap">
    <h2 class="display">{escape(u["cta"][0])}<br><span class="gold">{escape(u["cta"][1])}</span></h2>
    <p class="lead">{escape(u["cta_lead"])}</p>
    <div class="cta-row">
      {buy_btn(lang, pid)}
      <a class="btn btn-ghost" href="{u["plan_url"]}#pick">{escape(u["compare"])}</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    {footer_programs(lang, pid)}
    <nav class="guides" aria-label="Guides"><a href="{u["plan_url"]}">{escape(u["plan_link"])}</a><a href="{u["coaching_url"]}">{escape(u["coach_link"])}</a><a href="{home}#programs">{u["programs"]}</a></nav>
    <nav class="net" aria-label="STR2G"><p class="net-h">STR2G</p><ul>{net}</ul></nav>
    <div style="display:flex;align-items:center;gap:12px"><img loading="lazy" src="/favicon.svg?v=2" alt="" width="26" height="26" style="border:1px solid var(--line);border-radius:6px"><span>© 2026 STR2G · Stronger Together · Strivee</span></div>
    <div class="links">
      <a href="https://instagram.com/22segge_coach" target="_blank" rel="noopener">@22segge_coach</a>
      <a href="https://instagram.com/riahrusovskaofficial" target="_blank" rel="noopener">@riahrusovskaofficial</a>
      <a href="{"/cs/ochrana-osobnich-udaju/" if lang == "cs" else "/privacy/"}">{pages.PRIV_LBL[lang]}</a>
      <a href="#" onclick="str2gConsentReset();return false;">Cookies</a>
    </div>
  </div>
</footer>
</body>
</html>
'''
    html = head + body + tail
    nl = (Path(__file__).resolve().parent / "newsletter.html").read_text(encoding="utf-8").rstrip("\n")
    return html.replace("</body>", nl + "\n</body>", 1)


def build(root, parts):
    n = 0
    for pid in PROG_ORDER:
        for lang in PROG_LANGS:
            out = root / url_of(pid, lang).strip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page(lang, pid, parts), encoding="utf-8")
            n += 1
    print(f"program pages: {n} written")
