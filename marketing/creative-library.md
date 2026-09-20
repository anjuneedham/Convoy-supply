# ConvoySupply — Creative Library

**Date:** 2026-09-20
**Purpose:** the master register of every creative asset — what exists, what it's for, and whether it can legally and honestly be used. One place to look before making anything new.

---

## Naming convention

```
CS_[TYPE]_[CODE]_[RATIO]_[VERSION].[ext]

TYPE   PHOTO | AI | GRAPHIC | DIAGRAM
CODE   the concept code: P-01, E-02, B-01, AD-03, HERO-01, PROD-02
RATIO  4x5 (feed) | 1x1 (Marketplace/grid) | 16x9 (web) | 9x16 (story)
VER    v1, v2, v3
```

**Example:** `CS_PHOTO_B-01_4x5_v2.jpg`

**Why the TYPE prefix is not cosmetic:** it makes it impossible to accidentally ship an AI image where a real photograph is required. Anything prefixed `AI_` must never appear as product photography. This is a filesystem-level enforcement of the rule in `brand/brand-strategy.md`.

## Folder structure

```
/creative
  /photo        Real photographs. The only source for product imagery.
  /ai           AI-generated. Backgrounds, contexts, problem states ONLY.
  /graphic      Typographic and table graphics
  /diagram      Annotated dimension and layout diagrams
  /exports      Final, sized, compressed, ready to post
  /raw          Camera originals. Never delete.
```

*Kept out of git — image binaries bloat a repository. Store in cloud storage and keep this register as the index.*

---

## The one rule that matters

| Use | Real photo required? |
|---|---|
| Any frame containing our actual product | **YES. Always. No exception.** |
| Before/after | **YES — same cab, same angle, same light, same lens** |
| Backgrounds, textures | No — AI fine |
| Problem-state imagery with no product in frame | No — AI fine |
| Lifestyle context with no product in frame | No — AI fine |
| Infographic and table backgrounds | No — AI fine |
| Anything implying a real person used the product | **Prohibited entirely, AI or not** |

**Every AI image of a cab interior must be checked for plausibility before use.** Generative models produce semi truck interiors with wrong door geometry, impossible mirror placement, and dashboards that do not exist. A driver will spot it in half a second and the credibility cost is permanent. **If in doubt, do not use it.**

---

## The shoot list

One day of access to a real Class 8 sleeper produces nearly all the real photography the brand needs. **This is the single most important production dependency in the entire plan** — everything marked PHOTO below blocks on it.

### Setup
Tripod (mandatory for before/after) · 35mm and 50mm equivalents · natural light only, no flash · overcast or golden hour · shoot RAW · **do not clean the cab before the "before" shots.**

### Required shots

| Code | Shot | Feeds |
|---|---|---|
| PHOTO-01 | **Before/after pair, CS-01, tripod locked** | B-01, AD-01, HERO-01, landing hero |
| PHOTO-02 | CS-01 fitted and loaded, from driver's seat | PROD-01, AD-05, PDP hero |
| PHOTO-03 | Hand reaching into CS-01 | B-02, AD-05 |
| PHOTO-04 | CS-01 stitching and webbing macro | B-05, PDP gallery |
| PHOTO-05 | CS-01 alone, plain background, full view | PDP gallery |
| PHOTO-06 | CS-01 folded flat | PDP gallery |
| PHOTO-07 | CS-02 fitted and loaded on bunk wall | B-03, AD-07, PDP hero |
| PHOTO-08 | CS-02 detail, anchor strap on a real anchor point | PDP gallery |
| PHOTO-09 | CS-03 open, sleeves loaded with real paperwork | B-04, PDP hero |
| PHOTO-10 | Hand pulling a document from CS-03 | B-04 |
| PHOTO-11 | CS-04 open flat, packed | PDP hero, Marketplace |
| PHOTO-12 | CS-04 in a bay | PDP gallery |
| PHOTO-13 | All four laid out on the bunk, overhead | S-01, TRUST-01, PR-01 |
| PHOTO-14 | Cab Reset Kit three products together | PR-01, AD-09 |
| PHOTO-15 | Car organizer vs CS-01 against the same seat | C-01, E-02, AD-03 |
| PHOTO-16 | Organized cab wide, evening light | CTA-01, LP-FINAL |
| PHOTO-17 | **Cluttered passenger seat — genuinely messy** | P-01, LP-PROB-01 |
| PHOTO-18 | Cluttered footwell after a hard stop | P-03 |
| PHOTO-19 | Door pocket stuffed with paperwork | P-05 |
| PHOTO-20 | Tangled dash cables | P-10 |
| PHOTO-21 | Clean empty seat back, for diagram overlay | E-03, AD-04, LP-DEMO |
| PHOTO-22 | Scale reference, hand next to CS-01 | PDP gallery |

