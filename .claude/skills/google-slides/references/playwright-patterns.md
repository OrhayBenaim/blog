# Playwright Patterns for Google Slides Automation

## Core Strategy

Google Slides is a complex web app with dynamically generated DOM. Rely on these approaches in order of preference:

1. **Keyboard shortcuts** - Most reliable, not affected by DOM changes
2. **Tool Finder (Alt + /)** - Search menus by text, works for any command
3. **ARIA roles and labels** - Accessibility tree is more stable than CSS selectors
4. **Snapshots** - Use `browser_snapshot` to understand current page state before acting

## Authentication Detection

### Login Page Indicators
To detect if user needs to log in, take a snapshot and look for:
- Text containing "Sign in" or "Google Account"
- Email input fields
- "Use another account" buttons
- URL containing `accounts.google.com`

### Logged-In Indicators
- URL contains `docs.google.com/presentation`
- Presence of toolbar, filmstrip, or slide canvas
- Menu bar with File, Edit, View, Insert, etc.

## Page States

### Blank Presentation (New)
- URL: `docs.google.com/presentation/d/NEW_ID/edit`
- Contains: Empty slide with "Click to add title" and "Click to add subtitle" placeholders

### Existing Presentation
- URL: `docs.google.com/presentation/d/EXISTING_ID/edit`
- Contains: Slides in filmstrip, content in canvas

### Presentation Mode
- Fullscreen slide view
- Exit with Escape

## Navigation Patterns

### Creating a New Presentation
1. Navigate to `https://docs.google.com/presentation/create`
2. Wait for editor to load (look for canvas/filmstrip in snapshot)
3. Presentation opens with a blank title slide

### Opening Existing Presentation
1. Navigate to `https://docs.google.com/presentation/d/{PRESENTATION_ID}/edit`
2. Wait for content to load

### Creating Slides
- New blank slide: Press `Ctrl+m`
- Duplicate current: Press `Ctrl+d`
- To select a layout for the new slide: After Ctrl+m, right-click the slide in filmstrip and select "Apply layout"

## Interacting with Slide Content

### Clicking on Placeholders
1. Use `browser_snapshot` to see current accessibility tree
2. Look for elements with text "Click to add title" or "Click to add subtitle"
3. Click the placeholder element
4. Type content directly

### Adding Text Boxes
1. Use Tool Finder: Press keyboard shortcut `Alt+/`
2. Type "text box" and press Enter
3. Click and drag on the canvas to place the text box
4. Type content

### Adding Shapes
1. Use Tool Finder: `Alt+/` then type "shape"
2. Or use Insert menu: `Alt+i` then navigate to Shapes
3. Select desired shape
4. Click and drag on canvas to place

### Adding Images
1. Use Tool Finder: `Alt+/` then type "image"
2. Select source (Upload, By URL, Search, Drive, Photos, Camera)
3. For URL: paste the image URL
4. For Upload: use file upload dialog

### Adding Tables
1. Use Tool Finder: `Alt+/` then type "table"
2. Select table dimensions from the grid
3. Click cells to add content, Tab to move between cells

## Text Formatting Workflow

1. Select text (Shift + arrow keys, or Ctrl+a for all)
2. Apply formatting via keyboard shortcuts:
   - Bold: Ctrl+b
   - Italic: Ctrl+i
   - Font size: Ctrl+Shift+> / Ctrl+Shift+<
   - Alignment: Ctrl+Shift+l/r/e/j
3. For advanced formatting (font family, color), use Tool Finder:
   - `Alt+/` then type "font" for font picker
   - `Alt+/` then type "text color" for color picker

## Slide Themes and Layouts

### Changing Theme
1. Use Tool Finder: `Alt+/` then type "theme"
2. Or click "Theme" button in toolbar
3. Select from available themes in the sidebar

### Changing Slide Layout
1. Right-click slide in filmstrip
2. Select "Apply layout"
3. Choose from: Title Slide, Section Header, Title and Body, Title Only, One Column Text, Main Point, Section Title and Description, Caption, Big Number, Blank

## Exporting

### Download as PDF
1. File menu: `Alt+f`
2. Navigate to "Download" submenu
3. Select "PDF document (.pdf)"
4. Or use Tool Finder: `Alt+/` then type "PDF"

### Download as PPTX
1. File menu: `Alt+f` then "Download"
2. Select "Microsoft PowerPoint (.pptx)"
3. Or use Tool Finder: `Alt+/` then type "PowerPoint"

### Download as PNG/JPEG (current slide)
1. File menu: `Alt+f` then "Download"
2. Select image format

## Waiting and Timing

### Key Wait Points
- After navigation: Wait for slide canvas to appear in snapshot
- After inserting elements: Brief pause (500ms) for DOM to update
- After typing: Content appears immediately, no wait needed
- After theme change: Wait 1-2s for theme to apply
- After file operations: Wait for dialog/download to complete

### Detecting Loading States
- Look for "Loading..." text in snapshots
- Check for spinning indicators
- Canvas area being empty vs having content

## Error Recovery

### Common Issues
- **Element not found**: Take a fresh snapshot, DOM may have changed
- **Click missed target**: Use snapshot to verify element positions, try keyboard alternative
- **Dialog blocking**: Check for unexpected dialogs (share, save, etc.), dismiss with Escape
- **Slow loading**: Increase wait times, check network state

### Best Practice: Always Snapshot Before Acting
Before any complex interaction:
1. Take a `browser_snapshot`
2. Verify the expected UI state
3. Identify the correct element to interact with
4. Perform the action
5. Snapshot again to verify result
