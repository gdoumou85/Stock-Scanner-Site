# Article Style Guide

## Background Colors (Consistent Across All Articles)

All articles use the following background color system:

- **Article wrapper:** `--bg-primary` (white #ffffff)
- **Article header:** `--bg-primary` (white #ffffff)  
- **Article content:** `--bg-primary` (white #ffffff)
- **Highlighted sections:** `--bg-secondary` (ft-pink #fff1e5)
- **Data boxes:** `--bg-secondary` (ft-pink #fff1e5) with magenta left border

## Standard Article Structure

```markdown
---
layout: post
title: "Article Title Here"
date: YYYY-MM-DD HH:MM:SS -0400
tags: [tag1, tag2, tag3]
read_time: X min
---

# Main Headline
*Subtitle or dateline*

---

## Section Header

Content here...

---

## Another Section

### Subsection

Content with **bold** and *italic* text.

| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |

---

*Closing note or disclaimer*
```

## Formatting Rules

1. **Always include front matter** with layout: post, title, date, tags
2. **Use horizontal rules** (`---`) to separate major sections
3. **Start with H1** for the main headline, then use H2/H3 for subsections
4. **Italicize datelines** under the main headline
5. **Use tables** for data (they get the pink background styling automatically)
6. **End with a disclaimer** for financial content

## Color Usage

- **Magenta (#9b1648):** Labels, accents, links on hover, important headers
- **Pink (#fff1e5):** Backgrounds for highlighted sections, data boxes, sidebars
- **Black (#333333):** Primary text
- **Grey (#6b6b6b):** Secondary text
- **Light Grey (#b0b0b0):** Muted text, borders
- **Green (#00875f):** Positive changes, gains
- **Red (#cc0000):** Negative changes, losses
