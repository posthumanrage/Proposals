## Current State and Next Steps for HTML Layout Refactoring

We have successfully created two dummy build note files: `build_notes_2025-09-28_v1.md` and `build_notes_2025-09-29_v2.md`.

The current objective is to refactor `html.html` to implement a two-pane layout. This layout will feature a left-hand menu displaying a list of build note extracts (filename and modification date/time) and a right-hand pane that will show the content of the selected build note.

**Next Steps:**

1.  **Extract Content**: Extract the existing content of the `<header>`, `<main>`, and `<footer>` tags from `html.html`.
2.  **Construct New `<body>`**: Build the new `<body>` content, incorporating a `main-layout` container. Inside `main-layout`, create an `<aside class="left-menu">` for the build notes list and a `<div class="right-content">` to house the extracted `<header>`, `<main>`, and `<footer>` content.
3.  **Replace `<body>` Tag**: Replace the entire `<body>` tag in `html.html` with this newly constructed two-pane structure.
4.  **Add CSS for Layout**: Define CSS rules for `.main-layout`, `.left-menu`, and `.right-content` to establish the two-pane visual structure.
5.  **Add JavaScript for Functionality**: Implement JavaScript to:
    *   Use the `glob` tool to find all `build_notes_*.md` files.
    *   Dynamically populate the `<ul id="build-notes-list">` in the `left-menu` with the filename and modification date/time of each build note.
    *   Add event listeners to these list items so that clicking a build note loads its content (using `read_file`) into the `<main>` section of the `right-content` pane.