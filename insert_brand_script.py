"""
Insert new Brand Script page after the SARA Collective page (page 07).
Renumber existing pages 08-31 → 09-32.

The Brand Script uses Donald Miller's 7-part StoryBrand framework, aligned
to the updated deck: refers to the Collective tiers, the Culture tagline,
and the multigenerational family positioning.
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── NEW CSS ─────────────────────────────────────────────────────────────
NEW_CSS = """
/* ───── BRAND SCRIPT · 7-part framework ───── */
.script-list{display:flex;flex-direction:column;gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:30px}
.script-item{background:var(--ink);padding:22px 30px;display:grid;grid-template-columns:60px 220px 1fr;gap:30px;align-items:start}
.script-item.apex{background:linear-gradient(180deg,var(--ink) 0%,rgba(184,148,88,.05) 100%)}
.script-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.8rem;color:var(--gold-lt);line-height:1;padding-top:2px}
.script-side{display:flex;flex-direction:column;gap:4px}
.script-tag{font-family:'Jost',sans-serif;font-weight:200;font-size:.54rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.script-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.25rem;color:var(--white);line-height:1.2;margin-top:4px}
.script-strap{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:var(--gold-lt);line-height:1.4;margin-top:4px}
.script-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.7;color:rgba(255,255,255,.74);padding-top:4px}
.script-text ul{list-style:none;padding:0;margin:6px 0 0;display:flex;flex-direction:column;gap:5px}
.script-text li{padding-left:14px;position:relative;font-family:'Jost',sans-serif;font-weight:300;font-size:.74rem;line-height:1.6;color:rgba(255,255,255,.7)}
.script-text li::before{content:'';position:absolute;left:0;top:8px;width:7px;height:1px;background:rgba(184,148,88,.55)}
.script-text li strong{color:var(--gold-lt);font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.85rem;letter-spacing:.01em;margin-right:8px}
"""

text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── NEW PAGE HTML ───────────────────────────────────────────────────────
new_page = """
<!-- ═══════════════════ 08 NEW WELLNESS BRAND · THE BRAND SCRIPT ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">New Wellness Brand Development &middot; The Brand Script</div>
    <div class="D2" style="max-width:980px;margin-bottom:14px">The story SARA <span class="it gd">tells.</span></div>
    <div class="rule"></div>
    <p class="body lg" style="max-width:920px">A brand is a story it tells consistently. SARA&rsquo;s story has seven beats &mdash; the hero, the problem, the guide, the plan, the action, the failure averted, the success won. Held with discipline, this is the script every channel, every member, every team uses.</p>

    <div class="script-list">
      <div class="script-item">
        <div class="script-num">01</div>
        <div class="script-side">
          <div class="script-tag">The Hero</div>
          <h3 class="script-name">Character</h3>
          <div class="script-strap">The multigenerational family.</div>
        </div>
        <div class="script-text">Three generations under one roof, or three generations bound by one philosophy. Grandparents who want vitality without surrender. Parents who want a practice they can pass down. Children who want a way of life, not a treatment. People who choose to live well &mdash; together, across years.</div>
      </div>

      <div class="script-item">
        <div class="script-num">02</div>
        <div class="script-side">
          <div class="script-tag">What they face</div>
          <h3 class="script-name">Problem</h3>
          <div class="script-strap">Wellness is fragmented &mdash; and not made for families.</div>
        </div>
        <div class="script-text">Spa treatments are episodic. Fitness apps are solitary. Retreats happen once a year. Nothing connects across generations. Families live alongside each other instead of together. Wellbeing is treated as something you visit, not something you live.</div>
      </div>

      <div class="script-item">
        <div class="script-num">03</div>
        <div class="script-side">
          <div class="script-tag">Who shows them the way</div>
          <h3 class="script-name">Guide</h3>
          <div class="script-strap">SARA. Building the Culture of Living Well.</div>
        </div>
        <div class="script-text">SARA arrives with empathy and authority. Empathy: wellness is family-shaped, not individual-shaped. Authority: twenty-plus years of Trisara luxury hospitality, the medical lineage of Clinique La Prairie, the Michelin discipline of PRU, the residential commitment of Tri Vananda. One family of brands, one stewardship.</div>
      </div>

      <div class="script-item">
        <div class="script-num">04</div>
        <div class="script-side">
          <div class="script-tag">The path forward</div>
          <h3 class="script-name">Plan</h3>
          <div class="script-strap">Three doors into the Collective.</div>
        </div>
        <div class="script-text">
          <ul>
            <li><strong>Open Experiences &mdash;</strong> step into the Collective for a taste. Day passes, sampler retreats, seasonal events. No commitment.</li>
            <li><strong>Yearly Membership &mdash;</strong> belong to the Collective. Year-round access, the 52-week calendar, member spaces and rituals.</li>
            <li><strong>The Patrons &mdash;</strong> make the Collective home. Residence ownership at Tri Vananda, founding-family status, legacy participation.</li>
          </ul>
        </div>
      </div>

      <div class="script-item">
        <div class="script-num">05</div>
        <div class="script-side">
          <div class="script-tag">The invitation</div>
          <h3 class="script-name">Call to Action</h3>
          <div class="script-strap">Begin now.</div>
        </div>
        <div class="script-text">
          <ul>
            <li><strong>Direct &mdash;</strong> book an Open Experience at SARA Coastal, Farm &amp; Forest, or Retreat.</li>
            <li><strong>Transitional &mdash;</strong> apply for the Founding Membership cohort, opening Q4 2026.</li>
            <li><strong>Aspirational &mdash;</strong> reserve a residence at Tri Vananda.</li>
          </ul>
        </div>
      </div>

      <div class="script-item">
        <div class="script-num">06</div>
        <div class="script-side">
          <div class="script-tag">What is avoided</div>
          <h3 class="script-name">Failure</h3>
          <div class="script-strap">A life lived alongside, not with.</div>
        </div>
        <div class="script-text">Without SARA, wellness stays fragmented. Generations stay divided by their individual practices. Time at the table becomes shorter. Wellbeing remains a service consumed, not a culture inherited. The family lives next to itself, not as itself.</div>
      </div>

      <div class="script-item apex">
        <div class="script-num">07</div>
        <div class="script-side">
          <div class="script-tag">What is won</div>
          <h3 class="script-name">Success</h3>
          <div class="script-strap">A family that lives well, together &mdash; for generations.</div>
        </div>
        <div class="script-text">Wellbeing as a daily practice, not an annual event. Three generations sharing one way of life. A culture inherited, not a service consumed. Family that returns to itself &mdash; and to SARA &mdash; year after year, generation after generation.</div>
      </div>
    </div>
  </div>
  <div class="pg">08</div>
