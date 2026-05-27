"""
Refocus the 30-brand study pages around BRAND IDENTITY (visual + verbal/copy).
- Page 09 (intro): remove thumbnail grid; intro on what brand identity is
- Pages 10-19 (categories): each brand card now shows Visual identity + Copy
- Page 20 (summary): Brand Identity Development for SARA (5 visual + 5 verbal dimensions)
- Page 21 (direction): SARA's Brand Identity Direction (5 visual + 5 verbal cards)
"""

from pathlib import Path
import re

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")

# ─── CSS REPLACEMENT BLOCK ──────────────────────────────────────────────
# We replace the old "30-BRAND STUDY" CSS block with this new one
NEW_CSS = """
/* ───── 30-BRAND STUDY · INTRO (no thumbnails) ───── */
.bi-frame{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:48px}
.bi-frame-cell{background:var(--ink);padding:42px 44px;display:flex;flex-direction:column;gap:18px;min-height:340px}
.bi-frame-h{font-family:'Jost',sans-serif;font-weight:200;font-size:.65rem;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.bi-frame-title{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:2.2rem;color:var(--white);line-height:1.1;margin-bottom:6px}
.bi-frame-title .it{font-style:italic;color:var(--gold-lt)}
.bi-dims{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.bi-dim{display:grid;grid-template-columns:170px 1fr;gap:24px;align-items:baseline;padding:14px 0;border-top:1px solid rgba(184,148,88,.14)}
.bi-dim:first-child{border-top:0;padding-top:6px}
.bi-dim-name{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold-lt);line-height:1.6}
.bi-dim-text{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.02rem;color:rgba(255,255,255,.68);line-height:1.45}
.bi-legend{display:grid;grid-template-columns:repeat(5,1fr);gap:36px;margin-top:48px;padding-top:36px;border-top:1px solid rgba(184,148,88,.15)}
.bi-legend-cell{}
.bi-legend-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.3rem;color:var(--gold-lt);line-height:1;margin-bottom:8px}
.bi-legend-name{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.7);line-height:1.6}

/* ───── 30-BRAND STUDY · CATEGORY PAGE (visual + copy per brand) ───── */
.cat-head{display:flex;justify-content:space-between;align-items:flex-end;gap:48px;margin-bottom:42px;padding-bottom:24px;border-bottom:1px solid rgba(184,148,88,.18)}
.cat-head-left{}
.cat-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.05rem;color:var(--gold-lt);line-height:1;letter-spacing:.04em}
.cat-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:clamp(2rem,3.6vw,3rem);line-height:1.05;color:var(--white);margin-top:12px}
.cat-q{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.1rem;color:rgba(255,255,255,.6);line-height:1.4;max-width:480px;text-align:right;padding-bottom:8px}
.cat-three{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18)}
.cat-card{background:var(--ink);display:flex;flex-direction:column;position:relative;min-height:680px}
.cat-card.pinned{background:linear-gradient(180deg,var(--ink) 0%,rgba(184,148,88,.04) 100%)}
.cat-pin{position:absolute;top:14px;right:14px;font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--ink);background:var(--gold);padding:5px 10px;border-radius:2px;z-index:3;line-height:1}
.cat-img{aspect-ratio:1/1;position:relative;overflow:hidden;background:#000}
.cat-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.cat-img::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,15,19,0) 0%,rgba(11,15,19,.55) 100%);z-index:1;pointer-events:none}
.cat-body{padding:22px 24px 26px;display:flex;flex-direction:column;gap:10px;flex:1}
.cat-card-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.45rem;color:var(--white);line-height:1.1}
.cat-card.pinned .cat-card-name{color:var(--gold-lt)}
.cat-card-loc{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.26em;text-transform:uppercase;color:rgba(184,148,88,.75);line-height:1.5}
.cat-card-essence{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:rgba(255,255,255,.6);line-height:1.4;padding:8px 0 4px;border-bottom:1px solid rgba(184,148,88,.12)}
.cat-block{display:flex;flex-direction:column;gap:5px;padding-top:6px}
.cat-block-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);line-height:1.5}
.cat-block-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.74rem;line-height:1.65;color:rgba(255,255,255,.74)}
.cat-takeaway{margin-top:32px;padding:22px 30px;border-left:2px solid var(--gold);background:rgba(184,148,88,.04);display:flex;align-items:baseline;gap:32px}
.cat-takeaway-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.56rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);flex-shrink:0;white-space:nowrap;line-height:1.6}
.cat-takeaway-text{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.2rem;color:var(--white);line-height:1.4}
.cat-takeaway-text .it{font-style:italic;color:var(--gold-lt)}

/* ───── 30-BRAND STUDY · SUMMARY (Brand identity development for SARA) ───── */
.bid-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:42px}
.bid-col{background:var(--ink);padding:36px 38px;display:flex;flex-direction:column}
.bid-col-h{font-family:'Jost',sans-serif;font-weight:200;font-size:.65rem;letter-spacing:.38em;text-transform:uppercase;color:var(--gold);line-height:1.5;margin-bottom:10px}
.bid-col-title{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.8rem;color:var(--white);line-height:1.15;margin-bottom:28px;padding-bottom:14px;border-bottom:1px solid rgba(184,148,88,.18)}
.bid-col-title .it{font-style:italic;color:var(--gold-lt)}
.bid-row{display:grid;grid-template-columns:30px 130px 1fr;gap:14px;padding:16px 0;border-top:1px solid rgba(184,148,88,.1);align-items:baseline}
.bid-row:first-of-type{border-top:0;padding-top:6px}
.bid-row-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.1rem;color:var(--gold-lt);line-height:1}
.bid-row-name{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.3em;text-transform:uppercase;color:var(--white);line-height:1.6}
.bid-row-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.7;color:rgba(255,255,255,.7)}

/* ───── 30-BRAND STUDY · DIRECTION (SARA visual + verbal direction) ───── */
.bdir-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin-top:42px}
.bdir-col{background:var(--ink);padding:32px 34px;display:flex;flex-direction:column}
.bdir-col-h{font-family:'Jost',sans-serif;font-weight:200;font-size:.62rem;letter-spacing:.38em;text-transform:uppercase;color:var(--gold);line-height:1.5;margin-bottom:8px}
.bdir-col-title{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.7rem;color:var(--white);line-height:1.15;margin-bottom:24px;padding-bottom:14px;border-bottom:1px solid rgba(184,148,88,.18)}
.bdir-col-title .it{font-style:italic;color:var(--gold-lt)}
.bdir-card{padding:18px 0;border-top:1px solid rgba(184,148,88,.1)}
.bdir-card:first-of-type{border-top:0;padding-top:4px}
.bdir-tag{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold-lt);line-height:1.5;margin-bottom:5px}
.bdir-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.25rem;color:var(--white);line-height:1.2;margin-bottom:8px}
.bdir-name .it{font-style:italic;color:var(--gold-lt)}
.bdir-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.76rem;line-height:1.7;color:rgba(255,255,255,.72)}
.bdir-refuse{font-family:'Jost',sans-serif;font-weight:200;font-size:.68rem;line-height:1.6;color:rgba(255,255,255,.45);margin-top:6px;font-style:italic}
"""

