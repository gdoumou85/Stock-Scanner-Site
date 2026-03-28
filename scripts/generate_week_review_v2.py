#!/usr/bin/env python3
"""
Week in Review Generator v2 - Narrative Style
Creates an engaging weekly summary like a newsletter
"""

import json
import glob
import os
from datetime import datetime, timedelta
import shutil

def load_week_headlines():
    """Extract major headlines from the week"""
    # This would parse actual news files
    # For now, return structure for AI to fill
    return {
        'major_events': [],  # Fed decisions, geopolitical, etc.
        'earnings_surprises': [],  # Companies that beat/missed
        'sector_moves': [],  # Which sectors led/lagged
        'notable_news': []  # Other significant headlines
    }

def get_tracked_performance():
    """Get performance of tickers we tracked"""
    # Read from data/performance or calculate
    return {
        'total_tickers': 20,  # 4 per day x 5 days
        'winners': [],
        'losers': [],
        'lessons': []
    }

def generate_narrative_review(week_start, week_end):
    """Generate narrative Week in Review"""
    
    date_range = f"{week_start.strftime('%B %d')} - {week_end.strftime('%B %d, %Y')}"
    
    article = f"""---
layout: post
title: "Week in Review: {date_range}"
date: {week_end.strftime('%Y-%m-%d')} 10:00:00 -0400
tags: [week-in-review, weekly-summary]
read_time: 8 min
---

# Week in Review: {date_range}
*Saturday, {week_end.strftime('%B %d, %Y')}*

---

## This Week in Markets

[AI: Write 3-4 paragraphs summarizing the week's major themes. What drove markets? What were the big stories? How did sectors rotate?]

**The big themes:**
- **[Theme 1]** — [Brief explanation of what happened]
- **[Theme 2]** — [Another major development]
- **[Theme 3]** — [Third key theme]

**Notable events:**
- [Major earnings surprise or miss]
- [Fed speaker or economic data]
- [Geopolitical development]
- [Sector rotation or breakout]

---

## Our Week: The Good

### Best Call: [Ticker]
Sometimes the setup is just right. This week, [ticker] delivered exactly what we expected — and then some.

**What we saw:** [Brief setup from earlier in week]

**What happened:** [How it played out]

**The result:** [Performance number]

**Why it worked:** [Analysis of what made this a good call]

---

### Honorable Mentions
- **[Ticker]** — [Brief success story]
- **[Ticker]** — [Brief success story]

---

## Our Week: The Not-So-Good

### Learning Moment: [Ticker]
Not every setup plays out. This week reminded us that [lesson about risk management or timing].

**What we saw:** [The setup that looked good]

**What happened:** [Why it didn't work]

**The result:** [Performance, with honesty]

**The lesson:** [What we learned — this is the important part]

---

## By the Numbers

| Metric | This Week |
|--------|-----------|
| Tickers Monitored | [X] |
| Winners | [X] |
| Losers | [X] |
| Win Rate | [X]% |
| Average Return (Winners) | +[X]% |
| Average Return (Losers) | -[X]% |
| Best Performer | [Ticker] +[X]% |
| Worst Performer | [Ticker] -[X]% |

---

## What Worked This Week

**Technical Setups:**
[Did breakouts work? Did oversold bounces play out?]

**News-Driven Plays:**
[Did earnings trades work? Did upgrades/downgrades matter?]

**Sectors:**
[Which sector themes paid off?]

---

## Market Musings

[AI: Write 2-3 paragraphs of reflection. What surprised us? What patterns emerged? Any changes to our approach needed?]

**Key insight:** [One major takeaway from the week]

**Surprise of the week:** [Something unexpected that happened]

**Looking ahead:** [Brief transition to next week]

---

## Archived for History

This week's data has been archived for future analysis:
- **Market scans:** [X] files covering futures, sectors, and macro data
- **News scans:** [X] files capturing headlines and signals
- **Technical screens:** [X] files screening [X] stocks

All data moved to: `data/archive/week_{week_start.strftime('%Y%m%d')}/`

---

## Coming Up

Tomorrow we publish our **Week Ahead Preview** — economic calendar, earnings schedule, and what we're watching for next week.

**Back to daily coverage Monday at 5:30 AM EST.**

---

*Thanks for following along this week. Here's to better calls next week.*

**— The Market Pulse Scanner Team**

**Disclaimer:** Past performance does not predict future results. Our analysis is for informational purposes only.
"""
    
    return article

def archive_and_clean(week_start):
    """Archive week's data and clean up"""
    data_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data')
    archive_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data/archive')
    
    week_folder = f"{archive_dir}/week_{week_start.strftime('%Y%m%d')}"
    os.makedirs(week_folder, exist_ok=True)
    
    for subdir in ['market', 'news', 'technical']:
        subdir_path = f"{week_folder}/{subdir}"
        os.makedirs(subdir_path, exist_ok=True)
        
        # Move files from last 7 days
        for i in range(7):
            date_str = (week_start - timedelta(days=i)).strftime('%Y%m%d')
            files = glob.glob(f"{data_dir}/{subdir}/*{date_str}*.json")
            for f in files:
                shutil.move(f, subdir_path)
    
    print(f"Week archived to: {week_folder}")
    print("Data folders cleaned for new week")

def main():
    """Main function"""
    print(f"[{datetime.now()}] Generating narrative Week in Review...")
    
    week_end = datetime.now()
    week_start = week_end - timedelta(days=6)
    
    # Generate narrative article
    article = generate_narrative_review(week_start, week_end)
    
    # Save article
    posts_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/_posts')
    os.makedirs(posts_dir, exist_ok=True)
    
    filename = f"{week_end.strftime('%Y-%m-%d')}-week-in-review.md"
    filepath = os.path.join(posts_dir, filename)
    
    with open(filepath, 'w') as f:
        f.write(article)
    
    print(f"Article saved to {filepath}")
    
    # Archive and clean
    archive_and_clean(week_start)
    
    print("\n✅ Week in Review complete!")
    print("📦 Data archived")
    print("📝 Ready for tomorrow's Week Ahead Preview")

if __name__ == '__main__':
    main()
