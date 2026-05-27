"""
Rebuild the Collective offerings page (V2 page 09) with the new 9-pillar framework
ordered Family → Heritage → Community → Farm & Table → Nature → Stewardship → Body → Mind → Recovery.
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── PILLAR DATA ─────────────────────────────────────────────────────────
PILLARS = [
    {
        "num": "01",
        "name": "Family &amp; Multi-Generations",
        "img": "collective-09.jpg",
        "sub": "The brand's centre",
        "items": [
            ("Multigenerational Programmes", "Across every age"),
            ("Children's Wellness &amp; Adventure", "For the youngest"),
            ("Teen Wellness Programmes", "For adolescents"),
            ("Active Aging", "Graceful aging via blue zones"),
            ("Mother-Daughter &middot; Father-Son", "Pair retreats"),
            ("Family Retreats", "Multi-day stays"),
            ("Pregnancy &amp; Postnatal", "Mother &amp; baby"),
            ("Senior Wellness", "Aging with dignity"),
            ("Dog-Assisted Therapy", "Animal companionship that heals"),
            ("Babysitting &amp; Kids' Camps", "Supervised care"),
            ("Intergenerational Classes", "Shared learning"),
            ("Family Conversations", "Facilitated dialogues"),
        ],
    },
    {
        "num": "02",
        "name": "Heritage &amp; Wisdom",
        "img": "collective-08.jpg",
        "sub": "The Thai foundation",
        "items": [
            ("Buddhist Temple Visits", "Local spiritual tradition"),
            ("Buddhist Philosophy Lectures", "Thai-led wisdom"),
            ("Traditional Thai Doctor", "Thai medicine consultation"),
            ("Thai Cooking Classes", "Food as medicine"),
            ("Thai Craft Workshops", "Pottery, textile, weaving"),
            ("Praya Palazzo Heritage Stay", "Riverside Thai-Italian"),
            ("Thai Language &amp; Etiquette", "Cultural literacy"),
            ("Local Wisdom Salons", "Community storytelling"),
            ("Thai Classical Music", "Ambient programming"),
            ("Botanical Heritage Lectures", "Herbal knowledge"),
            ("Library &amp; Reading Rooms", "Books, journals, archive"),
            ("Mentorship Programmes", "Intergenerational learning"),
        ],
    },
    {
        "num": "03",
        "name": "Community &amp; Belonging",
        "img": "collective-07.jpg",
        "sub": "The room, the gatherings",
        "items": [
            ("Yearly Membership", "Annual access &amp; admission"),
            ("52-Week Members' Calendar", "Programming, salons, workshops"),
            ("Members' Lounge &amp; Spaces", "Exclusive access"),
            ("Community Mall", "Shared centre"),
            ("Social Aqathermal", "Communal water rituals"),
            ("Founding Members' Programme", "Early cohort"),
            ("Cultural Conversations", "Speakers &amp; civic salons"),
            ("Resident Artists Programme", "Visiting practitioners"),
            ("Members' Gatherings", "Periodic events"),
            ("Sponsorship &amp; Admission", "Curated entry"),
            ("Co-Working Amenities", "For resident members"),
            ("Live Music &amp; Performance", "Curated programming"),
        ],
    },
    {
        "num": "04",
        "name": "The Farm &amp; The Table",
        "img": "collective-06.jpg",
        "sub": "From the land to the plate",
        "items": [
            ("Trivananda Farm", "Working organic farm"),
            ("PRU", "Michelin-starred dining"),
            ("Jampa", "Farm-to-table dining"),
            ("Long Table Communal Dining", "Family-style"),
            ("Food as Medicine Programme", "Traditional Thai approach"),
            ("Thai Cooking Masterclasses", "For guests &amp; members"),
            ("Thai Herbal Teas &amp; Infusions", "Botanical estate"),
            ("Estate Honey, Oil &amp; Preserves", "Take-home product line"),
            ("Wine Pairings &amp; Cellar", "Curated provisions"),
            ("Plant-Based Cuisine", "For cleansing &amp; vitality"),
            ("Farm Visits &amp; Harvest", "Guest participation"),
            ("Local Food Excursions", "Phuket markets &amp; dining"),
        ],
    },
    {
        "num": "05",
        "name": "Nature &amp; Ecotherapy",
        "img": "collective-05.jpg",
        "sub": "What nature gives",
        "items": [
            ("1.2 km Forest Bathing Trail", "Shinrin-yoku immersion"),
            ("Walking &amp; Hiking Trails", "Phuket interior"),
            ("Nature Playground", "Children &amp; families"),
            ("Ocean Immersion at Trisara", "Beachfront access"),
            ("Free-Diving Sessions", "House reef training"),
            ("Snorkelling &amp; Reef Trips", "Local marine life"),
            ("Bird-Watching", "Phuket biodiversity"),
            ("Stargazing &amp; Observatory", "Night-sky programming"),
            ("Sunrise Meditation", "Outdoor practice"),
            ("Outdoor Sport Hub", "Multi-discipline"),
            ("Forest Sound Baths", "Natural acoustics"),
            ("Botanical Garden Walks", "Native species"),
        ],
    },
    {
        "num": "06",
        "name": "Stewardship &amp; Regeneration",
        "img": "collective-03.jpg",
        "sub": "What we give back",
        "items": [
            ("Honey Bee Farm", "Biodiversity &amp; honey programme"),
            ("Butterfly Farm", "Native species sanctuary"),
            ("Animal Quarter", "Ducks, chickens, rabbits, swans"),
            ("Coral Reef Conservation", "Reef restoration"),
            ("Sustainability Dialogues", "Ocean ecology talks"),
            ("Farm Participation", "Planting &amp; harvest"),
            ("Composting &amp; Circular Farming", "Closed-loop ecology"),
            ("Local Food Sovereignty", "Supply security"),
            ("Plastic-Free Practice", "Material conscience"),
            ("Biodiversity Walks", "Guided naturalist tours"),
            ("Reforestation Programme", "Climate participation"),
            ("Regenerative Agriculture", "Soil &amp; seed"),
        ],
    },
    {
        "num": "07",
        "name": "Body &amp; Practice",
        "img": "collective-02.jpg",
        "sub": "The daily body",
        "items": [
            ("Muay Thai Programme", "Thai martial heritage"),
            ("Yoga", "Private &amp; group classes"),
            ("Tai Chi &amp; Qigong", "Moving meditation"),
            ("Free-Diving Training", "Breath &amp; body"),
            ("Personal Fitness Training", "Bespoke programme"),
            ("Strength &amp; Conditioning", "Outdoor Sport Hub"),
            ("Pilates Studio", "Core practice"),
            ("Hiking &amp; Outdoor Training", "Terrain-based"),
            ("Aquatic Practice", "Lap pool &amp; swimming"),
            ("Boxing Match Excursions", "Thai sport culture"),
            ("Cycling &amp; Mountain Bike", "Phuket trails"),
            ("Mobility &amp; Stretch Studio", "Recovery-side practice"),
        ],
    },
    {
        "num": "08",
        "name": "Mind &amp; Spirit",
        "img": "collective-04.jpg",
        "sub": "The interior life",
        "items": [
            ("Meditation Hall", "Silent practice"),
            ("Private &amp; Group Meditation", "Spirit of Thailand"),
            ("Breathwork", "Pranayama &amp; breath training"),
            ("Buddhist Philosophy", "Thai-led lectures"),
            ("Mindfulness Exercises", "Daily practice"),
            ("Silence Practice", "Half-day or full-day"),
            ("Sound Bath &amp; Healing", "Vibrational therapy"),
            ("Cognitive Healing", "The brain-care frontier"),
            ("Journaling &amp; Reflection", "Guided"),
            ("Dream Work &amp; Inquiry", "Deeper layers"),
            ("Compassion Training", "Buddhist practice"),
            ("Forest Meditation", "Outdoor stillness"),
        ],
    },
    {
        "num": "09",
        "name": "Recovery &amp; Renewal",
        "img": "collective-01.jpg",
        "sub": "The deepest care",
        "items": [
            ("Thai Massage", "Full-body restoration"),
            ("Thai Poultice Massage", "Herbal heat therapy"),
            ("Acupuncture &amp; Cupping", "TCM bridge"),
            ("Lymphatic Drainage", "Circulatory healing"),
            ("Hydrotherapy &amp; Aqathermal", "Water therapies"),
            ("Salt Grotto &amp; Halotherapy", "Respiratory wellness"),
            ("Cryotherapy &amp; Contrast", "Inflammation protocols"),
            ("CLP Longevity Programmes", "Clinical authority"),
            ("Cellular Renewal Protocols", "Preventive care"),
            ("Biomarker &amp; Genetic Testing", "Personalised mapping"),
            ("IV Therapy &amp; NAD+", "Targeted infusions"),
            ("Hyperbaric Oxygen", "Cellular regeneration"),
        ],
    },
]

# ─── BUILD HTML ──────────────────────────────────────────────────────────
def build_cell(pillar):
    items_html = "\n".join([
        f'          <li><span class="ot-name">{name}</span><span class="ot-desc">{desc}</span></li>'
        for name, desc in pillar["items"]
    ])
    return f"""    <div class="ot-cell">
      <div class="ot-hero">
        <img src="images/{pillar["img"]}" alt="{pillar["name"]}" loading="lazy">
        <div class="ot-hero-overlay">
          <span class="ot-num">{pillar["num"]}</span><span class="ot-cat-h">{pillar["name"]}</span>
        </div>
      </div>
      <div class="ot-body">
        <div class="ot-cat-sub">{pillar["sub"]}</div>
        <ul class="ot-list">
{items_html}
        </ul>
      </div>
    </div>"""

cells_html = "\n".join([build_cell(p) for p in PILLARS])

# ─── BUILD ENTIRE NEW SECTION ────────────────────────────────────────────
new_section = f"""<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->
<section class="S ink">
  <div class="eye">New Wellness Brand Development &middot; The Collective</div>
  <div class="D2" style="max-width:980px;margin-bottom:18px">The offerings &mdash; <span class="it gd">across every generation.</span></div>
  <p class="body lg" style="max-width:920px">The Collective opens with the multigenerational family at its centre &mdash; supported by heritage, community, the table, and the land. Each pillar is a way of living well; together they describe a life shared across generations.</p>

  <div class="offerings-table">
{cells_html}
  </div>

  <div class="pg">09</div>
</section>"""

# ─── REPLACE THE OLD OFFERINGS SECTION ───────────────────────────────────
old_start = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->"
old_end_anchor = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND · 30-BRAND IDENTITY STUDY · COVER ═══════════════════ -->"

if old_start not in text:
    raise RuntimeError("Could not find offerings page start anchor")
if old_end_anchor not in text:
    raise RuntimeError("Could not find 30-brand cover end anchor")

start_idx = text.index(old_start)
end_idx = text.index(old_end_anchor)
text = text[:start_idx] + new_section + "\n\n" + text[end_idx:]

V2.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
print(f"File size: {len(text):,} chars")
