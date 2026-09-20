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
**2026-09-20 · ACTIVE**

**Decision:** Hold 10–15 units each of CS-01 and CS-02 (~$300 **[A]**). CS-03 and CS-04 listed as made-to-order with an honest ship date until demand is proven.

**Rationale:** Shipping speed is already our weakest position against Amazon (`research/competitor-analysis.md`). Dropshipping makes the thing we are worst at even worse, and the offer is fragile there. $300 protects the two SKUs most likely to sell.

**Alternatives considered:** Full dropship — rejected, slow shipping undermines the whole offer. Large inventory buy — rejected, too much capital before evidence.

**Reverses if:** Landed cost or MOQ makes a small buy impossible, or a supplier offers genuinely fast blind dropshipping under 5 days.

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

## Open decisions

| # | Question | Needs | When |
|---|---|---|---|
| OPEN-01 | Which supplier? | Three quotes per SKU | Day 5 |
| OPEN-02 | Who pays return shipping? | Margin model + return-rate estimate | Before publishing the returns policy |
| OPEN-03 | Business entity — sole proprietor or LLC? | Liability view, especially if CS-05 ever launches | Before first sale |
| OPEN-04 | Fulfillment — self-ship or 3PL? | Volume estimate | Day 5 |
| OPEN-05 | Marketplace price parity with the site? | Test data | After 2 weeks live |
| OPEN-06 | Annual or monthly Shopify billing? | Confidence in continuing past month 1 | Day 30 |

**Reference tags [V2], [H] are defined in `research/niche-analysis.md` and `research/customer-avatar.md`.**
