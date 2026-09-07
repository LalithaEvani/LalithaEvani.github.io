# Change log

What this repository changes relative to a stock [al-folio](https://github.com/alshedivat/al-folio)
checkout. The authoritative history is `git log`; this file is a human summary.

## 2026-09-07 — Initial setup

**Site configuration (`_config.yml`)**
- `first_name` / `last_name` set to `Lalitha` / `Evani`; `title` left blank so the
  full name is used; new `keywords`, `description`, favicon.
- `url: https://LalithaEvani.github.io`, `baseurl: ""` (GitHub user page).
- `scholar.first_name` / `scholar.last_name` set for jekyll-scholar.
- `enable_publication_thumbnails: false`, `enable_project_categories: false`,
  `enable_publication_badges.inspirehep: false`.
- Collections trimmed to `news` and `projects` (removed `books`, `teachings`).

**Content — all real text is a placeholder marked `TODO`**
- `_pages/about.md` — bio, IIIT Hyderabad subtitle, contact block; homepage
  announcements and latest-posts panels disabled; visitor counter block added.
- `_bibliography/papers.bib` — two template BibTeX entries + field cheatsheet.
- `_data/cv.yml` — placeholder Education / Experience / Publications / Skills.
- `_pages/cv.md` — download button points at `assets/pdf/cv.pdf`.
- `_projects/1_project.md … 3_project.md` — three placeholder cards.
- `_data/socials.yml` — GitHub + email live; Google Scholar and LinkedIn are
  commented out with instructions.
- `_data/coauthors.yml`, `_data/venues.yml` — replaced demo data with CV/ML stubs.
- `assets/pdf/cv.pdf` — generated one-page placeholder; replace with your real CV.

**Removed (demo cruft / not needed for a portfolio)**
- Demo pages: `blog`, `books`, `teaching`, `repositories`, `people`, `submenus`,
  `plugins`, `about_einstein`.
- Collections/content: `_posts/`, `_news/`, `_books/`, `_teachings/`.
- ~40 MB of demo media under `assets/` (video, audio, plotly, jupyter, extra
  images), al-folio's own `.github` project meta, and dev-only dotfiles
  (`.prettierrc`, `.pre-commit-config.yaml`, …).
- All GitHub workflows **except** `.github/workflows/deploy.yml`.

**Deployment**
- `deploy.yml` builds with Jekyll on every push to `main` and publishes `_site/`
  to the `gh-pages` branch. GitHub Pages must be set to serve from `gh-pages`
  (Settings → Pages → Deploy from a branch).

## 2026-09-07 — CI build fix

- Removed the blog/archives stack that broke the build: `jekyll-archives-v2`
  (crashed on the now-deleted `books` collection) and `jekyll-paginate-v2`,
  plus their config blocks.
- `external_sources: []` — stop fetching Medium/Google RSS during the build.
- Restored `assets/json/resume.json` (read by `jekyll_get_json`) and added an
  empty `_data/citations.yml` stub.

## 2026-09-07 — Visitor counter

- Added an optional GoatCounter visitor count at the bottom of the home page,
  controlled by `goatcounter_code` in `_config.yml` (hidden while blank).
- Enabled it with code `lalithae`.
- Replaced GoatCounter's `TOTAL.svg` badge image with a small plain-text count
  fetched from the `TOTAL.json` endpoint and styled to match the site
  typography (muted, centred, eye icon). It renders only after the count
  loads and hides silently on any error.
