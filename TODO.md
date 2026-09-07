# TODO — finish version 1

From the default al-folio template to a complete, filled-in site. Everything
below is a placeholder that was scaffolded in; search the repo for `TODO` to
jump to each spot. Roughly most-visible-first.

## A. Blocking — the site currently shows placeholder or broken text

- [ ] **1. Write the bio** — 2–3 short paragraphs (what you work on, background,
      roles you're seeking). Right now the live page reads *"Before my MS, I ."*
      and *"interested in ."* because the TODO comments are empty.
      → `_pages/about.md` (lines ~26–39)
- [ ] **2. Replace the profile photo** — current one is a stock al-folio image.
      Square, ≥ 400×400, ideally < 500 KB, keep the filename.
      → `assets/img/prof_pic.jpg`
- [ ] **3. Real publications** — swap the 2 fake BibTeX entries for real papers
      (Google Scholar → "Cite" → BibTeX). Add `selected={true}` to the 1–3 to
      feature on the homepage. No papers yet? Add an "under submission" entry, or
      set `selected_papers: false` in `_pages/about.md` to hide the homepage list.
      → `_bibliography/papers.bib`
- [ ] **4. Real CV PDF** — replace the generated placeholder, keep the filename.
      → `assets/pdf/cv.pdf`
- [ ] **5. Fill the CV page data** — name, label, summary, Education, Experience,
      Publications, Skills, Languages; fix the guessed dates; delete unused
      sections.
      → `_data/cv.yml`
- [ ] **6. Real projects** — replace the 3 placeholder cards (problem / approach /
      results / links) or delete extras. Swap the stock images
      `assets/img/{1,3,7}.jpg` for your own figures, or remove the `img:` line.
      → `_projects/1_project.md`–`3_project.md`
- [ ] **7. Social links** — uncomment and fill `scholar_userid` and
      `linkedin_username`; confirm `email` is the address you want public.
      → `_data/socials.yml`

## B. Recommended polish for a research-application site

- [ ] **8. Contact block** under the photo — real office / how to find you, or trim.
      → `_pages/about.md` (`profile.more_info`)
- [ ] **9. News feed (optional, adds life)** — create `_news/announcement_1.md`
      etc. with 2–3 items, then set `announcements.enabled: true`.
      → `_news/`, `_pages/about.md`
- [ ] **10. Link previews / SEO** — set `serve_og_meta: true`,
      `serve_schema_org: true`, add an `og_image` PNG in `assets/img/`.
      Optionally add `google_site_verification`.
      → `_config.yml`
- [ ] **11. Favicon** — currently the 🔬 emoji; set a custom `icon:` /
      `apple_touch_icon:` if desired.
      → `_config.yml`

## C. Optional housekeeping

- [ ] Delete `docs/` (al-folio's own manual) and `assets/json/resume.json`
      (unused with the `rendercv` CV format) for a leaner repo — or keep as reference.
- [ ] Custom domain: add a `CNAME` file, update `url` in `_config.yml`, point DNS.
- [ ] Leave giscus/disqus comments off for v1.

## D. Workflow for every change

1. Edit → `git add -A && git commit -m "…" && git push`
2. The **Deploy site** Action rebuilds; live in ~3–5 min (hard-refresh for the CDN).
3. Add a bullet to `CHANGES.md`.
