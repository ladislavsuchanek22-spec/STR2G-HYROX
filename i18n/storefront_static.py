"""Statický obsah storefrontu pro vyhledávače, celý z appky Strong Coach.

Do storefront/index.html (mezi <!--SF_STATIC--> a <!--/SF_STATIC-->) vloží:
- seznam programů z appky: obrázek, název, cena, typ, dny/minuty, popis (CZ část), odkaz na nákup,
- strukturovaná data ItemList s produkty a cenami (JSON-LD).
Blok je uvnitř <str2g-storefront>. Jakmile se načte živý storefront z appky (shadow DOM), návštěvník
vidí ten; vyhledávač a prohlížeč bez JavaScriptu vidí tenhle statický seznam. Obsah je stejný.
Volá i18n/build.py po app_store.sync().
"""
import html, json, re
import app_store
from merchant_ld import add_merchant_fields

BASE = "https://str2g.com"
KIND = {"group": "Měsíční program", "one_to_one": "Individuální koučink 1:1", "fixed": "Jednorázový program"}


def _lang_part(text, lang="CZ"):
    """Popis může mít sekce **CZ** / **EN**. Vrátí požadovanou, jinak celý text."""
    t = (text or "").strip()
    m = re.search(r"\*\*%s\*\*\s*(.*?)(?=\n\s*\*\*(?:CZ|EN)\*\*|\Z)" % lang, t, flags=re.S)
    return m.group(1).strip() if m else t


def _md(text):
    """Jednoduchý markdown z appky: odstavce, odrážky '- ', **tučně**."""
    out, items = [], []
    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
            items.clear()
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        for l in lines:
            esc = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(l))
            if l.startswith(("- ", "• ")):
                items.append(esc[2:])
            else:
                flush()
                out.append(f"<p>{esc}</p>")
        flush()
    return "\n".join(out)


def _price(r):
    czk = int(r.get("price_cents") or 0) // 100
    p = f"{czk:,}".replace(",", " ") + " Kč"
    return p + (" / měsíc" if r.get("billing_period") else ""), czk


def _plain(text, n=300):
    t = re.sub(r"\*\*|^- ", "", text, flags=re.M)
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"


def build(root):
    progs = app_store.load()
    space = app_store.load_space()
    rows = sorted(progs.items(), key=lambda kv: (kv[1].get("sf_sort") or 9999, kv[1].get("name") or ""))
    cards, items = [], []
    for i, (uid, r) in enumerate(rows, 1):
        name = (r.get("name") or "").strip()
        if not name:
            continue
        price_txt, czk = _price(r)
        desc = _lang_part(r.get("description"))
        meta = " · ".join(x for x in (
            KIND.get(r.get("kind"), "Program"),
            f"{r['sf_days']} dní v týdnu" if r.get("sf_days") else "",
            f"cca {r['sf_minutes']} min" if r.get("sf_minutes") else "") if x)
        url = f"{app_store.STORE_PATH}?program={uid}"
        img = r.get("image_url")
        cards.append(f"""<article class="sf-static-card">
{f'<img src="{html.escape(img)}" alt="{html.escape(name)}" loading="lazy" width="640" height="360">' if img else ''}
<h2>{html.escape(name)}</h2>
<p class="sf-static-price"><b>{price_txt}</b> · {html.escape(meta)}</p>
{_md(desc) if desc else ''}
<p><a href="{url}">{'Předplatit' if r.get('billing_period') else 'Koupit'}: {html.escape(name)}</a></p>
</article>""")
        offer = {"@type": "Offer", "price": str(czk), "priceCurrency": "CZK",
                 "availability": "https://schema.org/InStock", "url": BASE + url}
        if r.get("billing_period"):
            offer["priceSpecification"] = {"@type": "UnitPriceSpecification", "price": str(czk),
                                           "priceCurrency": "CZK", "billingDuration": "P1M"}
        add_merchant_fields(offer)
        prod = {"@type": "Product", "name": name, "brand": {"@type": "Brand", "name": "STR2G"},
                "description": _plain(desc), "offers": offer}
        if img:
            prod["image"] = img
        items.append({"@type": "ListItem", "position": i, "item": prod})

    about = _lang_part(space.get("about") or "", "CZ")
    about_html = _md(about.split("\n\n")[0]) if about else ""
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Programy STR2G HYROX",
          "url": BASE + app_store.STORE_PATH, "numberOfItems": len(items), "itemListElement": items}
    block = f"""<!--SF_STATIC-->
<div class="sf-static">
<h1>Programy STR2G HYROX</h1>
{about_html}
{chr(10).join(cards)}
</div>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<!--/SF_STATIC-->"""
    p = root / "storefront" / "index.html"
    s = p.read_text(encoding="utf-8")
    if "<!--SF_STATIC-->" in s:
        s = re.sub(r"<!--SF_STATIC-->.*?<!--/SF_STATIC-->", lambda m: block, s, count=1, flags=re.S)
    else:
        s = s.replace('<str2g-storefront slug="str2g-hyrox"><p class="state" data-t="loading">Načítám programy…</p></str2g-storefront>',
                      f'<str2g-storefront slug="str2g-hyrox">\n{block}\n</str2g-storefront>', 1)
    assert "<!--SF_STATIC-->" in s, "storefront/index.html: nenašel jsem místo pro statický obsah"
    p.write_text(s, encoding="utf-8")
    print(f"storefront: statický obsah z appky, {len(cards)} programů")
