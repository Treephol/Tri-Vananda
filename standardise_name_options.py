"""
Rebuild Options 2 and 3 to follow the SAME 9-line format as Option 1.

Each option must carry:
  1. Eyebrow      — New Wellness Brand Development · The Name · Option N
  2. Label        — Introducing
  3. Positioning  — Product/positioning line (varies by concept)
  4. Name         — PATTAMA (same)
  5. Pronunciation — ปฐม · paṭhama (same)
  6. Tagline      — Living Well + concept (varies)
  7. Sub-tagline  — concept-specific (varies)
  8. Meaning      — concept-specific etymology (varies)
  9. Explanation  — concept-specific narrative (varies)
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── REPLACE PAGE 06 (LOTUS) ─────────────────────────────────────────────
new_page_06 = """<!-- ═══════════════════ 06 NEW WELLNESS BRAND · THE NAME · OPTION 2 · THE LOTUS ═══════════════════ -->
<section class="S bg">
  <div class="vyana-wrap">
    <div class="vyana-inner">
      <div class="eye" style="margin-bottom:0">New Wellness Brand Development &middot; The Name &middot; Option 2</div>
      <div class="vyana-label">Introducing</div>
      <div class="vyana-positioning">A Garden of Awakening</div>
      <div class="vyana-name">PATTAMA</div>
      <div class="vyana-script">ปฐม &middot; <em>paṭhama</em></div>
      <div class="vyana-tagline">Living Well, in Quiet Bloom</div>
      <div class="vyana-strapline">Rooted in the depths, rising in light &mdash; for the multigenerational family.</div>
      <div class="vyana-etymology">Pali &middot; Sanskrit &middot; Thai. paṭhama &middot; padma &middot; pathum. First. Lotus. The flower of awakening.</div>
      <div class="vyana-description">The lotus opens first at dawn, before the rest of the garden &mdash; clean from muddy water, untouched by what surrounds it. It is the central image of Thai Buddhist awakening, the flower of the Buddha. PATTAMA carries this depth: firstness, unfolding, the quiet emergence from the depths. A way of living that opens itself, daily, to meaning.</div>
    </div>
  </div>
  <div class="pg">06</div>
</section>"""

# Find old page 06 (Lotus) and replace
old_page_06_start = "<!-- ═══════════════════ 06 NEW WELLNESS BRAND · THE NAME · OPTION 2 · THE LOTUS ═══════════════════ -->"
old_page_06_end_anchor = "<!-- ═══════════════════ 07 NEW WELLNESS BRAND · THE NAME · OPTION 3 · THE FAMILY NAME ═══════════════════ -->"

if old_page_06_start not in text:
    raise RuntimeError("Cannot find old page 06 anchor")
if old_page_06_end_anchor not in text:
    raise RuntimeError("Cannot find old page 07 anchor")

start_idx = text.index(old_page_06_start)
end_idx = text.index(old_page_06_end_anchor)
text = text[:start_idx] + new_page_06 + "\n" + text[end_idx:]

# ─── REPLACE PAGE 07 (FAMILY NAME) ───────────────────────────────────────
new_page_07 = """<!-- ═══════════════════ 07 NEW WELLNESS BRAND · THE NAME · OPTION 3 · THE FAMILY NAME ═══════════════════ -->
<section class="S bg">
  <div class="vyana-wrap">
    <div class="vyana-inner">
      <div class="eye" style="margin-bottom:0">New Wellness Brand Development &middot; The Name &middot; Option 3</div>
      <div class="vyana-label">Introducing</div>
      <div class="vyana-positioning">A House of Stewardship</div>
      <div class="vyana-name">PATTAMA</div>
      <div class="vyana-script">ปฐม &middot; <em>paṭhama</em></div>
      <div class="vyana-tagline">Living Well, Through the Generations</div>
      <div class="vyana-strapline">The standards a family stewards &mdash; for the multigenerational family.</div>
      <div class="vyana-etymology">Thai. Pattamasevi. The family name. The contract. The inheritance.</div>
      <div class="vyana-description">Like the world&rsquo;s most enduring luxury houses &mdash; Herm&egrave;s, Chanel, Bulgari, Soneva, Reschio &mdash; PATTAMA carries a family name. Pattamasevi. The family becomes the contract: every standard the brand keeps is a standard the family signs. Not branding &mdash; a name handed down.</div>
    </div>
  </div>
  <div class="pg">07</div>
</section>"""

old_page_07_start = "<!-- ═══════════════════ 07 NEW WELLNESS BRAND · THE NAME · OPTION 3 · THE FAMILY NAME ═══════════════════ -->"
old_page_07_end_anchor = "<!-- ═══════════════════ 07 NEW WELLNESS BRAND · ORGANISATION STRUCTURE ═══════════════════ -->"

if old_page_07_start not in text:
    raise RuntimeError("Cannot find old page 07 anchor")
if old_page_07_end_anchor not in text:
    raise RuntimeError("Cannot find Org Structure anchor")

start_idx = text.index(old_page_07_start)
end_idx = text.index(old_page_07_end_anchor)
text = text[:start_idx] + new_page_07 + "\n" + text[end_idx:]

V2.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
