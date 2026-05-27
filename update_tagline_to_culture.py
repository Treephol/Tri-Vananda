"""
Replace tagline 'A platform of living well' → 'The Culture of Living Well'
Update related SARA-context 'platform' references to 'culture'
Preserve business-architecture 'platform' (multi-property platform, platform brand)
"""

from pathlib import Path
import re

DECK = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/tri-vananda-2026-pr-communications-strategy.html")

# ─── HTML DECK CHANGES ──────────────────────────────────────────────────
text = DECK.read_text()

# Direct tagline replacements (all 8 instances)
text = text.replace("A platform of living well", "The Culture of Living Well")
text = text.replace("a platform of living well", "the Culture of Living Well")
text = text.replace("the platform of living well", "the Culture of Living Well")

# Related SARA-context "platform" → "culture" changes
# These are SPECIFIC string replacements to avoid over-matching
context_changes = [
    # Timeline label
    ("Platform, naming &amp; identity", "Culture, naming &amp; identity"),
    # CLP card — "signing the platform's clinical..."
    ("signing the platform&rsquo;s clinical and longevity protocols",
     "signing the culture&rsquo;s clinical and longevity protocols"),
    # Tri Vananda card — "in the platform where it is own-able"
    ("The only place in the platform where it is own-able",
     "The only place in the culture where it is own-able"),
    # Plan section — "Step into the platform"
    ("Step into the platform through whichever door fits the family",
     "Step into the culture through whichever door fits the family"),
    # Plan section — "Three · Live the platform"
    ("Three &middot; Live the platform", "Three &middot; Live the culture"),
    ("Three · Live the platform", "Three · Live the culture"),
    # Org structure — "residential expression of the platform"
    ("The new development at Tri Vananda &mdash; the residential expression of the platform.",
     "The new development at Tri Vananda &mdash; the residential expression of the culture."),
    # Page 08 section
    ("═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE PLATFORM ═══════════════════",
     "═══════════════════ 09 NEW WELLNESS BRAND DEVELOPMENT · THE CULTURE ═══════════════════"),
    ('<div class="eye">New Wellness Brand Development · The Platform</div>',
     '<div class="eye">New Wellness Brand Development · The Culture</div>'),
    # Page 08 body paragraph
    ("The platform delivers a different experience for every age",
     "The culture takes a different form at every age"),
    # Vocabulary card on Direction page
    ("Adopt: Method, Platform, Living well, Practice, Family, Pru, Andaman, Phuket.",
     "Adopt: Method, Culture, Living well, Practice, Family, Pru, Andaman, Phuket."),
    # Signature phrases candidates
    ("Starting candidates: &lsquo;The platform of living well.&rsquo;",
     "Starting candidates: &lsquo;The Culture of Living Well.&rsquo;"),
    # Summary recap
    ("Platform for luxury wellness across generations",
     "A culture of luxury wellness across generations"),
]

for old, new in context_changes:
    if old not in text:
        print(f"  ⚠️  Not found (may already be updated): {old[:60]}...")
    text = text.replace(old, new)

# Also handle the H2 headline on page 04 (The Name reveal):
# "A platform of living well — for multigenerational families."
# was already covered by the direct tagline replacement above.

# Update PLATFORM OFFERINGS GRID CSS comment for consistency
text = text.replace("/* ───── PLATFORM OFFERINGS GRID ───── */",
                    "/* ───── CULTURE OFFERINGS GRID ───── */")

DECK.write_text(text)

# Verify
remaining_old_tagline = text.lower().count("platform of living well")
remaining_sara_platform = sum(
    1 for keyword in ["Step into the platform", "Live the platform", "residential expression of the platform"]
    if keyword in text
)
new_tagline_count = text.count("The Culture of Living Well")
print(f"\n=== HTML DECK ===")
print(f"  Old tagline 'platform of living well' remaining: {remaining_old_tagline}")
print(f"  New tagline 'The Culture of Living Well' instances: {new_tagline_count}")
print(f"  Stale SARA-context 'platform' references: {remaining_sara_platform}")

# ─── KEY INSIGHTS DOCX ──────────────────────────────────────────────────
import zipfile
import shutil
import tempfile

def update_docx(path, replacements):
    """Update text in a docx by editing document.xml directly."""
    path = Path(path)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "unpacked"
        tmp_path.mkdir()
        with zipfile.ZipFile(path, 'r') as z:
            z.extractall(tmp_path)
        doc_xml = tmp_path / "word" / "document.xml"
        xml_text = doc_xml.read_text(encoding='utf-8')
        original_len = len(xml_text)
        change_count = 0
        for old, new in replacements:
            if old in xml_text:
                count = xml_text.count(old)
                xml_text = xml_text.replace(old, new)
                change_count += count
        doc_xml.write_text(xml_text, encoding='utf-8')
        # Repack
        new_zip = path.with_suffix('.tmp.docx')
        with zipfile.ZipFile(new_zip, 'w', zipfile.ZIP_DEFLATED) as z:
            for f in tmp_path.rglob("*"):
                if f.is_file():
                    z.write(f, f.relative_to(tmp_path))
        shutil.move(new_zip, path)
        return change_count

# Note: smart quotes from docx (’ ‘ “ ”) — match what was actually written
docx_replacements = [
    # Tagline replacement (smart quotes from docx-js output)
    ("A platform of living well", "The Culture of Living Well"),
    ("a platform of living well", "the Culture of Living Well"),
    ("the platform of living well", "the Culture of Living Well"),
    ("The platform of living well", "The Culture of Living Well"),
    # SARA-context (these brand-claim usages should shift to culture)
    ("SARA is the platform of living well",
     "SARA is the Culture of Living Well"),
    # The category claim sentence in Key Insights
    ("SARA is the world&#8217;s first platform of living well",
     "SARA is the world&#8217;s first Culture of Living Well"),
    ("SARA is the world's first platform of living well",
     "SARA is the world's first Culture of Living Well"),
    # Vocabulary update wherever the list appears
    ("Method, Platform, Living well", "Method, Culture, Living well"),
]

INSIGHTS = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/sara-brand-research-key-insights.docx")
if INSIGHTS.exists():
    n = update_docx(INSIGHTS, docx_replacements)
    print(f"\n=== KEY INSIGHTS DOCX ===")
    print(f"  Replacements made: {n}")

BOOK = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/sara-brand-research-book.docx")
if BOOK.exists():
    n = update_docx(BOOK, docx_replacements)
    print(f"\n=== RESEARCH BOOK DOCX ===")
    print(f"  Replacements made: {n}")

print("\nDone.")
