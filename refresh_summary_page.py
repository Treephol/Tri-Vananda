"""
Option A: Refresh summary page stale content.
1. Remove Press Conference references from intro paragraph and end card
2. Add Trisara Launch milestone as a new highlighted row (Sep-Oct)
3. Update Continuing Communications copy to reflect the SARA Collective
4. Update count from 'Twelve' to 'Thirteen' initiatives
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── 1. UPDATE SUMMARY INTRO PARAGRAPH ───────────────────────────────────
old_intro = "The roadmap is a single piece of work. Each initiative depends on the one before it; each opens the one after. The Summit week recruits the room. The Press Conference on 1 November reveals the brand. The Press Campaigns carry it through to year-end."
new_intro = "The roadmap is a single piece of work. Each initiative depends on the one before it; each opens the one after. The Renovated Trisara Wellness opens in Sep&ndash;Oct. The Pru Farm Festival on 1 November celebrates the property. Summit week (10&ndash;13 November) recruits the room. The PR Campaign carries the position through to year-end."
if old_intro in text:
    text = text.replace(old_intro, new_intro)
    print("✓ Intro paragraph updated")
else:
    print("⚠ Intro paragraph not found")

# ─── 2. ADD TRISARA LAUNCH ROW ───────────────────────────────────────────
# Insert between Marketing Collateral Preparation (Aug-Oct) and Pru Farm Festival (1 Nov)
old_anchor = """    <div class="sum-row">
      <div class="sum-when">Aug – Oct 2026</div>
      <div class="sum-name">Marketing Collateral Preparation — <span class="it">renderings, photos, films, and the masterplan model.</span></div>
    </div>
    <div class="sum-row" style="background:rgba(184,148,88,.06);border-top:1px solid rgba(184,148,88,.32)">
      <div class="sum-when" style="color:var(--gold-lt)">1 November 2026 · Activation</div>
      <div class="sum-name">Pru Farm Festival — <span class="it">a celebration moment at the property.</span></div>
    </div>"""

new_anchor = """    <div class="sum-row">
      <div class="sum-when">Aug – Oct 2026</div>
      <div class="sum-name">Marketing Collateral Preparation — <span class="it">renderings, photos, films, and the masterplan model.</span></div>
    </div>
    <div class="sum-row" style="background:rgba(184,148,88,.06);border-top:1px solid rgba(184,148,88,.32)">
      <div class="sum-when" style="color:var(--gold-lt)">Sep – Oct 2026 &middot; Launch</div>
      <div class="sum-name">Renovated Trisara Wellness — <span class="it">the new brand opens in the existing property.</span></div>
    </div>
    <div class="sum-row" style="background:rgba(184,148,88,.06)">
      <div class="sum-when" style="color:var(--gold-lt)">1 November 2026 · Activation</div>
      <div class="sum-name">Pru Farm Festival — <span class="it">a celebration moment at the property.</span></div>
    </div>"""

if old_anchor in text:
    text = text.replace(old_anchor, new_anchor)
    print("✓ Trisara Launch row inserted")
else:
    print("⚠ Trisara insertion anchor not found")

# ─── 3. UPDATE CONTINUING COMMUNICATIONS COPY ────────────────────────────
old_cc = "Continuing Communications — <span class=\"it\">Membership Club and Wellness Retreat enter the public picture.</span>"
new_cc = "Continuing Communications — <span class=\"it\">the SARA Collective enters cultural conversation, into 2027.</span>"
if old_cc in text:
    text = text.replace(old_cc, new_cc)
    print("✓ Continuing Communications copy updated")
else:
    print("⚠ Continuing Communications copy not found")

# ─── 4. UPDATE HEADLINE COUNT (Twelve → Thirteen) ────────────────────────
old_headline = '<div class="D2" style="max-width:920px;margin-bottom:18px">Twelve initiatives. <span class="it gd">One brand system. One year.</span></div>'
new_headline = '<div class="D2" style="max-width:920px;margin-bottom:18px">Thirteen initiatives. <span class="it gd">One brand system. One year.</span></div>'
if old_headline in text:
    text = text.replace(old_headline, new_headline)
    print("✓ Summary headline updated")
else:
    print("⚠ Summary headline not found")

# ─── 5. END CARD BODY — REMOVE PRESS CONFERENCE REFERENCE ────────────────
old_end_body = "The Press Conference on 1 November sets the stage. Summit week (10–13 November) recruits the room. The work that holds the position runs through Q1 2027."
new_end_body = "The Renovated Trisara Wellness opens in Sep&ndash;Oct. The Pru Farm Festival on 1 November celebrates the property. Summit week (10&ndash;13 November) recruits the room. The work that holds the position runs through Q1 2027."
if old_end_body in text:
    text = text.replace(old_end_body, new_end_body)
    print("✓ End card body updated")
else:
    print("⚠ End card body not found")

# ─── 6. END CARD SUBTITLE COUNT (Twelve → Thirteen) ──────────────────────
old_end_sub = "Twelve initiatives. Three key activations. One brand system in motion."
new_end_sub = "Thirteen initiatives. Three key activations. One brand system in motion."
if old_end_sub in text:
    text = text.replace(old_end_sub, new_end_sub)
    print("✓ End card subtitle updated")
else:
    print("⚠ End card subtitle not found")

HTML_PATH.write_text(text)
print("\nDone.")
