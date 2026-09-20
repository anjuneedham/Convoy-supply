# ConvoySupply — Homepage Copy

**Date:** 2026-09-20
**Status:** Ready to paste into Shopify
**Convention:** `[IMAGE: ...]` marks an image slot — prompts in `prompts/image-generation-prompts.md`. `[TBC]` marks a value that must be confirmed before publishing.

---

## 1. Announcement bar

> Free US shipping over $75 · 30-day returns · Shipping to a terminal? We can do that.

---

## 2. Header

Logo: **CONVOYSUPPLY** (Barlow Condensed 700, uppercase, letter-spaced)
Nav: Shop ▾ · Kits · What Fits My Truck · About · 🛒

---

## 3. Hero

`[IMAGE: HERO-01 — interior of a Class 8 sleeper cab at dawn, shot from the driver's seat. Passenger seat organized with the CS-01 fitted. Natural light through the windshield. Real wear on the steering wheel and dash. Documentary, not advertising.]`

**Eyebrow:** PURPOSE-BUILT CAB STORAGE

**H1:**
> ## YOUR PASSENGER SEAT IS NOT A SHELF.

**Sub:**
> A sleeper cab is a living space that ships with no storage. We make gear sized for the actual cab — no drilling, no tools, nothing modified.

**Primary CTA:** `Get the CS-01 — $54.99` → `/pages/cs-01`
**Secondary CTA:** `See all four pieces` → `/collections/all`

**Under-CTA microcopy:** Free US shipping over $75 · 30-day returns

*Note: the H1 is the problem, not the product. A visitor who has never heard of us needs to recognize themselves before they will read a product name.*

---

## 4. The problem

**H2:**
> ## EVERYTHING YOU OWN LIVES IN 60 SQUARE FEET. NONE OF IT HAS A HOME.

**Body:**
> Your truck was engineered to move freight. Nobody engineered it for the person living in it.
>
> There's a bunk, a dash, and a couple of shallow cubbies. That's the storage. Everything else — clothes, food, tools, paperwork, chargers, a coat, three weeks of laundry — ends up on the passenger seat, on the bunk, or on the floor.
>
> Then you brake hard and half of it's in the footwell.

**Three problem cards:**

| `[IMAGE: PROB-01]` | `[IMAGE: PROB-02]` | `[IMAGE: PROB-03]` |
|---|---|---|
| **The passenger seat pile** | **Storing things on your bed** | **Paperwork in a door pocket** |
| Phone, water, gloves, clipboard, whatever you ate at 2am. It slides when you brake and it's buried by Thursday. | The wall next to your bunk is empty. Your mattress is where the bag goes. That's backwards. | Logs, BOLs, permits, receipts. Creased, damp, and never where you left them. |

---

## 5. Featured product — CS-01

`[IMAGE: PROD-01 — CS-01 fitted to a real passenger seat back, loaded with real gear, shot from the driver's position]`

**Eyebrow:** THE ONE THAT CHANGES THE MOST

**H2:**
> ## CS-01 CAB COMMAND ORGANIZER

> Straps to the passenger seat back and gives every daily-use item a defined home. Deep pockets for bulk, elastic sleeves for cables and tools, a padded tablet slot, and a flat document pocket that fits a clipboard without folding it.
>
> Two minutes to fit. Nothing gets modified.

- Sized for a Class 8 seat back, not a car seat
- Box-stitched at every load point so loaded pockets don't sag
- Reaches from the driver's seat — no twisting, no unbuckling
- Folds flat when you switch trucks

**Price:** $54.99
**CTA:** `See the full spec →` `/pages/cs-01`

---

## 6. Benefits

**H2:**
> ## WHAT ACTUALLY CHANGES

