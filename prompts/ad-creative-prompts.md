# ConvoySupply — Ad Creative Prompts

**Date:** 2026-09-20
**For:** the ten Meta ad concepts in `marketing/meta-ads.md`

---

## Which ads need a real photograph

Six of the ten. **This is the production constraint that drives the entire 30-day schedule.**

| Ad | Angle | Image source | Wave |
|---|---|---|---|
| **AD-01** | Before/after | **REAL PHOTO — PHOTO-01** | 1 |
| AD-02 | Problem/solution | AI — `PROB-SEARCHING` | 1 |
| **AD-03** | Comparison | **REAL PHOTO — PHOTO-15** | 1 |
| AD-04 | Educational | AI base `EDU-SEAT-BACK` + diagram | 1 |
| **AD-05** | Product benefit | **REAL PHOTO — PHOTO-03** | 1 |
| AD-06 | Time saving | AI — `BG-CLOCK` + graphic | 2 |
| AD-07 | Curiosity | AI — `PROB-BUNK-WALL` | 2 |
| AD-08 | Lifestyle | AI — `LIFE-EVENING` | 2 |
| **AD-09** | Bundle | **REAL PHOTO — PHOTO-14** | 2 |
| AD-10 | Objection-first | AI — `BG-ASPHALT` + typography | 2 |

**Three of the five Wave 1 ads are blocked on physical samples**, which is why samples are ordered on Day 1 of `execution/30-day-plan.md` rather than Day 5. Nothing else in the plan has that much downstream dependency.

AI prompt bodies live in `prompts/image-generation-prompts.md` under the codes above. This file covers the ad-specific treatment.

---

## Ad creative rules

Beyond the standard AI rules:

1. **The hook must be readable at 200px wide.** Facebook feed thumbnails are small. Most competitor ad creative fails this and it is the cheapest advantage available.
2. **Keep on-image text under ~20% of area.** Meta no longer hard-rejects text-heavy images, but delivery still suffers. One hook, not a paragraph.
3. **One hi-viz amber emphasis per image.** Two competing highlights means none.
4. **4:5 portrait, 1080×1350.** Maximum feed real estate on mobile.
5. **Under 300 KB.** This audience is frequently on poor cellular signal.
6. **No fabricated review, rating, star, or testimonial in any creative.**
7. **No countdown, urgency graphic, or "limited time" badge.**
8. **No competitor brand mark or name.**

---

# AD-01 — Before/After **[LAUNCH]**

**REAL PHOTOGRAPH. NO AI.**

**Shot direction:**
> Tripod, locked off. Same cab, same camera position, same lens, same light, one session. Shoot the "before" first with a genuinely cluttered passenger seat — do not stage the mess, let it be real. Fit the CS-01, load it with the same items, shoot the "after" without moving the camera by a millimeter.

**Composition:** shot from the driver's seat position, passenger seat filling the frame, windshield light from the left. Natural overcast light.

**Layout:** vertical split, before left, after right. Thin hi-viz divider. Hook across the bottom third over an asphalt scrim. Small "BEFORE" / "AFTER" labels in Roboto Mono, hi-viz, top corners.

**Hook:** SAME SEAT. TWO MINUTES APART.

> **If the two frames don't match exactly, the ad doesn't run.** A before/after with a different angle or different light is a dishonest comparison, and this is the flagship creative — it has to be beyond question.

---

# AD-02 — Problem/Solution **[LAUNCH]**

**AI permitted** — no product in frame.

**Prompt:** `PROB-SEARCHING` from `image-generation-prompts.md`.

**Treatment:** full-bleed image, heavy asphalt gradient scrim from the bottom 40%. Hook bottom-left. Slight desaturation so the amber text separates cleanly.

**Hook:** YOU KNOW IT'S IN HERE SOMEWHERE.

**Plausibility risk: low.** Tight crop on a hand and soft goods, no cab geometry visible — the safest AI shot in the set.

---

# AD-03 — Comparison **[LAUNCH]**

**REAL PHOTOGRAPH. NO AI.** Requires both products in one honest frame.

**Shot direction:**
> Hold a generic car seat-back organizer against a Class 8 passenger seat back, then the CS-01 in the same position. Same camera position, same light. The size difference has to be visible without annotation — if it needs an arrow to be obvious, the shot is wrong.

**Critical:** **no competitor brand mark visible.** Turn the label away, or crop it out.

**Layout:** side by side. Hi-viz outline on the CS-01 side only. Hook across the top.

**Hook:** ONE OF THESE FITS A CLASS 8 SEAT.

---

# AD-04 — Educational **[LAUNCH]**

**AI base + designed diagram overlay.**

**Prompt:** `EDU-SEAT-BACK`.

**Overlay:** three measurement callouts with dimension arrows and labels — (1) seat back height, (2) seat back width, (3) headrest clearance. Hi-viz arrows, white labels in Roboto Mono, thin white leader lines.

**Hook:** MEASURE THESE 3 THINGS FIRST.

**Keep perspective distortion minimal** in the base image — dimension annotations over a distorted frame read as wrong even when they are right.

**Destination is the fit guide, not the product page.** Deliberate, and the reason this ad exists (EXP-008).

---

# AD-05 — Product benefit **[LAUNCH]**

**REAL PHOTOGRAPH. NO AI.**

