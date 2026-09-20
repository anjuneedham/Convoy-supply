# ConvoySupply — Metrics

**Purpose:** one place for the numbers. Filled in as the test runs.
**Rule: record actuals only.** No projections in this file, no estimates, no "roughly." An empty cell is more useful than a guessed one — it is honest about what we do not know.

---

## Reference thresholds

From `finance/unit-economics.md`. Re-run `finance/unit_economics.py` and update these when real costs land.

| Threshold | Value | Meaning |
|---|---|---|
| **Break-even CPA (base mix)** | **$39.16** | Above this, every order loses money |
| Break-even CPA (pessimistic mix) | $31.30 | If CS-02 dominates the mix |
| **Target CPA @30% margin** | **$16.88** | Where this becomes a business |
| Break-even ROAS (product revenue) | 1.90 | Meta will report ~13% higher |
| Base-case AOV | $74.29 | Below $66 means bundles are failing |
| Contribution margin floor | 45% | Below this, stop (failure condition 5) |
| Refund rate ceiling | 8% | Above this on the first 50 orders, stop |

⚠️ **All thresholds are [A] until supplier quotes replace the cost estimates.**

---

## Daily — paid ads

Fill from Ads Manager and Shopify. **Purchases come from Shopify, never from Meta.**

| Date | Day | Spend | Impr | CPM | Clicks | CTR | CPC | LPV | ATC | IC | **Purch** | Revenue | **Meta CPA** | **Blended CPA** | AOV | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | 1 | | | | | | | | | | | | | | | |
| | 2 | | | | | | | | | | | | | | | |
| | 3 | | | | | | | | | | | | | | | |
| | 4 | | | | | | | | | | | | | | | First read — kill <0.5% CTR + 0 ATC |
| | 5 | | | | | | | | | | | | | | | |
| | 6 | | | | | | | | | | | | | | | |
| | 7 | | | | | | | | | | | | | | | Kill bottom 2 by CPA; add Wave 2 |
| | 8 | | | | | | | | | | | | | | | |
| | 9 | | | | | | | | | | | | | | | |
| | 10 | | | | | | | | | | | | | | | Retargeting gate check |
| | 11 | | | | | | | | | | | | | | | |
| | 12 | | | | | | | | | | | | | | | |
| | 13 | | | | | | | | | | | | | | | |
| | 14 | | | | | | | | | | | | | | | **DECISION POINT** |

**Blended CPA = total spend ÷ total Shopify orders.** This is the only number that comes out of the bank account. Meta's CPA is for ranking creatives against each other; blended CPA is for deciding whether the business works.

---

## Per-creative

Fill at Day 4, Day 7, Day 14.

| Creative | Angle | Spend | Impr | CTR | CPC | ATC | Purch | **CPA** | Contribution/order | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| AD-01 | Before/after | | | | | | | | | |
| AD-02 | Problem/solution | | | | | | | | | |
| AD-03 | Comparison | | | | | | | | | |
| AD-04 | Educational → fit guide | | | | | | | | | |
| AD-05 | Product benefit | | | | | | | | | |
| AD-06 | Time saving | | | | | | | | | |
| AD-07 | Curiosity (CS-02) | | | | | | | | | |
| AD-08 | Lifestyle | | | | | | | | | |
| AD-09 | Bundle | | | | | | | | | |
| AD-10 | Objection-first | | | | | | | | | |

**Rank on contribution per order, not on CPA.** A bundle creative with a worse CPA can produce more profit per purchase (EXP-003). Ranking on CPA alone will pick the wrong winner.

## Per-audience

| Ad set | Spend | Impr | CPM | CTR | Purch | **CPA** | Verdict |
|---|---|---|---|---|---|---|---|
| A — Broad | | | | | | | |
| B — Interest stack | | | | | | | |
| C — Advantage+ | | | | | | | |

Answers **EXP-001**. Read with the CBO caveat in DEC-007 in mind.

---

## Funnel