# ─── BRAND DATA (visual + copy per brand) ────────────────────────────────
CATEGORIES = [
    {
        "num": "01",
        "name": "Vitality & Longevity",
        "question": "What identity earns medical credibility?",
        "takeaway": "Borrow the visual <span class='it'>discipline of medicine</span>, not the language of spa. CLP partnership = science-first identity.",
        "brands": [
            ("01", "Clinique La Prairie", "Montreux · 1931",
             "Swiss longevity laboratory for self-extension.",
             "Clinical white + glacial blue. Helvetica-clean type. Hexagonal cellular motif. Lake-Alps landscapes paired with microscope imagery. Marble, glass, soft Swiss lighting.",
             "Institutional. Doctor-led. &ldquo;Revitalisation, longevity, cellular renewal.&rdquo; Speaks like a Swiss bank, not a spa. No emotional adjectives. No aspirational verbs.",
             True),
            ("02", "SHA Wellness Clinic", "Alicante · 2008",
             "Macrobiotic medicine for measurable transformation.",
             "White ziggurat architecture. Sand + sage palette. Geometric sans-serif. Mediterranean light photography. Diagnostic and clinical imagery deliberately mixed.",
             "Methodical. Outcomes-led. &ldquo;The SHA Method&reg; delivers measurable transformation.&rdquo; East-West vocabulary fused with confidence.",
             False),
            ("03", "Lanserhof", "Tegernsee · 1984",
             "F.X. Mayr precision for modern bodies.",
             "Architect-led (Ingenhoven). Wood + glass + green roofs. Monochrome restraint. Photography of buildings dominates; guests rarely shown.",
             "Disciplined. Functional. &ldquo;The Cure.&rdquo; &ldquo;The Concept.&rdquo; Refuses spa or hospitality language. Reads like a medical journal.",
             False),
        ],
    },
    {
        "num": "02",
        "name": "Athletics & Practice",
        "question": "What identity makes movement an identity?",
        "takeaway": "Identity must be <span class='it'>specific enough to exclude.</span> The room is curated by the visual and verbal posture.",
        "brands": [
            ("04", "Equinox", "New York · 1991",
             "Performance fashion for the urban athlete.",
             "Black, white, blood-red. Brutalist club architecture. Steven Klein-era provocative photography. Athletic editorial typography. Tagline as visual element.",
             "Confrontational. &ldquo;It&rsquo;s Not Fitness. It&rsquo;s Life.&rdquo; &ldquo;Commit to Something.&rdquo; Imperative tense. The tagline is the brand.",
             False),
            ("05", "Heimat", "Los Angeles · 2022",
             "European bathhouse culture, Los Angeles edition.",
             "Earth-tone monochrome (cream + terracotta + sand). Mediterranean modernism. Vintage athletic photography. Custom millwork. No visible logos anywhere.",
             "Restrained. European. &ldquo;Belonging.&rdquo; &ldquo;Homeland.&rdquo; &ldquo;Bath.&rdquo; Quiet, member-coded vocabulary. Refuses fitness language.",
             True),
            ("06", "Tracy Anderson Method", "New York · 2006",
             "Cult method for the long, lean body.",
             "Cool grey + dancer pink + brushed gold. Soft-lit studio photography. Founder always on-camera. Feminine, dance-influenced rather than gym-coded.",
             "Personal. Founder-voiced. &ldquo;The Method.&rdquo; First-person testimonial layered with proprietary terminology.",
             False),
        ],
    },
    {
        "num": "03",
        "name": "Recovery & Bodywork",
        "question": "What identity makes a ritual feel sacred?",
        "takeaway": "Identity is <span class='it'>sensory and sparse</span>. The atmosphere does the work copy cannot.",
        "brands": [
            ("07", "Remedy Place", "Los Angeles · 2019",
             "Social wellness for the recovery generation.",
             "Apothecary cream + sage + brass. Apple-store minimalism applied to ice baths. Branded ritual signage. Instagram-engineered without looking it.",
             "Social. &ldquo;Social wellness.&rdquo; &ldquo;Self-care reimagined.&rdquo; Casual yet branded &mdash; speaks like a wellness DTC startup with discipline.",
             False),
            ("08", "AIRE Ancient Baths", "Multiple cities · 2008",
             "Candlelit baths in ancient architecture.",
             "Stone, candlelight, water, shadow. Almost no logo. Sensory-led photography. Low light always. Heritage building as visual identity.",
             "Sparse. Sensual. &ldquo;Thermal circuit.&rdquo; Refuses the wellness vocabulary. Reads like a museum&rsquo;s exhibition catalogue.",
             True),
            ("09", "Bathhouse", "Brooklyn · 2019",
             "Concrete cathedral for cold-warm contrast.",
             "Raw concrete. Brutalist warehouse. Soft warm lighting against hard surfaces. No-logo restraint. Helvetica discipline. Masculine without being macho.",
             "Direct. Slightly skeptical. &ldquo;Bath. Sauna. Cold plunge. Restaurant.&rdquo; Functional list-driven copy. Tone of a record label, not a wellness brand.",
             False),
        ],
    },
    {
        "num": "04",
        "name": "Mind & Cognition",
        "question": "What identity treats the inner life with care?",
        "takeaway": "Identity is <span class='it'>editorial</span>. Long-tail content carries the brand beyond the property.",
        "brands": [
            ("10", "Open", "Los Angeles · 2018",
             "Movement and breath, designed beautifully.",
             "Warm peach + cream + clay. Custom serif typography. Generous whitespace. Hand-illustrated mark. Premium app UI craft.",
             "Editorial-soft. &ldquo;Practice,&rdquo; not &ldquo;session.&rdquo; Refuses gamification language. Slow, present-tense, sensory.",
             False),
            ("11", "The School of Life", "London · 2008",
             "Emotional intelligence as cultural project.",
             "Mid-century illustration. Mustard + ink + cream. Classic serif (Caslon-feel). Bookish editorial layout. Hand-drawn whimsy.",
             "Philosophical. Conversational. &ldquo;How to&hellip;&rdquo; &ldquo;The challenge of&hellip;&rdquo; Reads like an essay, never a brochure.",
             True),
            ("12", "Hoffman Institute", "Napa · 1967",
             "Eight-day deep emotional reset.",
             "Sage green + warm cream. Photography of people-in-process (eyes closed, hands held). Serif typography. Retreat aesthetic rather than spa.",
             "Therapeutic. Restrained. &ldquo;The Process.&rdquo; Speaks like a serious psychological methodology, not a wellness offering.",
             False),
        ],
    },
    {
        "num": "05",
        "name": "Detox & Reset",
        "question": "What identity makes discipline desirable?",
        "takeaway": "Identity is <span class='it'>family.</span> Generational continuity reads as trust no chain can buy.",
        "brands": [
            ("13", "Buchinger Wilhelmi", "&Uuml;berlingen · 1920",
             "Therapeutic fasting since 1920.",
             "Clinical-warm. White + soft yellow + medical pale blue. Mediterranean (Marbella) and Bavarian (&Uuml;berlingen) architectures. Lab-coat photography.",
             "Generational. Medical. &ldquo;The Fast.&rdquo; Speaks in plural-family voice. Cites peer-reviewed research as design element.",
             True),
            ("14", "Vivamayr", "Maria W&ouml;rth · 2004",
             "Modern Mayr medicine, alpine precision.",
             "White-on-white interiors. Sage + dove grey + glacial blue. Lakefront photography. Chewing-spoon iconography. Minimal typography.",
             "Methodical. Alpine-restrained. &ldquo;Cure.&rdquo; &ldquo;Diagnostic.&rdquo; Speaks like a Swiss watch instruction manual.",
             False),
            ("15", "The Ranch Malibu", "Malibu · 2010",
             "Boot-camp wellness for high-output people.",
             "Sun-bleached California ranch. Weathered wood + cream linen + olive green. Hand-lettered signage. Golden-hour photography. Equestrian motifs.",
             "Direct. Demanding. &ldquo;The Programme.&rdquo; Speaks in command voice. &ldquo;4 AM. Lights out 9 PM.&rdquo; No negotiation.",
             False),
        ],
    },
    {
        "num": "06",
        "name": "The Table",
        "question": "What identity turns food into philosophy?",
        "takeaway": "Identity is <span class='it'>terroir.</span> The land becomes the brand becomes the product.",
        "brands": [
            ("16", "Noma", "Copenhagen · 2003",
             "Nordic terroir made into philosophy.",
             "Brutalist + organic. Raw wood, foraged greens, fermented browns. Hand-thrown ceramics. Ren&eacute; as face. No logo, no neon.",
             "Philosophical. Place-specific. &ldquo;Right here, right now.&rdquo; &ldquo;Foraged.&rdquo; Reads like a manifesto, not a menu.",
             False),
            ("17", "Flamingo Estate", "Los Angeles · 2017",
             "Garden-to-everything California sensuality.",
             "Tropical pinks, oranges, deep greens. Hand-painted botanical illustrations. Vintage botanical typography. Founder Richard Christiansen visible everywhere.",
             "Sensual. Playful. Flirtatious. &ldquo;Sex,&rdquo; &ldquo;garden,&rdquo; &ldquo;scent,&rdquo; &ldquo;harvest.&rdquo; The most daringly tonal brand in this study.",
             True),
            ("18", "Single Thread", "Healdsburg · 2016",
             "Kaiseki precision on Sonoma farmland.",
             "Pacific NW + Japanese restraint. Charcoal, clay, wood. Custom ceramics by founder. Donabe pots feature. Hand-bound menus.",
             "Quiet. Husband-wife voice. &ldquo;One thread.&rdquo; Refuses superlatives. Speaks like a kaiseki menu &mdash; sparse, deliberate.",
             False),
        ],
    },
    {
        "num": "07",
        "name": "Beauty & Aesthetics",
        "question": "What identity makes a product a belief?",
        "takeaway": "Identity is <span class='it'>voice.</span> The brand's writing is the moat. The product is honestly average.",
        "brands": [
            ("19", "Aesop", "Melbourne · 1987",
             "Apothecary intellectualism in amber glass.",
             "Amber bottle (signature). Brown cream serif (Optima derivative). Institutional grey + cream packaging. Architect-led store design. No model photography.",
             "Literary. Borges-quoting. Long-sentence, semicolon-loving. The voice IS the moat. Refuses celebrity, paid ads, and influencer copy.",
             False),
            ("20", "Augustinus Bader", "Leipzig · 2018",
             "Stem-cell science from a German laboratory.",
             "Clinical white + cool blue + minimal gold. Professor-as-spokesperson. Lab photography. Peer-reviewed citations used as design elements.",
             "Scientific. Restrained. &ldquo;TFC8&reg;.&rdquo; &ldquo;Cellular regeneration.&rdquo; Speaks like a biotech filing, not a beauty pitch.",
             False),
            ("21", "Le Labo", "New York · 2006",
             "Hand-blended perfume with your name on it.",
             "Apothecary lab-coat aesthetic. Mustard yellow + black + raw kraft paper. Hand-typed labels. Smith Corona typewriter in every store.",
             "Anti-corporate. Ritual-led. &ldquo;Hand-blended.&rdquo; &ldquo;City Exclusive.&rdquo; Reads like a 1920s chemist&rsquo;s shop. Refuses advertising entirely.",
             True),
        ],
    },
    {
        "num": "08",
        "name": "Culture & Learning",
        "question": "What identity makes a club a creative institution?",
        "takeaway": "Identity is <span class='it'>insider language.</span> The brand's vocabulary signals who belongs.",
        "brands": [
            ("22", "Soho House", "London · 1995",
             "Members' clubs for creative industries.",
             "Mid-century modern + colonial Victorian + Brooklyn loft hybrid. Deep greens + burnt orange. Liberty fabric. Gallery-wall art curation. Cookhouse menus.",
             "Insider. &ldquo;Members.&rdquo; &ldquo;Houses.&rdquo; Speaks in a club&rsquo;s voice, not a hotel&rsquo;s. Industry-coded vocabulary throughout.",
             True),
            ("23", "The Battery", "San Francisco · 2013",
             "Tech-built private club with cultural soul.",
             "Victorian-meets-tech. Brass, leather, indigo. Restored 1860s building. Hand-bound member directory. Strict no-photography rule throughout.",
             "Private. Civic. Speaks rarely &mdash; the brand&rsquo;s voice lives in the architecture and rules, not in marketing.",
             False),
            ("24", "Annabel&rsquo;s London", "Mayfair · 1963",
             "Maximalist Mayfair nightclub theatre.",
             "Maximalist florals. Jewel tones. Gold leaf. Hand-painted ceilings. Custom Martin Brudnizki wallpapers. No surface unadorned.",
             "Theatrical. Heritage-led. Speaks in club ritual: dinner, dancing, garden, discotheque &mdash; across five floors and one inheritance.",
             False),
        ],
    },
    {
        "num": "09",
        "name": "Family & Generations",
        "question": "What identity makes luxury include children?",
        "takeaway": "Identity is <span class='it'>informal at full price.</span> Barefoot luxury reframes the category.",
        "brands": [
            ("25", "Soneva", "Maldives · 1995",
             "Barefoot luxury for conscious families.",
             "Sun-bleached driftwood + sea-salt cream + Maldivian-Thai indigo. Hand-drawn maps. Child-handwriting brand mark. Sandy footprints in signage.",
             "Family-led. &ldquo;Slow life.&rdquo; &ldquo;No News, No Shoes.&rdquo; Casual, barefoot, deliberately informal at $5,000-per-night price points.",
             True),
            ("26", "Soho Farmhouse", "Oxfordshire · 2015",
             "Cotswold farm reimagined as members' club.",
             "English countryside + Hamptons hybrid. Whitewashed stone + reclaimed wood + tartan. Cabin architecture. Muddy-boots-friendly luxury.",
             "Soho House insider extension. &ldquo;Cabins, Main Barn, cinema.&rdquo; Rural-deluxe vocabulary, member-coded.",
             False),
            ("27", "Paws Up", "Montana · 2005",
             "Glamping ranch for legacy American families.",
             "Big-sky photography. Vintage Americana. Weathered leather + denim + canvas. Taxidermy + cowhide + cast iron. Log-cabin grandeur.",
             "American-West. &ldquo;Ranch. Camp. Trail.&rdquo; Masculine-coded. Speaks like a Yellowstone-era film opening.",
             False),
        ],
    },
    {
        "num": "10",
        "name": "Farm House Real Estate",
        "question": "What identity makes an estate a brand world?",
        "takeaway": "Identity is <span class='it'>one obsessive voice.</span> Editor-grade direction makes the property publishable.",
        "brands": [
            ("28", "Castello di Reschio", "Umbria · 1994",
             "Eight-century estate, family-restored.",
             "Faded ochre + olive green + terracotta + raw linen. Hand-restored architecture. Bolza-family-designed furniture. Vintage Fiat 500s. No chrome.",
             "Family-led. Italian-restrained. &ldquo;Estate.&rdquo; &ldquo;Restoration.&rdquo; Speaks like a Cabana magazine spread &mdash; archival, slow, considered.",
             True),
            ("29", "Babylonstoren", "Franschhoek · 2007",
             "Working Cape Dutch farm, fully brandified.",
             "Cape Dutch whitewashed architecture. Vegetable-garden green. Terracotta. Hand-painted typography on packaging. Botanical illustration throughout.",
             "Editor-curated. &ldquo;Garden.&rdquo; &ldquo;Farm.&rdquo; Speaks like a magazine &mdash; every detail captioned at editorial quality.",
             False),
            ("30", "The Newt", "Somerset · 2019",
             "English country estate, museum-grade.",
             "Hand-painted apple illustrations. Deep British green + cream. Georgian-house typography. Cyder bottle as design hero. Walled-garden photography.",
             "Country-estate. Numbered-edition. &ldquo;Cyder, Garden, Hotel.&rdquo; Speaks like a Georgian estate brochure &mdash; slow, archival, deeply detailed.",
             False),
        ],
    },
]

