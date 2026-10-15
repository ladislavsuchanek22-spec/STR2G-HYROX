"""Build /cs/, /de/ and /pl/ from the English index.html.

Run from the repo root:  python3 i18n/build.py
Edit index.html (English) and the i18n/*.json files, then re-run.
"""
import json, re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://str2g.com"
LANGS = {"cs": "cs_CZ", "de": "de_DE", "pl": "pl_PL"}
ATTRS = ("alt", "aria-label", "content", "title")

src = (ROOT / "index.html").read_text(encoding="utf-8")


def translate_text(html, t, missing):
    parts = re.split(r"(<[^>]+>)", html)
    raw = 0
    for i, p in enumerate(parts):
        if p.startswith("<"):
            tag = p[1:].split()[0].split(">")[0].lower() if len(p) > 1 else ""
            if tag in ("script", "style"):
                raw += 1
            elif tag in ("/script", "/style"):
                raw -= 1
            # attributes
            def attr_sub(m):
                v = m.group(2)
                return f'{m.group(1)}="{t[v]}"' if v in t else m.group(0)
            parts[i] = re.sub(r'\b(%s)="([^"]*)"' % "|".join(ATTRS), attr_sub, p)
            continue
        if raw or not p.strip():
            continue
        core = p.strip()
        if core in t:
            lead = p[: len(p) - len(p.lstrip())]
            trail = p[len(p.rstrip()):]
            val = t[core]
            if val[:1] in ".,;:!?":
                lead = ""
            parts[i] = lead + val + trail
        elif re.search(r"[A-Za-z]{3}", core):
            missing.add(core)
    return "".join(parts)


for lang, locale in LANGS.items():
    t = json.loads((ROOT / "i18n" / f"{lang}.json").read_text(encoding="utf-8"))
    missing = set()
    out = translate_text(src, t, missing)
    out = out.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    out = out.replace('content="en_GB"', f'content="{locale}"', 1)
    out = out.replace(f'<link rel="canonical" href="{BASE}/">', f'<link rel="canonical" href="{BASE}/{lang}/">', 1)
    out = out.replace(' aria-current="page">EN<', '>EN<', 1)
    out = out.replace(f'hreflang="{lang}" lang="{lang}">', f'hreflang="{lang}" lang="{lang}" aria-current="page">', 1)
    out = re.sub(r'(src|content)="img/', r'\1="../img/', out)
    out = out.replace("'→ Our pick: '", json.dumps(t.get("__hint", "→ Our pick: "), ensure_ascii=False).replace('"', "'"))
    d = ROOT / lang
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(out, encoding="utf-8")
    print(f"{lang}: written, {len(missing)} untranslated text nodes")
    for m in sorted(missing):
        print("   ·", m[:90])
