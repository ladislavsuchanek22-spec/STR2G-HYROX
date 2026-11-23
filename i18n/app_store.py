"""Napojení webu na appku Strong Coach (jediné místo pravdy pro programy a ceny).

- APP_IDS: program na webu -> id programu v appce (storefront prostoru str2g-hyrox).
- sync(): stáhne z veřejného API appky profil storefrontu a programy (texty, obrázky, ceny) a uloží je do i18n/app_programs.json.
  Když API není dostupné (třeba lokálně bez sítě), použije se poslední uložený stav.
- apply(PROGRAMS): přepíše ceny a měsíční/jednorázové podle appky.
- buy_url(pid): odkaz na nákup na vlastním storefrontu (str2g.com/storefront/?program=…).

Build (i18n/build.py) volá sync() na začátku, takže změna ceny v appce se po novém buildu
propíše na všechny stránky, do feedu i do strukturovaných dat.
"""
import json, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
SNAP = ROOT / "app_programs.json"
API = "https://nqivuuwnlckgvnohcrlv.supabase.co/rest/v1"
KEY = "sb_publishable_XTnwDJvGx75s3ctFO6m-fA_8JFPm7P6"  # veřejný klíč appky, určený do prohlížeče
SPACE_SLUG = "str2g-hyrox"

APP_IDS = {
    "basic":      "c18b7800-f596-441d-841e-1e81d444d00c",
    "competitor": "4bb39d07-5f72-4c58-b074-b6c2f3d25730",
    "pro":        "cb99bf54-d8b4-433e-a08b-d0fe2a138ee5",
    "raceprep":   "9cb1e2aa-9a7e-4f05-93b8-4b948b461891",
    "advanced":   "bf5b8a49-3c35-4fb5-ba06-837f9f40a650",
    "singles":    "1f4f0945-7a22-4b7e-a5aa-558536973d6b",
    "doubles":    "b63f4bcc-0007-4bee-b040-7a0349f59f04",
    "running":    "74b976b7-5861-4567-8771-516438a6f406",
    "taper":      "f82e4048-8685-4e56-ae09-1ed40367a1b8",
    "coaching":   "f855a4e1-d333-40e2-b35f-fe3c7387f271",
}
STORE_PATH = "/storefront/"


def _get(path):
    req = urllib.request.Request(API + path, headers={"apikey": KEY, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))


FIELDS = ("name", "kind", "description", "image_url", "price_cents", "currency", "billing_period",
          "sf_level", "sf_days", "sf_minutes", "sf_sessions", "sf_sort")
SPACE_FIELDS = ("name", "about", "banner_url", "logo_url", "website", "instagram")


def sync():
    """Stáhne z appky profil storefrontu a všechny jeho programy (texty, obrázky, ceny, parametry).
    Vrací (programy, zdroj). Profil storefrontu vrací load_space()."""
    try:
        sp = _get(f"/storefront_spaces?slug=eq.{SPACE_SLUG}&select=id," + ",".join(SPACE_FIELDS))[0]
        rows = _get(f"/storefront_programs?space_id=eq.{sp['id']}&select=id," + ",".join(FIELDS))
        snap = {"space": {k: sp.get(k) for k in SPACE_FIELDS},
                "programs": {r["id"]: {k: r.get(k) for k in FIELDS} for r in rows}}
        SNAP.write_text(json.dumps(snap, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        return snap["programs"], "app"
    except Exception as e:  # bez sítě: poslední uložený stav
        print(f"app_store: API appky nedostupné ({type(e).__name__}), používám uložený stav")
        return load(), "snapshot"


def _snap():
    d = json.loads(SNAP.read_text(encoding="utf-8")) if SNAP.exists() else {}
    return d if "programs" in d else {"space": {}, "programs": d}  # starý formát = jen programy


def load():
    return _snap()["programs"]


def load_space():
    return _snap()["space"]


def apply(programs, data=None):
    """Ceny a měsíční/jednorázové z appky. Program, který v appce chybí, zůstane podle webu."""
    data = load() if data is None else data
    for pid, uid in APP_IDS.items():
        r = data.get(uid)
        if pid not in programs or not r or not r.get("price_cents"):
            continue
        sid, _czk, _monthly, name = programs[pid]
        programs[pid] = (sid, int(r["price_cents"]) // 100, bool(r.get("billing_period")), name)
    return programs


def missing(data=None):
    data = load() if data is None else data
    return [pid for pid, uid in APP_IDS.items() if uid not in data]


def buy_url(pid):
    return f"{STORE_PATH}?program={APP_IDS[pid]}"
