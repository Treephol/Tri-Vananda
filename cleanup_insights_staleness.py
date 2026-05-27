"""
Clean up two stale 'platform' phrasings in Key Insights that reference the
old category-claim framing (not the business-architecture sense).
"""
from pathlib import Path
import zipfile, shutil, tempfile

def update_docx(path, replacements):
    path = Path(path)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "unpacked"
        tmp_path.mkdir()
        with zipfile.ZipFile(path, 'r') as z:
            z.extractall(tmp_path)
        doc_xml = tmp_path / "word" / "document.xml"
        xml_text = doc_xml.read_text(encoding='utf-8')
        change_count = 0
        for old, new in replacements:
            if old in xml_text:
                count = xml_text.count(old)
                xml_text = xml_text.replace(old, new)
                change_count += count
            else:
                print(f"  Not found: {old[:60]}")
        doc_xml.write_text(xml_text, encoding='utf-8')
        new_zip = path.with_suffix('.tmp.docx')
        with zipfile.ZipFile(new_zip, 'w', zipfile.ZIP_DEFLATED) as z:
            for f in tmp_path.rglob("*"):
                if f.is_file():
                    z.write(f, f.relative_to(tmp_path))
        shutil.move(new_zip, path)
        return change_count

# Key Insights: subtitle + Pattern 09 SARA sentence
INSIGHTS = "/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/sara-brand-research-key-insights.docx"
n = update_docx(INSIGHTS, [
    # Cover subtitle: "world-class wellness platform brand" → "world-class wellness brand"
    ("Ten strategic patterns for the building of a world-class wellness platform brand",
     "Ten strategic patterns for the building of a world-class wellness brand"),
    # Pattern 09 SARA section: "The platform language already in development is the foundation"
    ("The platform language already in development is the foundation",
     "The Culture language already in development is the foundation"),
])
print(f"Key Insights: {n} replacement(s)")
