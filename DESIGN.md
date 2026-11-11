# Personal academic website

Audience: researchers, potential collaborators, and readers. Priorities: introduce the research, distinguish publication statuses, and provide the real CV.

Palette: paper #FFFFFF, ink #142F3E, secondary text #50636E, link blue #22627C, ice #EDF4F7, divider #DCE5EA. Aptos / Segoe UI for identity and headings; Charter / Georgia for prose. Local font fallbacks, 1080px content width, left alignment, readable 58-68-character lines.

```text
Name                       Research  Publications  Experience  Contact
Aolong Xu                                    [existing cat avatar]
Role, institution, research, biography        Ghent, Belgium
[Download CV] [Email]
Research        Two research questions and methods
Publications    Published / in press, then work in progress
Experience      Education, professional work, teaching
Contact         Public email and labelled profile links
```

Review: the actual cat avatar replaces the unrelated landscape and informs the blue accent. Research themes are unnumbered because they are not sequential steps. Whitespace establishes hierarchy; no repeated decorative cards or automatic motion. A single-column mobile layout preserves reading order. All pages share local navigation, footer, and AX favicon. Upstream license notices remain in LICENSE.md.

The CV is rebuilt by scripts/build_cv.py from the author profile and the publications and references in the supplied Aolong_Xu_CV_Postdoc.pdf. The original source PDF is preserved. The updated two-page download includes the newly supplied Meituan experience, expected completion month, and personal interests.

Homepage detail is intentionally reduced: one biography paragraph, concise research summaries, compact experience, and expandable ongoing manuscripts. Full profile and experience pages retain the detail. Three selected user photographs appear under Outside research, after the complete academic sequence. A dedicated Photography page shows six photographs. Original frames are preserved and Hugo generates responsive JPEGs.

Update: Outside research now sits at the end of the homepage, after Contact, as two sentences with links to the Photography and LEGO pages. Photographs and LEGO builds no longer appear on the homepage. Browser icons are generated from the cat avatar, with the AX SVG kept as the scalable icon.
