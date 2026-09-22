# Tinker Theme Overrides — ConvoySupply

Built by editing the actual exported JSON from your live store (`nax2hx-gr.myshopify.com`, Tinker v4.2.0) in place — same block structure, only the text/color values changed. This is lower-risk than hand-written new sections since the schema is already proven valid on your store.

## Files

- `index.json` → replaces `templates/index.json`. Updates the homepage hero (headline, subhead, adds a "Shop the Collection" button), the "Productivity Essentials" section (renamed to "Four Pieces. One Sorted Cab."), and the collection list heading ("Shop by Zone"). Your existing product-linked sections (the 4 featured-product-information blocks pointing at CS-01–CS-04, and the product-list section) are untouched — they were already correct.
- `settings_data.json` → replaces `config/settings_data.json`. Sets the theme's global color palette to ConvoySupply's brand tokens:
  - `background` → `#FAF9F7` (paper)
  - `foreground` → `#14171A` (ink)
  - `color1` → `#E8B23A` (hi-viz amber — this drives your primary button color)
  - `color2` → `#3A4247` (steel)
  - `color3` → `#1C1F21` (asphalt)
  - `color4` → `#EDEBE7` (concrete)

## How to install (Shopify admin, no CLI needed)

1. Go to **Online Store → Themes**, find Tinker, click the **⋯** menu → **Edit code**
2. In the file browser, open **`templates/index.json`**
3. Select all existing content, delete it, paste in the contents of this repo's `index.json`
4. Save
5. Open **`config/settings_data.json`**
6. Select all, delete, paste in this repo's `settings_data.json`
7. Save
8. Go back to **Customize** on the theme and check the homepage — hero copy, button, and colors should now reflect the brand

## What this does NOT do

- Does not touch your product titles/descriptions — still update those manually in **Products** using `store/product-descriptions-live.md`
- Does not add the bundle products (Cab Reset Kit, Full Rig Kit) — create those as new products manually, per the fulfillment notes in `store/product-descriptions-live.md`
- Does not add a real logo image — the header still shows Tinker's default logo/text setting. Set your wordmark text or upload the SVG logo separately under **Theme settings → Logo**

## Rollback

Before pasting over these files, Shopify's Edit Code keeps version history — you can revert from the **Files** panel's history icon if anything looks wrong after saving.
