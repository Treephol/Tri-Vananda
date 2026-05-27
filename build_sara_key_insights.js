// SARA Brand Research — Key Insights Summary
// 10 strategic patterns synthesised from 30-brand identity comparison
// Tier-S strategic document for SARA brand development

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel,
  LevelFormat, BorderStyle, PageBreak, Header, Footer, PageNumber,
  TabStopType, TabStopPosition, ShadingType
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

const para = (text, opts = {}) => new Paragraph({
  children: [new TextRun({ text, font: "Calibri", size: opts.size || 22, color: opts.color || INK, bold: opts.bold || false, italics: opts.italic || false })],
  spacing: { after: opts.after !== undefined ? opts.after : 160 },
  alignment: opts.align || AlignmentType.LEFT,
});

const bullet = (text) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  children: [new TextRun({ text, font: "Calibri", size: 22, color: INK })],
  spacing: { after: 100 },
});

const h1 = (number, text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [
    new TextRun({ text: number + "  ", font: "Calibri", size: 56, bold: true, color: GOLD }),
    new TextRun({ text: text, font: "Calibri", size: 36, bold: true, color: FOREST }),
  ],
  spacing: { before: 0, after: 80 },
});

const strapline = (text) => new Paragraph({
  children: [new TextRun({ text: text, font: "Calibri", size: 24, italics: true, color: MUTED })],
  spacing: { after: 360 },
  border: ruleBelow,
});

const sectionHeading = (text) => new Paragraph({
  children: [new TextRun({ text: text.toUpperCase(), font: "Calibri", size: 18, bold: true, color: GOLD })],
  spacing: { before: 280, after: 120 },
});

const body = (text) => new Paragraph({
  children: [new TextRun({ text, font: "Calibri", size: 22, color: INK })],
  spacing: { after: 200, line: 320 },
  alignment: AlignmentType.JUSTIFIED,
});

const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

