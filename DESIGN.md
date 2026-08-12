---
name: Kinetic Identity
colors:
  surface: '#11131c'
  surface-dim: '#11131c'
  surface-bright: '#373943'
  surface-container-lowest: '#0c0e17'
  surface-container-low: '#191b25'
  surface-container: '#1d1f29'
  surface-container-high: '#282934'
  surface-container-highest: '#32343f'
  on-surface: '#e1e1ef'
  on-surface-variant: '#c3c5d9'
  inverse-surface: '#e1e1ef'
  inverse-on-surface: '#2e303a'
  outline: '#8d90a2'
  outline-variant: '#434656'
  surface-tint: '#b7c4ff'
  primary: '#b7c4ff'
  on-primary: '#002682'
  primary-container: '#0052ff'
  on-primary-container: '#dfe3ff'
  inverse-primary: '#004ced'
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#c4c7c9'
  on-tertiary: '#2d3133'
  tertiary-container: '#636668'
  on-tertiary-container: '#e2e4e6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b7c4ff'
  on-primary-fixed: '#001452'
  on-primary-fixed-variant: '#0038b6'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#11131c'
  on-background: '#e1e1ef'
  surface-variant: '#32343f'
typography:
  display:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  button:
    fontFamily: Sora
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1280px
---

## Brand & Style

The design system is engineered for high-end tech environments, drawing inspiration from physical event credentials and digital collectibles. It balances the precision of an engineering tool with the prestige of a premium conference experience. 

The aesthetic is **Modern/Corporate with a High-Contrast Edge**. It utilizes a "Digital Physicality" approach—where elements feel like solid, high-tech objects through the use of sharp definition, micro-textures, and high-impact typography. The goal is to evoke a sense of exclusivity, innovation, and technical mastery. Key visual drivers include ultra-crisp borders, intentional white space, and localized vibrant accents that mimic light-emissive displays.

## Colors

The palette is built on a high-contrast foundation to ensure legibility and a "tech-forward" feel.

- **Primary (Electric Blue):** Used for key actions, active states, and high-priority branding elements. It should feel luminescent against the dark background.
- **Secondary (Deep Slate):** The core background and container color. This provides the "tech" foundation, moving away from pure black to a more sophisticated, deep oceanic charcoal.
- **Tertiary (Crisp White):** Reserved for primary headers and high-contrast text to ensure a "badge-like" punch.
- **Accent (Cyan):** Used sparingly for data visualization, secondary highlights, or success states to create a multi-layered blue light effect.

Surface colors should use a "Deep Slate" ramp, where containers are slightly lighter than the background to create a subtle sense of physical layers.

## Typography

Typography is the primary vehicle for the "event badge" aesthetic. 

1.  **Headlines:** Use **Sora** for its aggressive geometric stance and tech-optimistic feel. Large displays should be tightly tracked and heavy in weight to mimic high-end editorial layouts.
2.  **Body:** **Hanken Grotesk** provides a clean, contemporary grotesque feel that ensures readability in dense information blocks.
3.  **Labels/Technical Data:** **JetBrains Mono** is used for metadata, timestamps, and ID numbers, reinforcing the developer-centric/tech-focused nature of the design system.

All labels should be rendered in uppercase with increased letter-spacing to enhance the "ID Card" look.

## Layout & Spacing

The layout philosophy follows a **Structural Grid** model. Content should feel docked and organized, much like information on a printed PCB or a technical blueprint.

- **Grid:** A 12-column fluid grid for desktop, transitioning to 4 columns for mobile.
- **Rhythm:** A strict 4px/8px baseline grid ensures vertical alignment.
- **Badge Framing:** Key components (like cards) should use generous internal padding (32px) to allow elements to breathe and feel like "premium objects" rather than crowded web modules.
- **Borders as Spacing:** Use thin (1px) borders to separate sections instead of relying solely on whitespace, creating a structured, technical feel.

## Elevation & Depth

This design system avoids traditional soft shadows in favor of **Tonal Layering and Inner Glows**.

- **Surface Levels:** The base background is the darkest Slate. Elevated cards use a slightly lighter Slate with a subtle 1px border in a low-opacity White or Primary Blue.
- **Glows:** Instead of drop shadows, use "Outer Glows" for primary elements. A soft, blurred Electric Blue shadow with 15-20% opacity creates the effect of a glowing screen or neon indicator.
- **Textures:** Apply a faint "noise" or "scanline" overlay (2-3% opacity) to primary cards to give them a physical, tactile quality.
- **Glassmorphism:** Use backdrop-blur (12px+) on navigation bars and floating overlays to maintain the depth of the "digital collectible" look.

## Shapes

The shape language is **Precise and Industrial**. 

- **Corners:** Use "Soft" (0.25rem) as the default for most interactive elements to maintain a modern, machined feel. 
- **Large Containers:** Cards and badges may use `rounded-lg` (0.5rem) to differentiate them from smaller buttons.
- **Chamfered Alternative:** Where possible in custom CSS, use subtle 45-degree corner cuts instead of rounds for high-priority technical badges to emphasize the "tech-hardware" aesthetic.
- **Interactive States:** Buttons and inputs should maintain a consistent, tight radius to feel like solid physical toggles.

## Components

- **Buttons:** Primary buttons are solid Electric Blue with White uppercase Sora text. Secondary buttons are outlined with a 1px Blue border and a subtle glass-like background blur.
- **Event Badges (Cards):** These are the hero components. They must feature a high-contrast header section, a JetBrains Mono "ID Number" in the top right, and a subtle gradient background (Deep Slate to a slightly lighter Blue-Slate).
- **Chips/Tags:** Small, rectangular labels with `label-mono` typography. Use high-contrast background fills (e.g., a "VIP" tag in Electric Blue with White text).
- **Input Fields:** Dark background, 1px Slate border that glows Primary Blue on focus. Labels should always be positioned above the field in `label-mono`.
- **Status Indicators:** Use small, circular "LED" style pips that use a pulse animation to indicate live/active events.
- **Dividers:** Use dashed or dotted lines for a "perforated" look, mimicking tear-off sections of physical tickets.