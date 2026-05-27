"""
Insert 13 new pages (intro + 10 category + summary + SARA direction) into the SARA deck
- 30-brand identity study
- Uses images 01.png-30.png from images/ folder
- Renumbers existing pages 09-16 to 22-29
"""

from pathlib import Path
import re

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")

# ─── CSS ADDITIONS ───────────────────────────────────────────────────────
CSS_ADDITIONS = """
/* ───── 30-BRAND STUDY · INTRO ───── */
.study-grid{display:grid;grid-template-columns:repeat(10,1fr);gap:1px;background:rgba(184,148,88,.14);border:1px solid rgba(184,148,88,.2);margin-top:48px}
.study-thumb{aspect-ratio:1/1;background:var(--ink);position:relative;overflow:hidden}
.study-thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.62;transition:opacity .3s ease}
.study-thumb:hover img{opacity:1}
.study-thumb::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,15,19,.15) 0%,rgba(11,15,19,.5) 100%);z-index:1;pointer-events:none}
.study-legend{display:grid;grid-template-columns:repeat(5,1fr);gap:36px;margin-top:48px;padding-top:36px;border-top:1px solid rgba(184,148,88,.15)}
.study-legend-cell{}
.study-legend-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.3rem;color:var(--gold-lt);line-height:1;margin-bottom:8px}
.study-legend-name{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.7);line-height:1.6}

/* ───── 30-BRAND STUDY · CATEGORY PAGE ───── */
.cat-head{display:flex;justify-content:space-between;align-items:flex-end;gap:48px;margin-bottom:48px;padding-bottom:24px;border-bottom:1px solid rgba(184,148,88,.18)}
.cat-head-left{}
.cat-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.05rem;color:var(--gold-lt);line-height:1;letter-spacing:.04em}
.cat-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:clamp(2.2rem,4vw,3.4rem);line-height:1.05;color:var(--white);margin-top:12px}
.cat-q{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.18rem;color:rgba(255,255,255,.6);line-height:1.4;max-width:480px;text-align:right;padding-bottom:8px}
.cat-three{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18)}
.cat-card{background:var(--ink);display:flex;flex-direction:column;position:relative;min-height:520px}
.cat-card.pinned{background:linear-gradient(180deg,var(--ink) 0%,rgba(184,148,88,.04) 100%)}
.cat-pin{position:absolute;top:14px;right:14px;font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--ink);background:var(--gold);padding:5px 10px;border-radius:2px;z-index:3;line-height:1}
.cat-img{aspect-ratio:1/1;position:relative;overflow:hidden;background:#000}
.cat-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.cat-img::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,15,19,0) 0%,rgba(11,15,19,.55) 100%);z-index:1;pointer-events:none}
.cat-body{padding:24px 26px 28px;display:flex;flex-direction:column;gap:12px;flex:1}
.cat-card-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.55rem;color:var(--white);line-height:1.1}
.cat-card.pinned .cat-card-name{color:var(--gold-lt)}
.cat-card-loc{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.26em;text-transform:uppercase;color:rgba(184,148,88,.75);line-height:1.5}
.cat-card-essence{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.02rem;color:rgba(255,255,255,.62);line-height:1.4;padding-top:8px;border-top:1px solid rgba(184,148,88,.14)}
.cat-card-diff{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.65;color:rgba(255,255,255,.78);margin-top:auto;padding-top:14px}
.cat-card-diff-label{display:block;font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin-bottom:6px;line-height:1.5}
.cat-takeaway{margin-top:36px;padding:24px 32px;border-left:2px solid var(--gold);background:rgba(184,148,88,.04);display:flex;align-items:baseline;gap:32px}
.cat-takeaway-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.58rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);flex-shrink:0;white-space:nowrap;line-height:1.6}
.cat-takeaway-text{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.25rem;color:var(--white);line-height:1.4}
.cat-takeaway-text .it{font-style:italic;color:var(--gold-lt)}

/* ───── 30-BRAND STUDY · TEN PATTERNS SUMMARY ───── */
.pat-grid{display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(2,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:48px}
.pat-cell{background:var(--ink);padding:32px 26px;display:flex;flex-direction:column;gap:14px;min-height:280px}
.pat-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:2.4rem;color:var(--gold-lt);line-height:.85}
.pat-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.32rem;color:var(--white);line-height:1.2}
.pat-strap{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.6;color:rgba(255,255,255,.62);margin-top:auto;padding-top:14px;border-top:1px solid rgba(184,148,88,.12)}

/* ───── 30-BRAND STUDY · SARA DIRECTION ───── */
.dir-grid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:48px}
.dir-cell{background:var(--ink);padding:32px 30px;display:flex;flex-direction:column;gap:14px;min-height:280px;position:relative}
.dir-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1rem;color:var(--gold-lt);line-height:1;letter-spacing:.04em}
.dir-tag{font-family:'Jost',sans-serif;font-weight:200;font-size:.58rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin-top:4px;line-height:1.5}
.dir-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.55rem;color:var(--white);line-height:1.2;margin-top:10px}
.dir-name .it{font-style:italic;color:var(--gold-lt)}
.dir-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.82rem;line-height:1.75;color:rgba(255,255,255,.72);margin-top:auto;padding-top:18px}
"""

