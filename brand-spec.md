# Lia — brand and asset notes

## Identity

- **Logo:** `public/logo_lia.png` (original asset; do not redraw or recolor).
- **Primary teal:** `#0d9488`.
- **Deep teal:** `#134e4a`.
- **Accent amber:** `#f59e0b`; light accent `#fbbf24`.
- **Typography:** Bricolage Grotesque for landing-page display headings, Inter for body text and controls, and Poppins inside the app-screen preview; loaded from Google Fonts by `src/layouts/Layout.astro`.
- **Visual direction:** warm, clear, and caring; use tints of the teal/amber palette and restrained neutral surfaces.

## Photography used in `/v0`

- `public/v2/woman-and-dog-portrait.jpg` — “Woman and dog portrait” by Scarleth Marie, CC BY 2.0. Source/credit: [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=108100191).
- `public/v2/american-eskimo-dog-portrait-above.jpg` — photo by SheltieBoy, CC BY 2.0. Source/credit: [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=1923059).
- `public/v2/dog-walking-in-the-mission-in-san.webm` (poster: `public/v2/dog-walking-in-the-mission-in-san-poster.jpg`) — video by Sage Ross, CC BY-SA 3.0. Source/credit: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dog_walking_in_the_Mission_in_San_Francisco.ogv).

The Lía app screens in the phone mockup are a locally authored visual preview; any names and screen content are illustrative, not real customer or veterinary data. The waitlist form is not connected to a backend. Photo/video credits remain visible outside the media rather than as overlays on top of it.

- `public/packs/esencial.png`, `public/packs/equilibrado.png`, and `public/packs/premium.png` are original, unbranded reference packshots generated locally with `scripts/generate-food-packs.py`. They use the credited SheltieBoy dog photo and distinguish the three food tiers; they are not real retail products.

## Landing-page inspiration — Lía app mockups

Use the supplied seven-screen mobile mockup as the visual and product-story reference for the landing page. The screens show onboarding, personalized food-plan selection, the customer home screen, a pet profile, and a loyalty-points page. They are inspiration for the marketing page, not a request to reproduce the app screens literally.

### Product idea and message

- Lía helps dog owners avoid running out of food: it estimates when a bag will run out and arranges timely replenishment through a neighborhood store.
- Core promise from the mockup: **“La comida de tu perro llega antes de que se acabe.”**
- The onboarding flow personalizes recommendations using the dog’s photo and profile details (name, birth date, weight, breed, and activity level), then estimates daily food needs and how long a bag will last.
- Customers choose among three food tiers (Esencial, Equilibrado, Premium) and can enable automatic replenishment. Emphasize secure payment, flexibility, and the ability to cancel.
- The app experience also includes delivery tracking, pet-care/food guidance, and rewards for timely replenishment.
- Use Spanish-language copy and a warm, reassuring, practical tone. Treat names, dates, prices, and point totals shown in the mockups as illustrative examples, not verified product facts.

### Visual direction and palette

The mockups use a calm, high-contrast teal-led palette with a vivid orange call to action and very light cool-neutral surfaces. The following hex values are visual estimates from the supplied images, not sampled source tokens:

- Deep blue-green / primary dark surface: approximately `#0B3D4A`.
- Dark teal text and outlines: approximately `#123C48`.
- Teal secondary surfaces: approximately `#155766`.
- Muted teal for progress and icons: approximately `#78D2C8`.
- Bright orange CTA and highlights: approximately `#F87527`.
- Pale cool-gray page background: approximately `#F4F7F6`.
- White cards and fields: `#FFFFFF`, with subtle cool-gray borders around `#DCE6E7`.

Prefer deep teal for prominent hero or feature surfaces; orange for primary actions and small highlights; pale neutral backgrounds for the main page; and white rounded cards with restrained borders. Keep contrast and hierarchy clear. This mockup palette is a design reference and may differ from the older brand color values listed above.

### Logo and visual motifs

- Use the existing original logo asset at `public/logo_lia.png`; do not redraw or recolor it. The official asset is the teal running-dog silhouette with orange motion accents. It appears in the landing-page header and footer, and in the app preview’s home-screen header.
- Do not substitute the older white dog-profile mark from the inspirational mockups for the official running-dog asset.
- Recurring UI motifs in the mockups: rounded pill-shaped orange buttons, rounded white cards, simple teal line icons, pet photography, progress indicators/rings, and step progress bars. These can inform the landing page’s visual language without implying that every app control belongs on the marketing page.

### Current landing-page implementation

The `/` route applies this direction with a deep-petrol hero, oversized Bricolage Grotesque headings, orange primary actions, a rotating orbital motif, the app phone preview, a scroll-led onboarding tour, and an interactive bag-duration calculator. The other routes (`/v0`, `/v2`, `/v3`, and `/tiendas`) are preserved as independent versions. The calculator is explicitly an estimate, and the waitlist form is explicitly an unconnected demonstration.
