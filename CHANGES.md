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
- The count line stays hidden until it reaches 1, so a freshly deployed site
  never shows "0 visits" (lower the threshold in `_pages/about.md` to always
  show it).

## 2026-09-07 — Version 1 checklist

- Added `TODO.md` at the repo root: the checklist of placeholders to fill in
  (bio, photo, publications, CV PDF + data, projects, social links) to take the
  site from template to a finished v1.

## 2026-09-07 — Profile photo

- Replaced the stock al-folio `assets/img/prof_pic.jpg` with a processed version
  of `profile_photo.jpeg`: square head-and-shoulders crop, mild white balance /
  brightness / contrast cleanup, upscaled to 800×800 (LANCZOS + light unsharp —
  interpolation, not AI super-resolution).
- The original `profile_photo.jpeg` is kept locally but git-ignored, for future
  re-crops or the planned formal-wear edit.
- Still worth improving later: it is a night shot with a busy background.

## 2026-09-10 — Link to portfolio-template

- Created a sibling `portfolio-template` repo (generic placeholders) so new
  sites can be started from it and design changes can be shared.
- Added `bin/sync-from-template` and `docs/TEMPLATE-SYNC.md`: run the script to
  pull only the shared/design files from the `template` remote; personal
  content (bio, publications, CV, projects, photo, name/URL in `_config.yml`,
  README/CHANGES/TODO) is never touched. `_config.yml` is reviewed by hand.
- A plain `git merge template/main` is *not* used — the two repos have separate
  histories and a merge would overwrite personal files.

## 2026-09-17 — Remove profile photo

- Deleted `assets/img/prof_pic.jpg` (the site copy) and `profile_photo.jpeg`
  (the local-only original). Commented out `profile.image` in `_pages/about.md`
  so the About page renders without a photo. Add a new `assets/img/prof_pic.jpg`
  and uncomment that line to show a photo again.

## 2026-09-18 — Unpin the footer

- `footer_fixed: false` in `_config.yml` — the copyright bar was pinned to the
  bottom of the viewport while scrolling; now it sits at the end of the page
  like a normal footer.

## 2026-09-18 — Footer still pinned: override the include directly

- `footer_fixed: false` alone did not change the rendered footer class (still
  `fixed-bottom` on a fresh build from that exact commit) — root cause in the
  al_folio_core 1.0.15 theme gem was not pinned down.
- Added `_includes/footer.liquid` (site-level override — Jekyll uses a
  same-path file in the site over the theme gem's) hard-coding the
  non-fixed "sticky-bottom" footer, bypassing the flag entirely.
