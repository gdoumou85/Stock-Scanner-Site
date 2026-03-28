#!/usr/bin/env python3
"""
Daily Brief Generator
Analyzes market data and generates the Daily Brief article
Saves as Markdown for Jekyll
"""

import json
import os
from datetime import datetime, timedelta
import glob

def load_latest_data():
    """Load the most recent scan data"""
    data_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data')
    
    data = {}
    
    # Find latest market scan
    market_files = sorted(glob.glob(f"{data_dir}/market/market_scan_*.json"))
    if market_files:
        with open(market_files[-1]) as f:
            data['market'] = json.load(f)
    
    # Find latest news scan
    news_files = sorted(glob.glob(f"{data_dir}/news/news_scan_*.json"))
    if news_files:
        with open(news_files[-1]) as f:
            data['news'] = json.load(f)
    
    # Find latest technical screen
    tech_files = sorted(glob.glob(f"{data_dir}/technical/technical_screen_*.json"))
    if tech_files:
        with open(tech_files[-1]) as f:
            data['technical'] = json.load(f)
    
    return data

def generate_daily_brief_template():
    """Generate template for AI to fill in"""
    
    tomorrow = datetime.now() + timedelta(days=1)
    date_str = tomorrow.strftime("%B %d, %Y")
    
    template = f"""---
layout: post
title: "{tomorrow.strftime("%B %d")} Pre-Market Brief: [TBD - Title based on overnight data]"
date: {tomorrow.strftime("%Y-%m-%d")} 05:30:00 -0400
tags: [daily-brief, pre-market, macro]
read_time: 6 min
---

# {tomorrow.strftime("%B %d")} Pre-Market Brief
*{tomorrow.strftime("%A, %B %d, %Y")} | 5:30 AM EST*

---

## What Happened Overnight

[AI: Fill based on futures and overnight market data]

**Key Data Points:**
- S&P 500 Futures: [TBD]
- Nasdaq Futures: [TBD]
- VIX: [TBD]

---

## Today's Watchlist

[AI: Based on technical screening, select 4-6 tickers]

### [Ticker 1] ($[price])
[AI: Brief setup description]

### [Ticker 2] ($[price])
[AI: Brief setup description]

[Continue for all selected tickers...]

---

## Important Events Today

[AI: Based on economic calendar data]

---

## My Take

[AI: Overall market analysis and strategy]

---

*Markets open at 9:30 AM EST. Updates every hour after that.*

**Disclaimer:** This is market analysis, not financial advice.
"""
    
    return template

def main():
    """Main function"""
    print(f"[{datetime.now()}] Loading latest data...")
    
    data = load_latest_data()
    
    print(f"Loaded:")
    print(f"  - Market data: {'Yes' if 'market' in data else 'No'}")
    print(f"  - News data: {'Yes' if 'news' in data else 'No'}")
    print(f"  - Technical data: {'Yes' if 'technical' in data else 'No'}")
    
    # Generate template
    template = generate_daily_brief_template()
    
    # Save to file
    posts_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/_posts')
    os.makedirs(posts_dir, exist_ok=True)
    
    tomorrow = datetime.now() + timedelta(days=1)
    filename = f"{tomorrow.strftime('%Y-%m-%d')}-daily-brief-ready-for-analysis.md"
    filepath = os.path.join(posts_dir, filename)
    
    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"\nTemplate saved to: {filepath}")
    print(f"\nNext steps:")
    print(f"1. Review the data files in ~/.openclaw/workspace/projects/stock-scanner-site/data/")
    print(f"2. Fill in the template with analysis")
    print(f"3. Commit and push to publish")

if __name__ == '__main__':
    main()
