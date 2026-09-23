# Tara Hayes, Realtor — Static Site (GitHub Pages)

24-page static build. Brand: **Tara Hayes, Realtor / The Broker in a Hat** (H2 Home Group retired).
Full spec (metadata source of truth): the "Tara Hayes Site Build Spec" doc.

## Before launch — find/replace + fill-ins
1. **Domain:** `https://www.tarahayesrealtor.com` is the placeholder in every canonical, OG tag,
   schema block, robots.txt, and sitemap.xml. If the final domain differs, find/replace across the repo.
   Add a `CNAME` file with the bare domain when DNS is ready.
2. **Formspree:** replace `REPLACE_FORM_ID` in contact.html and home-valuation.html with the real
   form ID (create at formspree.io → send-to tara's email). `page_source` hidden field already set per form.
3. **GBP review link:** replace `REPLACE-WITH-GBP-SHORTLINK` in reviews.html with her
   "Ask for reviews" short link.
4. **Images:** drop into /images/: `tara-hayes.jpg` (headshot in hat), `og-tara-hayes.jpg`
   (1200×630 branded share image), `favicon.ico`. Schema + OG tags already point at these names.
5. **Email:** currently `tara@h2homegroup.com` sitewide (footer, contact, schema). When the new
   domain email exists, find/replace it.
6. **Geo coordinates:** the site-wide RealEstateAgent schema (index.html) omits `geo` — optionally
   add lat/lng for 10255 Kingston Pike (right-click the pin in Google Maps → copy coordinates).

## IDX
- search.html and every /areas/ page have a marked `IDX EMBED GOES HERE` block.
- Launch stopgap (free): Flexmls IDX 2.0 lite link — Tara: Flexmls → Menu → Preferences →
  IDX Manager → "IDX 2.0 lite".
- Production: Buying Buddy ($49/mo, any-HTML embed, ~2-day feed approval), IDX Broker, or
  iHomefinder — all approved East Tennessee REALTORS® vendors. Forced registration ON,
  lead forwarding → Tara's CRM. Vendor application needs her MLS ID + principal broker sign-off.

## Content TODOs (marked with <!-- TODO --> in files)
- reviews.html: swap placeholder quotes for real, permissioned quotes (First name + neighborhood).
- Each /areas/ page: expand to 500–800 words of original local copy per the build spec.
- Analytics: add the existing GA4 tag (same measurement ID as the Real Geeks phase) to every page
  before launch; re-verify Search Console on the new domain and submit /sitemap.xml.

## Structure
- Interior pages were generated from a shared template — nav/footer/head are identical everywhere.
  To add a page, copy any service page and update: title, description, canonical/OG URLs, breadcrumb,
  h1/sub, body. Then add it to sitemap.xml.
- Compliance footer (Realty Executives Associates, firm line (865) 693-3232, license #333578,
  Equal Housing) is on every page — TN advertising rules; don't remove.

## Cutover order (from the build spec)
Confirm domain + CRM ingest → IDX vendor signup (long pole) → finish content → 301 map from
Real Geeks URLs → DNS cutover → GSC verify + sitemap → update GBP website link → cancel Real Geeks LAST.