# ─── BRAND DATA ──────────────────────────────────────────────────────────
# Each tuple: (image_num, brand, location, essence, differentiation, is_pinned_for_sara)
CATEGORIES = [
    {
        "num": "01",
        "name": "Vitality & Longevity",
        "question": "How does a wellness brand earn medical credibility?",
        "takeaway": "SARA's CLP partnership is the <span class='it'>deepest moat</span> in the brand. Surface the science. The clinical core must lead.",
        "brands": [
            ("01", "Clinique La Prairie", "Montreux · 1931", "Swiss longevity laboratory for self-extension.", "Medical institution disguised as hospitality. Nine decades of clinical IP no resort can replicate.", True),
            ("02", "SHA Wellness Clinic", "Alicante · 2008", "Macrobiotic medicine for measurable transformation.", "East-meets-West method named, trademarked, made transferable across continents.", False),
            ("03", "Lanserhof", "Tegernsee · 1984", "F.X. Mayr precision for modern bodies.", "Award-winning architecture functioning as silent brand book. Buildings write the copy.", False),
        ],
    },
    {
        "num": "02",
        "name": "Athletics & Practice",
        "question": "How does movement become an identity?",
        "takeaway": "<span class='it'>Cap</span> SARA Membership. Scarcity creates the room. The room is the product.",
        "brands": [
            ("04", "Equinox", "New York · 1991", "Performance fashion for the urban athlete.", "Provocation as positioning. Builds tribe by being divisive on purpose.", False),
            ("05", "Heimat", "Los Angeles · 2022", "European bathhouse culture, Los Angeles edition.", "Capped at 3,500 members. Scarcity itself is the offer.", True),
            ("06", "Tracy Anderson Method", "New York · 2006", "Cult method for the long, lean body.", "One woman. One method. Fifteen years. Founder credibility is the entire brand.", False),
        ],
    },
    {
        "num": "03",
        "name": "Recovery & Bodywork",
        "question": "How does ritual become the brand?",
        "takeaway": "Atmosphere is the product. Brief the architect on <span class='it'>light, scent, sound</span> — not on the menu.",
        "brands": [
            ("07", "Remedy Place", "Los Angeles · 2019", "Social wellness for the recovery generation.", "Invented the category. Reframed recovery from solo discipline into social currency.", False),
            ("08", "AIRE Ancient Baths", "Multiple cities · 2008", "Candlelit baths in ancient architecture.", "Sells darkness, candlelight, and time. Refuses the wellness vocabulary entirely.", True),
            ("09", "Bathhouse", "Brooklyn · 2019", "Concrete cathedral for cold-warm contrast.", "Gym + spa + restaurant + bar in one building. Hybrid use-cases multiply revenue per guest.", False),
        ],
    },
    {
        "num": "04",
        "name": "Mind & Cognition",
        "question": "How is the inner life made into a product?",
        "takeaway": "SARA needs a <span class='it'>publishable content layer</span> that lives outside the property — book, podcast, film.",
        "brands": [
            ("10", "Open", "Los Angeles · 2018", "Movement and breath, designed beautifully.", "Restraint as positioning. Refuses to do meditation badly in a maximalist category.", False),
            ("11", "The School of Life", "London · 2008", "Emotional intelligence as cultural project.", "Books, classes, journals, cards. Content is the long-tail moat.", True),
            ("12", "Hoffman Institute", "Napa · 1967", "Eight-day deep emotional reset.", "Eight residential days. Length is the filter. Filters wellness tourists out.", False),
        ],
    },
    {
        "num": "05",
        "name": "Detox & Reset",
        "question": "How does discipline become luxury?",
        "takeaway": "Lean on Montara <span class='it'>family lineage</span>. Multi-generational stewardship is a brand asset.",
        "brands": [
            ("13", "Buchinger Wilhelmi", "Überlingen · 1920", "Therapeutic fasting since 1920.", "Four generations. One family. One fast. Lineage equals trust.", True),
            ("14", "Vivamayr", "Maria Wörth · 2004", "Modern Mayr medicine, alpine precision.", "Multi-property platform around one method. Five locations, one Mayr.", False),
            ("15", "The Ranch Malibu", "Malibu · 2010", "Boot-camp wellness for high-output people.", "No menu. No choice. No flexibility. Total prescription for the decision-fatigued.", False),
        ],
    },
    {
        "num": "06",
        "name": "The Table",
        "question": "How does food become philosophy?",
        "takeaway": "The Pru farm is undervalued. <span class='it'>Build products.</span> Let the land travel home with the guest.",
        "brands": [
            ("16", "Noma", "Copenhagen · 2003", "Nordic terroir made into philosophy.", "Invented New Nordic. Owns the terroir narrative. Place itself is the position.", False),
            ("17", "Flamingo Estate", "Los Angeles · 2017", "Garden-to-everything California sensuality.", "A property turned into a brand turned into a product line. The estate is the brand.", True),
            ("18", "Single Thread", "Healdsburg · 2016", "Kaiseki precision on Sonoma farmland.", "Farm plus restaurant plus inn under one couple. Integration itself is the brand.", False),
        ],
    },
    {
        "num": "07",
        "name": "Beauty & Aesthetics",
        "question": "How does a product become a belief?",
        "takeaway": "SARA's <span class='it'>verbal identity</span> matters more than any single programme. Voice is the moat.",
        "brands": [
            ("19", "Aesop", "Melbourne · 1987", "Apothecary intellectualism in amber glass.", "Brand voice is the only true moat. The product is honestly average — the voice is irreproducible.", False),
            ("20", "Augustinus Bader", "Leipzig · 2018", "Stem-cell science from a German laboratory.", "Real professor. Real research. Two SKUs only. $1B valuation in three years.", False),
            ("21", "Le Labo", "New York · 2006", "Hand-blended perfume with your name on it.", "City-exclusive scarcity. Hand-blended in front of you. Place-bound by design.", True),
        ],
    },
    {
        "num": "08",
        "name": "Culture & Learning",
        "question": "How does a club become a creative institution?",
        "takeaway": "<span class='it'>Curate the room.</span> Wrong members destroy faster than wrong architecture can save.",
        "brands": [
            ("22", "Soho House", "London · 1995", "Members' clubs for creative industries.", "Membership committee curation. Money alone does not buy entry. Members are the brand.", True),
            ("23", "The Battery", "San Francisco · 2013", "Tech-built private club with cultural soul.", "Programming is the membership. 200+ events yearly. No photographs allowed.", False),
            ("24", "Annabel's London", "Mayfair · 1963", "Maximalist Mayfair nightclub theatre.", "Maximalism with conviction. Sixty years of social history money cannot buy.", False),
        ],
    },
    {
        "num": "09",
        "name": "Family & Generations",
        "question": "How does luxury include children?",
        "takeaway": "Design SARA for <span class='it'>children first.</span> Multigenerational is the position, not the afterthought.",
        "brands": [
            ("25", "Soneva", "Maldives · 1995", "Barefoot luxury for conscious families.", "Children are the proposition. 'Slow life' philosophy trademarked since 1995.", True),
            ("26", "Soho Farmhouse", "Oxfordshire · 2015", "Cotswold farm reimagined as members' club.", "Cabin format outperforms villa format. Members claim their hut, return seasonally.", False),
            ("27", "Paws Up", "Montana · 2005", "Glamping ranch for legacy American families.", "Invented glamping. 37,000 acres. All-inclusive priced as luxury for three generations.", False),
        ],
    },
    {
        "num": "10",
        "name": "Farm House Real Estate",
        "question": "How does an estate become a brand world?",
        "takeaway": "One owner, one vision, one <span class='it'>obsessive direction.</span> SARA cannot be designed by committee.",
        "brands": [
            ("28", "Castello di Reschio", "Umbria · 1994", "Eight-century estate, family-restored.", "Eight centuries restored by one family. Olive oil, wine, perfume, furniture — the estate as product line.", True),
            ("29", "Babylonstoren", "Franschhoek · 2007", "Working Cape Dutch farm, fully brandified.", "Magazine editor designed it. The 3.5-acre vegetable garden is the brand's hero.", False),
            ("30", "The Newt", "Somerset · 2019", "English country estate, museum-grade.", "Same editor, second act. English country estate brandified to museum-grade detail.", False),
        ],
    },
]

