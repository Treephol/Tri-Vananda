"""
Add two new pages after the PATTAMA Reveal (page 05):
- Page 06: Option 2 · The Lotus (paṭhama / padma / pathum connection)
- Page 07: Option 3 · The Family Name (Pattamasevi in the lineage of family-named houses)

Also retroactively label the existing reveal page as Option 1.
Renumber subsequent pages by +2.
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── 1. UPDATE EXISTING PAGE 05 EYEBROW TO MARK AS OPTION 1 ──────────────
text = text.replace(
    '<div class="eye" style="margin-bottom:0">New Wellness Brand Development · The Name</div>',
    '<div class="eye" style="margin-bottom:0">New Wellness Brand Development · The Name · Option 1</div>'
)

# ─── 2. NEW CSS ─────────────────────────────────────────────────────────
NEW_CSS = """
/* ───── NAME DESCRIPTION OPTIONS · meaning chart + houses grid ───── */
.meaning-chart{display:grid;grid-template-columns:1fr;gap:0;margin:36px auto 32px;max-width:580px;border:1px solid rgba(184,148,88,.25);background:rgba(184,148,88,.04)}
.meaning-row{display:grid;grid-template-columns:200px 1fr;padding:18px 28px;border-bottom:1px solid rgba(184,148,88,.14);align-items:baseline;gap:24px}
.meaning-row:last-child{border-bottom:0;background:rgba(184,148,88,.06)}
.meaning-word{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.15rem;color:var(--gold-lt);line-height:1.3;letter-spacing:.01em}
.meaning-word small{display:block;font-family:'Jost',sans-serif;font-style:normal;font-weight:200;font-size:.55rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);line-height:1.5;margin-top:4px}
.meaning-def{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.05rem;color:rgba(255,255,255,.78);line-height:1.4}

.houses-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;background:rgba(184,148,88,.18);border:1px solid rgba(184,148,88,.18);margin:36px auto 32px;max-width:900px}
.house-cell{background:var(--ink);padding:22px 18px;display:flex;flex-direction:column;gap:6px;text-align:center}
.house-name{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.15rem;color:var(--white);line-height:1.2}
.house-meta{font-family:'Jost',sans-serif;font-weight:200;font-size:.56rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);line-height:1.55}
.house-founder{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.4;margin-top:6px}
"""

text = text.replace("</style>", NEW_CSS + "\n</style>", 1)

# ─── 3. NEW PAGES HTML ──────────────────────────────────────────────────
PAGE_06 = """
<!-- ═══════════════════ 06 NEW WELLNESS BRAND · THE NAME · OPTION 2 · THE LOTUS ═══════════════════ -->
<section class="S bg">
  <div class="vyana-wrap">
    <div class="vyana-inner">
      <div class="eye" style="margin-bottom:0">New Wellness Brand Development &middot; The Name &middot; Option 2</div>
      <div class="vyana-label">Another meaning</div>
      <div class="vyana-positioning">PATTAMA, <span style="font-style:normal">the Lotus.</span></div>
      <div class="meaning-chart">
        <div class="meaning-row">
          <div class="meaning-word">paṭhama<small>Pali</small></div>
          <div class="meaning-def">First. Foremost. The beginning.</div>
        </div>
        <div class="meaning-row">
          <div class="meaning-word">padma<small>Sanskrit</small></div>
          <div class="meaning-def">The lotus. The flower of awakening.</div>
        </div>
        <div class="meaning-row">
          <div class="meaning-word">ปทุม &middot; pathum<small>Thai</small></div>
          <div class="meaning-def">The sacred lotus. The first to bloom.</div>
        </div>
        <div class="meaning-row">
          <div class="meaning-word">PATTAMA<small>The brand</small></div>
          <div class="meaning-def">The first to rise. The first to open.</div>
        </div>
      </div>
      <div class="vyana-tagline">Living Well Begins Together</div>
      <div class="vyana-strapline">The meaningful aspects of life for the multigenerational family.</div>
      <div class="vyana-description">The lotus opens first at dawn, before the rest of the garden. It rises clean from muddy water, untouched by what surrounds it. It is the central image of Thai Buddhist awakening &mdash; the flower of the Buddha. PATTAMA carries this depth: the firstness, the unfolding, the quiet emergence from the depths. A brand for the way of life that opens itself, daily, to meaning.</div>
    </div>
  </div>
  <div class="pg">06</div>
