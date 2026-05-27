// SARA Brand Research — Research Book Build
// 30 brand profiles, 6 sections each

const fs = require("fs");
const PROFILES = require("./sara_research_book_data.js");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel,
  LevelFormat, BorderStyle, PageBreak, Header, Footer, PageNumber,
  TabStopType, TabStopPosition
} = require("docx");

// ─── PALETTE ────────────────────────────────────────────────────────────
const FOREST = "1F3A2E";
const GOLD   = "B89968";
const INK    = "1A1A1A";
const MUTED  = "5A5A5A";
const RULE   = "D6CFC2";

// ─── HELPERS ────────────────────────────────────────────────────────────
const ruleBelow = {
  bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 6 }
};

const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

const body = (text) => new Paragraph({
  children: [new TextRun({ text, font: "Calibri", size: 22, color: INK })],
  spacing: { after: 180, line: 320 },
  alignment: AlignmentType.JUSTIFIED,
});

const sectionLabel = (text) => new Paragraph({
  children: [new TextRun({ text: text.toUpperCase(), font: "Calibri", size: 16, bold: true, color: GOLD, characterSpacing: 30 })],
  spacing: { before: 260, after: 100 },
});

const blank = (size = 22, after = 200) => new Paragraph({
  children: [new TextRun({ text: "", font: "Calibri", size })],
  spacing: { after }
});

// ─── BUILD ──────────────────────────────────────────────────────────────
const children = [];

// COVER PAGE
children.push(
  blank(22, 2400),
  new Paragraph({
    children: [new TextRun({ text: "SARA", font: "Calibri", size: 96, bold: true, color: FOREST })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "—", font: "Calibri", size: 36, color: GOLD })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Research Book", font: "Calibri", size: 36, color: INK })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 120 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Thirty world-class brand profiles for SARA brand development", font: "Calibri", size: 24, italics: true, color: MUTED })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 2800 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Tri Vananda  ·  Montara Hospitality Group", font: "Calibri", size: 20, color: MUTED })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 120 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Internal Document  ·  v1.0  ·  May 2026", font: "Calibri", size: 18, color: MUTED })],
    alignment: AlignmentType.CENTER,
  }),
  pageBreak(),
);

// INTRODUCTION + HOW TO READ
children.push(
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "How to Read This Book", font: "Calibri", size: 40, bold: true, color: FOREST })],
    spacing: { after: 80 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "A field guide to the brands that built the category SARA is entering.", font: "Calibri", size: 24, italics: true, color: MUTED })],
    spacing: { after: 360 },
    border: ruleBelow,
  }),
  body("This book is the third deliverable in the SARA brand research series. The first was a single-page comparison table mapping all thirty brands across nine strategic dimensions. The second was a Key Insights document synthesising the ten strategic patterns drawn from the table. This third deliverable is the long-form research underneath both — a brand-by-brand profile of every one of the thirty references."),
  body("Each profile follows the same six-section structure: Essence (the brand’s irreducible idea), Visual Identity (the design markers), Narrative (the story the brand tells), Audience & Pricing (who buys, what it costs, how access works), Why It Works (the strategic mechanism, the moat), and Lessons for SARA (the actionable takeaways)."),
  body("Read selectively. This is a reference book, not a manuscript. When the team is briefing the architect, read the Visual Identity sections of Lanserhof, Aesop, AIRE, and The Newt. When briefing the membership model, read Soho House, Heimat, The Battery, and Hoffman. When briefing product development, read Flamingo Estate, Reschio, Babylonstoren, and Le Labo. The Lessons for SARA section at the end of each profile is the bridge between observation and action."),
  body("The thirty brands were chosen for the precision of their identity, not the size of their business. Some are global ($1B+ valuations); others operate at single sites. All thirty have done something distinctive — they have made a creative, strategic, or operational choice that competitors cannot easily replicate. That distinctiveness is what we are studying."),
  body("Quality note: this is a strategic document, not an audit. The price points, locations, and founder details are accurate to the best of available knowledge as of May 2026, and have been triangulated across multiple editorial sources. Specific numbers (membership counts, valuation rounds, recent openings) may have moved since publication; the strategic principles are the durable layer."),
  sectionLabel("The Ten Categories"),
);

// TOC by category
const categories = [];
PROFILES.forEach(p => {
  if (!categories.find(c => c.name === p.category)) {
    categories.push({ name: p.category, brands: [] });
  }
  categories.find(c => c.name === p.category).brands.push(p.brand);
});

categories.forEach((cat, idx) => {
  children.push(
    new Paragraph({
      children: [
        new TextRun({ text: String(idx + 1).padStart(2, "0") + "  ", font: "Calibri", size: 22, bold: true, color: GOLD }),
        new TextRun({ text: cat.name, font: "Calibri", size: 22, bold: true, color: FOREST }),
        new TextRun({ text: "  ·  " + cat.brands.join("  ·  "), font: "Calibri", size: 20, color: MUTED }),
      ],
      spacing: { after: 100 },
    })
  );
});