# ─── PATTERNS (Summary page) ─────────────────────────────────────────────
PATTERNS = [
    ("01", "Name the Method", "Turn an experience into intellectual property."),
    ("02", "Own the Terroir", "Claim a specific place — never a vague region."),
    ("03", "Make the Founder Visible", "One obsessive voice. Never a committee."),
    ("04", "Curate the Room", "Membership is the brand. Members are the product."),
    ("05", "Programme the Calendar", "Members pay for what happens, not what is."),
    ("06", "Demand the Commitment", "Length signals seriousness. Filter for the right guests."),
    ("07", "Extend Beyond the Stay", "The brand must travel home with the guest."),
    ("08", "Atmosphere Beats Programming", "Sensory immersion is more memorable than feature lists."),
    ("09", "Reframe the Category", "Don't compete in the space. Invent the space."),
    ("10", "One Method, Many Doors", "A platform brand scales across owned places."),
]

# ─── DIRECTIONS (Suggested Direction for SARA) ───────────────────────────
DIRECTIONS = [
    ("01", "The Category Claim", "Position", "SARA is the <span class='it'>platform of living well.</span>", "Adopt the category claim in the manifesto. Use it in every editorial, pitch, and conversation. Repetition is what makes a category claim stick."),
    ("02", "The Method", "Trademark", "Name and codify <span class='it'>The SARA Method</span> within ninety days.", "Define the phases, duration, daily structure, and expected outcomes. Trademark the name and acronym before external use. Make the protocol referenceable in conversation."),
    ("03", "The Membership", "Curation", "Cap inaugural members at <span class='it'>five hundred.</span>", "Establish a Membership Committee with external curators (designers, doctors, artists, family-office leaders). Admission by sponsorship or interview. Money alone does not buy entry."),
    ("04", "The Calendar", "Programming", "Hire a Programming Director. Build the <span class='it'>fifty-two-week SARA Calendar.</span>", "Weekly anchors (Sunday Long Table, Wednesday Sound Bath) plus seasonal flagships (Pru Farm Festival, New Year Reset, monsoon retreat). The calendar is the membership."),
    ("05", "The Product Layer", "Extension", "Six take-home products within <span class='it'>twenty-four months.</span>", "SARA Tea · Pru Honey · SARA Balm · A signature scent (with a noted perfumer) · A sound album · The SARA Method Book. The brand must travel home with the guest."),
    ("06", "The Atmosphere", "Architecture", "Brief the architect on <span class='it'>sensory profile</span> first.", "Define the scent, light, sound, and material profile of every guest space. Commission a signature SARA scent. Build the sonic identity. Atmosphere is the product."),
]

