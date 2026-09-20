# ConvoySupply — 30-Day Launch Plan

**Start date:** `[SET ON DAY 1]`
**Effort:** ~3–4 hours/day, with two heavier days (the cab shoot, and launch day)
**Budget:** see `finance/testing-budget.md`

---

## How this differs from the brief's suggested schedule, and why

The brief proposed: research → products → brand → store → pages → creatives → Marketplace → organic → ads → launch, roughly sequential.

**Three changes, all driven by real dependencies rather than preference:**

### 1. Samples are ordered on Day 1, not Day 5

**This is the most important change.** Four of the five launch ad creatives and nine of the thirty static posts are **blocked on having physical product to photograph** (`marketing/creative-library.md`). Samples ship in 7–14 days **[A]**. Ordering them on Day 5 puts the photo shoot around Day 19 and leaves no slack before the ads need creative.

Ordering on Day 1 puts samples in hand by roughly Day 10 and the shoot on Day 12. **Everything else can happen in parallel; this cannot.**

### 2. Trademark clearance is a Day 1 gate

Convoy Supply Ltd. is a real building-materials distributor **[V2]**. Every hour spent on logo, domain, or packaging before clearance is an hour at risk. **This gate runs first and blocks brand spend, not brand thinking.**

### 3. The store is built with placeholders from Day 6

The store build does not need final photography to progress — structure, copy, products, policies, shipping, and tracking can all be built against placeholder images and swapped on Day 13. Waiting for photography to start the store would waste a week.

**Net effect: research and product selection compress, the store build starts earlier, and Days 1–5 run several tracks at once.** The schedule below reflects that.

---

## Phase 0 — Gates (Day 1)

### Day 1 — Unblock everything

| # | Task | Why it is on Day 1 |
|---|---|---|
| 1 | **USPTO TESS search** — classes 12, 18, 35. State business name search. Domain and handle availability. | **GATE.** Blocks all brand spend. DEC-001. |
| 2 | **Meta Ad Library search** for competitors running trucker-accessory ads | Tests the "Tier 4 is vacant" claim in `competitor-analysis.md`. **If a funded DTC competitor is already running this playbook, the plan needs revisiting today, not on Day 20.** |
| 3 | **Contact 5+ suppliers** for CS-01 and CS-02. Request quotes, spec sheets, MOQs, lead times, and samples. | **GATE.** Longest lead time in the plan. |
| 4 | **Arrange cab access** for a shoot day around Day 12 | **GATE.** The single hardest logistical dependency. Start asking now. |
| 5 | Register business email, open the Shopify trial | Cheap, unblocks Day 6 |

**Do not proceed to Day 2 without item 1 resolved and items 3 and 4 in motion.**

---

## Phase 1 — Research and validation (Days 2–4)

Most of this repository's research is already written. These days are for **checking it against reality**, not redoing it.

### Day 2 — Competitive reality check
- Pull 20 real Amazon listings for semi truck cab organizers into a spreadsheet: price, review count, rating, seller, key complaints
- Read the **1- and 2-star reviews specifically.** They are the highest-value research available and they are free — every complaint is an angle, an FAQ answer, or a product requirement.
- Update `research/competitor-analysis.md` with real data, replacing the **[A]** price estimates

### Day 3 — Audience reality check
- Join 5 trucking Facebook Groups. **Read only. Post nothing.**
- Search them for "organizer," "storage," "cab setup." Log real language, real complaints, real product mentions.
- Update `research/customer-avatar.md` — promote hypotheses to verified where the evidence supports it, and **delete any that the groups contradict**

### Day 4 — Supplier follow-up and offer check
- Chase quotes. Compare on landed cost, MOQ, lead time, spec sheet quality, and communication responsiveness
- **Communication quality is a real selection criterion**, not a soft one — a supplier who takes four days to answer a spec question will take four days when there is a defect
- Confirm the fit dimensions for the five named truck models
- Update `research/product-selection.md`

---

## Phase 2 — Product and economics lock (Day 5)

### Day 5 — The go/no-go on margin
- **Order samples.** CS-01 and CS-02 at minimum. Pay for expedited shipping — it is the cheapest time you can buy in this plan.
- Enter real landed costs into `finance/unit_economics.py` and **re-run it**
- **Check the hero against the $22 landed red line.** Above it, contribution margin falls under 45% and the offer must be re-priced or the SKU dropped before anything else is built.
- Commit the updated script output to `finance/unit-economics.md`
- Log the decision in `execution/decisions.md`

