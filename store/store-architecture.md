# ConvoySupply — Shopify Store Architecture

**Date:** 2026-09-20
**Platform:** Shopify, Basic plan — **$39/mo month-to-month ($29/mo billed annually)**, Shopify Payments **2.9% + 30¢** online **[V7]**
**Base theme:** Dawn (free, Online Store 2.0, fast, sections-everywhere)
**Custom code:** in `/theme` in this repository

---

## Why Dawn and not a paid theme

A $180–$400 premium theme buys sections we do not need and page-weight we cannot afford. Dawn is free, fast, and fully section-based, and the differentiation in this brand comes from **photography and copy**, not from theme features. The money saved goes into ad spend, which is the actual constraint.

Six custom sections (in `/theme/sections`) cover everything Dawn does not do.

---

## Site map

```
/                                Homepage
/pages/cs-01                     ► HERO LANDING PAGE (custom funnel template)
/products/cs-01-cab-command-organizer
/products/cs-02-bunk-shelf-net
/products/cs-03-manifest-folio
/products/cs-04-haul-bag
/products/cab-reset-kit          Bundle
/products/full-rig-kit           Bundle
/collections/all
/collections/front-of-cab
/collections/sleeper-and-bunk
/collections/kits
/pages/what-fits-my-truck        Fit guide — high commercial value
/pages/about
/pages/shipping                  Includes the driver-delivery guidance
/pages/returns
/pages/contact
/pages/faq
/policies/*                      Shopify-generated legal pages
```

**Deliberately absent at launch:** blog, reviews page, rewards program, account area beyond checkout, wishlist, live chat. Each is a maintenance burden with no launch-phase return. The blog gets added in the SEO phase, after the paid test resolves.

### `/pages/what-fits-my-truck` deserves its own note

Fit is the **strongest objection** in the avatar research. A dedicated page that answers it does three jobs: it removes the objection pre-purchase, it is linkable from every PDP and from Marketplace replies, and it is the one page with genuine long-term organic search value (*"cascadia cab organizer fit"*). It is cheap to build and should not be cut.

---

## Navigation

### Header (primary)

| Label | Target | Why |
|---|---|---|
| **Shop** | Dropdown → Front of Cab / Sleeper & Bunk / Kits / All | Zone-based, teaches the mental model |
| **Kits** | `/collections/kits` | **Surfaced separately on purpose** — bundles are the AOV lever and must not be buried one level down |
| **What Fits My Truck** | `/pages/what-fits-my-truck` | Kills the top objection from the nav bar |
| **About** | `/pages/about` | Trust for an unknown brand |

Cart icon right. No search at launch — four products.

### Announcement bar

> **Free US shipping over $75 · 30-day returns · Shipping to a terminal? We can do that.**

Rotating is available in Dawn; **do not rotate at launch.** One message, always visible. The $75 threshold sits just below the $89 Cab Reset Kit, which is the entire point of choosing $75.

The third clause is unusual for an announcement bar and it earns its place — it is niche-specific, no competitor says it, and it answers a real objection in seven words.

### Footer

Four columns: **Shop** (4 products + 2 kits) · **Help** (Fit guide, Shipping, Returns, FAQ, Contact) · **Company** (About, Policies) · **Contact** (real email, response-time commitment, no fake phone number)

Bottom bar: wordmark, "Squared away.", payment icons, copyright.

**No newsletter popup at launch.** We have nothing to email. An email capture in the footer only, with an honest promise: *"New products and restocks. Nothing else. Maybe one email a month."*

---

## Homepage section order

Copy in `store/homepage-copy.md`. Section files in `/theme/sections`.

| # | Section | Purpose | Implementation |
|---|---|---|---|
| 1 | Announcement bar | Shipping + returns + terminal note | Dawn native |
| 2 | Header / nav | Navigation, cart | Dawn native |
| 3 | **Hero** | Problem in 5 words + hero image + CTA | `cs-hero.liquid` |
| 4 | **The problem** | Name the pain concretely | `cs-problem.liquid` |
| 5 | **Featured product (CS-01)** | Push straight to the hero product | Dawn `featured-product` |
| 6 | **Benefits** | Four benefit blocks, image + headline + line | `cs-benefits.liquid` |
| 7 | **Collection grid** | All four products | Dawn `featured-collection` |
| 8 | **Why ConvoySupply** | Differentiation vs. generic + specialty | `cs-why.liquid` |
| 9 | **Social proof placeholder** | Honest "no reviews yet" — structured for real ones later | `cs-proof.liquid` |
| 10 | **How it works** | Order → ship → fit → return. Kills logistics anxiety | `cs-how.liquid` |
| 11 | **Kits** | Bundle upsell | Dawn `featured-collection` (kits) |
| 12 | **FAQ** | Top 6 objections | `cs-faq.liquid` |
| 13 | **Guarantee / returns** | Plain-language returns | Dawn `rich-text` |
| 14 | **Final CTA** | Last conversion opportunity | `cs-cta.liquid` |
| 15 | Footer | Nav, contact, email | Dawn native |

### Why this order

**Problem before product (3→4→5).** An unknown brand has to establish that it understands the situation before it has permission to sell. Leading with a product grid, which most Shopify stores do, wastes the only moment we have the visitor's full attention.

