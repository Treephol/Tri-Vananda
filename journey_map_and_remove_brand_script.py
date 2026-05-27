"""
1. Replace SARA Collective tier section with journey-map style (concise, infographic).
2. Remove the Brand Script page (page 06).
3. Renumber subsequent pages 07-34 → 06-33.
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── 1. ADD JOURNEY-MAP CSS ──────────────────────────────────────────────
NEW_CSS = """
/* ───── SARA COLLECTIVE · JOURNEY MAP (infographic) ───── */
.journey-wrap{margin-top:36px}
.journey-track{display:grid;grid-template-columns:repeat(3,1fr);align-items:start;margin-bottom:8px;position:relative}
.journey-stop{display:flex;align-items:center;justify-content:center;flex-direction:column;position:relative;z-index:2;padding:0 12px}
.journey-stop::before{content:'';position:absolute;left:calc(50% + 18px);right:calc(-50% + 18px);top:18px;height:1px;background:linear-gradient(90deg,rgba(184,148,88,.55) 0%,rgba(184,148,88,.55) 90%,transparent 100%);z-index:1}
.journey-stop:last-child::before{display:none}
.journey-stop::after{content:'';position:absolute;right:calc(-50% + 22px);top:14px;width:0;height:0;border-left:6px solid rgba(184,148,88,.65);border-top:4px solid transparent;border-bottom:4px solid transparent;z-index:1}
.journey-stop:last-child::after{display:none}
.journey-marker{width:36px;height:36px;border-radius:50%;background:var(--ink);border:1px solid var(--gold);display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1rem;color:var(--gold);position:relative;z-index:3}
.journey-stop.apex .journey-marker{background:linear-gradient(135deg,var(--gold) 0%,var(--gold-lt) 100%);color:var(--ink);border-color:var(--gold-lt);box-shadow:0 0 0 5px rgba(184,148,88,.16)}
.journey-stop-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.36em;text-transform:uppercase;color:var(--gold);margin-top:14px}

.journey-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:20px}
.journey-card{background:var(--ink);padding:30px 26px 26px;display:flex;flex-direction:column;gap:10px;min-height:340px}
.journey-card.apex{background:linear-gradient(180deg,var(--ink) 0%,rgba(184,148,88,.06) 100%)}
.journey-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.55rem;color:var(--white);line-height:1.15}
.journey-card.apex .journey-name{color:var(--gold-lt)}
.journey-name .it{font-style:italic;color:var(--gold-lt)}
.journey-strap{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1rem;color:rgba(255,255,255,.6);line-height:1.4;padding-bottom:14px;border-bottom:1px solid rgba(184,148,88,.16)}
.journey-items{display:flex;flex-direction:column;gap:8px;margin-top:6px}
.journey-item{font-family:'Jost',sans-serif;font-weight:300;font-size:.76rem;line-height:1.55;color:rgba(255,255,255,.76);padding-left:14px;position:relative}
.journey-item::before{content:'';position:absolute;left:0;top:8px;width:7px;height:1px;background:rgba(184,148,88,.55)}
.journey-aud{margin-top:auto;padding-top:14px;border-top:1px solid rgba(184,148,88,.12);font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.85rem;color:rgba(184,148,88,.82);line-height:1.4}
"""

text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── 2. REPLACE TIER SECTION WITH JOURNEY MAP ────────────────────────────
old_tier_block_start = '  <div class="tier-grid">'
old_tier_block_end = '  </div>\n\n  <div class="units-tier">'

# Find boundaries
start_idx = text.index(old_tier_block_start)
# End: before <div class="units-tier">
end_idx = text.index('  <div class="units-tier">')

new_journey_block = """  <div class="journey-wrap">
    <div class="journey-track">
      <div class="journey-stop">
        <div class="journey-marker">01</div>
        <div class="journey-stop-label">The Doorway</div>
      </div>
      <div class="journey-stop">
        <div class="journey-marker">02</div>
        <div class="journey-stop-label">The Core</div>
      </div>
      <div class="journey-stop apex">
        <div class="journey-marker">03</div>
        <div class="journey-stop-label">The Apex</div>
      </div>
    </div>

    <div class="journey-grid">
      <div class="journey-card">
        <h3 class="journey-name">Open <span class="it">Experiences</span></h3>
        <div class="journey-strap">A taste, no commitment.</div>
        <div class="journey-items">
          <div class="journey-item">Day passes &mdash; Coastal &amp; Farm &amp; Forest</div>
          <div class="journey-item">Open Experience retreats (2&ndash;3 days)</div>
          <div class="journey-item">Sampler dining &amp; seasonal events</div>
        </div>
        <div class="journey-aud">For the first-time visitor.</div>
      </div>
      <div class="journey-card">
        <h3 class="journey-name">Yearly <span class="it">Membership</span></h3>
        <div class="journey-strap">The practice made daily.</div>
        <div class="journey-items">
          <div class="journey-item">Year-round access &mdash; all SARA venues</div>
          <div class="journey-item">52-week programming calendar</div>
          <div class="journey-item">Member spaces, rituals, rates</div>
        </div>
        <div class="journey-aud">For the ongoing practice.</div>
      </div>
      <div class="journey-card apex">
        <h3 class="journey-name">The <span class="it">Patrons</span></h3>
        <div class="journey-strap">A home within the philosophy.</div>
        <div class="journey-items">
          <div class="journey-item">Tri Vananda residence ownership</div>
          <div class="journey-item">Founding-family patronage</div>
          <div class="journey-item">Curator privileges &amp; legacy</div>
        </div>
        <div class="journey-aud">For founders &amp; legacy families.</div>
      </div>
    </div>
  </div>

  """

text = text[:start_idx] + new_journey_block + text[end_idx:]

# ─── 3. REMOVE BRAND SCRIPT PAGE (page 06) ───────────────────────────────
# The Brand Script section is identified by its comment header
bs_start = "<!-- ═══════════════════ 06 SARA · THE BRAND SCRIPT ═══════════════════ -->"
bs_end = '  <div class="pg">06</div>\n</section>'

if bs_start in text:
    start_idx = text.index(bs_start)
    # Find the matching </section> after pg 06
    end_idx = text.index(bs_end, start_idx) + len(bs_end)
    text = text[:start_idx] + text[end_idx:]
    print("Brand Script page removed.")
else:
    print("⚠ Brand Script anchor not found")

# Clean up the empty line and renumber pages 07-34 → 06-33
# Now the next page (Org Structure, currently page 07) becomes page 06
# Page 08 (SARA Collective) becomes page 07
# etc.
for old, new in [(7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11),
                 (13, 12), (14, 13), (15, 14), (16, 15), (17, 16), (18, 17),
                 (19, 18), (20, 19), (21, 20), (22, 21), (23, 22), (24, 23),
                 (25, 24), (26, 25), (27, 26), (28, 27), (29, 28), (30, 29),
                 (31, 30), (32, 31), (33, 32), (34, 33)]:
    text = text.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')

HTML_PATH.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
