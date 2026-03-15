---
name: google-slides
description: Create, edit, read, and export Google Slides presentations using Playwright browser automation. This skill should be used when the user asks to create a presentation, build slides, edit Google Slides, export a deck, or mentions Google Slides in any capacity. Triggers on phrases like "create a presentation", "make slides", "build a deck", "Google Slides", "presentation about X", "slide deck".
---

# Google Slides Automation via Playwright

Automate Google Slides using Playwright MCP browser tools. Interact with Google Slides through keyboard shortcuts, the Tool Finder (Alt+/), and accessibility-tree-based navigation.

## Prerequisites

Playwright MCP server must be connected. The skill uses `mcp__playwright__browser_*` tools for all interactions.

## Workflow Overview

Every Google Slides task follows these phases:

1. **Discovery** - Understand what the user wants to create
2. **Auth Check** - Ensure user is logged into Google
3. **Execute** - Create/edit/read/export the presentation
4. **Verify** - Screenshot the result for confirmation

---

## Phase 1: Discovery (Brief Q&A)

Before touching the browser, gather requirements with a short conversation. Ask only what is needed, in a single message:

### For New Presentations

Ask:
- **Topic**: What is the presentation about?
- **Audience**: Who is this for? (e.g., investors, team, students, clients)
- **Slide count**: Approximate number of slides? (suggest a default based on type)
- **Style/tone**: Professional, casual, minimal, bold, creative?
- **Key sections**: Any specific sections or content to include?
- **Special elements**: Charts, images, tables, diagrams needed?

### For Editing Existing Presentations

Ask:
- **URL**: The Google Slides URL
- **Changes**: What needs to be modified?

### For Reading/Exporting

Ask:
- **URL**: The Google Slides URL
- **Format**: PDF, PPTX, or images?

After gathering answers, summarize the plan back to the user and get confirmation before proceeding.

---

## Phase 2: Auth Check

### Step 1: Navigate to Google Slides

```
Navigate to: https://docs.google.com/presentation/create
```

### Step 2: Take a Snapshot

Use `browser_snapshot` to inspect the page state.

### Step 3: Evaluate Login Status

**If logged in** (snapshot shows slide editor, canvas, toolbar):
- Proceed to Phase 3

**If login screen detected** (snapshot shows "Sign in", email input, `accounts.google.com` in URL):
1. Inform the user: "Google Slides requires you to be logged in. Please sign in to your Google account in the browser window."
2. **Wait for user confirmation** - Ask: "Let me know once you've signed in and I'll continue."
3. After user confirms, take another snapshot to verify login succeeded
4. If still on login page, repeat the prompt

**If CAPTCHA or 2FA detected**:
1. Inform user about the additional verification step
2. Wait for confirmation before proceeding

---

## Phase 3: Execution

### Creating a New Presentation

#### Step 1: Set Up the Presentation

1. Navigate to `https://docs.google.com/presentation/create`
2. Wait for editor to load (snapshot should show canvas)
3. Set the presentation title by clicking the "Untitled presentation" text in the top-left and typing the title

#### Step 2: Choose a Theme (Optional)

If user requested a specific style:
1. Use Tool Finder: press `Alt+/`, type "theme", press Enter
2. Take snapshot to see available themes
3. Select an appropriate theme based on user's style preference
4. Wait 1-2 seconds for theme to apply

#### Step 3: Build Slides

For each slide in the plan:

**Title Slide (first slide):**
1. Click the title placeholder ("Click to add title")
2. Type the title
3. Click the subtitle placeholder ("Click to add subtitle")
4. Type the subtitle

**Content Slides:**
1. Create new slide: press `Ctrl+m`
2. Take snapshot to see the new slide layout
3. Click placeholders and type content
4. For additional text boxes: `Alt+/` then type "text box", Enter, then click-drag on canvas
5. Format text using keyboard shortcuts (see references/keyboard-shortcuts.md)