# ─── HTML BUILDERS ───────────────────────────────────────────────────────
def build_intro(page_num):
    visual_dims = [
        ("Typography", "Display serif paired with functional sans."),
        ("Palette", "Two or three colours that never widen."),
        ("Photography", "Ritual, landscape, material &mdash; never lifestyle."),
        ("Materials", "Wood, linen, stone, ceramic, brass."),
        ("Iconography", "A signature object the brand owns."),
    ]
    verbal_dims = [
        ("Tone", "Decided, not discovered. Never neutral."),
        ("Vocabulary", "Brand-owned words. Refused words."),
        ("Signature phrases", "Five to seven lines that recur."),
        ("Narrative", "Origin story compressed to one paragraph."),
        ("Naming", "One logic for programmes, products, places."),
    ]
    vis_html = "\n".join([
        f'        <div class="bi-dim"><div class="bi-dim-name">{n}</div><div class="bi-dim-text">{t}</div></div>'
        for n, t in visual_dims
    ])
    verb_html = "\n".join([
        f'        <div class="bi-dim"><div class="bi-dim-name">{n}</div><div class="bi-dim-text">{t}</div></div>'
        for n, t in verbal_dims
    ])
    legend = "\n".join([
        f'      <div class="bi-legend-cell"><div class="bi-legend-num">{cat["num"]}</div><div class="bi-legend-name">{cat["name"]}</div></div>'
        for cat in CATEGORIES
    ])
    return f"""
<!-- ═══════════════════ 09 NEW WELLNESS BRAND · 30-BRAND IDENTITY STUDY · INTRODUCTION ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">Initiative · New Wellness Brand Development</div>
    <h2 class="D2">Brand identity &mdash; <span class="gd it">visual and verbal.</span></h2>
    <div class="rule"></div>
    <div class="body lg">A brand identity is the visible part of strategy &mdash; what a brand looks like, and how it speaks. Across thirty world-class brands in ten categories, we studied both dimensions: typography, palette, photography, materials, and iconography on the visual side; tone, vocabulary, signature phrases, narrative, and naming on the verbal side. The question is not who is biggest. It is whose identity is most ownable.</div>
    <div class="bi-frame">
      <div class="bi-frame-cell">
        <div class="bi-frame-h">Dimension 1 of 2</div>
        <h3 class="bi-frame-title">Visual <span class="it">identity.</span></h3>
        <div class="bi-dims">
{vis_html}
        </div>
      </div>
      <div class="bi-frame-cell">
        <div class="bi-frame-h">Dimension 2 of 2</div>
        <h3 class="bi-frame-title">Verbal <span class="it">identity.</span></h3>
        <div class="bi-dims">
{verb_html}
        </div>
      </div>
    </div>
    <div class="bi-legend">
{legend}
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

def build_category(cat, page_num):
    cards = []
    for img, brand, loc, essence, visual, copy, pinned in cat["brands"]:
        pin = '<div class="cat-pin">SARA benchmark</div>' if pinned else ""
        pinned_cls = " pinned" if pinned else ""
        cards.append(f"""    <div class="cat-card{pinned_cls}">
      {pin}
      <div class="cat-img"><img src="images/{img}.png" alt="{brand}" loading="lazy"></div>
      <div class="cat-body">
        <div class="cat-card-name">{brand}</div>
        <div class="cat-card-loc">{loc}</div>
        <div class="cat-card-essence">{essence}</div>
        <div class="cat-block">
          <div class="cat-block-label">Visual</div>
          <div class="cat-block-text">{visual}</div>
        </div>
        <div class="cat-block">
          <div class="cat-block-label">Copy</div>
          <div class="cat-block-text">{copy}</div>
        </div>
      </div>
    </div>""")
    cards_html = "\n".join(cards)
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · CATEGORY {cat["num"]} · {cat["name"].upper()} ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study · Category {cat["num"]} of 10</div>
    <div class="cat-head">
      <div class="cat-head-left">
        <div class="cat-num">&mdash; {cat["num"]} &mdash;</div>
        <h2 class="cat-name">{cat["name"]}</h2>
      </div>
      <div class="cat-q">{cat["question"]}</div>
    </div>
    <div class="cat-three">
{cards_html}
    </div>
    <div class="cat-takeaway">
      <div class="cat-takeaway-label">Identity lesson for SARA</div>
      <div class="cat-takeaway-text">{cat["takeaway"]}</div>
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

# Summary: 5 visual + 5 verbal dimensions, what 30 brands taught us
VISUAL_SUMMARY = [
    ("01", "Typography", "A deliberate serif-sans pairing carries the brand's voice on the page. Display serif for emotion. Functional sans for clarity. The pairing IS the voice."),
    ("02", "Palette", "Two or three primary colours that never widen. Restraint signals authority. Aesop's amber. Equinox's red. Le Labo's mustard."),
    ("03", "Photography", "Three layers always: ritual (hands, faces), landscape (place), material (objects, food). Never lifestyle stock. Never drone-glamour."),
    ("04", "Materials", "Brand-coded materials carry the identity into space. Wood, linen, stone, ceramic, brass. No chrome. No plastic finishes."),
    ("05", "Iconography", "A signature object the brand owns: amber bottle, chewing spoon, apple, candle. The thing guests photograph and remember."),
]
VERBAL_SUMMARY = [
    ("01", "Tone", "Decided, not discovered. Scientific (CLP), confrontational (Equinox), sensual (Flamingo), philosophical (TSOL). Never neutral."),
    ("02", "Vocabulary", "Brand-owned words and brand-refused words. 'Method,' 'practice,' 'ritual,' 'cure.' Refused: 'wellness journey,' 'treatment,' 'self-care.'"),
    ("03", "Signature phrases", "Five to seven recurring brand lines that travel everywhere. 'It's Not Fitness. It's Life.' 'No News, No Shoes.' 'Slow Life.'"),
    ("04", "Narrative", "Origin story compressed to a single paragraph and repeated everywhere. Niehans in Montreux, 1931. Bolza in Umbria, 1994."),
    ("05", "Naming system", "Programmes, products, places all follow one naming logic. The Buchinger Fast. The Hoffman Process. The SHA Method&reg;."),
]

def build_summary(page_num):
    vis = "\n".join([
        f"""      <div class="bid-row">
        <div class="bid-row-num">{num}</div>
        <div class="bid-row-name">{name}</div>
        <div class="bid-row-text">{text}</div>
      </div>"""
        for num, name, text in VISUAL_SUMMARY
    ])
    verb = "\n".join([
        f"""      <div class="bid-row">
        <div class="bid-row-num">{num}</div>
        <div class="bid-row-name">{name}</div>
        <div class="bid-row-text">{text}</div>
      </div>"""
        for num, name, text in VERBAL_SUMMARY
    ])
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · BRAND IDENTITY DEVELOPMENT SUMMARY ═══════════════════ -->
<section class="S deep">
  <div>
    <div class="eye">30-Brand Identity Study · Synthesis</div>
    <h2 class="D2">Brand identity development &mdash; <span class="gd it">what we learned.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Across thirty brands, two sets of decisions repeatedly produced ownable identity: five on the visual side, five on the verbal side. The brands that made these decisions deliberately are inimitable. The brands that let them happen by default are interchangeable. SARA must make each of the ten with conviction.</div>
    <div class="bid-grid">
      <div class="bid-col">
        <div class="bid-col-h">Dimension 1 of 2</div>
        <h3 class="bid-col-title">Visual <span class="it">identity.</span></h3>
{vis}
      </div>
      <div class="bid-col">
        <div class="bid-col-h">Dimension 2 of 2</div>
        <h3 class="bid-col-title">Verbal <span class="it">identity.</span></h3>
{verb}
      </div>
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

# Direction: 5 visual + 5 verbal cards
VISUAL_DIRECTION = [
    ("Typography", "Cormorant + Jost.",
     "Maintain Cormorant Garamond (display serif, italic-friendly) paired with Jost (functional sans). Italic for emotion. Letter-spaced uppercase for tags.",
     "Refuse: bolded serifs · decorative scripts · sans-serif headlines."),
    ("Palette", "Forest. Gold. Cream.",
     "Forest green (depth) + gold (warmth, authority) + cream (calm). Sage and stone as neutrals.",
     "Refuse: chrome · neon · navy · beige hospitality default."),
    ("Photography", "Three layers, never four.",
     "Ritual (hands, breath, eyes closed), landscape (Andaman, Phuket forest, Pru farm), material (botanicals, food, ceramics, linen).",
     "Refuse: lifestyle stock · drone-glamour · over-saturated colour."),
    ("Materials", "Linen, wood, stone, ceramic, brass.",
     "Specify the material profile of every guest space. Teak and jackwood. Hand-thrown ceramic. Brushed brass.",
     "Refuse: chrome · glossy plastic · mass-produced finishes."),
    ("Iconography", "One signature object.",
     "Commission one signature SARA object &mdash; a brass measuring cup, a hand-thrown bowl, a perfume stopper &mdash; that becomes the brand&rsquo;s visual hero.",
     "Refuse: borrowed iconography · generic botanical clip-art."),
]
VERBAL_DIRECTION = [
    ("Tone", "Restrained but warm.",
     "Scientific but sensual. The CLP-meets-Soneva voice &mdash; clinical credibility wearing barefoot informality.",
     "Refuse: neutral wellness-conference voice · aspirational marketing copy."),
    ("Vocabulary", "Brand-owned words.",
     "Adopt: Method, Platform, Living well, Practice, Family, Pru, Andaman, Phuket.",
     "Refuse: Detox · Self-care · Wellness journey · Treatment · Reset."),
    ("Signature phrases", "Five lines that travel.",
     "Develop the SARA repertoire. Starting candidates: &lsquo;The platform of living well.&rsquo; &lsquo;The SARA Method.&rsquo; &lsquo;From the Pru.&rsquo;",
     "Refuse: borrowed taglines · interchangeable wellness adjectives."),
    ("Narrative", "One paragraph origin.",
     "Compress SARA&rsquo;s story: Montara family lineage + Phuket terroir + CLP partnership + multi-generational philosophy.",
     "Refuse: long brand essays · multiple origin versions · history-by-committee."),
    ("Naming system", "&lsquo;The SARA [Noun].&rsquo;",
     "All programmes follow one logic: The SARA Method · The SARA Reset · The SARA Calendar · The SARA Cabin · The SARA Honey.",
     "Refuse: free-form programme names · borrowed naming patterns from competitors."),
]

def build_direction(page_num):
    def cards(items):
        return "\n".join([
            f"""      <div class="bdir-card">
        <div class="bdir-tag">{tag}</div>
        <h4 class="bdir-name">{name}</h4>
        <div class="bdir-text">{text}</div>
        <div class="bdir-refuse">{refuse}</div>
      </div>"""
            for tag, name, text, refuse in items
        ])
    vis_html = cards(VISUAL_DIRECTION)
    verb_html = cards(VERBAL_DIRECTION)
    return f"""
