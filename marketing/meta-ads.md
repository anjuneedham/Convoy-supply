# ConvoySupply — Meta Ads Strategy

**Date:** 2026-09-20
**Budget posture:** small, deliberately. **Assume nothing is profitable until measured.**
**Placements:** Facebook Feed primary, Instagram Feed secondary, Advantage+ placements on for delivery efficiency

---

## Benchmarks we are testing against

Industry figures, **not our numbers**. They exist to make our results legible, not to predict them.

| Metric | 2026 benchmark | Source note |
|---|---|---|
| CPM, all industries | **$14.19** (+20.1% YoY from $11.82) | **[V8]** |
| CPM, ecommerce | **~$10.42** | **[V8]** |
| CPM, DTC median | **$13.52** (IQR $11.04–$22.90) | **[V8]** |
| **CPM, automotive** | **~$10.01 — lowest tracked vertical** | **[V8]** |
| CPC, all industries | **$0.78** | **[V8]** |
| CPC, ecommerce | **~$0.67** (median $0.57, IQR $0.33–$1.01) | **[V8]** |
| Ecommerce purchase CVR | **1–3%** | **[V8]** |
| Purchase ROAS, DTC median | **2.96** (IQR 2.50–5.30) | **[V8]** |

**The automotive CPM figure is the most useful number here.** At ~$10.01 it is the lowest tracked vertical, and our audience sits in that space. That is a real tailwind on the cost side — and it is also why any failure will be a *conversion* failure rather than a *reach* failure, which is worth knowing before we start reading the data.

**CPM rose ~20% year over year.** Anyone planning against 2025 numbers is planning against the wrong ones.

---

## Campaign structure

Two campaigns. The second does not launch until it is earned.

```
CAMPAIGN 1 — COLD ACQUISITION                    launches Day 1
  Objective: Sales (Purchase)  ·  Budget: CBO $30/day
  ├── Ad Set A — BROAD          US, 30–65, all genders, no interests
  ├── Ad Set B — INTEREST STACK trucking occupation + brand + retail interests
  └── Ad Set C — ADVANTAGE+     Meta's automated audience
      Each ad set carries the SAME 5 creatives → the creative is held constant so
      the audience is the variable being measured.

CAMPAIGN 2 — RETARGETING                         GATED (see below)
  Objective: Sales (Purchase)  ·  Budget: $10/day
  ├── Ad Set D — ATC + IC, 14d, excluding purchasers
  └── Ad Set E — Viewers 25%+ / LPV, 30d, excluding ATC and purchasers
```

### Retargeting gate — do not open early

Campaign 2 stays off until **all three** are true:

1. **1,000+ landing page views** in the last 14 days
2. **50+ add-to-carts** in the last 14 days
3. Campaign 1 has run at least **10 days**

Spending on retargeting before there is an audience to retarget is the most common way a small test wastes its budget. You pay premium CPMs to reach a few dozen people repeatedly, learn nothing, and burn the days you needed for the cold test. **Recorded as DEC-005 in `execution/decisions.md`.**

### Why three cold ad sets and not one

The central open question from `research/customer-avatar.md` is **whether broad beats interest targeting for this niche.** The hypothesis on record — written down before the test so it cannot be claimed retroactively — is:

> **[H] Broad will outperform interest stacks, because strong creative self-selects this audience more precisely than Meta's occupational interest taxonomy does.**

Three ad sets with identical creative is the cleanest way to answer that. If broad wins, we consolidate and the account gets simpler and cheaper. If interests win, we have found something genuinely useful about a niche audience.

### Why CBO and not per-ad-set budgets

At $30/day, per-ad-set budgets give each ad set ~$10/day, which will not exit the learning phase within the test window. Campaign Budget Optimization lets Meta concentrate spend where it works. We lose some cleanliness in the audience comparison and gain the ability to get any statistically meaningful result at all. **That is the right trade at this budget, and the imprecision should be acknowledged when reading the audience results.**

---

## Targeting research

