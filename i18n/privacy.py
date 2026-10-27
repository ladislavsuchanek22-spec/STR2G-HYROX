"""Zásady ochrany osobních údajů: /privacy/ (EN) a /cs/ochrana-osobnich-udaju/ (CS).
Generuje i18n/build.py. Text uprav tady a spusť python3 i18n/build.py.
"""
from pathlib import Path

UPDATED = {"en": "18 October 2026", "cs": "18. 10. 2026"}
PATHS = {"en": "/privacy/", "cs": "/cs/ochrana-osobnich-udaju/"}
EMAIL = "info@ladislavsuchanek.cz"

CONTENT = {
"cs": {
"title": "Zásady ochrany osobních údajů | STR2G",
"h1": "Ochrana osobních údajů",
"updated": "Platné od",
"back": "Zpět na STR2G",
"body": f"""
<p class="lead">Tady najdeš, jaké údaje o tobě na str2g.com sbíráme, proč a co s nimi děláme. Píšeme to lidsky, ale platí to v plném rozsahu.</p>

<h2>Kdo tvoje údaje zpracovává</h2>
<p>Správcem osobních údajů je <b>Ladislav Suchánek, IČO 73563769</b>. Web str2g.com provozuji pod značkou STR2G HYROX společně s Riou Suchánek Hrušovskou.</p>
<p>Se vším, co se týká osobních údajů, mi napiš na <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Newsletter</h2>
<ul>
<li><b>Jaké údaje:</b> křestní jméno, e-mail, jazyk webu a stránka, ze které ses přihlásil(a).</li>
<li><b>Proč:</b> abychom ti mohli posílat newsletter. Tréninkové tipy, novinky a nabídky STR2G programů.</li>
<li><b>Na jakém základě:</b> tvůj souhlas, který dáváš odesláním formuláře (čl. 6 odst. 1 písm. a) GDPR).</li>
<li><b>Jak dlouho:</b> dokud se neodhlásíš. Odhlásit se můžeš kdykoliv odkazem v každém e-mailu nebo zprávou na {EMAIL}. Po odhlášení si necháme jen e-mail se záznamem o odhlášení, abychom ti omylem znovu nepsali.</li>
</ul>

<h2>Ukázkový týden zdarma</h2>
<ul>
<li><b>Jaké údaje:</b> křestní jméno, e-mail, jazyk webu a program, jehož ukázku sis stáhl(a).</li>
<li><b>Proč:</b> ukázkový týden v PDF dáváme zdarma výměnou za odběr STR2G newsletteru. Tvoje údaje použijeme k zápisu do newsletteru (viz výše) a k přehledu, o které programy je zájem.</li>
<li><b>Na jakém základě:</b> tvůj souhlas, který dáváš zaškrtnutím políčka ve formuláři (čl. 6 odst. 1 písm. a) GDPR). Podmínka odběru je u formuláře jasně napsaná ještě před odesláním.</li>
<li><b>Jak dlouho:</b> dokud se neodhlásíš z newsletteru. Odhlásit se můžeš kdykoliv jedním klikem v každém e-mailu, PDF ti zůstává.</li>
</ul>

<h2>Cookies, měření a reklama</h2>
<p>Analytické a reklamní nástroje (Google Analytics 4, Google Ads a Meta Pixel) spouštíme jen s tvým souhlasem přes cookie lištu. Pomáhají nám zjistit, odkud lidé na web chodí, co je zajímá a které reklamy fungují. Bez souhlasu se Meta Pixel vůbec nenačte a Google neukládá žádné cookies.</p>
<p>Souhlas můžeš kdykoliv změnit přes <a href="#" onclick="str2gConsentReset();return false;">Nastavení cookies</a>.</p>
<p>Web si navíc ve tvém prohlížeči pamatuje pár technických věcí, třeba zvolený jazyk nebo to, že jsi zavřel(a) okno newsletteru. Tyhle informace zůstávají jen u tebe.</p>

<h2>Nákup programů</h2>
<p>Programy se kupují a platí v aplikaci Strivee. Údaje, které zadáš při registraci, platbě a v aplikaci, zpracovává Strivee podle svých zásad ochrany osobních údajů.</p>

<h2>Komu údaje předáváme</h2>
<p>Údaje neprodáváme. Předáváme je jen službám, bez kterých by web a newsletter nefungovaly:</p>
<ul>
<li><b>MailerLite</b> (UAB MailerLite, Litva): rozesílání newsletteru</li>
<li><b>Netlify</b> (USA): hosting webu a záloha přihlášek z formuláře</li>
<li><b>Google</b> (Irsko / USA): měření návštěvnosti a reklama, jen s tvým souhlasem</li>
<li><b>Meta Platforms</b> (Irsko / USA): měření reklamy, jen s tvým souhlasem</li>
</ul>
<p>U služeb se sídlem v USA probíhá předání na základě rámce EU–USA pro ochranu osobních údajů (Data Privacy Framework) nebo standardních smluvních doložek Evropské komise.</p>

<h2>Tvoje práva</h2>
<p>Máš právo:</p>
<ul>
<li>zjistit, jaké údaje o tobě máme, a dostat jejich kopii,</li>
<li>nechat je opravit nebo smazat,</li>
<li>omezit jejich zpracování nebo vznést námitku,</li>
<li>nechat si je předat v běžném formátu,</li>
<li>kdykoliv odvolat souhlas (zpracování před odvoláním tím zůstává v pořádku),</li>
<li>podat stížnost u Úřadu pro ochranu osobních údajů (<a href="https://uoou.gov.cz" target="_blank" rel="noopener">uoou.gov.cz</a>).</li>
</ul>
<p>Stačí napsat na <a href="mailto:{EMAIL}">{EMAIL}</a>. Odpovíme nejpozději do 30 dnů.</p>

<h2>Změny</h2>
<p>Když tyhle zásady změníme, nová verze bude tady na webu s novým datem.</p>
""",
},
"en": {
"title": "Privacy Policy | STR2G",
"h1": "Privacy Policy",
"updated": "Effective",
"back": "Back to STR2G",
"body": f"""
<p class="lead">This page explains what personal data we collect on str2g.com, why, and what we do with it. Written in plain language, binding all the same.</p>

<h2>Who is responsible for your data</h2>
<p>The data controller is <b>Ladislav Suchánek, company ID (IČO) 73563769</b>, Czech Republic. I run str2g.com under the STR2G HYROX brand together with Ria Suchánek Hrušovská.</p>
<p>For anything related to your personal data, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Newsletter</h2>
<ul>
<li><b>What we collect:</b> your first name, email address, the site language and the page you signed up on.</li>
<li><b>Why:</b> to send you our newsletter. Training tips, news and offers on STR2G programs.</li>
<li><b>Legal basis:</b> your consent, given by submitting the form (Art. 6(1)(a) GDPR).</li>
<li><b>How long:</b> until you unsubscribe. You can do that anytime via the link in every email or by writing to {EMAIL}. After that we only keep your email with an unsubscribe record, so we never contact you again by mistake.</li>
</ul>

<h2>Free sample week</h2>
<ul>
<li><b>What we collect:</b> your first name, email address, the site language and the program whose sample you downloaded.</li>
<li><b>Why:</b> the PDF sample week is free in exchange for subscribing to the STR2G newsletter. We use your details to add you to the newsletter (see above) and to see which programs people are interested in.</li>
<li><b>Legal basis:</b> your consent, given by ticking the box in the form (Art. 6(1)(a) GDPR). The subscription condition is stated clearly next to the form before you submit it.</li>
<li><b>How long:</b> until you unsubscribe from the newsletter. You can do that anytime with one click in every email, and you keep the PDF.</li>
</ul>

<h2>Cookies, analytics and ads</h2>
<p>Analytics and advertising tools (Google Analytics 4, Google Ads and Meta Pixel) only run if you agree in the cookie banner. They show us where visitors come from, what they're interested in and which ads work. Without your consent the Meta Pixel doesn't load at all and Google stores no cookies.</p>
<p>You can change your choice anytime in <a href="#" onclick="str2gConsentReset();return false;">Cookie settings</a>.</p>
<p>The site also remembers a few technical things in your browser, like your language or that you closed the newsletter window. That information stays on your device.</p>

<h2>Buying a program</h2>
<p>Programs are bought and paid for in the Strivee app. The data you enter when you register, pay and train in the app is processed by Strivee under its own privacy policy.</p>

<h2>Who we share data with</h2>
<p>We never sell your data. We only share it with services the site and newsletter can't run without:</p>
<ul>
<li><b>MailerLite</b> (UAB MailerLite, Lithuania): sending the newsletter</li>
<li><b>Netlify</b> (USA): website hosting and a backup of form signups</li>
<li><b>Google</b> (Ireland / USA): analytics and advertising, only with your consent</li>
<li><b>Meta Platforms</b> (Ireland / USA): ad measurement, only with your consent</li>
</ul>
<p>Transfers to US-based services rely on the EU–US Data Privacy Framework or the European Commission's standard contractual clauses.</p>

<h2>Your rights</h2>
<p>You have the right to:</p>
<ul>
<li>know what data we hold about you and get a copy,</li>
<li>have it corrected or deleted,</li>
<li>restrict or object to its processing,</li>
<li>receive it in a common, portable format,</li>
<li>withdraw your consent at any time (this doesn't affect processing before you withdrew),</li>
<li>lodge a complaint with a data protection authority, in the Czech Republic the Office for Personal Data Protection (<a href="https://uoou.gov.cz/en" target="_blank" rel="noopener">uoou.gov.cz</a>), or the one in your own country.</li>
</ul>
<p>Just email <a href="mailto:{EMAIL}">{EMAIL}</a>. We reply within 30 days.</p>

<h2>Changes</h2>
<p>If we change this policy, the new version will be published here with a new date.</p>
""",
},
}

