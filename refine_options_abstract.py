"""
Refine Options 2 and 3:
- Positioning more abstract (no Garden/House imagery)
- Each line linked to meaningful living + the offerings
- Parallel structure to Option 1
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── OPTION 2 — THE LOTUS / AWAKENED LIVING ──────────────────────────────
swaps_opt2 = [
    # Positioning: A Garden of Awakening → A World of Quiet Awakening
    ('<div class="vyana-positioning">A Garden of Awakening</div>',
     '<div class="vyana-positioning">A World of Quiet Awakening</div>'),
    # Tagline: Living Well, in Quiet Bloom → Living Well, Awakening Together
    ('<div class="vyana-tagline">Living Well, in Quiet Bloom</div>',
     '<div class="vyana-tagline">Living Well, Awakening Together</div>'),
    # Sub-tagline
    ('<div class="vyana-strapline">Rooted in the depths, rising in light &mdash; for the multigenerational family.</div>',
     '<div class="vyana-strapline">The slow unfolding of meaningful life &mdash; for the multigenerational family.</div>'),
    # Meaning kept (paṭhama · padma · pathum)
    # Explanation rewritten to map to offering pillars
    ('<div class="vyana-description">The lotus opens first at dawn, before the rest of the garden &mdash; clean from muddy water, untouched by what surrounds it. It is the central image of Thai Buddhist awakening, the flower of the Buddha. PATTAMA carries this depth: firstness, unfolding, the quiet emergence from the depths. A way of living that opens itself, daily, to meaning.</div>',
     '<div class="vyana-description">PATTAMA is the slow awakening of meaningful living &mdash; where the body, the table, the land, and the family rise together. Like the lotus, the practice emerges from depth, unfolds in light, and roots in everyday life. Not escape. A daily flowering.</div>'),
]

# ─── OPTION 3 — THE FAMILY NAME / INHERITED LIVING ───────────────────────
swaps_opt3 = [
    # Positioning: A House of Stewardship → A World of Quiet Inheritance
    ('<div class="vyana-positioning">A House of Stewardship</div>',
     '<div class="vyana-positioning">A World of Quiet Inheritance</div>'),
    # Tagline kept: Living Well, Through the Generations
    # Sub-tagline
    ('<div class="vyana-strapline">The standards a family stewards &mdash; for the multigenerational family.</div>',
     '<div class="vyana-strapline">The inheritance of meaningful life &mdash; for the multigenerational family.</div>'),
    # Meaning rewrite — more philosophical
    ('<div class="vyana-etymology">Thai. Pattamasevi. The family name. The contract. The inheritance.</div>',
     '<div class="vyana-etymology">Thai. A family name. A promise across generations. An inheritance of meaningful living.</div>'),
    # Explanation rewrite — map to offering pillars
    ('<div class="vyana-description">Like the world&rsquo;s most enduring luxury houses &mdash; Herm&egrave;s, Chanel, Bulgari, Soneva, Reschio &mdash; PATTAMA carries a family name. Pattamasevi. The family becomes the contract: every standard the brand keeps is a standard the family signs. Not branding &mdash; a name handed down.</div>',
     '<div class="vyana-description">PATTAMA is the inheritance of meaningful living &mdash; heritage, family, the table, the land, the body, held by a name across generations. Like Herm&egrave;s, Chanel, Bulgari, Soneva, Reschio, the family signs every standard. Not branding &mdash; a way of living protected.</div>'),
]

for old, new in swaps_opt2 + swaps_opt3:
    if old in text:
        text = text.replace(old, new, 1)
        print(f"  ✓ {old[:60]}...")
    else:
        print(f"  ⚠ NOT FOUND: {old[:60]}...")

V2.write_text(text)
print("\nDone.")