**Shot direction:**
> Camera at the driver's eye position, belted in. A forearm and hand reaching across to the CS-01 fitted on the passenger seat back, mid-reach, pulling out a flashlight or a water bottle. The frame has to communicate *reachable from the seat* — that is the whole benefit, and it can only be shown from this exact viewpoint.

**Layout:** full bleed, hook bottom-left over a scrim, price in Roboto Mono bottom-right.

**Hook:** EVERYTHING WITHOUT LEAVING YOUR SEAT.

---

# AD-06 — Time saving *(Wave 2)*

**AI base + graphic.**

**Prompt:** `BG-CLOCK`.

**Treatment:** dashboard clock sharp in the foreground, cluttered dash soft behind. Hook over the blurred area.

**Hook:** 17 HOURS A YEAR. LOOKING FOR A FLASHLIGHT.

> The 17-hour figure is arithmetic from a stated 20-minutes-a-week premise, which is itself a hypothesis. **Frame it as an illustration in the copy, never as a measured finding.** The caption in `marketing/meta-ads.md` does this — do not tighten it into a claim.

---

# AD-07 — Curiosity *(Wave 2)*

**AI base + annotation.**

**Prompt:** `PROB-BUNK-WALL`.

**Overlay:** a hi-viz dashed rectangle outlining the empty wall area, with a small label — "4 sq ft. Doing nothing."

**Hook:** THE SPACE IN YOUR CAB YOU'VE NEVER USED.

**Plausibility risk: medium.** Bunk geometry is visible. Run the full five-question check and crop tighter if anything looks wrong.

---

# AD-08 — Lifestyle *(Wave 2)*

**AI permitted** — no product in frame.

**Prompt:** `LIFE-EVENING`.

**Treatment:** full bleed, minimal overlay. This is the quietest creative in the set and the type should stay out of the way. Hook small, bottom-left, generous margin.

**Hook:** HOME FOR THE NEXT 19 DAYS.

**Plausibility risk: high.** A wide cab interior is the hardest thing for a model to get right. **If the geometry is not convincing, crop to a detail or drop the concept.** Do not ship a wide shot with a wrong dashboard.

---

# AD-09 — Bundle *(Wave 2)*

**REAL PHOTOGRAPH. NO AI.**

**Shot direction:**
> Overhead, the three Cab Reset Kit products laid out on a truck bunk. Natural light through the sleeper curtain. Arranged but not styled — this is a working kit, not a flat-lay.

**Layout:** full bleed. Price block bottom-right in Roboto Mono, showing $112.97 struck through and $89.00 in hi-viz.

**Hook:** THREE PIECES. $23.97 OFF.

> The struck-through price must be the genuine sum of the three individual prices, which are really charged. This is the only place a strike-through appears in any ConvoySupply creative.

---

# AD-10 — Objection-first *(Wave 2)*

**Typographic. No product image at all.**

**Prompt:** `BG-ASPHALT`.

**Treatment:** the copy is the creative. Hook large, centered-left, Barlow Condensed 700. Sub-line beneath in Inter. Wordmark small at the bottom. Nothing else in the frame.

**Hook:** WE'RE NOT CHEAPER THAN AMAZON.
**Sub:** But we're built for your truck.

> **The highest-variance creative in the set.** Leading with a disadvantage either stops the scroll cold or reads as weakness. Recorded prediction: lowest CTR, highest conversion rate on the clicks it gets. If that holds it is the most valuable thing learned in the whole test, because it says the audience responds to honesty over persuasion. Whatever happens, log it against EXP-002 — do not quietly drop it for having a low CTR.

---

## Text overlay template

One template. Swap image and hook.

| Element | Spec |
|---|---|
| Canvas | 1080 × 1350 |
| Scrim | Linear gradient, `#1C1F21` at 85% → transparent, bottom 45% |
| Hook | Barlow Condensed 700, uppercase, 72–96px, `#EDEBE7`, bottom-left, 64px margin |
| Emphasis | **One** word or phrase in `#E8B23A`. One only. |
| Sub-line | Inter 500, 32px, `#C9C5BE`, under the hook |
| Price | Roboto Mono 400, 36px, `#E8B23A`, bottom-right |
| Wordmark | Barlow Condensed 700, 24px, letterspaced, `#EDEBE7` at 60%, bottom-right corner |
| Labels | Roboto Mono 400, 20px, letterspaced, `#E8B23A` |

**No borders. No drop shadows. No swooshes. No badges.**

## Variant testing

For any creative that performs, test in this order — **one variable at a time**:

1. **Hook wording** — cheapest change, largest effect
2. **Image crop** — tight vs. wide
3. **Scrim position** — top vs. bottom hook
4. **Price shown vs. hidden**

Log each variant as `v2`, `v3` in `marketing/creative-library.md` and record which version ran when in `execution/experiments.md`. **A creative "fatiguing" and a creative "being replaced by a worse version" look identical in the data if you cannot tell them apart.**

## Before any ad goes live

- [ ] Real photograph used wherever the product is in frame
- [ ] AI images pass the five plausibility questions
- [ ] Before/after is the same cab, angle, light and lens
- [ ] Hook readable at 200px
- [ ] On-image text under ~20% of area
- [ ] One hi-viz emphasis only
- [ ] No fabricated review, rating or testimonial
- [ ] No countdown or urgency graphic
- [ ] No competitor brand mark
- [ ] Strike-through price is a genuine sum of real prices
- [ ] Under 300 KB, 1080×1350
- [ ] Link UTM-tagged with the AD-XX code
- [ ] Complies with Meta's advertising policies
