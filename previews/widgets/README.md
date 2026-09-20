# Profile widget previews

Five alternatives implemented in separate Git worktrees by subagents. Screenshots show each widget below the existing profile in light and dark appearances. Open [the visual gallery](index.html) locally to compare.

| Widget | Branch / commit | Dark | Light |
| --- | --- | --- | --- |
| Moon dial | `widgets/moon-dial` / `aac7db2` | [Screenshot](moon-dial-dark.png) | [Screenshot](moon-dial-light.png) |
| Copy my theme | `widgets/theme` / `b310d8a` | [Screenshot](palette-dark.png) | [Screenshot](palette-light.png) |
| Code search shrine | `widgets/discovery` / `5127196` | [Screenshot](code-search-dark.png) | [Screenshot](code-search-light.png) |
| Lunar bookmark | `widgets/bookmark` / `b156bc5` | [Screenshot](lunar-bookmark-dark.png) | [Screenshot](lunar-bookmark-light.png) |
| Theme workbench | `widgets/workbench` / `860d931` | [Screenshot](workbench-dark.png) | [Screenshot](workbench-light.png) |

## Worktrees

- **Moon dial:** `../../../malinoskj2-moon-dial` — Timezone-aware South Carolina snapshot, hourly refresh workflow, and live-clock link.
- **Copy my theme:** `../../../malinoskj2-theme` — Profile palette with Kitty and VS Code workspace downloads.
- **Code search shrine:** `../../../malinoskj2-discovery` — Three scoped searches across public GitHub code.
- **Lunar bookmark:** `../../../malinoskj2-bookmark` — Configurable linked resource card; NixOS package search is a curated example.
- **Theme workbench:** `../../../malinoskj2-workbench` — README preview and interactive local page with working appearance/app selection, clipboard, and downloads.

The workbench branch builds on the palette branch. All changes are committed locally; no branches are pushed or merged. The main profile README is unchanged.

## Interactive workbench

Screenshots: [dark](workbench-page-dark.png), [light](workbench-page-light.png), [mobile](workbench-page-mobile.png).

Run from the project directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory ../malinoskj2-workbench
```

Open http://127.0.0.1:8000/widgets/theme/. The page is ready for static hosting but has not been deployed.

## Verification

Chromium verified both appearances, all four theme downloads, app switching, copying hex values, and mobile layout without horizontal overflow or JavaScript errors. SVG parsing, search query encoding, generator checks, and DST boundary checks passed. All ten profile screenshots loaded without broken images.

Profile previews use the existing Grip GitHub styles with original Markdown/picture markup rendered locally; these are browser previews, not screenshots of a published GitHub profile.
