# Martin Davidsen — Personal Portfolio

Person-first portfolio site for job applications. Software & AI engineer framing
(not a company), so prospective employers see *me*, not a consultancy.

Shares its visual language with [codecraft.cc](https://codecrafts.cc) (same dark
theme, Inter, card styling) but the content is re-framed entirely in the first
person and leads with software/AI work, with the industrial track record as
supporting experience.

## Stack

Plain static site — no build step.

- `index.html` — single page, bilingual (EN / NO via `data-en` / `data-no`)
- `styles.css` — base shared with codecraft + personal-portfolio additions at the bottom
- `script.js` — language toggle, mobile menu, scroll animations, runtime-assembled email
- `images/` — portrait, project shots, company logos
- `Dockerfile` + `nginx.conf` — nginx:alpine container, same as codecraft

## Run locally

```bash
# any static server, e.g.
python -m http.server 8080
# or build the container
docker build -t martin-portfolio .
docker run --rm -p 8080:80 martin-portfolio
```

## Sections

Hero → About → What I Do → Selected Work → Experience (timeline) → Skills → Contact

## Notes

- Email address is base64-assembled at runtime in `script.js` to keep the
  plaintext out of the committed source (bot harvesting).
- Project descriptions are deliberately domain-generic, matching what's already
  public on codecraft.cc.
