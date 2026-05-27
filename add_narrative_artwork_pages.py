"""
Add 3 sample-artwork pages, one after each of the three Narrative options.
Each artwork page shows the relevant narrative-NN.jpg as a full-bleed background,
with PATTAMA wordmark + tagline + sub-tagline overlaid in restrained scale.
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── NEW CSS for artwork sample pages ────────────────────────────────────
NEW_CSS = """
/* ───── NARRATIVE · SAMPLE ARTWORK PAGES ───── */
.S.artwork{padding:0;min-height:100vh;position:relative;display:block;background:#000;overflow:hidden}
.artwork-bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:1}
.artwork-bg::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,15,19,.25) 0%,rgba(11,15,19,.35) 50%,rgba(11,15,19,.7) 100%);z-index:2}
.artwork-overlay{position:absolute;inset:0;z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:80px}
.artwork-mark{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(2.8rem,5.5vw,4.6rem);color:var(--gold-lt);line-height:1;letter-spacing:.025em;margin-bottom:6px;text-shadow:0 2px 18px rgba(11,15,19,.4)}
.artwork-rule{width:50px;height:1px;background:var(--gold);margin:18px 0 18px;opacity:.85}
.artwork-tagline{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(1rem,1.5vw,1.35rem);color:rgba(255,255,255,.92);line-height:1.4;letter-spacing:.005em;margin-bottom:10px;text-shadow:0 1px 12px rgba(11,15,19,.5)}
.artwork-subtagline{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(.82rem,1.1vw,.98rem);color:rgba(255,255,255,.7);line-height:1.5;max-width:480px;text-shadow:0 1px 10px rgba(11,15,19,.5)}
.artwork-caption{position:absolute;bottom:32px;left:0;right:0;text-align:center;font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.42em;text-transform:uppercase;color:rgba(255,255,255,.45);z-index:4}
.S.artwork .pg{color:rgba(255,255,255,.35);z-index:5}
"""

text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── ARTWORK PAGE TEMPLATES ──────────────────────────────────────────────
OPTIONS = [
    {
        "n": 1,
        "image": "narrative-01.jpg",
        "tagline": "Living Well Begins Together",
        "subtagline": "The meaningful aspects of life for the multigenerational family.",
    },
    {
        "n": 2,
        "image": "narrative-02.jpg",
        "tagline": "Living Well, Awakening Together",
        "subtagline": "The slow unfolding of meaningful life &mdash; for the multigenerational family.",
    },
    {
        "n": 3,
        "image": "narrative-03.jpg",
        "tagline": "Living Well, Generation After Generation",
        "subtagline": "A living tradition of meaningful life &mdash; for the multigenerational family.",
    },
]

def build_artwork_page(opt, page_num):
    return f"""<!-- ═══════════════════ NEW WELLNESS BRAND · THE NARRATIVE · OPTION {opt['n']} · SAMPLE ARTWORK ═══════════════════ -->
<section class="S artwork">
  <div class="artwork-bg" style="background-image:url('images/{opt['image']}')"></div>
  <div class="artwork-overlay">
    <div class="artwork-mark">PATTAMA</div>
    <div class="artwork-rule"></div>
    <div class="artwork-tagline">{opt['tagline']}</div>
    <div class="artwork-subtagline">{opt['subtagline']}</div>
  </div>
  <div class="artwork-caption">Sample artwork &middot; The Narrative &middot; Option {opt['n']}</div>
  <div class="pg">{page_num:02d}</div>
