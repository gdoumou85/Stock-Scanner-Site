#!/usr/bin/env python3
"""
News Scanner v2 - Enhanced with Signal Extraction
Extracts actionable trading signals from news sources
"""

import json
import urllib.request
import urllib.error
import ssl
import re
from datetime import datetime
import os

ssl._create_default_https_context = ssl._create_unverified_context

# Keywords for sentiment analysis
BULLISH_KEYWORDS = [
    'upgrade', 'beats', 'outperform', 'buy', 'strong buy', 'price target raise',
    'partnership', 'deal', 'contract', 'expansion', 'growth', 'record revenue',
    'insider buying', 'share buyback', 'dividend increase', 'guidance raise',
    'fda approval', 'breakthrough', 'milestone', 'beats expectations'
]

BEARISH_KEYWORDS = [
    'downgrade', 'misses', 'underperform', 'sell', 'strong sell', 'price target cut',
    'lawsuit', 'investigation', 'sec probe', 'accounting irregularities',
    'insider selling', 'guidance cut', 'layoffs', 'recall', 'data breach',
    'bankruptcy', 'restructuring', 'short report', 'muddy waters'
]

VOLATILITY_KEYWORDS = [
    'earnings', 'earnings report', 'earnings call', 'conference call',
    'fda decision', 'clinical trial results', 'merger', 'acquisition',
    'ipo', 'offering', 'secondary offering'
]

def analyze_sentiment(text):
    """Simple sentiment analysis based on keywords"""
    text_lower = text.lower()
    
    bullish_score = sum(1 for word in BULLISH_KEYWORDS if word in text_lower)
    bearish_score = sum(1 for word in BEARISH_KEYWORDS if word in text_lower)
    volatility_score = sum(1 for word in VOLATILITY_KEYWORDS if word in text_lower)
    
    if bullish_score > bearish_score:
        return 'bullish', bullish_score - bearish_score, volatility_score
    elif bearish_score > bullish_score:
        return 'bearish', bearish_score - bullish_score, volatility_score
    else:
        return 'neutral', 0, volatility_score

def extract_tickers(text):
    """Extract stock tickers from text (2-5 uppercase letters)"""
    tickers = re.findall(r'\b[A-Z]{2,5}\b', text)
    # Filter out common false positives
    exclude = {'CEO', 'CFO', 'CTO', 'COO', 'USA', 'US', 'EU', 'CEO', 'IPO', 'EPS', 'GDP', 'CPI', 'FED', 'SEC', 'FDA'}
    return [t for t in tickers if t not in exclude][:5]  # Limit to 5

def fetch_yahoo_headlines():
    """Fetch Yahoo Finance trending headlines"""
    headlines = []
    
    tickers_to_check = ['SOFI', 'NVDA', 'TSLA', 'AAPL', 'PLTR', 'XOM', 'JPM', 'COIN']
    
    for ticker in tickers_to_check:
        try:
            url = f"https://query1.finance.yahoo.com/v1/finance/search?q={ticker}&newsCount=3"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.load(response)
                
                if data.get('news'):
                    for item in data['news']:
                        title = item.get('title', '')
                        if title:
                            sentiment, score, vol = analyze_sentiment(title)
                            headlines.append({
                                'source': 'Yahoo Finance',
                                'ticker': ticker,
                                'title': title,
                                'sentiment': sentiment,
                                'score': score,
                                'volatility': vol,
                                'time': item.get('published', '')
                            })
        except:
            continue
    
    return headlines

def fetch_reddit_wsb():
    """Fetch trending from WallStreetBets"""
    trending = []
    
    try:
        url = "https://www.reddit.com/r/wallstreetbets/hot.json?limit=15"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.load(response)
            
            for post in data.get('data', {}).get('children', []):
                title = post['data'].get('title', '')
                score = post['data'].get('score', 0)
                comments = post['data'].get('num_comments', 0)
                
                if score > 50:  # Only popular posts
                    tickers = extract_tickers(title)
                    sentiment, sig_score, vol = analyze_sentiment(title)
                    
                    if tickers:
                        trending.append({
                            'source': 'Reddit WSB',
                            'tickers': tickers,
                            'title': title[:120],
                            'upvotes': score,
                            'comments': comments,
                            'sentiment': sentiment,
                            'score': sig_score
                        })
    except:
        pass
    
    return trending

def generate_signals(news_items):
    """Generate trading signals from news"""
    signals = {
        'strong_buy': [],
        'buy': [],
        'avoid': [],
        'short_candidate': [],
        'earnings_today': [],
        'high_volatility': []
    }
    
    for item in news_items:
        title = item.get('title', '')
        ticker = item.get('ticker', '')
        sentiment = item.get('sentiment', 'neutral')
        score = item.get('score', 0)
        
        if not ticker:
            continue
        
        # Check for earnings
        if 'earnings' in title.lower():
            signals['earnings_today'].append({
                'ticker': ticker,
                'headline': title,
                'sentiment': sentiment
            })
            signals['high_volatility'].append(ticker)
        
        # Strong bullish signals
        if sentiment == 'bullish' and score >= 2:
            if any(x['ticker'] == ticker for x in signals['strong_buy']):
                continue
            signals['strong_buy'].append({
                'ticker': ticker,
                'headline': title,
                'confidence': score
            })
        
        # Moderate bullish
        elif sentiment == 'bullish' and score == 1:
            if ticker not in [x['ticker'] for x in signals['buy']]:
                signals['buy'].append({
                    'ticker': ticker,
                    'headline': title
                })
        
        # Bearish signals
        if sentiment == 'bearish' and score >= 2:
            if ticker not in [x['ticker'] for x in signals['avoid']]:
                signals['avoid'].append({
                    'ticker': ticker,
                    'headline': title,
                    'reason': 'negative_news'
                })
                signals['short_candidate'].append(ticker)
    
    return signals

def scan_news_v2():
    """Enhanced news scan with signal extraction"""
    print(f"[{datetime.now()}] Starting enhanced news scan...")
    
    # Gather all news
    all_headlines = fetch_yahoo_headlines()
    reddit_trending = fetch_reddit_wsb()
    
    # Generate signals
    signals = generate_signals(all_headlines)
    
    # Also check Reddit
    for post in reddit_trending:
        if post['sentiment'] == 'bullish' and post['score'] >= 1:
            for ticker in post['tickers']:
                if not any(x['ticker'] == ticker for x in signals['buy']):
                    signals['buy'].append({
                        'ticker': ticker,
                        'headline': f"Reddit buzz: {post['title'][:50]}...",
                        'social_sentiment': 'bullish'
                    })
    
    news_data = {
        'scan_time': datetime.now().isoformat(),
        'headlines': all_headlines[:15],  # Top 15
        'reddit_trending': reddit_trending[:10],
        'signals': signals,
        'summary': {
            'bullish_signals': len(signals['strong_buy']) + len(signals['buy']),
            'bearish_signals': len(signals['avoid']),
            'earnings_today': len(signals['earnings_today']),
            'high_volatility': len(signals['high_volatility'])
        }
    }
    
    # Save
    output_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data/news')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"news_signals_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w') as f:
        json.dump(news_data, f, indent=2)
    
    print(f"Saved to {filepath}")
    print(f"\nSignal Summary:")
    print(f"  Strong Buy: {len(signals['strong_buy'])}")
    print(f"  Buy: {len(signals['buy'])}")
    print(f"  Avoid/Short: {len(signals['avoid'])}")
    print(f"  Earnings Today: {len(signals['earnings_today'])}")
    
    return news_data

if __name__ == '__main__':
    scan_news_v2()
