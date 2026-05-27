"""
Replace pages 22-25 (collateral set sample) with digital campaign sample:
  22 — Intro
  23 — Ad (3 placements)
  24 — Landing Page (3 sections)
  25 — Social Media (3 formats)
Page count stays the same; no renumbering required.
"""

from pathlib import Path
import re

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")

# ─── GROUPS ──────────────────────────────────────────────────────────────
GROUPS = [
    {
        "letter": "A",
        "title": "Ad",
        "subtitle": "How SARA enters culture.",
        "items": [
            {
                "num": "01",
                "tag": "Paid social hero",
                "name": "Hero <span class='it'>Digital Ad</span>",
                "format": "Landscape · 1200&times;628",
                "photo": "A single hero photograph &mdash; multi-generational hands reaching across a long table laden with breakfast at Pru. Three generations visible by hands and forearms only; no faces. Soft window light, raked from the right. Tropical foliage in soft focus behind.",
                "artwork": "1200&times;628 canvas. Full-bleed photograph on the left two-thirds. Right one-third: dark forest-green block. On the green: SARA wordmark at top in gold foil-effect. Below: italic Cormorant &ldquo;A culture begins.&rdquo; Bottom-right: thin gold rule and &ldquo;Phuket &middot; 2027 &middot; Founding cohort opening.&rdquo; in Jost 9pt letter-spaced caps.",
            },
            {
                "num": "02",
                "tag": "Premium display network",
                "name": "Programmatic <span class='it'>Skyscraper</span>",
                "format": "Portrait · 300&times;600",
                "photo": "A vertical photograph of a single hand &mdash; older, slightly weathered &mdash; touching a pandan leaf in golden-hour light. Background: out-of-focus Pru farmland in deep green.",
                "artwork": "300&times;600 vertical canvas. Photo occupies the upper 60% of the frame. Lower 40%: forest-green block. SARA wordmark gold, top of block. Italic Cormorant headline: &ldquo;The Culture of Living Well.&rdquo; Below: Jost 200 letter-spaced caps, 9pt: &ldquo;Begin the practice.&rdquo; Below: thin gold rule. Bottom: &ldquo;sara.com&rdquo; in Jost gold.",
            },
            {
                "num": "03",
                "tag": "Instagram feed promotion",
                "name": "Paid Social <span class='it'>Square</span>",
                "format": "Square · 1080&times;1080",
                "photo": "A top-down flatlay of a SARA breakfast moment &mdash; hand-thrown ceramic bowl with a single mango, brass teaspoon, linen napkin, sprig of pandan, cup of green tea. Stone surface. Soft natural light from the upper-left.",
                "artwork": "1080&times;1080 square. Photo fills the canvas. Lower-third overlay: a subtle linear gradient from transparent to dark forest. Lower-right corner: SARA wordmark gold, italic Cormorant subtitle &ldquo;A culture begins.&rdquo;, and small CTA &ldquo;Join the founding cohort &rarr;&rdquo; in Jost 200 letter-spaced caps.",
            },
        ],
    },
    {
        "letter": "B",
        "title": "Landing Page",
        "subtitle": "Where SARA gathers attention.",
        "items": [
            {
                "num": "04",
                "tag": "First impression",
                "name": "Hero <span class='it'>Section</span>",
                "format": "Desktop · 1440&times;900",
                "photo": "Full-bleed hero photograph: a wide landscape of the Pru farm at the moment between golden hour and twilight. A single figure (silhouette only) walks down a path between rice paddies. Mountains deep in the background. A sliver of Andaman blue visible at the horizon.",
                "artwork": "1440&times;900 desktop view. Photograph full-bleed. Top: minimal navigation bar &mdash; SARA wordmark left; four nav items right (The Culture &middot; The Practice &middot; Membership &middot; Visit) in Jost 200 letter-spaced caps 11pt. Centre: italic Cormorant headline &ldquo;The Culture of Living Well&rdquo; at 6vw. Below: Jost subtitle &ldquo;A luxury wellness practice for the multigenerational family.&rdquo; Bottom-left: a small scroll cue arrow.",
            },
            {
                "num": "05",
                "tag": "What SARA is",
                "name": "Proposition <span class='it'>Section</span>",
                "format": "Desktop · 1440&times;800",
                "photo": "A wide horizontal photograph of three pairs of hands &mdash; three generations &mdash; reaching across a hand-thrown ceramic bowl at the centre of a stone table. Single light source. The bowl reads as the gravitational centre; the three pairs of hands create a triangular dynamic around it.",
                "artwork": "1440&times;800 frame. Cream background. Photo occupies the right two-thirds. Left third: italic Cormorant heading &ldquo;A culture, not a treatment.&rdquo; Below: justified Jost paragraph (300 weight, 13pt, line-height 1.7): &ldquo;SARA is the practice of living well, designed for generations who choose to live well together. From the Andaman tides to a working farm called Pru, it is a culture built on family, terroir, and the discipline of returning to what truly matters.&rdquo;",
            },
            {
                "num": "06",
                "tag": "Conversion",
                "name": "Membership <span class='it'>Section</span>",
                "format": "Desktop · 1440&times;600",
                "photo": "A close-up still life: a brass key on a folded square of cream linen, beside a hand-bound member&rsquo;s pamphlet. Soft top-down light. Stone table surface. Warm and quiet.",
                "artwork": "1440&times;600 frame. Forest green background. Centre-aligned content. Cormorant italic heading: &ldquo;Founding members open Q4 2026.&rdquo; Below: a single Jost 200 paragraph &mdash; &ldquo;An invitation to live the culture from the first day. Five hundred members, by sponsorship or interview.&rdquo; Below: a sparse button &mdash; gold border, transparent fill, &ldquo;Begin &rarr;&rdquo; in Jost 200 letter-spaced caps 12pt. Below button: small footnote &ldquo;sara.com/founding&rdquo; in gold.",
            },
        ],
    },
    {
        "letter": "C",
        "title": "Social Media",
        "subtitle": "How SARA shows up daily.",
        "items": [
            {
                "num": "07",
                "tag": "Daily presence",
                "name": "Instagram <span class='it'>Feed Post</span>",
                "format": "Square · 1080&times;1080",
                "photo": "A close-up of a senior woman&rsquo;s hands cradling a cup of tea in soft window light from the left. The cup is hand-thrown ceramic, the colour of stone. Her hands are at rest, not posed. Background: out-of-focus, warm cream.",
                "artwork": "1080&times;1080 photograph, full-bleed. No overlay text on the image itself &mdash; the brand voice lives in the caption. Caption (plain text, Instagram feed): &ldquo;There is a difference between rest and pause. SARA is the practice of rest.&rdquo; Caption signed: &ldquo;&mdash; from the Pru.&rdquo;",
            },
            {
                "num": "08",
                "tag": "Ephemeral storytelling",
                "name": "Story <span class='it'>/ Reel Cover</span>",
                "format": "Vertical · 1080&times;1920",
                "photo": "A still frame from a slow-motion video: morning light catching the steam from a kettle being poured into a teapot at the long table at Pru. Foreground sharp, background soft. A second hand reaches in from the right edge of frame.",
                "artwork": "1080&times;1920 vertical canvas. Photo / video full-bleed. Upper third: italic Cormorant Garamond overlay &ldquo;A small ritual.&rdquo; Below: Jost 200 letter-spaced caps subtitle &ldquo;Morning at the long table &middot; Episode 04.&rdquo; Bottom: SARA wordmark gold, very small, with thin gold rule. Tap-to-progress dots at top of frame.",
            },
            {
                "num": "09",
                "tag": "Educational sequence",
                "name": "Carousel <span class='it'>Post</span>",
                "format": "Square × 5 · 1080&times;1080",
                "photo": "A five-slide sequence. Slide 1 title card: cream background. Slide 2: a hand on a chest, breath. Slide 3: a wide table with morning food. Slide 4: a body in motion (a single yoga pose, late light). Slide 5: stone, water, dusk. Each slide a single restrained image &mdash; ritual, table, movement, stillness.",
                "artwork": "Five-slide square sequence. Slide 1 (title): cream background, italic Cormorant &ldquo;The SARA Method&rdquo; with gold underline. Slides 2&ndash;4: full-bleed photographs with overlay copy at bottom in Jost 200 letter-spaced caps: &ldquo;Breath.&rdquo; &middot; &ldquo;Table.&rdquo; &middot; &ldquo;Body.&rdquo; Slide 5: cream background with a single Cormorant italic line: &ldquo;A culture, practised daily. &rarr; sara.com/founding&rdquo;",
            },
        ],
    },
]

