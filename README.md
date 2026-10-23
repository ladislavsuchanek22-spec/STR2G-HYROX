# STR2G HYROX

Sales website for the STR2G online HYROX programs by Láďa and Ria Suchánek.

One static page (`index.html`), no build step. Every Start / Buy button links straight to checkout in the Strivee app.

## Programs on the site

| Program | Price | Type |
|---|---|---|
| HYROX Basic | CZK 750 / month | Monthly |
| HYROX Competitor | CZK 960 / month | Monthly |
| HYROX Pro Athlete | CZK 1,350 / month | Monthly |
| 12-Week HYROX Race Prep | CZK 2,100 | Race build |
| 12-Week HYROX Advanced | CZK 1,900 | Race build (first race, all levels) |
| 8-Week HYROX Singles | CZK 1,500 | Race build |
| 8-Week HYROX Doubles | CZK 1,700 | Race build |
| Running for HYROX 2.0 (12 weeks) | CZK 1,000 | Specialist block |
| 2-Week HYROX Taper 2.0 | CZK 550 | Specialist block |
| HYROX Individual Program 1:1 | CZK 3,500 / month | 1:1 coaching |

Source of prices and links: https://train.strivee.app/p/str2g-hyrox

## Publishing

Turn on GitHub Pages in Settings → Pages → Deploy from branch → `main` / root. The site will be live at `https://<account>.github.io/str2g-hyrox/`.

## Languages

English is `index.html` (source). Czech, German and Polish live in `/cs/`, `/de/`, `/pl/` and are generated:

1. Edit `index.html` (English).
2. Add or update the matching lines in `i18n/cs.json`, `i18n/de.json`, `i18n/pl.json` (key = exact English text).
3. Run `python3 i18n/build.py` and commit everything.

## Trhy a landing pages (EN/UK, CZ, SK, DE, PL, FR, ES, IT, NL)

- Hlavní stránka: EN (`/`, i pro UK), `/cs/`, `/sk/`, `/de/`, `/pl/`, `/fr/`, `/es/`, `/it/`, `/nl/`. Překlady v `i18n/*.json`.
- Landing pages pro každý trh: obsah v `i18n/pages_content.py`, šablona v `i18n/pages.py`.
  - Tréninkový plán: `/hyrox-training-plan/`, `/cs/hyrox-treninkovy-plan/`, `/sk/hyrox-treningovy-plan/`, `/de/hyrox-trainingsplan/`, `/pl/plan-treningowy-hyrox/`, `/fr/programme-hyrox/`, `/es/plan-entrenamiento-hyrox/`, `/it/programma-allenamento-hyrox/`, `/nl/hyrox-trainingsschema/`
  - Online trenér: `/online-hyrox-coach/`, `/cs/online-hyrox-trener/`, `/sk/online-hyrox-trener/`, `/de/hyrox-online-coaching/`, `/pl/trener-hyrox-online/`, `/fr/coach-hyrox-en-ligne/`, `/es/entrenador-hyrox-online/`, `/it/coach-hyrox-online/`, `/nl/hyrox-online-coach/`
- Stránky programů (zatím EN + CS): obsah v `i18n/programs_content.py`, šablona v `i18n/programs.py`. URL `/programs/<program>/` a `/cs/programy/<program>/`. Ostatní jazyky odkazují „Details“ zatím na Strivee a kartu 12-Week Advanced nemají (bloky `<!--ADV-->` v `index.html`).
- Orientační ceny v €, £ a zł počítá `price()` v `pages_content.py` podle kurzů v `RATES`. Platí se vždy v CZK přes Strivee.
- Po každé změně spusť `python3 i18n/build.py`. Přegeneruje jazyky, landing pages i `sitemap.xml`.
