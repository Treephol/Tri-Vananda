"""
Refactor timeline to 4 equal columns ending at Dec 2026 (no Jan 2027).

1. CSS — grid columns 6-eff → 4 equal
2. Main timeline bars — remap all grid-column values
3. Axis labels — 4 boxes (May-Jun, Jul-Aug, Sep-Oct, Nov-Dec)
4. Summit overlay — reposition for Nov (first half of col 4)
5. All 8 mini-timelines — 6 cells → 4 cells, axis 5 labels → 4 labels
6. Content text — replace 'Jan 2027' / 'Q1 2027' / 'Nov-Jan' / 'Aug-Jan' references
"""

from pathlib import Path
import re

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── 1. CSS UPDATES ──────────────────────────────────────────────────────
# .tlx and .tlx-axis: 6-eff → 4 equal
text = text.replace(
    ".tlx{display:grid;grid-template-columns:1fr 0.5fr 0.5fr 1fr 1fr 1fr;gap:1px;background:rgba(184,148,88,.14);border:1px solid rgba(184,148,88,.18);position:relative}",
    ".tlx{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(184,148,88,.14);border:1px solid rgba(184,148,88,.18);position:relative}"
)
text = text.replace(
    ".tlx-axis{display:grid;grid-template-columns:1fr 0.5fr 0.5fr 1fr 1fr 1fr;gap:1px;border-top:1px solid rgba(184,148,88,.32)}",
    ".tlx-axis{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;border-top:1px solid rgba(184,148,88,.32)}"
)

# Summit column overlay — Nov is now first half of col 4 (75-87.5%)
text = text.replace(
    ".tlx-summit-col{position:absolute;top:0;bottom:0;left:calc(3 / 5 * 100%);width:calc(1 / 5 * 100%);background:linear-gradient(180deg,rgba(184,148,88,.06) 0%,rgba(184,148,88,.02) 80%);border-left:1px dashed rgba(184,148,88,.4);border-right:1px dashed rgba(184,148,88,.4);pointer-events:none;z-index:0}",
    ".tlx-summit-col{position:absolute;top:0;bottom:0;left:75%;width:12.5%;background:linear-gradient(180deg,rgba(184,148,88,.06) 0%,rgba(184,148,88,.02) 80%);border-left:1px dashed rgba(184,148,88,.4);border-right:1px dashed rgba(184,148,88,.4);pointer-events:none;z-index:0}"
)

# Summit tag — centered on Nov (first half of col 4)
text = text.replace(
    ".tlx-summit-tag{position:absolute;top:0px;left:calc((3 / 5 * 100%) + (0.5 / 5 * 100%));transform:translateX(-50%);font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.4em;color:var(--gold-lt);background:var(--ink);padding:5px 14px;border:1px solid rgba(184,148,88,.4);border-radius:2px;white-space:nowrap;z-index:2}",
    ".tlx-summit-tag{position:absolute;top:0px;left:81.25%;transform:translateX(-50%);font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.4em;color:var(--gold-lt);background:var(--ink);padding:5px 14px;border:1px solid rgba(184,148,88,.4);border-radius:2px;white-space:nowrap;z-index:2}"
)

# .init-mini-bar and .init-mini-axis: 6-eff → 4 equal
text = text.replace(
    ".init-mini-bar{display:grid;grid-template-columns:1fr 0.5fr 0.5fr 1fr 1fr 1fr;gap:1px;background:rgba(184,148,88,.14)}",
    ".init-mini-bar{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(184,148,88,.14)}"
)
text = text.replace(
    ".init-mini-axis{display:grid;grid-template-columns:1fr 0.5fr 0.5fr 1fr 1fr 1fr;gap:1px;margin-top:8px}",
    ".init-mini-axis{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;margin-top:8px}"
)

