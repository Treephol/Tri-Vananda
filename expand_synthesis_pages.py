"""
Replace pages 20-22 with a 3-page expanded Synthesis:
  20 — Overview + Logo sample (incorporates the brand-identity sample from old Direction page)
  21 — Visual Identity summary (5 dimensions with image placeholders)
  22 — Verbal Identity summary (5 dimensions with text examples)

Page count unchanged (3 pages out, 3 pages in).
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── NEW CSS ─────────────────────────────────────────────────────────────
NEW_CSS = """
/* ───── BRAND IDENTITY SUMMARY · Multi-page (Synthesis) ───── */
.bsum-frame{display:flex;flex-direction:column;align-items:center;margin-top:42px;padding:56px 60px;background:linear-gradient(180deg,rgba(184,148,88,.05) 0%,rgba(184,148,88,.02) 100%);border:1px solid rgba(184,148,88,.28);max-width:820px;margin-left:auto;margin-right:auto;gap:0}
.bsum-frame-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);line-height:1.5;margin-bottom:24px}
.bsum-frame-mark{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(4rem,8vw,6.5rem);color:var(--gold-lt);line-height:1;letter-spacing:.02em}
.bsum-frame-rule{width:60px;height:1px;background:var(--gold);margin:22px 0 20px}
.bsum-frame-tagline{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(1.15rem,1.8vw,1.5rem);color:rgba(255,255,255,.85);line-height:1.4;letter-spacing:.01em;text-align:center}
.bsum-frame-sub{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:clamp(.88rem,1.15vw,1.05rem);color:rgba(255,255,255,.55);line-height:1.5;margin-top:14px;letter-spacing:.01em;text-align:center;max-width:540px}

.bsum-roadmap{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:48px;max-width:820px;margin-left:auto;margin-right:auto}
.bsum-roadmap-cell{background:var(--ink);padding:28px 30px;display:flex;flex-direction:column;gap:10px}
.bsum-roadmap-tag{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.36em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.bsum-roadmap-title{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.5rem;color:var(--white);line-height:1.2}
.bsum-roadmap-title .it{font-style:italic;color:var(--gold-lt)}
.bsum-roadmap-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;color:rgba(255,255,255,.66);line-height:1.65;margin-top:4px}

/* Dimension card (horizontal: image left, text right) */
.dim-list{display:flex;flex-direction:column;background:rgba(184,148,88,.06);border:1px solid rgba(184,148,88,.18);margin-top:32px}
.dim-card{display:grid;grid-template-columns:160px 1fr;gap:32px;padding:22px 26px;border-bottom:1px solid rgba(184,148,88,.14);align-items:center;background:var(--ink)}
.dim-card:last-child{border-bottom:0}
.dim-img{width:160px;height:120px;background:radial-gradient(ellipse at 50% 30%,rgba(110,130,100,.18),transparent 65%),radial-gradient(ellipse at 60% 80%,rgba(184,148,88,.15),transparent 60%),linear-gradient(135deg,#1e2820 0%,#0b0f13 50%,#141c22 100%);border:1px solid rgba(184,148,88,.18);position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.dim-img-await{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.7rem;color:rgba(244,239,229,.35);line-height:1.4;text-align:center;padding:0 14px}
.dim-text-wrap{display:grid;grid-template-columns:48px 1fr;gap:14px;align-items:baseline}
.dim-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.6rem;color:var(--gold-lt);line-height:1}
.dim-body{display:flex;flex-direction:column;gap:6px}
.dim-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.35rem;color:var(--white);line-height:1.2}
.dim-strap{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.98rem;color:var(--gold-lt);line-height:1.35;margin-top:2px}
.dim-desc{font-family:'Jost',sans-serif;font-weight:300;font-size:.76rem;color:rgba(255,255,255,.7);line-height:1.65;margin-top:6px;max-width:620px}
"""

text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── NEW PAGES HTML ──────────────────────────────────────────────────────
PAGE_20 = """
<!-- ═══════════════════ NEW WELLNESS BRAND · BRAND IDENTITY DEVELOPMENT SUMMARY ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study · Synthesis · 1 of 3</div>
    <h2 class="D2">Brand identity for SARA &mdash; <span class="gd it">in summary.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Brand identity is the visible part of strategy. From the thirty-brand study, two sets of decisions emerged &mdash; five visual, five verbal &mdash; that together make a brand inimitable. The next pages summarise both. This is the brand identity, in one breath.</div>
    <div class="bsum-frame">
      <div class="bsum-frame-label">The brand identity, in one breath</div>
      <div class="bsum-frame-mark">SARA</div>
      <div class="bsum-frame-rule"></div>
      <div class="bsum-frame-tagline">Building the Culture of Living Well</div>
      <div class="bsum-frame-sub">A meaningful wellness way of life for the multigenerational family.</div>
    </div>
    <div class="bsum-roadmap">
      <div class="bsum-roadmap-cell">
        <div class="bsum-roadmap-tag">Next &middot; Page 21</div>
        <h3 class="bsum-roadmap-title">Visual <span class="it">identity.</span></h3>
        <div class="bsum-roadmap-text">Typography &middot; palette &middot; photography &middot; materials &middot; iconography &mdash; the five decisions that make SARA visually unmistakable.</div>
      </div>
      <div class="bsum-roadmap-cell">
        <div class="bsum-roadmap-tag">Next &middot; Page 22</div>
        <h3 class="bsum-roadmap-title">Verbal <span class="it">identity.</span></h3>
        <div class="bsum-roadmap-text">Tone &middot; vocabulary &middot; signature phrases &middot; narrative &middot; naming &mdash; the five decisions that make SARA verbally unmistakable.</div>
      </div>
    </div>
  </div>
  <div class="pg">20</div>
