# ConvoySupply — Product Page Specification

**Date:** 2026-09-20
**Applies to:** all products. CS-01 also has a separate funnel landing page — see `store/landing-page.md`.

---

## Mandatory PDP structure

Every product page contains these, in this order. No exceptions, no "we'll add it later."

| # | Block | Required |
|---|---|---|
| 1 | Product title (SKU + name) | Yes |
| 2 | One-sentence value proposition | Yes |
| 3 | Image gallery — min. 6 | Yes |
| 4 | Price | Yes |
| 5 | Compare-at price | **Only if genuinely offered** — bundles only at launch |
| 6 | Add to cart + express checkout | Yes |
| 7 | Trust strip | Yes |
| 8 | Benefits (4–6) | Yes |
| 9 | Specs table | Yes |
| 10 | What's included | Yes |
| 11 | Fit block | Yes |
| 12 | Shipping block | Yes |
| 13 | Returns block | Yes |
| 14 | Honest review placeholder | Yes |
| 15 | FAQ (min. 5) | Yes |
| 16 | Bundle / upsell | Yes |
| 17 | Related products | Yes |
| 18 | Final CTA | Yes |

### Banned on every PDP
Countdown timers · fake stock counters · "X people are viewing" · fabricated reviews or star ratings · inflated compare-at pricing · exit-intent discount popups · unfunded guarantees · any safety, medical, or compliance claim

---

## Gallery standard — 6 images minimum

| # | Shot | Purpose |
|---|---|---|
| 1 | **In situ, in a real cab, loaded** | Hero. Context beats isolation. |
| 2 | Product alone, plain background, full view | The clean reference shot |
| 3 | Detail — stitching, webbing, hardware | Proves build quality without adjectives |
| 4 | Scale — human hand or a known object | Answers "how big is it, really" |
| 5 | **Dimension diagram with numbers on it** | Kills the fit objection inside the gallery |
| 6 | In use — a hand reaching, gear going in | Shows the behaviour, not the object |

**Image rules:** all product images are photographs of the real product. No AI product renders. See `brand/brand-strategy.md`. WebP, under 200 KB each, explicit dimensions, descriptive alt text.

---

## Trust strip

Sits immediately under Add to Cart, one line, icons + text:

> ✓ Free US shipping over $75 · ✓ 30-day returns · ✓ No installation · ✓ Ships to a terminal

---

## Honest review placeholder — every PDP

> **No reviews yet.**
>
> We launched this month. We're not putting fake ones here and we're not buying any. Be the first — good or bad, we want to hear it.

Same structural rule as the homepage: a `blocks` array of type `review`, empty at launch, message auto-hides when real reviews exist. **No review app capable of importing unverified reviews is installed.**

---

# CS-01 — Cab Command Organizer

**URL:** `/products/cs-01-cab-command-organizer` · **$54.99** · no compare-at

**Value prop:** A seat-back command center that gets every daily-use item off your passenger seat and within arm's reach.

**Description:** Use the long-form CS-01 copy from `brand/brand-copy.md`.

**Benefits**
- **Nothing lives on the passenger seat anymore** — deep pockets with defined positions for bulk items, elastic sleeves for cables and tools
- **Reaches from the driver's seat** — positioned so you're not twisting or unbuckling
- **Loaded pockets don't sag** — box-stitched at every load point
- **Two minutes to fit, nothing modified** — cam-buckle straps, no tools, comes off as fast as it goes on
- **Sized for a Class 8 seat back** — not a car organizer with truck keywords
- **Folds flat** — comes with you to the next truck

**Specs [TBC — placeholders until supplier spec sheets arrive]**

| Spec | Value |
|---|---|
| Deployed | 22" H × 15" W × 4" D |
| Folded | 15" × 4" × 2" |
| Weight | ~1.6 lb |
| Shell | 1680D ballistic nylon |
| Lining | 210D ripstop |
| Webbing | 1.5" polypropylene, cam-buckle |
| Stitching | Box-stitched, all load points |
| Pockets | 2 deep · 3 elastic · 1 padded tablet · 1 document |
| Color | Asphalt black / hi-viz amber trim |
| Install | None |

**What's included:** 1 × CS-01 · 2 × adjustable seat-back straps · 1 × anchor strap · fit card