# ─── 2. MAIN TIMELINE BARS — replace the entire block ────────────────────
old_timeline = """      <!-- Row 1 · New Wellness Brand Development (May–Jul, cols 1-2) + Marketing Collateral Preparation (Aug-Oct, cols 3-4) + Continuing Communications (Nov-Jan, cols 5-6) -->
      <div class="tlx-bar fill" style="grid-row:1;grid-column:1 / span 2">New Wellness Brand Development<small>Brand, naming &amp; identity</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:3 / span 2">Marketing Collateral Preparation<small>Renderings · photos · videos · masterplan model</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:5 / span 2">Continuing Communications<small>Luxury Wellness Lifestyle Brand</small></div>
      <!-- Row 2 · Renovated Trisara Wellness Launch (Sep-Oct, col 4) -->
      <div class="tlx-bar" style="grid-row:2;grid-column:1 / span 3"></div>
      <div class="tlx-bar fill launch" style="grid-row:2;grid-column:4 / span 1">Renovated Trisara Wellness<small>Launch &middot; Sep &ndash; Oct</small></div>
      <div class="tlx-bar" style="grid-row:2;grid-column:5 / span 2"></div>
      <!-- Row 3 · PR Agency Selection (May–Jul, cols 1-2) + PR Campaign (Aug–Jan, cols 3-6) -->
      <div class="tlx-bar fill" style="grid-row:3;grid-column:1 / span 2">PR Agency Selection<small>Closed shortlist · 3 months</small></div>
      <div class="tlx-bar fill" style="grid-row:3;grid-column:3 / span 4">PR Campaign<small>Sustained Aug 2026 – Jan 2027</small></div>
      <!-- Row 4 · Pru Farm Festival (1 Nov, col 5) -->
      <div class="tlx-bar" style="grid-row:4;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill summit" style="grid-row:4;grid-column:5 / span 1">Pru Farm Festival<small>Supporting activation · 1 Nov</small></div>
      <div class="tlx-bar" style="grid-row:4;grid-column:6 / span 1"></div>
      <!-- Row 5 · GWS Collaboration (May–Jul, cols 1-2) + Pre-Summit Setup (Aug–Oct, cols 3-4) + Join GWS as Exhibitor (10–13 Nov, col 5) -->
      <div class="tlx-bar fill" style="grid-row:5;grid-column:1 / span 2">GWS Collaboration<small>Connect with them to find the best format of collaboration</small></div>
      <div class="tlx-bar fill" style="grid-row:5;grid-column:3 / span 2">Pre-Summit Setup<small>Format · event organizer · experience design</small></div>
      <div class="tlx-bar fill summit" style="grid-row:5;grid-column:5 / span 1">Join GWS as Exhibitor<small>Conference presence · 10–13 Nov</small></div>
      <div class="tlx-bar" style="grid-row:5;grid-column:6 / span 1"></div>
      <!-- Row 6 · Hosted Experience (10–13 Nov, col 5) -->
      <div class="tlx-bar" style="grid-row:6;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill summit" style="grid-row:6;grid-column:5 / span 1">Hosted Experience<small>For potential referrers · 10–13 Nov</small></div>
      <div class="tlx-bar" style="grid-row:6;grid-column:6 / span 1"></div>
      <!-- Row 7 · Founding Industry Network (Nov – Jan 2027, cols 5-6) -->
      <div class="tlx-bar" style="grid-row:7;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill" style="grid-row:7;grid-column:5 / span 2">Founding Industry Network<small>4% commission · onboarding</small></div>"""

new_timeline = """      <!-- Row 1 · NWB Dev (May-Jun) + Marketing Collateral (Jul-Oct) + Continuing Comms (Nov-Dec) -->
      <div class="tlx-bar fill" style="grid-row:1;grid-column:1 / span 1">New Wellness Brand Development<small>Brand, naming &amp; identity</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:2 / span 2">Marketing Collateral Preparation<small>Renderings · photos · videos · masterplan model</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:4 / span 1">Continuing Communications<small>Luxury Wellness Lifestyle Brand</small></div>
      <!-- Row 2 · Renovated Trisara Wellness Launch (Sep-Oct, col 3) -->
      <div class="tlx-bar" style="grid-row:2;grid-column:1 / span 2"></div>
      <div class="tlx-bar fill launch" style="grid-row:2;grid-column:3 / span 1">Renovated Trisara Wellness<small>Launch &middot; Sep &ndash; Oct</small></div>
      <div class="tlx-bar" style="grid-row:2;grid-column:4 / span 1"></div>
      <!-- Row 3 · PR Agency Selection (May-Jun) + PR Campaign (Jul-Dec) -->
      <div class="tlx-bar fill" style="grid-row:3;grid-column:1 / span 1">PR Agency Selection<small>Closed shortlist · 3 months</small></div>
      <div class="tlx-bar fill" style="grid-row:3;grid-column:2 / span 3">PR Campaign<small>Sustained Aug – Dec 2026</small></div>
      <!-- Row 4 · Pru Farm Festival (1 Nov, col 4) -->
      <div class="tlx-bar" style="grid-row:4;grid-column:1 / span 3"></div>
      <div class="tlx-bar fill summit" style="grid-row:4;grid-column:4 / span 1">Pru Farm Festival<small>Supporting activation · 1 Nov</small></div>
      <!-- Row 5 · GWS Collaboration (May-Jun) + Pre-Summit Setup (Jul-Oct) + GWS Exhibitor (Nov-Dec) -->
      <div class="tlx-bar fill" style="grid-row:5;grid-column:1 / span 1">GWS Collaboration<small>Connect with them to find the best format of collaboration</small></div>
      <div class="tlx-bar fill" style="grid-row:5;grid-column:2 / span 2">Pre-Summit Setup<small>Format · event organizer · experience design</small></div>
      <div class="tlx-bar fill summit" style="grid-row:5;grid-column:4 / span 1">Join GWS as Exhibitor<small>Conference presence · 10–13 Nov</small></div>
      <!-- Row 6 · Hosted Experience (Nov, col 4) -->
      <div class="tlx-bar" style="grid-row:6;grid-column:1 / span 3"></div>
      <div class="tlx-bar fill summit" style="grid-row:6;grid-column:4 / span 1">Hosted Experience<small>For potential referrers · 10–13 Nov</small></div>
      <!-- Row 7 · Founding Industry Network (Nov-Dec) -->
      <div class="tlx-bar" style="grid-row:7;grid-column:1 / span 3"></div>
      <div class="tlx-bar fill" style="grid-row:7;grid-column:4 / span 1">Founding Industry Network<small>4% commission · onboarding</small></div>"""

