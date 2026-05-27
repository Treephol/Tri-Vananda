"""
Move each narrative explanation paragraph from the option text pages
to the corresponding sample artwork pages. Position top-left, larger scale.
Remove 'Sample artwork ·' prefix from the caption.
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── 1. ADD NEW CSS for top-left description overlay ─────────────────────
NEW_CSS = """
.artwork-description{position:absolute;top:80px;left:80px;right:auto;max-width:540px;font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(1.1rem,1.55vw,1.45rem);color:rgba(255,255,255,.92);line-height:1.5;letter-spacing:.005em;z-index:4;text-shadow:0 1px 14px rgba(11,15,19,.55)}
"""

# Insert before </style>
text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── 2. THE THREE NARRATIVE PARAGRAPHS ───────────────────────────────────
descriptions = {
    1: "PATTAMA is the beginning of meaningful living &mdash; where wellbeing is integrated into everyday life, relationships, nature, and time itself. Not escape. Living well, fully, and together.",
    2: "PATTAMA is the slow awakening of meaningful living &mdash; where the body, the table, the land, and the family rise together. Like the lotus, the practice emerges from depth, unfolds in light, and roots in everyday life. Not escape. A daily flowering.",
    3: "PATTAMA is a living tradition of meaningful living &mdash; heritage, family, the table, the land, the body, kept in practice by a family name across generations. Like Herm&egrave;s, Chanel, Bulgari, Soneva, Reschio, the family signs every standard. Not branding &mdash; a way of living, still lived.",
}

# ─── 3. REMOVE vyana-description from each narrative option text page ────
old_descriptions_in_pages = [
    '<div class="vyana-description">PATTAMA is the beginning of meaningful living &mdash; where wellbeing is integrated into everyday life, relationships, nature, and time itself. Not escape. Living well, fully, and together.</div>',
    '<div class="vyana-description">PATTAMA is the slow awakening of meaningful living &mdash; where the body, the table, the land, and the family rise together. Like the lotus, the practice emerges from depth, unfolds in light, and roots in everyday life. Not escape. A daily flowering.</div>',
    '<div class="vyana-description">PATTAMA is a living tradition of meaningful living &mdash; heritage, family, the table, the land, the body, kept in practice by a family name across generations. Like Herm&egrave;s, Chanel, Bulgari, Soneva, Reschio, the family signs every standard. Not branding &mdash; a way of living, still lived.</div>',
]

for old in old_descriptions_in_pages:
    if old in text:
        text = text.replace(old, "", 1)
        # Also clean up any leftover blank-line whitespace right after the removal
        print(f"  ✓ Removed description from narrative text page")
    else:
        print(f"  ⚠ Description not found: {old[:60]}...")

# ─── 4. ADD artwork-description to each artwork page ─────────────────────
# Each artwork page has the pattern:
#   <div class="artwork-bg" style="...narrative-NN.jpg..."></div>
#   <div class="artwork-overlay">...</div>
# We insert the artwork-description div right after the artwork-bg, before the overlay.

for n, paragraph in descriptions.items():
    image_file = f"narrative-0{n}.jpg"
    old_marker = f'<div class="artwork-bg" style="background-image:url(\'images/{image_file}\')"></div>'
    new_marker = f'<div class="artwork-bg" style="background-image:url(\'images/{image_file}\')"></div>\n  <div class="artwork-description">{paragraph}</div>'
    if old_marker in text:
        text = text.replace(old_marker, new_marker, 1)
        print(f"  ✓ Added artwork-description to artwork page for Option {n}")
    else:
        print(f"  ⚠ Could not find artwork-bg marker for Option {n}")

# ─── 5. REMOVE 'Sample artwork ·' prefix from caption ────────────────────
old_caption = 'Sample artwork &middot; The Narrative'
new_caption = 'The Narrative'
n_caps = text.count(old_caption)
text = text.replace(old_caption, new_caption)
print(f"  ✓ Captions updated (removed 'Sample artwork ·'): {n_caps}x")

V2.write_text(text)
print("\nDone.")
