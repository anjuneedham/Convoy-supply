# ConvoySupply — Testing Budget & Decision Framework

**Date:** 2026-09-20
**Principle:** the budget is sized so that **losing all of it is survivable and informative.** Nothing here assumes profitability.

---

## Total 30-day budget

| Line | Amount | Notes |
|---|---|---|
| Meta ads — cold test, 14 days @ $30/day | **$420** | The core experiment |
| Meta ads — extension or retargeting, days 15–30 | **$300** | **Conditional.** Only spent if Phase 1 clears its gate. |
| Product samples (4 SKUs) | **$150** | **[A]** Blocks all photography. Spend first. |
| Shopify Basic, 1 month | **$39** | **[V7]** |
| Domain | **$15** | **[A]** |
| Initial inventory (or fulfillment deposit) | **$400** | **[A]** Depends on the model chosen — see below |
| Photography (cab access, props) | **$100** | **[A]** May be $0 if access is borrowed |
| Trademark clearance search | **$0–$300** | **[A]** DEC-001. $0 if self-searched, up to $300 for an attorney hour. |
| Contingency | **$150** | |
| **TOTAL** | **$1,574–$1,874** | |

**Committed before any revenue: roughly $1,100** (samples, Shopify, domain, photography, clearance, contingency, Phase 1 ads). The remaining $700–800 is conditional.

**The most important structural feature of this budget is that $720 of the $1,574 is gated.** Ad spend beyond Phase 1 and inventory beyond samples are both decisions made *after* evidence arrives, not before.

---

## The inventory question — decide before ordering

| Model | Upfront | Margin | Speed | Risk |
|---|---|---|---|---|
| **Hold stock** | $400+ | Best | Best | Dead inventory if the test fails |
| **Dropship / print-on-demand equivalent** | ~$0 | Worst | Worst | Slow shipping undermines the offer |
| **Small buy (10–15 units of CS-01 and CS-02 only)** | ~$300 | Good | Good | Limited, and stock-outs are possible |

**Recommendation: the small buy.** Order CS-01 and CS-02 only — the hero and the entry SKU. CS-03 and CS-04 can be listed as made-to-order with an honest ship date until demand is proven.

The reasoning is that **shipping speed is already our weakest position against Amazon** (see `research/competitor-analysis.md`), and a dropship model makes the one thing we are worst at even worse. Holding a small amount of the two SKUs most likely to sell protects the offer where it is most fragile, at a cost of roughly $300.

*Recorded as DEC-006 in `execution/decisions.md`.*

---

## Phase 1 — Cold test (Days 1–14)

| Parameter | Value |
|---|---|
| Daily budget | **$30/day CBO** |
| Total | **$420** |
| Campaign | Cold acquisition, Sales objective, Purchase |
| Ad sets | 3 — Broad · Interest stack · Advantage+ |
| Creatives | 5 at launch, identical across all three ad sets |
| Duration | 14 days |
| First read | Day 4 |
| First optimization | Day 7 |
| Decision point | **Day 14** |

### Why $30/day and not less

At $10/day, no ad set exits the learning phase inside 14 days and the test produces noise. At the benchmark ecommerce CPM of ~$10.42 **[V8]**, $30/day buys roughly **2,880 impressions/day** — around 40,000 over 14 days. At a 1% CTR that is ~400 clicks and, at a 2% conversion rate, **~8 purchases.**

**Eight purchases is not statistical significance and nobody should pretend it is.** It is enough to distinguish "clearly working" from "clearly not," which is the actual question. Anyone promising statistical confidence at this budget is selling something.

### Why $30/day and not more
More spend before knowing whether the creative works is buying an expensive answer to a cheap question.

### What must be true before a dollar is spent

Hard gate. **Do not launch if any of these fail:**

- [ ] Meta Pixel live and firing
- [ ] **Conversions API enabled** — not optional
- [ ] Test purchase confirmed in Events Manager, correct value and currency
- [ ] Domain verified in Business Manager
- [ ] Aggregated Event Measurement configured, Purchase prioritized
- [ ] All 5 creatives approved and UTM-tagged
- [ ] Landing page live, mobile-tested on real cellular, under 2.5s LCP
- [ ] Every `[TBC]` replaced with a real value across the store
- [ ] Returns, shipping and privacy policies live
- [ ] Support email monitored
- [ ] Inventory physically in hand for anything listed as in stock

**An ad test with broken attribution wastes the entire budget and teaches nothing.** This checklist is cheaper than the $420.

---

## Phase 1 success criteria — Day 14

Written before the test so they cannot be rationalized afterward. Base-mix break-even CPA is **$39.16** (`finance/unit-economics.md`).

### PASS — continue and extend
**All** of:
- At least **one creative** at CPA **below $39.16**
- **5+ purchases** total
- LPV → ATC **above 3%**
- Best creative CTR **above 1.0%**

→ Kill the losers, scale the winner to $50/day, open retargeting if gated conditions are met, spend the conditional $300.

### CONDITIONAL — extend once, do not scale
**Any** of:
- CPA between **$39.16 and $55**, trending down over the last 7 days
- 2–4 purchases with ATC rate above 3%
- One creative clearly outperforming but with too little volume to judge

→ Extend 7 days at $30/day with the two best creatives only and two Wave 2 concepts. **One extension. Not two.** A test that needs a third extension has answered the question.