if old_timeline not in text:
    raise RuntimeError("Old timeline block not found")
text = text.replace(old_timeline, new_timeline)

# ─── 3. AXIS LABELS ──────────────────────────────────────────────────────
old_axis = """    <div class="tlx-axis">
      <div class="tlx-month" style="grid-column:1">May – Jun<strong>2026</strong></div>
      <div class="tlx-month" style="grid-column:2 / span 2">Jul – Aug</div>
      <div class="tlx-month" style="grid-column:4">Sep – Oct</div>
      <div class="tlx-month summit" style="grid-column:5">Nov</div>
      <div class="tlx-month" style="grid-column:6">Dec – Jan<strong>2027</strong></div>
    </div>"""

new_axis = """    <div class="tlx-axis">
      <div class="tlx-month" style="grid-column:1">May – Jun<strong>2026</strong></div>
      <div class="tlx-month" style="grid-column:2">Jul – Aug</div>
      <div class="tlx-month" style="grid-column:3">Sep – Oct</div>
      <div class="tlx-month summit" style="grid-column:4">Nov – Dec</div>
    </div>"""

if old_axis not in text:
    raise RuntimeError("Old axis block not found")
text = text.replace(old_axis, new_axis)

# ─── 4. MINI-TIMELINES ───────────────────────────────────────────────────
# Each mini-timeline has 6 cells; need to map to 4 cells based on initiative dates.
# Pattern: find each <div class="init-mini-bar"> ... </div> block and replace contents.

# Define each mini-timeline's NEW 4-cell pattern (off/on)
# Using initiative names to identify which block is which
mini_replacements = [
    # Marketing Collateral Preparation (Aug-Oct) — currently active in Jul-Aug & Sep-Oct
    {
        "context": 'Marketing Collateral <span class="it">Preparation.</span>',
        "old_bar": """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell summit"></div>
          <div class="init-mini-cell"></div>
""",
        "new_bar": """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell"></div>
""",
    },
    # Trisara Launch (Sep-Oct, just added)
    {
        "context": 'Renovated Trisara <span class="it">Wellness.</span>',
        "old_bar": """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell summit"></div>
          <div class="init-mini-cell"></div>
        </div>""",
        "new_bar": """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell"></div>
        </div>""",
    },
    # Pru Farm Festival (1 Nov)
    # GWS Exhibitor (10-13 Nov)
    # Hosted Experience (10-13 Nov)
    # All three are summit-only activations
]

# Generic transformation: any mini-bar with 6 cells where col 5 is summit
# We'll process all remaining mini-timelines after these specific ones

# Apply specific replacements first
for r in mini_replacements:
    if r["context"] in text and r["old_bar"] in text:
        text = text.replace(r["old_bar"], r["new_bar"], 1)
        print(f"  ✓ Updated mini-bar for: {r['context'][:50]}...")
    else:
        print(f"  ⚠ Could not find mini-bar for: {r['context'][:50]}...")

# Now handle the remaining mini-bars individually by looking at their content/context.
# Each remaining one is one of: Pru Farm Fest, GWS Exhibitor, Hosted Experience, PR Campaign,
# Founding Industry Network, Continuing Communications.

# Define replacements for each remaining initiative
generic_summit_only = ("""        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell summit"></div>
          <div class="init-mini-cell"></div>
""",
"""        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
""")

# Apply summit-only pattern wherever it remains
n_summit_only = text.count(generic_summit_only[0])
text = text.replace(generic_summit_only[0], generic_summit_only[1])
print(f"  ✓ Replaced {n_summit_only} summit-only mini-bars")

# PR Campaign (Aug-Jan, active Aug onwards)
pr_old = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell summit"></div>
          <div class="init-mini-cell on"></div>
