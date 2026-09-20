Build tools live here. The current README artwork lives in `assets/`, and the
generated preview lives in `build/`.

Run from the repository root:

```sh
./scripts/build.sh
```

Requires Python and either Grip or Nix. The build renders the README, applies preview styling, and copies the assets into
`build/`. Open `build/index.html` to preview the result.

- `style-preview.py`: applies the preview shell and synchronizes light/dark themes.
