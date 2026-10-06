# EnCompass e.V. — Website

The public website of **EnCompass e.V.**, a non-profit association based in Berlin that works to spread liberal values, open society and personal freedoms in Germany and abroad.

It is a single static page with no build step and no dependencies. It is available in English, German and Arabic.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The whole page: markup, inline SVG logos and the small script for language switching and the mobile menu |
| `style.css` | All styles. The colours and layout values are CSS variables in `:root` |
| `translations.js` | The text of the page in each language (`en`, `de`, `ar`) |
| `events/` | Calendar files (`.ics`) for the "Add to Calendar" buttons |
| `.github/workflows/` | GitHub Actions workflows that deploy the site to GitHub Pages |

## Page content

The page is one long scroll. The navigation bar links to each section by its anchor.

1. **Navigation**: compass logo, links (About, What We Do, Events, Membership, Contact), the EN / DE / AR language switcher, and a hamburger menu on small screens.
2. **Hero** (`#home`): "Berlin · Est. 2024". The headline is *Advancing Liberal Values & Personal Freedoms*, with buttons to *Our Mission* and *Join Us*.
3. **About** (`#about`): who the association is and why it exists. Three key facts:
   - Based in Berlin, registered e.V. under German law
   - International reach, with activities in Germany and abroad
   - Non-profit, recognised under §52 AO
4. **What We Do** (`#work`): four areas of activity:
   - **Art & Culture**: artistic projects and cultural events that support freedom of expression
   - **Media & Content**: print, digital and broadcast content about liberal values
   - **Workshops & Seminars**: educational events for practitioners, academics, students and the public
   - **Authors & Academics**: platforms, funding and networks for writers and researchers
5. **Events** (`#events`): upcoming events, each with buttons to add it to a calendar and to get directions. The current event is:
   - **Berlin Voted — Now What?** (*برلين صوّتت، هلأ شو؟*): an open discussion in Arabic about the election results. Saturday 7 November 2026, 7 pm, at Casino for Social Medicine, Sonnenallee 100, 12045 Berlin
6. **Membership** (`#membership`): the three types of membership:
   - **Ordinary (Active) Member**: pays fees and volunteers. Full voting rights and can stand for election
   - **Honorary Member**: appointed by the General Assembly. Full voting rights
   - **Supporting Member**: gives financial support only. Open to legal entities. No voting rights
7. **Contact** (`#contact`): address (Berlin), email `info@encompass.ngo`, legal status, and a contact form (name, email, subject, message).
8. **Footer**: logo, tagline, links to the sections and membership types, and the legal line.

> **Contact form:** the site has no backend, so **Send Message** opens **Gmail** in a new tab with an email to `info@encompass.ngo` already filled in. The subject is filled in, and the visitor's name and email are added at the end of the message. A note then tells them to press Send. For visitors who don't use Gmail, the note links to the same email as a `mailto:` link, which opens their default email app, and also gives the address. The code is `handleSubmit()` and `draftEmail()` in `index.html`.

## Languages

All text that can be translated is marked in `index.html` with one of these attributes:

- `data-i18n="key"`: replaces the element's text
- `data-i18n-html="key"`: replaces the element's HTML (used for text with `<br>`, `<em>` and similar tags)
- `data-i18n-placeholder="key"`: replaces an input's placeholder

The text for each key is in `translations.js`. Choosing a language also sets `lang` and `dir` on `<html>`, so Arabic is shown right to left. The language can be set in the link with the `lang` parameter:

- `https://encompass.ngo/?lang=en`: English
- `https://encompass.ngo/?lang=de`: German
- `https://encompass.ngo/?lang=ar`: Arabic

Section anchors still work, for example `?lang=ar#events`. When a visitor switches language, the `lang` parameter in the address bar changes too, so a copied link opens in the same language. Without the parameter, the page uses the visitor's last choice (saved in `localStorage` under `preferred-lang`), or English if they have never chosen one. An unknown value, such as `?lang=fr`, is ignored.

**To change text:** edit the key in all three languages in `translations.js`. The English text in `index.html` is only a fallback.
**To add a language:** add a new object to `translations.js` and a new `.lang-btn` button with a matching `data-lang`.

## Design

- Theme: a compass, in navy `#1E3A5F` (`--color-primary`) and gold `#C9A227` (`--color-accent`)
- Font: the system font stack, so no web fonts are loaded
- Logos and illustrations are inline SVG, so there are no image files

## Running locally

Open `index.html` in a browser. If you prefer a local server:

```sh
python -m http.server 8000
```

## Deployment

Every push to `master` deploys the repository root to **GitHub Pages** using GitHub Actions. It can also be started by hand from the Actions tab.
