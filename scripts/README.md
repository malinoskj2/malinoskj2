Build tools live here. The current README artwork lives in `assets/`, and the
generated preview lives in `build/`.

Run from the repository root:

```sh
./scripts/build.sh
```

Requires Python and either Grip or Nix. The build regenerates both SVGs,
renders the README, applies preview styling, and copies the assets into
`build/`. Open `build/index.html` to preview the result.

- `generate-profile.py`: generates the light/dark SVGs with the embedded animated sword.
- `style-preview.py`: applies the preview shell and synchronizes light/dark themes.
