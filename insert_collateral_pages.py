"""
Insert 4 new pages after the SARA Direction page (21):
  22 — Intro to the Collateral Set Sample
  23 — Group A: Identity Core (3 items)
  24 — Group B: Print & Hospitality (3 items)
  25 — Group C: Product, Event & Audience (3 items)

Each item card carries: title, use case, placeholder image, photo direction, artwork direction.
Subsequent pages 22-29 → 26-33.
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")

# ─── CSS ADDITIONS ──────────────────────────────────────────────────────
NEW_CSS = """
/* ───── COLLATERAL SET SAMPLE ───── */
.coll-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:42px}
.coll-card{background:var(--ink);padding:30px 28px;display:flex;flex-direction:column;gap:14px;position:relative;min-height:780px}
.coll-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:var(--gold-lt);line-height:1;letter-spacing:.04em}
.coll-tag{font-family:'Jost',sans-serif;font-weight:200;font-size:.54rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);line-height:1.5;margin-top:-4px}
.coll-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.42rem;color:var(--white);line-height:1.2;margin-top:6px;margin-bottom:6px}
.coll-name .it{font-style:italic;color:var(--gold-lt)}
.coll-placeholder{aspect-ratio:4/5;background:radial-gradient(ellipse at 50% 30%,rgba(110,130,100,.08),transparent 65%),radial-gradient(ellipse at 60% 80%,rgba(184,148,88,.06),transparent 60%),linear-gradient(135deg,#0e131a 0%,#141c22 100%);border:1px solid rgba(184,148,88,.22);position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;margin:8px 0 14px}
.coll-crop{position:absolute;width:14px;height:14px;border-color:rgba(184,148,88,.55);border-style:solid;border-width:0}
.coll-crop.tl{top:10px;left:10px;border-top-width:1px;border-left-width:1px}
.coll-crop.tr{top:10px;right:10px;border-top-width:1px;border-right-width:1px}
.coll-crop.bl{bottom:10px;left:10px;border-bottom-width:1px;border-left-width:1px}
.coll-crop.br{bottom:10px;right:10px;border-bottom-width:1px;border-right-width:1px}
.coll-await{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:rgba(244,239,229,.4);text-align:center;padding:0 24px;line-height:1.4;margin-bottom:14px}
.coll-format{font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.36em;text-transform:uppercase;color:var(--gold);line-height:1.5;position:absolute;bottom:14px;left:50%;transform:translateX(-50%);white-space:nowrap}
.coll-block{display:flex;flex-direction:column;gap:5px;padding-top:6px;border-top:1px solid rgba(184,148,88,.12)}
.coll-block:first-of-type{border-top:0}
.coll-block-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.coll-block-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.7rem;line-height:1.7;color:rgba(255,255,255,.72)}
/* Collateral intro page */
.coll-intro-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:42px}
.coll-intro-cell{background:var(--ink);padding:32px 30px;display:flex;flex-direction:column;gap:12px;min-height:300px}
.coll-intro-h{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.coll-intro-title{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.45rem;color:var(--white);line-height:1.2;margin-bottom:6px}
.coll-intro-title .it{font-style:italic;color:var(--gold-lt)}
.coll-intro-list{display:flex;flex-direction:column;gap:9px;margin-top:6px}
.coll-intro-row{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.6;color:rgba(255,255,255,.7);display:grid;grid-template-columns:24px 1fr;gap:10px;align-items:baseline}
.coll-intro-row .n{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:var(--gold-lt);line-height:1}
"""

# ─── ITEM DATA ───────────────────────────────────────────────────────────
GROUPS = [
    {
        "letter": "A",
        "title": "Identity Core",
        "subtitle": "How SARA shows itself.",
        "items": [
            {
                "num": "01",
                "tag": "Identity foundation",
                "name": "Wordmark <span class='it'>&middot;</span> Master Logo",
                "format": "Landscape · 4:3",
                "photo": "Studio macro of the SARA wordmark, foil-stamped in gold on cream linen card. Raking low-angle light from the left to catch the foil grain. Single light source. Subject centred, generous negative space around. Background: cream linen at the same tone, slightly out of focus.",
                "artwork": "Wordmark set in Cormorant Garamond Italic 200, gold (#B89458) on cream (#F4EFE5). Wordmark at 60% card width. Below: a thin gold rule, 40mm wide. Below the rule: &ldquo;A platform of living well&rdquo; in Jost 200, 9pt, letter-spaced uppercase, gold.",
            },
            {
                "num": "02",
                "tag": "The printed conscience",
                "name": "Brand Book <span class='it'>&middot;</span> Manifesto Spread",
                "format": "Landscape · 16:9",
                "photo": "Top-down photograph of a soft-cover linen book lying open on a teak table. Natural diffused window light from the upper-left. Beside the book: a brass measuring cup, a sprig of pandan, a porcelain teacup with green tea. Book occupies 70% of frame; objects frame the negative space at the right edge.",
                "artwork": "Spread layout. Left page: SARA wordmark in gold foil on cream stock, centred, with the manifesto title &ldquo;A platform of living well&rdquo; in italic Cormorant beneath. Right page: a single justified paragraph (Cormorant 11pt, line-height 1.6) — the SARA origin paragraph. Margins 25mm. Page numbers in Jost 200, 7pt, gold.",
            },
            {
                "num": "03",
                "tag": "Direction sheet",
                "name": "Photography <span class='it'>&middot;</span> Style Sheet",
                "format": "Portrait · A4",
                "photo": "A printed style sheet laid flat on a stone surface. The sheet shows three photographic panels — top: a hand cupping water (ritual layer); middle: a wide landscape of the Pru farm at golden hour (landscape layer); bottom: a close-up of a hand-thrown bowl with a single mango (material layer). Stone surface lightly textured; soft diffused overhead light.",
                "artwork": "A4 cream paper sheet. Header: &ldquo;SARA · Photography Direction&rdquo; in Cormorant 16pt. Three-panel grid below — each panel 60mm &times; 40mm. Captions in Jost 200, letter-spaced: &ldquo;Ritual&rdquo; / &ldquo;Landscape&rdquo; / &ldquo;Material.&rdquo; Footer in italic gold: &ldquo;Refuse lifestyle stock, drone-glamour, over-saturated colour.&rdquo;",
            },
        ],
    },
    {
        "letter": "B",
        "title": "Print &amp; Hospitality",
        "subtitle": "How SARA touches the hand.",
        "items": [
            {
                "num": "04",
                "tag": "The quiet daily presence",
                "name": "Stationery <span class='it'>Suite</span>",
                "format": "Landscape · 4:3 flatlay",
                "photo": "Top-down flatlay on natural linen background. Suite composed of A4 letterhead (upper-left), envelope (upper-right, hand-addressed), business card (lower-left, foil side up), with-compliments slip (lower-right). Soft diffused side light from the right at golden hour. A brass pen rests beside the pieces; a single sprig of jasmine sits on the envelope.",
                "artwork": "All pieces share the same identity. Wordmark in Cormorant Italic, gold foil, top-left, with a thin gold rule beneath. Sender details in Jost 200, 8pt, ink black. Business card 85&times;55mm, cream Wove 350gsm. Envelope: cream, Italian Diamond fold. Letterhead: cream, 100gsm. With-compliments: cream, half-letter.",
            },
            {
                "num": "05",
                "tag": "The arrival document",
                "name": "Welcome <span class='it'>Book</span>",
                "format": "Portrait · 200×280mm",
                "photo": "The book held in two mature hands at chest height, against a soft-focus arrival lobby (warm light, teak panelling, sage-green plant). Hands wear a single brass ring. Soft natural light, side rim light on the book edge. The cover faces camera, slight downward tilt as if about to be opened.",
                "artwork": "Hardcover, linen-wrapped in deep forest green. Front: blind-embossed SARA wordmark (no foil), upper-third. Below: &ldquo;Welcome&rdquo; in italic Cormorant 18pt, gold foil. Below: &ldquo;A book for your stay&rdquo; in Jost 200, 9pt, letter-spaced, gold. Spine: SARA wordmark vertical in gold foil. Back cover: a single Cormorant italic line — &ldquo;From the Pru, with care.&rdquo;",
            },
            {
                "num": "06",
                "tag": "Environmental brand",
                "name": "Wayfinding <span class='it'>&amp;</span> Signage",
                "format": "Portrait · property",
                "photo": "A vertical brass signpost set into a teak pillar at a path intersection in the property. Tropical foliage behind, out of focus. Golden hour. Side rim light catches the brass edges. Sign in left third of frame; foliage in right two-thirds. Deep depth of field.",
                "artwork": "Brushed brass plate 80&times;220mm, mounted on teak. Wordmark &ldquo;SARA&rdquo; in cast brass, 24pt Cormorant, at the top. Three directional lines below in Jost 200, 10pt letter-spaced uppercase, each followed by an arrow: &ldquo;The Bath House&rdquo; / &ldquo;The Long Table&rdquo; / &ldquo;The Pru Farm.&rdquo; Refuse: backlit signs, decals, plastic, icons.",
            },
        ],
    },
    {
        "letter": "C",
        "title": "Product, Event &amp; Audience",
        "subtitle": "How SARA travels.",
        "items": [
            {
                "num": "07",
                "tag": "The brand travels home",
                "name": "Product <span class='it'>Packaging</span>",
                "format": "Landscape · still life",
                "photo": "Studio still life on a stone slab. Three SARA products grouped in a triangular composition: a glass jar of Pru Honey (250g, amber liquid visible), a cylindrical tin of SARA Tea (90g, brushed forest green), and a small ceramic pot of SARA Balm (50ml, cream ceramic with brass lid). Soft north-facing window light. Background: out-of-focus stone wall, warm grey.",
                "artwork": "One identity system across three formats. Honey jar: clear glass, cream paper label, SARA wordmark in italic Cormorant centred, &ldquo;Pru Honey&rdquo; in Jost 200 letter-spaced caps below, harvest year (&ldquo;Harvest · 2026 · Vol. II&rdquo;). Tea tin: brushed forest green metal, wordmark debossed (no foil), tea name on a slipped-in Jost-typeset card. Balm pot: hand-thrown ceramic, ingredients hand-written underside in gold paint pen.",
            },
            {
                "num": "08",
                "tag": "Pru Farm Festival",
                "name": "Invitation <span class='it'>Suite</span>",
                "format": "Portrait · 110×160mm",
                "photo": "The invitation card held loosely in a hand against the backdrop of the Pru farm at twilight (string lights barely visible in the blur). Card tilted slightly. The hand wears a single brass ring. Card occupies the right two-thirds; twilight farm in soft focus on the left third.",
                "artwork": "Two-piece invitation. Outer envelope: cream linen, hand-addressed in brown ink. Inner card: 110&times;160mm portrait, cream linen-textured stock. Top: &ldquo;Pru Farm Festival&rdquo; in Jost 200 letter-spaced caps, gold foil. Centre: a fine pen-and-ink botanical illustration of a pandan leaf (commissioned). Below: &ldquo;An evening at the farm · 24 October 2026 · From sundown&rdquo; in Cormorant italic. Bottom: thin gold rule, then &ldquo;SARA · Tri Vananda · Phuket&rdquo; in Jost 8pt.",
            },
            {
                "num": "09",
                "tag": "Hero campaign",
                "name": "Magazine <span class='it'>Spread</span>",
                "format": "Landscape · double-page",
                "photo": "A two-page magazine spread photographed flat from above. Left page: a single hero photograph of a Thai-Italian breakfast table at Pru, with multi-generational hands reaching across (three generations visible by hands and forearms only, no faces). Right page: cream, with a single italic Cormorant line centred. The open magazine rests on a stone surface beside a brass pen and a teacup.",
                "artwork": "Full-bleed photography on the left page. Right page: 80% negative cream space. A single line of copy in Cormorant Garamond Italic 200, 24pt, centred horizontally and vertically: &ldquo;A platform of living well.&rdquo; Bottom of the right page: SARA wordmark in gold foil, 10mm tall. Below the wordmark: &ldquo;Phuket · Andaman · Pru&rdquo; in Jost 200, 7pt, letter-spaced, gold. No URL. No phone number. No body copy.",
            },
        ],
    },
]

# ─── HTML BUILDERS ───────────────────────────────────────────────────────
def build_intro(page_num):
    group_cells = []
    for grp in GROUPS:
        items_html = "\n".join([
            f"""        <div class="coll-intro-row"><span class="n">{i["num"]}</span><span>{i["name"].replace("<span class='it'>","").replace("</span>","")}</span></div>"""
            for i in grp["items"]
        ])
        group_cells.append(f"""    <div class="coll-intro-cell">
      <div class="coll-intro-h">Group {grp["letter"]}</div>
      <h3 class="coll-intro-title">{grp["title"]} <span class="it">— {grp["subtitle"].rstrip(".")}</span></h3>
      <div class="coll-intro-list">
{items_html}
      </div>
    </div>""")
    intro_grid = "\n".join(group_cells)
    return f"""
<!-- ═══════════════════ {page_num:02d} NEW WELLNESS BRAND · COLLATERAL SET SAMPLE · INTRODUCTION ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">Initiative · New Wellness Brand Development</div>
    <h2 class="D2">Collateral set &mdash; <span class="gd it">a working sample.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Nine sample pieces &mdash; three on identity, three on print and hospitality, three on product, event and audience. Each piece carries a placeholder for the artwork and the photography. The descriptions tell production what to source and what to design, so the brand direction can be translated from page to object without losing fidelity. The point of this section is not to show finished work. It is to prove that the direction can be produced.</div>
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
<!-- ═══════════════════ NEW WELLNESS BRAND · COLLATERAL · GROUP {group["letter"]} · {group["title"].replace("&amp;","&").upper()} ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">Collateral Set Sample · Group {group["letter"]} of 3</div>
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

# ─── EDIT FILE ───────────────────────────────────────────────────────────
text = HTML_PATH.read_text()

# 1) Add CSS before </style>
style_end = "</style>"
text = text.replace(style_end, NEW_CSS + "\n" + style_end, 1)

# 2) Insert new sections after the SARA Direction section (page 21) and before Marketing Collateral
splice_anchor = """  <div class="pg">21</div>
</section>

<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"""

new_splice = f"""  <div class="pg">21</div>
</section>
{new_block}

<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"""

if splice_anchor not in text:
    raise RuntimeError("Splice anchor not found")
text = text.replace(splice_anchor, new_splice, 1)

# 3) Renumber existing pages 22-29 → 26-33 (only AFTER the new block)
anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"
head, _, tail = text.partition(anchor)
for old, new in [(29, 33), (28, 32), (27, 31), (26, 30), (25, 29), (24, 28), (23, 27), (22, 26)]:
    tail = tail.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')
text = head + anchor + tail

HTML_PATH.write_text(text)

# Verify
sections = text.count("<section")
closes = text.count("</section>")
print(f"Sections: {sections} open, {closes} close")
print(f"File size: {len(text):,} chars")
