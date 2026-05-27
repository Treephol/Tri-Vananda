"""
Fix: Replace the (wrongly built) SARA direction content on pages 20-22
with the actual 30-Brand Study synthesis — the 10 strategic patterns
that emerged from studying the thirty brands.

Pages 20-22 become:
  20 — Overview: 10 patterns at a glance
  21 — Patterns 1-5 (with image placeholders)
  22 — Patterns 6-10 (with image placeholders)
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── NEW CSS for pattern cards (reusing dim-* and adding pattern-specific bits) ──
NEW_CSS = """
/* ───── 30-BRAND STUDY · SYNTHESIS · 10 PATTERNS ───── */
.pat-overview{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:42px}
.pat-overview-cell{background:var(--ink);padding:22px 18px;display:flex;flex-direction:column;gap:6px;min-height:140px}
.pat-overview-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.4rem;color:var(--gold-lt);line-height:1}
.pat-overview-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.02rem;color:var(--white);line-height:1.2;margin-top:4px}
.pat-overview-strap{font-family:'Jost',sans-serif;font-weight:300;font-size:.66rem;line-height:1.55;color:rgba(255,255,255,.6);margin-top:auto}
/* dim-card / dim-img are already defined; we add evidence styling */
.dim-evidence{font-family:'Jost',sans-serif;font-weight:300;font-size:.68rem;line-height:1.65;color:rgba(184,148,88,.85);margin-top:8px;letter-spacing:.02em}
.dim-evidence-label{display:inline-block;font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin-right:8px;vertical-align:baseline}
"""

text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── PATTERNS DATA ───────────────────────────────────────────────────────
PATTERNS = [
    ("01", "Name the Method", "Turn an experience into intellectual property.",
     "The most defensible wellness brands don&rsquo;t sell treatments &mdash; they sell named, proprietary methodologies. A method is trademarkable, teachable, transferable.",
     "Tracy Anderson Method &middot; SHA Method&reg; &middot; Lanserhof Concept &middot; 8-Day Hoffman Process &middot; Buchinger Fast"),
    ("02", "Own the Terroir", "Claim a specific place, never a vague region.",
     "The strongest wellness brands stake a claim on one piece of earth and refuse to abstract it. Place becomes the position; the position becomes the moat.",
     "Noma (Nordic) &middot; Reschio (Umbria) &middot; Babylonstoren (Cape) &middot; The Newt (Somerset) &middot; Flamingo Estate (Eagle Rock)"),
    ("03", "Make the Founder Visible", "One obsessive voice. Never a committee.",
     "Every Tier-S brand has a visible single visionary whose taste is unmistakable. Multi-author brands feel hotel-managed; single-author brands feel curated.",
     "Karen Roos &middot; Count Bolza &middot; Professor Bader &middot; Ren&eacute; Redzepi &middot; Alain de Botton &middot; Tracy Anderson"),
    ("04", "Curate the Room", "Membership is the brand. Members are the product.",
     "The members make the experience, not the building. Curation creates the room; the room creates the value. Wrong members destroy the brand.",
     "Soho House &middot; Annabel&rsquo;s &middot; The Battery &middot; Heimat &middot; Remedy Place &middot; Hoffman alumni"),
    ("05", "Programme the Calendar", "Members pay for what happens, not what is.",
     "A members&rsquo; club without programming is a hotel that doesn&rsquo;t take walk-ins. The calendar IS the membership. The membership fee is a subscription to the calendar.",
     "The Battery (200+ events/year) &middot; Soho House weekly calendars &middot; Hoffman cohorts &middot; School of Life curriculum"),
    ("06", "Demand the Commitment", "Length signals seriousness.",
     "Tier-S wellness brands refuse to shorten their flagship experience. Length is a filter &mdash; it filters out wellness tourists and filters in transformation seekers.",
     "Hoffman 8 days &middot; Buchinger 7&ndash;21 days &middot; Lanserhof 14&ndash;21 days &middot; SHA multi-week &middot; Ranch Malibu 4&ndash;7 days"),
    ("07", "Extend Beyond the Stay", "The brand must travel home with the guest.",
     "The most valuable wellness brands generate revenue and brand awareness when guests are not there. They sell products, books, content, scent &mdash; the brand lives on the kitchen counter, the bookshelf, the bathroom.",
     "Aesop &middot; Augustinus Bader &middot; Reschio (wine, oil, furniture, perfume) &middot; Flamingo Estate &middot; Le Labo &middot; School of Life books"),
    ("08", "Atmosphere Beats Programming", "Sensory immersion is more memorable than feature lists.",
     "People don&rsquo;t remember which treatment they had &mdash; they remember the candlelight, the silence, the scent, the materials. Atmosphere is the product. Programming is the proof.",
     "AIRE Ancient Baths &middot; Bathhouse Brooklyn &middot; Lanserhof &middot; Annabel&rsquo;s &middot; Aesop stores &middot; Soneva"),
    ("09", "Reframe the Category", "Invent the space, don&rsquo;t compete in it.",
     "Tier-S brands win by reframing the category, not by being best inside an existing one. They name the category; the category becomes a brand-defined market.",
     "Remedy Place (social wellness) &middot; Soho House (creative club) &middot; Paws Up (glamping) &middot; Noma (New Nordic) &middot; Equinox (performance fashion)"),
    ("10", "One Method, Many Doors", "A platform brand scales across owned places.",
     "The most valuable wellness brands develop one proprietary method and deploy it across multiple owned properties. One property is boutique. Three is a brand. Five is a platform.",
     "Lanserhof (5 cities) &middot; Vivamayr (5 properties) &middot; SHA (Spain + Mexico) &middot; Soneva (Maldives + Thailand) &middot; Soho House (40+)"),
]

# ─── PAGE 20: OVERVIEW ───────────────────────────────────────────────────
overview_cells = "\n".join([
    f"""      <div class="pat-overview-cell">
        <div class="pat-overview-num">{num}</div>
        <div class="pat-overview-name">{name}</div>
        <div class="pat-overview-strap">{strap}</div>
      </div>"""
    for num, name, strap, _, _ in PATTERNS
])

PAGE_20 = f"""
<!-- ═══════════════════ 30-BRAND IDENTITY STUDY · SYNTHESIS · OVERVIEW ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study &middot; Synthesis &middot; 1 of 3</div>
    <h2 class="D2">Ten patterns of an <span class="gd it">inimitable brand.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Across thirty world-class brands in ten categories, ten structural patterns repeatedly produced an ownable identity. They are not platitudes. They are the choices that made these brands inimitable &mdash; the patterns SARA must adopt with conviction, in its own expression.</div>
    <div class="pat-overview">
{overview_cells}
    </div>
  </div>
  <div class="pg">20</div>
