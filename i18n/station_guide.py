"""Landing page lead magnetu STR2G HYROX Station Guide (PDF, 8 stanic).

/station-guide/ (EN) a /cs/pruvodce-stanicemi/ (CZ). Formulář a stažení řeší i18n/stationguide.html
(Netlify formulář "station-guide"). Odkazy na sem vedou i z ladislavsuchanek.cz a hyrox-prague.eu.
Volá se z i18n/build.py.
"""
import json
from html import escape
from pathlib import Path

from pages import BASE, T, card, faq_html, shead, NET
import programs
import guides

URLS = {"en": "/station-guide/", "cs": "/cs/pruvodce-stanicemi/"}

STATIONS = [
    # klíč průvodce, EN název, CZ název, vzdálenost, EN popis, CZ popis
    ("skierg", "SkiErg", "SkiErg", "1000 m", "Hip hinge, damper, how not to burn your arms at station one.", "Práce z boků, damper a jak si hned na první stanici nezničit ruce."),
    ("sled-push", "Sled push", "Sled push", "50 m", "Body position, short steps and where to rest.", "Pozice těla, krátké kroky a kde si odpočinout."),
    ("sled-pull", "Sled pull", "Sled pull", "50 m", "Pull with your legs, manage the rope, save your grip.", "Táhni nohama, hlídej lano, šetři úchop."),
    ("burpee-broad-jumps", "Burpee broad jumps", "Burpee broad jumps", "80 m", "One rhythm, jump count, no no-reps.", "Jeden rytmus, počet skoků, žádné neplatné opakování."),
    ("rowing", "Rowing", "Veslování", "1000 m", "Legs, body, arms and how to reset at halfway.", "Nohy, trup, ruce a jak se v půlce závodu srovnat."),
    ("farmers-carry", "Farmers carry", "Farmers carry", "200 m", "Grip, posture and a break plan.", "Úchop, držení těla a plán pauz."),
    ("sandbag-lunges", "Sandbag lunges", "Sandbag lunges", "100 m", "Stride length, standard and a rhythm you can hold.", "Délka kroku, pravidla a rytmus, který udržíš."),
    ("wall-balls", "Wall balls", "Wall balls", "100 reps", "Standards, technique and how to split 100 reps.", "Pravidla, technika a jak si rozdělit 100 opakování."),
]

C = {
    "en": dict(
        title="Free HYROX Station Guide (PDF): All 8 Stations Explained | STR2G",
        desc="Free 64-page HYROX Station Guide by STR2G coaches: technique, common mistakes, race pacing and 12 workouts for every station from SkiErg to Wall Balls.",
        eyebrow="Free PDF · 64 pages",
        h1=("HYROX Station Guide", "All 8 stations. One guide."),
        lead="Technique, the most common mistakes, race pacing and 12 workouts for every HYROX station. From our coaching practice and our own races, in one free PDF.",
        btn="Get the free guide",
        inside_h="What's inside",
        inside_eb="8 chapters",
        per="Every chapter: why the station matters, the race rules, technique step by step, six common mistakes with fixes, how to pace it and 12 workouts, six of them with running.",
        read="Read the short version",
        who_h="Who wrote it",
        who="Ladislav Suchánek and Ria Suchánek Hrušovská, HYROX coaches and active racers behind STR2G. We coach athletes online worldwide and in person in Prague.",
        picks_h="Want the full plan?",
        faq=[
            ("Is the HYROX Station Guide really free?", "Yes. You get the PDF in exchange for subscribing to the STR2G newsletter with HYROX tips and offers. You can unsubscribe anytime with one click."),
            ("What language is the guide in?", "English. A Czech version is available on the Czech page."),
            ("Is it for beginners?", "Yes. Each chapter starts with the rules and basic technique and builds up to pacing and workouts, so it works for a first race and for experienced athletes."),
        ],
        locale="en_GB",
    ),
    "cs": dict(
        title="HYROX Station Guide zdarma (PDF): průvodce všemi 8 stanicemi | STR2G",
        desc="Průvodce všemi 8 HYROX stanicemi zdarma, 64 stran od trenérů STR2G: technika, nejčastější chyby, tempo na závodě a 12 tréninků ke každé stanici.",
        eyebrow="PDF zdarma · 64 stran",
        h1=("HYROX Station Guide", "8 stanic. Jeden průvodce."),
        lead="Technika, nejčastější chyby, tempo na závodě a 12 tréninků ke každé HYROX stanici. Z naší trenérské praxe a vlastních závodů, v jednom PDF zdarma.",
        btn="Chci průvodce zdarma",
        inside_h="Co v něm najdeš",
        inside_eb="8 kapitol",
        per="Každá kapitola: proč na stanici záleží, pravidla závodu, technika krok za krokem, šest nejčastějších chyb a jak je opravit, jak stanici rozvrhnout a 12 tréninků, z toho šest s během.",
        read="Krátká verze (EN)",
        who_h="Kdo ho napsal",
        who="Ladislav Suchánek a Ria Suchánek Hrušovská, HYROX trenéři a aktivní závodníci za značkou STR2G. Trénujeme sportovce online po celém světě i osobně v Praze.",
        picks_h="Chceš celý plán?",
        faq=[
            ("Je průvodce opravdu zdarma?", "Ano. PDF dostaneš výměnou za odběr STR2G newsletteru s tipy na HYROX a nabídkami. Odhlásit se můžeš kdykoli jedním klikem."),
            ("V jakém jazyce průvodce je?", "V češtině. Anglická verze je na anglické stránce."),
            ("Hodí se i pro začátečníky?", "Ano. Každá kapitola začíná pravidly a základní technikou a pokračuje k tempu a tréninkům. Poslouží na první závod i zkušeným závodníkům."),
        ],
        locale="cs_CZ",
    ),
}