### FAIL — stop paid, keep organic and Marketplace
**Any** of:
- **Zero purchases** across 14 days and $420
- CPA above **$55** with no downward trend
- CTR below **0.8%** across all five creatives
- LPV → ATC below **1.5%** over 500+ LPVs

→ Stop the ads. Do not spend the conditional $300. Diagnose against the table below. Organic and Marketplace continue — they cost time, not money.

---

## Kill criteria — during the test, not just at the end

Apply these before Day 14. They exist to stop slow bleeding.

| Trigger | When | Action |
|---|---|---|
| A creative under 0.5% CTR with zero ATC | Day 4 | Kill that creative |
| A creative at 3× the best CPA | Day 7 | Kill it |
| **Contribution margin measured below 45%** | Any time | **Stop everything.** Failure condition 5. |
| **Refund or complaint rate above 8% on the first 50 orders** | Any time | **Stop everything.** Failure condition 6 — the product is not good enough. |
| Total spend hits $420 | Day 14 | Hard stop. Decide before spending more. |

The last row is the discipline that matters. **The budget is a stop, not a target.** Budgets get quietly extended by people who are almost there, and "almost there" is where most small tests die.

---

## Scaling criteria — do not scale early

Only after **10+ purchases** at a CPA below target, and only:

- **Increase by 20–30% at a time, no more than every 3 days.** Larger jumps reset the learning phase.
- **Duplicate the winner into a new ad set before raising budget on the existing one.** Protects a working ad set from being destabilized.
- **Raise AOV before raising budget.** A bundle attach improvement is free; more spend is not. (See the bundle finding in `finance/unit-economics.md`.)
- **Never scale on a single good day.** Use a 3-day rolling average.

---

## Metrics tracked daily

Logged in `execution/metrics.md`.

| Metric | Source | Watch for |
|---|---|---|
| Spend | Ads Manager | Against the $420 cap |
| Impressions / CPM | Ads Manager | CPM >$25 sustained |
| CTR | Ads Manager | <0.8% across all creatives |
| CPC | Ads Manager | >$2.00 sustained |
| Landing page views | Ads Manager + GA4 | LP view rate <80% = speed problem |
| Add to cart | Pixel + Shopify | LPV→ATC <3% |
| Initiate checkout | Pixel + Shopify | ATC→IC <45% |
| Purchases | **Shopify** | The only trustworthy source |
| Revenue / AOV | Shopify | AOV <$66 = bundles failing |
| **Meta-reported CPA** | Ads Manager | For creative comparison only |
| **Blended CPA** | spend ÷ Shopify orders | **The real number** |
| Refunds | Shopify | >8% = stop |
| Marketplace inquiries / sales | Manual | Parallel channel |

**Meta's CPA is for ranking creatives against each other. Blended CPA is for deciding whether the business works.** Never confuse them.

---

## Diagnosing a failure

| Symptom | Most likely cause | Next test |
|---|---|---|
| Low CTR everywhere | Audience doesn't recognize the problem, or creative is weak | New angles before new audiences |
| High CTR, low ATC | Page or offer fails, not the ad | Rebuild the landing page. Test PDP vs landing (EXP-007). |
| High ATC, low checkout | Shipping cost surprise | Test free shipping on everything, price rolled in |
| High checkout, low purchase | Payment or a checkout bug | **Complete a real purchase yourself on a phone** |
| Interest beats broad by a lot | Occupational targeting works here | Build more interest stacks |
| Broad beats interest by a lot | Creative is self-selecting | Consolidate; spend on creative, not targeting |
| CS-02 outsells CS-01 | Price sensitivity is the binding constraint | Re-price the range down; volume model |
| Bundles outsell singles | AOV strategy is working | Lead with the kit everywhere |
| Everything flat, no signal at all | Wrong audience or wrong product | Return to `research/niche-analysis.md` |

---

## Day 14 and Day 30 decision trees

### Day 14
```
5+ purchases AND best CPA < $39.16?
├── YES → PASS. Kill losers, scale winner to $50/day, spend the $300.
└── NO
    ├── 2-4 purchases, CPA trending down? → CONDITIONAL. One 7-day extension.
    └── 0-1 purchases or CPA > $55 flat  → FAIL. Stop paid. Keep organic + Marketplace.
```

### Day 30
```
Is blended CPA below break-even CPA for the actual order mix?
├── YES → Continue. Month 2 at a higher budget. Reinvest contribution only.
└── NO
    ├── Improving trend + at least 10 purchases → One more 30-day cycle. Fix the weakest funnel step.
    └── Flat or worsening → STOP PAID.
        ├── Marketplace producing sales? → Marketplace-first business. Shopify becomes the back end.
        └── Nothing working?             → Hypothesis falsified. Back to research/niche-analysis.md
                                            with the learnings intact.
```

---

## What "failure" actually costs

Worth stating plainly before starting.

**Maximum realistic loss: about $1,100–$1,500**, most of it in ad spend and samples, minus whatever inventory can be recovered by selling at cost on Marketplace.

In exchange we would know, with evidence:
- Whether truck drivers buy cab gear from an unknown brand on Facebook
- What it actually costs to reach them
- Which of five buying motivations moves money
- Whether broad beats interest targeting for a niche occupational audience
- Whether Marketplace is a real channel for shipped auto accessories
- What the actual landed costs and margins are

**That is a reasonable price for those answers**, and it is considerably cheaper than finding them out at scale. A test designed so that failure is affordable and informative is the only kind worth running at this budget.

**Reference tags: [V7] `store/store-architecture.md`. [V8] `marketing/meta-ads.md`.**
