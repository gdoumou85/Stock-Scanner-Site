#!/usr/bin/env python3
"""
News Aggregation Script
Scans multiple sources for headlines, analyst moves, SEC filings
Saves to JSON for AI analysis
"""

import json
import urllib.request
import urllib.error
import ssl
from datetime import datetime
import os
import re

ssl._create_default_https_context = ssl._create_unverified_context

def fetch_sec_filings():
    """Fetch recent SEC 8-K filings for notable companies"""
    filings = []
    
    # List of tickers to monitor for filings
    watchlist = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 
                 'NFLX', 'AMD', 'INTC', 'SOFI', 'COIN', 'PLTR', 'XOM', 'JPM']
    
    for ticker in watchlist:
        try:
            # SEC EDGAR RSS feed
            url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=8-K&CIK={ticker}&count=1&output=atom"
            # Note: SEC requires proper headers
            req = urllib.request.Request(url, headers={
                'User-Agent': 'MarketPulseScanner contact@marketpulse.com'
            })
            
            # Skip for now - SEC needs proper setup
            pass
        except:
            pass
    
    return filings

def fetch_reddit_sentiment():
    """Fetch trending tickers from Reddit (basic scraping)"""
    trending = []
    
    try:
        # r/wallstreetbets hot posts
        url = "https://www.reddit.com/r/wallstreetbets/hot.json?limit=10"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
            for post in data.get('data', {}).get('children', []):
                title = post['data'].get('title', '')
                # Extract ticker mentions (all caps 2-5 letters)
                tickers = re.findall(r'\b[A-Z]{2,5}\b', title)
                if tickers:
                    trending.append({
                        'tickers': tickers,
                        'title': title[:100],
                        'score': post['data'].get('score', 0)
                    })
    except:
        pass
    
    return trending

def fetch_yahoo_news():
    """Fetch Yahoo Finance trending news"""
    news_items = []
    
    try:
        # Yahoo Finance news RSS
        url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^GSPC&region=US&lang=en-US"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode()
            # Simple parsing - in production use proper RSS parser
            titles = re.findall(r'&lt;title&gt;([^&lt;]+)&lt;/title&gt;', content)
            for title in titles[:10]:
                news_items.append({'source': 'Yahoo Finance', 'title': title})
    except:
        pass
    
    return news_items

def scan_news():
    """Scan all news sources"""
    print(f"[{datetime.now()}] Starting news scan...")
    
    news_data = {
        'scan_time': datetime.now().isoformat(),
        'reddit_trending': fetch_reddit_sentiment(),
        'yahoo_news': fetch_yahoo_news(),
        'sec_filings': fetch_sec_filings(),
        'analyst_moves': [],  # Placeholder for Benzinga API
        'earnings': []        # Placeholder
    }
    
    # Save
    output_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data/news')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"news_scan_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w') as f:
        json.dump(news_data, f, indent=2)
    
    print(f"Saved to {filepath}")
    print(f"Found: {len(news_data['reddit_trending'])} Reddit posts, {len(news_data['yahoo_news'])} news items")
    
    return news_data

if __name__ == '__main__':
    scan_news()
