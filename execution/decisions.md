# ConvoySupply — Decision Log

Every significant decision, why it was made, and what would reverse it. **Append only — never edit or delete a past entry.** If a decision changes, add a new one that supersedes it.

The point of the "what would reverse this" column is to stop decisions from calcifying. A decision with no reversal condition is a belief.

**Format**

```
## DEC-XXX — Title
Date · Status: ACTIVE | SUPERSEDED by DEC-YYY | REVERSED
Decision:  what we're doing
Rationale: why
Alternatives considered: what we didn't do, and why not
Reverses if: the specific evidence that would change this
```

---

## DEC-001 — Trademark clearance gates all brand spend
**2026-09-20 · ACTIVE · Owner: Founder**

**Decision:** No money is spent on logo, domain, packaging, or paid ads until a USPTO TESS search (classes 12, 18, 35), a state business-name search, and a domain/handle check are complete. Always write the brand as one word — **ConvoySupply**, never "Convoy Supply."

**Rationale:** Convoy Supply Ltd. is a real building-envelope and building-materials wholesale distributor, founded 1972, operating across Canada, the Pacific Northwest US, and Maryland **[V2]**. We are in a different category, which helps materially, but "different category" is an argument, not a guarantee.

**Alternatives considered:** Launch first and deal with it later — rejected; a cease-and-desist after brand and ad spend costs far more than a search now. Rename pre-emptively — rejected; the name is genuinely good for this niche and the categories are distinct.

**Reverses if:** Clearance comes back clear (proceed), or comes back contested (rename before any further spend).

---

## DEC-002 — Trades / jobsite niche is disqualified
**2026-09-20 · ACTIVE**

**Decision:** ConvoySupply will not enter construction, roofing, insulation, siding, or contractor supply under this name — ever, not just at launch.

**Rationale:** That is Convoy Supply Ltd.'s exact trade **[V2]**. It is the single worst category choice available to this brand name, and it scored second-highest on commercial merit, so the reasoning is recorded to stop it being revisited on commercial grounds.

**Reverses if:** Only on written legal advice, or a rename.

---

## DEC-003 — No dark patterns, anywhere
**2026-09-20 · ACTIVE**

**Decision:** No countdown timers, fake stock counters, "X people viewing," exit-intent discount popups, fabricated reviews, spin-to-win, or fake purchase notifications. No compare-at price unless the higher price was genuinely offered — at launch, bundles only.

**Rationale:** Two reasons. First, it is honest. Second, and pragmatically: this audience is unusually suspicious of marketing **[H]**, discusses sellers in Facebook Groups, and will publicly mock a fake countdown. Our only real asset at launch is being visibly honest in a category that visibly is not.

The theme code enforces this structurally — `cs-proof` cannot render a review that was not entered as a real one, `cs-offer` derives savings from Shopify's own compare-at price, and no urgency component exists to enable.

**Alternatives considered:** "Just a small timer" — rejected; the line has to be absolute or it erodes.

**Reverses if:** Never. If the business only works with dark patterns, it does not work.

---

## DEC-004 — CS-05 Dash Power Rail is gated out of launch
**2026-09-20 · ACTIVE**

**Decision:** The 12V/USB power rail does not launch. It is listed only if **all** of: UL or ETL certification for the exact SKU (not a similar model), documented and published fuse rating, product liability insurance in force, the first 30 days complete with the soft-goods hypothesis validated, and no installation instructions in the copy.

**Rationale:** It is the product drivers most want and the one most likely to hurt us. Electrical products in vehicles carry heat, short, and fire failure modes that soft goods do not. Return rates on cheap 12V electronics are structurally higher. Margin is the worst in the catalog at 64.4%, so it absorbs the most risk while contributing the least.

**Reverses if:** All five conditions are met. Otherwise the catalog is four products, which is fine — four coherent products beat five with a liability in the middle.

---

## DEC-005 — Retargeting is gated behind real traffic
**2026-09-20 · ACTIVE**

**Decision:** Campaign 2 does not launch until 1,000+ landing page views and 50+ add-to-carts in a 14-day window, and Campaign 1 has run 10+ days.

**Rationale:** Retargeting a few dozen people at premium CPMs teaches nothing and burns the days the cold test needs. It is the most common way a small test wastes its budget, and it feels productive while doing it.

