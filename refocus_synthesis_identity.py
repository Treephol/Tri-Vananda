"""
Refocus pages 20-22 (Synthesis) on BRAND IDENTITY observations from the 30 brands.
- 5 visual dimensions (Typography, Palette, Photography, Materials, Iconography)
- 5 verbal dimensions (Tone, Vocabulary, Signature Phrases, Narrative, Naming)

Each dimension presents OBSERVATIONS, not SARA-direction prescriptions.
This becomes the foundation for the SARA Identity work that follows.
"""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# ─── DATA — VISUAL DIMENSIONS ────────────────────────────────────────────
VISUAL_DIMS = [
    ("01", "Typography", "Display serif + functional sans, italic for emotion.",
     "Every Tier-S brand pairs a display serif with a functional sans-serif. Italic serif weights carry the emotional register; letter-spaced uppercase sans handles tags and categories. Bolded serifs are systematically avoided.",
     "Aesop (Optima-derivative cream serif) &middot; Castello di Reschio &middot; The Newt &middot; School of Life (Caslon-feel) &middot; Hoffman &middot; CLP (Helvetica-clean clinical)"),
    ("02", "Palette", "Two or three colours, never widening.",
     "Restraint signals authority. Palettes lean earth-coded over chromatic &mdash; forest, ochre, terracotta, cream &mdash; with one signature accent. Brands that widened their palette diluted their identity; brands that held the line compounded recognition.",
     "Aesop (amber + cream + grey) &middot; Equinox (black + white + blood red) &middot; Le Labo (mustard + black + kraft) &middot; Soneva (driftwood + sea-salt + indigo) &middot; Reschio (ochre + olive + linen)"),
    ("03", "Photography", "Three layers &mdash; ritual, landscape, material.",
     "Photography organises into three subject layers: ritual (hands at practice, eyes closed), landscape (the place), material (objects, food, plants). Hands frequently substitute for full-face portraiture. Lifestyle stock is refused. Architecture is often photographed as portrait.",
     "AIRE &middot; Single Thread (hands at the table) &middot; Lanserhof (architecture as portrait) &middot; Aesop (products only, no people) &middot; Soneva &middot; Reschio &middot; Flamingo Estate"),
    ("04", "Materials &amp; Surfaces", "Brand-coded materials in every guest space.",
     "Materials extend the identity into physical space. Wood, linen, stone, ceramic, brass dominate the Tier-S vocabulary. Chrome, plastic, glossy finishes are refused systematically. The material register is more identifiable than the logo.",
     "Soneva (driftwood, sand, linen) &middot; Reschio (teak, hand-thrown ceramic, brushed brass) &middot; Aesop (architect-driven, store-by-store) &middot; Bathhouse (raw concrete + warm wood) &middot; Lanserhof (wood + glass + green roofs)"),
    ("05", "Iconography &amp; Mark", "A signature object owns the brand.",
     "Beyond the wordmark, Tier-S brands often own a single object more recognisable than their logo. The object appears across packaging, photography, signage, even tone of voice. The object becomes the brand&rsquo;s visual hero.",
     "Aesop (the amber bottle) &middot; Vivamayr (the chewing spoon) &middot; The Newt (hand-painted apple) &middot; AIRE (the candle in stone) &middot; Le Labo (typewriter-typed label) &middot; Reschio (vintage Fiat 500)"),
]

