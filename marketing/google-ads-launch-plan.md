# Google Ads Launch Plan

**Per DEC-014:** Google is the first paid channel. Facebook second, TikTok third.
**Status:** Ready to set up — all 4 products are listed and priced.

---

## Why Google first (the reasoning, so it can be challenged later)

Someone typing "truck cab organizer" into Google has already decided they want the thing. Someone scrolling Facebook has not. For an unknown brand with no social proof and no reviews, buying warm intent is cheaper than manufacturing cold demand.

The tradeoff: search volume for this niche is capped. Google will find the people already looking, but it won't create new ones. That's what Facebook and TikTok are for later — once the funnel is proven to convert at all.

---

## The numbers you're working against

Real contribution per order, from actual CJdropshipping landed costs:

| Offer | Price | Landed cost | Contribution | **Break-even CPA** |
|---|---|---|---|---|
| CS-01 Cab Command Organizer | $50.00 | $28.77 | $23.08 | **$23.08** |
| CS-02 Bunk Shelf Net | $29.99 | $12.50 | $20.92 | **$20.92** |
| CS-03 Manifest Folio | $27.99 | $9.08 | $22.50 | **$22.50** |
| CS-04 Haul Bag | $49.00 | $32.81 | $18.12 | **$18.12** |
| **Cab Reset Kit** | $89.00 | $50.35 | **$37.42** | **$37.42** |
| **Full Rig Kit** | $129.00 | $83.16 | **$41.45** | **$41.45** |

*(Contribution = revenue incl. $6.95 shipping charged − landed cost − 2.9%+$0.30 payment fee − 5% refund allowance − $0.65 platform cost)*

**The single most important line here:** bundles give you **$37–41 of CPA room** versus **$18–23** for single items. Same insight as the original unit-economics model — margin *percentage* is worse on bundles, but absolute contribution per order is nearly double, and absolute contribution is what buys customers.

**Practical implication:** push the kits in ad copy and on the landing page. A campaign that sells only CS-04 at $18 break-even CPA will struggle in a category where clicks aren't free. A campaign that sells Cab Reset Kits at $37 break-even CPA has real headroom.

**[A] Assumption to validate:** automotive/accessory CPCs typically run $0.80–$2.50. At a 2–4% site conversion rate, that implies roughly $25–$100 per conversion before optimization. **Your first two weeks will likely run above break-even CPA.** Budget for that as tuition, not failure.

---

## Phase 1 — Setup (before any spend)

### 1. Install the Google & YouTube channel in Shopify
Shopify admin → **Apps** → search "Google & YouTube" → install (free, first-party).

This is the fastest path to a product feed. It auto-syncs your 4 products into Google Merchant Center and keeps price/availability updated. Doing this manually via Merchant Center feed files is slower and breaks more.

### 2. Create/connect Google Merchant Center
The Shopify channel will walk you through it. You need:
- A Google account
- Your store URL verified and claimed (the Shopify app does this automatically)
- Shipping settings configured in Merchant Center (must match what you actually charge — free over $75, flat rate under)
- Return policy published on your site (Merchant Center requires it)

### 3. Fix product images FIRST
**Do not sync the feed until the image audit is applied** (`store/product-image-audit.md`). Three supplier images have promotional text overlays and will get those products disapproved. Set the compliant image as each product's featured image before syncing.

### 4. Set up conversion tracking
Without this you are flying blind and Google's bidding has nothing to optimize toward.
- The Google & YouTube Shopify app installs the Google tag and sets up Purchase conversion automatically
- **Verify it fires:** place a real test order on your own store, then check Google Ads → Goals → Conversions within 24h for a recorded conversion
- **This is a hard gate.** No campaign launches until a test purchase has registered a correctly-valued conversion.

### 5. Merchant Center approval wait
Product approval typically takes **1–3 business days**, sometimes longer for a new account. Start this early — it's the longest lead time in the setup.

---

## Phase 2 — Campaign structure

### Starter variant: $5/day, two products, Shopping only

**Use this to launch, then graduate to the full plan below once the pipeline is validated.**

At $5/day you get roughly 3–6 clicks total (at $0.80–$1.50 CPC) — not enough to meaningfully split across campaign types or the full 4-product catalog. So:

- **One campaign: Standard Shopping only.** Skip Search at this budget — Shopping matches your product feed directly, no keyword research needed.
- **Products:** **CS-01 and CS-02 only**, via a product group filter that excludes CS-03 and CS-04 from this campaign's targeting. Reasoning:
  - **CS-01** — best keyword match to real search volume ("truck cab organizer," "truck seat organizer"), break-even CPA $23.08
  - **CS-02** — lower price point for an easier first purchase from an unknown brand, real search terms exist ("truck cargo net"), break-even CPA $20.92, best margin of the two (69.8%)
  - CS-03 excluded: weak standalone search demand (upsell item, not something people search for directly)
  - CS-04 excluded: below the 45% margin floor per DEC-015, not advertised standalone regardless of budget
- **Bidding:** Manual CPC, max **$0.75** (lower than the full-plan $1.00, to stretch the thin daily budget across more clicks)
- **Budget:** $5.00/day
- **Goal at this stage is not performance — it's validating the pipeline** (feed approved, images compliant, checkout completes, conversion tracking fires). Expect roughly a week to gather 20-30 clicks. Once validated, graduate to the full plan below.