**Reverses if:** All three conditions are met.

---

## DEC-006 — Small inventory buy, not dropship
**2026-09-20 · SUPERSEDED by DEC-013**

**Decision:** Hold 10–15 units each of CS-01 and CS-02 (~$300 **[A]**). CS-03 and CS-04 listed as made-to-order with an honest ship date until demand is proven.

**Rationale:** Shipping speed is already our weakest position against Amazon (`research/competitor-analysis.md`). Dropshipping makes the thing we are worst at even worse, and the offer is fragile there. $300 protects the two SKUs most likely to sell.

**Alternatives considered:** Full dropship — rejected, slow shipping undermines the whole offer. Large inventory buy — rejected, too much capital before evidence.

**Reverses if:** Landed cost or MOQ makes a small buy impossible, or a supplier offers genuinely fast blind dropshipping under 5 days.

**Superseded:** Speed to launch was prioritized over the shipping-speed disadvantage. See DEC-013.

---

## DEC-007 — Broad and interest targeting tested head to head
**2026-09-20 · ACTIVE**

**Decision:** Three cold ad sets — Broad, Interest stack, Advantage+ — with **identical creative**, under one CBO campaign.

**Rationale:** Whether broad beats interest targeting for a niche occupational audience is the biggest open question in `research/customer-avatar.md`. Holding creative constant is the only way to attribute the difference to the audience.

**Recorded prediction, written before the test:** broad will win, because our creative is unusually self-selecting — a photo of a sleeper cab interior is invisible to anyone who is not a driver. This is on record so it cannot be claimed retroactively either way.

**Known imprecision:** CBO means Meta will concentrate spend unevenly, so the audience comparison is not clean. At $30/day, per-ad-set budgets would leave each ad set unable to exit the learning phase, which is worse. Accepted trade — and it must be acknowledged when reading the results.

**Reverses if:** One approach wins decisively by Day 14 — consolidate onto it.

---

## DEC-008 — Dawn, not a paid theme
**2026-09-20 · ACTIVE**

**Decision:** Free Dawn theme plus nine custom sections. **Zero apps at launch.**

**Rationale:** A $180–$400 premium theme buys sections we do not need and page weight we cannot afford. Differentiation in this brand is photography and copy, not theme features. Apps are the single largest cause of Shopify page-speed loss, and mobile speed matters more here than almost anywhere — this audience browses on a phone in a parking lot, frequently on poor signal.

**Reverses if:** A specific, measured conversion problem requires functionality Dawn genuinely cannot provide. "It would be nice" is not that.

---

## DEC-009 — Landing page and PDP both exist for CS-01
**2026-09-20 · ACTIVE**

**Decision:** CS-01 has a standard PDP and a separate funnel landing page at `/pages/cs-01`. Paid traffic goes to the landing page initially.

**Rationale:** They do different jobs. The PDP serves visitors with context — collection, search, cart. The landing page serves a stranger who tapped an ad ten seconds ago. One page cannot do both well.

**Reverses if:** EXP-007 shows the PDP converts paid traffic better. Then retire the landing page and save the maintenance.

---

## DEC-010 — No promotional posting in Facebook Groups
**2026-09-20 · ACTIVE**

**Decision:** Participate helpfully in trucking Groups. Post no promotional content, share no links, for the first 30 days minimum.

**Rationale:** Trucking Groups are high-trust and hostile to advertising **[H]**. Getting banned from the three biggest groups in week one costs more than any post could earn, and the ban is usually permanent.

**Reverses if:** A group explicitly permits vendor posts and we have been a genuine participant for months.

---

## DEC-011 — Honest "no reviews" messaging instead of review software
**2026-09-20 · ACTIVE**

**Decision:** No review app at launch. Homepage and every PDP state plainly that we have no reviews yet and are not buying any. The structure is built so genuine reviews populate the same section later.

**Rationale:** Most review apps can import or generate unverified reviews, and having the capability installed is a standing temptation. The honest message also converts the weakness into evidence of honesty, which is the most credible thing on the page for an unknown brand.

**Reverses if:** Genuine verified reviews exist in volume — then install a review app that only accepts verified purchases.

---

## DEC-012 — Unit economics built as a script, not a spreadsheet
**2026-09-20 · ACTIVE**