### Ad Set A — Broad
- US · 30–65 · all genders · no interests · Advantage+ placements
- **Why:** Meta's delivery has been consistently better at finding buyers from creative signal than from interest layering, and our creative is unusually self-selecting — a photo of a sleeper cab interior is invisible to anyone who is not a driver. Broad also gives the pixel the widest signal to learn from.
- **Risk:** at a small budget, broad may spread too thin to converge.

### Ad Set B — Interest stack

**Verify every one of these in Ads Manager before building. Meta's interest taxonomy changes without notice and occupational interests are especially unreliable.**

| Group | Interests |
|---|---|
| Occupational | Truck driver · Commercial driver's license · Trucking industry · Owner-operator · Semi-trailer truck |
| Truck brands | Freightliner · Peterbilt · Kenworth · Volvo Trucks · Mack Trucks · International Trucks |
| Trade media / retail | Overdrive Magazine · Trucker Path · TA Travel Centers · Pilot Flying J · Love's Travel Stops · Iowa 80 |
| Adjacent | Diesel engines · Long-haul trucking · Logistics |

- US · 30–65 · **no narrowing, no exclusions**
- **Why:** if occupational interests work at all, this is the version that works. Truck-brand and truck-stop interests are the strongest signals in the set because they are behavioral rather than self-declared.
- **Risk:** interest audiences for occupations are frequently polluted by enthusiasts rather than practitioners, and we may pay to reach people who like trucks rather than people who drive them. **This is the specific failure mode to watch for** — high CTR with low conversion is its signature.

### Ad Set C — Advantage+ Audience
- Advantage+ with the interest stack as a suggestion, letting Meta expand
- **Why:** it is the middle path, and it is increasingly where Meta's delivery performs best. Cheap to include as a third arm.

### Demographics

| Setting | Value | Reasoning |
|---|---|---|
| Age | **30–65** | Average driver 47, owner-operators 56 **[V3]**. Range is deliberately wider than the average to avoid pre-filtering. |
| Gender | **All** | We have not verified the gender split and will not exclude on an assumption. Women drive trucks. |
| Location | **US only** | Shipping and returns are domestic |
| Language | English | |

**Do not narrow the age range in week one.** If purchase data shows a clear concentration, narrow in week three — but let the data say it.

### Behaviors
Meta's behavior targeting for occupations is thin and unreliable. **Not used in the initial test.** If interest targeting shows promise, revisit.

### Lookalikes — later, not now
A 1% purchaser lookalike needs **100+ purchases** to be meaningful. We will not have that in 30 days. **Do not build one on 20 purchases** — it will be noise and it will burn budget looking authoritative. Revisit at 100+ purchasers.

### Retargeting audiences (Campaign 2, once gated)

| Audience | Window | Exclusions | Message |
|---|---|---|---|
| Add to cart | 14d | Purchasers | Objection handling — fit, shipping, returns |
| Initiate checkout | 14d | Purchasers | Friction removal — shipping cost, payment options |
| Landing page views | 30d | ATC, purchasers | Re-state the offer + the bundle |
| Video/page 25%+ | 30d | ATC, purchasers | Social proof + differentiation |
| **Purchasers** | 180d | — | **Excluded from all prospecting.** Later: cross-sell the other SKUs. |

Excluding purchasers from prospecting is basic and routinely forgotten. At our volumes it matters more, not less.

---

## AD CREATIVE — 10 CONCEPTS

Five launch on Day 1 (marked **LAUNCH**). Five are the second wave, introduced as launch creatives fatigue.

Every concept maps to a **distinct angle** and a **distinct buying motivation** from `research/selected-niche.md`. We do not assume one angle works — we assume we do not know which one does.

| # | Angle | Motivation tested | Wave |
|---|---|---|---|
| AD-01 | Before/after | Control over the space | **LAUNCH** |
| AD-02 | Problem/solution | Stop losing things | **LAUNCH** |
| AD-03 | Comparison | Fit / anti-generic | **LAUNCH** |
| AD-04 | Educational | Competence | **LAUNCH** |
| AD-05 | Product benefit | Convenience | **LAUNCH** |
| AD-06 | Time saving | Stop losing things | Wave 2 |
| AD-07 | Curiosity | — | Wave 2 |
| AD-08 | Lifestyle / identity | Pride in the rig | Wave 2 |
| AD-09 | Cost saving / bundle | Value | Wave 2 |
| AD-10 | Objection-first | Trust | Wave 2 |