| | | | |
|---|---|---|---|
| `[IMAGE: BEN-01]` | `[IMAGE: BEN-02]` | `[IMAGE: BEN-03]` | `[IMAGE: BEN-04]` |
| **Nothing moves under braking** | **You stop hunting** | **Nothing gets modified** | **Sized for your cab** |
| Loose gear gets secured. Elastic retention on the sleeves, deep pockets with defined positions. | Everything has one place. You stop losing twenty minutes a week to the same three items. | Straps, hangs, sits. No drilling, no bolts, no tools. Comes with you to the next truck. | Designed against real Class 8 dimensions. Every measurement published — check before you buy. |

---

## 7. Collection grid

**H2:**
> ## FOUR PIECES. ONE SORTED CAB.

**Sub:** Each one solves a different zone. Together they're the whole cab.

| Product | Zone | Price |
|---|---|---|
| **CS-01 Cab Command Organizer** | Passenger seat back | $54.99 |
| **CS-02 Bunk Shelf Net** | Bunk wall | $29.99 |
| **CS-03 Manifest Folio** | Paperwork | $27.99 |
| **CS-04 Haul Bag** | Under-bunk bay | $49.99 |

**CTA:** `Shop all →`

---

## 8. Why ConvoySupply

**H2:**
> ## BUILT FOR THE CAB, NOT THE CATALOG

> Most gear sold for trucks is a car product with truck keywords in the listing title. The straps don't reach. The pockets sag. It was designed for the back of a minivan seat.
>
> We started from the cab. Real dimensions, real seat backs, real bunk geometry. Everything we make is sized for the space it goes in, and every measurement is published so you can check it against your truck before you spend anything.

**Comparison table:**

| | Generic marketplace organizers | Specialty truck retail | **ConvoySupply** |
|---|---|---|---|
| Designed for | Cars, sold for trucks | Trucks | **Class 8 sleepers specifically** |
| Dimensions published | Rarely | Sometimes | **Always** |
| Installation | Varies | Often required | **None. Ever.** |
| Sold as a system | No | No | **Yes — four zones** |
| Typical price | $15–$40 | ~$75.99 **[V4]** | **$27.99–$54.99** |
| Reviews | Volume, often manipulated | Some | **None yet — we're new and we say so** |

*The last row is deliberate. Publishing our own weakness in a comparison table is the most credible thing on the page.*

---

## 9. Social proof — honest placeholder

**H2:**
> ## NO REVIEWS YET.

> We launched this month.
>
> We're not going to put fake reviews here, and we're not going to buy any. When we have real ones from real drivers, they'll go here — good and bad.
>
> If you're one of the first people to try this, tell us what's wrong with it. We'd rather fix the product than pad the page.
>
> **— [FOUNDER FIRST NAME], ConvoySupply**

`[IMAGE: TRUST-01 — the four products laid out on a truck bunk, overhead, natural light. Real, not a studio flat-lay.]`

**Implementation note:** build this as a section with a `blocks` array of type `review`. At launch the array is empty and the honest message renders. When real reviews exist, they populate the same section and the message auto-hides. **Do not swap in a review app that can generate or import unverified reviews.**

---

## 10. How it works

**H2:**
> ## HOW THIS WORKS

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| **Check the fit** | **Order** | **Tell us where you'll be** | **30 days to decide** |
| Every dimension is on the product page, plus a fit guide by truck model. Measure if you're running something unusual. | Free US shipping over $75. Ships in `[TBC]` business days, `[TBC]` days in transit. | Home address for when you're back, a terminal, or hold-for-pickup. Not sure? Email before you order. | If it doesn't fit or doesn't work, send it back within 30 days. Unused and in the packaging. |

**Bold callout:**
> **You're probably not home. We know.**
> Most of our customers are 1,500 miles from their mailbox when the package lands. Tell us where you'll actually be and we'll work with it.

---

## 11. Kits

**H2:**
> ## BUY THE SET, SAVE THE DIFFERENCE

**Sub:** Real savings against the real individual prices. Nothing is marked up first.

