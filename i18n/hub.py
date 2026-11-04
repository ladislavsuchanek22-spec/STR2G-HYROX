"""Rozcestník všech programů: /programs/ (EN) a /cs/programy/ (CS).

Cílí na dotazy „HYROX training programs“ / „HYROX tréninkové programy“.
Fakta (cena, dny, minuty, týdny, úroveň) bere z pages_content.PROGRAMS a programs_content (PT, PDATA),
takže se po změně ceny nebo programu přepíše sama. Volá ji i18n/build.py.
"""
import json
from html import escape

from pages_content import PROGRAMS, HOME, LOCALE, price
from programs_content import PT, PDATA, PROG_ORDER
import pages
import programs as P

BASE = "https://str2g.com"
HUB = {"en": "/programs/", "cs": "/cs/programy/"}
HUB_LANGS = ["en", "cs"]

HUB_CSS = """
.cmp-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%}
.cmp{min-width:820px;max-width:1180px}
.cmp td{overflow-wrap:normal}
.cmp td:first-child{width:auto;min-width:230px;font-size:20px;line-height:1.1}
.cmp td:first-child small{font-family:var(--body,inherit);font-style:normal;font-weight:400;text-transform:none;font-size:12.5px}
.cmp td:last-child{white-space:nowrap}
.cmp td:first-child a{color:var(--fg);font-weight:600;text-decoration:none}.cmp td:first-child a:hover{color:var(--accent)}
.cmp td small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.pick{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 40px;max-width:1080px}
.pick li{border-top:1px solid var(--line);padding:16px 0;font-size:16px;line-height:1.5;color:var(--muted)}
.pick li b{display:block;color:var(--fg);font-weight:500;margin-bottom:2px}
.pick a{color:var(--accent);font-weight:500;text-decoration:none}.pick a:hover{text-decoration:underline}
@media (max-width:760px){.pick{grid-template-columns:1fr}}
"""