---

### AD-01 — Before/After **[LAUNCH]**

**Primary text:**
> Your passenger seat is where everything ends up. Phone, water, gloves, a clipboard, whatever you ate at 2am.
>
> The CS-01 straps to the seat back and gives all of it one place. Two minutes to fit. No drilling, no tools, nothing on your truck gets modified.
>
> Sized for a Class 8 sleeper — every dimension published so you can check before you buy.

**Headline:** Same seat. Two minutes apart.
**Description:** $54.99 · Free shipping over $75 · 30-day returns
**CTA button:** Shop Now
**Visual:** Split frame, real photograph. Identical angle, light, and lens. Left cluttered, right CS-01 fitted.
**Prompt:** **REAL PHOTOGRAPH REQUIRED.** Tripod, one session, camera does not move. The "before" must be genuinely messy.
**Pain point:** The passenger seat pile · **Angle:** Before/after · **Destination:** `/pages/cs-01`

*The highest-expectation creative in the set. If this one fails, the problem is the audience or the offer — not the creative.*

---

### AD-02 — Problem/Solution **[LAUNCH]**

**Primary text:**
> Four minutes looking for the same flashlight you had yesterday. Dock appointment in twenty.
>
> It isn't that you're disorganized. The truck gave you a bunk, a dash and two shallow cubbies, and everything else has to go somewhere.
>
> The CS-01 gives every daily-use item a defined place, within reach from the driver's seat.

**Headline:** You know it's in here somewhere.
**Description:** Built for Class 8 sleepers · No installation · $54.99
**CTA:** Learn More
**Visual:** Hand searching a cluttered bunk, slight motion blur, dim interior light.
**Prompt:** *Close-up photorealistic shot of a hand searching through a cluttered semi truck sleeper bunk — clothing, a duffel, cables, a logbook. Slight motion blur on the hand. Dim interior light. Documentary, shallow depth of field. No text, no faces.*
**Pain point:** Time lost searching · **Destination:** `/pages/cs-01`

---

### AD-03 — Comparison **[LAUNCH]**

**Primary text:**
> Most "semi truck" organizers are car organizers with truck keywords in the listing title.
>
> The straps are built for a 19-inch car seat. A Class 8 seat back runs well over 20 inches. So it doesn't reach, or it sits crooked and sags the moment you load it.
>
> The CS-01 was sized against actual Class 8 dimensions. Every measurement is on the page — check it against your truck before you spend anything.

**Headline:** One of these fits a Class 8 seat.
**Description:** Fits Cascadia, 579, T680, VNL, LT · 30-day returns
**CTA:** Shop Now
**Visual:** Both products held against the same seat back, real photograph.
**Prompt:** **REAL PHOTOGRAPH REQUIRED.** No competitor brand mark visible.
**Pain point:** Wrong-size products · **Destination:** `/pages/cs-01`

---

### AD-04 — Educational **[LAUNCH]**

**Primary text:**
> Before you buy anything for your cab, measure three things:
>
> 1. Seat back height, cushion to headrest base
> 2. Seat back width at the widest point
> 3. Clearance behind the headrest
>
> Write them in your phone. You'll use them every time — buying from us or from anyone else.
>
> Ours needs 20" × 14" minimum. Every dimension is published.

**Headline:** Measure these 3 things first.
**Description:** Full fit guide · Free shipping over $75
**CTA:** Learn More
**Visual:** Diagram over a clean cab photo, three dimensions arrowed.
**Prompt:** *Photorealistic side view of a semi truck passenger seat back inside the cab, clean and unobstructed, even light. Plain composition suitable for measurement annotation overlays. Documentary. No text, no people.*
**Pain point:** Fit uncertainty · **Destination:** `/pages/what-fits-my-truck`

*Sends to the fit guide, not the product page. Deliberate — it tests whether a low-pressure, genuinely useful destination converts better for a cold audience. If it does, that reshapes the whole funnel.*