// ─── PATTERNS ───────────────────────────────────────────────────────────
const PATTERNS = [
  {
    number: "01",
    title: "Name the Method",
    strapline: "Turn an experience into intellectual property.",
    pattern: "The most defensible wellness brands don’t sell treatments — they sell named, proprietary methodologies. A method is an asset: trademarkable, teachable, transferable, and quotable in editorial. A treatment is a commodity.",
    evidence: "The Tracy Anderson Method. The SHA Method®. The Lanserhof Concept. The 8-Day Hoffman Process. The Buchinger Fast. Tier X by Equinox. The Newt’s Cyder Method. Each one converts a discipline into a name people can refer their friends to.",
    sara: "SARA needs a named protocol that lives independently of any one property. The Method should be referenceable in conversation, teachable to new staff, exportable to a sister site one day, and ownable in trademark and editorial. Without a named method, SARA is competing on amenity rather than IP.",
    actions: [
      "Name SARA’s flagship multi-day programme (working title: The SARA Method · The SARA Reset · The SARA Arc).",
      "Codify the protocol in writing: phases, duration, daily structure, expected outcomes.",
      "Trademark the name and the protocol acronym before external use.",
      "Refer to it consistently in all editorial — capitalised, branded, never generic.",
    ],
  },
  {
    number: "02",
    title: "Own the Terroir",
    strapline: "Claim a specific place — never a vague region.",
    pattern: "The strongest wellness brands stake a claim on one piece of earth and refuse to abstract it. Noma is not “Scandinavian” — it is the rocks of the Danish coast. Castello di Reschio is not “Italian” — it is 3,700 acres of Umbrian valley. Babylonstoren is not “African” — it is 350 years of Franschhoek Cape Dutch farmland.",
    evidence: "Noma’s foraged kelp. Reschio’s estate olive oil. Babylonstoren’s walled garden. The Newt’s Somerset apples. Flamingo Estate’s 7 acres in Eagle Rock. Single Thread’s 24-acre Sonoma farm. Each brand owns a piece of land that its competitors cannot replicate.",
    sara: "SARA must claim Phuket, the Andaman, and Thai botanicals as proprietary — not generic “Asian wellness.” The Pru farm is the strategic asset most undervalued in current planning. The brand should sound like it could only exist here, with these plants, this water, this climate.",
    actions: [
      "Audit Pru farm produce — list every species growable in Phuket’s soil and climate.",
      "Commission a botanist or ethnobotanist to author SARA’s plant manifesto (Phuket-native, Thai-medicinal, Andaman-coastal).",
      "Replace generic copy (“Asian wellness,” “tropical luxury”) with terroir-specific language (“Andaman tides,” “Phuket monsoon,” named botanicals).",
      "Source 60-80% of consumables from the Pru farm or named regional partners within 3 years.",
    ],
  },
  {
    number: "03",
    title: "The Founder Must Be Visible",
    strapline: "One obsessive voice. Never a committee.",
    pattern: "Every Tier-S brand in this study has a visible single visionary. The brand reads as their personal taste — unmistakable, idiosyncratic, sometimes uncomfortable. Multi-author brands feel hotel-managed. Single-author brands feel curated.",
    evidence: "Karen Roos at Babylonstoren and The Newt. Count Antonio Bolza and his son Benedikt at Reschio. Sonu and Eva Shivdasani at Soneva. René Redzepi at Noma. Professor Augustinus Bader. Alain de Botton at The School of Life. Tracy Anderson. Dr Jonathan Leary at Remedy Place. Richard Christiansen at Flamingo Estate.",
    sara: "SARA cannot be designed by committee. The Montara leadership voice (Khun Anudej / family ownership) must be visible in the brand — in interviews, in editorial, in the manifesto. The lead practitioners and scientific partners (CLP doctors, wellness leads, chef) must also be surfaced as named, faced, quoted figures, not anonymous staff.",
    actions: [
      "Commission a founder profile (Robb Report / Tatler / WSJ Magazine) within 12 months of launch.",
      "Identify and brief 4-6 named brand voices: founder, medical lead, wellness director, executive chef, head of horticulture, head of architecture.",
      "Build a single-page “Makers of SARA” brand asset — faces, names, philosophies — for press and website.",
      "Refuse to publish anonymous brand copy. Every long-form piece is bylined by a real human inside the brand.",
    ],
  },
  {
    number: "04",
    title: "Curate the Room",
    strapline: "Membership is the brand. Members are the product.",
    pattern: "The members make the experience, not the building. Soho House is rich because its rooms are full of the right people. Annabel’s waitlist exists because no money buys admission. The Battery’s no-photography rule protects an interior climate worth more than the building. Members’ club logic outperforms resort logic because it monetises curation, not just space.",
    evidence: "Soho House (200,000 members, 8-year waitlists). Annabel’s (lifetime waitlist). The Battery SF (~3,000 members, committee admission). Heimat (capped at ~3,500). Remedy Place (founding tier $1,500/month). The Hoffman alumni network as referral engine.",
    sara: "SARA Membership must be capped, curated, and conferring. The wrong members will destroy the brand faster than the right architecture can save it. Membership should require sponsorship or interview, not just willingness to pay. The community of members is the most valuable asset SARA can build — worth more than the buildings.",
    actions: [
      "Cap inaugural SARA Membership at a defined number (recommended: ~500 founding members).",
      "Establish a Membership Committee — not just Montara executives, but external curators (designers, doctors, artists, family-office leaders).",
      "Define a sponsorship-or-interview admission gate. Money alone does not buy entry.",
      "Build a private member directory and — critically — publish nothing of it externally.",
    ],
  },
  {
    number: "05",
    title: "Programme the Calendar",
    strapline: "Members pay for what happens, not what is.",
    pattern: "A members’ club without programming is a hotel that doesn’t take walk-ins. The brands that turn members into evangelists run a year-round calendar of residencies, talks, salons, dinners, classes, and rituals. The calendar is the membership. The membership fee is the subscription to the calendar.",
    evidence: "The Battery SF runs 200+ events per year. Soho House calendars run weekly per house. Hoffman runs ~25 Process cohorts per year. Open delivers daily class drops live and on-demand. School of Life publishes a perpetual curriculum. Reschio runs olive harvest, truffle hunts, garden tours seasonally.",
    sara: "SARA Membership must include a published, perpetual calendar. Without programming, Membership is just a hotel discount. A live calendar transforms the property from a destination into a participation — something members return to monthly, not annually.",
    actions: [
      "Build a 52-week SARA Calendar with weekly anchor events (Sunday Long Table, Wednesday Sound Bath, etc.) and seasonal flagships (Pru Farm Festival, New Year Reset, monsoon retreat).",
      "Commission a programming director — distinct from F&B and operations — reporting to brand leadership.",
      "Allocate a programming budget per year, ring-fenced from operations.",
      "Publish the calendar quarterly in print and digitally — visible to members, glimpsed by non-members.",
    ],
  },
  {
    number: "06",
    title: "Demand the Commitment",
    strapline: "Length signals seriousness. Filter for the right guests.",
    pattern: "Tier-S wellness brands refuse to make their flagship experience short. Length is a filter — it filters out wellness tourists and filters in the actual transformation audience. Short stays attract people who want to take photos. Long stays attract people who want to be changed.",
    evidence: "Hoffman Institute requires 8 full days, no shorter version offered. Buchinger’s standard is 7-21 days. Lanserhof prefers 14-21 days. SHA recommends multi-week stays. The Ranch Malibu’s shortest programme is 4 days; the flagship is 7. CLP’s Revitalisation is a 7-day minimum.",
    sara: "SARA’s flagship retreat should require a 7-day minimum, ideally 10-14 days. The Open Experience can be shorter (weekends, half-week) to feed the funnel, but the headline programme must demand a real commitment. If SARA can be done in three days, it cannot make a 50-year-old’s life different.",
    actions: [
      "Set the flagship SARA programme at 7 days minimum, with 10-day and 14-day extended options.",
      "Communicate length as a feature, not a barrier. “This takes time. That is the point.”",
      "Build the Open Experience as a sampler (2-3 days) that converts into a full programme booking.",
      "Refuse to discount on shorter stays. Short stays are not the flagship product.",
    ],
  },
  {
    number: "07",
    title: "Extend Beyond the Stay",
    strapline: "The brand must travel home with the guest.",
    pattern: "The most valuable wellness brands generate revenue and brand awareness when guests are not there. They sell products, books, content, music, and member-only memorabilia. The hotel is the apex of the experience pyramid — but its base is everything the guest can carry home and put on their kitchen counter, bookshelf, or bathroom shelf.",
    evidence: "Aesop sells $25-150 products in 400+ stores. Augustinus Bader is a $1B+ skincare company built from one cream. Reschio sells wine, olive oil, perfume, furniture. Flamingo Estate is a property turned product line. Le Labo is a perfume house. Babylonstoren sells books, garden tools, beauty. Noma Projects sells fermented condiments. The School of Life sells books worldwide.",
    sara: "SARA must build a take-home product line within 24 months of launch. Pru honey, SARA tea, Tri Vananda balm, a SARA book of the method, a SARA sound bath album. Every product is a brand asset that lives in a guest’s home for years — quietly recruiting the next guest.",
    actions: [
      "Audit Pru farm output — identify 6-10 candidate products from existing harvest (honey, oils, teas, sauces, salts).",
      "Commission a brand book for the SARA Method — publishable, sellable, gift-able.",
      "Develop a SARA bath ritual product line (oils, salts, balms) for sale on property and at international retail partners.",
      "Build a digital extension: SARA app (meditations, recipes, breath, classes) as the year-round version of the property.",
    ],
  },
  {
    number: "08",
    title: "Atmosphere Beats Programming",
    strapline: "Sensory immersion is more memorable than feature lists.",
    pattern: "The most memorable wellness experiences are remembered as atmospheres, not itineraries. People do not remember which treatment they had — they remember the candlelight, the silence, the smell of cedar, the texture of the linen, the weight of the cup. Atmosphere is the product. Programming is the proof.",
    evidence: "AIRE Ancient Baths is darkness, candlelight, and time — not a treatment list. Bathhouse Brooklyn is concrete and warm light. Lanserhof’s buildings function as silent brand books. Annabel’s every surface adorned with intent. Aesop’s stores each architect-designed individually. Soneva’s sandy footprints. Reschio’s estate — no chrome, no plastic, no clock.",
    sara: "SARA’s spaces must be designed for atmosphere first and programming second. The villa entry sequence, the spa transition corridor, the breakfast room at 7 AM — these are the brand. The temperature, the light, the scent, the sound, the materials. The treatment menu can be world-class and the brand will still feel cheap if the atmosphere is generic.",
    actions: [
      "Brief the architect on sensory not functional: “This room should feel like X.” Define the scent, light, sound, and material profile of every guest space.",
      "Design a signature SARA scent (developed with a noted perfumer) used in all properties — a single olfactory signature.",
      "Commission a SARA sonic identity — a curated soundscape and music programme — for property, app, and brand film.",
      "Audit current Tri Vananda spaces against a sensory brief; identify three quick-wins for atmosphere correction.",
    ],
  },
  {
    number: "09",
    title: "Reframe the Category",
    strapline: "Don’t compete in the space. Invent the space.",
    pattern: "Tier-S brands win by reframing the category, not by being the best in an existing one. Remedy did not invent the ice bath — it invented the social context for the ice bath. Soho House did not invent the private club — it invented the creative-industry private club. Equinox reframed “gym” as “performance fashion.” Paws Up reframed camping as “glamping.” Noma reframed Scandinavian as “New Nordic.”",
    evidence: "The most enduring brands in this study each named a category they could own. Once named, the category becomes a brand-defined market — with the founding brand as the natural reference point. Categories are more defensible than products.",
    sara: "SARA’s strategic move is to reframe wellness itself — from “treatment” to “platform of living well.” From episodic intervention to continuous practice. From spa to community. The brief is to invent the SARA category, not to compete inside an existing one. The platform language already in development is the foundation; it needs strategic conviction to become a category claim.",
    actions: [
      "Commit to a category claim in the brand manifesto: “SARA is the world’s first platform of living well.” (or a sharper variant).",
      "Articulate what the category is NOT — not a resort, not a clinic, not a retreat, not a gym, not a club. Defining the negatives sharpens the positive.",
      "Use the category language consistently in all editorial, PR, and pitch. Repetition is what makes a category claim stick.",
      "Anchor the category in an industry moment — a Global Wellness Summit talk, a book, a manifesto film — within 18 months.",
    ],
  },
  {
    number: "10",
    title: "One Method, Many Doors",
    strapline: "A platform brand is a methodology that scales across owned places.",
    pattern: "The most valuable wellness brands are platforms, not single sites. They develop one proprietary method (see Pattern 01) and then deploy it across multiple owned properties — each location reinforcing the others, each new location compounding the brand’s authority and reach. One property is boutique. Three is a brand. Five is a platform.",
    evidence: "Lanserhof: Tegernsee, Sylt, Lans, London, Mallorca (under development). Vivamayr: 5 properties across Austria, London, Marbella. SHA: Spain, Mexico (→ Saudi planned). Soneva: 4 Maldives properties + Thailand + residences. Soho House: 40+ houses. Buchinger Wilhelmi: Marbella + Überlingen. Reschio: hotel + 50 farmhouses on one estate (a horizontal platform).",
    sara: "SARA must be designed as a platform from day one — not as a single Phuket project. Even if only one property exists for the first 5 years, the brand architecture, the method, the visual identity, the verbal identity, and the operating playbook should be built so that property 2 (Bangkok urban club? Chiang Mai retreat? Bali villa community?) can be launched without rebranding. The 10-year roadmap is 3-5 SARA properties.",
    actions: [
      "Develop a SARA 10-year property roadmap: confirmed (Phuket), pipeline (urban club · second resort · international flagship).",
      "Build the SARA Brand Book to platform standard — not site-specific. Verbal, visual, sonic, scent, service all transferable.",
      "Codify the SARA Method as transferable IP that could be deployed in any climate, any culture, any building type.",
      "Plan property 2 in narrative terms before site is selected: “When SARA opens its second door, it will look like X.”",
    ],
  },
];