</section>"""

PAGE_07 = """
<!-- ═══════════════════ 07 NEW WELLNESS BRAND · THE NAME · OPTION 3 · THE FAMILY NAME ═══════════════════ -->
<section class="S bg">
  <div class="vyana-wrap">
    <div class="vyana-inner">
      <div class="eye" style="margin-bottom:0">New Wellness Brand Development &middot; The Name &middot; Option 3</div>
      <div class="vyana-label">A family name</div>
      <div class="vyana-positioning">PATTAMA, <span style="font-style:normal">the Family.</span></div>
      <div class="houses-grid">
        <div class="house-cell">
          <div class="house-meta">Paris &middot; 1837</div>
          <div class="house-name">Herm&egrave;s</div>
          <div class="house-founder">Thierry Herm&egrave;s</div>
        </div>
        <div class="house-cell">
          <div class="house-meta">Paris &middot; 1909</div>
          <div class="house-name">Chanel</div>
          <div class="house-founder">Coco Chanel</div>
        </div>
        <div class="house-cell">
          <div class="house-meta">Rome &middot; 1884</div>
          <div class="house-name">Bulgari</div>
          <div class="house-founder">Sotirio Bulgari</div>
        </div>
        <div class="house-cell">
          <div class="house-meta">Maldives &middot; 1995</div>
          <div class="house-name">Soneva</div>
          <div class="house-founder">Sonu &amp; Eva Shivdasani</div>
        </div>
        <div class="house-cell">
          <div class="house-meta">Umbria &middot; 1994</div>
          <div class="house-name">Reschio</div>
          <div class="house-founder">Bolza family</div>
        </div>
      </div>
      <div class="vyana-tagline">Living Well Begins Together</div>
      <div class="vyana-strapline">The meaningful aspects of life for the multigenerational family.</div>
      <div class="vyana-description">The world&rsquo;s most enduring luxury houses bear the name of a family. The name is a contract &mdash; a promise that the family stands behind every choice the brand makes. PATTAMA is named for the Pattamasevi family, the stewards who founded the brand. The family is the accountability layer. The name is the inheritance.</div>
    </div>
  </div>
  <div class="pg">07</div>
</section>"""

new_block = PAGE_06 + "\n" + PAGE_07

# ─── 4. INSERT AFTER PAGE 05 (PATTAMA REVEAL) ───────────────────────────
# Find the end of page 05 — the closing </section> right after pg "05"
idx_pg5 = text.index('<div class="pg">05</div>')
idx_end = text.index('</section>', idx_pg5) + len('</section>')

text = text[:idx_end] + new_block + text[idx_end:]

# ─── 5. RENUMBER pages 06-32 → 08-34 (shift by 2) ───────────────────────
# Find the existing page 06 (Org Structure) which comes AFTER our new insertions
# We need to renumber it and all subsequent pages
# Find the FIRST occurrence of the existing Org Structure anchor
org_anchor = "<!-- ═══════════════════ 07 NEW WELLNESS BRAND · ORGANISATION STRUCTURE ═══════════════════ -->"
if org_anchor not in text:
    raise RuntimeError("Cannot find Org Structure anchor for renumbering")

head, _, tail = text.partition(org_anchor)
# In tail, renumber existing 06-32 → 08-34 (high to low)
for old, new in [(32, 34), (31, 33), (30, 32), (29, 31), (28, 30),
                 (27, 29), (26, 28), (25, 27), (24, 26), (23, 25),
                 (22, 24), (21, 23), (20, 22), (19, 21), (18, 20),
                 (17, 19), (16, 18), (15, 17), (14, 16), (13, 15),
                 (12, 14), (11, 13), (10, 12), (9, 11), (8, 10),
                 (7, 9), (6, 8)]:
    tail = tail.replace(f'<div class="pg">{old:02d}</div>', f'<div class="pg">{new:02d}</div>')
text = head + org_anchor + tail

V2.write_text(text)

sections = text.count("<section")
closes = text.count("</section>")
pgs = text.count('<div class="pg">')
print(f"Sections: {sections} open, {closes} close")
print(f"Page tags: {pgs}")
