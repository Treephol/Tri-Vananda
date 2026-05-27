"""Enlarge text on the 30-Brand research pages (category cards + synthesis dimension cards)."""

from pathlib import Path

HTML_PATH = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")
text = HTML_PATH.read_text()

# Replacements (each pair is (old, new))
swaps = [
    # ─── CATEGORY (brand) CARDS (pages 11-20) ──────────────────────────────
    # Brand name
    (".cat-card-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.45rem;color:var(--white);line-height:1.1}",
     ".cat-card-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.75rem;color:var(--white);line-height:1.15}"),
    # Brand location (small caps)
    (".cat-card-loc{font-family:'Jost',sans-serif;font-weight:200;font-size:.55rem;letter-spacing:.26em;text-transform:uppercase;color:rgba(184,148,88,.75);line-height:1.5}",
     ".cat-card-loc{font-family:'Jost',sans-serif;font-weight:200;font-size:.65rem;letter-spacing:.28em;text-transform:uppercase;color:rgba(184,148,88,.8);line-height:1.5}"),
    # Brand essence (italic)
    (".cat-card-essence{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.95rem;color:rgba(255,255,255,.6);line-height:1.4;padding:8px 0 4px;border-bottom:1px solid rgba(184,148,88,.12)}",
     ".cat-card-essence{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.12rem;color:rgba(255,255,255,.65);line-height:1.4;padding:10px 0 6px;border-bottom:1px solid rgba(184,148,88,.14)}"),
    # Block label (Visual / Verbal)
    (".cat-block-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);line-height:1.5}",
     ".cat-block-label{font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);line-height:1.5}"),
    # Block body text
    (".cat-block-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.74rem;line-height:1.65;color:rgba(255,255,255,.74)}",
     ".cat-block-text{font-family:'Jost',sans-serif;font-weight:300;font-size:.88rem;line-height:1.7;color:rgba(255,255,255,.78)}"),

    # ─── SYNTHESIS DIMENSION CARDS (pages 21-22) ──────────────────────────
    # Dim image placeholder (bigger)
    (".dim-img{width:160px;height:120px;background:radial-gradient(ellipse at 50% 30%,rgba(110,130,100,.18),transparent 65%),radial-gradient(ellipse at 60% 80%,rgba(184,148,88,.15),transparent 60%),linear-gradient(135deg,#1e2820 0%,#0b0f13 50%,#141c22 100%);border:1px solid rgba(184,148,88,.18);position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}",
     ".dim-img{width:200px;height:160px;background:radial-gradient(ellipse at 50% 30%,rgba(110,130,100,.18),transparent 65%),radial-gradient(ellipse at 60% 80%,rgba(184,148,88,.15),transparent 60%),linear-gradient(135deg,#1e2820 0%,#0b0f13 50%,#141c22 100%);border:1px solid rgba(184,148,88,.18);position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}"),
    # Dim card padding and gap
    (".dim-card{display:grid;grid-template-columns:160px 1fr;gap:32px;padding:22px 26px;border-bottom:1px solid rgba(184,148,88,.14);align-items:center;background:var(--ink)}",
     ".dim-card{display:grid;grid-template-columns:200px 1fr;gap:42px;padding:32px 36px;border-bottom:1px solid rgba(184,148,88,.14);align-items:center;background:var(--ink)}"),
    # Dim number
    (".dim-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.6rem;color:var(--gold-lt);line-height:1}",
     ".dim-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:2.1rem;color:var(--gold-lt);line-height:1}"),
    # Dim name
    (".dim-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.35rem;color:var(--white);line-height:1.2}",
     ".dim-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.7rem;color:var(--white);line-height:1.2}"),
    # Dim strapline
    (".dim-strap{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.98rem;color:var(--gold-lt);line-height:1.35;margin-top:2px}",
     ".dim-strap{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.18rem;color:var(--gold-lt);line-height:1.4;margin-top:4px}"),
    # Dim description
    (".dim-desc{font-family:'Jost',sans-serif;font-weight:300;font-size:.76rem;color:rgba(255,255,255,.7);line-height:1.65;margin-top:6px;max-width:620px}",
     ".dim-desc{font-family:'Jost',sans-serif;font-weight:300;font-size:.95rem;color:rgba(255,255,255,.76);line-height:1.7;margin-top:10px;max-width:720px}"),
    # Dim evidence
    (".dim-evidence{font-family:'Jost',sans-serif;font-weight:300;font-size:.68rem;line-height:1.65;color:rgba(184,148,88,.85);margin-top:8px;letter-spacing:.02em}",
     ".dim-evidence{font-family:'Jost',sans-serif;font-weight:300;font-size:.82rem;line-height:1.7;color:rgba(184,148,88,.88);margin-top:14px;letter-spacing:.02em}"),
    # Dim evidence label
    (".dim-evidence-label{display:inline-block;font-family:'Jost',sans-serif;font-weight:200;font-size:.5rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin-right:8px;vertical-align:baseline}",
     ".dim-evidence-label{display:inline-block;font-family:'Jost',sans-serif;font-weight:200;font-size:.6rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);margin-right:10px;vertical-align:baseline}"),
    # Dim image await text
    (".dim-img-await{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.7rem;color:rgba(244,239,229,.35);line-height:1.4;text-align:center;padding:0 14px}",
     ".dim-img-await{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:.85rem;color:rgba(244,239,229,.4);line-height:1.4;text-align:center;padding:0 14px}"),

    # ─── PATTERN OVERVIEW PAGE 20 (5+5 grid) ──────────────────────────────
    # Slightly larger to match
    (".pat-overview-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.4rem;color:var(--gold-lt);line-height:1}",
     ".pat-overview-num{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:200;font-size:1.65rem;color:var(--gold-lt);line-height:1}"),
    (".pat-overview-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.02rem;color:var(--white);line-height:1.2;margin-top:4px}",
     ".pat-overview-name{font-family:'Cormorant Garamond',serif;font-weight:200;font-size:1.18rem;color:var(--white);line-height:1.25;margin-top:6px}"),
    (".pat-overview-strap{font-family:'Jost',sans-serif;font-weight:300;font-size:.66rem;line-height:1.55;color:rgba(255,255,255,.6);margin-top:auto}",
     ".pat-overview-strap{font-family:'Jost',sans-serif;font-weight:300;font-size:.78rem;line-height:1.6;color:rgba(255,255,255,.65);margin-top:auto}"),
    (".pat-overview-cell{background:var(--ink);padding:22px 18px;display:flex;flex-direction:column;gap:6px;min-height:140px}",
     ".pat-overview-cell{background:var(--ink);padding:28px 22px;display:flex;flex-direction:column;gap:8px;min-height:160px}"),
]

# Apply each swap exactly once (replace_all in case duplicates exist)
for old, new in swaps:
    n = text.count(old)
    if n == 0:
        print(f"  ⚠ Not found: {old[:60]}...")
    else:
        text = text.replace(old, new)
        print(f"  ✓ Updated ({n}x): {old.split('{')[0][:40]}")

HTML_PATH.write_text(text)
print("\nDone.")
