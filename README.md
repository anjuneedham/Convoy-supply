# ConvoySupply

**Purpose-built cab storage for people whose vehicle is their workplace — starting with over-the-road truck drivers.**

> *Squared away.*

This repository is the operating system for ConvoySupply: the research behind the niche, the brand, the store, the marketing system, the economics, and the launch plan. It is the single source of truth. If a decision is not written down here, it was not made.

**Status:** pre-launch. **Nothing in here is proven.** This is a market hypothesis with a test designed around it.

---

## Start here

| If you want to know… | Read |
|---|---|
| Why this niche and not another | `research/niche-analysis.md` → `research/selected-niche.md` |
| What we're selling and for how much | `research/product-selection.md` |
| Who we're selling to | `research/customer-avatar.md` |
| What the brand sounds like | `brand/brand-strategy.md` → `brand/brand-copy.md` |
| How the store is built | `store/store-architecture.md` → `theme/README.md` |
| What the landing page looks like | Open `prototype/cs-01-landing.html` in a browser |
| Whether the numbers work | Run `python3 finance/unit_economics.py` |
| What we do on day one | `execution/30-day-plan.md` |
| Why we decided something | `execution/decisions.md` |

---

## The thesis, in one paragraph

A Class 8 sleeper cab is 50–70 square feet that a driver lives in for weeks at a time, and it ships with a bunk, a dash, and two shallow cubbies. Everything else lives on the passenger seat. The market for fixing this is full of **products but has no brand** — Amazon listings are generic car organizers with truck keywords, and specialty truck retailers are distributors, not brands. That gap can be attacked with photography, copy, and honesty rather than capital, which is the only kind of gap a small operator can actually close. We are testing whether a professional driver will buy cab gear from an unknown brand on Facebook.

**Six candidate niches were evaluated.** This one won because it is the only one that cleared every hard constraint at once — static-image sellability, Marketplace price band, margin headroom, low operational risk, and brand-name coherence. The full comparison, including the two niches that scored well and were rejected anyway, is in `research/niche-analysis.md`.

---

## Repository map

```
research/     Niche analysis, selection, products, customer, competitors
brand/        Positioning, voice, visual identity, reusable copy
store/        Architecture, homepage copy, PDP spec, hero landing page
theme/        Shopify Liquid — 9 custom Dawn sections + 2 templates
prototype/    Static HTML preview of the landing page
marketing/    30 static posts, 30-day organic calendar, Marketplace, Meta ads, creative register
finance/      unit_economics.py (the model) + unit-economics.md (its output) + testing budget
execution/    30-day plan, decision log, experiment log, metrics, daily log
prompts/      AI image prompts for organic and ads
```

---

## Three things to know before reading anything else

### 1. There is a naming conflict, and it is real

**Convoy Supply Ltd.** is an existing building-envelope and building-materials wholesale distributor, founded 1972, operating across Canada, the Pacific Northwest US, and Maryland, at `convoy-supply.com`.

This shaped the strategy rather than being noted and forgotten:

- It **disqualified the trades/jobsite niche**, which scored second-highest on commercial merit (`DEC-002`)
- It makes a **USPTO clearance search a Day 1 gate** that blocks all brand spend (`DEC-001`)
- The brand is always written as **one word — ConvoySupply** — never "Convoy Supply"

If clearance fails, the rename touches the brand doc, the theme's color tokens, and the logo. Product names deliberately carry no brand prefix so they survive it.

### 2. Every claim is tagged, and most of them are hypotheses

- **[V]** verified against a cited source
- **[H]** hypothesis — reasoned, testable, unproven
- **[A]** assumption — needs replacing with real data

**Every cost figure in this repository is [A] until supplier quotes arrive on Day 5.** Most of the customer avatar is **[H]**. That is honest rather than weak — the 30-day test exists to convert **[H]** into **[V]**, and labelling them makes it possible to tell which is which later.

**There are no fabricated statistics, reviews, testimonials, or customer quotes anywhere in this repository.** Where a number would normally appear and we do not have one, the document says so.

### 3. The honest-marketing rules are enforced in code, not just stated

`DEC-003` bans dark patterns. The theme implements the ban structurally:

- `cs-proof.liquid` **cannot render a review that was not entered as a real one.** At launch the array is empty and an honest "no reviews yet" message renders instead.
- `cs-offer.liquid` derives savings from Shopify's own compare-at price, so it cannot display a discount that isn't configured.
- **No countdown, stock-counter, "X viewing", or exit-intent component exists in the theme.** Adding one means writing it, which is the point.
- Zero apps at launch — partly for speed, partly because most review apps can import unverified reviews and having the capability installed is a standing temptation.

This is not only ethics. This audience is unusually suspicious of marketing, discusses sellers publicly in Facebook Groups, and will screenshot a fake countdown. **Being visibly honest in a category that visibly is not is the only real asset we have at launch.**

---

## The catalog

Four launch SKUs plus one gated. They are **one system sold in pieces** — each addresses a different zone of the cab, which is what makes the bundle a real argument rather than a discount gimmick.

