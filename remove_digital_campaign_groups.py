"""
Remove pages 23-25 (Digital Campaign Sample · Groups A, B, C — Ad, Landing Page, Social Media).
Keep the intro page (22).
Renumber subsequent pages 26-33 → 23-30.
"""

from pathlib import Path
import re

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# Find and remove the three group sections (A, B, C)
group_anchors = [
    "<!-- ═══════════════════ NEW WELLNESS BRAND · DIGITAL CAMPAIGN · GROUP A · AD ═══════════════════ -->",
    "<!-- ═══════════════════ NEW WELLNESS BRAND · DIGITAL CAMPAIGN · GROUP B · LANDING PAGE ═══════════════════ -->",
    "<!-- ═══════════════════ NEW WELLNESS BRAND · DIGITAL CAMPAIGN · GROUP C · SOCIAL MEDIA ═══════════════════ -->",
]

# Find boundaries and remove
removed = 0
for i, anchor in enumerate(group_anchors):
    if anchor not in text:
        print(f"⚠ Anchor not found: {anchor[:50]}...")
        continue
    start_idx = text.index(anchor)
    # Find the </section> after this anchor
    section_end_pattern = '</section>'
    end_idx = text.index(section_end_pattern, start_idx) + len(section_end_pattern)
    text = text[:start_idx] + text[end_idx + 1:]  # +1 to remove trailing newline
    removed += 1
    print(f"  Removed Group {chr(65+i)} ({anchor[60:90]}...)")

print(f"\nTotal sections removed: {removed}")

# Clean up any consecutive blank lines
text = re.sub(r'\n{3,}', '\n\n', text)

# Renumber subsequent pages 26-33 → 23-30
for old, new in [(26, 23), (27, 24), (28, 25), (29, 26), (30, 27), (31, 28), (32, 29), (33, 30)]:
    text = text.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')

HTML_PATH.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"\nSections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