// ─── DOCUMENT BUILD ─────────────────────────────────────────────────────
const children = [];

// ── COVER PAGE
children.push(
  new Paragraph({ children: [new TextRun("")], spacing: { before: 2400 } }),
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
    children: [new TextRun({ text: "Key Insights from the 30-Brand Identity Study", font: "Calibri", size: 32, color: INK })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 120 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "Ten strategic patterns for the building of a world-class wellness platform brand", font: "Calibri", size: 22, italics: true, color: MUTED })],
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

// ── INTRODUCTION
children.push(
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "Introduction", font: "Calibri", size: 40, bold: true, color: FOREST })],
    spacing: { after: 80 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "What thirty brands taught us about building one.", font: "Calibri", size: 24, italics: true, color: MUTED })],
    spacing: { after: 360 },
    border: ruleBelow,
  }),
  body("This document synthesises ten strategic patterns drawn from a study of thirty world-class brands across the wellness, hospitality, beauty, culture, and farm-real-estate categories. Each brand was selected not for its size but for its identity — the precision of its visual world, the conviction of its narrative, and the defensibility of its position."),
  body("The patterns that follow are not platitudes. They are the structural choices that made these brands inimitable. Some of them were already implicit in the SARA brief; others sharpen what has been developing; a few will require conviction to adopt."),
  body("This is the strategic intelligence layer beneath the comparison table. Read it once before reviewing the table, and again before any creative-direction conversation. The pattern names should become shorthand in the room — “that’s a Pattern 04 problem,” “we haven’t solved Pattern 07 yet” — so that a complex brand-building project has a shared vocabulary."),
  sectionHeading("The Ten Patterns"),
);