CSS = """
:root{--bg:#050505;--panel:#0F0F0E;--line:#262521;--fg:#fff;--muted:#9A978F;--accent:#C9A950;
--display:"Barlow Condensed","Arial Narrow",Impact,sans-serif;--body:"Archivo","Helvetica Neue",Arial,sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,monospace;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--body);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:0 max(20px,env(safe-area-inset-left,0px))}
header{border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px;gap:16px}
.logo{font-family:var(--display);font-weight:900;font-style:italic;font-size:28px;color:var(--fg);text-decoration:none}
.logo span{color:var(--accent)}
header a.back{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);text-decoration:none}
header a.back:hover{color:var(--fg)}
main{padding:56px 0 80px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin:0 0 14px}
h1{font-family:var(--display);font-weight:900;font-style:italic;text-transform:uppercase;font-size:clamp(44px,9vw,76px);line-height:.9;margin:0 0 28px}
h2{font-family:var(--display);font-weight:800;font-style:italic;text-transform:uppercase;font-size:30px;line-height:1;margin:44px 0 14px;padding-top:28px;border-top:1px solid var(--line)}
p,li{color:#D6D3CC}
.lead{font-size:19px;color:var(--fg)}
ul{padding-left:20px}
li{margin:0 0 8px}
b{color:var(--fg)}
a{color:var(--accent)}
a:hover{color:var(--fg)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
footer{border-top:1px solid var(--line);padding:28px 0 40px;font-family:var(--mono);font-size:12px;color:var(--muted)}
"""