**Fit block**
> **Confirmed on:** Freightliner Cascadia · Peterbilt 579 · Kenworth T680 · Volvo VNL · International LT
>
> Needs a passenger seat back at least 20" tall and 14" wide, with clearance behind the headrest for the anchor strap.
>
> Running something else? Measure your seat back against the dimensions above. If it doesn't work, send it back within 30 days. Full guide: **What Fits My Truck →**

**FAQ**
1. *Will it fit my seat?* → See fit block; measure; 30-day returns.
2. *How much weight will it hold?* → `[TBC — do not publish a load figure until tested. If untested, say: "We haven't published a rated load because we haven't tested one properly. Load points are box-stitched. We'll publish a number when we've measured it."]`
3. *Does it block the passenger seat?* → It hangs on the back. The seat stays usable.
4. *Will my carrier allow it?* → Nothing drills or bolts. Nothing is modified.
5. *Can I wash it?* → Wipe with a damp cloth and mild soap. Don't machine wash — it'll distort the panel.
6. *Does it work in a day cab?* → Yes, if the seat back meets the minimum dimensions.

**Upsell:** *"Add the CS-02 and CS-03 for $34.01 more and get the Cab Reset Kit — save $23.97."*
**Related:** CS-02, CS-03, Cab Reset Kit

---

# CS-02 — Bunk Shelf Net

**URL:** `/products/cs-02-bunk-shelf-net` · **$29.99**

**Value prop:** Turns unused bunk-wall space into a shelf, so gear stops living on your mattress.

**Benefits**
- **Storage where there was none** — vertical wall space is the most wasted area in the cab
- **You can see what's in it** — stretch mesh, no digging
- **Fits different bunk geometries** — 36" to 52" adjustable
- **Five minutes, no tools** — straps to existing anchor points
- **Cheapest change with the biggest immediate difference**

**Specs [TBC]:** 36"–52" adjustable × 14" deep · ~0.7 lb · knotless nylon mesh · 1" webbing, cam buckles · four anchor straps · approx. 15 lb soft goods · install: none

**What's included:** 1 × net · 4 × anchor straps · 2 × extension straps

**Fit block**
> Needs two anchor points 36"–52" apart. Most sleepers have usable points at the curtain track, grab handle, or existing tie-downs. Measure before ordering.

**FAQ**
1. *What if I don't have anchor points?* → Extension straps reach most grab handles and curtain tracks. If yours has nothing usable, it won't work — send it back.
2. *How much will it hold?* → Rated `[TBC]` for soft goods. Not for tools or anything with a hard edge.
3. *Will it sag?* → Some stretch under load is by design. Tension the straps to adjust.
4. *Will it damage the interior?* → Nothing adhesive, nothing drilled. Straps only.
5. *Can I use two?* → Yes — stacking is common if your wall height allows.

**Upsell:** Cab Reset Kit · **Related:** CS-01, CS-04

---

# CS-03 — Manifest Folio

**URL:** `/products/cs-03-manifest-folio` · **$27.99**

**Value prop:** One place for logs, BOLs, permits, and receipts, so you can put your hand on any of it in seconds.

**Benefits**
- **Everything in one place, labeled** — six sleeves for the documents you actually carry
- **A spilled coffee is an annoyance, not a problem** — TPU-lined interior
- **Flat enough to live in a door pocket** or in the CS-01's document slot
- **Pen loop, so there's always a pen**
- **Elastic closure** — nothing falls out when it goes in a bag

**Compliance note — binding:** copy describes **organization only.** No claim, implication, or suggestion about inspections, compliance, audits, or legal adequacy. Do not edit this note out.

**Specs [TBC]:** 13" × 10" × 1.5" closed · ~0.6 lb · 600D poly shell · TPU-lined interior · 6 labeled sleeves · 1 zip pocket · pen loop · elastic closure

**What's included:** 1 × folio · 6 × blank sleeve labels

**FAQ**
1. *Does it fit standard log sheets and BOLs?* → Sized for standard US letter and common BOL formats.
2. *Is it waterproof?* → Water-*resistant*. It handles a spill. It won't survive submersion.
3. *Will it fit in the CS-01?* → Yes, that's what the document pocket is sized for.
4. *Can I relabel the sleeves?* → Yes, blanks included.
5. *Does this help with inspections?* → It organizes your paperwork. That's all we'll claim.

**Upsell:** Cab Reset Kit · **Related:** CS-01, Cab Reset Kit

---

# CS-04 — Haul Bag