// TOC
PATTERNS.forEach(p => {
  children.push(
    new Paragraph({
      children: [
        new TextRun({ text: p.number + "  ", font: "Calibri", size: 22, bold: true, color: GOLD }),
        new TextRun({ text: p.title, font: "Calibri", size: 22, bold: true, color: FOREST }),
        new TextRun({ text: "  ·  " + p.strapline, font: "Calibri", size: 22, italics: true, color: MUTED }),
      ],
      spacing: { after: 100 },
    })
  );
});

children.push(pageBreak());

// ── PATTERN PAGES
PATTERNS.forEach((p, i) => {
  children.push(
    h1(p.number, p.title),
    strapline(p.strapline),
    sectionHeading("The Pattern"),
    body(p.pattern),
    sectionHeading("The Evidence"),
    body(p.evidence),
    sectionHeading("What it Means for SARA"),
    body(p.sara),
    sectionHeading("The Action"),
  );
  p.actions.forEach(a => children.push(bullet(a)));
  if (i < PATTERNS.length - 1) children.push(pageBreak());
});

// ── CLOSING BRIEF
children.push(
  pageBreak(),
  new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: "A Ten-Point Brief", font: "Calibri", size: 40, bold: true, color: FOREST })],
    spacing: { after: 80 },
  }),
  new Paragraph({
    children: [new TextRun({ text: "If the brand team did only these ten things in the next 18 months — SARA would be Tier-S.", font: "Calibri", size: 24, italics: true, color: MUTED })],
    spacing: { after: 360 },
    border: ruleBelow,
  }),
);