</section>"""

# ─── INSERT ARTWORK PAGE AFTER EACH OPTION ───────────────────────────────
# Existing anchors for the three Option pages' closing </section>:
# - Option 1 (pg 05) → insert artwork after it (becomes pg 06)
# - Option 2 (was pg 06, now pg 07 after insertion) → insert artwork after (becomes pg 08)
# - Option 3 (was pg 07, now pg 09 after two insertions) → insert artwork after (becomes pg 10)

# We'll insert one at a time, starting from the LAST option to avoid shifting issues
# Actually simpler: insert each artwork page right after its option's </section>,
# working from option 3 backwards so the anchors don't shift.

# Find the Option section comments
option_anchors = [
    "<!-- ═══════════════════ 07 NEW WELLNESS BRAND · THE NARRATIVE · OPTION 3 · THE FAMILY NAME ═══════════════════ -->",
    "<!-- ═══════════════════ 06 NEW WELLNESS BRAND · THE NARRATIVE · OPTION 2 · THE LOTUS ═══════════════════ -->",
    "<!-- ═══════════════════ 05 NEW WELLNESS BRAND · THE TAGLINE · OPTION 1 ═══════════════════ -->",
]

# Option 1's section comment still uses TAGLINE because we only updated 5's eyebrow not its comment
# Let me check both possible names
fallback_anchors_opt1 = [
    "<!-- ═══════════════════ 05 NEW WELLNESS BRAND · THE TAGLINE · OPTION 1 ═══════════════════ -->",
    "<!-- ═══════════════════ 05 NEW WELLNESS BRAND · THE NARRATIVE · OPTION 1 ═══════════════════ -->",
    "<!-- ═══════════════════ 05 NEW WELLNESS BRAND · THE NAME ═══════════════════ -->",
]

# Working from Option 3 backwards: find each </section> following the option anchor
def insert_after_section(text, section_anchor, new_html):
    if section_anchor not in text:
        return text, False
    start = text.index(section_anchor)
    # Find the </section> that closes THIS section
    end = text.index("</section>", start) + len("</section>")
    return text[:end] + "\n" + new_html + text[end:], True

# Insert Option 3 artwork (page after option 3, which is currently pg 07)
opt3 = OPTIONS[2]
artwork_html_3 = build_artwork_page(opt3, 8)  # will become pg 08 after insertion
text, ok = insert_after_section(text, option_anchors[0], artwork_html_3)
print(f"Option 3 artwork inserted: {ok}")

# Insert Option 2 artwork (after option 2, currently pg 06)
opt2 = OPTIONS[1]
artwork_html_2 = build_artwork_page(opt2, 7)  # will become pg 07
text, ok = insert_after_section(text, option_anchors[1], artwork_html_2)
print(f"Option 2 artwork inserted: {ok}")

# Insert Option 1 artwork (after option 1, currently pg 05)
opt1 = OPTIONS[0]
artwork_html_1 = build_artwork_page(opt1, 6)  # will become pg 06
ok = False
for anchor in fallback_anchors_opt1:
    text, ok = insert_after_section(text, anchor, artwork_html_1)
    if ok:
        print(f"Option 1 artwork inserted (anchor: {anchor[:60]}...)")
        break
if not ok:
    print("⚠ Option 1 artwork NOT inserted — anchor not found")

# Now renumber pages AFTER the option 3 artwork (i.e., from old pg 08 onward)
# Currently after our 3 insertions:
# - pg 05 (Option 1)
# - pg 06 (NEW artwork 1)
# - pg 06 (Option 2 - duplicate temporarily, need to renumber)
# Wait this won't be right because the option pages still say pg 05/06/07.

# Actually let's recount what we have:
# Option 1 page has pg "05" (unchanged)
# After insert: NEW artwork page with pg "06" (we set)
# Option 2 page has pg "06" (was 06 before)  ← DUPLICATE!
# After insert: NEW artwork page with pg "07" (we set)
# Option 3 page has pg "07" (was 07 before)  ← DUPLICATE!
# After insert: NEW artwork page with pg "08" (we set)
# Then OLD pg "08" (Org Structure) ← DUPLICATE!

# We need to renumber so that:
# Option 1 = 05, Artwork 1 = 06, Option 2 = 07, Artwork 2 = 08, Option 3 = 09, Artwork 3 = 10, Org Structure = 11, etc.

# So options 2 and 3 need to be renumbered to 07 and 09 respectively.
# And subsequent pages 08 onward need to shift by 3.

# Better approach: do the renumbering AFTER all insertions.

# Strategy: find each section in turn and adjust its pg number.
# To avoid double-replacement, work from the highest number down.

# Step 1: shift old pg 08+ → pg 11+ (anything in original deck that was pg 08 onward becomes 11 onward)
# Actually old pg 08 (Org Structure) needs to become 11
# Old pg 09 → 12
# Old pg 10 → 13
# ...
# Old pg 33 → 36

# Renumber high to low to avoid collisions
import re

# First, find the boundary: anything AFTER our 3rd artwork insertion needs +3 numbering
# But we already set our 3 artwork pages to 06, 07, 08 — those are the NEW correct numbers.
# Wait — our artwork pages are:
#   Artwork 1 → pg 06 (correct, between Option 1 [05] and Option 2)
#   Artwork 2 → pg 07
#   Artwork 3 → pg 08
# But Option 2 page still has pg 06, Option 3 has pg 07 — they need to be updated to 07 and 09 respectively.

# Let me just rebuild this step-by-step using a different approach.
# 1. Update Option 2 page pg from 06 to 07
# 2. Artwork 2 (already 07) needs to be 08
# 3. Update Option 3 page pg from 07 to 09
# 4. Artwork 3 (already 08) needs to be 10
# 5. Update everything from old pg 08 onward to +3

# Hmm this is getting tangled. Let me just renumber EVERYTHING after Option 1 in correct sequence.

# Find page 05 (Option 1) — that's our anchor. Everything after should be renumbered fresh.
# Get all pg occurrences after that
text_before, _, text_after_pg5 = text.partition('<div class="pg">05</div>')

# Now in text_after_pg5, the FIRST pg should be 06 (our Artwork 1), then 07 (Option 2), then 08, etc.
# But the actual values are: 06 (Artwork 1), 06 (Option 2), 07 (Artwork 2), 07 (Option 3), 08 (Artwork 3), 08 (Org Structure was 08), 09 (was 09), etc.

# We want: 06, 07, 08, 09, 10, 11, 12, ...
# To get this, replace pg occurrences in order, one at a time, with incrementing numbers.

def renumber_pg_sequential(text_after, start_num):
    """Replace each <div class="pg">XX</div> with sequential numbers starting at start_num."""
    pattern = re.compile(r'<div class="pg">(\d{2})</div>')
    counter = [start_num - 1]
    def repl(m):
        counter[0] += 1
        return f'<div class="pg">{counter[0]:02d}</div>'
    return pattern.sub(repl, text_after)

text_after_renumbered = renumber_pg_sequential(text_after_pg5, 6)

text = text_before + '<div class="pg">05</div>' + text_after_renumbered

V2.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"\nSections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