| Step | Count | Rate | Target | Read |
|---|---|---|---|---|
| Impressions | | — | — | |
| Clicks | | CTR | >1.0% | <0.8% = audience doesn't recognize the problem |
| Landing page views | | LPV rate | >80% | <80% = page speed, not the ad |
| Add to cart | | LPV→ATC | >3% | <3% over 1,000 LPVs = failure condition 2 |
| Initiate checkout | | ATC→IC | >45% | <45% = shipping surprise or cart UX |
| Purchase | | IC→Purch | >60% | <60% = payment options or a checkout bug |

**Debug top down.** The most common mistake is fixing the ad when the problem is in the cart.

---

## Product mix

| SKU | Units | Revenue | Share of orders | Contribution |
|---|---|---|---|---|
| CS-01 | | | | |
| CS-02 | | | | |
| CS-03 | | | | |
| CS-04 | | | | |
| Cab Reset Kit | | | | |
| Full Rig Kit | | | | |
| **Bundle share of orders** | | | **target >30%** | |

Below 30% bundle share means the AOV lever is not working. **Fix that before raising ad budget** — it is free.

---

## Weekly — organic

| Week | Posts | Reach | Engagement rate | **Saves** | **Shares** | Comments | Link clicks | Sessions | New followers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |

**Saves and shares matter more than likes.** A save means "I'll need this," which is the strongest organic intent signal available. Track EXP-006 here.

### Best and worst post each week

| Week | Best post | Why **[H]** | Worst post | Why **[H]** |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Writing down *why* is the whole point. "Post 7 did well" teaches nothing. "Post 7 did well because it named a specific truck model" is a testable pattern.

---

## Weekly — Facebook Marketplace

| Week | Listings live | Views | Inquiries | Sales | **Inquiry→sale** | Revenue | Median response time |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

**Kill:** 30+ listing-weeks over 21 days with zero sales.
**Scale:** inquiry→sale above 15% with 5+ sales in 21 days.

### Most-asked questions

The highest-value free research in the plan. Every inquiry is a customer interview.

| Question | Times asked | Where it should be answered |
|---|---|---|
| | | |

Feed these into the PDP FAQ, the ad copy, and the fit guide.

---

## Monthly rollup

| Metric | Month 1 | Month 2 | Month 3 |
|---|---|---|---|
| Total ad spend | | | |
| Total revenue | | | |
| Orders | | | |
| AOV | | | |
| **Blended CPA** | | | |
| Gross margin % | | | |
| **Contribution margin %** | | | |
| **Contribution profit** | | | |
| Refund rate | | | |
| Marketplace revenue | | | |
| Organic sessions | | | |

**Contribution profit is not profit.** It excludes founder time, samples, tooling, inventory carrying cost, and every fixed cost outside Shopify. See the exclusions list in `finance/unit-economics.md`.

---

## Health check — review weekly

| Condition | Threshold | Status |
|---|---|---|
| Contribution margin | ≥45% | |
| Refund / complaint rate (first 50 orders) | ≤8% | |
| Blended CPA | ≤ break-even | |
| LPV→ATC | ≥3% | |
| Best-creative CTR | ≥0.8% | |
| Spend against budget | ≤$420 Phase 1 | |

**Any two red = stop and reassess. Contribution margin or refund rate red alone = stop immediately.**

---

## Data sources

| Metric | Source | Trust |
|---|---|---|
| Spend, impressions, CPM, CTR, CPC | Meta Ads Manager | Reliable |
| Meta-reported CPA and ROAS | Meta Ads Manager | **Over-reports. Creative comparison only.** |
| **Purchases, revenue, AOV, refunds** | **Shopify** | **Source of truth** |
| Sessions, funnel, UTM attribution | GA4 | Reliable with UTMs intact |
| Marketplace | Manual log | Only source |
| Organic | Meta Business Suite | Reliable |

**When Meta and Shopify disagree on orders, Shopify is right.** Meta's attribution window credits conversions it influenced loosely or not at all. That is useful for optimization and misleading for accounting.
