#!/usr/bin/env python3
"""Build assets/pdf/cv.pdf from _data/cv.yml, so the web CV page and the PDF
always come from the same data.

Why a converter instead of feeding cv.yml to RenderCV directly: the web CV
layout (al_folio_cv) reads a few fields RenderCV's schema rejects (`label`,
`image`, `studyType`, `releaseDate`, `end_date: Present`, ...), and RenderCV
wants some shapes the web layout doesn't (`degree`, `journal`, one-line skills).
This script maps cv.yml into a RenderCV-valid document, writes it to a scratch
dir, and runs RenderCV on it. cv.yml itself is never modified.

Usage (from the repo root):
    pip install pyyaml "rendercv[full]==2.8"    # needs Python >= 3.12
    python bin/build-cv-pdf.py

Output: assets/pdf/cv.pdf (overwrites the committed fallback copy).
The deploy workflow runs this before `jekyll build`; if it fails, the deploy
still proceeds and the last committed cv.pdf is served instead.
"""
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_data" / "cv.yml"
BUILD_DIR = ROOT / ".cv_build"  # dot-dir: git-ignored and skipped by Jekyll
OUT_PDF = ROOT / "assets" / "pdf" / "cv.pdf"

# Sections rendered as "Label: details" one-liners instead of full entries.
ONE_LINE_SECTIONS = {"Skills", "Languages", "Interests"}

DESIGN = {
    "theme": "classic",
    "page": {"size": "a4", "show_footer": False, "show_top_note": False},
    "sections": {"show_time_spans_in": []},
    # Education entries reserve a 1cm "degree" column even when unused (the
    # degree is folded into `area` instead), which indents them vs. other sections.
    "entries": {"degree_width": "0cm"},
}


def date(value):
    """cv.yml dates -> RenderCV dates ('2024', '2023-08', 'present')."""
    if value is None or value == "":
        return None
    if isinstance(value, int):
        return value
    text = str(value).strip()
    if text.lower() == "present":
        return "present"
    if re.fullmatch(r"\d{4}", text):
        return int(text)  # year-only: RenderCV prints ints as-is, but "2025" as "Jan 2025"
    return text


def compact(entry):
    """Drop empty values so RenderCV doesn't see blank fields."""
    return {k: v for k, v in entry.items() if v not in (None, "", [], {})}


def dates(src):
    """Carry over either a single `date` or a start/end range."""
    if src.get("date") is not None and src.get("start_date") is None:
        return {"date": date(src["date"])}
    return {"start_date": date(src.get("start_date")), "end_date": date(src.get("end_date"))}


def education(e):
    degree = e.get("studyType") or e.get("degree")
    area = e.get("area")
    return compact({
        "institution": e.get("institution"),
        "area": f"{degree} in {area}" if degree and area else (area or degree),
        "location": e.get("location"),
        **dates(e),
        "summary": e.get("summary"),
        "highlights": e.get("highlights"),
    })


def experience(e):
    return compact({
        "company": e.get("company") or e.get("name"),
        "position": e.get("position"),
        "location": e.get("location"),
        **dates(e),
        "summary": e.get("summary"),
        "highlights": e.get("highlights"),
    })


def publication(e):
    return compact({
        "title": e.get("title"),
        "authors": e.get("authors"),
        "doi": e.get("doi"),
        "journal": e.get("publisher"),
        "date": date(e.get("releaseDate") or e.get("date")),
        "url": e.get("url"),
        "summary": e.get("summary"),
    })


def one_line(e):
    return compact({
        "label": e.get("name"),
        "details": e.get("keywords") or e.get("summary") or e.get("level"),
    })


def award(e):
    summary = ". ".join(x for x in (e.get("awarder"), e.get("summary")) if x)
    return compact({"name": e.get("title"), "date": date(e.get("date")), "summary": summary})


def certificate(e):
    summary = ". ".join(x for x in (e.get("issuer"), e.get("summary")) if x)
    return compact({"name": e.get("name"), "date": date(e.get("date")), "summary": summary})


def normal(e):
    return compact({
        "name": e.get("name") or e.get("title"),
        "location": e.get("location"),
        **dates(e),
        "summary": e.get("summary") or e.get("reference"),
        "highlights": e.get("highlights"),
    })


def convert_entry(section, e):
    if section in ONE_LINE_SECTIONS:
        return one_line(e)
    if "institution" in e:
        return education(e)
    if "company" in e or "position" in e:
        return experience(e)
    if "authors" in e and "title" in e:
        return publication(e)
    if "awarder" in e:
        return award(e)
    if "issuer" in e:
        return certificate(e)
    return normal(e)


def build_document(cv):
    person = {
        "name": cv["name"],
        "headline": cv.get("label"),
        "location": cv.get("location"),
        "email": cv.get("email"),
        "social_networks": [
            {"network": s["network"], "username": s["username"]}
            for s in cv.get("social_networks", [])
        ],
        "sections": {
            title: [convert_entry(title, e) for e in entries]
            for title, entries in (cv.get("sections") or {}).items()
            if entries
        },
    }
    return {
        "cv": compact(person),
        "design": DESIGN,
        "locale": {"language": "english"},
        "settings": {
            "bold_keywords": [cv["name"]],  # bold your own name in author lists
            "render_command": {
                "typst_path": str(BUILD_DIR / "cv.typ"),
                "pdf_path": str(OUT_PDF),
                "dont_generate_markdown": True,
                "dont_generate_html": True,
                "dont_generate_png": True,
            },
        },
    }


def main():
    cv = yaml.safe_load(SRC.read_text(encoding="utf-8"))["cv"]
    BUILD_DIR.mkdir(exist_ok=True)
    generated = BUILD_DIR / "cv_render.yaml"
    generated.write_text(
        yaml.safe_dump(build_document(cv), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run([sys.executable, "-m", "rendercv", "render", str(generated)])
    if result.returncode != 0:
        sys.exit(f"RenderCV failed (exit {result.returncode}); see output above.")
    print(f"Wrote {OUT_PDF.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
