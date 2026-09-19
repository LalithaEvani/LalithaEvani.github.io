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
- [x] **3. Real publications** — done: all 3 papers from your Google Scholar
      profile, full details incl. DOIs (SemiHastakshar/ICVGIP 2025, Indic
      HTR/CVIP 2024, Text Summarization/ICAAIC 2023). The IDASCN 2022 paper
      from the resume isn't on Scholar, so it's left out — say the word if you
      want it added too. `selected_papers` is `false` in `_pages/about.md` —
      flip to `true` if you want a homepage list.
      → `_bibliography/papers.bib`, `_pages/about.md`
- [x] **4. Real CV PDF** — done: generated from `_data/cv.yml` by RenderCV on
      every deploy (`bin/build-cv-pdf.py`), so the PDF and the `/cv/` page
      always match. Edit `_data/cv.yml` to change both. A committed copy of
      `assets/pdf/cv.pdf` is the fallback if a render ever fails.
      → `_data/cv.yml`, `bin/build-cv-pdf.py`
- [x] **5. Fill the CV page data** — done, from your resume + transcript:
      Education, Experience, Projects, Skills, Certificates, summary. No phone
      number anywhere (kept out deliberately). Publications section still a
      placeholder — see item 3.
      → `_data/cv.yml`
- [x] **6. Real projects** — done, all 3: each links out to its own project
      page (Indic HTR, SemiHastakshar, Medical Document Summarization), with
      real content, real thumbnails, and `{% cite %}` pulling in the matching
      bib entry's Website/Code buttons.
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
- [ ] **11. Favicon** — currently the 🔬 emoji. Explore other options (a
      different emoji, or a real image via `apple_touch_icon:`) and pick one.
      → `_config.yml`
- [ ] **12. Project thumbnails** — resize (the 3 card images are each paper's
      own teaser figure at its original size/aspect ratio, not sized for a
      card thumbnail — inconsistent and sometimes oddly cropped) and
      reconsider whether the current images are the right ones to use as
      thumbnails at all.
      → `assets/img/{indic-htr-teaser,semihastakshar-teaser,textsumm-rouge-chart}.png`
- [ ] **13. Sign language avatar on the homepage** — accessibility feature;
      bigger/newer than the other items here, needs its own discussion on
      approach (e.g. a pre-rendered video/animation vs. a third-party
      avatar/signing service, which language — ISL presumably given the
      site's context, and where on the page it sits) before implementing.
      → `_pages/about.md`

- [ ] **20. CV page: look at more templates** — the `/cv/` page currently uses
      al-folio's default layout. Browse alternatives (other al-folio-style CV
      layouts, academic-site CV pages) and pick a nicer design.
      → `_pages/cv.md`, `_data/cv.yml`
- [ ] **21. CV PDF: can it match the Overleaf design?** — the auto-generated PDF
      (RenderCV, `bin/build-cv-pdf.py`) is plain next to the sidebar design made
      in Overleaf (`Lalitha_CV2 (3).pdf`). Investigate matching it while keeping
      it generated from `_data/cv.yml`: needs the Overleaf `.tex` source; options
      are a LaTeX template filled from `cv.yml` (LaTeX in CI) or another
      RenderCV theme. Public version must leave out phone, home address,
      Instagram, and the blank 2nd page.
      → `bin/build-cv-pdf.py`, `.github/workflows/deploy.yml`
- [ ] **22. Projects page: look at better templates** — the card thumbnails and
      the overall design don't look good. Browse project-page layouts for
      good card/thumbnail designs (extends item 12, which only covers resizing
      the current images).
      → `_pages/projects.md`, `_projects/`

## E. Research artifacts & repos (datasets, GitHub, course/independent-study work)

- [ ] **14. Upload the ICVGIP datasets** (SemiHastakshar paper — e.g. the
      Indic-HW-Wild unlabeled corpus and the datasets it's evaluated on),
      then link them from the paper's project page and repo README.
      → `SemiHastakshar` repo, `SemiHastakshar-page`
- [ ] **15. Dataset links for the CVIP paper** (Indic HTR — the
      IIIT-INDIC-HW-WORDS dataset it's trained/evaluated on): find or host
      the download link, then add it to the project page and repo README.
      → `Indic-HTR-CVIP-2024-page`, `Indic-HTR-CVIP-2024` repo
- [ ] **16. Bring GitHub up to date** for the CVIP paper, the ICVGIP paper,
      and the B.Tech project — READMEs, structure, links to the papers and
      project pages, anything stale or missing.
      → `Indic-HTR-CVIP-2024`, `SemiHastakshar`, B.Tech project repo
- [ ] **17. Course projects: DIP, INLP, SAL** — for each, get the repo in
      shape and write up a report, then build a project page for it (same
      paper-template pipeline as the paper pages, minus a paper), and add
      each to the site's `/projects/` cards.
      → 3 course-project repos (e.g. `SAL_Project`), 3 new project pages,
        `_projects/`
- [ ] **18. Independent study** — work on its repo, decide what to do with
      it (write-up? extend into something publishable? just tidy and archive?),
      and give it a project page.
      → independent-study repo, new project page, `_projects/`
- [ ] **19. Two B.Tech mini projects** — update the repos only (READMEs,
      cleanup); no project pages needed for these.
      → 2 B.Tech mini-project repos

## C. Optional housekeeping

- [ ] Delete `docs/` (al-folio's own manual) and `assets/json/resume.json`
      (unused with the `rendercv` CV format) for a leaner repo — or keep as reference.
- [ ] Custom domain: add a `CNAME` file, update `url` in `_config.yml`, point DNS.
- [ ] Leave giscus/disqus comments off for v1.

## D. Workflow for every change

1. Edit → `git add -A && git commit -m "…" && git push`
2. The **Deploy site** Action rebuilds; live in ~3–5 min (hard-refresh for the CDN).
3. Add a bullet to `CHANGES.md`.