# ─── HTML BUILDERS ───────────────────────────────────────────────────────
def build_intro(page_num):
    group_cells = []
    for grp in GROUPS:
        items_html = "\n".join([
            f"""        <div class="coll-intro-row"><span class="n">{i["num"]}</span><span>{re.sub(r"<[^>]+>", "", i["name"]).strip()}</span></div>"""
            for i in grp["items"]
        ])
        group_cells.append(f"""    <div class="coll-intro-cell">
      <div class="coll-intro-h">Group {grp["letter"]} &middot; {grp["title"]}</div>
      <h3 class="coll-intro-title">{grp["title"]} <span class="it">&mdash; {grp["subtitle"].rstrip(".")}</span></h3>
      <div class="coll-intro-list">
{items_html}
      </div>
    </div>""")
    intro_grid = "\n".join(group_cells)
    return f"""
<!-- ═══════════════════ {page_num:02d} NEW WELLNESS BRAND · DIGITAL CAMPAIGN SAMPLE · INTRODUCTION ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">Initiative · New Wellness Brand Development</div>
    <h2 class="D2">Digital campaign sample &mdash; <span class="gd it">a working sample.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Nine digital placements &mdash; three ads, three landing-page sections, three social formats &mdash; under one campaign idea: <em>a culture begins</em>. Each piece carries a placeholder for the artwork and the photography. The descriptions tell production what to source and what to design, so the brand identity can be translated from page to pixel without losing fidelity. The point of this section is not to show finished work. It is to prove that the SARA identity can be produced &mdash; digitally.</div>
    <div class="coll-intro-grid">
{intro_grid}
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

def build_group(group, page_num):
    cards = []
    for item in group["items"]:
        cards.append(f"""    <div class="coll-card">
      <div class="coll-num">&mdash; {item["num"]} &mdash;</div>
      <div class="coll-tag">{item["tag"]}</div>
      <h4 class="coll-name">{item["name"]}</h4>
      <div class="coll-placeholder">
        <div class="coll-crop tl"></div><div class="coll-crop tr"></div>
        <div class="coll-crop bl"></div><div class="coll-crop br"></div>
        <div class="coll-await">Awaiting photography<br>+ artwork</div>
        <div class="coll-format">{item["format"]}</div>
      </div>
      <div class="coll-block">
        <div class="coll-block-label">Photo direction</div>
        <div class="coll-block-text">{item["photo"]}</div>
      </div>
      <div class="coll-block">
        <div class="coll-block-label">Artwork direction</div>
        <div class="coll-block-text">{item["artwork"]}</div>
      </div>
    </div>""")
    cards_html = "\n".join(cards)
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · DIGITAL CAMPAIGN · GROUP {group["letter"]} · {group["title"].upper()} ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">Digital Campaign Sample &middot; Group {group["letter"]} of 3</div>
    <div class="cat-head">
      <div class="cat-head-left">
        <div class="cat-num">&mdash; {group["letter"]} &mdash;</div>
        <h2 class="cat-name">{group["title"]}</h2>
      </div>
      <div class="cat-q">{group["subtitle"]}</div>
    </div>
    <div class="coll-grid">
{cards_html}
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

# ─── ASSEMBLE ────────────────────────────────────────────────────────────
parts = [build_intro(22)]
page = 23
for grp in GROUPS:
    parts.append(build_group(grp, page))
    page += 1
new_block = "\n".join(parts)

# ─── DO THE EDITS ────────────────────────────────────────────────────────
text = HTML_PATH.read_text()

# Replace the 4 collateral pages (22-25) with the new 4 digital campaign pages.
# Anchor: from the collateral intro comment through to (but not including) marketing collateral section.
old_start = "<!-- ═══════════════════ 22 NEW WELLNESS BRAND · COLLATERAL SET SAMPLE · INTRODUCTION ═══════════════════ -->"
old_end_anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"

if old_start not in text or old_end_anchor not in text:
    raise RuntimeError("Could not find collateral block boundaries")

start_idx = text.index(old_start)
end_idx = text.index(old_end_anchor)
text = text[:start_idx] + new_block.lstrip() + "\n\n" + text[end_idx:]

HTML_PATH.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
print(f"File size: {len(text):,} chars")
