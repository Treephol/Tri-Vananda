"""
Second pass: catch the docx tagline references that the first script missed
due to smart-quote and case-sensitivity issues.
"""

from pathlib import Path
import zipfile, shutil, tempfile, re

def update_docx(path, fn_xml_transform):
    """Apply a transform function to the document.xml of a docx."""
    path = Path(path)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "unpacked"
        tmp_path.mkdir()
        with zipfile.ZipFile(path, 'r') as z:
            z.extractall(tmp_path)
        doc_xml = tmp_path / "word" / "document.xml"
        xml_text = doc_xml.read_text(encoding='utf-8')
        new_xml, changes = fn_xml_transform(xml_text)
        doc_xml.write_text(new_xml, encoding='utf-8')
        new_zip = path.with_suffix('.tmp.docx')
        with zipfile.ZipFile(new_zip, 'w', zipfile.ZIP_DEFLATED) as z:
            for f in tmp_path.rglob("*"):
                if f.is_file():
                    z.write(f, f.relative_to(tmp_path))
        shutil.move(new_zip, path)
        return changes


def transform(xml_text):
    changes = 0
    # Use case-insensitive regex to catch "platform of living well" / "Platform of Living Well" / etc.
    # Replace with "The Culture of Living Well" (title case as user specified)
    # But preserve surrounding quotes if present.

    # Pattern 1: "platform of living well" (any case) → "Culture of Living Well"
    # Preserve the article preceding ("A", "a", "the", "The") and translate
    pattern = re.compile(r'\b(a|the|A|The)\s+platform\s+of\s+living\s+well\b', re.IGNORECASE)
    def repl(m):
        nonlocal changes
        article = m.group(1)
        # If the article was lowercase 'a' or 'the', use lowercase 'the'
        # If uppercase 'A' or 'The', use uppercase 'The'
        if article[0].isupper():
            return "The Culture of Living Well"
        else:
            return "the Culture of Living Well"
    new_xml, n1 = pattern.subn(repl, xml_text)
    changes += n1
    # Pattern 2: bare "platform of living well" (no article preceding)
    pattern2 = re.compile(r'\bplatform\s+of\s+living\s+well\b', re.IGNORECASE)
    new_xml, n2 = pattern2.subn("Culture of Living Well", new_xml)
    changes += n2
    return new_xml, changes


for name in ["sara-brand-research-key-insights.docx", "sara-brand-research-book.docx"]:
    path = Path("/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda") / name
    if path.exists():
        n = update_docx(path, transform)
        print(f"{name}: {n} replacement(s)")