const finalBrief = [
  "Name and trademark the SARA Method within 90 days.",
  "Commission the Phuket-and-Andaman botanical manifesto from a named ethnobotanist within 6 months.",
  "Surface four founder voices in editorial: ownership, medical, wellness, culinary. Photograph and profile them.",
  "Cap SARA Membership at ~500 founding members. Establish a Membership Committee external to operations.",
  "Build the SARA 52-week Calendar. Hire a Programming Director reporting to brand leadership.",
  "Set the flagship retreat at 7-day minimum. Refuse to shorten. Communicate length as a feature.",
  "Develop six take-home products within 24 months: SARA Tea, Pru Honey, SARA Balm, the SARA Method Book, a sound album, and a signature scent.",
  "Brief the architect on atmosphere first — define the scent, light, sound, and material profile of every guest space.",
  "Adopt the category claim in the manifesto: “SARA is the platform of living well.” Use it everywhere.",
  "Build the SARA Brand Book to platform standard. Plan property 2 in narrative terms before site selection.",
];

finalBrief.forEach((item, idx) => {
  children.push(new Paragraph({
    children: [
      new TextRun({ text: String(idx + 1).padStart(2, "0") + "  ", font: "Calibri", size: 26, bold: true, color: GOLD }),
      new TextRun({ text: item, font: "Calibri", size: 22, color: INK }),
    ],
    spacing: { after: 200 },
    indent: { left: 0, hanging: 0 },
  }));
});

children.push(
  new Paragraph({
    children: [new TextRun({ text: "", font: "Calibri", size: 22 })],
    spacing: { before: 600, after: 0 },
    border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 6 } }
  }),
  new Paragraph({
    children: [new TextRun({ text: "End of document.", font: "Calibri", size: 18, italics: true, color: MUTED })],
    alignment: AlignmentType.CENTER,
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
        run: { size: 36, bold: true, font: "Calibri", color: FOREST },
        paragraph: { spacing: { before: 0, after: 200 }, outlineLevel: 0 },
      },
    ],
  },
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 540, hanging: 270 } } }
        }]
      }
    ]
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
            new TextRun({ text: "\tKey Insights from the 30-Brand Identity Study", font: "Calibri", size: 16, color: MUTED }),
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
  const out = "/sessions/cool-optimistic-lovelace/mnt/Tri-Vananda/sara-brand-research-key-insights.docx";
  fs.writeFileSync(out, buffer);
  console.log("Saved: " + out);
  console.log("Patterns: " + PATTERNS.length);
});