children.push(pageBreak());

// PROFILES BY CATEGORY
let lastCategory = "";
PROFILES.forEach((p, i) => {
  // CATEGORY DIVIDER PAGE
  if (p.category !== lastCategory) {
    if (lastCategory !== "") {
      // already on a new page from previous brand's break
    }
    children.push(
      blank(22, 3200),
      new Paragraph({
        children: [new TextRun({ text: "PART " + String(categories.findIndex(c => c.name === p.category) + 1).padStart(2, "0"), font: "Calibri", size: 20, bold: true, color: GOLD, characterSpacing: 60 })],
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
      }),
      new Paragraph({
        children: [new TextRun({ text: p.category, font: "Calibri", size: 56, bold: true, color: FOREST })],
        alignment: AlignmentType.CENTER,
        spacing: { after: 280 },
      }),
      new Paragraph({
        children: [new TextRun({ text: "Three brands.", font: "Calibri", size: 24, italics: true, color: MUTED })],
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
      }),
      new Paragraph({
        children: [new TextRun({ text: categories.find(c => c.name === p.category).brands.join("  ·  "), font: "Calibri", size: 22, color: INK })],
        alignment: AlignmentType.CENTER,
      }),
      pageBreak(),
    );
    lastCategory = p.category;
  }

  // BRAND PROFILE PAGE
  children.push(
    new Paragraph({
      children: [new TextRun({ text: p.category.toUpperCase(), font: "Calibri", size: 16, bold: true, color: GOLD, characterSpacing: 60 })],
      spacing: { after: 60 },
    }),
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      children: [new TextRun({ text: p.brand, font: "Calibri", size: 44, bold: true, color: FOREST })],
      spacing: { after: 80 },
    }),
    new Paragraph({
      children: [new TextRun({ text: p.strapline, font: "Calibri", size: 24, italics: true, color: MUTED })],
      spacing: { after: 60 },
    }),
    new Paragraph({
      children: [new TextRun({ text: p.location, font: "Calibri", size: 18, color: MUTED })],
      spacing: { after: 280 },
      border: ruleBelow,
    }),
    sectionLabel("Essence"),
    body(p.essence),
    sectionLabel("Visual Identity"),
    body(p.visual),
    sectionLabel("Narrative"),
    body(p.narrative),
    sectionLabel("Audience & Pricing"),
    body(p.audience),
    sectionLabel("Why It Works"),
    body(p.why),
    sectionLabel("Lessons for SARA"),
    body(p.lessons),
  );

  if (i < PROFILES.length - 1) {
    children.push(pageBreak());
  }
});

// CLOSING
children.push(
  pageBreak(),
  blank(22, 1200),
  new Paragraph({
    children: [new TextRun({ text: "—", font: "Calibri", size: 36, color: GOLD })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 280 },
  }),
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "A Final Note", font: "Calibri", size: 36, bold: true, color: FOREST })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 280 },
  }),
  body("These thirty brands are not templates. They are evidence. They demonstrate that the strategic decisions which make a brand inimitable — naming the method, owning the terroir, making the founder visible, curating the room, programming the calendar, demanding the commitment, extending beyond the stay, designing for atmosphere first, reframing the category, building for the platform — are decisions that have been made, in different ways, by every great brand in this study."),
  body("SARA does not need to imitate any of them. SARA needs to make its own decisions with the same conviction. The patterns are universal; the expressions are individual. The work ahead is to make SARA’s expression of these patterns unmistakably SARA — and unmistakably better than the brands that taught us how."),
  blank(22, 600),
  new Paragraph({
    children: [new TextRun({ text: "End of research book.", font: "Calibri", size: 18, italics: true, color: MUTED })],
    alignment: AlignmentType.CENTER,
    border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 12 } },
    spacing: { before: 200 },
  }),
);

// ─── DOCUMENT ───────────────────────────────────────────────────────────
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Calibri", size: 22, color: INK } } },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 44, bold: true, font: "Calibri", color: FOREST },
        paragraph: { spacing: { before: 0, after: 200 }, outlineLevel: 0 },
      },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          children: [
            new TextRun({ text: "SARA", font: "Calibri", size: 18, bold: true, color: FOREST }),
            new TextRun({ text: "\tResearch Book — Thirty Brand Profiles", font: "Calibri", size: 16, color: MUTED }),
          ],
          tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          children: [
            new TextRun({ text: "Tri Vananda  ·  Montara Hospitality Group  ·  Internal", font: "Calibri", size: 16, color: MUTED }),
            new TextRun({ text: "\t", font: "Calibri", size: 16 }),
            new TextRun({ children: [PageNumber.CURRENT], font: "Calibri", size: 16, color: MUTED }),
          ],
          tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
        })]
      })
    },
    children: children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  const out = "/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/sara-brand-research-book.docx";
  fs.writeFileSync(out, buffer);
  console.log("Saved: " + out);
  console.log("Profiles: " + PROFILES.length);
  console.log("Categories: " + categories.length);
});