H = {}
H["en"] = dict(
    title="HYROX Training Programs: Compare All Online Plans | STR2G",
    desc="Compare every STR2G HYROX training program: beginner, 12-week race prep, singles, doubles, running and taper. Days per week, session length, price and who each one is for.",
    crumb="HYROX training programs", eyebrow="9 programs · 1:1 coaching · Strivee app",
    h1=("HYROX training", "programs."),
    lead="Nine online HYROX programs and 1:1 coaching from two coaches who race. Pick by your race date and level, not by which plan looks the hardest.",
    pick_h=("Pick in", "30 seconds."),
    pick=[("No race booked yet, or you're new to HYROX", "basic"),
          ("Your first HYROX is about 12 weeks away", "advanced"),
          ("Race in about 12 weeks and you have a training base", "raceprep"),
          ("Race in about 8 weeks, racing Singles", "singles"),
          ("Race in about 8 weeks, racing Doubles", "doubles"),
          ("You lose places on the runs, not on the stations", "running"),
          ("Your race is two weeks away", "taper"),
          ("You race regularly and want a faster time", "competitor"),
          ("You've raced a few times and want our top monthly tier", "pro"),
          ("You want a plan written only for you", "coaching")],
    cmp_h=("Side by", "side."),
    cols=("Program", "Length", "Days / week", "Min / day", "Level", "Price"),
    monthly_len="Ongoing, monthly", weeks="{} weeks",
    all_h=("All", "programs."),
    same_h=("What every program", "has in common."),
    same=["HYROX is not a random workout. Every week is planned around running, strength, the eight stations and the transitions between them.",
          "Work under fatigue: running after stations, stations after running. That's where races are won and lost.",
          "Pacing and race tactics, not just hard sessions. You learn what pace you can actually hold.",
          "Loads and volume you can scale to your level, so you finish sessions with quality instead of just surviving them.",
          "Written by Láďa and Ria, who coach HYROX clubs in Prague, Brno and Ostrava and race HYROX themselves."],
    faq=[("Which HYROX training program is best for beginners?",
          "HYROX Basic if you don't have a race date yet. If your first race is about 12 weeks away, take the 12-Week HYROX Advanced: it's a full race build that works for all levels."),
         ("How long should a HYROX training program be?",
          "For a specific race, 8 to 12 weeks of focused preparation is the usual range if you already train regularly. If you're starting from zero, give yourself longer and begin with a monthly program like HYROX Basic."),
         ("Is there a HYROX Doubles training program?",
          "Yes. The 8-Week HYROX Doubles program is built for pairs, including how to split the stations. The price is per athlete."),
         ("How do I get the program?",
          "You buy the program through Strivee and every session appears in the Strivee app on your phone. Payment runs in Czech koruna (CZK), your bank converts it."),
         ("Can I get a plan written just for me?",
          "Yes. HYROX 1:1 coaching is a plan built only for you, adjusted to your schedule, your race and your results.")],
    cta=("Pick a plan.", "Start tomorrow."),
)
H["cs"] = dict(
    title="HYROX tréninkové programy: srovnání všech plánů | STR2G",
    desc="Srovnání všech HYROX tréninkových programů STR2G: pro začátečníky, 12týdenní příprava, singles, doubles, běh a taper. Dny v týdnu, délka tréninku, cena a pro koho je.",
    crumb="HYROX tréninkové programy", eyebrow="9 programů · individuální koučink · aplikace Strivee",
    h1=("HYROX tréninkové", "programy."),
    lead="Devět online HYROX programů a individuální koučink od dvou trenérů, kteří sami závodí. Vybírej podle data závodu a úrovně, ne podle toho, který plán vypadá nejtěžší.",
    pick_h=("Vyber za", "30 vteřin."),
    pick=[("Závod ještě nemáš, nebo s HYROXem začínáš", "basic"),
          ("První HYROX máš zhruba za 12 týdnů", "advanced"),
          ("Závod máš zhruba za 12 týdnů a máš tréninkový základ", "raceprep"),
          ("Závod máš zhruba za 8 týdnů, jdeš Singles", "singles"),
          ("Závod máš zhruba za 8 týdnů, jdete Doubles", "doubles"),
          ("Místa ztrácíš na běhu, ne na stanicích", "running"),
          ("Závod máš za dva týdny", "taper"),
          ("Závodíš pravidelně a chceš lepší čas", "competitor"),
          ("HYROX máš párkrát za sebou a chceš naši nejvyšší úroveň", "pro"),
          ("Chceš plán napsaný jen pro sebe", "coaching")],
    cmp_h=("Srovnání", "vedle sebe."),
    cols=("Program", "Délka", "Dny v týdnu", "Min denně", "Úroveň", "Cena"),
    monthly_len="Průběžně, měsíčně", weeks="{} týdnů",
    all_h=("Všechny", "programy."),
    same_h=("Co mají všechny", "programy společné."),
    same=["HYROX není náhodný workout. Každý týden má strukturu: běh, síla, osm stanic a přechody mezi nimi.",
          "Práce pod únavou: běh po stanici, stanice po běhu. Tam se závod vyhrává i prohrává.",
          "Tempo a taktika, ne jen těžké tréninky. Naučíš se, jaké tempo opravdu udržíš.",
          "Váhy a objem si upravíš na svou úroveň, takže tréninky dokončuješ kvalitně, ne jen přežiješ.",
          "Píšou je Láďa a Ria, kteří vedou HYROX kluby v Praze, Brně a Ostravě a sami HYROX závodí."],
    faq=[("Který HYROX tréninkový program je nejlepší pro začátečníky?",
          "HYROX Basic, pokud ještě nemáš datum závodu. Když máš první závod zhruba za 12 týdnů, vezmi 12týdenní HYROX Advanced: je to kompletní příprava na závod pro všechny úrovně."),
         ("Jak dlouhá má být příprava na HYROX?",
          "Na konkrétní závod obvykle 8 až 12 týdnů cílené přípravy, pokud už pravidelně trénuješ. Když začínáš od nuly, dej si víc času a začni měsíčním programem, třeba HYROX Basic."),
         ("Máte tréninkový program na HYROX Doubles?",
          "Ano. 8týdenní HYROX Doubles je postavený pro dvojice, včetně toho, jak si rozdělit stanice. Cena je za jednoho závodníka."),
         ("Jak program dostanu?",
          "Program koupíš přes Strivee a všechny tréninky se ti objeví v aplikaci Strivee v mobilu. Platí se v korunách."),
         ("Můžu mít plán napsaný jen pro sebe?",
          "Ano. Individuální HYROX koučink je plán postavený jen pro tebe, podle tvého času, závodu a výsledků.")],
    cta=("Vyber plán.", "Začni zítra."),
)


def _len(lang, pid):
    w = PDATA[pid]["weeks"]
    return H[lang]["monthly_len"] if w is None else H[lang]["weeks"].format(w)


def _price_cell(lang, pid):
    main, period, fx = P.price_parts(lang, pid)
    return f'{main}<small>{escape(period)}{" · " + escape(fx) if fx else ""}</small>'


def _name(lang, pid):
    if pid == "coaching":
        return PT[lang]["ui"]["coaching_name"]
    return PT[lang]["programs"][pid]["name"]


def _url(lang, pid):
    return PT[lang]["ui"]["coaching_url"] if pid == "coaching" else P.url_of(pid, lang)


