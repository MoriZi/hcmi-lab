# HCMI Brand Kit

Source brand assets for the HCMI Lab. This folder is reference material: Hugo does not
build or publish it. Web-ready copies used by the site live in `static/images/`.

## Contents

| Path | What it is |
|---|---|
| `logo/hcmi-logo-primary.png` / `.svg` | Primary logo, navy lettering. Use on light backgrounds. |
| `logo/hcmi-logo-bright.png` / `.svg` | Bright logo, light lettering. Use on dark backgrounds. |
| `visual/color-palette.md` | Brand colour direction. |
| `visual/typography.md` | Brand typefaces. |
| `linkedin/Paper-Visual-Template.png` | Layout template for LinkedIn paper announcements. |

The `.svg` files wrap the PNG artwork (an embedded raster image), so they do not scale
like true vector logos. Use the PNGs, or ask the designer for vector originals.

## Where the website uses these

| Brand asset | Website copy | Used in |
|---|---|---|
| `logo/hcmi-logo-primary.png` | `static/images/hcmi-logo-primary.png` (resized to 144px tall) | Header, `layouts/partials/components/headers/navbar.html` |
| `logo/hcmi-logo-bright.png` | `static/images/hcmi-logo-bright.png` | Footer, `layouts/partials/site_footer.html` |

To update a logo, replace the file here, then regenerate the web copy in `static/images/`
at the size noted above.

## Website design tokens

The website's colours and fonts are defined once, as CSS custom properties at the top of
`assets/scss/template.scss` (section 1, "CSS VARIABLES"). The site's 2026 visual refresh
evolved the palette and heading font beyond the notes in `visual/`:

| | Brand kit (`visual/`) | Website (`template.scss`) |
|---|---|---|
| Primary navy | `#0B2A4A` | `#102E4F` (`--hcmi-navy`) |
| Accent | `#C9A227` gold | `#B38A43` aged brass (`--hcmi-brass`) |
| Background | `#FFFFFF` | `#F7F5F0` warm ivory (`--hcmi-ivory`) |
| Headings | Source Serif 4, 600 | Newsreader, 600 (`--font-display`) |
| Body / UI | Inter | Inter (`--font-ui`) |

If the refreshed values become the official brand, update `visual/` to match.