# ---------- Vrácení peněz (refund policy): /refund-policy/ (EN) a /cs/vraceni-penez/ (CS)
REFUND_UPDATED = {"en": "27 October 2026", "cs": "27. 10. 2026"}
REFUND_PATHS = {"en": "/refund-policy/", "cs": "/cs/vraceni-penez/"}
REFUND = {
"cs": {
"title": "Vrácení peněz | STR2G",
"h1": "Vrácení peněz",
"updated": "Platné od",
"back": "Zpět na STR2G",
"body": f"""
<p class="lead">STR2G programy jsou digitální obsah. Po zaplacení je máš hned k dispozici v aplikaci Strivee. Proto peníze za zakoupené programy nevracíme.</p>
<h2>Jednorázové programy</h2>
<p>Programy placené jednorázově (8týdenní Singles a Doubles, Taper, Running for HYROX, Race Prep, Advanced) nevracíme, jakmile je program zakoupený a zpřístupněný.</p>
<h2>Měsíční předplatné</h2>
<p>Měsíční předplatné (HYROX Basic, HYROX Competitor, HYROX Pro Athlete, individuální program 1:1) můžeš kdykoliv zrušit. Zrušením se zastaví další platby. Už zaplacené období nevracíme, ani jeho část, i když předplatné ukončíš v jeho průběhu.</p>
<h2>Digitální obsah a odstoupení od smlouvy</h2>
<p>Nákupem souhlasíš s tím, že ti program zpřístupníme hned, a bereš na vědomí, že tím ztrácíš právo odstoupit od smlouvy do 14 dnů.</p>
<h2>Kontakt</h2>
<p>Pokud máš s nákupem nebo přístupem problém, napiš na <a href="mailto:{EMAIL}">{EMAIL}</a>. Vyřešíme to.</p>
""",
},
"en": {
"title": "Refund policy | STR2G",
"h1": "Refund policy",
"updated": "Effective from",
"back": "Back to STR2G",
"body": f"""
<p class="lead">STR2G programs are digital content. You get access in the Strivee app right after payment, so we don't offer refunds on purchased programs.</p>
<h2>One-time programs</h2>
<p>Programs paid once (8-Week Singles and Doubles, Taper, Running for HYROX, Race Prep, Advanced) are non-refundable once purchased and unlocked.</p>
<h2>Monthly subscriptions</h2>
<p>You can cancel a monthly subscription (HYROX Basic, HYROX Competitor, HYROX Pro Athlete, individuální program 1:1) at any time. Cancelling stops future payments. Periods already paid are not refunded, in full or in part, even if you cancel mid-period.</p>
<h2>Digital content and withdrawal</h2>
<p>By purchasing, you agree that we give you access immediately and acknowledge that you lose your 14-day right of withdrawal.</p>
<h2>Contact</h2>
<p>If something is wrong with your purchase or access, email <a href="mailto:{EMAIL}">{EMAIL}</a> and we'll sort it out.</p>
""",
},
}