</section>"""

# ─── INSERT NEW PAGE AFTER SARA COLLECTIVE (page 07) ─────────────────────
anchor = """  <div class="pg">07</div>
</section>"""

# Find the FIRST </section> after page 07 — that's the end of the SARA Collective page
# We need to be careful — there are multiple </section> in the file
# Find the </section> right after pg 07
idx_pg7 = text.index('<div class="pg">07</div>')
idx_end = text.index('</section>', idx_pg7) + len('</section>')

# Insert the new page right after
text = text[:idx_end] + new_page + text[idx_end:]

# ─── RENUMBER pages 08-31 → 09-32 ────────────────────────────────────────
# Only renumber what comes AFTER our new page 08
# Find marker: the first occurrence of pg 08 AFTER our new insert
# But we just inserted our new page with pg 08, so the OLD page 08 (Collective offerings)
# now has pg 08 still. Let's count — we have 2 instances of "08" now.

# Use partition at our new page's end (the </section> right after our pg 08)
# Better: find the next pg tag after our insertion and renumber from there.

# Simpler approach: locate the anchor for the OLD page 08 (Collective offerings)
# and renumber everything from there onward
collective_offerings_anchor = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->"
if collective_offerings_anchor not in text:
    raise RuntimeError("Could not find Collective offerings anchor for renumbering")

head, _, tail = text.partition(collective_offerings_anchor)
# In tail, renumber pg 08-31 → 09-32 (high to low)
for old, new in [(31, 32), (30, 31), (29, 30), (28, 29), (27, 28), (26, 27),
                 (25, 26), (24, 25), (23, 24), (22, 23), (21, 22), (20, 21),
                 (19, 20), (18, 19), (17, 18), (16, 17), (15, 16), (14, 15),
                 (13, 14), (12, 13), (11, 12), (10, 11), (9, 10), (8, 9)]:
    tail = tail.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')

text = head + collective_offerings_anchor + tail

HTML_PATH.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
