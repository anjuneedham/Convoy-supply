# Higgsfield Creative Prompts — CS-01 Cab Command Organizer

**Status:** Written for use in Higgsfield's web app (higgsfield.ai) since CLI auth couldn't complete in this remote session. Paste directly into their video/image generation tools.

**Grounded in the actual product photo** (fold-down tray, tablet/mirror pocket, 2 bottle/cup holders, quilted tissue-box pocket, mesh pocket) — not invented specs, per `brand/brand-copy.md` honesty rules.

---

## A) Video Ad — 20-30 seconds (Meta/Facebook, A-side of test)

**Use Higgsfield's `ad_creative_pack` or general video generation mode.**

```
A 25-second vertical (9:16) product ad video for a truck cab seat-back organizer,
in a realistic documentary style, natural lighting, no text overlays baked into
the video itself (captions will be added separately).

SCENE 1 (0-4s): Interior of a semi-truck cab, passenger seat. Loose items visible
on the seat — a phone, a water bottle, a charging cable, a granola bar wrapper.
Handheld camera feel, slightly messy, realistic daily clutter. Natural window
light.

SCENE 2 (4-10s): Cut to a hand mounting a black quilted-leather seat-back
organizer onto the seat back in front, adjustable straps being pulled tight
around the headrest posts. Quick, confident motion — takes about 2 minutes in
real life, shown in a fast 6-second sequence.

SCENE 3 (10-20s): Close-up sequence showing the organizer's features in use:
- A tablet propped into the small mesh/mirror pocket at the top
- The fold-down tray being lowered flat, holding a coffee cup steady
- A hand placing a water bottle into one of the two quilted side holders
- A hand pulling a tissue from the central quilted tissue pocket
- The bottom mesh pocket holding a folded jacket

SCENE 4 (20-26s): Wide shot, driver's point of view from the driver's seat,
looking at the now-organized passenger seat — tray down, everything in its
place, seat visibly clear and usable again. Calm, satisfied pacing, not
triumphant or over-produced.

SCENE 5 (26-30s): Final still-ish frame on the product alone, mounted and
loaded, soft natural light, black asphalt-dark background vignette.

Style: realistic, handheld documentary feel, muted natural color grade,
no upbeat commercial music sting, no on-screen text, no fast MTV-style cuts.
This should feel like a real driver's dashcam or phone footage, not a polished
studio ad.
```

**Caption to add after export (not baked into video):**
> Your passenger seat isn't a desk. This straps on in two minutes. $50.

---

## B) Static Image — A/B test variant (B-side, same campaign)

**Use Higgsfield's `product_shot` or `ad_creative_pack` mode, single still image.**

```
A single square (1:1) product ad image for a truck cab seat-back organizer.
Split-frame before/after composition, left half and right half of the same
frame.

LEFT HALF: A cluttered truck cab passenger seat — loose phone, water bottle,
tangled charging cable, fast food wrapper, scattered across the seat. Slightly
desaturated, flat overhead natural light, documentary realism, not staged-ugly.

RIGHT HALF: The same seat, same camera angle and lighting, now with the black
quilted-leather seat-back organizer mounted and loaded — tablet in the top
pocket, tray folded down holding a coffee cup, water bottle in a side holder,
tissue pocket visible, bottom mesh pocket holding a folded item. Everything
visibly contained and orderly.

A thin vertical divider line down the center of the frame. No text, no
graphics, no arrows — the visual contrast alone tells the story. Natural,
slightly warm daylight. Realistic, not glossy/CGI-looking.
```

**Caption to add after export:**
> Everything in its place. Nothing in your way. $50 — free shipping over $75.

---

## Why this A/B pairing

Per `brand/brand-strategy.md`, before/after is "the single highest-leverage static image available to this brand" — the static version leads with that directly. The video gives the same argument motion and context (the 2-minute install, the tray/holders in actual use), testing whether motion outperforms the static before/after for this audience. Both use identical brand voice: no fake urgency, no invented specs beyond what's visible in the real product photo, real price shown plainly.

## Setup note

Both ads should run as a **CBO split test within one ad set pair** per the existing `marketing/meta-ads.md` structure (if that file exists) or as two variants under the same audience/budget per `DEC-007`'s identical-creative testing logic — same audience and budget, only the creative format differs, so the difference in performance is attributable to video vs. static rather than audience variance.