**22 shots. One day. Everything else in the library is derived from these.**

PHOTO-17 through PHOTO-20 are the problem shots — capture them **before** anything is tidied or fitted. They cannot be recreated later and they are half the ad library.

---

## Register

`READY` shot and approved · `SHOOT` waiting on the cab day · `AI` generate from a prompt · `DESIGN` build in Canva/Figma · `BLOCKED` waiting on product samples

### Product photography — all blocked on samples + cab access

| Code | Asset | Type | Status |
|---|---|---|---|
| PHOTO-01…22 | Full shoot list above | PHOTO | **BLOCKED** — samples then cab day |

### Static post creatives (`marketing/static-post-system.md`)

| Code | Concept | Source | Status |
|---|---|---|---|
| P-01 | Passenger seat | PHOTO-17 or AI | SHOOT / AI |
| P-02 | Four-minute search | AI | AI |
| P-03 | Hard brake | PHOTO-18 or AI | SHOOT / AI |
| P-04 | Storing on your bed | AI + annotation | AI + DESIGN |
| P-05 | Paperwork | PHOTO-19 or AI | SHOOT / AI |
| P-06 | 60 square feet | AI | AI |
| P-07 | $180,000 problem | AI split | AI |
| P-08 | Thursday pile | AI pair | AI |
| P-09 | Somebody gets in | AI | AI |
| P-10 | Cables | PHOTO-20 or AI | SHOOT / AI |
| E-01 | Four zones carousel | AI + annotation | AI + DESIGN |
| E-02 | Stop buying car organizers | **PHOTO-15** | **BLOCKED** |
| E-03 | Measuring guide | PHOTO-21 + diagram | SHOOT + DESIGN |
| E-04 | Company truck rules | AI | AI |
| E-05 | 20-minute reset | AI | AI |
| B-01 | **Before/after — flagship** | **PHOTO-01** | **BLOCKED** |
| B-02 | Everything in reach | **PHOTO-03** | **BLOCKED** |
| B-03 | That wall was doing nothing | **PHOTO-07** | **BLOCKED** |
| B-04 | Three seconds | **PHOTO-10** | **BLOCKED** |
| B-05 | Spec shot | **PHOTO-04** | **BLOCKED** |
| C-01 | Car vs truck organizer | **PHOTO-15** | **BLOCKED** |
| C-02 | Three ways to store | AI ×2 + PHOTO-02 | AI + BLOCKED |
| C-03 | Price honesty | GRAPHIC | DESIGN |
| L-01 | 4am | AI | AI |
| L-02 | Home for 19 days | AI | AI |
| L-03 | Show us your setup | AI + grid frame | AI + DESIGN |
| S-01 | First customers | **PHOTO-13** | **BLOCKED** |
| S-02 | Founder note | **PHOTO-02** | **BLOCKED** |
| PR-01 | The kit | **PHOTO-14** | **BLOCKED** |
| PR-02 | Free shipping | GRAPHIC | DESIGN |

### Ad creatives (`marketing/meta-ads.md`)

