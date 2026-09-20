# Foliage border

Generated with the built-in imagegen tool, using `knight-moon.png` for print texture and the supplied William Morris poetry-page reference for the botanical forms.

## Final prompt

Use case: stylized-concept. Create a transparent PNG decorative botanical top border for a personal GitHub README. Wide shallow 4:1 composition. Image 1 (knight) is reference for hand-inked, etched and weathered print technique. Image 2 (William Morris illuminated poetry pages) is the PRIMARY reference for botanical design: delicate sinuous branching vines, many tiny narrow pointed leaves, intricately interwoven stems, a few tiny muted rose buds. Foliage enters from the extreme top-left and top-right corners and curls gently downward along both outer edges, tapering inward. Each corner cluster occupies only the outermost 28 percent of width, central 44 percent remains completely transparent for breathing room. Airy organic asymmetrical fine tracery, miniature manuscript botanical ornament, NOT large broad leaves, NOT chunky branches. Colors subdued sage green leaves, dusty pale rose tiny buds, muted warm parchment highlights and charcoal ink fine outlines. Match knight's analog printed texture but use Morris botanical forms. Branches touch and are cropped by top and side edges. No text, no lettering, no paper, no rectangle, no background, no knight, no moon. Genuine alpha transparency everywhere between branches and in large open center. Final asset only.

## Integration

Run `python3 assets/frame.py` to rebuild both self-contained SVG headers from the foliage PNG and existing animated knight and sword assets. Then run `./build.sh` to preview the README.