</section>"""

VISUAL_DIMS = [
    ("01", "Typography", "Cormorant + Jost.",
     "Cormorant Garamond display serif paired with Jost functional sans. Italic for emotion, letter-spaced uppercase for tags. The pairing carries the brand&rsquo;s voice on the page."),
    ("02", "Palette", "Forest. Gold. Cream.",
     "Forest green for depth, gold for warmth and authority, cream for calm. Sage and stone as quiet neutrals. Two or three colours that never widen &mdash; restraint signals authority."),
    ("03", "Photography", "Three layers, never four.",
     "Ritual &mdash; hands, breath, eyes closed. Landscape &mdash; Andaman, Phuket forest, Pru farm. Material &mdash; botanicals, food, ceramics, linen. Never lifestyle stock, never drone-glamour."),
    ("04", "Materials", "Linen, wood, stone, ceramic, brass.",
     "Brand-coded materials in every guest space. Teak and jackwood. Hand-thrown ceramic. Brushed brass. Refused: chrome, glossy plastic, mass-produced finishes."),
    ("05", "Iconography", "One signature object.",
     "A signature object the brand owns &mdash; a brass measuring cup, a hand-thrown bowl, a perfume stopper. The thing guests photograph and remember."),
]

VERBAL_DIMS = [
    ("01", "Tone", "Restrained but warm.",
     "Scientific but sensual. The CLP-meets-Soneva voice &mdash; clinical credibility wearing barefoot informality. Decided, not discovered. Never neutral."),
    ("02", "Vocabulary", "Method, Culture, Family.",
     "Brand-owned words: Method, Culture, Living well, Practice, Family, Pru, Andaman, Phuket. Refused: Detox, Self-care, Wellness journey, Treatment, Reset."),
    ("03", "Signature phrases", "Five lines that travel.",
     "Develop a repertoire of five-to-seven recurring brand lines. &lsquo;Building the Culture of Living Well.&rsquo; &lsquo;The SARA Method.&rsquo; &lsquo;From the Pru.&rsquo; Lines that recur in every channel."),
    ("04", "Narrative", "One paragraph origin.",
     "Compress SARA&rsquo;s story to a single paragraph &mdash; Montara family lineage, Phuket terroir, CLP partnership, multi-generational philosophy. Repeat the same paragraph across every touchpoint."),
    ("05", "Naming", "The SARA [Noun].",
     "All programmes, products, places follow one naming logic: The SARA Method, The SARA Reset, The SARA Calendar, The SARA Cabin, The SARA Honey. Products carry the family name forward."),
]

def build_dim_page(page_num, eye_label, title_main, title_it, intro, dims):
    cards = []
    for num, name, strap, desc in dims:
        cards.append(f"""      <div class="dim-card">
        <div class="dim-img"><span class="dim-img-await">Image<br>placeholder</span></div>
        <div class="dim-text-wrap">
          <div class="dim-num">{num}</div>
          <div class="dim-body">
            <h4 class="dim-name">{name}</h4>
            <div class="dim-strap">{strap}</div>
            <div class="dim-desc">{desc}</div>
          </div>
        </div>
      </div>""")
    cards_html = "\n".join(cards)
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · {eye_label.upper()} ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study &middot; Synthesis &middot; {page_num - 19} of 3</div>
    <h2 class="D2">{title_main} &mdash; <span class="gd it">{title_it}</span></h2>
    <div class="rule"></div>
    <div class="body lg">{intro}</div>
    <div class="dim-list">
{cards_html}
    </div>
  </div>
  <div class="pg">{page_num}</div>
</section>"""

PAGE_21 = build_dim_page(
    21,
    "Visual Identity Summary",
    "Visual identity",
    "what we&rsquo;ll build.",
    "Five visual decisions. Typography, palette, photography, materials, and iconography &mdash; each chosen with conviction, each refusing alternatives. These make SARA visually unmistakable across every touchpoint.",
    VISUAL_DIMS,
)

PAGE_22 = build_dim_page(
    22,
    "Verbal Identity Summary",
    "Verbal identity",
    "how we&rsquo;ll speak.",
    "Five verbal decisions. Tone, vocabulary, signature phrases, narrative, and naming &mdash; the brand&rsquo;s voice on every page, in every conversation. These make SARA verbally unmistakable.",
    VERBAL_DIMS,
)

new_block = PAGE_20 + "\n" + PAGE_21 + "\n" + PAGE_22

# ─── REPLACE PAGES 20-22 ─────────────────────────────────────────────────
# Boundary 1: start of old page 20 (Brand Identity Development Summary)
old_start = "<!-- ═══════════════════ NEW WELLNESS BRAND · BRAND IDENTITY DEVELOPMENT SUMMARY ═══════════════════ -->"
# Boundary 2: end of old page 22 (Digital Campaign Sample · Introduction)
# That section's closing </section> is right before the next initiative section (Marketing Collateral Preparation, which is page 23+)
old_end_anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"

if old_start not in text:
    raise RuntimeError("Could not find old Synthesis start anchor")
if old_end_anchor not in text:
    raise RuntimeError("Could not find Marketing Collateral anchor")

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
