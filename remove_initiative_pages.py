"""
Remove 7 initiative pages (14-20):
  - Marketing Collateral Preparation
  - Renovated Trisara Wellness Launch
  - Pru Farm Festival
  - Join GWS as Exhibitor
  - Hosted Experience
  - PR Campaign
  - Founding Industry Network

Renumber subsequent pages. Continuing Communications, Summary, End Card stay.
"""

from pathlib import Path
import re

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# Section comment anchors that mark each initiative page to remove
section_anchors = [
    "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->",
    "<!-- ═══════════════════ 24 LAUNCH — RENOVATED TRIPATTAMA WELLNESS ═══════════════════ -->",
    "<!-- ═══════════════════ 17 SUPPORTING ACTIVATION — PRU FARM FESTIVAL ═══════════════════ -->",
    "<!-- ═══════════════════ 13 KEY ACTIVATION — JOIN GWS AS EXHIBITOR ═══════════════════ -->",
    "<!-- ═══════════════════ 14 KEY ACTIVATION — HOSTED EXPERIENCE ═══════════════════ -->",
    "<!-- ═══════════════════ 14X INITIATIVE — PR CAMPAIGN ═══════════════════ -->",
    "<!-- ═══════════════════ 15 INITIATIVE — FOUNDING INDUSTRY NETWORK ═══════════════════ -->",
]

removed = 0
for anchor in section_anchors:
    if anchor not in text:
        print(f"  ⚠ Not found: {anchor[:60]}...")
        continue
    start = text.index(anchor)
    end = text.index("</section>", start) + len("</section>")
    # Include trailing newline
    if text[end:end+1] == "\n":
        end += 1
    text = text[:start] + text[end:]
    removed += 1
    print(f"  ✓ Removed: {anchor[60:120]}")

print(f"\nRemoved {removed} sections.")

# Clean any consecutive blank lines
text = re.sub(r'\n{3,}', '\n\n', text)

# Renumber pages — sequential from 05 (or 04) onward
text_before, _, text_after = text.partition('<div class="pg">04</div>')
pattern = re.compile(r'<div class="pg">(\d{2})</div>')
counter = [4]
def repl(m):
    counter[0] += 1
    return f'<div class="pg">{counter[0]:02d}</div>'
text_after_renumbered = pattern.sub(repl, text_after)
text = text_before + '<div class="pg">04</div>' + text_after_renumbered

V2.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"\nFinal: Sections {sections} open / {closes} close, Page tags {pgs}")
