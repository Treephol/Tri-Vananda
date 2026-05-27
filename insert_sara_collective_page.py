"""
Insert new page 08 'SARA Collective' after Organisation Structure (page 07).
Renumber subsequent pages 08-33 → 09-34.
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── NEW CSS ─────────────────────────────────────────────────────────────
NEW_CSS = """
/* ───── SARA COLLECTIVE · TIER CARDS ───── */
.tier-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:36px}
.tier-card{background:var(--ink);padding:36px 32px 32px;display:flex;flex-direction:column;gap:14px;position:relative;min-height:520px}
.tier-card.patrons{background:linear-gradient(180deg,var(--ink) 0%,rgba(184,148,88,.06) 100%)}
.tier-num{font-family:'Jost',sans-serif;font-weight:200;font-size:.56rem;letter-spacing:.36em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.tier-tag{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1rem;color:rgba(184,148,88,.8);line-height:1.3;margin-top:-4px}
.tier-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.6rem;color:var(--white);line-height:1.2;margin-top:8px;padding-bottom:14px;border-bottom:1px solid rgba(184,148,88,.18)}
.tier-card.patrons .tier-name{color:var(--gold-lt)}
.tier-name .it{font-style:italic;color:var(--gold-lt)}
.tier-body{font-family:'Jost',sans-serif;font-weight:300;font-size:.82rem;line-height:1.75;color:rgba(255,255,255,.72);margin-top:6px}
.tier-list{display:flex;flex-direction:column;gap:8px;padding:0;margin:14px 0 0;list-style:none}
.tier-list li{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.55;color:rgba(255,255,255,.74);padding-left:16px;position:relative}
.tier-list li::before{content:'';position:absolute;left:0;top:8px;width:8px;height:1px;background:rgba(184,148,88,.6)}
.tier-audience{margin-top:auto;padding-top:18px;border-top:1px solid rgba(184,148,88,.14);font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:rgba(184,148,88,.85);line-height:1.45}

