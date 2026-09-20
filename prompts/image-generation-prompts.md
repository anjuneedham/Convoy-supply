# ConvoySupply — Image Generation Prompts

**Date:** 2026-09-20
**For:** organic static posts, store imagery, backgrounds and contexts

---

## The rule that governs this entire file

| Use | AI allowed? |
|---|---|
| Any frame containing our actual product | **NO. Real photograph. Always.** |
| Before/after of our product | **NO. Same cab, same angle, same light, same lens.** |
| "Customer" photos | **NO. Prohibited entirely.** |
| Any image implying a real person used the product | **NO.** |
| Problem states with no product in frame | Yes |
| Lifestyle context with no product in frame | Yes |
| Backgrounds, textures, infographic bases | Yes |
| Diagram bases | Yes |

**Why this is absolute:** a rendered image of a product that does not exist, presented as a photograph of a product you can buy, is a lie about the thing being sold. This audience is unusually suspicious of marketing and discusses sellers publicly in Facebook Groups **[H]**. The credibility cost of being caught is permanent and it is not recoverable by apology.

## The plausibility check — non-negotiable

Generative models produce semi truck interiors with **wrong door geometry, impossible mirror placement, dashboards that do not exist, and steering wheels at the wrong angle.** A professional driver spots this in half a second.

**Before any AI cab image is used:**
1. Does the dashboard layout resemble a real Class 8 truck?
2. Is the steering wheel angle plausible for a semi (near-horizontal, not car-like)?
3. Are the mirrors, windows and door geometry right?
4. Is the sleeper proportioned like a real sleeper?
5. Would a driver look at this and immediately know it is fake?

**Any doubt on any question = do not use it.** Crop tighter, reshoot, or use a detail shot instead. A tight crop of a cluttered footwell is far safer than a wide cab interior, and usually more effective anyway.

---

## Base style block — append to every prompt

```
Photorealistic documentary photography. Natural light only, no flash, no
artificial studio lighting. Slightly desaturated color, slightly lifted
blacks. Realistic wear and use — scuffs, dust, worn upholstery. 35mm lens
character, shallow depth of field where appropriate. No text, no logos, no
brand marks, no watermarks, no people's faces. Unstaged, candid, honest.
```

### Negative prompt — use every time

```
cartoon, illustration, 3D render, CGI, digital art, oversaturated, HDR,
lens flare, chrome gleam, sunset silhouette, stock photo aesthetic,
smiling model, thumbs up, text, watermark, logo, brand name, pristine
showroom, artificial studio lighting, wide-angle distortion, plastic
looking, AI artifacts, extra fingers, warped geometry
```

**"Chrome gleam" and "sunset silhouette" are excluded deliberately** — they are the trucking-imagery cliché this audience is most tired of, and models default to them hard.

---

## Problem-state prompts

### PROB-PASSENGER-SEAT · P-01, LP-PROB-01
```
Photorealistic interior of a semi truck sleeper cab viewed from the driver's
seat. The passenger seat is cluttered with a stainless water bottle, worn
work gloves, a clipboard with loose papers, tangled phone charging cables, a
folded jacket and food packaging. Overcast morning light through the
windshield. Worn grey upholstery with visible use. Documentary photography,
35mm, natural slightly desaturated color. No text, no logos, no people.
```

### PROB-SEARCHING · P-02, AD-02
```
Close-up photorealistic shot of a hand searching through a cluttered semi
truck sleeper bunk — rumpled clothing, a canvas duffel bag, charging cables,
a spiral logbook. Slight motion blur on the hand. Dim warm interior light
from a single overhead lamp. Documentary, shallow depth of field, 50mm. No
text, no faces, no logos.
```

### PROB-FOOTWELL · P-03
```
Photorealistic footwell of a semi truck passenger side. A water bottle on
its side, work gloves, loose papers and a small flashlight scattered across
a worn rubber floor mat. Harsh midday daylight from the side window casting
hard shadows. Dust, grit, realistic wear. Documentary, unstaged, 35mm. No
text, no people, no logos.
```

### PROB-BUNK-WALL · P-04, AD-07
```
Photorealistic semi truck sleeper bunk with a duffel bag, folded clothes and
a work jacket lying on the mattress. The wall panel above and beside the bunk
is completely bare and empty. Soft natural light entering through a gap in
the sleeper curtain. Documentary interior photography, 35mm, natural color.
No text, no people, no logos.
```

### PROB-DOOR-POCKET · P-05
```
Close-up photorealistic shot of a semi truck door pocket crammed with creased
paperwork, curled receipts, a folded map and a ballpoint pen. Worn grey
plastic door trim with scuffs. Natural side light from the window. Documentary,
shallow depth of field, 50mm. No readable text, no logos, no people.
```

### PROB-CABLES · P-10
```
Photorealistic close-up of a semi truck dashboard with four or five tangled
black charging cables running from a 12V socket across the dash surface. A
phone mount, sunglasses and a crumpled receipt nearby. Bright daylight through
the windshield. Worn dashboard plastic. Documentary, natural color, 35mm. No
text, no logos, no people.
```

### PROB-WIDE-CAB · P-06, E-01
```
Wide-angle photorealistic interior of a semi truck sleeper cab showing the
bunk, the backs of both seats and the shallow overhead storage cubbies. Late
afternoon light through the side window. Realistic wear on every surface.
Composition leaves clear negative space in the upper third for a headline
overlay. Documentary architectural interior photography, natural color. No
text, no people, no logos.
```

