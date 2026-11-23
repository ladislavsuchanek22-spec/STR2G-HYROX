"""Obchodní podmínky (CZ /cs/obchodni-podminky/, EN /terms/) pro prodej programů přes vlastní storefront.

Generuje se stejnou šablonou jako zásady ochrany osobních údajů (privacy._build_doc).
Volá i18n/build.py. Návrh, před ostrým spuštěním ať ho zkontroluje právník / účetní.
"""
import privacy

EMAIL = privacy.EMAIL
TERMS_UPDATED = {"en": "1 December 2026", "cs": "1. 12. 2026"}
TERMS_PATHS = {"en": "/terms/", "cs": "/cs/obchodni-podminky/"}

TERMS = {
"cs": {
"title": "Obchodní podmínky | STR2G",
"h1": "Obchodní podmínky",
"updated": "Platné od",
"back": "Zpět na STR2G",
"body": f"""
<p class="lead">Podmínky pro nákup online tréninkových programů a koučinku STR2G HYROX na webu str2g.com.</p>

<h2>1. Kdo prodává</h2>
<p><b>Ladislav Suchánek, IČO 73563769</b>, podnikající fyzická osoba, provozuje značku STR2G HYROX společně s Riou Suchánek Hrušovskou. Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>2. Co prodáváme</h2>
<ul>
<li><b>Programy</b> (Basic, Competitor, Pro Athlete, 12týdenní a 8týdenní přípravy, Running, Taper): digitální obsah, tréninkový plán v aplikaci Strong Coach (app.str2g.com).</li>
<li><b>Koučink 1:1</b>: služba, individuální plán a průběžné úpravy od trenéra v aplikaci Strong Coach.</li>
</ul>
<p>Popis, délka a cena každého programu jsou uvedeny u programu na webu.</p>

<h2>3. Objednávka a platba</h2>
<ul>
<li>Program vybereš na str2g.com a zaplatíš kartou. Platbu zpracovává Stripe. Údaje o kartě dostane jen Stripe, my je nevidíme.</li>
<li>Ceny jsou v českých korunách a jsou konečné. Při platbě v jiné měně přepočítává tvoje banka.</li>
<li>Smlouva vzniká zaplacením. Potvrzení přijde na e-mail zadaný při platbě.</li>
</ul>

<h2>4. Předplatné</h2>
<ul>
<li>Měsíční programy a koučink 1:1 jsou předplatné, které se automaticky obnovuje každý měsíc, dokud ho nezrušíš.</li>
<li>Zrušit ho můžeš kdykoli v aplikaci Strong Coach (Programy → Spravovat platby a kartu). Platí do konce zaplaceného období, další platba už se nestrhne.</li>
<li>Přípravy na závod a specializované bloky jsou jednorázová platba, nic se neobnovuje.</li>
</ul>

<h2>5. Přístup k programu</h2>
<p>Hned po zaplacení ti na e-mail přijde odkaz do aplikace Strong Coach, kde si nastavíš heslo. Program tam najdeš okamžitě. Aplikace běží v prohlížeči v telefonu i počítači.</p>

<h2>6. Odstoupení od smlouvy</h2>
<ul>
<li>Jako spotřebitel můžeš od smlouvy uzavřené přes internet odstoupit do 14 dnů od jejího uzavření, a to e-mailem na <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
<li><b>Digitální obsah (programy):</b> pokud ti na tvou výslovnou žádost zpřístupníme program ještě před uplynutím lhůty a ty bereš na vědomí, že tím ztrácíš právo na odstoupení, právo na odstoupení zaniká zpřístupněním programu (§ 1837 písm. l) občanského zákoníku).</li>
<li><b>Koučink 1:1 (služba):</b> pokud na tvou žádost začneme plnit už během lhůty a od smlouvy odstoupíš, zaplatíš poměrnou část za to, co už bylo poskytnuto.</li>
<li>Peníze vracíme do 14 dnů od odstoupení stejným způsobem, jakým jsi platil(a).</li>
</ul>

<h2>7. Reklamace</h2>
<p>Když program nefunguje nebo neodpovídá popisu, napiš na <a href="mailto:{EMAIL}">{EMAIL}</a>. Reklamaci vyřídíme bez zbytečného odkladu, nejpozději do 30 dnů.</p>

<h2>8. Zdraví</h2>
<p>Trénink je fyzicky náročný. Cvičíš na vlastní odpovědnost a podle svého zdravotního stavu. Pokud máš zdravotní omezení nebo jsi po zranění, poraď se nejdřív s lékařem. Programy nenahrazují lékařskou péči.</p>

<h2>9. Spory</h2>
<p>Se stížností se obrať nejdřív na nás. Spotřebitel může využít mimosoudní řešení sporu u České obchodní inspekce (<a href="https://www.coi.cz" target="_blank" rel="noopener">coi.cz</a>). Platí české právo.</p>

<h2>10. Osobní údaje</h2>
<p>Jak zpracováváme osobní údaje, popisují <a href="/cs/ochrana-osobnich-udaju/">Zásady ochrany osobních údajů</a>.</p>
""",
},
"en": {
"title": "Terms and conditions | STR2G",
"h1": "Terms and conditions",
"updated": "Effective from",
"back": "Back to STR2G",
"body": f"""
<p class="lead">Terms for buying STR2G HYROX online training programs and coaching on str2g.com.</p>

<h2>1. Seller</h2>
<p><b>Ladislav Suchánek, company ID (IČO) 73563769</b>, a sole trader in the Czech Republic, runs the STR2G HYROX brand together with Ria Suchánek Hrušovská. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>2. What we sell</h2>
<ul>
<li><b>Programs</b> (Basic, Competitor, Pro Athlete, 12-week and 8-week race builds, Running, Taper): digital content, a training plan in the Strong Coach app (app.str2g.com).</li>
<li><b>1:1 coaching</b>: a service, an individual plan with ongoing adjustments from a coach in the Strong Coach app.</li>
</ul>
<p>The description, length and price of each program are shown with the program on the website.</p>

<h2>3. Order and payment</h2>
<ul>
<li>You pick a program on str2g.com and pay by card. Payments are processed by Stripe. Your card details go only to Stripe; we never see them.</li>
<li>Prices are in Czech koruna (CZK) and are final. If your card is in another currency, your bank converts it.</li>
<li>The contract is concluded when you pay. A confirmation is sent to the e-mail you enter at checkout.</li>
</ul>

<h2>4. Subscriptions</h2>
<ul>
<li>Monthly programs and 1:1 coaching are subscriptions that renew automatically every month until you cancel.</li>
<li>You can cancel anytime in the Strong Coach app (Programs → Manage payments and card). Access runs to the end of the paid period and no further payment is taken.</li>
<li>Race builds and specialist blocks are a one-time payment; nothing renews.</li>
</ul>

<h2>5. Access</h2>
<p>Right after payment you get an e-mail with a link to the Strong Coach app, where you set your password. Your program is there straight away. The app runs in the browser on your phone or computer.</p>

<h2>6. Right of withdrawal</h2>
<ul>
<li>As a consumer you can withdraw from a contract made online within 14 days of concluding it, by e-mail to <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
<li><b>Digital content (programs):</b> if, at your express request, we give you access before the 14 days are over and you acknowledge that you lose the right of withdrawal, the right of withdrawal ends once the program is made available to you.</li>
<li><b>1:1 coaching (service):</b> if we start at your request within the 14 days and you then withdraw, you pay a proportionate amount for what has already been provided.</li>
<li>Refunds are made within 14 days of withdrawal, using the same payment method.</li>
</ul>

<h2>7. Complaints</h2>
<p>If a program doesn't work or doesn't match its description, e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>. We handle complaints without undue delay, within 30 days at the latest.</p>

<h2>8. Health</h2>
<p>Training is physically demanding. You train at your own risk and according to your health. If you have a medical condition or are coming back from injury, check with a doctor first. Our programs do not replace medical care.</p>

<h2>9. Disputes</h2>
<p>Please contact us first. Consumers can use out-of-court dispute resolution with the Czech Trade Inspection Authority (<a href="https://www.coi.cz/en/" target="_blank" rel="noopener">coi.cz</a>). Czech law applies.</p>

<h2>10. Personal data</h2>
<p>How we handle personal data is described in our <a href="/privacy/">Privacy policy</a>.</p>
""",
},
}


def build(root, tracking, fonts, icons):
    privacy._build_doc(root, tracking, fonts, icons, TERMS, TERMS_PATHS, TERMS_UPDATED)
    print("terms pages: 2 written")
