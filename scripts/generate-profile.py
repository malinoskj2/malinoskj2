"""Build theme-aware README typography with an embedded animated sword."""

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets"
sword = 'data:image/gif;base64,' + base64.b64encode(
    (ROOT / 'sword-divider.gif').read_bytes()
).decode()

for theme, heading, body, blue in (
    ('latte', '#182147', '#74709e', '#064bea'),
    ('mocha', '#e2e7ff', '#aaa7cc', '#82aaff'),
):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="750" height="395" viewBox="0 0 750 395" role="img" aria-labelledby="title desc">
  <title id="title">Hi, I'm Jesse — software engineer in South Carolina</title>
  <desc id="desc">PHP, TypeScript, Rust, Java, Lua, Nix. Vue, Laravel, Docker, Wayland, Linux. Building things, configuring Linux, collecting pixels.</desc>
  <g text-anchor="middle" font-family="ui-monospace, 'JetBrains Mono', 'Fira Code', SFMono-Regular, Menlo, Consolas, monospace">
    <text x="347" y="101" fill="{heading}" font-size="50" font-weight="700">hi, i'm Jesse</text>
    <path d="M 585 65 C 563 63 552 83 562 98 C 570 111 589 111 599 97 C 580 104 571 82 585 65 Z" fill="#d98289"/>
    <text x="375" y="142" fill="{body}" font-size="21">software engineer · south carolina</text>
    <g fill="{heading}" font-size="21">
      <text x="375" y="205">PHP · TypeScript · Rust · Java · Lua · Nix</text>
      <text x="375" y="240">Vue · Laravel · Docker · Wayland · Linux</text>
    </g>
    <text x="375" y="358" fill="{body}" font-size="17">building things · configuring linux · collecting pixels</text>
  </g>
  <image href="{sword}" x="250" y="274" width="250" height="35"/>
  <g fill="#d98289">
    <path d="M 207 287 l 2 6 4 2 -4 2 -2 6 -2 -6 -4 -2 4 -2 Z"/>
    <path d="M 548 295 l 2 6 4 2 -4 2 -2 6 -2 -6 -4 -2 4 -2 Z"/>
  </g>
  <g fill="{blue}">
    <path d="M 233 298 l 1.5 4 3.5 1.5 -3.5 1.5 -1.5 4 -1.5 -4 -3.5 -1.5 3.5 -1.5 Z"/>
    <path d="M 524 280 l 1.5 4 3.5 1.5 -3.5 1.5 -1.5 4 -1.5 -4 -3.5 -1.5 3.5 -1.5 Z"/>
  </g>
</svg>
'''
    (ROOT / f'profile-framed-{theme}.svg').write_text(svg)
