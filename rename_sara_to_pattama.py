"""
Rename brand from SARA to Pattama in the V2 deck.
Updates the brand name, the Pali script, the etymology line, and the philosophical description.
"""

from pathlib import Path

V2 = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy-v2-pattama.html")
text = V2.read_text()

# ─── 1. THE PALI SCRIPT + ETYMOLOGY (page 05 reveal) ─────────────────────
# Old: सार · sāra | "Sanskrit and Pali. Essence. What truly matters..."
# New: ปฐม · paṭhama | "Thai and Pali. First. Foremost. The beginning. The original way of living."

text = text.replace(
    'सार &middot; <em>sāra</em>',
    'ปฐม &middot; <em>paṭhama</em>',
    1,
)

text = text.replace(
    'Sanskrit and Pali. Essence. What truly matters. Inner value. The core of life.',
    'Thai and Pali. First. Foremost. The beginning. The original way of living.',
)

# ─── 2. THE BRAND DESCRIPTION (replace SARA reference inside) ────────────
text = text.replace(
    'SARA is a return to meaningful living &mdash; where wellbeing is integrated into everyday life, relationships, nature, and time itself. Not escape. Living well, fully, and together.',
    'Pattama is the beginning of meaningful living &mdash; where wellbeing is integrated into everyday life, relationships, nature, and time itself. Not escape. Living well, fully, and together.',
)

# ─── 3. BRAND NAME REPLACEMENT EVERYWHERE ────────────────────────────────
# "SARA" → "Pattama" (case-sensitive uppercase brand name)
sara_count = text.count("SARA")
text = text.replace("SARA", "Pattama")
print(f"Replaced 'SARA' with 'Pattama': {sara_count} occurrences")

# Title attribute / page metadata — handle the deck title if it mentions SARA
# (doesn't appear in this deck's title, but just in case)

# ─── 4. URL / DOMAIN REFERENCES ──────────────────────────────────────────
# sara.com → pattama.com (in any remaining artwork directions)
url_count = text.count("sara.com")
text = text.replace("sara.com", "pattama.com")
print(f"Replaced 'sara.com' with 'pattama.com': {url_count} occurrences")

# @sara handle if present
at_sara_count = text.count("@sara")
text = text.replace("@sara", "@pattama")
print(f"Replaced '@sara' with '@pattama': {at_sara_count} occurrences")

# Lowercase brand references in copy (Sanskrit transliteration aside)
# "sara" alone → "Pattama" — be very careful to avoid breaking sāra/sara-class-names
# Check what's left
import re
remaining_lc_sara = re.findall(r'\bsara\b', text, flags=re.IGNORECASE)
print(f"Remaining lowercase/mixed-case 'sara' word boundaries: {len(remaining_lc_sara)}")
# These remaining ones likely include 'sāra' (etymology) — leave as-is

V2.write_text(text)

# Verify
final_sara = text.count("SARA")
final_pattama = text.count("Pattama")
print(f"\nFinal counts:")
print(f"  SARA: {final_sara}")
print(f"  Pattama: {final_pattama}")