def schema(lang, url, h, faq):
    home = BASE + HOME[lang]
    items = []
    for i, pid in enumerate(PROG_ORDER + ["coaching"], 1):
        sid, czk, monthly, pname = PROGRAMS[pid]
        items.append({"@type": "ListItem", "position": i, "url": BASE + _url(lang, pid), "name": _name(lang, pid)})
    graph = [
        {"@type": "CollectionPage", "@id": url, "url": url, "name": h["title"], "description": h["desc"], "inLanguage": lang,
         "isPartOf": {"@id": BASE + "/#web"}, "mainEntity": {"@id": url + "#list"}},
        {"@type": "ItemList", "@id": url + "#list", "name": h["crumb"], "numberOfItems": len(items), "itemListElement": items},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "STR2G HYROX", "item": home},
            {"@type": "ListItem", "position": 2, "name": h["crumb"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def page(lang, parts):
    tracking, style, fonts, verify, icons = parts
    h = H[lang]
    u = PT[lang]["ui"]
    home = HOME[lang]
    url = BASE + HUB[lang]
    faq = h["faq"] + u.get("extra_faq", [])
    img = "lada-ria-finish-line"
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{HUB[l]}">' for l in HUB_LANGS) + \
        f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{HUB["en"]}">'
    langnav = "".join(
        f'<a href="{HUB[l]}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{P.LANG_LABEL[l]}</a>' for l in HUB_LANGS)

    pick = "".join(f'<li><b>{escape(t)}</b><a href="{_url(lang, pid)}">{escape(_name(lang, pid))} →</a></li>' for t, pid in h["pick"])
    rows = ""
    for pid in PROG_ORDER:
        d = PDATA[pid]
        p = PT[lang]["programs"][pid]
        rows += (f'<tr><td><a href="{_url(lang, pid)}">{escape(p["name"])}</a><small>{escape(p["kind"])}</small></td>'
                 f'<td>{escape(_len(lang, pid))}</td><td>{d["days"]}</td><td>{d["mins"]}{" · " + str(d["sess"]) + "×" if d["sess"] > 1 else ""}</td>'
                 f'<td>{escape(p["level"])}</td><td>{_price_cell(lang, pid)}</td></tr>')
    rows += (f'<tr><td><a href="{_url(lang, "coaching")}">{escape(u["coaching_name"])}</a><small>{escape(u["coaching_kind"])}</small></td>'
             f'<td>{escape(h["monthly_len"])}</td><td>–</td><td>–</td><td>–</td><td>{_price_cell(lang, "coaching")}</td></tr>')
    cols = "".join(f"<th>{escape(c)}</th>" for c in h["cols"])
    cards = "".join(P.related_card(lang, pid) for pid in PROG_ORDER + ["coaching"])
    same = "".join(f"<li>{escape(x)}</li>" for x in h["same"])
    app = "".join(f"<li>{escape(x)}</li>" for x in u["app"])
    faq_items = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faq)
    net = "".join(f'<li><a href="{x}" target="_blank" rel="noopener"><b>{escape(t)}</b></a></li>' for x, t in pages.NET[lang])
    guides_nav = __import__("guides").nav(lang)

    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(h["title"])}</title>
<meta name="description" content="{escape(h["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#050505">
{verify}
<link rel="canonical" href="{url}">
{alts}
<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:site_name" content="STR2G HYROX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escape(h["title"])}">
<meta property="og:description" content="{escape(h["desc"])}">
<meta property="og:image" content="{BASE}/img/{img}.jpg">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">{schema(lang, url, h, faq)}</script>
<style>{style}{pages.EXTRA_CSS}{P.PROG_CSS}{HUB_CSS}</style>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="{home}" aria-label="STR2G HYROX"><img class="mark" src="/favicon.svg?v=2" alt="" width="34" height="34"><b>STR<span class="gold">2</span>G</b><small>{escape(u["programs"])}</small></a>
    <div class="navlinks">
      <a class="txt" href="{u["plan_url"]}">{escape(u["plan_link"])}</a>
      <a class="txt" href="{u["coaching_url"]}">{escape(u["coach_link"])}</a>
      <nav class="lang" aria-label="{u["lang"]}">{langnav}</nav>
      <a class="btn btn-gold" href="#all">{escape(u["programs"])}</a>
    </div>
  </div>
</nav>