"""
pr_new = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
          <div class="init-mini-cell on"></div>
"""
if pr_old in text:
    text = text.replace(pr_old, pr_new, 1)
    print("  ✓ PR Campaign mini-bar updated")
else:
    print("  ⚠ PR Campaign mini-bar pattern not found")

# Founding Industry Network / Continuing Communications (Nov-Jan)
nov_jan_old = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell summit"></div>
          <div class="init-mini-cell on"></div>
"""
nov_jan_new = """        <div class="init-mini-bar">
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell"></div>
          <div class="init-mini-cell on"></div>
"""
n_nov_jan = text.count(nov_jan_old)
text = text.replace(nov_jan_old, nov_jan_new)
print(f"  ✓ Replaced {n_nov_jan} Nov-Jan mini-bars (Founding Industry Network, Continuing Comms)")

# ─── 5. MINI-AXIS LABELS — convert all 5-label axes to 4-label ───────────
old_mini_axis = """        <div class="init-mini-axis">
          <div class="init-mini-month" style="grid-column:1">May–Jun</div>
          <div class="init-mini-month" style="grid-column:2 / span 2">Jul–Aug</div>
          <div class="init-mini-month" style="grid-column:4">Sep–Oct</div>
          <div class="init-mini-month s" style="grid-column:5">Summit</div>
          <div class="init-mini-month y" style="grid-column:6">Dec–Jan</div>
        </div>"""

new_mini_axis = """        <div class="init-mini-axis">
          <div class="init-mini-month" style="grid-column:1">May–Jun</div>
          <div class="init-mini-month" style="grid-column:2">Jul–Aug</div>
          <div class="init-mini-month" style="grid-column:3">Sep–Oct</div>
          <div class="init-mini-month s" style="grid-column:4">Nov–Dec</div>
        </div>"""

n_axis = text.count(old_mini_axis)
text = text.replace(old_mini_axis, new_mini_axis)
print(f"  ✓ Updated {n_axis} mini-axis label blocks")

# Also handle Trisara Launch's variant (s class on col 4 instead of 5)
trisara_axis_old = """        <div class="init-mini-axis">
          <div class="init-mini-month" style="grid-column:1">May–Jun</div>
          <div class="init-mini-month" style="grid-column:2 / span 2">Jul–Aug</div>
          <div class="init-mini-month s" style="grid-column:4">Sep–Oct</div>
          <div class="init-mini-month" style="grid-column:5">Summit</div>
          <div class="init-mini-month y" style="grid-column:6">Dec–Jan</div>
        </div>"""
trisara_axis_new = """        <div class="init-mini-axis">
          <div class="init-mini-month" style="grid-column:1">May–Jun</div>
          <div class="init-mini-month" style="grid-column:2">Jul–Aug</div>
          <div class="init-mini-month s" style="grid-column:3">Sep–Oct</div>
          <div class="init-mini-month" style="grid-column:4">Nov–Dec</div>
        </div>"""
if trisara_axis_old in text:
    text = text.replace(trisara_axis_old, trisara_axis_new, 1)
    print("  ✓ Trisara axis updated")

# ─── 6. TEXT REFERENCES TO JAN 2027 / Q1 2027 ────────────────────────────
text_updates = [
    # PR Campaign descriptors
    ("Sustained Aug 2026 – Jan 2027", "Sustained Aug – Dec 2026"),
    ("Aug 2026 – Jan 2027", "Aug – Dec 2026"),
    ("Aug 2026 – Jan 2027", "Aug – Dec 2026"),
    # Founding Industry Network and Continuing Comms
    ("Nov 2026 → Q1 2027", "Nov – Dec 2026"),
    ("Nov 2026 → Q1 2027", "Nov – Dec 2026"),
    ("Nov 2026 – Q1 2027", "Nov – Dec 2026"),
    ("Nov 2026 – Q1 2027", "Nov – Dec 2026"),
    ("Nov – Jan 2027", "Nov – Dec 2026"),
    ("Nov – Jan 2027", "Nov – Dec 2026"),
    # Generic
    ("through Q1 2027", "through Dec 2026"),
    ("runs through Q1 2027", "runs through Dec 2026"),
    ("into 2027", "into Dec"),
    # Summary recap line
    ("into cultural conversation, into 2027", "into cultural conversation, sustained through Dec 2026"),
    # End card copy
    ("carries the position through to year-end.", "carries the position through Dec 2026."),
]

for old, new in text_updates:
    if old in text:
        n = text.count(old)
        text = text.replace(old, new)
        print(f"  ✓ Replaced '{old[:50]}...' ({n}x)")

HTML_PATH.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"\nFinal: {sections} sections open, {closes} close, {pgs} page tags")