---

### AD-05 — Product benefit **[LAUNCH]**

**Primary text:**
> Water, gloves, flashlight, tablet, clipboard — all of it within reach without unbuckling.
>
> Deep pockets for bulk. Elastic sleeves for cables and tools. A padded slot for a tablet. A flat document pocket that takes a clipboard without folding it.
>
> Straps on in two minutes. Nothing drills, nothing bolts, nothing gets modified — so there's nothing to clear with your carrier.

**Headline:** Everything without leaving your seat.
**Description:** $54.99 · No installation · 30-day returns
**CTA:** Shop Now
**Visual:** Real photo from the driver's position, hand reaching into a loaded CS-01.
**Prompt:** **REAL PHOTOGRAPH REQUIRED.**
**Pain point:** Reaching, twisting, unbuckling · **Destination:** `/pages/cs-01`

---

### AD-06 — Time saving *(Wave 2)*

**Primary text:**
> Twenty minutes a week hunting for the same three things. That's seventeen hours a year, in a job where hours are the whole business.
>
> One place for everything, within reach from the seat.

**Headline:** Seventeen hours a year, looking for a flashlight.
**Description:** CS-01 Cab Command Organizer · $54.99
**CTA:** Shop Now
**Visual:** Clock graphic over a cab interior.
**Prompt:** *Photorealistic semi truck cab interior with a dashboard clock in focus, cluttered surfaces softly out of focus behind. Early morning light. Documentary, shallow depth of field. No text, no people.*
**Angle:** Time saving · **Destination:** `/pages/cs-01`
> The 17-hour figure is arithmetic from the stated 20-minutes-a-week premise, which is itself a hypothesis. **Phrase it as an illustration, never as a measured finding.**

---

### AD-07 — Curiosity *(Wave 2)*

**Primary text:**
> There's about four square feet of usable space in your cab you've probably never used.
>
> It's the wall next to your bunk. It's completely vertical, completely empty, and your gear is sitting on the mattress instead.
>
> The CS-02 turns it into a shelf. $29.99, five minutes, no tools.

**Headline:** The space in your cab you've never used.
**Description:** CS-02 Bunk Shelf Net · $29.99
**CTA:** Learn More
**Visual:** Bunk with gear on it, empty wall above, arrow annotation.
**Prompt:** *Photorealistic semi truck sleeper bunk with a duffel bag and folded clothes on the mattress. The wall above is completely bare. Soft natural light from a curtain gap. Documentary. No text, no people.*
**Angle:** Curiosity · **Destination:** `/products/cs-02-bunk-shelf-net`
> Tests the **$29.99 entry price** against the $54.99 hero. A lower-priced winner would be a major finding for the whole model.

---

### AD-08 — Lifestyle / identity *(Wave 2)*

**Primary text:**
> Nineteen days out. It's not a hotel and it was never going to be.
>
> But it can be squared away.

**Headline:** Home for the next 19 days.
**Description:** Cab organization built for Class 8 sleepers
**CTA:** Shop Now
**Visual:** Wide interior of a well-set-up sleeper, warm evening light.
**Prompt:** *Photorealistic wide interior of a well-organized semi truck sleeper cab in warm evening light. Bunk made, gear stowed, a jacket hung. Lived-in but orderly. Documentary interior photography, natural warm color. No text, no people.*
**Angle:** Lifestyle / pride · **Destination:** `/collections/all`
> The shortest copy in the set. Tests whether identity alone converts, or whether this audience needs the functional argument. **[H] Prediction: it will win on CTR and lose on CPA.** Worth knowing either way.

---

### AD-09 — Cost saving / bundle *(Wave 2)*

**Primary text:**
> Three pieces: the seat-back organizer, the bunk shelf net, and the document folio.
>
> $112.97 bought separately. $89 together.
>
> That's the real difference between the kit price and what we actually charge for each one. Nothing gets marked up so it can be discounted.

