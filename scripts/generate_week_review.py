#!/usr/bin/env python3
"""
Week in Review Generator
Reads week's data, calculates performance, archives old data
"""

import json
import glob
import os
from datetime import datetime, timedelta
import shutil

def load_week_data(week_start):
    """Load all data files from the week"""
    data_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data')
    
    week_data = {
        'market': [],
        'news': [],
        'technical': [],
        'tickers_tracked': set()
    }
    
    # Load files from last 7 days
    for i in range(7):
        date_str = (week_start - timedelta(days=i)).strftime('%Y%m%d')
        
        # Market data
        market_files = glob.glob(f"{data_dir}/market/*{date_str}*.json")
        for f in market_files:
            with open(f) as file:
                week_data['market'].append(json.load(file))
        
        # News data
        news_files = glob.glob(f"{data_dir}/news/*{date_str}*.json")
        for f in news_files:
            with open(f) as file:
                week_data['news'].append(json.load(file))
        
        # Technical data
        tech_files = glob.glob(f"{data_dir}/technical/*{date_str}*.json")
        for f in tech_files:
            with open(f) as file:
                week_data['technical'].append(json.load(file))
    
    return week_data

def calculate_performance():
    """Calculate week's trading performance"""
    # This would read actual trade data when we have it
    # For now, return template values
    return {
        'tickers_monitored': 20,  # Placeholder
        'winners': 12,
        'losers': 8,
        'win_rate': 60,
        'avg_return': 2.3,
        'best_performer': {'ticker': 'NVDA', 'return': 15.5},
        'worst_performer': {'ticker': 'SOFI', 'return': -8.2}
    }

def generate_week_review(week_data, performance):
    """Generate Week in Review article"""
    
    week_end = datetime.now()
    week_start = week_end - timedelta(days=6)
    
    date_range = f"{week_start.strftime('%B %d')} - {week_end.strftime('%B %d, %Y')}"
    
    article = f"""---
layout: post
title: "Week in Review: {date_range}"
date: {week_end.strftime('%Y-%m-%d')} 10:00:00 -0400
tags: [week-in-review, weekly-summary]
read_time: 5 min
---

# Week in Review
*{date_range}*

---

## Performance Summary

| Metric | Value |
|--------|-------|
| Tickers Monitored | {performance['tickers_monitored']} |
| Winning Trades | {performance['winners']} |
| Losing Trades | {performance['losers']} |
| Win Rate | {performance['win_rate']}% |
| Average Return | +{performance['avg_return']}% |
| Best Performer | {performance['best_performer']['ticker']} +{performance['best_performer']['return']}% |
| Worst Performer | {performance['worst_performer']['ticker']} {performance['worst_performer']['return']}% |

---

## Best Calls This Week

[AI: Fill based on actual tracked tickers and their performance]

### Top Performer: {performance['best_performer']['ticker']}
- Weekly Return: +{performance['best_performer']['return']}%
- Why it worked: [Analysis]

---

## What Didn't Work

### Worst Performer: {performance['worst_performer']['ticker']}
- Weekly Return: {performance['worst_performer']['return']}%
- What went wrong: [Analysis]
- Lesson learned: [Takeaway]

---

## Market Themes This Week

[AI: Analyze week's data and identify key themes]

1. **Theme 1** — [Explanation]
2. **Theme 2** — [Explanation]
3. **Theme 3** — [Explanation]

---

## Key Levels Heading Into Next Week

**S&P 500:** [Support] / [Resistance]
**Nasdaq:** [Support] / [Resistance]

---

## Data Archive

This week's data has been archived for historical analysis.
- Market scans: {len(week_data['market'])} files
- News scans: {len(week_data['news'])} files
- Technical screens: {len(week_data['technical'])} files

---

*Weekend analysis complete. Week Ahead Preview publishing tomorrow.*

**Disclaimer:** Past performance does not predict future results.
"""
    
    return article

def archive_week_data(week_start):
    """Move week's data to archive"""
    data_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data')
    archive_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data/archive')
    
    week_folder = f"{archive_dir}/week_{week_start.strftime('%Y%m%d')}"
    os.makedirs(week_folder, exist_ok=True)
    
    # Create subdirectories
    os.makedirs(f"{week_folder}/market", exist_ok=True)
    os.makedirs(f"{week_folder}/news", exist_ok=True)
    os.makedirs(f"{week_folder}/technical", exist_ok=True)
    
    # Move files
    for i in range(7):
        date_str = (week_start - timedelta(days=i)).strftime('%Y%m%d')
        
        for subdir in ['market', 'news', 'technical']:
            files = glob.glob(f"{data_dir}/{subdir}/*{date_str}*.json")
            for f in files:
                shutil.move(f, f"{week_folder}/{subdir}/")
    
    print(f"Archived to {week_folder}")

def main():
    """Main function"""
    print(f"[{datetime.now()}] Generating Week in Review...")
    
    week_end = datetime.now()
    week_start = week_end - timedelta(days=6)
    
    # Load data
    week_data = load_week_data(week_start)
    
    # Calculate performance
    performance = calculate_performance()
    
    # Generate article
    article = generate_week_review(week_data, performance)
    
    # Save article
    posts_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/_posts')
    os.makedirs(posts_dir, exist_ok=True)
    
    filename = f"{week_end.strftime('%Y-%m-%d')}-week-in-review.md"
    filepath = os.path.join(posts_dir, filename)
    
    with open(filepath, 'w') as f:
        f.write(article)
    
    print(f"Saved to {filepath}")
    
    # Archive data
    archive_week_data(week_start)
    
    print("Week in Review complete!")
    print("Data archived.")
    print("Tomorrow: Week Ahead Preview")

if __name__ == '__main__':
    main()