| SKU | Product | Price | Zone | Role |
|---|---|---|---|---|
| CS-01 | Cab Command Organizer | $54.99 | Passenger seat back | **Hero** |
| CS-02 | Bunk Shelf Net | $29.99 | Bunk wall | Entry / acquisition |
| CS-03 | Manifest Folio | $27.99 | Paperwork | Upsell |
| CS-04 | Haul Bag | $49.99 | Under-bunk bay | Bundle anchor |
| CS-05 | Dash Power Rail | $44.99 | Dash power | **Gated — `DEC-004`** |

**Bundles:** Cab Reset Kit **$89** (save $23.97) · Full Rig Kit **$129** (save $33.96). Savings are real differences against prices genuinely charged.

**CS-05 is gated out of launch** because it is an electrical product in a vehicle with the worst margin in the range. It launches only if UL/ETL certification, a documented fuse rating, liability insurance, and a validated soft-goods hypothesis are all in place. Four coherent products beat five with a liability in the middle.

---

## The economics

Run the model rather than trusting a table:

```bash
python3 finance/unit_economics.py
```

Everything in `finance/unit-economics.md` is output from that script. Change the inputs, re-run, commit both.

**The finding that shapes the whole offer:**

| | CS-01 alone | Cab Reset Kit |
|---|---|---|
| Contribution margin | **59.3%** | 47.8% |
| Break-even CPA | $32.59 | **$42.52** |

The bundle gives up 11.5 points of margin percentage and buys **$9.93 more room per order** to pay for the customer. **Margin percentage is a vanity metric when the binding constraint is acquisition cost.** That is why bundles appear in the cart, on every PDP, and as the second option on the landing page.

**The counterintuitive corollary:** if the $29.99 CS-02 ad wins, AOV falls and blended break-even CPA drops from $39.16 to $31.30. **A "winning" ad can make the business harder**, which is why `marketing/meta-ads.md` says to judge creative on contribution per order rather than on CPA alone.

**Red line:** if CS-01's landed cost comes back above **$22**, contribution margin falls under the 45% floor and the offer must be re-priced before anything else is built.

---

## The test

| | |
|---|---|
| **Budget** | ~$1,574–$1,874 total, of which **$720 is gated** on evidence |
| **Paid test** | $30/day × 14 days = $420 |
| **Structure** | 3 cold audiences × 5 creatives, creative held constant so audience is the variable |
| **Retargeting** | Gated behind 1,000+ LPVs and 50+ ATCs (`DEC-005`) |
| **Decision point** | **Calendar Day 38** — ads launch Day 25 |

### Failure is defined in advance

From `research/selected-niche.md`, written before the test so it cannot be rationalized afterward:

1. CPA above break-even across all angles with no downward trend
2. LPV → ATC under 3% across 1,000+ views
3. CTR under 0.8% across all 10 creatives
4. Zero Marketplace sales from 30+ listings over 21 days
5. Contribution margin under 45%
6. Refund/complaint rate over 8% on the first 50 orders

**Any two = stop and reassess. 5 or 6 alone = stop immediately.**

### What failure costs, and buys

Maximum realistic loss is roughly **$1,100–$1,500**. In exchange we would know whether drivers buy from an unknown brand on Facebook, what reaching them actually costs, which of five buying motivations moves money, whether broad beats interest targeting, whether Marketplace works for shipped auto accessories, and what our real landed costs are.

**That is a reasonable price for those answers**, and far cheaper than finding out at scale.

---

## A scheduling reality

**The 14-day ad test does not finish inside the 30-day plan.** Samples take 7–14 days, photography depends on samples, creative depends on photography, and ads depend on creative. Ads launch on Day 25, so the decision point is calendar Day 38.

This is what the dependencies produce, not a planning error. Compressing it would mean launching with weak creative, which wastes the budget and answers nothing. **Day 30 is a checkpoint, not a verdict.** Plan cash accordingly.

Two channels can produce results inside 30 days, and both cost time rather than money: **Marketplace** (live Day 19) and **organic** (live Day 21).

---

## Working conventions

1. **Append-only logs.** `decisions.md` and `daily-log.md` are never edited, only added to. If something changes, supersede it.
2. **Hypotheses before results.** `experiments.md` requires the prediction and the success criterion to be written before the test starts, and never edited after.
3. **Tag every claim** as [V], [H] or [A].
4. **When a hypothesis is falsified, delete it** from the research docs — do not soften the wording. A hedged wrong belief still shapes decisions while looking harmless.
5. **Formulas, not conclusions.** Financial figures come from the script.
6. **No `[TBC]` ships.** Every published page must have its placeholders replaced; the pre-publish checklists cover this.

---

## Immediate next actions

The three Day 1 gates. Everything else has slack; these do not.

1. **USPTO TESS clearance search** — classes 12, 18, 35. Blocks all brand spend. (`DEC-001`)
2. **Meta Ad Library competitor check** — tests the "no DTC competitor" claim the whole strategy rests on. **If a funded competitor is already running this playbook, the plan needs revisiting on Day 1, not Day 20.** (`EXP-009`)
3. **Contact suppliers and order samples** — longest lead time in the plan, and blocks three of the five launch ad creatives.

Then: arrange cab access for a shoot around Day 12.

Full sequence in `execution/30-day-plan.md`.