**Headline:** Three pieces. $23.97 off.
**Description:** The Cab Reset Kit · Free shipping · 30-day returns
**CTA:** Shop Now
**Visual:** Real photo of all three products together on a bunk.
**Prompt:** **REAL PHOTOGRAPH REQUIRED.**
**Angle:** Value · **Destination:** `/products/cab-reset-kit`
> Tests **AOV directly.** Even at a worse CPA, an $89 AOV may beat a $54.99 AOV on contribution. Judge this one on contribution profit per purchase, not on CPA.

---

### AD-10 — Objection-first *(Wave 2)*

**Primary text:**
> You can probably get something similar on Amazon cheaper, and it'll get there faster. We're not going to pretend otherwise.
>
> What you'll get is a car organizer with truck keywords in the title, from a seller whose name changes every six months.
>
> Ours is sized for a Class 8 sleeper. Every dimension is published. If it doesn't fit, send it back within 30 days.
>
> If two-day shipping matters more than fit, buy the Amazon one. We'd rather you were happy than out $55.

**Headline:** We're not cheaper than Amazon.
**Description:** Built for Class 8 sleepers · Every dimension published
**CTA:** Learn More
**Visual:** Plain typographic treatment on asphalt. **No product image** — the copy is the creative.
**Prompt:** *Flat dark asphalt-gray background with subtle concrete texture, even lighting, clean and empty, suitable for a bold typographic overlay. No text, no objects.*
**Angle:** Objection handling / radical honesty · **Destination:** `/pages/cs-01`
> The highest-variance creative in the set. Leading with a disadvantage either stops the scroll cold or reads as weakness. **[H] Prediction: lowest CTR, highest conversion rate on the clicks it gets.** If that holds, it is the most valuable thing we learn all month.

---

## Creative testing protocol

- **5 creatives per ad set at launch**, identical across all three ad sets
- **Do not touch anything for 72 hours.** Editing resets the learning phase and wastes the spend already made. This is the single most commonly broken rule in small-budget testing.
- **Day 4:** first read. Kill any creative with **<0.5% CTR** and zero add-to-carts.
- **Day 7:** kill the bottom two by CPA. Introduce two Wave 2 creatives.
- **Day 10:** retargeting gate check.
- **Day 14:** full assessment against the criteria in `finance/testing-budget.md`.

**One variable at a time.** Changing creative and audience together produces a result that explains nothing.

---

## UTM convention

Enforced on every ad. No exceptions — a link without UTMs is invisible to GA4 and the data is gone permanently.

```
?utm_source=facebook
&utm_medium=paid
&utm_campaign=cold-acquisition
&utm_content=AD-01-beforeafter
&utm_term=broad
```

`utm_content` = the AD-XX code. `utm_term` = the ad set (`broad` / `interest` / `advantage`).

---

## Tracking prerequisites — ship nothing until these pass

1. Meta Pixel live via Shopify's Facebook & Instagram channel
2. **Conversions API enabled.** Not optional — browser-only tracking loses a meaningful share of events and the entire test depends on attribution.
3. Test purchase fired and confirmed in Events Manager: Purchase event present, correct value, correct currency
4. Event Match Quality acceptable on Purchase
5. Domain verified in Business Manager
6. Aggregated Event Measurement configured, Purchase prioritized first
7. GA4 receiving traffic with UTMs intact

**An ad test with broken attribution wastes the whole budget and teaches nothing.** Verify all seven before the first dollar.

---

## Rules

1. No fabricated reviews, testimonials, or ratings in any ad
2. No fake urgency, countdowns, or expiring offers
3. No health, safety, medical, or compliance claims
4. No before/after that is not the same cab, same angle, same light
5. No AI-generated image of our actual product presented as product photography
6. No unsubstantiated superlatives — "best," "#1," "the only"
7. No competitor brand marks or names
8. Meta's advertising policies govern everything above; where they conflict, they win

**Reference tags [V3], [V8] — [V3] in `research/niche-analysis.md`. [V8]: Meta ads benchmarks 2026, aggregated from TopGrowth Marketing DTC panel, Triple Whale, Sovran, Visible Factors, ROAS Hack, Get Ryze and MHI Growth Engine. Secondary aggregations, directionally reliable, not precise.**
