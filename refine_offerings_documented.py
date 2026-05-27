"""
Refine V2 offerings page:
- No Praya Palazzo
- Only documented offerings (from masterplan + Trisara programs + RFP)
- No membership references (services and experiences only)
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── REFINED PILLAR DATA (documented offerings only) ─────────────────────
PILLARS = [
    {
        "num": "01",
        "name": "Family &amp; Multi-Generations",
        "img": "collective-09.jpg",
        "sub": "The brand's centre",
        "items": [
            ("Multigenerational Programmes", "Across every age"),
            ("Children's Wellness &amp; Adventure", "For the youngest"),
            ("Active Aging", "Graceful aging via blue zones"),
            ("Senior Wellness", "Aging with dignity"),
            ("Family Retreats", "Multi-day stays"),
            ("Dog-Assisted Therapy", "Animal companionship that heals"),
            ("Nature Playground", "Children &amp; families"),
            ("Intergenerational Programming", "Shared learning"),
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
            ("Spirit of Thailand Programme", "Cultural immersion"),
            ("Traditional Thai Doctor Consultation", "Thai medicine authority"),
            ("Thai Cooking Classes", "Food as cultural craft"),
        ],
    },
    {
        "num": "03",
        "name": "Community &amp; Belonging",
        "img": "collective-07.jpg",
        "sub": "The room, the gatherings",
        "items": [
            ("Community Mall", "Shared centre"),
            ("Social Aqathermal", "Communal water rituals"),
            ("Restaurant Outlets", "Three dining venues"),
            ("Communal Dining Experiences", "Multi-gen gatherings"),
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
            ("La Crique", "Coastal dining"),
            ("Plant-Based Cuisine", "Back to Earth menu"),
            ("Thai Herbal Teas", "Botanical infusions"),
            ("Farm Visits &amp; Harvest", "Guest participation"),
            ("Food as Medicine", "Traditional Thai approach"),
            ("Local Food Market Excursions", "Phuket food culture"),
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
            ("Nature Playground", "Outdoor immersion"),
            ("Ocean Immersion at Trisara", "Beachfront access"),
            ("Free-Diving Sessions", "House reef training"),
            ("Snorkelling &amp; Reef Trips", "Local marine life"),
            ("Sea of Tranquillity Programme", "Ocean-led stress management"),
            ("Day Boat Excursions", "Coastal exploration"),
            ("Outdoor Sport Hub", "Multi-discipline"),
        ],
    },
    {
        "num": "06",
        "name": "Stewardship &amp; Regeneration",
        "img": "collective-03.jpg",
        "sub": "What we give back",
        "items": [
            ("Honey Bee Farm", "Biodiversity &amp; honey"),
            ("Butterfly Farm", "Native species sanctuary"),
            ("Animal Quarter", "Ducks, chickens, rabbits, swans"),
            ("Coral Reef Conservation", "House reef stewardship"),
            ("Sustainability Officer Talks", "Ocean ecology &amp; reef"),
            ("Farm Participation Sessions", "Planting &amp; harvest"),
            ("Food Security Practices", "Local sovereignty"),
            ("Ocean Ecology Programme", "Marine education"),
        ],
    },
    {
        "num": "07",
        "name": "Body &amp; Practice",
        "img": "collective-02.jpg",
        "sub": "The daily body",
        "items": [
            ("Muay Thai Programme", "Fighting Chance"),
            ("Wai Kru Ceremony", "Muay Thai cultural ritual"),
            ("Yoga", "Private &amp; group classes"),
            ("Tai Chi &amp; Qigong", "Moving meditation"),
            ("Free-Diving Training", "Breath &amp; body"),
            ("Personal Fitness Training", "Stretching, weights, cardio"),
            ("Hiking &amp; Outdoor Training", "Terrain-based fitness"),
            ("Fitness Centre", "Indoor training"),
            ("Outdoor Sport Hub", "Multi-discipline"),
            ("Thai Boxing Match Excursions", "Sport culture"),
        ],
    },
    {
        "num": "08",
        "name": "Mind &amp; Spirit",
        "img": "collective-04.jpg",
        "sub": "The interior life",
        "items": [
            ("Meditation", "Private &amp; group practice"),
            ("Breathwork", "Pranayama &amp; breath training"),
            ("Mindfulness Practice", "Daily exercises"),
            ("Meditation Hall", "Silent practice space"),
            ("Cognitive Healing", "Brain-care frontier"),
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
            ("Acupuncture", "TCM precision"),
            ("Cupping", "Circulation &amp; release"),
            ("Lymphatic Drainage", "Circulatory healing"),
            ("Hydrotherapy", "Water-based therapy"),
            ("Social Aqathermal", "Communal water rituals"),
            ("Treatment Zone", "Dedicated therapy spaces"),
            ("Wellness Studio", "Integrated treatment"),
            ("Thai Herbal Medicine", "Traditional remedies"),
            ("CLP Longevity Programmes", "Clinical authority"),
            ("Active Aging Programmes", "Blue-zone clinical"),
        ],
    },
]

# ─── BUILD CELLS ─────────────────────────────────────────────────────────
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

# ─── REPLACE OLD OFFERINGS SECTION ───────────────────────────────────────
old_start = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE COLLECTIVE ═══════════════════ -->"
old_end_anchor = "<!-- ═══════════════════ 09 NEW WELLNESS BRAND · 30-BRAND IDENTITY STUDY · COVER ═══════════════════ -->"

start_idx = text.index(old_start)
end_idx = text.index(old_end_anchor)
text = text[:start_idx] + new_section + "\n\n" + text[end_idx:]

V2.write_text(text)
print(f"File size: {len(text):,} chars")

# Verify no Praya Palazzo and no membership terms
for term in ["Praya Palazzo", "Yearly Membership", "Founding Members", "Members' Calendar", "Sponsorship", "Members' Lounge"]:
    count = text.count(term)
    if count > 0:
        # Check if it's only in research section (acceptable) or in offerings (not)
        # For simplicity, just print
        print(f"  '{term}': {count} remaining mention(s) in file")