### The Cab Reset Kit — $89.00
CS-01 + CS-02 + CS-03 · Individually $112.97 · **Save $23.97**
> The three that change the most: your passenger seat, your bunk wall, and your paperwork.

### The Full Rig Kit — $129.00
All four · Individually $162.96 · **Save $33.96**
> Front of cab, bunk, paperwork, bulk storage. The whole system.

**CTA:** `Compare the kits →`

---

## 12. FAQ

**H2:** COMMON QUESTIONS

**Will it fit my truck?**
Confirmed on Freightliner Cascadia, Peterbilt 579, Kenworth T680, Volvo VNL and International LT. Every dimension is published on each product page and there's a fit guide by model. Running something else? Measure your seat back. If it doesn't work, 30-day returns.

**Can I get this cheaper on Amazon?**
Probably, and it'll get there faster. What you'll get is a car organizer with truck keywords in the title. Ours is sized for a Class 8 sleeper and the dimensions are published so you can check. If two-day shipping matters more than fit, buy the Amazon one — we'd rather you were happy than out $55.

**Do I have to install anything?**
No. Everything straps, hangs or sits. No drilling, no bolts, no tools. Nothing on your truck gets modified, which also means nothing to clear with your carrier.

**I'm never home to sign for a package.**
Ship to your home address for whenever you get back, to a terminal, or to a hold-for-pickup location. If your route makes that complicated, email us before you order.

**How long does shipping take?**
`[TBC]` business days to ship, then `[TBC]` days in transit via `[TBC]`. Free over $75, `$[TBC]` flat rate under. We'll give you a real number, not "fast shipping."

**What if I don't like it?**
Send it back within 30 days, unused and in the packaging, and we'll refund it. Return shipping is `[TBC — confirm who pays before publishing]`.

**CTA:** `All questions →` `/pages/faq`

---

## 13. Guarantee / returns

**H2:** 30 DAYS. NO ARGUMENT.

> If it doesn't fit your truck, or it isn't what you expected, send it back within 30 days of delivery. Unused, in the original packaging, and we'll refund the product price.
>
> That's the whole policy. We're not going to promise a lifetime warranty we can't fund, and we're not going to make you argue with a chatbot.
>
> `[TBC: return shipping terms]`

---

## 14. Final CTA

`[IMAGE: CTA-01 — wide interior shot of a fully-organized sleeper, low evening light, all four products in place]`

**H2:**
> ## SQUARED AWAY.

> Four pieces. One sorted cab. Nothing drilled, nothing bolted, nothing modified.

**Primary:** `Get the Cab Reset Kit — $89`
**Secondary:** `Start with the CS-01 — $54.99`

**Microcopy:** Free US shipping over $75 · 30-day returns · Real person on the other end of support@`[TBC]`

---

## 15. Footer

**SHOP** — CS-01 · CS-02 · CS-03 · CS-04 · Cab Reset Kit · Full Rig Kit
**HELP** — What Fits My Truck · Shipping · Returns · FAQ · Contact
**COMPANY** — About · Privacy · Terms · Refund Policy
**CONTACT** — support@`[TBC]` · We answer within one business day, usually faster.

**Email capture:**
> New products and restocks. Nothing else. Maybe one email a month.
> `[email field]` `Sign up`

**Bottom:** CONVOYSUPPLY · Squared away. · © 2026 · `[payment icons]`

---

## Pre-publish checklist

- [ ] Every `[TBC]` replaced with a real, confirmed value
- [ ] Founder first name filled in §9
- [ ] Support email live and monitored
- [ ] Every `[IMAGE:]` slot filled with a real photograph of the real product (AI images only where `brand/brand-strategy.md` permits)
- [ ] Compare-at prices reflect the genuine sum of real individual prices
- [ ] No fake reviews, timers, or stock counters present
- [ ] Read aloud end to end — does it sound like a driver wrote it?
- [ ] Mobile QA on a real phone on cellular
