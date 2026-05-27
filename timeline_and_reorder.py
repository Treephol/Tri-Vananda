"""
Two changes:
1. Insert new row 2 in timeline (Renovated Trisara Wellness Launch, Sep-Oct, highlighted).
   Renumber existing rows 2-6 to rows 3-7.
2. Reorder Page 04 brand pillar cards: Trisara | CLP | Tri Vananda → Trisara | Tri Vananda | CLP.
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── 1. TIMELINE: INSERT NEW ROW 2 + RENUMBER ───────────────────────────
# Old timeline bar block boundaries
old_timeline = """      <!-- Row 1 · New Wellness Brand Development (May–Jul, cols 1-2) + Marketing Collateral Preparation (Aug-Oct, cols 3-4) + Continuing Communications (Nov-Jan, cols 5-6) -->
      <div class="tlx-bar fill" style="grid-row:1;grid-column:1 / span 2">New Wellness Brand Development<small>Culture, naming &amp; identity</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:3 / span 2">Marketing Collateral Preparation<small>Renderings · photos · videos · masterplan model</small></div>
      <div class="tlx-bar fill" style="grid-row:1;grid-column:5 / span 2">Continuing Communications<small>Luxury Wellness Lifestyle Brand</small></div>
      <!-- Row 2 · PR Agency Selection (May–Jul, cols 1-2) + PR Campaign (Aug–Jan, cols 3-6) -->
      <div class="tlx-bar fill" style="grid-row:2;grid-column:1 / span 2">PR Agency Selection<small>Closed shortlist · 3 months</small></div>
      <div class="tlx-bar fill" style="grid-row:2;grid-column:3 / span 4">PR Campaign<small>Sustained Aug 2026 – Jan 2027</small></div>
      <!-- Row 3 · Pru Farm Festival (1 Nov, col 5) -->
      <div class="tlx-bar" style="grid-row:3;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill summit" style="grid-row:3;grid-column:5 / span 1">Pru Farm Festival<small>Supporting activation · 1 Nov</small></div>
      <div class="tlx-bar" style="grid-row:3;grid-column:6 / span 1"></div>
      <!-- Row 4 · GWS Collaboration (May–Jul, cols 1-2) + Pre-Summit Setup (Aug–Oct, cols 3-4) + Join GWS as Exhibitor (10–13 Nov, col 5) -->
      <div class="tlx-bar fill" style="grid-row:4;grid-column:1 / span 2">GWS Collaboration<small>Connect with them to find the best format of collaboration</small></div>
      <div class="tlx-bar fill" style="grid-row:4;grid-column:3 / span 2">Pre-Summit Setup<small>Format · event organizer · experience design</small></div>
      <div class="tlx-bar fill summit" style="grid-row:4;grid-column:5 / span 1">Join GWS as Exhibitor<small>Conference presence · 10–13 Nov</small></div>
      <div class="tlx-bar" style="grid-row:4;grid-column:6 / span 1"></div>
      <!-- Row 5 · Hosted Experience (10–13 Nov, col 5) -->
      <div class="tlx-bar" style="grid-row:5;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill summit" style="grid-row:5;grid-column:5 / span 1">Hosted Experience<small>For potential referrers · 10–13 Nov</small></div>
      <div class="tlx-bar" style="grid-row:5;grid-column:6 / span 1"></div>
      <!-- Row 6 · Founding Industry Network (Nov – Jan 2027, cols 5-6) -->
      <div class="tlx-bar" style="grid-row:6;grid-column:1 / span 4"></div>
      <div class="tlx-bar fill" style="grid-row:6;grid-column:5 / span 2">Founding Industry Network<small>4% commission · onboarding</small></div>"""

new_timeline = """      <!-- Row 1 · New Wellness Brand Development (May–Jul, cols 1-2) + Marketing Collateral Preparation (Aug-Oct, cols 3-4) + Continuing Communications (Nov-Jan, cols 5-6) -->
      <div class="tlx-bar fill" style="grid-row:1;grid-column:1 / span 2">New Wellness Brand Development<small>Culture, naming &amp; identity</small></div>
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

if old_timeline not in text:
    raise RuntimeError("Timeline block not found")
text = text.replace(old_timeline, new_timeline)

# ─── 2. REORDER PAGE 04 BRAND PILLAR CARDS ──────────────────────────────
# Order: Trisara | CLP | Tri Vananda → Trisara | Tri Vananda | CLP
old_pillars = """  <div class="bt-grid">
    <div class="bt-cell">
      <div class="bt-name">Renovated <span class="it">Trisara Wellness.</span></div>
      <div class="bt-desc">The beachfront expression &mdash; where resort guests at Trisara experience the new brand. Twenty years of luxury hospitality, refreshed under the new brand&rsquo;s standards.</div>
    </div>
    <div class="bt-cell">
      <div class="bt-name">Health Resort by <span class="it">Clinique La Prairie.</span></div>
      <div class="bt-desc">Switzerland&rsquo;s most established medical-wellness brand, signing the culture&rsquo;s clinical and longevity protocols. The credentialing layer that no competitor can replicate.</div>
    </div>
    <div class="bt-cell">
      <div class="bt-name">New Development <span class="it">at Tri Vananda.</span></div>
      <div class="bt-desc">The new wellness facilities and residential community &mdash; where the new brand becomes a way of life. The only place in the culture where it is own-able, not just visit-able.</div>
    </div>
  </div>"""

new_pillars = """  <div class="bt-grid">
    <div class="bt-cell">
      <div class="bt-name">Renovated <span class="it">Trisara Wellness.</span></div>
      <div class="bt-desc">The beachfront expression &mdash; where resort guests at Trisara experience the new brand. Twenty years of luxury hospitality, refreshed under the new brand&rsquo;s standards.</div>
    </div>
    <div class="bt-cell">
      <div class="bt-name">New Development <span class="it">at Tri Vananda.</span></div>
      <div class="bt-desc">The new wellness facilities and residential community &mdash; where the new brand becomes a way of life. The only place in the culture where it is own-able, not just visit-able.</div>
    </div>
    <div class="bt-cell">
      <div class="bt-name">Health Resort by <span class="it">Clinique La Prairie.</span></div>
      <div class="bt-desc">Switzerland&rsquo;s most established medical-wellness brand, signing the culture&rsquo;s clinical and longevity protocols. The credentialing layer that no competitor can replicate.</div>
    </div>
  </div>"""

if old_pillars not in text:
    raise RuntimeError("Pillar block not found")
text = text.replace(old_pillars, new_pillars)

HTML_PATH.write_text(text)
print("Both changes applied.")
print(f"File size: {len(text):,} chars")