**If the margin structure does not hold, stop here.** Everything downstream assumes it does. This is the cheapest possible place to find out.

---

## Phase 3 — Brand (Days 6–8, running alongside the store build)

### Day 6 — Identity
- Assuming Day 1 clearance passed: buy the domain, register handles
- Logo: wordmark in Barlow Condensed. **Do not commission a mark.** A clean wordmark is correct for this brand and costs nothing.
- Set the color tokens from `brand/brand-strategy.md`

### Day 7 — Voice and copy
- Fill every `[TBC]` in `brand/brand-copy.md` that is now knowable — founder first name, support email
- Draft the About page and the founder note
- **Read every headline aloud.** Apply the voice check. Cut anything that could sell a phone case.

### Day 8 — Assets
- Build the master static-post template (Canva or Figma)
- Generate the AI images that need no product: P-02, P-04, P-06, P-07, P-08, P-09, E-01, E-04, E-05, L-01, L-02, AD-02, AD-07, AD-08
- **Check every AI cab interior for plausibility.** Wrong door geometry or impossible mirrors will be spotted instantly and the credibility cost is permanent.

---

## Phase 4 — Store build (Days 6–14, parallel track)

Placeholder images throughout. Real photography swaps in on Day 13.

| Day | Task |
|---|---|
| **6** | Install Dawn, duplicate, apply tokens and fonts, render `cs-tokens` |
| **7** | Upload the nine custom sections from `/theme/sections`. Verify each renders in the editor. |
| **8** | Create products, variants, collections. Both bundles as real products with genuine compare-at prices. |
| **9** | Build the homepage from `templates/index.json`. Paste copy from `store/homepage-copy.md`. |
| **10** | Build all four PDPs from `store/product-pages.md`. All 18 required blocks on each. |
| **11** | Build the CS-01 landing page. Suppress nav. Test the sticky CTA on a real phone. |
| **12** | Build the fit guide, About, FAQ, Shipping, Returns, Contact. Generate and **plain-English-edit** the legal policies. |
| **13** | **Swap in real photography.** Compress everything to WebP. Alt text on every image. |
| **14** | Shipping profiles and rates. Payments. **Complete a real test purchase on a phone.** Pixel + CAPI + GA4. **Verify the Purchase event in Events Manager.** |

**Day 14's test purchase is a hard gate.** No ad spend until a real purchase has fired a correctly-valued Purchase event.

---

## Phase 5 — The shoot (Day 12)

**The single most important production day in the plan.** Samples should have arrived around Day 10. If they have not, the shoot moves and everything downstream moves with it.

- Full 22-shot list in `marketing/creative-library.md`
- **Shoot the problem states first (PHOTO-17 to PHOTO-20), before anything is tidied or fitted.** They cannot be recreated once the cab is organized, and they are half the ad library.
- **Tripod for the before/after. Do not move the camera between frames.** The before/after is the flagship creative and it is worthless if the two frames don't match.
- Natural light only. Shoot RAW. Overshoot — a second day of cab access may not be available.

---

## Phase 6 — Creative production (Days 15–18)

| Day | Task |
|---|---|
| **15** | Cull and edit the shoot. Export masters. |
| **16** | Build all 30 static posts in the template. **Run the 200px test on every one.** |
| **17** | Build the 5 Wave 1 ad creatives. Then the 5 Wave 2 creatives so they are ready before they are needed. |
| **18** | Schedule the first two weeks of organic from `marketing/organic-content-calendar.md`. Run the compliance checklist over every asset. |

---

## Phase 7 — Channels (Days 19–24)

### Days 19–20 — Marketplace
- Photograph for Marketplace specifically — 1:1, in-cab hero first
- Write all five listings from `marketing/marketplace-strategy.md`
- **Read Facebook's Commerce Policies before posting the first listing**
- Post all five. Set up saved replies from the response scripts.
- **Only list what is physically in hand.**

### Days 21–22 — Organic launch
- Facebook Page live: cover image, About, contact, hours, real response-time commitment
- Instagram live, cross-posting enabled
- **Start posting.** Week 1 of the calendar — problem and education, zero product links.
- Begin Group participation. **No promotional posts. None.**