# ─── BUILD SECTION HTML ──────────────────────────────────────────────────
def build_intro(page_num):
    thumbs = "\n".join([f'        <div class="study-thumb"><img src="images/{i:02d}.png" alt="Brand {i:02d}" loading="lazy"></div>' for i in range(1, 31)])
    legend = "\n".join([
        f'      <div class="study-legend-cell"><div class="study-legend-num">{cat["num"]}</div><div class="study-legend-name">{cat["name"]}</div></div>'
        for cat in CATEGORIES
    ])
    return f"""
<!-- ═══════════════════ 09 NEW WELLNESS BRAND · 30-BRAND STUDY · INTRODUCTION ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">Initiative · New Wellness Brand Development</div>
    <h2 class="D2">The thirty-brand <span class="gd it">identity study.</span></h2>
    <div class="rule"></div>
    <div class="body lg">A reference field of thirty world-class brands across ten categories — selected not for their size, but for the precision of their identity, the conviction of their narrative, and the defensibility of their position. The question is not who is biggest. It is who is most ownable.</div>
    <div class="study-grid">
{thumbs}
    </div>
    <div class="study-legend">
{legend}
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

def build_category(cat, page_num):
    cards_html = []
    for img, brand, loc, essence, diff, pinned in cat["brands"]:
        pin = '<div class="cat-pin">SARA benchmark</div>' if pinned else ""
        pinned_cls = " pinned" if pinned else ""
        cards_html.append(f"""    <div class="cat-card{pinned_cls}">
      {pin}
      <div class="cat-img"><img src="images/{img}.png" alt="{brand}" loading="lazy"></div>
      <div class="cat-body">
        <div class="cat-card-name">{brand}</div>
        <div class="cat-card-loc">{loc}</div>
        <div class="cat-card-essence">{essence}</div>
        <div class="cat-card-diff"><span class="cat-card-diff-label">What it does differently</span>{diff}</div>
      </div>
    </div>""")
    cards = "\n".join(cards_html)
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · CATEGORY {cat["num"]} · {cat["name"].upper()} ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study · Category {cat["num"]} of 10</div>
    <div class="cat-head">
      <div class="cat-head-left">
        <div class="cat-num">— {cat["num"]} —</div>
        <h2 class="cat-name">{cat["name"]}</h2>
      </div>
      <div class="cat-q">{cat["question"]}</div>
    </div>
    <div class="cat-three">
{cards}
    </div>
    <div class="cat-takeaway">
      <div class="cat-takeaway-label">What this teaches SARA</div>
      <div class="cat-takeaway-text">{cat["takeaway"]}</div>
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

def build_summary(page_num):
    cells = "\n".join([
        f"""    <div class="pat-cell">
      <div class="pat-num">{num}</div>
      <div class="pat-name">{name}</div>
      <div class="pat-strap">{strap}</div>
    </div>"""
        for num, name, strap in PATTERNS
    ])
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · TEN PATTERNS SUMMARY ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study · Synthesis</div>
    <h2 class="D2">Ten patterns of an <span class="gd it">inimitable brand.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Across thirty brands and ten categories, ten structural patterns recur. They are not platitudes. They are the choices that made these brands inimitable — and the patterns SARA must adopt with conviction, in its own expression.</div>
    <div class="pat-grid">
{cells}
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

def build_direction(page_num):
    cells = "\n".join([
        f"""    <div class="dir-cell">
      <div class="dir-num">— {num} —</div>
      <div class="dir-tag">{tag}</div>
      <div class="dir-name">{name}</div>
      <div class="dir-text">{text}</div>
    </div>"""
        for num, name, tag, title, text in [(d[0], d[1], d[2], d[3], d[4]) for d in DIRECTIONS]
    ])
    # actually re-do mapping
    cells_list = []
    for num, name, tag, title, text in DIRECTIONS:
        cells_list.append(f"""    <div class="dir-cell">
      <div class="dir-num">— {num} —</div>
      <div class="dir-tag">{tag}</div>
      <div class="dir-name">{title}</div>
      <div class="dir-text">{text}</div>
    </div>""")
    cells = "\n".join(cells_list)
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · SUGGESTED DIRECTION FOR SARA ═══════════════════ -->
<section class="S forest">
  <div>
    <div class="eye">30-Brand Identity Study · Direction</div>
    <h2 class="D2">Six decisions for <span class="gd it">SARA.</span></h2>
    <div class="rule"></div>
    <div class="body lg">If the brand team made only these six decisions in the next eighteen months — with the conviction the thirty brands demonstrated in theirs — SARA would be the most distinctive new wellness brand of the decade.</div>
    <div class="dir-grid">
{cells}
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

# ─── ASSEMBLE INSERT ─────────────────────────────────────────────────────
parts = [build_intro(9)]
page = 10
for cat in CATEGORIES:
    parts.append(build_category(cat, page))
    page += 1
parts.append(build_summary(page))
page += 1
parts.append(build_direction(page))
page += 1

insert_block = "\n".join(parts)

# ─── DO THE EDITS ────────────────────────────────────────────────────────
text = HTML_PATH.read_text()

# 1) Insert CSS before the closing </style>
style_end_anchor = "</style>"
if text.count(style_end_anchor) >= 1:
    # Find the FIRST occurrence (the main style block) — append additions before it
    text = text.replace(style_end_anchor, CSS_ADDITIONS + "\n" + style_end_anchor, 1)
else:
    raise RuntimeError("Could not find </style> in HTML")

# 2) Insert new sections between Platform's end (page 08) and Marketing Collateral start
splice_anchor = """  <div class="pg">08</div>
</section>