</section>"""

# ─── PAGES 21 & 22: PATTERNS 1-5 & 6-10 ──────────────────────────────────
def build_pattern_page(page_num, eye_part, title_main, title_it, intro, patterns):
    cards = []
    for num, name, strap, body, evidence in patterns:
        cards.append(f"""      <div class="dim-card">
        <div class="dim-img"><span class="dim-img-await">Image<br>placeholder</span></div>
        <div class="dim-text-wrap">
          <div class="dim-num">{num}</div>
          <div class="dim-body">
            <h4 class="dim-name">{name}</h4>
            <div class="dim-strap">{strap}</div>
            <div class="dim-desc">{body}</div>
            <div class="dim-evidence"><span class="dim-evidence-label">Evidence</span>{evidence}</div>
          </div>
        </div>
      </div>""")
    cards_html = "\n".join(cards)
    return f"""
<!-- ═══════════════════ 30-BRAND IDENTITY STUDY · SYNTHESIS · {eye_part.upper()} ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study &middot; Synthesis &middot; {page_num - 19} of 3</div>
    <h2 class="D2">{title_main} <span class="gd it">{title_it}</span></h2>
    <div class="rule"></div>
    <div class="body lg">{intro}</div>
    <div class="dim-list">
{cards_html}
    </div>
  </div>
  <div class="pg">{page_num}</div>
</section>"""

PAGE_21 = build_pattern_page(
    21,
    "Patterns 1 to 5",
    "Patterns one to five &mdash;",
    "the IP, the place, the voice, the room, the calendar.",
    "The first five patterns concern what makes a brand structurally defensible: how it makes its method into property, claims its terroir, surfaces its founder, curates its membership, and programmes its calendar.",
    PATTERNS[:5],
)

PAGE_22 = build_pattern_page(
    22,
    "Patterns 6 to 10",
    "Patterns six to ten &mdash;",
    "the commitment, the product, the atmosphere, the category, the platform.",
    "The next five patterns concern how a brand sustains and scales: how it filters for serious guests, extends beyond the stay, designs for atmosphere, reframes its category, and grows into a multi-property platform.",
    PATTERNS[5:],
)

new_block = PAGE_20 + "\n" + PAGE_21 + "\n" + PAGE_22

# ─── REPLACE PAGES 20-22 ─────────────────────────────────────────────────
# Boundary 1: the start of (old) page 20
old_start = "<!-- ═══════════════════ NEW WELLNESS BRAND · BRAND IDENTITY DEVELOPMENT SUMMARY ═══════════════════ -->"
# Boundary 2: start of Marketing Collateral (page 23)
old_end_anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"

if old_start not in text:
    raise RuntimeError("Could not find old Synthesis start anchor")
if old_end_anchor not in text:
    raise RuntimeError("Could not find Marketing Collateral anchor")

start_idx = text.index(old_start)
end_idx = text.index(old_end_anchor)
text = text[:start_idx] + new_block.lstrip() + "\n\n" + text[end_idx:]

HTML_PATH.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