# ─── DATA — VERBAL DIMENSIONS ────────────────────────────────────────────
VERBAL_DIMS = [
    ("01", "Tone of Voice", "Decided, never neutral.",
     "Each brand chose a distinctive tonal register and held it. Scientific (CLP, Augustinus Bader). Confrontational (Equinox). Sensual (Flamingo Estate). Philosophical (School of Life). Restrained (Lanserhof, Aesop). Maximalist (Annabel&rsquo;s). Neutral wellness-conference voice was avoided uniformly.",
     "CLP (institutional medical) &middot; Augustinus Bader (peer-reviewed scientific) &middot; Equinox (imperative-provocative) &middot; Flamingo Estate (flirtatious) &middot; School of Life (conversational philosophy) &middot; Annabel&rsquo;s (theatrical heritage)"),
    ("02", "Vocabulary", "Owned words. Refused words.",
     "Each brand has five to fifteen words it owns &mdash; uses repeatedly &mdash; and an equal list of words it refuses. The refused list often defines the brand more sharply than the adopted list. The vocabulary becomes a litmus test for off-brand copy.",
     "Buchinger (&ldquo;the Fast,&rdquo; not &ldquo;detox&rdquo;) &middot; Hoffman (&ldquo;the Process,&rdquo; not &ldquo;retreat&rdquo;) &middot; Lanserhof (&ldquo;cure,&rdquo; not &ldquo;spa&rdquo;) &middot; SHA (&ldquo;Method,&rdquo; not &ldquo;programme&rdquo;) &middot; AIRE (&ldquo;Thermal circuit,&rdquo; refuses wellness vocabulary entirely)"),
    ("03", "Signature Phrases", "Five to seven lines that travel.",
     "Brands develop a small repertoire of recurring lines &mdash; five to seven phrases that surface across film, social, packaging, and stationery. These phrases become catchphrases for the audience to internalise and repeat.",
     "Soneva (&lsquo;No News, No Shoes&rsquo; + &lsquo;Slow Life&rsquo;) &middot; Equinox (&lsquo;It&rsquo;s Not Fitness. It&rsquo;s Life.&rsquo;) &middot; Aman (&lsquo;A way home&rsquo;) &middot; CLP (&lsquo;Live longer. Live better.&rsquo;) &middot; Le Labo (&lsquo;City Exclusive&rsquo;) &middot; Noma (&lsquo;Right here, right now&rsquo;)"),
    ("04", "Narrative Style", "Origin compressed to one paragraph.",
     "The origin story is told the same way every time, across every channel &mdash; book, website, brochure, magazine spread. Most Tier-S brands lean on three anchors: founder + place + year. The compression is the discipline.",
     "Buchinger (Dr Otto Buchinger &middot; Lake Constance &middot; 1920) &middot; CLP (Dr Paul Niehans &middot; Montreux &middot; 1931) &middot; Reschio (Count Bolza &middot; Umbria &middot; 1994) &middot; Babylonstoren (Karen Roos &middot; Franschhoek &middot; 2007) &middot; Noma (Redzepi &middot; Copenhagen &middot; 2003)"),
    ("05", "Naming System", "One logic across programmes, products, places.",
     "Naming follows a single consistent logic. Once chosen, the logic is applied to every new property, programme, product. This is what makes the brand portable across geographies and categories without losing coherence.",
     "SHA (The SHA Method&reg;, trademarked) &middot; Hoffman (The Hoffman Process &middot; 8 days) &middot; Buchinger (The Buchinger Fast) &middot; Aman (Amanwana &middot; Amanjiwo &middot; Amankora) &middot; Lanserhof (Lanserhof Tegernsee, Sylt, Lans) &middot; Reschio (Reschio Estate Wine, Olive Oil)"),
]

# ─── HTML BUILDERS ───────────────────────────────────────────────────────
def build_overview_page():
    visual_cells = "\n".join([
        f"""      <div class="pat-overview-cell">
        <div class="pat-overview-num">V&middot;{num}</div>
        <div class="pat-overview-name">{name}</div>
        <div class="pat-overview-strap">{strap}</div>
      </div>"""
        for num, name, strap, _, _ in VISUAL_DIMS
    ])
    verbal_cells = "\n".join([
        f"""      <div class="pat-overview-cell">
        <div class="pat-overview-num">W&middot;{num}</div>
        <div class="pat-overview-name">{name}</div>
        <div class="pat-overview-strap">{strap}</div>
      </div>"""
        for num, name, strap, _, _ in VERBAL_DIMS
    ])
    return f"""
<!-- ═══════════════════ 30-BRAND IDENTITY STUDY · SYNTHESIS · OVERVIEW ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study &middot; Synthesis &middot; 1 of 3</div>
    <h2 class="D2">What we learned about <span class="gd it">brand identity.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Across thirty brands and ten categories, the same identity decisions recurred &mdash; on the visual side, on the verbal side. These are the dimensions that made the brands inimitable. They are the dimensions SARA will use to build its own identity.</div>
    <div class="pat-overview" style="grid-template-columns:repeat(5,1fr)">
{visual_cells}
    </div>
    <div class="pat-overview" style="grid-template-columns:repeat(5,1fr);margin-top:1px">
{verbal_cells}
    </div>
  </div>
  <div class="pg">20</div>
</section>"""

def build_dim_page(page_num, eye_part, title_main, title_it, intro, dims):
    cards = []
    for num, name, strap, body, evidence in dims:
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

PAGE_20 = build_overview_page()

PAGE_21 = build_dim_page(
    21,
    "Visual Identity",
    "Visual identity &mdash;",
    "five dimensions across thirty brands.",
    "Five visual decisions recurred across the brands we studied: typography, palette, photography, materials, and iconography. Each card describes what was observed, with examples to anchor the pattern.",
    VISUAL_DIMS,
)

PAGE_22 = build_dim_page(
    22,
    "Verbal Identity",
    "Verbal identity &mdash;",
    "five dimensions across thirty brands.",
    "Five verbal decisions recurred across the brands we studied: tone, vocabulary, signature phrases, narrative, and naming. Each card describes what was observed, with examples to anchor the pattern.",
    VERBAL_DIMS,
)

new_block = PAGE_20 + "\n" + PAGE_21 + "\n" + PAGE_22

# ─── REPLACE PAGES 20-22 ─────────────────────────────────────────────────
old_start = "<!-- ═══════════════════ 30-BRAND IDENTITY STUDY · SYNTHESIS · OVERVIEW ═══════════════════ -->"
old_end_anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"

if old_start not in text:
    raise RuntimeError("Could not find old Synthesis Overview anchor")
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
