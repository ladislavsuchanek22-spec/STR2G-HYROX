"""Google Merchant product feed: /feed.xml (Czech) and /feed-en.xml (English).

Only the one-time programs (race builds + specialist blocks). Monthly subscriptions are left out:
Google Merchant does not allow digital content paid by recurring subscription.
Title, description and image come from the built program pages, price from pages_content.PROGRAMS,
so the feed always matches the website. Called at the end of i18n/build.py.
"""
import html, re
from pages_content import PROGRAMS
from programs_content import PSLUGS

BASE = "https://str2g.com"
FEED_IDS = ["raceprep", "advanced", "singles", "doubles", "running", "taper"]
TYPE = {
    "cs": {"raceprep": "Příprava na závod", "advanced": "Příprava na závod", "singles": "Příprava na závod",
           "doubles": "Příprava na závod", "running": "Specializovaný blok", "taper": "Specializovaný blok"},
    "en": {"raceprep": "Race build", "advanced": "Race build", "singles": "Race build",
           "doubles": "Race build", "running": "Specialist block", "taper": "Specialist block"},
}
META = {
    "cs": ("STR2G HYROX – online tréninkové programy", "Online HYROX tréninkové programy od Láďi a Rii. Platba a trénink v aplikaci Strivee."),
    "en": ("STR2G HYROX – online training programs", "Online HYROX training programs by Láďa and Ria. Payment and training in the Strivee app."),
}


def _meta(page, pattern):
    m = re.search(pattern, page)
    return html.unescape(m.group(1)).strip() if m else ""


def _x(s):
    return html.escape(s, quote=False)


def build(root):
    for lang, fname in (("cs", "feed.xml"), ("en", "feed-en.xml")):
        items = []
        for pid in FEED_IDS:
            path = PSLUGS[pid][lang]
            page = (root / path.strip("/") / "index.html").read_text(encoding="utf-8")
            title = _meta(page, r"<title>([^<]*)</title>").replace(" | STR2G", "")
            desc = _meta(page, r'<meta name="description" content="([^"]*)"')
            img = _meta(page, r'<meta property="og:image" content="([^"]*)"')
            price = PROGRAMS[pid][1]
            items.append(f"""    <item>
      <g:id>str2g-{pid}</g:id>
      <g:title>{_x(title)}</g:title>
      <g:description>{_x(desc)}</g:description>
      <g:link>{BASE}{path}</g:link>
      <g:image_link>{_x(img)}</g:image_link>
      <g:availability>in_stock</g:availability>
      <g:price>{price}.00 CZK</g:price>
      <g:condition>new</g:condition>
      <g:brand>STR2G</g:brand>
      <g:identifier_exists>no</g:identifier_exists>
      <g:product_type>HYROX &gt; {_x(TYPE[lang][pid])}</g:product_type>
      <g:custom_label_0>{_x(TYPE[lang][pid])}</g:custom_label_0>
      <g:shipping>
        <g:country>CZ</g:country>
        <g:service>Online (Strivee)</g:service>
        <g:price>0.00 CZK</g:price>
      </g:shipping>
    </item>""")
        t, d = META[lang]
        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
  <channel>
    <title>{_x(t)}</title>
    <link>{BASE}/{'cs/' if lang == 'cs' else ''}</link>
    <description>{_x(d)}</description>
{chr(10).join(items)}
  </channel>
</rss>
"""
        (root / fname).write_text(xml, encoding="utf-8")
    print(f"feed.xml + feed-en.xml: {len(FEED_IDS)} products")