**Decision:** `finance/unit_economics.py` generates every figure in `finance/unit-economics.md`. Both are version-controlled.

**Rationale:** Every cost input is currently a guess. When real quotes arrive, break-even CPA, target ROAS, and the go/no-go all need to recalculate — in one command, not by re-deriving the reasoning. A spreadsheet would drift out of sync with the document and neither would be reviewable in a diff.

**Reverses if:** Never, while the business is small enough for one file.

---

## DEC-013 — Dropship via DSers + AliExpress, not supplier-vetted inventory
**2026-09-20 · ACTIVE**

**Decision:** Launch on **DSers** (free Shopify app) sourcing generic equivalents of CS-01–CS-04 from **AliExpress**. No upfront inventory purchase, no multi-supplier RFQ cycle, no sample-evaluation gate before launch. One quality-control sample per SKU is ordered for the founder's own review, in parallel with store setup, not as a blocking gate.

**Rationale:** The Day 1–5 supplier RFQ process (`decisions.md` DEC-006, `execution/day-1-supplier-launch.md`) trades speed for supplier-quality certainty the business doesn't have evidence it needs yet. Nothing has sold. DSers is the official free Shopify-AliExpress integration — no monthly fee at this volume, no MOQ, products can be imported and listed same-day. This converts the biggest bottleneck in the 30-day plan (7–14 day supplier lead time before any store work could reasonably start) into same-day product listing.

**What this costs us:**
- **Landed cost per unit is higher** than a bulk-negotiated supplier quote would be — AliExpress dropship pricing has no MOQ discount built in. Contribution margin in `finance/unit-economics.md` will compress; re-run the model against real DSers per-unit prices before setting final retail prices.
- **Shipping time to customer is 12–25 days** on standard AliExpress shipping, materially slower than the "ships in 2–3 days" framing used elsewhere in this repo. PDP and checkout copy must state real ship times — this is a DEC-003 (no dark patterns) requirement, not optional.
- **No control over packaging** unless a specific AliExpress supplier explicitly offers no-branding / private packaging — check this per-supplier inside DSers before importing.
- **Product match quality is unverified** — DSers products are generic equivalents (car seat-back organizer, cargo net, document organizer, duffel), not the exact spec'd CS-01–CS-04 (1680D ballistic nylon, named truck-model fit, etc.). Marketing copy must not claim specs the actual sourced product doesn't have.

**Alternatives considered:** Continue the 5-supplier RFQ (DEC-006) — rejected for this decision, too slow for the founder's stated priority. Zendrop or Spocket — rejected as primary; both have effectively-required paid tiers ($27–$39/mo+) for the product variety needed, where DSers' free tier covers this catalog size. CJdropshipping — kept as a **fallback**, not primary: also free, and better suited if a specific SKU (especially CS-01, the hero) needs private-label branding or can't be found generic on AliExpress.

**Reverses if:** Real sales volume justifies moving CS-01 (and/or CS-02) to a vetted bulk supplier for better margin and faster shipping — this is the natural DEC-006 path once demand is proven, not before.

---

## DEC-014 — Channel sequencing: Google first, then scale to Facebook and TikTok
**2026-09-21 · ACTIVE**

