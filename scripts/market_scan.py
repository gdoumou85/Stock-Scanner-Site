#!/usr/bin/env python3
"""
Market-Wide Scan Script
Gathers macro data: futures, VIX, sectors, commodities
Saves to JSON for AI analysis
"""

import json
import urllib.request
import urllib.error
import ssl
from datetime import datetime
import os

# Disable SSL verification for Yahoo Finance
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_yahoo_data(symbols):
    """Fetch data from Yahoo Finance"""
    results = {}
    
    for symbol in symbols:
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=5d"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                
                if data.get('chart', {}).get('result'):
                    result = data['chart']['result'][0]
                    meta = result['meta']
                    
                    # Get current price
                    current = meta.get('regularMarketPrice', 0)
                    prev = meta.get('previousClose', meta.get('chartPreviousClose', 0))
                    
                    change = current - prev if prev else 0
                    change_pct = (change / prev * 100) if prev else 0
                    
                    results[symbol] = {
                        'price': round(current, 2),
                        'previous_close': round(prev, 2),
                        'change': round(change, 2),
                        'change_pct': round(change_pct, 2)
                    }
        except Exception as e:
            results[symbol] = {'error': str(e)}
    
    return results

def scan_markets():
    """Scan all market data"""
    print(f"[{datetime.now()}] Starting market scan...")
    
    # Market futures
    futures = fetch_yahoo_data(['ES=F', 'NQ=F', 'YM=F', 'CL=F', 'GC=F', 'BTC-USD'])
    
    # Sector ETFs
    sectors = fetch_yahoo_data(['XLF', 'XLK', 'XLE', 'XLI', 'XLU', 'XLP', 'XLB', 'XLY', 'XLV'])
    
    # VIX
    vix_data = fetch_yahoo_data(['^VIX'])
    
    # Major indices
    indices = fetch_yahoo_data(['^GSPC', '^IXIC', '^DJI', '^RUT'])
    
    # Dollar
    dollar = fetch_yahoo_data(['DX-Y.NYB'])
    
    market_data = {
        'scan_time': datetime.now().isoformat(),
        'futures': futures,
        'sectors': sectors,
        'vix': vix_data,
        'indices': indices,
        'dollar': dollar
    }
    
    # Save to file
    output_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data/market')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"market_scan_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w') as f:
        json.dump(market_data, f, indent=2)
    
    print(f"Saved to {filepath}")
    print(f"Scan complete: {len(futures)} futures, {len(sectors)} sectors, {len(indices)} indices")
    
    return market_data

if __name__ == '__main__':
    scan_markets()
