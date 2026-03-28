# Article Templates

This folder contains templates for creating new articles with consistent formatting and styling.

## Available Templates

| Template | Use For | File |
|----------|---------|------|
| **Daily Brief** | Pre-market daily updates | `daily-brief.md` |
| **Market Holiday** | Market closure announcements | `market-holiday.md` |
| **Week Ahead** | Sunday preview of upcoming week | `week-ahead-preview.md` |
| **Week in Review** | Saturday recap of the week | `week-in-review.md` |
| **Generic Article** | Any standard article | `generic-article.md` |

## Style Guide

All articles follow the **Financial Times inspired** color scheme:

- **Background:** White (`--bg-primary` / #ffffff)
- **Accent Background:** Pink (`--ft-pink` / #fff1e5)
- **Primary Accent:** Magenta (`--ft-magenta` / #9b1648)
- **Positive/Gains:** Green (#00875f)
- **Negative/Losses:** Red (#cc0000)

## Creating a New Article

1. Copy the appropriate template
2. Replace all `[bracketed placeholders]` with actual content
3. Update the front matter (title, date, tags)
4. Save to `_posts/` folder with format: `YYYY-MM-DD-title.md`
5. The styling will be applied automatically via `main.scss`

## Front Matter Required

```yaml
---
layout: post
title: "Your Article Title"
date: YYYY-MM-DD HH:MM:SS -0400
tags: [tag1, tag2]
read_time: X min
---
```

## Formatting Tips

- Use `---` horizontal rules to separate major sections
- Start with H1 (`#`) for the main headline
- Use H2 (`##`) for section headers
- Use H3 (`###`) for subsections
- Tables automatically get styled with pink backgrounds
- Use `**bold**` for emphasis, `*italic*` for datelines
- Always end with a disclaimer for financial content
