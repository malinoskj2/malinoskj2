Edit `profile.json` to change the heading, subtitle, language/tool lists, footer,
links, or artwork descriptions. Then run:

```sh
./scripts/build.sh
```

Requires Python and either Grip or Nix. The build generates `README.md` and the
light/dark text SVGs, renders the README, applies preview styling, and copies
assets into `build/`. Open `build/index.html` to preview the result.

- `generate-profile.py`: generates README markup and header/footer SVGs from `profile.json`, using only the Python standard library.
- `style-preview.py`: applies the preview shell and synchronizes light/dark themes.

The sword and knight remain standalone GIFs referenced directly by the README.
Neither animation is embedded in an SVG. Generated artwork lives in `assets/`;
build tools live here. To regenerate the README without building the HTML preview,
run `python scripts/generate-profile.py`.