**URL:** `/products/cs-04-haul-bag` · **$49.99**

**Value prop:** A clamshell duffel sized to a truck storage bay, so you can see everything without unpacking anything.

**Benefits**
- **Opens flat** — full-perimeter zip, whole contents visible at once
- **Sized to a bay, not to an airline** — an odd shape on purpose, and the reason it fits
- **Laundry stays separate** — zipped end pocket
- **Compression straps** keep everything put on rough road
- **Water-resistant base** for a wet bay floor

**Honest note in the description:** *"A duffel is a duffel. The difference here is the dimensions and the clamshell opening — if you already have a bag that fits your bay and opens flat, you don't need this one."*

*Rationale: CS-04 is the weakest differentiation story in the catalog. Saying so costs a small number of sales and buys credibility that applies to the whole range. Keep it.*

**Specs [TBC]:** 28" L × 13" W × 12" H · ~65L · ~2.2 lb · 900D poly shell · water-resistant TPU base · #8 zips · internal compression straps · zipped end pocket · padded handles + removable shoulder strap

**FAQ**
1. *Will it fit my bay?* → Dimensions above — measure your bay. 30-day returns.
2. *Is it waterproof?* → Water-resistant base and shell. Not waterproof.
3. *Can I check it on a flight?* → It's over standard carry-on. Fine as checked.
4. *Does it stand up on its own?* → Semi-rigid base, yes, when partly loaded.
5. *How much does it hold?* → Around 65L. Roughly two to three weeks of clothes.

**Upsell:** Full Rig Kit · **Related:** CS-02, Full Rig Kit

---

# Bundles

## Cab Reset Kit — `/products/cab-reset-kit`
**$89.00** · compare-at **$112.97** *(the genuine sum of individual prices, all really charged)* · **Save $23.97 (21%)**

> The three pieces that change the most: your passenger seat, your bunk wall, and your paperwork.
>
> CS-01 Cab Command Organizer — $54.99
> CS-02 Bunk Shelf Net — $29.99
> CS-03 Manifest Folio — $27.99
> **Together: $89.00. Save $23.97.**

Page includes each product's specs in collapsible blocks, plus the combined fit requirements.

## Full Rig Kit — `/products/full-rig-kit`
**$129.00** · compare-at **$162.96** · **Save $33.96 (21%)**

> Everything we make. Front of cab, bunk wall, paperwork, bulk storage.

**Compare-at integrity:** each component is genuinely sold at the stated individual price on its own PDP. No price is inflated to manufacture a discount. This is the only place compare-at pricing appears anywhere on the store.

---

## Inventory and stock messaging

- Real stock levels only. No "only 3 left" unless Shopify's inventory says so.
- Out of stock → *"Out of stock. Email us and we'll tell you when it's back."* No back-in-stock guessing on dates.
- Pre-order **only** if we can state a real ship date.

## SEO

| Page | Title | Meta |
|---|---|---|
| CS-01 | CS-01 Cab Command Organizer — Semi Truck Seat Back Organizer \| ConvoySupply | Seat-back organizer sized for Class 8 sleeper cabs. No drilling. Full dimensions published. Fits Cascadia, 579, T680, VNL, LT. $54.99. |
| CS-02 | CS-02 Bunk Shelf Net — Semi Truck Bunk Storage \| ConvoySupply | Adjustable cargo net shelf for sleeper bunk walls. 36"–52", no tools, no drilling. $29.99. |
| CS-03 | CS-03 Manifest Folio — Truck Driver Document Organizer \| ConvoySupply | Organizer for logs, BOLs, permits and receipts. Water-resistant lining, six labeled sleeves. $27.99. |
| CS-04 | CS-04 Haul Bag — Under-Bunk Truck Duffel \| ConvoySupply | Clamshell duffel sized for a truck storage bay. 65L, opens flat. $49.99. |

## Pre-publish checklist per PDP

- [ ] All 18 required blocks present
- [ ] 6+ real photographs of the real product
- [ ] Every `[TBC]` replaced with a supplier-confirmed value — **no spec published that a spec sheet doesn't support**
- [ ] Fit block names real models and real minimum dimensions
- [ ] No compare-at price unless genuinely offered
- [ ] Honest review placeholder present, no review app installed
- [ ] No timers, counters, or fake scarcity
- [ ] CS-03 carries no compliance claim
- [ ] Mobile QA on a real phone