def page(lang, parts):
    tracking, style, fonts, verify, icons = parts
    c = C[lang]
    u = T[lang]["ui"]
    url = BASE + URLS[lang]
    home = "/" if lang == "en" else "/cs/"
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}">' for l, p in URLS.items()) + f'<link rel="alternate" hreflang="x-default" href="{BASE}{URLS["en"]}">'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "STR2G HYROX", "item": BASE + home},
            {"@type": "ListItem", "position": 2, "name": c["h1"][0], "item": url}]},
        {"@type": "WebPage", "@id": url, "url": url, "name": c["title"].split(" | ")[0], "description": c["desc"], "inLanguage": lang,
         "isPartOf": {"@id": BASE + "/#web"}},
        {"@type": "DigitalDocument", "name": "STR2G HYROX Station Guide", "inLanguage": lang, "numberOfPages": 64,
         "isAccessibleForFree": True, "author": [{"@type": "Person", "@id": "https://www.ladislavsuchanek.cz/#person", "name": "Ladislav Suchánek"},
                                                  {"@type": "Person", "@id": "https://riahrusovska.cz/#ria", "name": "Ria Suchánek Hrušovská"}],
         "publisher": {"@id": BASE + "/#org"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]},
    ]}
    items = []
    for i, (key, en, cz, dist, den, dcz) in enumerate(STATIONS, 1):
        g = guides.GUIDES.get(key)
        link = f' <a href="{g["slug"]}">{escape(c["read"])} →</a>' if g and not g.get("draft") else ""
        name = en if lang == "en" else cz
        desc = den if lang == "en" else dcz
        items.append(f'<li><span class="st-no">{i:02d}</span><div><b>{escape(name)}</b> <span class="st-d">{escape(dist)}</span><br>{escape(desc)}{link}</div></li>')
    cards = "".join(card(lang, p, T[lang]["picks"].get(p, "Program")) for p in ["basic", "advanced", "competitor"])
    net = "".join(f'<li><a href="{h}" target="_blank" rel="noopener"><b>{escape(t)}</b></a></li>' for h, t in NET[lang])
    progs = programs.footer_programs(lang)
    sg = (Path(__file__).resolve().parent / "stationguide.html").read_text(encoding="utf-8").rstrip("\n")
    priv = "/cs/ochrana-osobnich-udaju/" if lang == "cs" else "/privacy/"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(c["title"])}</title>