### Days 23–24 — Ads preparation
- Business Manager, ad account, domain verification
- Aggregated Event Measurement, Purchase prioritized
- Build Campaign 1: three ad sets, five creatives each, identical
- **UTM-tag every link.** A link without UTMs is data lost permanently.
- Run the full pre-launch gate checklist from `finance/testing-budget.md`
- **Do not launch if any item fails.**

---

## Phase 8 — Launch and optimize (Days 25–30)

### Day 25 — Launch
- Campaign 1 live at $30/day CBO
- **Then do nothing for 72 hours.** Editing resets the learning phase and wastes the spend already made. This is the most commonly broken rule in small-budget testing and the hardest to follow.
- Keep posting organically. Keep answering Marketplace.

### Day 26 — Observe
- Check that delivery has started and spend is pacing
- **Do not touch the campaign.**
- Log baseline metrics

### Day 27 — Observe
- Same. Answer messages. Post. **Do not touch the campaign.**

### Day 28 — First read (72 hours in)
- Kill any creative with **<0.5% CTR and zero add-to-carts**
- Change nothing else
- Log the read in `execution/daily-log.md`

### Day 29 — Flex
- Post the flex organic slot
- Renew Marketplace listings
- Full funnel review: where is the biggest drop-off?

### Day 30 — Review, not launch
- **No posting. No ad changes.**
- Pull 30 days of data into `execution/metrics.md`
- Write the retro in `execution/daily-log.md`
- Update `execution/decisions.md` and `execution/experiments.md`
- Work the Day 14 decision tree from `finance/testing-budget.md` — note that the **ad test's** Day 14 falls on **calendar Day 38**, because ads launch on Day 25

---

## A scheduling reality worth stating plainly

**The 14-day ad test does not finish inside the 30-day plan.** Ads launch on Day 25, so the Day 14 ad decision point lands on calendar Day 38.

This is not a planning error — it is what the dependencies produce. Product samples take 7–14 days, photography depends on samples, creative depends on photography, and ads depend on creative. Compressing any of those would mean launching ads with weak creative, which would waste the budget and answer nothing.

**Day 30 is a checkpoint, not a verdict.** The real go/no-go on paid is Day 38. Plan cash accordingly.

Two things *can* produce results inside 30 days, and both are free:
- **Marketplace** — listings live from Day 19, so 11 days of data by Day 30
- **Organic** — posting from Day 21, so 9 days of data

If either produces sales before the ads have run, that is a genuine and useful finding.

---

## Critical path

```
Day 1  Order samples ─────────────────┐
Day 1  Arrange cab access ────────────┤
Day 1  Trademark clearance ───────────┤
                                      ▼
Day 10 Samples arrive [A] ──────► Day 12 SHOOT ──────► Days 15-18 Creative
                                                              │
Days 6-14 Store build (parallel) ─────────────────────────────┤
                                                              ▼
                                            Days 23-24 Ads prep ──► Day 25 LAUNCH
                                                                          │
                                                                    Day 38 DECISION
```

**The three Day 1 gates are the whole schedule.** Everything else has slack; these do not.

## Slippage plan

| If | Then |
|---|---|
| Samples late | Shoot slips, everything slips. **Order on Day 1 and pay for fast shipping.** |
| No cab access | Fall back to a day cab or a friend's truck. **Do not fake it with AI** — a driver will spot it and the credibility loss is worse than a delayed launch. |
| Trademark unclear | Pause brand spend. Keep building the store under a working name. Get an attorney hour. |
| Landed cost above $22 | Stop at Day 5. Re-price or re-select. Do not build on a broken margin. |
| Supplier quality poor on samples | Re-source. A bad product makes every other part of this plan worthless. |
| Meta ad account restricted | Appeal. Run Marketplace and organic while waiting. Do not create a second account — that makes it worse. |

## Daily routine throughout

**Morning (30 min):** post the scheduled item · clear Marketplace messages · check ads (after launch) · log yesterday.
**Evening (45 min):** reply to all comments and messages · 10 min of Group participation, no links · the day's build task · update `execution/daily-log.md`.

**The log is not optional.** Thirty days of unrecorded decisions is thirty days of learning thrown away, and by Day 38 nobody remembers why anything was changed.