### Full plan (once validated): Standard Shopping + a small Search campaign. Not Performance Max, not yet.

PMax is Google's default recommendation and it is the wrong first campaign for you. It needs conversion history to optimize, spends across YouTube/Display/Gmail where your cold audience doesn't convert, and gives you almost no visibility into what's working. With zero conversion data and a sub-$25 break-even CPA on singles, it will burn budget teaching itself. Revisit it once you have 30+ conversions.

### Campaign 1 — Standard Shopping
- **Budget:** $15/day to start
- **Bidding:** Manual CPC, max $1.00 to start (raise only if impression share is starved)
- **Targeting:** US and Canada (matches actual shipping policy — verify CJdropshipping Canada shipping cost/time before launch, since figures used elsewhere in this doc are from the US-specific shipping method)
- **Products:** All 4, but create a separate ad group for the bundles once they're listed
- Shopping campaigns target by *product feed*, not keywords — so the product titles matter enormously (see title formula below)

### Campaign 2 — Search (exact + phrase match only)
- **Budget:** $15/day
- **Bidding:** Manual CPC, max $1.50
- **No broad match at launch.** Broad match on a small budget is how you end up paying for "truck parts near me."

**Starting keyword list:**
```
[truck cab organizer]
[semi truck organizer]
[semi truck seat organizer]
[truck seat back organizer]
"trucker cab storage"
"semi truck storage organizer"
[truck cargo net ceiling]
[truck document holder]
"sleeper cab organizer"
```

**Negative keywords — add these on day one:**
```
free, cheap, used, second hand, wholesale, bulk,
repair, parts, wiring, engine, tires, diy, plans,
rental, hire, job, jobs, salary, insurance,
amazon, walmart, ebay, temu
```

---

## Phase 3 — Product titles for the feed

Shopping matches on your product title. Your current Shopify titles are still the raw CJ supplier names — fix these before syncing, or the feed matches on the wrong terms.

**Formula:** `[Brand] [Product Name] — [Key descriptor] for [Use case]`

| SKU | Recommended feed title |
|---|---|
| CS-01 | ConvoySupply CS-01 Cab Command Organizer — Seat Back Organizer with Fold-Down Tray for Truck Drivers |
| CS-02 | ConvoySupply CS-02 Bunk Shelf Net — Mesh Cargo Storage Net for Truck Cab and Sleeper |
| CS-03 | ConvoySupply CS-03 Manifest Folio — A4 Document Holder for Truck Drivers, Logs and Permits |
| CS-04 | ConvoySupply CS-04 Haul Bag — Large Leather Duffel Bag for Truck Drivers |

Keep titles under 150 characters. Front-load the words people actually search.

---

## Phase 4 — Launch and read

### Day 1–3: launch and do not touch it
Set budgets, launch both campaigns, then leave them alone for 72 hours. Editing bids daily on a new campaign prevents Google from gathering enough data to be useful.

### Day 4: first read
| Metric | Healthy | Read if not |
|---|---|---|
| Impressions | >500/day combined | Bids too low, or feed disapproved — check Merchant Center diagnostics |
| CTR (Shopping) | >0.8% | Images or price uncompetitive |
| CTR (Search) | >3% | Ad copy not matching intent |
| CPC | <$1.50 | Bidding too aggressively, or keywords too broad |
| Landing page views / clicks | >90% | Site speed problem |

### Day 7: first optimization
- Pause any keyword with 30+ clicks and zero add-to-carts
- Add search terms that converted as exact-match keywords
- Add junk search terms as negatives (check the Search Terms report — this is the single highest-value 20 minutes each week)
- If CPA is above break-even but add-to-carts are happening, the problem is checkout, not ads

### Day 14: the real decision point
| Situation | Action |
|---|---|
| CPA below break-even ($23 singles / $37 bundles) | Raise budget 20–30%. Do not double it. |
| CPA 1–2× break-even, but improving | Hold budget, keep optimizing. Push bundles harder. |
| CPA >2× break-even, flat | Something upstream is broken — page, price, or offer. Don't fix it with more spend. |
| Under 1,000 impressions total | Not a performance problem, a visibility problem. Check feed approval and bids. |
| Zero add-to-carts after 200+ clicks | The offer isn't landing. Fix the page before spending more. |

---

## Budget summary

| Item | Cost |
|---|---|
| Google & YouTube Shopify app | Free |
| Google Merchant Center | Free |
| Shopping campaign | $15/day |
| Search campaign | $15/day |
| **Total ad spend** | **$30/day (~$420 over 14 days)** |

Treat the first 14 days as a data purchase, not a profit attempt. The output you're buying is: which keywords convert, what your real CPC is, and whether the page converts at all. Those three answers are what make the Facebook and TikTok phases worth running.

---

## Hard gates before you spend anything

- [ ] All 4 product titles updated from supplier names to branded names
- [ ] Product descriptions pasted in from `store/product-descriptions-live.md`
- [ ] Compliant featured image set per `store/product-image-audit.md`
- [ ] Merchant Center account approved, all 4 products showing "Active"
- [ ] Return policy and shipping policy pages published and linked
- [ ] Test purchase completed and conversion recorded in Google Ads
- [ ] Negative keyword list applied
- [ ] Both bundles created as products (bundles are where the CPA headroom is)

**Do not launch with any box unchecked.** Every one of these is cheaper to fix now than after spend has started.
