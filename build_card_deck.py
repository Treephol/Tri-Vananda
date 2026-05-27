"""
Rebuild PASSION deck image mapping using only SAFE images
(no human faces, no overlay text).

Overwrites the existing 52 files in card-deck-images/ in place
(keeps each file's existing filename + extension; replaces bytes).
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

ROOT = Path("/sessions/upbeat-affectionate-goodall/mnt/Tri-Vananda")
OUT = ROOT / "card-deck-images"
IB = ROOT / "image-bank"
IMG = ROOT / "images"

# ============================================================
# 52-card mapping: (suit, rank, headline, source_file, rationale)
# Sources confirmed SAFE — no human faces, no overlay text.
# ============================================================

PASSION_MAP = [
    # ============ HEARTS — COURAGE ============
    ("hearts", "A",  "vulnerability",
     IB/"_DSC9828.jpg",
     "Cupped hands holding water — the open-palm gesture of vulnerability."),
    ("hearts", "2",  "speaking-up",
     IB/"SHIN_040324_Trisara_004099.jpg",
     "A single ripple breaking the water surface — one voice into stillness."),
    ("hearts", "3",  "first-step",
     IB/"TVND-PFRM-SHIN-15.jpg",
     "Fresh grass blades — first sprouts pushing through, the first step."),
    ("hearts", "4",  "facing-fear",
     IB/"IMGL0602.jpg",
     "Dusk pond into dark treeline — walking toward what cannot yet be seen."),
    ("hearts", "5",  "saying-no",
     IB/"TVND-PFRM-SHIN-16-2.jpg",
     "A clean band of lily pads across open water — one decisive line."),
    ("hearts", "6",  "asking-for-help",
     IB/"IMGL1879.jpg",
     "Two hands together cradling a cacao pod — the gesture of receiving help."),
    ("hearts", "7",  "facing-shame",
     IMG/"offerings-02.jpg",
     "Temple silhouette against burning sun — stepping into the shadow."),
    ("hearts", "8",  "standing-alone",
     IB/"TVND-PFRM-SHIN-30.jpg",
     "A single dragonfly alone on a slender stem — standing upright."),
    ("hearts", "9",  "choosing-hope",
     IB/"IMG_7888.jpg",
     "Hand reaching toward a red ginger flower — a small flame held in hope."),
    ("hearts", "10", "embracing-discomfort",
     IMG/"farm-and-forest-03.png",
     "Architectural opening descending toward water — entering the unknown."),
    ("hearts", "J",  "defending-others",
     IMG/"trisara-01.jpg",
     "Aerial of the resort sheltering the coastline — a guardian's posture."),
    ("hearts", "Q",  "leading-without-certainty",
     IB/"DJI_0699.jpg",
     "Aerial farmland with branching paths — leading across uncertain terrain."),
    ("hearts", "K",  "accepting-mortality",
     IB/"Trisara_Highlight-20.jpg",
     "Sun setting behind a distant island — light draining at the end."),

    # ============ DIAMONDS — CURIOSITY ============
    ("diamonds", "A",  "wonder",
     IB/"SHIN_040324_Trisara_004099.jpg",
     "Split-level shot of water and fish — eye opening onto another world."),
    ("diamonds", "2",  "asking-why",
     IB/"SHIN_040324_Trisara_004610.jpg",
     "A clownfish circling in an anemone — the curiosity of the small."),
    ("diamonds", "3",  "noticing",
     IMG/"narrative-02.jpg",
     "A flower in extreme close-up — what only the patient eye sees."),
    ("diamonds", "4",  "perspective-taking",
     IMG/"offerings-04.jpg",
     "Overhead view of hands and tea across a table — two perspectives meeting."),
    ("diamonds", "5",  "appetite-for-the-new",
     IB/"IMG_2473.jpg",
     "A river winding into the mountains — the path that promises a destination."),
    ("diamonds", "6",  "sitting-with-uncertainty",
     IB/"Trisara by Johannes 6186.jpg",
     "A hammock strung between two posts at dusk — held in the space between."),
    ("diamonds", "7",  "following-a-thread",
     IB/"Hideaway-014.jpg",
     "Ducks following each other in a single line on a still lake."),
    ("diamonds", "8",  "cross-domain-thinking",
     IB/"TVND-PFRM-SHIN-16-2.jpg",
     "Overlapping lily pads forming a natural Venn — disciplines intersecting."),
    ("diamonds", "9",  "embracing-complexity",
     IB/"Dahla01.jpg",
     "A torch-ginger bloom — petal upon petal in fractal layers."),
    ("diamonds", "10", "unlearning",
     IMG/"farm-and-forest-01.png",
     "Illustrated masterplan — old land redrawn into something new."),
    ("diamonds", "J",  "synthesizing",
     IB/"Gym - Nature -bird-260.jpg",
     "A small bird against open green — many movements held in one form."),
    ("diamonds", "Q",  "imagining-alternatives",
     IMG/"farm-and-forest-04.png",
     "A pavilion opening onto a mountain horizon — a doorway to elsewhere."),
    ("diamonds", "K",  "loving-the-question",
     IB/"Trisara by Johannes 0089.jpg",
     "Aerial of an open coastline — a question still vast and undivided."),

    # ============ CLUBS — DEDICATION ============
    ("clubs", "A",  "commitment",
     IB/"IMGL1879.jpg",
     "Hands locked on a cacao pod — the moment a choice becomes a hold."),
    ("clubs", "2",  "consistency",
     IB/"Hideaway-014.jpg",
     "Ducks in a near-identical line — the same step, taken again."),
    ("clubs", "3",  "delayed-gratification",
     IB/"gardening-226.jpg",
     "Garden vegetables ready to lift — the seed's long answer."),
    ("clubs", "4",  "practice",
     IMG/"farm-and-forest-02.png",
     "An empty tennis court — the worn ground where mastery is rehearsed."),
    ("clubs", "5",  "focus",
     IB/"TVND-PFRM-SHIN-30.jpg",
     "A dragonfly held perfectly still on a single stem — attention concentrated."),
    ("clubs", "6",  "keeping-private-promises",
     IB/"_DSC9828.jpg",
     "Water held in cupped hands — a quiet promise that nobody sees."),
    ("clubs", "7",  "patience",
     IB/"Trisara by Johannes 0089.jpg",
     "An aerial of grown coconut palms — decades, made visible."),
    ("clubs", "8",  "sacrifice",
     IB/"gardening-226.jpg",
     "The harvest pulled from the soil — what was given up for it to ripen."),
    ("clubs", "9",  "mastery-seeking",
     IB/"IMG_2473.jpg",
     "A river climbing toward distant peaks — the slow line toward a summit."),
    ("clubs", "10", "long-term-thinking",
     IB/"DJI_0699.jpg",
     "Aerial farmland — fields drawn for the next generation, not next month."),
    ("clubs", "J",  "mentorship",
     IB/"IMGL1879.jpg",
     "One hand steadies, the other reaches — the gesture of passing down."),
    ("clubs", "Q",  "adapting-without-quitting",
     IB/"IMG_2473.jpg",
     "A river bending around terrain — never breaking course, only shape."),
    ("clubs", "K",  "legacy",
     IB/"Trisara_Highlight-20.jpg",
     "A solitary island catching the last light — what remains after the day."),

    # ============ SPADES — RESISTANCE ============
    ("spades", "A",  "inertia",
     IB/"TVND-PFRM-SHIN-15.jpg",
     "Dense grass — quiet, settled, hard to begin moving through."),
    ("spades", "2",  "fear-of-judgment",
     IB/"Hideaway-014.jpg",
     "A duck on still water under a watched sky — the gaze that freezes."),
    ("spades", "3",  "perfectionism",
     IB/"Dahla.jpg",
     "A flower endlessly refined by nature — perfection's slow trap."),
    ("spades", "4",  "comparison",
     IB/"Dahla01.jpg",
     "One ginger bloom set apart from the green around it — the unequal mirror."),
    ("spades", "5",  "avoidance",
     IMG/"offerings-02.jpg",
     "A temple bypassed in silhouette — the door not entered."),
    ("spades", "6",  "cynicism",
     IB/"IMGL0602.jpg",
     "A pond at dusk under a heavy sky — the world dimmed by doubt."),
    ("spades", "7",  "comfort-addiction",
     IB/"Trisara by Johannes 6186.jpg",
     "A hammock that asks nothing of you — the soft cage of ease."),
    ("spades", "8",  "scarcity-thinking",
     IB/"Gym - Nature -bird-295.jpg",
     "A single ripe tomato on the vine — the mind that still sees only one."),
    ("spades", "9",  "learned-helplessness",
     IB/"SHIN_040324_Trisara_004610.jpg",
     "A clownfish that won't leave its anemone — safe, and stuck."),
    ("spades", "10", "conformity",
     IB/"TVND-PFRM-SHIN-16-2.jpg",
     "Lily pads laid out in a uniform field — every shape the same."),
    ("spades", "J",  "busyness",
     IB/"Gym - Nature -bird-260.jpg",
     "A bird mid-motion in foliage — movement that may not be progress."),
    ("spades", "Q",  "fixed-identity",
     IMG/"narrative-02.jpg",
     "A bloom frozen at its peak — beauty that refuses to change."),
    ("spades", "K",  "resistance-to-resistance",
     IMG/"farm-and-forest-04.png",
     "A structure built directly into the hillside — meeting force with form."),
]

SUIT_FOLDER = {
    "hearts":   "01_hearts_courage",
    "diamonds": "02_diamonds_curiosity",
    "clubs":    "03_clubs_dedication",
    "spades":   "04_spades_resistance",
}

SUIT_TITLE = {
    "hearts":   "HEARTS — COURAGE",
    "diamonds": "DIAMONDS — CURIOSITY",
    "clubs":    "CLUBS — DEDICATION",
    "spades":   "SPADES — RESISTANCE",
}

# Build map: (suit, rank, headline) -> existing destination file path
existing = defaultdict(dict)
for sf in SUIT_FOLDER.values():
    folder = OUT / sf
    for f in folder.glob("*"):
        if f.name == "_MANIFEST.txt":
            continue
        # filename pattern: NN_R_headline.ext  e.g. 01_A_vulnerability.jpg
        stem = f.stem
        parts = stem.split("_", 2)
        if len(parts) >= 3:
            rank = parts[1]
            headline = parts[2]
            existing[sf][(rank, headline)] = f

# Process each card: overwrite existing file
by_suit = defaultdict(list)
for entry in PASSION_MAP:
    by_suit[entry[0]].append(entry)

RANK_TO_SORT = {"A": "01", "2": "02", "3": "03", "4": "04", "5": "05",
                "6": "06", "7": "07", "8": "08", "9": "09", "10": "10",
                "J": "11", "Q": "12", "K": "13"}

missing_src = []
copied = 0
created = 0
for (suit, rank, headline, src, rationale) in PASSION_MAP:
    folder_name = SUIT_FOLDER[suit]
    key = (rank, headline)
    dest = existing[folder_name].get(key)
    if not src.exists():
        missing_src.append(str(src))
        continue
    if dest is None:
        # Create a new file
        sort_n = RANK_TO_SORT[rank]
        ext = src.suffix.lower()
        new_name = f"{sort_n}_{rank}_{headline}{ext}"
        dest = OUT / folder_name / new_name
        existing[folder_name][key] = dest
        created += 1
    shutil.copy2(src, dest)
    copied += 1

print(f"Copied: {copied} / 52  (newly created: {created})")
if missing_src:
    print("MISSING SOURCE FILES:")
    for m in missing_src:
        print(f"  {m}")

# Rebuild manifests
for suit, entries in by_suit.items():
    folder = OUT / SUIT_FOLDER[suit]
    lines = [
        SUIT_TITLE[suit],
        "=" * 60,
        "",
        "All images selected to contain NO HUMAN FACES and NO OVERLAY TEXT.",
        "Some images repeat across cards because the safe-image pool is limited.",
        "",
    ]
    for (s, rank, headline, src, rationale) in entries:
        dest = existing[SUIT_FOLDER[suit]].get((rank, headline))
        fname = dest.name if dest else "(missing)"
        lines.append(f"  {rank:>2}  {headline.replace('-', ' ').title()}")
        lines.append(f"      File: {fname}")
        lines.append(f"      Why : {rationale}")
        lines.append("")
    (folder / "_MANIFEST.txt").write_text("\n".join(lines), encoding="utf-8")

# Top-level README
readme = [
    "PASSION DECK — IMAGE LIBRARY",
    "=" * 60,
    "",
    "52 cards across 4 suits. Filenames keep the original",
    "naming pattern: NN_R_headline.ext",
    "  NN = sort index 01..13",
    "  R  = card rank (A, 2..10, J, Q, K)",
    "",
    "Open _MANIFEST.txt inside each suit folder to see the",
    "rationale behind every image choice.",
    "",
    "Filter applied:",
    "  - No human faces",
    "  - No overlay text",
    "",
    "Some images are reused across cards because the safe-image",
    "pool is bounded by these constraints.",
    "",
    "Folders:",
    "  01_hearts_courage      - Hearts (Courage)",
    "  02_diamonds_curiosity  - Diamonds (Curiosity)",
    "  03_clubs_dedication    - Clubs (Dedication)",
    "  04_spades_resistance   - Spades (Resistance)",
]
(OUT / "README.txt").write_text("\n".join(readme), encoding="utf-8")

print("DONE.")
