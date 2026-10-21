# Tara Hayes, Realtor — Knoxville & East Tennessee

Jekyll static site deployed via **GitHub Actions** (same architecture as Britney's & Karen's sites).
~46 pages: home (video hero), about, reviews, contact, search, valuation, 10 service pages,
30 area pages, blog — plus an auto-publishing blog calendar.

## ⚙️ ONE-TIME SETUP (required before the site goes live)
In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**.
The first push triggers `deploy-pages.yml`; the site lands at
`https://westyn3.github.io/tara-hayes-realtor/`.

## How the blog auto-publishes
- Posts live in `_posts/`, dated every **Friday from Oct 23, 2026 → Jan 1, 2027** (11 posts).
- `_config.yml` sets `future: false`, so future-dated posts are excluded from builds.
- `.github/workflows/publish-scheduled-posts.yml` rebuilds and redeploys the site daily
  (two UTC crons for redundancy) — each run publishes whatever has become due. No manual steps.
- Homepage and `/blog.html` list posts automatically; `sitemap.xml` and `feed.xml` update themselves.

## Domain cutover (when the new domain is picked)
1. In `_config.yml`: set `url:` to the new domain, `baseurl:` to `""`.
2. Add a `CNAME` file containing the bare domain; configure DNS (A records / CNAME → GitHub Pages).
3. Settings → Pages → Custom domain + Enforce HTTPS.
4. Update the GBP website link, GSC domain property, and re-submit `sitemap.xml`.
Everything else (canonicals, OG, schema, sitemap, feed) flows from those two config lines.

## Fill-ins before/at launch
- **Formspree:** replace `REPLACE_FORM_ID` in `contact.html` and `home-valuation.html`.
- **GA4:** uncomment + fill the gtag snippet in `_layouts/default.html` (same property as before).
- **Images:** `images/og-tara-hayes.jpg` is currently the hero poster — swap for a branded
  1200×630 with Tara's headshot when ready. Add a real headshot to About.
- **IDX:** marked `IDX EMBED GOES HERE` blocks on `search.html` + every `areas/` page.
  Stopgap: Flexmls "IDX 2.0 lite" link (Tara: Flexmls → Preferences → IDX Manager).
  Production: Buying Buddy / IDX Broker / iHomefinder (all approved East TN REALTORS® vendors),
  forced registration ON, leads → her CRM.
- **Reviews page:** quotes are from her real public Google/Zillow reviews (lightly trimmed);
  confirm Tara's comfortable featuring them, swap in attributions with permission.
- **Area pages:** each has a TODO to expand to 500–800 words. Priority: Farragut, Hardin Valley,
  West Knoxville, Maryville, Tellico Village.

## Compliance (don't remove)
Footer on every page: Realty Executives Associates, office line (865) 693-3232, broker address,
TN License #333578, Equal Housing — TN advertising rules. Tara's direct (865) 242-8010 is the
header CTA and schema phone. Site credit: Knoxline Systems.

## Structure
- `_layouts/default.html` — all chrome + full SEO head (canonical, OG, Twitter, geo, RealEstateAgent
  + breadcrumb JSON-LD). Page content files carry front matter (title/description/crumb) only.
- `_layouts/post.html` — blog post wrapper with BlogPosting schema + related posts.
- `css/style.css` — design tokens at top (pine/brass/ivory, Fraunces/Archivo).
- Hero video: `hero.mp4` (desktop) / `hero-mobile.mp4` / `hero-poster.jpg`.
