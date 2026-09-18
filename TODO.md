# TODO — finish version 1

From the default al-folio template to a complete, filled-in site. Everything
below is a placeholder that was scaffolded in; search the repo for `TODO` to
jump to each spot. Roughly most-visible-first.

## A. Blocking — the site currently shows placeholder or broken text

- [x] **1. Write the bio** — done: CVIT, advisors, OCR/Indic HTR focus,
      research interests, industry/AI4SG goal, personal note.
      → `_pages/about.md` (lines ~26–39)
- [ ] **2. Replace the profile photo** — currently a **temporary illustrated
      placeholder** (`assets/img/prof_pic.png`), not a real photo. Swap for an
      actual headshot before this site goes in front of anyone (labs,
      committees) — not standard for a research portfolio. See the chat for why.
      → `assets/img/prof_pic.jpg`
- [ ] **3. Real publications** — CVIP 2024 and ICAAIC 2023 added (ICAAIC has
      full details; CVIP is missing a DOI/link until the proceedings are
      published). Still missing: **IDASCN 2022** ("Chronic Disease Prediction
      using Supervised Learning Techniques") — need the full author list and a
      DOI/link, resume didn't have them. `selected_papers` is `false` in
      `_pages/about.md` — flip to `true` if you want a homepage list.
      → `_bibliography/papers.bib`, `_pages/about.md`
- [ ] **4. Real CV PDF** — deferred; you're editing your own version to publish.
      Replace the generated placeholder, keep the filename `cv.pdf`.
      → `assets/pdf/cv.pdf`
- [x] **5. Fill the CV page data** — done, from your resume + transcript:
      Education, Experience, Projects, Skills, Certificates, summary. No phone
      number anywhere (kept out deliberately). Publications section still a
      placeholder — see item 3.
      → `_data/cv.yml`
- [ ] **6. Real projects** — replace the 3 placeholder cards (problem / approach /
      results / links) or delete extras. Swap the stock images
      `assets/img/{1,3,7}.jpg` for your own figures, or remove the `img:` line.
      → `_projects/1_project.md`–`3_project.md`
- [ ] **7. Social links** — GitHub + LinkedIn done. Still need
      `scholar_userid` (uncomment and fill once you have a Scholar profile);
      confirm `email` is the address you want public.
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
