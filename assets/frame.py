"""Build self-contained README headers; embedded GIFs retain their animation."""

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def embedded(name, mime):
    return f"data:{mime};base64,{base64.b64encode((ROOT / name).read_bytes()).decode()}"


foliage = embedded("foliage-border.png", "image/png")
knight = embedded("moon-knight-ribbon.gif", "image/gif")
sword = embedded("sword-divider.gif", "image/gif")

for theme, heading, body in (
    ("latte", "#303446", "#6c6f85"),
    ("mocha", "#f5e0dc", "#a6adc8"),
):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="420" viewBox="0 0 1000 420" role="img" aria-labelledby="title desc">
  <title id="title">Hi, I'm Jesse — software engineer in South Carolina</title>
  <desc id="desc">PHP, TypeScript, Rust, Java, Lua, Nix. Vue, Laravel, Docker, Wayland, Linux. Building things, configuring Linux, collecting pixels. A crescent and tiny stars echo the moonlit knight within a leafy frame.</desc>
  <image href="{foliage}" x="0" y="0" width="1000" height="400" preserveAspectRatio="none"/>
  <image href="{knight}" x="730" y="74" width="178" height="300"/>
  <g text-anchor="middle" font-family="ui-monospace, 'JetBrains Mono', 'Fira Code', SFMono-Regular, Menlo, Consolas, monospace">
    <text x="423" y="153" fill="{heading}" font-size="38" font-weight="700">hi, i'm Jesse</text>
    <path d="M 598 127 A 13 13 0 1 0 608 148 A 12 12 0 0 1 598 127 Z" fill="#d99b9f"/>
    <path d="M 414 168 H 466" stroke="{'#1646ac' if theme == 'latte' else '#82aaff'}" stroke-width="2" stroke-linecap="round"/>
    <text x="440" y="199" fill="{body}" font-size="17">software engineer · south carolina</text>
    <g fill="{body}" font-size="16">
      <text x="440" y="240">PHP · TypeScript · Rust · Java · Lua · Nix</text>
      <text x="440" y="266">Vue · Laravel · Docker · Wayland · Linux</text>
    </g>
    <text x="440" y="345" fill="{body}" font-size="12">building things · configuring linux · collecting pixels</text>
  </g>
  <image href="{sword}" x="300" y="291" width="280" height="32"/>
  <g fill="#d99b9f">
    <path d="M 275 299 l 2 6 6 2 -6 2 -2 6 -2 -6 -6 -2 6 -2 Z"/>
    <path d="M 607 291 l 1.5 4.5 4.5 1.5 -4.5 1.5 -1.5 4.5 -1.5 -4.5 -4.5 -1.5 4.5 -1.5 Z"/>
    <path d="M 588 318 l 1 3 3 1 -3 1 -1 3 -1 -3 -3 -1 3 -1 Z"/>
  </g>
</svg>
'''
    (ROOT / f"profile-framed-{theme}.svg").write_text(svg)
