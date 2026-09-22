# Product Image Audit — Google Shopping Compliance

**Date:** 2026-09-22
**Source:** 14 supplier images from CJdropshipping listings
**All images:** 800×800px (two at 790×790) — meets Google's recommended minimum

---

## Google Shopping image policy — the rules that matter here

Google disapproves product images that contain:
- **Promotional text or overlays** ("Double the storage," "Large capacity," etc.)
- Watermarks, logos, or borders added over the product
- Placeholder or generic images
- Images where the product doesn't fill roughly 75–90% of the frame

Disapproved images mean the product is removed from Shopping results — not a warning, a removal. Fix before submitting the feed, not after.

---

## Verdict per image

### ✅ APPROVED — safe to submit

| Product | Image | Use as | Note |
|---|---|---|---|
| CS-02 Bunk Shelf Net | Cargo net, orange zipper, white bg | **PRIMARY** | Clean, centered, fills frame |
| CS-02 | Cargo net, green zipper, white bg | Secondary | Color variant |
| CS-04 Haul Bag | Brown duffel, front 3/4, white bg | **PRIMARY** | Best angle, shows pockets + handles |
| CS-04 | Brown duffel, back view | Secondary | Shows rear zip pocket |
| CS-04 | Brown duffel, top-down angle | Secondary | Shows shoulder strap |
| CS-03 Manifest Folio | Single brown folio, white bg | **PRIMARY** | Clean product-only shot |
| CS-03 | Hand holding folio w/ laptop + phone | Secondary | Shows scale/capacity — strong |
| CS-03 | Three folios (orange/brown/navy), gray bg | Secondary | Shows color options |
| CS-03 | Folios stacked w/ laptop + coffee | Secondary | Lifestyle |
| CS-01 Cab Command Organizer | Black organizer, product render, white bg | **PRIMARY** | Only clean CS-01 image available |

### ❌ REJECTED — do not submit to Google Shopping

| Image | Why | Can still be used for |
|---|---|---|
| Two organizers in car, "A pair is neater / Double the storage" | Promotional text overlay | Website page content only — NOT the feed |
| Black organizer flat, "Large storage capacity… Top: Fixed strap" | Text overlay + annotation lines | Website only |
| Organizer in seat back, "Multifunctional storage / Upgrade folding board" | Text overlay | Website only |

**These three are still usable on your Shopify product page and homepage** — Google's policy applies to the *feed image*, not every image on your site. Just never set them as the product's featured/primary image, because that's what syncs to Merchant Center.

---

## The CS-01 problem

**CS-01 (your highest-priced single SKU at $50) has only ONE compliant image** — the black product render on white. Every other CS-01 shot has text burned in.

This is a real weakness: Shopping listings with one image underperform listings with 4–6. Options, cheapest first:

1. **Request clean images from the supplier.** Message the CJ supplier (Yiwu Aiqi Trading) directly and ask for product photos without text overlays. Most suppliers have them — the text versions are made for marketplace listings. Costs nothing but a day or two.
2. **Crop the text out.** Two of the rejected images may survive a tight crop if the text sits in a band at the edge. Check whether cropping leaves the product filling enough of the frame.
3. **Shoot your own** once the QC sample arrives. Per `brand/brand-strategy.md`, real in-cab photography is the single biggest differentiator available — supplier renders on white are exactly what every competitor uses.

---

## Recommended primary image per product (what syncs to the feed)

| SKU | Primary image | Compliant |
|---|---|---|
| CS-01 Cab Command Organizer | Black organizer render, white bg | ✅ |
| CS-02 Bunk Shelf Net | Cargo net, orange zipper, white bg | ✅ |
| CS-03 Manifest Folio | Single brown folio, white bg | ✅ |
| CS-04 Haul Bag | Brown duffel, front 3/4, white bg | ✅ |

---

## Before uploading to Shopify

- [ ] Set the compliant image as **featured/first** on each product (that's what Merchant Center pulls)
- [ ] Add the text-overlay images further down the gallery, or omit entirely
- [ ] Add alt text to every image (helps SEO and accessibility)
- [ ] Rename files descriptively before upload (`cs-01-cab-command-organizer-black.jpg`, not `768e3314.jpg`) — minor SEO benefit
- [ ] Keep files under ~200KB each where possible; 800×800 JPEGs should compress well
