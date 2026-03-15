# Blog Redesign: "Forest Glass"

## Overview

Redesign the Astro blog with a nature-immersive glassmorphism aesthetic. An organic, blurred forest-themed background serves as the canvas, with frosted glass panels floating above it. The palette draws from earth and forest tones, creating a calm, sophisticated reading experience.

## Color System

| Token         | Hex       | Usage                                          |
| ------------- | --------- | ---------------------------------------------- |
| Pine Teal     | `#344e41` | Primary background tint, navbar                |
| Hunter Green  | `#3a5a40` | Glass card backgrounds (with alpha), borders   |
| Fern          | `#588157` | Accent color — links, tags, active states      |
| Dry Sage      | `#a3b18a` | Secondary text, muted elements, dates          |
| Dust Grey     | `#dad7cd` | Primary text color, headings                   |

Glass surfaces use `rgba()` versions of Hunter Green/Pine Teal with `backdrop-filter: blur()` for the frosted effect.

## Background

- A high-quality abstract organic/forest texture image, heavily blurred and darkened
- Subtle CSS gradient overlay using Pine Teal → Hunter Green for depth
- Fixed positioning (`background-attachment: fixed`) so content scrolls over it

## Typography

- **Headings:** Plus Jakarta Sans (700/800 weight) in Dust Grey
- **Body:** Inter (400/500) in Dust Grey with Dry Sage for muted text
- **Code:** JetBrains Mono
- Line height: 1.7 body, 1.3 headings

## Components

### Floating Glass Navbar (fixed)

- Frosted glass pill with `border-radius: 16px`
- `backdrop-filter: blur(16px)`, semi-transparent Hunter Green background
- Subtle 1px border in `rgba(163, 177, 138, 0.2)` (Dry Sage at low alpha)
- Detached from viewport edges with margin
- Blur intensifies slightly on scroll (12px → 20px)
- Logo/site name left, nav links right, RSS icon

### Post Cards (2-column grid)

- Frosted glass cards with `border-radius: 16px`
- Semi-transparent background, 1px subtle border
- Content: title, description, date, reading time, tags as small glass pills
- Hover: card lifts (`translateY(-4px)`), border glows with Fern, subtle shadow increase
- Responsive: collapses to single column on mobile

### Blog Post Page

- Single centered glass panel containing the article
- `max-width: 720px`, generous padding
- Tags displayed as small frosted pills at the top
- Code blocks get their own slightly darker glass treatment
- Smooth fade-in on load

### Tags Page

- Grid of glass pill/cards, each showing tag name + post count
- Hover glow effect matching the post cards

### About Page

- Single glass panel, same layout as blog post

### Footer

- Minimal text at the bottom, no heavy glass — just Dry Sage text on the background

## Animations & Micro-interactions

- **Cards:** `translateY(-4px)` + border glow on hover, `transition: 0.3s ease`
- **Navbar:** blur intensity 12px → 20px on scroll
- **Page content:** `opacity 0→1` + `translateY(8px→0)` fade-in on load
- **Links:** color transition Dry Sage → Fern on hover
- **Easing:** `ease` or `cubic-bezier` for organic feel

## Responsive Behavior

- **Desktop:** 2-column card grid, floating navbar with margins
- **Tablet:** 2-column grid preserved, tighter margins
- **Mobile:** single column, navbar stretches closer to edges but keeps rounded corners

## Tech Stack (unchanged)

- Astro 6 with scoped CSS and CSS custom properties
- No CSS framework — pure CSS with design tokens as custom properties
- Google Fonts: Plus Jakarta Sans, Inter, JetBrains Mono