<!-- ═══════════════════ NEW WELLNESS BRAND · SARA BRAND IDENTITY DIRECTION ═══════════════════ -->
<section class="S forest">
  <div>
    <div class="eye">30-Brand Identity Study · Direction</div>
    <h2 class="D2">SARA brand identity &mdash; <span class="gd it">the direction.</span></h2>
    <div class="rule"></div>
    <div class="body lg">Ten direction decisions, made now, with conviction. Five on the visual side. Five on the verbal side. Each card states what we&rsquo;ll build and what we&rsquo;ll refuse &mdash; because identity is as much about restraint as about choice.</div>
    <div class="bdir-grid">
      <div class="bdir-col">
        <div class="bdir-col-h">Dimension 1 of 2</div>
        <h3 class="bdir-col-title">Visual <span class="it">direction.</span></h3>
{vis_html}
      </div>
      <div class="bdir-col">
        <div class="bdir-col-h">Dimension 2 of 2</div>
        <h3 class="bdir-col-title">Verbal <span class="it">direction.</span></h3>
{verb_html}
      </div>
    </div>
  </div>
  <div class="pg">{page_num:02d}</div>
</section>"""

# ─── ASSEMBLE ────────────────────────────────────────────────────────────
parts = [build_intro(9)]
page = 10
for cat in CATEGORIES:
    parts.append(build_category(cat, page))
    page += 1
parts.append(build_summary(page)); page += 1
parts.append(build_direction(page)); page += 1
new_block = "\n".join(parts)

# ─── PERFORM EDITS ───────────────────────────────────────────────────────
text = HTML_PATH.read_text()

# 1) Replace old CSS block (find from /* ───── 30-BRAND STUDY · INTRO ───── */ through last 30-brand class)
# Old block ended right before .next or the next existing CSS rule. Easier: regex strip from "/* ───── 30-BRAND STUDY · INTRO" to right before "</style>"
# But we don't want to strip OTHER stuff. Let me find the boundaries we wrote.
old_css_start = "/* ───── 30-BRAND STUDY · INTRO ───── */"
old_css_end = ".dir-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.82rem;line-height:1.75;color:rgba(255,255,255,.72);margin-top:auto;padding-top:18px}"
if old_css_start in text and old_css_end in text:
    start_idx = text.index(old_css_start)
    end_idx = text.index(old_css_end) + len(old_css_end)
    text = text[:start_idx] + NEW_CSS.strip() + text[end_idx:]
else:
    raise RuntimeError("Could not find old CSS boundaries")

# 2) Replace old 13-page block (between Platform end and Marketing Collateral)
block_start_anchor = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND · 30-BRAND STUDY · INTRODUCTION ═══════════════════ -->"
block_end_anchor = "<!-- ═══════════════════ 9B INITIATIVE — MARKETING COLLATERAL PREPARATION ═══════════════════ -->"
if block_start_anchor not in text or block_end_anchor not in text:
    raise RuntimeError("Could not find page block boundaries")
start_idx = text.index(block_start_anchor)
end_idx = text.index(block_end_anchor)
# Take whatever whitespace exists between the start anchor and the platform </section> above
# Actually we want to replace from start_idx to end_idx
before = text[:start_idx]
after = text[end_idx:]
text = before + new_block.lstrip() + "\n\n" + after

# Write
HTML_PATH.write_text(text)

# Verify counts
sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections open: {sections}  close: {closes}")
print(f"Page tags: {pgs}")
print(f"File size: {len(text):,} chars")