| Code | Angle | Source | Wave | Status |
|---|---|---|---|---|
| AD-01 | Before/after | PHOTO-01 | 1 | **BLOCKED** |
| AD-02 | Problem/solution | AI | 1 | AI |
| AD-03 | Comparison | PHOTO-15 | 1 | **BLOCKED** |
| AD-04 | Educational | PHOTO-21 + diagram | 1 | SHOOT + DESIGN |
| AD-05 | Product benefit | PHOTO-03 | 1 | **BLOCKED** |
| AD-06 | Time saving | AI + graphic | 2 | AI + DESIGN |
| AD-07 | Curiosity | AI | 2 | AI |
| AD-08 | Lifestyle | AI | 2 | AI |
| AD-09 | Bundle | PHOTO-14 | 2 | **BLOCKED** |
| AD-10 | Objection-first | GRAPHIC | 2 | DESIGN |

**Four of the five Wave 1 ads are blocked on product samples.** That dependency drives the whole schedule in `execution/30-day-plan.md` — samples are ordered on Day 5 and everything creative stacks behind their arrival.

### Store imagery

| Code | Use | Source | Status |
|---|---|---|---|
| HERO-01 | Homepage hero | PHOTO-01 or PHOTO-02 | **BLOCKED** |
| PROD-01 | Featured product | PHOTO-02 | **BLOCKED** |
| BEN-01…04 | Homepage benefits | PHOTO-02/03/04 + AI | Mixed |
| TRUST-01 | Homepage proof | PHOTO-13 | **BLOCKED** |
| CTA-01 | Homepage final CTA | PHOTO-16 | **BLOCKED** |
| LP-HERO | Landing hero | PHOTO-01 | **BLOCKED** |
| LP-PROB-01 | Landing problem | PHOTO-17 | SHOOT |
| LP-DEMO-01 | Annotated diagram | PHOTO-05 + design | **BLOCKED** + DESIGN |
| LP-FINAL | Landing final | PHOTO-16 | **BLOCKED** |

---

## Export specs

| Use | Ratio | Pixels | Max size | Format |
|---|---|---|---|---|
| Facebook / Instagram feed | 4:5 | 1080×1350 | 300 KB | JPG |
| Marketplace | 1:1 | 1200×1200 | 300 KB | JPG |
| Carousel | 1:1 | 1080×1080 | 300 KB | JPG |
| Website hero | 16:9 | 1920×1080 | 200 KB | **WebP** |
| PDP gallery | 1:1 | 1600×1600 | 200 KB | **WebP** |
| Meta ad | 4:5 | 1080×1350 | 300 KB | JPG |

**Meta ad text rule:** Meta no longer hard-rejects text-heavy images, but delivery still suffers. **Keep on-image text under ~20% of area.** The hook, not a paragraph.

---

## Graphic template

One master template does all 30 static posts. Build it once.

**Layout:** image fills frame · asphalt gradient scrim from the bottom for text legibility · hook in Barlow Condensed 700 uppercase, bottom-left, generous margin · one word or phrase in hi-viz amber, never more · wordmark bottom-right, 60% opacity · **no borders, no drop shadows, no swooshes.**

**Every export passes the 200px test:** shrink to thumbnail width. If the hook is unreadable, it fails. Most competitor creative fails this, which is exactly why it matters.

---

## Compliance check — before any asset is published

- [ ] If our product is in frame, it is a **real photograph**
- [ ] No AI product render presented as product photography
- [ ] No fabricated review, testimonial, rating, or customer quote
- [ ] No countdown, fake stock counter, or expiring offer that doesn't expire
- [ ] No safety, medical, compliance, or legal claim
- [ ] No competitor brand mark or name visible
- [ ] Before/after is the same cab, same angle, same light, same lens
- [ ] Every on-image spec figure traces to a supplier spec sheet
- [ ] No customer photo used without explicit permission
- [ ] Any AI cab interior checked for plausibility by someone who knows trucks
- [ ] Passes the 200px test

## Version discipline

Never overwrite. `v1 → v2 → v3`. Keep every version and log which version ran in which ad, because a creative "fatiguing" and a creative "being replaced by a worse version" look identical in the data if you cannot tell them apart.

Record what ran where in `execution/experiments.md`.