**Decision:** Launch paid acquisition on **Google** (Search + Shopping) first. Once Google traffic validates the offer (real orders, acceptable CPA against `finance/unit-economics.md`), add **Facebook**, then **TikTok** as scale channels. This changes the channel order from the original plan, which opened on Meta only (DEC-007's three ad sets).

**Rationale:** Google Search/Shopping captures existing purchase intent — someone searching "truck cab organizer" is closer to buying than someone scrolled past a Facebook ad. Starting there validates the offer against warmer traffic before spending on cold-audience Meta/TikTok testing. Facebook and TikTok remain the scale channels once Google proves the funnel converts, per the original DEC-005 gate (retargeting/scale waits on real traffic evidence).

**What does not change:** DEC-007's three-ad-set testing structure (Broad / Interest / Advantage+) still applies **once Meta launches** — it just launches second, not first. DEC-005 (retargeting gated behind 1,000+ LPVs and 50+ ATCs) still applies within each platform.

**Action needed:** Set up Google Ads account and Merchant Center (for Shopping) in parallel with the remaining product sourcing. Google Shopping specifically needs a working, published product feed — so this cannot start until the DSers/CJdropshipping product listings (CS-01–CS-04) are live and priced on Shopify.

**Reverses if:** Google CPA/CPC data suggests search intent doesn't exist for this product category (unlikely for branded organizer terms, more of a risk for generic terms) — then move Meta up in sequence.

---

## OPEN-08 — Atlas AI website tool: Shopify-compatible or replacement?
**Flagged 2026-09-21 · RESOLVED 2026-09-22**

**Resolution:** A theme export from the live store (`nax2hx-gr.myshopify.com`) confirms the store runs on **genuine Shopify**, using the **"Tinker" theme** (v4.2.0, an Online Store 2.0 theme with sections for hero, featured-product, product-list, collection-list, product-information, and product-recommendations). Whatever "Atlas AI" refers to, the underlying store is Shopify — so all CJdropshipping/DSers product sync work and the custom Liquid sections built in `theme/sections/` remain fully applicable.

**Note:** Tinker is a different theme than the Dawn theme assumed in DEC-008. Dawn-specific instructions in `theme/README.md` (install steps, section-group names for suppressing nav) will need adjusting for Tinker's actual section/group structure before the custom `cs-*` sections are added — the sections themselves are portable Liquid, but the install steps referencing Dawn's file layout are not guaranteed to match Tinker's.

**Original question:** Does Atlas AI build on top of the existing Shopify store or does it replace Shopify as the storefront platform?

---

## DEC-015 — CS-04 launched below the 45% margin floor
**2026-09-21 · ACTIVE**

**Decision:** CS-04 (Haul Bag) is listed at **$49.00** against a real CJdropshipping landed cost of **$32.81** ($10.28 product + $22.53 shipping), producing a contribution margin of **~37.0%** — below the 45% floor set in `research/selected-niche.md` failure condition 5.

**Rationale:** Founder chose to accept the thinner margin rather than keep searching for a cheaper/lighter duffel or raise the price further, prioritizing getting the full 4-SKU catalog live today. All four SKUs sourced via CJdropshipping in a single session: CS-01 ($50, 46.2%), CS-02 ($29.99, 69.8%), CS-03 ($27.99, 80.4%), CS-04 ($49, 37.0%).

**What this means in practice:** CS-04 makes real but thin money per order (~$18 contribution) and cannot absorb a high CPA — do not spend meaningfully on ads targeting CS-04 as a standalone item. It still works as a **bundle component** (Full Rig Kit) where CS-01/02/03's stronger margins carry the blended average.

**Reverses if:** A cheaper/lighter duffel listing is found later (weight is the driver of the $22.53 shipping cost), or CS-04 is dropped from standalone ad campaigns in favor of bundle-only distribution.

---

## Open decisions

| # | Question | Needs | When |
|---|---|---|---|
| ~~OPEN-01~~ | ~~Which supplier?~~ | **Resolved by DEC-013** — DSers/AliExpress, no single supplier selection needed | — |
| ~~OPEN-02~~ | ~~Who pays return shipping?~~ | **Resolved 2026-09-22** — no mail-in return for most cases. Damaged/defective/wrong items: refund or replace without requiring return shipping (CJdropshipping return shipping to China would exceed item value). Unwanted-but-correct items: case-by-case partial refund/credit within 14 days. See `store/policies/returns-policy.md`. | — |
| OPEN-03 | Business entity — sole proprietor or LLC? | Liability view, especially if CS-05 ever launches | Before first sale |
| ~~OPEN-04~~ | ~~Fulfillment — self-ship or 3PL?~~ | **Resolved by DEC-013** — dropship, supplier ships direct to customer | — |
| OPEN-05 | Marketplace price parity with the site? | Test data | After 2 weeks live |
| OPEN-06 | Annual or monthly Shopify billing? | Confidence in continuing past month 1 | Day 30 |
| OPEN-07 | Which AliExpress supplier per SKU inside DSers? | Compare 3-5 listings per product on: rating, order count, ship-from location (US warehouse if available), no-branding option | Day 1-2 |

**Reference tags [V2], [H] are defined in `research/niche-analysis.md` and `research/customer-avatar.md`.**
