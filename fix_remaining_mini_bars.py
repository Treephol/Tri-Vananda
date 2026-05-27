"""Convert remaining 6-cell mini-bars to 4 cells.
These had inline styles on the summit cell that didn't match my earlier patterns."""

from pathlib import Path
import re

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# Pattern: summit-only activations (Pru Farm Festival, GWS Exhibitor, Hosted Experience)
# 6 cells: off, off, off, off, summit(inline-styled), off
# Convert to 4 cells: off, off, off, on
summit_only_old = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell summit" style="background:linear-gradient(90deg,var(--gold) 0%,var(--gold-lt) 100%)"></div>
          <div class="init-mini-cell"></div>
"""
summit_only_new = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on" style="background:linear-gradient(90deg,var(--gold) 0%,var(--gold-lt) 100%)"></div>
"""

n = text.count(summit_only_old)
text = text.replace(summit_only_old, summit_only_new)
print(f"✓ Summit-only mini-bars converted: {n}")

# Pattern: PR Campaign (Aug-Jan) — active Aug onwards
# Look at what it actually is. Find by context.
# 6 cells: off, off, on, on, summit(inline-styled), on
pr_old_variant1 = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell summit" style="background:linear-gradient(90deg,var(--gold) 0%,var(--gold-lt) 100%)"></div>
          <div class="init-mini-cell on"></div>
"""
pr_new = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
"""
n2 = text.count(pr_old_variant1)
text = text.replace(pr_old_variant1, pr_new)
print(f"✓ PR Campaign mini-bar converted: {n2}")

# Pattern: Nov-Jan items (Founding Industry Network, Continuing Communications)
# 6 cells: off, off, off, off, summit(inline-styled), on
nov_jan_old = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell summit" style="background:linear-gradient(90deg,var(--gold) 0%,var(--gold-lt) 100%)"></div>
          <div class="init-mini-cell on"></div>
"""
nov_jan_new = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
"""
n3 = text.count(nov_jan_old)
text = text.replace(nov_jan_old, nov_jan_new)
print(f"✓ Nov-Jan mini-bars converted: {n3}")

HTML_PATH.write_text(text)

# Check if any 6-cell mini-bars remain
mini_bar_blocks = re.findall(r'<div class="init-mini-bar">(.*?)</div>', text, flags=re.DOTALL)
for i, block in enumerate(mini_bar_blocks):
    cell_count = block.count('<div class="init-mini-cell')
    if cell_count != 4:
        # Find the context
        idx = text.find(block)
        if idx > 0:
            # Look backward for the initiative name
            chunk = text[max(0, idx-300):idx]
            name_match = re.search(r'init-name[^>]*>([^<]+)<', chunk)
            name = name_match.group(1) if name_match else "(unknown)"
            print(f"⚠ Mini-bar with {cell_count} cells found near: {name.strip()}")
