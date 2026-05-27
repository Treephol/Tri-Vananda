"""
Remove the entire 30-Brand Identity Study section from V2:
- Cover ('A research of world-class brands in the industry.')
- 10 Category pages
- 3 Synthesis pages (Overview / Visual / Verbal)

Renumber subsequent pages.
"""

from pathlib import Path
import re

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── BOUNDARIES OF THE 30-BRAND IDENTITY STUDY SECTION ───────────────────
start_anchor = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND · 30-BRAND IDENTITY STUDY · COVER ═══════════════════ -->"
# We remove everything from this comment up to (but not including) the Marketing Collateral comment.
end_anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"

if start_anchor not in text:
    raise RuntimeError("Cannot find 30-Brand Study cover anchor")
if end_anchor not in text:
    raise RuntimeError("Cannot find Marketing Collateral anchor")

start_idx = text.index(start_anchor)
end_idx = text.index(end_anchor)

removed_chars = end_idx - start_idx
print(f"Removing {removed_chars:,} chars (the 30-Brand Identity Study section)")

# Count how many sections we're removing
removed_block = text[start_idx:end_idx]
removed_sections = removed_block.count("<section")
removed_pgs = removed_block.count('<div class="pg">')
print(f"  Sections removed: {removed_sections}")
print(f"  Page tags removed: {removed_pgs}")

# Apply removal
text = text[:start_idx] + text[end_idx:]

# ─── RENUMBER pages from current page 5 onward ───────────────────────────
text_before, _, text_after_pg4 = text.partition('<div class="pg">04</div>')
pattern = re.compile(r'<div class="pg">(\d{2})</div>')
counter = [4]
def repl(m):
    counter[0] += 1
    return f'<div class="pg">{counter[0]:02d}</div>'
text_after_renumbered = pattern.sub(repl, text_after_pg4)
text = text_before + '<div class="pg">04</div>' + text_after_renumbered

V2.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"\nFinal: Sections {sections} open / {closes} close, Page tags {pgs}")
