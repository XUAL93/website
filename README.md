# Aolong Xu - Personal Website

English academic website for Aolong Xu, PhD Fellow at Ghent University.

## Content

- `content/authors/admin/_index.md`: profile, contact, education, work, teaching, and interests.
- `content/_index.md`: detailed research copy.
- `content/publication/`: publications with explicit status labels.
- `layouts/`: custom page templates.
- `static/css/site.css`: responsive typography and layout.
- `static/favicon.svg`: personal AX browser icon.
- `static/uploads/resume.pdf`: current downloadable CV.

## Preview

Use Hugo 0.136.5:

```sh
hugo server
```

The templates and stylesheet are local. No external theme or Go module download is required.

## Rebuild the CV

Install `reportlab` and `PyYAML`, then run:

```sh
python scripts/build_cv.py
```

The script preserves the original source PDF and updates the website download. Publication and reference details should be reviewed when their status changes.

## Deploy

Commit source changes to `main`. The existing GitHub Pages workflow builds and publishes the site.

For browser uploads, retain the repository-relative paths for `content`, `config`, `layouts`, `static`, and `scripts`. Generated preview and build files are not needed.

Starter examples remain on disk as drafts and are excluded from processing in the site configuration. The upstream license is retained in LICENSE.md.
