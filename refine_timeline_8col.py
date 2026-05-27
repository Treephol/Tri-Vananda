"""
Refine timeline to 8 sub-columns for sub-month precision:
- Each named period (May-Jun, Jul-Aug, Sep-Oct, Nov-Dec) now spans 2 sub-columns
- PR Campaign and Pre-Summit Setup now start at half of Jul-Aug block (i.e., Aug = sub-col 4)
- Pre-Summit Setup reverts to Aug-Oct
- Pre-Summit Setup and GWS Exhibitor now share row 5 (no overlap; setup ends Oct, exhibitor Nov)
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── 1. UPDATE CSS — grid template columns from 4 to 8 ───────────────────
text = text.replace(
    ".tlx{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(184,148,88,.14);border:1px solid rgba(184,148,88,.18);position:relative}",
    ".tlx{display:grid;grid-template-columns:repeat(8,1fr);gap:1px;background:rgba(184,148,88,.14);border:1px solid rgba(184,148,88,.18);position:relative}"
)
text = text.replace(
    ".tlx-axis{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;border-top:1px solid rgba(184,148,88,.32)}",
    ".tlx-axis{display:grid;grid-template-columns:repeat(8,1fr);gap:1px;border-top:1px solid rgba(184,148,88,.32)}"
)

# Mini-bar grids — also 4-col → 8-col for consistency
text = text.replace(
    ".init-mini-bar{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(184,148,88,.14)}",
    ".init-mini-bar{display:grid;grid-template-columns:repeat(8,1fr);gap:1px;background:rgba(184,148,88,.14)}"
)
text = text.replace(
    ".init-mini-axis{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;margin-top:8px}",
    ".init-mini-axis{display:grid;grid-template-columns:repeat(8,1fr);gap:1px;margin-top:8px}"
)

# ─── 2. REBUILD THE TIMELINE BAR BLOCK ──────────────────────────────────
old_block_marker_start = '      <!-- Row 1 · NWB Dev (May-Jun) + Marketing Collateral (Jul-Oct) + Continuing Comms (Nov-Dec) -->'
old_block_marker_end = '    <div class="tlx-axis">'

start_idx = text.index(old_block_marker_start)
end_idx = text.index(old_block_marker_end)

new_bars = """      <!-- Row 1 · NWB Dev May-Jul (sub-cols 1-3) + Marketing Collateral Aug-Oct (4-6) + Continuing Comms Nov-Dec (7-8) -->
      <div class="tlx-bar fill" style="grid-row:1;grid-column:1 / span 3">New Wellness Brand Development<small>Brand, naming &amp; identity</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:4 / span 3">Marketing Collateral Preparation<small>Renderings · photos · videos · masterplan model</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:7 / span 2">Continuing Communications<small>Luxury Wellness Lifestyle Brand</small></div>
      <!-- Row 2 · Renovated Trisara Wellness Launch (Sep-Oct, sub-cols 5-6) -->
      <div class="tlx-bar" style="grid-row:2;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill launch" style="grid-row:2;grid-column:5 / span 2">Renovated Trisara Wellness<small>Launch &middot; Sep &ndash; Oct</small></div>
      <div class="tlx-bar" style="grid-row:2;grid-column:7 / span 2"></div>
      <!-- Row 3 · PR Agency Selection May-Jul (1-3) + PR Campaign Aug-Dec (4-8) -->
      <div class="tlx-bar fill" style="grid-row:3;grid-column:1 / span 3">PR Agency Selection<small>Closed shortlist · 3 months</small></div>
      <div class="tlx-bar fill" style="grid-row:3;grid-column:4 / span 5">PR Campaign<small>Sustained Aug – Dec 2026</small></div>
      <!-- Row 4 · Pru Farm Festival 1 Nov (sub-col 7) -->
      <div class="tlx-bar" style="grid-row:4;grid-column:1 / span 6"></div>
      <div class="tlx-bar fill summit" style="grid-row:4;grid-column:7 / span 1">Pru Farm Festival<small>Supporting activation · 1 Nov</small></div>
      <div class="tlx-bar" style="grid-row:4;grid-column:8 / span 1"></div>
      <!-- Row 5 · GWS Collaboration May-Jul (1-3) + Pre-Summit Setup Aug-Oct (4-6) + GWS Exhibitor Nov (7) -->
      <div class="tlx-bar fill" style="grid-row:5;grid-column:1 / span 3">GWS Collaboration<small>Connect with them to find the best format of collaboration</small></div>
      <div class="tlx-bar fill" style="grid-row:5;grid-column:4 / span 3">Pre-Summit Setup<small>Aug – Oct 2026 · format, event organizer, experience design</small></div>
      <div class="tlx-bar fill summit" style="grid-row:5;grid-column:7 / span 1">Join GWS as Exhibitor<small>Conference presence · 10–13 Nov</small></div>
      <div class="tlx-bar" style="grid-row:5;grid-column:8 / span 1"></div>
      <!-- Row 6 · Hosted Experience 10-13 Nov (sub-col 7) -->
      <div class="tlx-bar" style="grid-row:6;grid-column:1 / span 6"></div>
      <div class="tlx-bar fill summit" style="grid-row:6;grid-column:7 / span 1">Hosted Experience<small>For potential referrers · 10–13 Nov</small></div>
      <div class="tlx-bar" style="grid-row:6;grid-column:8 / span 1"></div>
      <!-- Row 7 · Founding Industry Network Nov-Dec (7-8) -->
      <div class="tlx-bar" style="grid-row:7;grid-column:1 / span 6"></div>
      <div class="tlx-bar fill" style="grid-row:7;grid-column:7 / span 2">Founding Industry Network<small>4% commission · onboarding</small></div>
    </div>
"""

text = text[:start_idx] + new_bars + text[end_idx:]

# ─── 3. UPDATE AXIS LABELS for 8-col grid ───────────────────────────────
old_axis = """    <div class="tlx-axis">
      <div class="tlx-month" style="grid-column:1">May – Jun<strong>2026</strong></div>
      <div class="tlx-month" style="grid-column:2">Jul – Aug</div>
      <div class="tlx-month" style="grid-column:3">Sep – Oct</div>
      <div class="tlx-month" style="grid-column:4">Nov – Dec</div>
    </div>"""

new_axis = """    <div class="tlx-axis">
      <div class="tlx-month" style="grid-column:1 / span 2">May – Jun<strong>2026</strong></div>
      <div class="tlx-month" style="grid-column:3 / span 2">Jul – Aug</div>
      <div class="tlx-month" style="grid-column:5 / span 2">Sep – Oct</div>
      <div class="tlx-month" style="grid-column:7 / span 2">Nov – Dec</div>
    </div>"""

text = text.replace(old_axis, new_axis)

# ─── 4. UPDATE Summary recap line ───────────────────────────────────────
text = text.replace(
    '<div class="sum-when">Aug – Dec 2026</div>\n      <div class="sum-name">Pre-Summit Setup — <span class="it">sustained format, event organisation, and experience design through the summit and beyond.</span></div>',
    '<div class="sum-when">Aug – Oct 2026</div>\n      <div class="sum-name">Pre-Summit Setup — <span class="it">format, event organisation, and experience design before the summit.</span></div>'
)

V2.write_text(text)
print(f"File size: {len(text):,} chars")
