"""
Fix: pre-research pages (02-08) shouldn't use 'Culture' framing — that's the post-research tagline.
Replace pre-research 'culture' → 'Collective' (the positioning).
Post-research instances stay (they're the tagline).
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# Strings to replace (pre-research only — each unique to its location):
replacements = [
    # Page 03 (Timeline) — small label under NWB Development
    ("New Wellness Brand Development<small>Culture, naming &amp; identity</small>",
     "New Wellness Brand Development<small>Brand, naming &amp; identity</small>"),
    # Page 04 (Brand Pillars) — Tri Vananda card
    ("The only place in the culture where it is own-able",
     "The only place in the Collective where it is own-able"),
    # Page 04 (Brand Pillars) — CLP card
    ("signing the culture&rsquo;s clinical and longevity protocols",
     "signing the Collective&rsquo;s clinical and longevity protocols"),
    # Page 06 (Brand Script) — Plan step One
    ("Step into the culture through whichever door fits the family",
     "Step into the Collective through whichever door fits the family"),
    # Page 06 (Brand Script) — Plan step Three header
    ("Three &middot; Live the culture",
     "Three &middot; Live the Collective"),
    ("Three · Live the culture",
     "Three · Live the Collective"),
    # Page 07 (Org Structure) — Tri Vananda sub-card
    ("the residential expression of the culture",
     "the residential expression of the Collective"),
    # Page 08 — section comment
    ("═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE CULTURE ═══════════════════",
     "═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════"),
    # Page 08 — eye text
    ('<div class="eye">New Wellness Brand Development · The Culture</div>',
     '<div class="eye">New Wellness Brand Development · The Collective</div>'),
    # Page 08 — body paragraph
    ("The culture takes a different form at every age",
     "The Collective takes a different form at every age"),
]

# Apply unique replacements
miss = []
for old, new in replacements:
    if old in text:
        text = text.replace(old, new, 1)
    else:
        miss.append(old[:60])

# CSS comments (duplicate — use replace_all-equivalent)
text = text.replace("/* ───── CULTURE OFFERINGS GRID ───── */",
                    "/* ───── COLLECTIVE OFFERINGS GRID ───── */")

HTML_PATH.write_text(text)

for m in miss:
    print(f"  ⚠ not found: {m}...")
print("Done.")