**Adding Elements:**

- **Text Box**: `Alt+/` -> "text box" -> Enter -> click-drag on canvas -> type content
- **Image (by URL)**: `Alt+/` -> "image" -> select "By URL" -> paste URL
- **Image (upload)**: `Alt+/` -> "image" -> select "Upload" -> use file upload
- **Shape**: `Alt+/` -> "shape" -> select shape type -> click-drag on canvas
- **Table**: `Alt+/` -> "table" -> select dimensions -> fill cells
- **Chart**: `Alt+/` -> "chart" -> select chart type
- **Video**: `Alt+/` -> "video" -> search or paste URL

**Formatting:**

Refer to `references/keyboard-shortcuts.md` for all formatting shortcuts. Key ones:
- Bold: `Ctrl+b`, Italic: `Ctrl+i`, Underline: `Ctrl+u`
- Font size: `Ctrl+Shift+>` / `Ctrl+Shift+<`
- Alignment: `Ctrl+Shift+l` (left), `Ctrl+Shift+e` (center), `Ctrl+Shift+r` (right)
- Lists: `Ctrl+Shift+8` (bullet), `Ctrl+Shift+7` (numbered)

**Arranging Objects:**
- Group: `Ctrl+Alt+g`
- Send backward/forward: `Ctrl+Down` / `Ctrl+Up`
- Send to back/front: `Ctrl+Shift+Down` / `Ctrl+Shift+Up`

#### Step 4: Add Speaker Notes (if requested)

1. Open speaker notes panel: `Ctrl+Alt+Shift+s`
2. Click the notes area
3. Type speaker notes

### Editing an Existing Presentation

1. Navigate to the provided Google Slides URL
2. Wait for editor to load
3. Take snapshot to understand current slide structure
4. Navigate to the target slide using filmstrip (Up/Down arrows)
5. Make requested changes using the same element interaction patterns above
6. Take screenshot after changes for verification

### Reading/Extracting Content

1. Navigate to the Google Slides URL
2. Take snapshot of each slide to read content
3. Navigate between slides using Page Down / Down arrow
4. Compile extracted text and structure
5. Present to user

### Exporting

1. Open the presentation in the editor
2. Use Tool Finder: `Alt+/`
3. Type the export format:
   - "PDF" for PDF download
   - "PowerPoint" for .pptx download
   - "PNG" for current slide as image
   - "JPEG" for current slide as image
   - "SVG" for current slide as vector
4. Press Enter to initiate download
5. Confirm download started

---

## Phase 4: Verification

After completing any operation:

1. Take a `browser_screenshot` of the final result
2. Show the screenshot to the user
3. Ask if any adjustments are needed
4. If the user wants changes, return to Phase 3 for the specific modifications

---

## Important Guidelines

### Reliability

- **Always snapshot before acting** - DOM state changes frequently
- **Prefer keyboard shortcuts over clicking** - More reliable than CSS selectors
- **Use Tool Finder (Alt+/) as fallback** - Can access any menu command by name
- **Wait after navigation** - Google Slides loads asynchronously; verify with snapshot

### Content Quality

When generating slide content:
- Keep bullet points concise (5-7 words per point)
- Limit to 5-6 bullet points per slide
- Use a clear visual hierarchy (title > subtitle > body)
- Suggest relevant images or diagrams where appropriate
- Match the tone to the audience (professional, casual, etc.)

### Error Handling

- If an element is not found in snapshot, try scrolling or navigating
- If a keyboard shortcut does not work, fall back to Tool Finder (Alt+/)
- If the page becomes unresponsive, try refreshing with `Ctrl+Shift+r`
- If a dialog appears unexpectedly, dismiss with `Escape`

### Reference Files

- `references/keyboard-shortcuts.md` - Complete keyboard shortcut reference for Google Slides
- `references/playwright-patterns.md` - Playwright-specific patterns, selectors, and automation strategies for Google Slides
