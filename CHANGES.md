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

## 2026-09-18 — Temporary illustrated profile photo

- Added `assets/img/prof_pic.png` (square-cropped, 800x800) from an AI-generated
  illustrated avatar the user supplied, wired into `_pages/about.md` as a
  stand-in. Flagged in TODO.md as a placeholder to replace with a real photo
  before the site is shared with labs/committees.

## 2026-09-18 — Real bio

- Replaced the placeholder biography in `_pages/about.md` with the real one:
  CVIT / IIIT Hyderabad, advisors (Prof. C.V. Jawahar, Dr. Ajoy Mondal), OCR /
  Indic handwritten text recognition focus, research interests, industry /
  AI4SG goal, personal note. Checked off in TODO.md.

## 2026-09-18 -- Real CV data, trimmed About page

- `_pages/about.md`: removed the subtitle line under the name; set
  `selected_papers: false` (hides the homepage "selected publications" block
  until real entries are added).
- `_data/cv.yml`: filled in from the resume/transcript the user supplied
  locally (never committed -- see below): real Education, Experience,
  Projects, Skills, and a new Certificates section; summary and label
  updated. No phone number anywhere by design. Publications section stays a
  placeholder, deferred to a later pass.
- `_data/socials.yml`: added the real `linkedin_username`.
- `.gitignore`: added `Lalitha__Resume.pdf` and `MS_transcript.png` -- source
  documents used only locally to fill in CV data. The resume has a phone
  number and the transcript has a date of birth and roll number; neither
  file is committed or published.

## 2026-09-18 -- Trim About page copy

- Removed the "On this site you can find my publications..." navigation-pointer
  paragraph from `_pages/about.md` (redundant with the navbar links).

## 2026-09-18 -- Remove CV page Professional Summary

- Deleted `cv.summary` in `_data/cv.yml` -- removes the "Professional Summary"
  block from the /cv/ page.

## 2026-09-18 -- Real publications (2 of 3)

- `_bibliography/papers.bib` and `_data/cv.yml` Publications: added CVIP 2024
  ("Enhancing Accuracy in Indic Handwritten Text Recognition", authors from
  the resume, no DOI yet -- accepted but not yet published) and ICAAIC 2023
  ("Text Summarization of Medical Documents using Abstractive Techniques",
  full details incl. DOI, from the resume).
- IDASCN 2022 ("Chronic Disease Prediction...") intentionally left out --
  the resume did not list its authors or a DOI/link; not guessing at
  co-authors. Flagged as a TODO in both files.

## 2026-09-18 -- All 3 publications from Google Scholar

- `_bibliography/papers.bib` and `_data/cv.yml` Publications: replaced with
  the 3 papers on the user's Google Scholar profile
  (scholar.google.com/citations?user=6wlLRUcAAAAJ), full details incl. DOIs:
  SemiHastakshar (ICVGIP 2025), Enhancing Accuracy in Indic Handwritten Text
  Recognition (CVIP 2024, Springer LNCS -- now has the page range/DOI the
  resume was missing), and Text Summarization of Medical Documents (ICAAIC
  2023). The resume's IDASCN 2022 paper is not on Scholar, so left out.

## 2026-09-18 -- Link CVIP 2024 paper to its new project page

- `_bibliography/papers.bib`: added `website` (the new
  Indic-HTR-CVIP-2024-page project page) and `code` (the paper's existing
  training-code repo) fields to the `evani2024indichtr` entry -- adds
  Website/Code buttons on /publications/.

## 2026-09-18 -- Link first project card to Indic HTR

- `_projects/1_project.md`: replaced the placeholder with real content --
  problem/approach/results, `related_publications: true` +
  `{% cite evani2024indichtr %}` (pulls the Website/Code buttons in
  automatically), and a real thumbnail (`assets/img/indic-htr-teaser.png`,
  the India-by-script map from the paper). Links to the project page, paper,
  and code.

## 2026-09-18 -- Project pages for the other two papers

- New standalone project pages (same seemandhar/paper-template pipeline as
  the Indic HTR page): SemiHastakshar (ICVGIP 2025, paper self-hosted --
  CC BY 4.0 -- plus links to ACM DL and the existing SemiHastakshar code
  repo) and Text Summarization of Medical Documents (ICAAIC 2023, no code
  repo exists so only a paper link, out to IEEE Xplore -- copyright not
  confirmed open). Both built from the actual PDFs: real abstracts, real
  figures, real results tables, no invented numbers.
- `_bibliography/papers.bib` / `_data/cv.yml`: added `website`/`code`
  fields for both new entries; fixed the Text Summarization author order to
  match the paper's own byline (Evani, Deepak, Ramani, Bindu, Shahida,
  Shaikshavali) -- the earlier order, taken from Google Scholar's
  abbreviated author list, was wrong.
