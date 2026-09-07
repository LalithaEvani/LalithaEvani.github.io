# LalithaEvani.github.io

Personal academic website of **Lalitha Evani** — MS researcher in computer vision
and machine learning at IIIT Hyderabad.

Live at <https://LalithaEvani.github.io>.

Built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme
(MIT licensed — see `LICENSE`).

## How it deploys

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site
with Jekyll and publishes the generated `_site/` to the `gh-pages` branch.
GitHub Pages then serves `gh-pages` at the URL above.

**One-time setup:** after the first successful Actions run, go to
**Settings → Pages → Build and deployment** and set **Source: Deploy from a branch**,
**Branch: `gh-pages` / `(root)`**.

## Editing content

| What | Where |
| --- | --- |
| Bio, affiliation, profile photo | `_pages/about.md`, `assets/img/prof_pic.jpg` |
| Publications | `_bibliography/papers.bib` |
| CV page sections | `_data/cv.yml` |
| CV PDF (download button) | `assets/pdf/cv.pdf` |
| Projects | `_projects/*.md` |
| Social links (GitHub / Scholar / LinkedIn) + email | `_data/socials.yml` |
| Site title, URL, name | `_config.yml` |

Search the repo for `TODO` to find every placeholder.

## Local preview (optional)

Requires Ruby. `bundle install` then `bundle exec jekyll serve`, or use the
provided `docker-compose.yml`.
