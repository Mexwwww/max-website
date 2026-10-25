# Max Geurts — Developer Portfolio

Complete static portfolio redesign, based on the supplied brief and the original `Mexwwww/portfolioFromMax` staticSoftwareDev branch.

## Contents

- `dist/`: the complete, ready-to-host website, including the newest supplied Dutch software CV, compressed project videos, original generated-site ZIP and optimised images.
- `redesign/projects.json`: authoritative project text, technology lists and existing project URLs.
- `redesign/build.py`: dependency-free Python 3 static page generator.
- `redesign/style.css` and `main.js`: shared responsive design and progressive enhancements.
- `redesign/check.py`: checks generated links, downloads, image references, heading counts, metadata and IDs.
- `.github/workflows/pages.yml`: GitHub Pages deployment workflow.

## Edit and build

Change project content in `redesign/projects.json`. Update the homepage or shared page templates in `redesign/build.py`. Run:

```sh
python3 redesign/build.py
python3 redesign/check.py
```

Committed `dist/` includes all media and documents; no download, package installation or image processing is needed for this build. The Python build deliberately retains those assets. The site also opens directly from `dist/index.html` and needs no backend. JavaScript only enhances navigation and project filters; all project content is generated as HTML.

## Publish as a NEW GitHub website

1. Create a new repository, for example `max-geurts-portfolio`.
2. Put the CONTENTS of this package at the repository root, including the `.github` directory. Do not upload the ZIP itself as the website.
3. Choose Settings → Pages → Build and deployment → Source: GitHub Actions.
4. Manually run the “Deploy static portfolio to GitHub Pages” workflow from Actions.
5. Use the final URL returned by the successful deployment. The workflow sets the canonical base URL from GitHub's Pages configuration.

No existing repository, default branch or Pages setting has been changed by this package. The source has been prepared for lucasjmgeurts-jpg/max-website. GitHub Pages deployment is optional and has not been enabled or verified.

## Publish to Max's EXISTING portfolio repository

The original repository's default branch is `master`, but its live homepage was verified byte-for-byte against `staticSoftwareDev/index.html` on 25 October 2026. No `.github` workflow exists in the checked static branch. The administrative Pages source setting could not be read through the connection, so confirm it in Settings → Pages before publishing.

Review the redesign in a separate branch. Keep the original source material if desired; this design publishes only `dist/`. Use the included Actions workflow only after confirming Pages is set to GitHub Actions. Do not point branch-based Pages at the repository root while the built homepage remains in `dist/`. Alternatively, copy the CONTENTS of `dist/` to the actual Pages publishing branch/root without changing the existing publishing method.

The default canonical URL is `https://lucasjmgeurts-jpg.github.io/max-website/`. For another host, set `PORTFOLIO_URL` when building:

```sh
PORTFOLIO_URL=https://example.com/ python3 redesign/build.py
```

For a GitHub project page, include the repository path. All navigational and asset links are relative, so the site works in a subdirectory.

## Source and attribution

The professional project descriptions are based on the supplied brief, the current software CV and the original public case pages. Business source code is not included. Conceptual diagrams and fictional example figures are labelled as illustrations.

The website redesign was implemented with AI assistance. The portfolio case explicitly distinguishes this redesigned implementation from Max's original Laravel/Blade and static portfolio work. Do not imply Max independently authored this redesign.

Original game images and footage, portrait and the permitted generated-site ZIP come from the original portfolio. Images were converted to WebP; five selected videos were transcoded to smaller MP4 files with no autoplay.

## Pending confirmations

- No verified LinkedIn URL was found. No placeholder LinkedIn link is published. Add the correct profile URL when supplied.
- The email `m.t.j.geurts@gmail.com`, completion of education and 32-hour availability come from the current supplied CV.
- Business project descriptions and employment details should receive Max's final factual review before he uses the site for applications.
- No production deployment, mail delivery, Lighthouse score or assistive-technology audit is claimed.

## Validation performed

- Complete build and link/asset/download checks on 18 static pages.
- JavaScript syntax check.
- Browser inspection of homepage and financial case study.
- Homepage rendered in iframe viewports of 375, 768 and 1440 px; no horizontal document overflow observed.
- Financial case at 375 px, AI case at 768 px and prototype case at 1440 px; no horizontal document overflow observed.
- Mobile menu opened successfully; project filtering returned exactly five game projects.
- Prototype archive verified to contain 28 HTML pages.
- No site JavaScript error was observed during these interactions; the browser's own extension emitted unrelated metadata errors.

Keyboard focus and reduced motion are implemented in CSS, but no full screen-reader audit or automated Lighthouse audit was performed.
