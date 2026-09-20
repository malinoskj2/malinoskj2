import base64, io, sys
from PIL import Image

W, H = 1800, 500
NAME = {"mocha": "#f5e0dc", "latte": "#303446"}
C = {
    "mocha": dict(text="#cdd6f4", sub="#bac2de", line="#45475a", dim="#6c7086", green="#a6e3a1", term="#181825", scrim="#11111b"),
    "latte": dict(text="#4c4f69", sub="#5c5f77", line="#acb0be", dim="#9ca0b0", green="#40a02b", term="#eff1f5", scrim="#eff1f5"),
}
WORDS = ["rust", "nix", "lua", "laravel", "wayland", "sched_ext"]

def banner(src, yoff):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    ch = round(w * H / W)
    top = max(0, min(h - ch, (h - ch) // 2 + yoff))
    im = im.crop((0, top, w, top + ch)).resize((W, H), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "WEBP", quality=88, method=6)
    return base64.b64encode(buf.getvalue()).decode()

for flavor, src, yoff in [("mocha", sys.argv[1], int(sys.argv[3])), ("latte", sys.argv[2], int(sys.argv[4]))]:
    c = C[flavor]; name = NAME[flavor]
    per = 2.4; total = len(WORDS) * per
    cycle = "".join(
        f'      <text x="94" y="198" font-size="15" fill="{c["text"]}" opacity="0">{w}'
        f'<tspan>▍<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan>'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.85;1" dur="{per}s" begin="{i * per}s;cycle.end+{i * per}s" fill="freeze"/></text>\n'
        for i, w in enumerate(WORDS))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="900" height="250" viewBox="0 0 900 250" role="img" aria-label="Jesse Malinosky — software engineer">
  <defs>
    <linearGradient id="scrim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c["scrim"]}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{c["scrim"]}" stop-opacity="0.55"/>
      <stop offset="1" stop-color="{c["scrim"]}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="card"><rect width="900" height="250" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#card)">
    <image width="900" height="250" preserveAspectRatio="xMidYMid slice" xlink:href="data:image/webp;base64,{banner(src, yoff)}"/>
    <rect width="560" height="250" fill="url(#scrim)"/>
  </g>
  <rect x="0.5" y="0.5" width="899" height="249" rx="18" fill="none" stroke="{c["line"]}"/>

  <rect x="60" y="150" width="440" height="64" rx="10" fill="{c["term"]}" opacity="0.92" stroke="{c["line"]}"/>
  <circle cx="78" cy="166" r="4" fill="#f38ba8"/>
  <circle cx="91" cy="166" r="4" fill="#f9e2af"/>
  <circle cx="104" cy="166" r="4" fill="#a6e3a1"/>

  <g font-family="ui-monospace, 'JetBrains Mono', 'Fira Code', SFMono-Regular, Menlo, Consolas, monospace">
    <text x="60" y="90" font-size="52" font-weight="700" fill="{name}" letter-spacing="-1">Jesse Malinosky</text>
    <text x="62" y="122" font-size="15" fill="{c["sub"]}">software engineer · south carolina</text>

    <text x="74" y="198" font-size="15" fill="{c["green"]}">❯</text>
    <text x="94" y="198" font-size="15" fill="{c["dim"]}" opacity="0"><set id="cycle" attributeName="opacity" to="0" dur="{total}s" begin="0s;cycle.end"/></text>
{cycle}  </g>
</svg>
'''
    open(f"assets/header-{flavor}.svg", "w").write(svg)
    print(flavor, len(svg))