<meta name="description" content="{escape(c["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#050505">
{verify}
<link rel="canonical" href="{url}">
{alt}
<meta property="og:type" content="website">
<meta property="og:locale" content="{c["locale"]}">
<meta property="og:site_name" content="STR2G HYROX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escape(c["title"])}">
<meta property="og:description" content="{escape(c["desc"])}">
<meta property="og:image" content="{BASE}/img/lada-ria-finish-line.jpg">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{style}</style>
<style>.st-list{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px 40px}}.st-list li{{display:flex;gap:16px;font-size:16px;line-height:1.5;color:var(--muted)}}.st-list b{{color:var(--fg);font-size:18px}}.st-list a{{color:var(--accent);text-decoration:none;font-weight:500}}.st-list a:hover{{text-decoration:underline}}.st-no{{font-family:var(--mono);color:var(--accent);font-size:13px;padding-top:4px}}.st-d{{font-family:var(--mono);font-size:12px;color:var(--accent);margin-left:6px}}.sg-per{{max-width:760px;margin:28px 0 0;font-size:16px;line-height:1.55;color:var(--muted)}}@media (max-width:760px){{.st-list{{grid-template-columns:1fr}}}}</style>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="{home}" aria-label="STR2G HYROX"><img class="mark" src="/favicon.svg?v=2" alt="" width="34" height="34"><b>STR<span class="gold">2</span>G</b></a>
    <div class="navlinks">
      <a class="txt" href="{home}#programs">{u["programs"]}</a>
      <button type="button" class="btn btn-gold" data-sg-cta>{escape(c["btn"])}</button>
    </div>
  </div>
</nav>

<header class="hero lp-hero" id="top">
  <img class="hero-img" src="/img/lada-ria-finish-line.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">STR2G HYROX</a><span aria-hidden="true">/</span><span>{escape(c["h1"][0])}</span></nav>
    <p class="eyebrow">{escape(c["eyebrow"])}</p>
    <h1 class="display">{escape(c["h1"][0])}<br><span class="gold">{escape(c["h1"][1])}</span></h1>
    <p class="lead">{escape(c["lead"])}</p>
    <div class="cta-row"><button type="button" class="btn btn-gold" data-sg-cta>{escape(c["btn"])}</button></div>
  </div>
</header>

<section>
  <div class="wrap">
    {shead(c["inside_eb"], escape(c["inside_h"]))}
    <ul class="st-list">{"".join(items)}</ul>
    <p class="sg-per">{escape(c["per"])}</p>
    <div class="cta-row" style="margin-top:28px"><button type="button" class="btn btn-gold" data-sg-cta>{escape(c["btn"])}</button></div>
  </div>
</section>

<section>
  <div class="wrap">
    {shead("STR2G", escape(c["who_h"]))}
    <p class="lead" style="max-width:760px">{escape(c["who"])}</p>
  </div>
</section>

<section id="pick">
  <div class="wrap">
    {shead(u["programs"], escape(c["picks_h"]))}
    <div class="grid">{cards}</div>
    <p class="lp-note">{escape(u["pay_note"])} <a href="{home}#programs">{escape(u["all_programs"])} →</a></p>
  </div>
</section>

{faq_html(lang, c["faq"])}

<footer>
  <div class="wrap">
    {progs}
    <nav class="net" aria-label="STR2G"><p class="net-h">STR2G</p><ul>{net}</ul></nav>
    <div class="links">
      <a href="https://instagram.com/22segge_coach" target="_blank" rel="noopener">@22segge_coach</a>
      <a href="https://instagram.com/riahrusovskaofficial" target="_blank" rel="noopener">@riahrusovskaofficial</a>
      <a href="{priv}">{"Ochrana osobních údajů" if lang == "cs" else "Privacy policy"}</a>
      <a href="#" onclick="str2gConsentReset();return false;">Cookies</a>
    </div>
  </div>
</footer>
{sg}
</body>
</html>
'''


def build(root, parts):
    out = {}
    for lang, path in URLS.items():
        f = root / path.strip("/") / "index.html"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(page(lang, parts), encoding="utf-8")
        out[lang] = BASE + path
    print(f"station guide landing: {len(out)} written")
    return out