def build(root, tracking, fonts, icons):
    _build_doc(root, tracking, fonts, icons, CONTENT, PATHS, UPDATED)
    _build_doc(root, tracking, fonts, icons, REFUND, REFUND_PATHS, REFUND_UPDATED)


def _build_doc(root, tracking, fonts, icons, CONTENT, PATHS, UPDATED):
    for lang, c in CONTENT.items():
        home = "/cs/" if lang == "cs" else "/"
        other = "en" if lang == "cs" else "cs"
        html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["title"]}</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://str2g.com{PATHS[lang]}">
<link rel="alternate" hreflang="{lang}" href="https://str2g.com{PATHS[lang]}">
<link rel="alternate" hreflang="{other}" href="https://str2g.com{PATHS[other]}">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap"><a class="logo" href="{home}">STR<span>2</span>G</a><a class="back" href="{home}">← {c["back"]}</a></div></header>
<main><div class="wrap">
<p class="eyebrow">{c["updated"]} {UPDATED[lang]}</p>
<h1>{c["h1"]}</h1>
{c["body"].strip()}
</div></main>
<footer><div class="wrap">© 2026 STR2G · Ladislav Suchánek · IČO 73563769 · <a href="{PATHS[other]}">{"English" if lang == "cs" else "Česky"}</a></div></footer>
</body>
</html>
"""
        out = Path(root) / PATHS[lang].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
    print("privacy pages: 2 written")
