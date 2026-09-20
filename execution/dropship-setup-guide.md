# Dropship Setup — DSers + AliExpress

**Supersedes:** `execution/day-1-supplier-launch.md` (RFQ-based supplier sourcing, DEC-006)
**Per:** DEC-013

---

## Why DSers

DSers is Shopify's official free AliExpress dropshipping integration.

| Feature | DSers Free Plan |
|---|---|
| Monthly cost | **$0** (paid tiers start at $19.90/mo for advanced automation — not needed at launch) |
| Order volume | Up to 3,000 orders/month on free tier |
| Products | Unlimited import |
| Bulk order placement | Yes — place multiple supplier orders in one checkout |
| Auto order-status sync | Yes — tracking numbers push to Shopify automatically |
| MOQ | **None.** Buy 1 unit at a time. |
| Setup time | Store connected and first product imported in under 30 minutes |

**Backup option:** CJdropshipping (also free) — better if a specific SKU needs private branding/packaging or isn't available generic on AliExpress. Use it per-SKU, not as a full replacement.

---

## Setup Steps (Day 1)

### 1. Install DSers (15 min)
- Shopify Admin → Apps → search "DSers-AliExpress Dropshipping"
- Install, connect to your Shopify store
- Link your AliExpress account (create one free if needed)

### 2. Find products for each SKU (1-2 hrs)

You're sourcing **generic equivalents**, not exact custom specs. Search AliExpress directly (not just DSers) using these terms, then import winners via the DSers browser extension:

| Your SKU | AliExpress Search Terms | What to look for |
|---|---|---|
| **CS-01** Cab Command Organizer | "car seat back organizer," "truck seat organizer," "multi-pocket car organizer" | Nylon/oxford fabric, multiple pockets, strap-mount, 4.5+ stars, 1000+ orders |
| **CS-02** Bunk Shelf Net | "car ceiling cargo net," "truck storage net," "mesh cargo net car" | Mesh construction, adjustable straps, load-rated if listed |
| **CS-03** Manifest Folio | "document organizer bag," "car file folder holder," "PU leather document bag" | Zippered closure, multiple compartments, water-resistant material |
| **CS-04** Haul Bag | "duffel bag large," "travel duffel canvas," "sports duffel bag" | Size in the 25-30L range, reinforced handles, clamshell opening if possible |

**Evaluation checklist per listing:**
- [ ] 4.5+ star rating with 500+ orders (proof of real fulfillment history)
- [ ] Ships from a location with reasonable delivery time (US/EU warehouse >> China warehouse)
- [ ] Check "shipping" tab for delivery estimate — reject anything over 25 days
- [ ] Check if the supplier offers "no branding" / neutral packaging (message them directly to confirm)
- [ ] Multiple photos from different angles, not just one stock photo
- [ ] Price allows for your target margin (see Economics section below)

### 3. Import to Shopify via DSers (30 min)
- Use the DSers Chrome extension while browsing AliExpress — click "Import to DSers" on each product
- In DSers dashboard → Import List → edit title, description, images, price for each product
- **Rewrite every title and description in your own words** — never publish AliExpress's stock text verbatim (thin, often broken English, and it's a giveaway to savvy shoppers)
- Push to Shopify as draft first, review on-site, then publish

### 4. Order 1 QC sample per SKU (same day, non-blocking)
- Order 1 unit of each product to your own address at full retail+shipping cost you'll pay
- This is **not a launch gate** — list and start selling while it's in transit
- When it arrives (7-20 days), check it against your product description. Pull the listing immediately if it doesn't match what you're advertising.

### 5. Set fulfillment settings in DSers
- Turn on **auto order sync** so paid Shopify orders push to AliExpress checkout automatically
- Turn on **tracking number sync** so customers get real tracking emails
- Set your **default supplier per product** (in case a listing has multiple seller options)

---

## What Changes in Your Store Copy

Per DEC-003 (no dark patterns) and DEC-013, these must be updated before launch:

| Old assumption | New reality | Where to fix |
|---|---|---|
| "Ships in 2-3 days" | **12-25 day delivery**, depending on supplier location | Shipping policy page, PDP shipping notice, checkout |
| Exact CS-01 spec (1680D ballistic nylon, named truck fit) | Generic organizer — **verify actual material/fit before claiming it** | `store/product-pages.md` — rewrite claims to match the real sourced product |
| Free returns | **Refund-only likely** — most AliExpress suppliers don't accept physical returns | Returns policy (OPEN-02) |
| "In stock, ships from our warehouse" | Never claim this — it's not true under dropshipping | All copy, everywhere |

**Be upfront about shipping time on the PDP.** A clearly stated "Arrives in 2-3 weeks" beats a customer finding out at day 10 with no explanation — that's a chargeback and a bad review, and it violates DEC-003 in spirit even if not letter.

---

## Updated Economics (rough — replace with real DSers prices)

Dropship unit costs run **higher** than a bulk-negotiated supplier quote because there's no volume discount. Expect landed cost per unit to sit **20-40% above** the DEC-006-era `[A]` estimates in `finance/unit-economics.md`.

| SKU | Old est. landed (bulk, DEC-006) | Dropship est. landed (DSers, no MOQ) |
|---|---|---|
| CS-01 | $15.50 | **~$19-22** |
| CS-02 | $6.80 | **~$9-12** |
| CS-03 | $6.50 | **~$8-10** |
| CS-04 | $14.00 | **~$18-24** |

**Action required:** Once you've picked actual AliExpress listings, plug the real per-unit price + shipping into `finance/unit_economics.py` and re-run it. CS-01 is close to the **$22 red line** under this model — if the listing you pick prices above that, either find a cheaper listing, raise the retail price, or accept a thinner margin for the speed tradeoff.

---

## Timeline Comparison

| | Old plan (RFQ + bulk buy) | New plan (DSers dropship) |
|---|---|---|
| Day 1 | Contact 5 suppliers | Store connected, products imported, listed live |
| Day 5 | Suppliers respond, margin gate check | Already selling; margin check done same-day against real DSers prices |
| Day 10 | Samples arrive | QC samples arrive (non-blocking, store already live) |
| Day 12 | Product shoot | Can shoot with QC sample once it arrives, or launch with supplier stock photos (edited/rewritten) meanwhile |
| Inventory cash outlay | ~$300 upfront | **$0 upfront** — pay-per-order only |

**Net effect: store can be live and taking orders same day instead of waiting on a 10-21 day supplier sample cycle.**

---

## Risks to Watch

1. **Slow shipping is a real conversion killer.** Set expectations clearly, and expect a higher return/complaint rate than a fast-shipping competitor. This is the direct tradeoff for speed — track it in `execution/metrics.md`.
2. **Supplier stock-outs.** AliExpress suppliers can run out without notice. Check stock in DSers before each order batch; have a backup listing saved per SKU.
3. **Quality drift.** The product that arrives for QC may not match future batches. Spot-check periodically, not just once.
4. **Thin margins compress your ad budget room.** Re-run unit economics before spending on ads — a break-even CPA that was $32 under DEC-006 could be $22-25 under dropship pricing.