### PROB-SPLIT-TRUCK · P-07
```
Split composition, two halves. Left: exterior three-quarter view of a clean
modern Class 8 semi truck parked in a truck stop lot under overcast light.
Right: the cluttered interior of a sleeper cab. Documentary photography with
a consistent color grade across both halves. No text, no logos, no people.
```

### PROB-MONDAY-THURSDAY · P-08
```
Two matching photorealistic frames of the same semi truck passenger seat from
an identical camera angle in identical light. Frame one: clean, empty, seat
belt neatly stowed. Frame two: the same seat covered in gear, clothing, cables
and food packaging. Documentary, identical composition and grade across both.
No text, no people, no logos.
```
> **Generate as one image with two panels, or generate twice with a fixed seed.** If the two frames do not match exactly the comparison is dishonest and the post does not run.

### PROB-OPEN-DOOR · P-09
```
Photorealistic view through an open passenger door of a semi truck, looking up
from ground level at a cluttered seat and floor. Daylight, truck stop lot
softly blurred in the background. Documentary, 35mm. No text, no people, no
logos.
```

---

## Lifestyle prompts

### LIFE-4AM · L-01
```
Photorealistic interior of a semi truck sleeper cab before dawn. Warm low
light from a single bunk reading lamp is the only illumination. A coffee cup
and a closed logbook rest on a tidy flat surface. Through the windshield, a
dark truck stop lot with distant amber lot lighting. Moody, quiet, still.
Documentary photography, slightly desaturated, 35mm, shallow depth of field.
No text, no people, no logos.
```

### LIFE-EVENING · L-02, LP-FINAL, CTA-01
```
Photorealistic wide interior of a well-organized semi truck sleeper cab in
warm evening light. Bunk neatly made, gear stowed out of sight, a work jacket
hung on a hook. Lived-in but orderly. Documentary interior photography, warm
natural color, 35mm. No text, no people, no logos.
```

### LIFE-ORGANIZED · L-03
```
Photorealistic photograph of a neatly organized semi truck sleeper cab
interior in even natural daylight. Clean uncluttered composition, everything
stowed, surfaces clear. Documentary interior photography, natural color, 35mm.
No text, no people, no logos.
```

---

## Educational and diagram bases

### EDU-SEAT-BACK · E-03, AD-04, LP-DEMO
```
Photorealistic side view of a semi truck passenger seat back from inside the
cab, unobstructed and clean, in even diffuse daylight. Plain uncluttered
composition suitable for measurement annotation overlays. Documentary, 50mm,
minimal perspective distortion. No text, no people, no logos.
```
> Keep perspective distortion minimal — dimension annotations over a distorted frame read as wrong.

### EDU-STRAP-DETAIL · E-04
```
Photorealistic close-up interior detail of a semi truck sleeper showing a
fabric strap fastened around a seat back frame with a cam buckle, no drilling
or permanent hardware visible. Natural window light. Documentary product-in-
context photography, 50mm, shallow depth of field. No text, no logos, no people.
```

### EDU-MID-RESET · E-05
```
Photorealistic semi truck sleeper cab interior partway through being
organized. A few items laid out on the bunk in deliberate separate groups, the
rest of the cab clear. Warm afternoon light through the side window.
Documentary, natural color, 35mm. No text, no people, no logos.
```

### EDU-CRATE · C-02
```
Photorealistic photograph of a plastic milk crate sitting on a semi truck
passenger seat, filled with mixed gear — a water bottle, gloves, a coiled
cable, a rag. Natural cab light through the windshield. Worn crate, realistic
scuffs. Documentary, 35mm. No text, no logos, no people.
```

---

## Graphic backgrounds

### BG-ASPHALT · C-03, PR-02, AD-10
```
Flat dark asphalt-grey surface, subtle fine concrete texture, even diffuse
lighting, no gradient hotspots, completely clean and empty. Top-down, filling
the frame. Suitable as a background for a bold typographic overlay. No text,
no objects, no people.
```

### BG-CLOCK · AD-06
```
Photorealistic semi truck cab interior with a dashboard clock display in sharp
focus in the foreground. Cluttered dash surfaces softly out of focus behind.
Early morning blue light through the windshield. Documentary, 50mm, shallow
depth of field. No readable text other than the clock, no logos, no people.
```

---

## Generation workflow

1. **Base prompt + style block + negative prompt**
2. **Generate 4 variations.** Costs nothing extra and the hit rate on plausible cab interiors is low.
3. **Run the plausibility check on every one.** Reject freely — a rejected image costs a minute, a published implausible one costs credibility.
4. **Prefer the tighter crop.** A detail shot of a cluttered footwell is safer than a wide cab interior and usually works better as a thumbnail anyway.
5. **Save as `CS_AI_[CODE]_[RATIO]_v[N]`.** The `AI_` prefix makes it structurally impossible to mistake for product photography later.
6. **Log it in `marketing/creative-library.md`.**

## Settings

| Setting | Value | Why |
|---|---|---|
| Aspect ratio | 4:5 feed · 1:1 Marketplace · 16:9 web | Match the destination |
| Resolution | 2048px min on the long edge | Room to crop |
| Style strength | Low-to-medium | High settings push toward stock-photo gloss |
| Seed | **Record it** | Needed for matched pairs like P-08 |

## Before publishing any AI image

- [ ] Contains **no** depiction of our actual product
- [ ] Passes all five plausibility questions
- [ ] No text, logos, or brand marks generated into the frame
- [ ] No faces
- [ ] No warped geometry, extra fingers, or visible artifacts
- [ ] Does not look like a stock photo
- [ ] Filename carries the `AI_` prefix
- [ ] Logged in the creative library
- [ ] **Would a driver believe this is a real truck?**

**Reference tag [H] is defined in `research/customer-avatar.md`.**
