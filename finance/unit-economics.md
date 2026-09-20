# ConvoySupply — Unit Economics

**Date:** 2026-09-20
**Model:** `finance/unit_economics.py` — run it, don't trust this page
**Status:** **every cost input is an [A] estimate pending supplier quotes (Day 5)**

---

## How to use this document

Every number below is **output from the script**, not typed by hand. When a cost changes:

```bash
python3 finance/unit_economics.py
```

Edit the inputs at the top of the script, re-run, paste the output here, and commit both. The reasoning never needs rewriting because the reasoning is in the formulas.

**This is the point of building it this way.** Landed cost is currently a guess. When the real quote arrives — and it will be different — break-even CPA, target ROAS, and the entire go/no-go decision recalculate in one command instead of requiring someone to re-derive the business.

---

## The formulas

```
Gross revenue        = product price + shipping charged to customer

Variable costs       = landed cost
                     + outbound shipping we pay
                     + payment fee            (2.9% × gross + $0.30)   [V7]
                     + packaging
                     + refund allowance       (refund rate × price)
                     + platform cost          (Shopify monthly ÷ orders)

Contribution         = gross revenue − variable costs
                       ↑ this is the money available to pay for advertising AND profit

Gross margin %       = (price − landed cost) ÷ price
Contribution margin% = contribution ÷ price

Break-even CPA       = contribution
                       (spend exactly this per order and you make exactly zero)
Break-even ROAS      = price ÷ contribution

Target CPA  @ m      = contribution − (price × m)
Target ROAS @ m      = price ÷ target CPA
                       where m = contribution margin retained after advertising
```

**Break-even CPA equals contribution.** That identity is the most important line in this document. Everything else is arithmetic around it.

## Shared inputs

| Input | Value | Source |
|---|---|---|
| Payment processing | **2.9% + $0.30** | Shopify Payments, Basic plan **[V7]** |
| Platform | **$39/mo** ÷ 60 orders = **$0.65/order** | Shopify Basic month-to-month **[V7]** |
| Refund allowance | **5%** of product revenue | **[A]** |
| Free shipping threshold | **$75** | Set just below the $89 kit, deliberately |
| Flat shipping below threshold | **$6.95** charged to customer | **[A]** |
| Orders/month for fixed-cost spread | **60** | **[A]** planning assumption |
| Target margin after ads | **30%** of product revenue | Decision, not a benchmark |

**On the $39/mo figure:** Shopify Basic is $39 month-to-month, or an effective $29/mo billed annually **[V7]**. The model uses $39 because committing to a year before the test has run is exactly the kind of decision this test exists to avoid. At 60 orders/month the difference is $0.17 per order — immaterial to the model, material to cash risk.

---

## Per-offer economics

*Output of `unit_economics.py`, 2026-09-20. Costs are **[A]**.*

| Offer | Price | Landed **[A]** | Contribution | GM% | **CM%** | **BE CPA** | BE ROAS | Target CPA @30% | Target ROAS @30% |
|---|---|---|---|---|---|---|---|---|---|
| CS-01 Cab Command Organizer | $54.99 | $15.50 | **$32.59** | 71.8% | 59.3% | **$32.59** | 1.69 | $16.10 | 3.42 |
| CS-02 Bunk Shelf Net | $29.99 | $6.80 | **$20.52** | 77.3% | 68.4% | **$20.52** | 1.46 | $11.52 | 2.60 |
| CS-03 Manifest Folio | $27.99 | $6.50 | **$18.98** | 76.8% | 67.8% | **$18.98** | 1.47 | $10.58 | 2.65 |
| CS-04 Haul Bag | $49.99 | $14.00 | **$28.39** | 72.0% | 56.8% | **$28.39** | 1.76 | $13.39 | 3.73 |
| **Cab Reset Kit** | $89.00 | $28.80 | **$42.52** | 67.6% | 47.8% | **$42.52** | 2.09 | $15.82 | 5.63 |
| **Full Rig Kit** | $129.00 | $42.80 | **$63.56** | 66.8% | 49.3% | **$63.56** | 2.03 | $24.86 | 5.19 |

### Worked example — CS-01