- `_projects/2_project.md` and `_projects/3_project.md`: same pattern as
  `1_project.md` -- real content, real thumbnail, `{% cite %}` pulling in
  the matching bib entry's buttons. All 3 project cards are now real.

## 2026-09-18 -- Fix Text Summarization author order (for real this time)

- The earlier "correction" to the paper's own byline was itself wrong: the
  PDF's author block is a 3-column grid, and raw text extraction reads it
  column-major (down col 1, then col 2, then col 3), not the true row-major
  reading order. Verified by rendering the actual PDF page as an image.
- True order: Evani Lalitha, Kasarapu Ramani, Dudekula Shahida, Esikela
  Venkata Sai Deepak, M. Hima Bindu, Diguri Shaikshavali -- which is what
  Google Scholar had all along. Reverted `_bibliography/papers.bib` and
  `_data/cv.yml` to that order; also fixed the Text-Summarization-ICAAIC-2023-page
  repo (index.html hero + BibTeX, README.md).
- Checked SemiHastakshar and Indic HTR author blocks too: both are single-row
  layouts with no column-major ambiguity, so those were already correct.

## 2026-09-18 -- Fix: site frozen since 11:00 GMT, real root cause

- Not a CDN caching issue after all. GitHub Pages' own secondary Jekyll
  build (the "pages build and deployment" step, separate from our custom
  "Deploy site" Action) has been failing on every push since commit
  e0636f61 -- because `gh-pages` had no `.nojekyll` file, so GitHub Pages
  tried to run Jekyll again on our already-built static output, using its
  restricted default plugin set (no jekyll-scholar etc.), and errored.
  The live site was stuck serving the last build that succeeded before that.
- Fixed in `.github/workflows/deploy.yml`: `touch _site/.nojekyll` before
  the Deploy step, so gh-pages always carries it and Pages just serves the
  static files without re-running Jekyll.

## 2026-09-18 -- Project card thumbnails link straight to project pages

- Added `redirect:` front matter to all 3 `_projects/*.md` files (al-folio's
  built-in support for this: `_includes/projects.liquid` links to
  `project.redirect` when set, instead of the internal detail page). Clicking
  a thumbnail on `/projects/` now opens the external project page directly.
  The internal detail pages (`/projects/1_project/` etc.) still exist and
  work if visited directly, just no longer linked from the listing.

## 2026-09-18 -- Add 2 TODO items

- TODO.md: added item 12 (resize + reconsider the 3 project card
  thumbnails) and reworded item 11 (favicon) to note exploring other
  options, not just picking a fixed replacement.

## 2026-09-18 -- Add TODO item: sign language avatar

- TODO.md: added item 13, a sign language avatar on the homepage
  (accessibility) -- flagged as needing its own approach discussion before
  implementation, unlike the smaller items around it.

## 2026-09-19 -- Add TODO items 14-19 (datasets, GitHub cleanup, course/independent-study work)

- TODO.md: new section E with items 14-19: upload the ICVGIP datasets, dataset
  links for the CVIP paper, bring GitHub up to date (CVIP, ICVGIP, B.Tech
  project), repos/reports/project pages for the DIP, INLP, and SAL course
  projects, independent-study repo + project page (and deciding what to do
  with it), and repo-only updates for the two B.Tech mini projects.

## 2026-09-19 -- CV PDF generated from cv.yml (one source of truth)

- `bin/build-cv-pdf.py` (new): maps `_data/cv.yml` into a RenderCV-valid
  document (RenderCV rejects some fields the web CV layout needs -- `label`,
  `image`, `studyType`, `releaseDate`, `end_date: Present` -- and wants
  others the web layout ignores) and renders `assets/pdf/cv.pdf`. `cv.yml`
  is never modified.
- `.github/workflows/deploy.yml`: new step runs it before `jekyll build`
  (RenderCV pinned to 2.8). `continue-on-error: true`, so a failed render
  serves the committed `assets/pdf/cv.pdf` instead of blocking the deploy.
  Editing `cv.yml` now updates the web CV and the PDF together.
- `assets/pdf/cv.pdf`: replaced the placeholder with the generated CV
  (committed as the fallback). No phone number, DOB, or roll number.
- Fixed a bug of mine: the web CV layout does not render the `score` field,
  so the CGPAs (8.8 / 9.06) never showed on `/cv/`. Moved them into
  `highlights`, which both the page and the PDF render.
- Added `doi` to the three publication entries (used by the PDF).
- `.gitignore`: `/.cv_build/` (generated RenderCV input); `requirements.txt`:
  `rendercv[full]==2.8`.

## 2026-09-19 -- Languages

- `_data/cv.yml`: Languages now Telugu (native), English (fluent), Hindi
  (fluent). Shows on the /cv/ page and in the generated PDF.
