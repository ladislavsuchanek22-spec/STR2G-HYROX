"""Anglické průvodce (guides) na str2g.com – článkové stránky s FAQ a kartami programů.

Volá se z i18n/build.py. Stránka s draft=True se negeneruje ani nepřidá do sitemap.
Zveřejnění: v GUIDES nastav draft=False a spusť python3 i18n/build.py.
"""
import json
from html import escape
from pages import BASE, T, card, faq_html, shead, ul, NET, extract  # noqa: F401
import programs

GUIDES = {
    "hyrox-taper": dict(
        draft=True,
        slug="/guides/hyrox-taper/",
        title="HYROX Taper: How to Taper for a HYROX Race (2-Week Plan) | STR2G",
        desc="How to taper for HYROX: what to cut, what to keep, a 2-week taper outline and race week checklist. From HYROX coaches who race themselves.",
        eyebrow="HYROX guide",
        h1=("HYROX taper", "Fresh legs, sharp engine."),
        lead="The last two weeks before a HYROX race decide whether you arrive fresh or flat. You can't build fitness now. You can only lose it or protect it. A good taper protects it.",
        sections=[
            ("What a taper is", """<p class="lp-p">A taper is a planned drop in training volume before a race while you keep the intensity. Less total work, same quality. Fatigue goes down faster than fitness, so you arrive at the start line rested and still sharp.</p>"""),
            ("What to cut and what to keep", """<ul class="lp-list">
<li><b>Cut volume:</b> roughly 30–50% less total running distance and fewer station sets than in your peak weeks.</li>
<li><b>Keep intensity:</b> short efforts at race pace and slightly faster, so your body remembers the speed.</li>
<li><b>Keep frequency:</b> train on similar days as before. Fewer sessions often make people feel sluggish.</li>
<li><b>Drop heavy new stimuli:</b> no max-effort lifts, no new exercises, no full race simulations.</li>
</ul>"""),
            ("A 2-week taper outline", """<table class="lp-table"><thead><tr><th>When</th><th>Focus</th><th>Example</th></tr></thead><tbody>
<tr><td>Week −2</td><td>Volume down, intensity kept</td><td>Run intervals at race pace, half-size station blocks, one shorter compromised run session</td></tr>
<tr><td>Week −1, early</td><td>Sharpen</td><td>Short race-pace runs (e.g. 4 × 400 m), a few reps on sleds and wall balls at race weight</td></tr>
<tr><td>2–3 days out</td><td>Prime</td><td>20–30 min easy, a few strides, mobility</td></tr>
<tr><td>Day before</td><td>Rest or shake-out</td><td>10–20 min easy jog, pack your bag, sleep</td></tr>
</tbody></table>
<p class="lp-p">Our <a href="/programs/hyrox-taper/">2-Week HYROX Taper</a> program has every session written out for Open, Doubles and Pro.</p>"""),
            ("Race week checklist", """<ul class="lp-list">
<li>Sleep more than usual, especially two nights before the race.</li>
<li>Eat normally with a bit more carbohydrate in the last two days. Nothing new.</li>
<li>Check your start time, division and the latest rulebook.</li>
<li>Pack shoes and kit you have trained in.</li>
<li>Plan your pacing: first two runs slower than you want.</li>
</ul>"""),
        ],
        picks=["taper", "singles", "raceprep"],
        faq=[
            ("How long should a HYROX taper be?", "Most athletes do well with 7–14 days. Beginners racing their first HYROX can use about one week, athletes after a long, heavy block often benefit from two."),
            ("Should I stop training before HYROX?", "No. Keep training, but do less. Stopping completely often makes you feel flat on race day. Reduce volume and keep short, sharp efforts."),
            ("Should I do a full HYROX simulation in race week?", "No. A full simulation takes days to recover from. Keep it to short parts of the race at race pace."),
            ("What should I eat before a HYROX race?", "A light, carb-based meal 2–3 hours before your start that you have tested in training. Avoid new foods on race day."),
        ],
    ),
    "compromised-running": dict(
        draft=True,
        slug="/guides/hyrox-compromised-running/",
        title="Compromised Running for HYROX: Workouts to Run Fast on Tired Legs | STR2G",
        desc="Compromised running is running right after a station. Why it decides your HYROX time, how to pace it and 5 workouts to train it.",
        eyebrow="HYROX guide",
        h1=("Compromised running", "Run fast on tired legs."),
        lead="In HYROX you never run fresh. Every kilometre after the first comes straight off a station. Training that is the single biggest lever for most athletes.",
        sections=[
            ("What compromised running is", """<p class="lp-p">Compromised running means running under fatigue from another effort: after sleds, burpees, lunges or wall balls. Your legs are heavy, your heart rate is high and your stride shortens. Athletes who only train fresh running often lose minutes on the second half of the race.</p>"""),
            ("How to pace it", """<ul class="lp-list">
<li>Start each run slightly slower than race pace for the first 100–200 m, then settle into your pace.</li>
<li>Use short, quick steps until your legs come back. Don't fight for long strides.</li>
<li>Control your breathing first. Speed follows.</li>
<li>Keep the Roxzone short: run into the station, run out of it.</li>
</ul>"""),
            ("5 compromised running workouts", """<ol class="lp-steps">
<li><b>Sled to run:</b> 4 rounds of 25 m sled push + 1 km at race pace. Rest 2 minutes.</li>
<li><b>Lunge to run:</b> 4 rounds of 50 m sandbag lunges + 800 m. The run after lunges is the hardest in the race.</li>
<li><b>Wall ball finisher:</b> 3 rounds of 1 km + 30 wall balls, no rest between.</li>
<li><b>Machine combo:</b> 5 rounds of 500 m row or SkiErg + 600 m run at race pace.</li>
<li><b>Half race:</b> 4 × (1 km + a station) at race pace, 4–6 weeks before the race.</li>
</ol>"""),
            ("How often to train it", """<p class="lp-p">One or two compromised running sessions a week is enough for most athletes, next to easy running and strength. More is not better here. These sessions are hard and need recovery. If running is your weak point, our <a href="/programs/running-for-hyrox/">Running for HYROX</a> program builds it over 12 weeks.</p>"""),
        ],
        picks=["running", "competitor", "basic"],
        faq=[
            ("What is compromised running in HYROX?", "Running right after a station, on tired legs and with a high heart rate. In HYROX every kilometre after the first is compromised."),
            ("How do I get better at running after sleds?", "Train it directly: short sled pushes or pulls followed by 1 km at race pace. Add strength work for legs twice a week and keep an easy running base."),
            ("How many compromised running sessions per week?", "One or two for most athletes, alongside easy runs and strength training."),
        ],
    ),
    "sled-pull": dict(
        draft=True,
        slug="/guides/hyrox-sled-pull-technique/",
        title="HYROX Sled Pull Technique: How to Pull Faster and Save Your Legs | STR2G",
        desc="How to improve your HYROX sled pull: technique, rope handling, weights for every division and workouts to get faster. From HYROX coaches.",
        eyebrow="HYROX guide",
        h1=("Sled pull", "Pull with your legs, not your arms."),
        lead="The sled pull is station three. 50 metres, pulled in by rope. Most people lose time here because they pull with their arms and burn out their grip before the next run.",
        sections=[
            ("Weights and rules", """<table class="lp-table"><thead><tr><th>Division</th><th>Total sled weight</th><th>Distance</th></tr></thead><tbody>
<tr><td>Women Open</td><td>78 kg</td><td>50 m</td></tr>
<tr><td>Men Open / Women Pro</td><td>103 kg</td><td>50 m</td></tr>
<tr><td>Men Pro</td><td>153 kg</td><td>50 m</td></tr>
</tbody></table>
<p class="lp-p">You pull the sled towards you, then walk back and repeat. Source: <a href="https://hyroxdach.com/wp-content/uploads/2025/06/25_26-Singles-Rulebook_en_R1.pdf" target="_blank" rel="noopener">HYROX Singles Rulebook 2025/26</a>. Always check the current rulebook before your race.</p>"""),
            ("Technique", """<ul class="lp-list">
<li><b>Sit back and drive with the legs.</b> Low hips, lean back, and push through your heels. Your arms just transfer the force.</li>
<li><b>Hand over hand, short and fast.</b> Long pulls look strong but kill your grip.</li>
<li><b>Keep the sled moving.</b> Restarting a stopped sled costs far more than keeping it rolling.</li>
<li><b>Manage the rope.</b> Let it pile behind you, not under your feet.</li>
<li><b>Breathe.</b> Exhale with every pull. Holding your breath spikes your heart rate before the burpees.</li>
</ul>"""),
            ("Workouts to get faster", """<ol class="lp-steps">
<li><b>Technique:</b> 4 × 12.5 m at moderate weight, focus on leg drive.</li>
<li><b>Race weight:</b> 3 × 25 m at race weight, 2 minutes rest.</li>
<li><b>Under fatigue:</b> 1 km run + 25 m sled push + 25 m sled pull, 3 rounds.</li>
<li><b>Strength:</b> rows, deadlifts and farmers carries twice a week for back and grip.</li>
</ol>
<p class="lp-p">All eight stations are built into our <a href="/programs/hyrox-basic/">HYROX Basic</a> and <a href="/programs/hyrox-competitor/">HYROX Competitor</a> programs.</p>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How heavy is the HYROX sled pull?", "Total sled weight is 78 kg for Women Open, 103 kg for Men Open and Women Pro, and 153 kg for Men Pro. Distance is 50 m in every division."),
            ("How do I improve my HYROX sled pull?", "Pull with your legs, not your arms: sit back, drive through your heels and use short, quick hand-over-hand pulls. Train it at race weight after runs and build back and grip strength."),
            ("Should I wear gloves for the sled pull?", "Many athletes do. Gloves are allowed in HYROX (grips are not). Test them in training first."),
        ],
    ),
}


def page(g, parts):
    tracking, style, fonts, verify, icons = parts
    u = T["en"]["ui"]
    url = BASE + g["slug"]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "STR2G HYROX", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": g["h1"][0], "item": url}]},
        {"@type": "Article", "headline": g["title"].split(" | ")[0], "description": g["desc"], "inLanguage": "en",
         "mainEntityOfPage": url, "image": BASE + "/img/lada-ria-finish-line.jpg",
         "author": [{"@type": "Person", "name": "Ladislav Suchánek"}, {"@type": "Person", "name": "Ria Suchánek Hrušovská"}],
         "publisher": {"@type": "Organization", "name": "STR2G HYROX", "url": BASE + "/"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]},
    ]}
    secs = "".join(f'''
<section>
  <div class="wrap">
    {shead(g["eyebrow"], escape(h))}
    {html}
  </div>
</section>''' for h, html in g["sections"])
    cards = "".join(card("en", p, T["en"]["picks"].get(p, "Program")) for p in g["picks"])
    net = "".join(f'<li><a href="{h}" target="_blank" rel="noopener"><b>{escape(t)}</b></a></li>' for h, t in NET["en"])
    progs = programs.footer_programs("en") + "\n    "
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(g["title"])}</title>
<meta name="description" content="{escape(g["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#050505">
{verify}
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="STR2G HYROX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escape(g["title"])}">
<meta property="og:description" content="{escape(g["desc"])}">
<meta property="og:image" content="{BASE}/img/lada-ria-finish-line.jpg">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{style}</style>
<style>.lp-p a,.lp-list a{{color:var(--gold, #c9a961);text-decoration:underline}}</style>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="/" aria-label="STR2G HYROX"><img class="mark" src="/favicon.svg?v=2" alt="" width="34" height="34"><b>STR<span class="gold">2</span>G</b></a>
    <div class="navlinks">
      <a class="txt" href="/#programs">{u["programs"]}</a>
      <a class="txt" href="/hyrox-training-plan/">{escape(u["plan_link"])}</a>
      <a class="btn btn-gold" href="#pick">{u["start"]}</a>
    </div>
  </div>
</nav>

<header class="hero lp-hero" id="top">
  <img class="hero-img" src="/img/lada-ria-finish-line.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">STR2G HYROX</a><span aria-hidden="true">/</span><span>{escape(g["h1"][0])}</span></nav>
    <p class="eyebrow">{escape(g["eyebrow"])}</p>
    <h1 class="display">{escape(g["h1"][0])}<br><span class="gold">{escape(g["h1"][1])}</span></h1>
    <p class="lead">{escape(g["lead"])}</p>
    <div class="cta-row"><a class="btn btn-gold" href="#pick">{u["start"]}</a></div>
  </div>
</header>
{secs}

<section id="pick">
  <div class="wrap">
    {shead(u["programs"], "Programs that train this")}
    <div class="grid">{cards}</div>
    <p class="lp-note">{escape(u["pay_note"])} <a href="/#programs">{escape(u["all_programs"])} →</a></p>
  </div>
</section>

{faq_html("en", g["faq"])}

<footer>
  <div class="wrap">
    {progs}<nav class="net" aria-label="STR2G"><p class="net-h">STR2G</p><ul>{net}</ul></nav>
    <div class="links">
      <a href="https://instagram.com/22segge_coach" target="_blank" rel="noopener">@22segge_coach</a>
      <a href="https://instagram.com/riahrusovskaofficial" target="_blank" rel="noopener">@riahrusovskaofficial</a>
      <a href="/privacy/">Privacy policy</a>
      <a href="#" onclick="str2gConsentReset();return false;">Cookies</a>
    </div>
  </div>
</footer>
</body>
</html>
'''
    return html


def build(root, parts):
    urls = []
    for key, g in GUIDES.items():
        if g.get("draft"):
            continue
        out = root / g["slug"].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(g, parts), encoding="utf-8")
        urls.append(BASE + g["slug"])
    print(f"guides: {len(urls)} written")
    return urls