```
  Product revenue                $54.99
  Shipping charged                $6.95
  GROSS                          $61.94
  − Landed cost            [A]   −$15.50
  − Outbound shipping      [A]    −$7.50
  − Payment fee (2.9%+$0.30)      −$2.10
  − Packaging                     −$0.85
  − Refund allowance (5%)         −$2.75
  − Platform ($39 ÷ 60)           −$0.65
  CONTRIBUTION                   $32.59   ← break-even CPA
```

### The finding that should change behaviour

**The bundle has a *worse* margin percentage and a *better* CPA ceiling.**

| | CS-01 alone | Cab Reset Kit |
|---|---|---|
| Contribution margin | **59.3%** | 47.8% |
| Break-even CPA | $32.59 | **$42.52** |

The kit gives up 11.5 points of margin percentage and buys **$9.93 more room per order** to pay for the customer.

At the benchmark ecommerce CPC of ~$0.67 **[V8]** and a 2% landing-page conversion rate, a purchase costs roughly $33.50 in clicks — which is **above** CS-01's break-even and **below** the kit's. On those assumptions, single-item orders barely wash and bundle orders work.

**That single comparison is the strongest argument in this repository for pushing bundles hard**, and it is why the bundle nudge sits in the cart, on the PDP, and as the second option on the landing page. Margin percentage is a vanity metric when the constraint is cost per acquisition. **Absolute contribution per order is what buys customers.**

---

## Blended by order mix

| Scenario | Mix | AOV | Contribution | CM% | **BE CPA** | BE ROAS | Target CPA @30% | Target ROAS @30% |
|---|---|---|---|---|---|---|---|---|
| **Base** | 55% CS-01 / 35% Kit / 10% Full | **$74.29** | **$39.16** | 52.7% | **$39.16** | 1.90 | $16.88 | 4.40 |
| **Pessimistic** | 40% CS-02 / 35% CS-01 / 20% Kit / 5% Full | **$55.49** | **$31.30** | 56.4% | **$31.30** | 1.77 | $14.65 | 3.79 |
| **Optimistic** | 40% CS-01 / 40% Kit / 20% Full | **$83.40** | **$42.76** | 51.3% | **$42.76** | 1.95 | $17.74 | 4.70 |

**The pessimistic scenario is not pessimism — it is the most likely outcome of a successful CS-02 ad.** CS-02 at $29.99 is the cheapest entry point and the concept most likely to win on CTR (AD-07). If it does, AOV falls to $55.49 and break-even CPA falls to **$31.30**.

**So a "winning" ad can make the business harder.** That is counterintuitive enough to be worth stating plainly, and it is why `marketing/meta-ads.md` says to judge AD-09 (the bundle ad) on **contribution profit per purchase, not on CPA**. A creative with a worse CPA and a higher AOV can be the better ad. Judging the test on CPA alone would pick the wrong winner.

---

## Sensitivity — what if landed cost is wrong?

It will be. This is the table to check when the quotes arrive.

| Landed cost **[A]** | Contribution | CM% | Break-even CPA |
|---|---|---|---|
| $10.00 | $38.09 | 69.3% | $38.09 |
| $12.50 | $35.59 | 64.7% | $35.59 |
| **$15.50 (modeled)** | **$32.59** | **59.3%** | **$32.59** |
| $18.00 | $30.09 | 54.7% | $30.09 |
| $20.00 | $28.09 | 51.1% | $28.09 |
| $22.00 | $26.09 | 47.5% | $26.09 |
| $25.00 | $23.09 | 42.0% | $23.09 |

**The red line is $22.00.** Above that, CS-01's contribution margin falls under the 45% floor in failure condition 5 of `research/selected-niche.md`, and the offer needs re-pricing or the SKU needs dropping.

**If quotes come back above $22 landed on the hero, stop and re-price before building anything else.** Every downstream decision in this repository assumes the margin structure holds.

---

## What a given CPA means — base mix

The decision table. Print it and put it next to Ads Manager.