<header class="hero lp-hero" id="top">
  <img class="hero-img" src="/img/{img}.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">STR2G HYROX</a><span aria-hidden="true">/</span><span>{escape(h["crumb"])}</span></nav>
    <p class="eyebrow">{escape(h["eyebrow"])}</p>
    <h1 class="display">{escape(h["h1"][0])}<br><span class="gold">{escape(h["h1"][1])}</span></h1>
    <p class="lead">{escape(h["lead"])}</p>
    <div class="cta-row">
      <a class="btn btn-gold" href="#pick">{escape(h["pick_h"][0])} {escape(h["pick_h"][1])}</a>
      <a class="btn btn-ghost" href="#compare">{escape(h["cmp_h"][0])} {escape(h["cmp_h"][1])}</a>
    </div>
  </div>
</header>

<section id="pick">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(h["crumb"])}</p><h2 class="display"><span class="num">01</span><span>{P.two(h["pick_h"])}</span></h2></div>
    <ul class="pick">{pick}</ul>
  </div>
</section>

<section id="compare">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(h["crumb"])}</p><h2 class="display"><span class="num">02</span><span>{P.two(h["cmp_h"])}</span></h2></div>
    <div class="cmp-wrap"><table class="lp-table cmp"><thead><tr>{cols}</tr></thead><tbody>{rows}</tbody></table></div>
    <p class="lp-note">{escape(u["pay_note"])}</p>
  </div>
</section>

<section id="all">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">{escape(u["programs"])}</p><h2 class="display"><span class="num">03</span><span>{P.two(h["all_h"])}</span></h2></div>
    <div class="grid">{cards}</div>
  </div>
</section>

<section id="method">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">STR2G</p><h2 class="display"><span class="num">04</span><span>{P.two(h["same_h"])}</span></h2></div>
    <ul class="lp-list">{same}</ul>
    <div class="app"><h3>{escape(u["app_h"])}</h3><ul class="lp-list">{app}</ul></div>
  </div>
</section>

<section id="coaches">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">STR2G</p><h2 class="display"><span>{P.two(u["coaches_h"])}</span></h2></div>
    <p class="lp-p">{u["lada"]}</p>
    <p class="lp-p">{u["ria"]}</p>
    <p class="lp-p">{escape(u["raced"])}</p>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="shead"><p class="eyebrow">FAQ</p><h2 class="display"><span>{P.two(u["faq_h"])}</span></h2></div>
    <div class="faq">{faq_items}</div>
  </div>
</section>

<section class="final">
  <img class="bgimg" src="/img/{img}.webp" alt="" loading="lazy">
  <div class="wrap">
    <h2 class="display">{escape(h["cta"][0])}<br><span class="gold">{escape(h["cta"][1])}</span></h2>
    <p class="lead">{escape(u["cta_lead"])}</p>
    <div class="cta-row">
      <a class="btn btn-gold" href="#all">{escape(u["programs"])}</a>
      <a class="btn btn-ghost" href="{u["plan_url"]}">{escape(u["plan_link"])}</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    {P.footer_programs(lang)}
    <nav class="guides" aria-label="Guides"><a href="{u["plan_url"]}">{escape(u["plan_link"])}</a><a href="{u["coaching_url"]}">{escape(u["coach_link"])}</a><a href="{HUB[lang]}" aria-current="page">{escape(h["crumb"])}</a>{guides_nav}</nav>
    <nav class="net" aria-label="STR2G"><p class="net-h">STR2G</p><ul>{net}</ul></nav>
    <div style="display:flex;align-items:center;gap:12px"><img loading="lazy" src="/favicon.svg?v=2" alt="" width="26" height="26" style="border:1px solid var(--line);border-radius:6px"><span>© 2026 STR2G · Stronger Together · Strivee</span></div>
    <div class="links">
      <a href="https://instagram.com/22segge_coach" target="_blank" rel="noopener">@22segge_coach</a>
      <a href="https://instagram.com/riahrusovskaofficial" target="_blank" rel="noopener">@riahrusovskaofficial</a>
      <a href="{"/cs/ochrana-osobnich-udaju/" if lang == "cs" else "/privacy/"}">{pages.PRIV_LBL[lang]}</a>
      <a href="{"/cs/vraceni-penez/" if lang == "cs" else "/refund-policy/"}">{"Vrácení peněz" if lang == "cs" else "Refund policy"}</a>
      <a href="#" onclick="str2gConsentReset();return false;">Cookies</a>
    </div>
  </div>
</footer>
</body>
</html>
'''
    from pathlib import Path
    nl = (Path(__file__).resolve().parent / "newsletter.html").read_text(encoding="utf-8").rstrip("\n")
    return html.replace("</body>", nl + "\n</body>", 1)


def build(root, parts):
    urls = {}
    for lang in HUB_LANGS:
        out = root / HUB[lang].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, parts), encoding="utf-8")
        urls[lang] = BASE + HUB[lang]
    print(f"programs hub: {len(urls)} written")
    return urls