<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"""

new_splice = f"""  <div class="pg">08</div>
</section>
{insert_block}

<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"""

if splice_anchor not in text:
    raise RuntimeError("Splice anchor not found")
text = text.replace(splice_anchor, new_splice, 1)

# 3) Renumber existing pages 09-16 → 22-29
# We need to do this from the highest down to avoid double-replacement
for old, new in [(16, 29), (15, 28), (14, 27), (13, 26), (12, 25), (11, 24), (10, 23), (9, 22)]:
    old_str = f'<div class="pg">{old:02d}</div>'
    new_str = f'<div class="pg">{new:02d}</div>'
    # Only replace the LAST occurrence (the original page, since new ones are higher up)
    # But for 9 — we already inserted pages numbered 09, 10, 11, ..., so we need to replace
    # the ORIGINAL 09 which is now AFTER our new pages.
    # The simplest: split the file at the insert_block, do replacements only in the tail
    pass

# Better approach: split file at marketing collateral anchor, only renumber what's AFTER
anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"
head, _, tail = text.partition(anchor)
# In tail, renumber old 09-16 → 22-29
for old, new in [(16, 29), (15, 28), (14, 27), (13, 26), (12, 25), (11, 24), (10, 23), (9, 22)]:
    tail = tail.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')
text = head + anchor + tail

# Write back
HTML_PATH.write_text(text)
print("Wrote:", HTML_PATH)
print("Inserted: 1 intro + 10 categories + 1 summary + 1 direction = 13 new pages")
print("Renumbered subsequent pages 09-16 → 22-29")