| CPA | Profit/order | Margin on AOV | Verdict |
|---|---|---|---|
| $10.00 | $29.16 | 39.3% | **Scale it** |
| $15.00 | $24.16 | 32.5% | **Scale it** |
| $20.00 | $19.16 | 25.8% | **Scale it** |
| $25.00 | $14.16 | 19.1% | Workable |
| $30.00 | $9.16 | 12.3% | Workable |
| $35.00 | $4.16 | 5.6% | Marginal |
| **$39.16** | **$0.00** | **0.0%** | Break-even |
| $45.00 | −$5.84 | −7.9% | **LOSS — stop** |
| $50.00 | −$10.84 | −14.6% | **LOSS — stop** |

---

## Reading ROAS correctly

**Meta's reported ROAS will not equal the break-even ROAS in these tables, and confusing the two will cost money.**

- Our break-even ROAS uses **product revenue** (price ÷ contribution)
- Meta reports ROAS on **purchase conversion value**, which is normally the full order total **including shipping charged**

For CS-01 that is $61.94 rather than $54.99 — Meta's number will read about **13% higher** than ours for the same underlying performance.

**Use CPA as the primary decision metric, not ROAS.** CPA is unambiguous, directly comparable to the contribution figures above, and not subject to a definitional gap. ROAS is for reporting; CPA is for deciding.

## Attribution — the bigger distortion

Meta's attribution window will over-report. Reconcile weekly:

```
Blended CPA = total ad spend ÷ total Shopify orders
```

Not Meta's reported CPA. Blended CPA is the number that has to clear the tables above, because it is the only one that comes out of the bank account.

---

## Metrics and how each one drives a decision

| Metric | What it tells you | Decision |
|---|---|---|
| **CPM** | Cost of reach. Automotive benchmark ~$10.01 **[V8]**. | >$25 sustained = audience too narrow or creative fatigued. Broaden or refresh. |
| **CTR** | Does the creative land? | <0.8% across all concepts = the audience doesn't recognize the problem. Failure condition 3. |
| **CPC** | Reach × relevance. Ecommerce benchmark ~$0.67 **[V8]**. | >$2.00 sustained = creative or audience problem. Fix CTR first. |
| **LP view rate** | Clicks that actually load. | <80% = page speed. Fix the site, not the ad. |
| **LPV → ATC** | Does the offer land? | <3% over 1,000+ LPVs = failure condition 2. The page or price is wrong, not the ad. |
| **ATC → IC** | Cart friction. | <45% = shipping cost surprise or cart UX |
| **IC → Purchase** | Checkout friction. | <60% = payment options or a checkout bug. Test it yourself. |
| **CPA** | **The primary decision metric.** | Against the table above |
| **AOV** | Bundle attach rate. | Below $66 = bundles aren't working. Push them harder before touching the ads. |
| **Contribution margin** | Whether the business works at all. | <45% = failure condition 5. Stop. |
| **Blended CPA** | The truth. | The only number that clears the bank |

### Diagnostic order — work top down

Most people debug the ad when the problem is further down the funnel. Work in this order:

1. **CTR low** → creative problem. Nothing downstream matters yet.
2. **CTR fine, LP view rate low** → page speed.
3. **LP views fine, ATC low** → offer, price, or fit confidence. Not the ad.
4. **ATC fine, checkout low** → shipping cost or a checkout bug.
5. **All fine, CPA still high** → the audience is expensive. Raise AOV before raising budget.

---

## What this model does not include

Named so nobody mistakes contribution for profit:

- Founder time (the largest real cost in the business, and unpaid)
- Product samples and photography
- Domain, email, and design tools
- Inventory carrying cost and cash tied up in stock
- Customs, duty and broker surprises beyond the landed estimate
- Chargebacks and fraud
- Any cost of a trademark clearance search or attorney time (DEC-001)

**Contribution ≠ profit.** Clearing break-even CPA means the marginal order is not losing money. It does not mean the business is making any.

---

## Actions

1. **Get three supplier quotes per SKU.** Replace every **[A]**. Until then this model is arithmetic on guesses. *(Day 4–5)*
2. **Confirm real shipped weights and dimensions** — outbound shipping is a top-three cost line and is currently estimated.
3. **Re-run the script and commit both the script and this page** once real numbers land.
4. **Check the hero against the $22 red line** before building anything further.
5. **Track blended CPA weekly**, not Meta's number, in `execution/metrics.md`.

**Reference tags: [V7] Shopify pricing — `store/store-architecture.md`. [V8] Meta benchmarks — `marketing/meta-ads.md`.**
