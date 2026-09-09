# Syncing with portfolio-template

This site was built from (or alongside) **portfolio-template**. The design —
layouts config, styling, the deploy workflow, page shells, build files — is
shared; your content is not.

## One-time setup (per clone)

```
git remote add template https://github.com/LalithaEvani/portfolio-template.git
```

## Pull design updates from the template

```
bin/sync-from-template
```

It fetches `template/main`, overwrites only the **shared** files listed in the
script, and stages them. Your personal files are never touched:

| Shared (script pulls these) | Personal (never touched) |
| --- | --- |
| `.github/workflows/`, `bin/`, `docs/` | `_pages/about.md` |
| `Gemfile*`, `package*.json`, `purgecss.config.js` | `_bibliography/papers.bib` |
| `Dockerfile`, `docker-compose*.yml` | `_data/socials.yml`, `_data/cv.yml` |
| `_pages/{404,cv,projects,publications}.md` | `_projects/*.md` |
| `_data/{coauthors,venues,citations}.yml` | `assets/img/prof_pic.jpg`, `assets/pdf/cv.pdf` |
| `assets/json/`, `robots.txt`, `LICENSE` | `README.md`, `CHANGES.md`, `TODO.md` |

Then review and commit:

```
git diff --cached
git commit -m "Sync shared files from portfolio-template" && git push
```

## `_config.yml`

Not auto-synced — it mixes shared settings (plugins, feature flags,
jekyll-scholar) with your name / URL / keywords. When the template changes it,
the script prints a `git diff` command; apply the shared hunks by hand.

## Sending an improvement back to the template

Make the change here, confirm it's generic (no personal data), then in a clone
of the template repo copy the file(s) over, commit, and push — or open a pull
request against `portfolio-template`.
