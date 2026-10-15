# STR2G HYROX

Sales website for the STR2G online HYROX programs by Láďa and Ria Suchánek.

One static page (`index.html`), no build step. Every Start / Buy button links straight to checkout in the Strivee app.

## Programs on the site

| Program | Price | Type |
|---|---|---|
| HYROX Basic | CZK 750 / month | Monthly |
| HYROX Competitor | CZK 960 / month | Monthly |
| HYROX Pro Athlete | CZK 1,350 / month | Monthly |
| 12-Week HYROX Race Prep | CZK 1,900 | Race build |
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