/* SARA Collective · Sub-units (Where the Collective lives) */
.units-tier{margin-top:32px;padding:24px 28px;background:rgba(184,148,88,.04);border:1px solid rgba(184,148,88,.18);width:100%;display:flex;flex-direction:column;gap:18px}
.units-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold-lt);line-height:1.5;text-align:center}
.units-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;width:100%}
.unit-card{background:var(--ink);padding:22px 22px 22px;display:flex;flex-direction:column;gap:10px;min-height:170px;border:1px solid rgba(184,148,88,.14)}
.unit-card.agent{background:linear-gradient(180deg,var(--ink) 0%,rgba(184,148,88,.04) 100%);border-color:rgba(184,148,88,.3)}
.unit-tag{font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.unit-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.25rem;color:var(--white);line-height:1.2}
.unit-card.agent .unit-name{color:var(--gold-lt)}
.unit-desc{font-family:'Jost',sans-serif;font-weight:300;font-size:.7rem;line-height:1.6;color:rgba(255,255,255,.6);margin-top:2px}
.unit-partners{display:flex;flex-direction:column;gap:5px;margin-top:8px;padding-top:10px;border-top:1px solid rgba(184,148,88,.14)}
.unit-partner{font-family:'Jost',sans-serif;font-weight:300;font-size:.7rem;color:rgba(255,255,255,.72);line-height:1.5;padding-left:10px;position:relative}
.unit-partner::before{content:'';position:absolute;left:0;top:8px;width:5px;height:1px;background:rgba(184,148,88,.55)}
"""

# Insert CSS before the FIRST </style>
style_end = "</style>"
text = text.replace(style_end, NEW_CSS + "\n" + style_end, 1)

# ─── NEW PAGE HTML ───────────────────────────────────────────────────────
new_page = """
<!-- ═══════════════════ 08 NEW WELLNESS BRAND · SARA COLLECTIVE ═══════════════════ -->
<section class="S forest">
  <div class="eye">New Wellness Brand Development · SARA Collective</div>
  <div class="D2" style="max-width:980px;margin-bottom:14px">The SARA Collective &mdash; <span class="it gd">a customer journey in three tiers.</span></div>
  <div class="rule"></div>
  <p class="body lg" style="max-width:920px">A Collective is something you enter, then choose to belong to, then choose to make your home. SARA is designed so the journey of commitment has three distinct stages &mdash; the doorway, the year-round practice, and the inheritance. Each tier opens different doors across the four sub-units of the brand.</p>

  <div class="tier-grid">
    <!-- Tier 01 -->
    <div class="tier-card">
      <div class="tier-num">Tier 01</div>
      <div class="tier-tag">The doorway</div>
      <h3 class="tier-name">Indicative <span class="it">&middot; Open Experiences</span></h3>
      <div class="tier-body">An indicative taste of the SARA practice &mdash; available to anyone, without commitment. The first step into the Collective for the curious, the gift recipient, the first-time visitor.</div>
      <ul class="tier-list">
        <li>Day passes to SARA Coastal &amp; Farm &amp; Forest</li>
        <li>Open Experience retreats (2&ndash;3 days)</li>
        <li>Sampler dinners &amp; tea ceremonies at PRU</li>
        <li>Pru Farm Festival &amp; seasonal public events</li>
      </ul>
      <div class="tier-audience">For those discovering SARA for the first time.</div>
    </div>
    <!-- Tier 02 -->
    <div class="tier-card">
      <div class="tier-num">Tier 02</div>
      <div class="tier-tag">The core</div>
      <h3 class="tier-name">Core Model <span class="it">&middot; Yearly Membership</span></h3>
      <div class="tier-body">The committed expression. Annual membership grants year-round access across the SARA Collective and admission to the members&rsquo; calendar &mdash; the practice made daily.</div>
      <ul class="tier-list">
        <li>Year-round access across all SARA venues</li>
        <li>52-week calendar of programming, salons, workshops</li>
        <li>Member-only spaces, rituals, and rates</li>
        <li>Curated community &mdash; sponsorship or interview admission</li>
      </ul>
      <div class="tier-audience">For those who choose SARA as their ongoing practice.</div>
    </div>
    <!-- Tier 03 -->
    <div class="tier-card patrons">
      <div class="tier-num">Tier 03</div>
      <div class="tier-tag">The apex</div>
      <h3 class="tier-name">The Patrons <span class="it">&middot; A Home Within the Philosophy</span></h3>
      <div class="tier-body">The deepest commitment. Residence ownership at Tri Vananda places a family inside the philosophy &mdash; a home, not a visit. Founding patrons help shape what the Collective becomes.</div>
      <ul class="tier-list">
        <li>Tri Vananda residence ownership</li>
        <li>Lifetime patron status &amp; founding-family designation</li>
        <li>Curator privileges &amp; programming influence</li>
        <li>Brand ambassadorship &amp; legacy participation</li>
      </ul>
      <div class="tier-audience">For founders &amp; legacy families committed across generations.</div>
    </div>
  </div>

  <div class="units-tier">
    <div class="units-label">Where the Collective lives &mdash; the four sub-units of SARA</div>
    <div class="units-row">
      <div class="unit-card">
        <div class="unit-tag">Venue &middot; Phuket</div>
        <h4 class="unit-name">SARA Farm &amp; Forest</h4>
        <div class="unit-desc">The Pru farm &amp; the forest reset &mdash; where the terroir lives.</div>
      </div>
      <div class="unit-card">
        <div class="unit-tag">Venue &middot; Phuket</div>
        <h4 class="unit-name">SARA Coastal</h4>
        <div class="unit-desc">The beachfront expression at Trisara &mdash; where the Andaman meets the practice.</div>
      </div>
      <div class="unit-card">
        <div class="unit-tag">Venue &middot; Phuket</div>
        <h4 class="unit-name">SARA Retreat</h4>
        <div class="unit-desc">Programmed multi-day retreats &mdash; the SARA Method delivered in full.</div>
      </div>
      <div class="unit-card agent">
        <div class="unit-tag">Partner brand layer</div>
        <h4 class="unit-name">SARA Agent</h4>
        <div class="unit-desc">Partner brands operating under the SARA Collective umbrella.</div>
        <div class="unit-partners">
          <div class="unit-partner">Clinique La Prairie</div>
          <div class="unit-partner">Tri Vananda Residences</div>
          <div class="unit-partner">PRU</div>
          <div class="unit-partner">Future partners &mdash; curated, never extended lightly</div>
        </div>
      </div>
    </div>
  </div>

  <div class="pg">08</div>
</section>"""

# Insert new page AFTER the Organisation Structure section close
# The Org Structure section ends with </section> right before the next page
anchor = """  <div class="pg">07</div>
</section>

<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->"""

new_anchor = f"""  <div class="pg">07</div>
</section>
{new_page}

<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->"""

if anchor not in text:
    raise RuntimeError("Insertion anchor not found")
text = text.replace(anchor, new_anchor, 1)

# Now renumber existing pages 08-33 → 09-34
# Need to be careful: we just added a new "08" tag. The renumbering must happen AFTER our new page.
# Split at the section after our new page (the offerings/Collective page)
post_anchor = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->"
head, _, tail = text.partition(post_anchor)
# Renumber high to low to avoid double-replacement
for old, new in [(33, 34), (32, 33), (31, 32), (30, 31), (29, 30),
                 (28, 29), (27, 28), (26, 27), (25, 26), (24, 25),
                 (23, 24), (22, 23), (21, 22), (20, 21), (19, 20),
                 (18, 19), (17, 18), (16, 17), (15, 16), (14, 15),
                 (13, 14), (12, 13), (11, 12), (10, 11), (9, 10),
                 (8, 9)]:
    tail = tail.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')
text = head + post_anchor + tail

HTML_PATH.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