**Social proof at 9, not at 3.** Conventionally proof goes high. We have none, so putting it high would just advertise the absence. At position 9 the visitor has already seen the problem framed correctly, the specs, and the differentiation — the honesty then reads as confidence rather than as a gap.

**"How it works" at 10, immediately after.** It follows the trust section because the questions it answers — when does it arrive, what if it doesn't fit — are exactly the ones a visitor has right after deciding the brand seems credible but unproven.

---

## Templates

| Template | File | Used by |
|---|---|---|
| Homepage | `templates/index.json` | `/` |
| **Hero funnel landing** | `templates/page.landing-cs01.json` | `/pages/cs-01` |
| Standard product | `templates/product.json` | CS-02, CS-03, CS-04 |
| Bundle product | `templates/product.bundle.json` | Both kits |
| Collection | `templates/collection.json` | All collections |
| Page | `templates/page.json` | About, FAQ, etc. |

**CS-01 has both a PDP and a landing page.** The PDP (`/products/cs-01-...`) serves organic, collection, and cart traffic. The landing page (`/pages/cs-01`) is the **paid traffic destination** — no nav distractions, funnel-structured, single conversion path. They are different jobs and a single page cannot do both well. Which one paid traffic performs better on is itself a test (EXP-007).

---

## Conversion mechanics

### Checkout
- Shopify Payments (2.9% + 30¢ **[V7]**), Shop Pay, PayPal, Apple/Google Pay
- **Express checkout buttons on PDP** — Shop Pay and Apple Pay above the fold materially reduce friction for mobile
- Guest checkout on, account creation optional
- No upsell app at launch — bundles are real products and need no app. Revisit post-launch.

### Cart
Drawer, not a page. Contains:
- Free-shipping progress bar to $75 *(honest — the threshold is real)*
- **One bundle nudge:** if cart contains CS-01 alone → *"Add CS-02 and CS-03 for $34.01 more and get the Cab Reset Kit (save $23.97)."* Real math, real saving.
- CS-03 as a single post-add upsell at $24.99 *(a real $3 discount, not a fake one)*

### Trust elements — placement

| Element | Where |
|---|---|
| Free shipping over $75 | Announcement bar, cart, PDP |
| 30-day returns | Announcement bar, PDP, footer, FAQ |
| Secure checkout | Cart, checkout |
| Real email + response time | Footer, contact, PDP FAQ |
| Published specs | Every PDP |
| Honest "no reviews yet" | Homepage §9, every PDP |
| Fit guide link | Every PDP, nav |

### Explicitly NOT implemented

Not oversights — decisions, recorded in `execution/decisions.md` as DEC-003:

- Countdown timers · fake stock counters · "X people viewing" · exit-intent discount popups · fake review apps · spin-to-win · "someone in Ohio just bought" notifications

Every one of these is available as a Shopify app and every one would be detected and mocked by this audience. The brand's only real asset at launch is being visibly honest in a category that is visibly not.

---

## Performance

Mobile is the only surface that matters — Facebook traffic is overwhelmingly mobile, and this audience browses on a phone in a parking lot, frequently on poor signal.

| Target | Value |
|---|---|
| LCP | < 2.5s on 4G |
| Homepage weight | < 1.2 MB |
| Hero image | < 200 KB, WebP, `loading="eager"` + `fetchpriority="high"` |
| All other images | WebP, `loading="lazy"`, explicit width/height |
| Fonts | 3 families, `font-display: swap`, preconnect to Google Fonts |
| Apps | **Zero at launch** — every app adds render-blocking script |

**The zero-apps rule is the most consequential performance decision here.** A typical Shopify store loses more speed to apps than to images.

---

## Tracking

| Tool | Purpose | Note |
|---|---|---|
| **Meta Pixel** | PageView, ViewContent, AddToCart, InitiateCheckout, Purchase | Via Shopify's native Facebook & Instagram channel |
| **Meta Conversions API** | Server-side, recovers signal lost to iOS/ad-block | **Not optional.** Browser-only pixel loses a meaningful share of events and the whole test depends on attribution. |
| **GA4** | Behaviour, funnel dropoff | Free |
| **Shopify Analytics** | Native sales data | Free |
| UTM discipline | Every link tagged | Enforced in `marketing/meta-ads.md` |

**Pre-launch verification:** fire a test purchase and confirm the Purchase event appears in Meta Events Manager with correct value and currency, and that Event Match Quality is acceptable. Ship nothing until this passes — an ad test with broken attribution is a waste of the whole budget.

---

## Build sequence

Days 9–17 of `execution/30-day-plan.md`.

1. Install Dawn, set colors and fonts from `brand/brand-strategy.md`
2. Legal pages (Shopify generators, then edited into plain English)
3. Products + variants + collections
4. Upload custom sections from `/theme/sections`
5. Build homepage from `templates/index.json`
6. Build PDPs
7. Build the CS-01 landing page
8. Build the fit guide
9. Shipping profiles + rates
10. Payments + test order
11. Pixel + CAPI + GA4, verify events
12. Mobile QA on a real phone on a real cellular connection
13. Speed test, fix regressions

**Reference tag [V7]:** Shopify Basic pricing and Shopify Payments rates, 2026 — shopify.com pricing, Shopify Help Center, corroborated by third-party pricing analyses.
