"""Doplní strukturovaná data FAQPage (pro Google a AI vyhledávače) na každou stránku,
která má sekci <section id="faq"> s <details><summary>otázka</summary><p>odpověď</p></details>.
Spouští se na konci build.py; je idempotentní (starý blok nahradí)."""
import html, json, re
from pathlib import Path

MARK_A, MARK_B = "<!--faq-ld-->", "<!--/faq-ld-->"

def _text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def apply(root):
    n = 0
    for f in Path(root).rglob("*.html"):
        if any(p in f.parts for p in ("i18n", "node_modules")):
            continue
        s = f.read_text(encoding="utf-8")
        s = re.sub(re.escape(MARK_A) + ".*?" + re.escape(MARK_B) + "\n?", "", s, flags=re.S)
        if "FAQPage" in s:  # stránka už FAQPage má (landing pages z pages.py)
            f.write_text(s, encoding="utf-8")
            continue
        sec = re.search(r'<section id="faq">(.*?)</section>', s, re.S)
        if not sec:
            continue
        qa = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", sec.group(1), re.S)
        if not qa:
            continue
        lang = (re.search(r'<html lang="([a-z-]+)"', s) or [None, "en"])[1]
        data = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
                "mainEntity": [{"@type": "Question", "name": _text(q),
                                "acceptedAnswer": {"@type": "Answer", "text": _text(a)}} for q, a in qa]}
        block = MARK_A + '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>" + MARK_B + "\n"
        s = s.replace("</head>", block + "</head>", 1)
        f.write_text(s, encoding="utf-8")
        n += 1
    print(f"FAQPage: {n} stránek")

if __name__ == "__main__":
    apply(Path(__file__).resolve().parent.parent)
