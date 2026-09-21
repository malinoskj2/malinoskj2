"""Apply the repository preview shell and synchronize its GitHub theme."""

import re
import sys
from pathlib import Path

page = Path(sys.argv[1])
html = page.read_text()
# A picture's img must be a direct child for native source selection to work.
# Grip's automatic image links otherwise leave the fallback image selected.
html = re.sub(
    r'(<picture>)(.*?)(</picture>)',
    lambda match: match[1] + re.sub(r'<a\b[^>]*>(\s*<img\b[^>]*>\s*)</a>',
                                  r'\1', match[2]) + match[3],
    html,
    flags=re.S,
)
style = '''<style id="readme-preview-style">
html { color-scheme: light dark; }
body { margin: 0; background: var(--bgColor-default, #fff); color: var(--fgColor-default, #182147); }
.preview-page { margin: 20px auto; }
.container-xl { max-width: 1200px; }
#readme { border: 1px solid var(--borderColor-default, #d0d7de); border-radius: 6px; }
#readme .Box-header { padding: 24px 26px 20px; }
#readme .Box-title { font: 14px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-weight: 400; }
#readme .Box-body { padding: 0 26px 26px !important; }
#grip-content { font-size: 16px; }
#grip-content a { color: var(--fgColor-accent, #0969da); text-decoration: none; }
#grip-content a:hover { text-decoration: underline; }
#grip-content img { background: transparent; }
@media (max-width: 600px) {
  #readme .Box-header { padding: 16px 12px; }
  #readme .Box-body { padding: 0 12px 16px !important; }
}
</style>
<script>
// Grip omits GitHub's theme initialization. Keep page colors and picture sources in sync.
const previewScheme = window.matchMedia('(prefers-color-scheme: dark)');
function syncPreviewTheme() {
  document.documentElement.dataset.colorMode = previewScheme.matches ? 'dark' : 'light';
}
syncPreviewTheme();
previewScheme.addEventListener('change', syncPreviewTheme);
</script>'''
html = html.replace('</head>', style + '\n</head>')
html = re.sub(r'(<h2 class="Box-title">)\s*README.md\s*(</h2>)',
              r'\1malinoskj2 / README.md\2', html)
page.write_text(html)
