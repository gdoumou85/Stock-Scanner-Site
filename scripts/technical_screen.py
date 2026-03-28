#!/usr/bin/env python3
"""
Technical Screener Script
Finds stocks meeting technical criteria
Saves to JSON for AI analysis
"""

import json
import urllib.request
import ssl
from datetime import datetime, timedelta
import os

ssl._create_default_https_context = ssl._create_unverified_context

def fetch_stock_data(symbol):
    """Fetch detailed stock data for screening"""
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1y"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
            if data.get('chart', {}).get('result'):
                result = data['chart']['result'][0]
                meta = result['meta']
                
                # Get price data
                current = meta.get('regularMarketPrice', 0)
                prev = meta.get('previousClose', 0)
                
                # Get historical data
                timestamps = result.get('timestamp', [])
                closes = result['indicators']['quote'][0].get('close', []) if result.get('indicators') else []
                volumes = result['indicators']['quote'][0].get('volume', []) if result.get('indicators') else []
                
                if not closes or len(closes) < 50:
                    return None
                
                # Calculate metrics
                valid_closes = [c for c in closes if c]
                if not valid_closes:
                    return None
                
                latest_close = valid_closes[-1]
                prev_close = valid_closes[-2] if len(valid_closes) > 1 else latest_close
                
                # 52-week high/low
                high_52w = max(valid_closes[-252:]) if len(valid_closes) >= 252 else max(valid_closes)
                low_52w = min(valid_closes[-252:]) if len(valid_closes) >= 252 else min(valid_closes)
                
                # Moving averages
                sma_20 = sum(valid_closes[-20:]) / 20 if len(valid_closes) >= 20 else None
                sma_50 = sum(valid_closes[-50:]) / 50 if len(valid_closes) >= 50 else None
                
                # Volume
                avg_volume = sum(volumes[-20:]) / 20 if volumes else 0
                latest_volume = volumes[-1] if volumes else 0
                volume_spike = (latest_volume / avg_volume) if avg_volume > 0 else 1
                
                # Change
                change_pct = ((latest_close - prev_close) / prev_close * 100) if prev_close else 0
                
                return {
                    'symbol': symbol,
                    'price': round(latest_close, 2),
                    'change_pct': round(change_pct, 2),
                    'high_52w': round(high_52w, 2),
                    'low_52w': round(low_52w, 2),
                    'sma_20': round(sma_20, 2) if sma_20 else None,
                    'sma_50': round(sma_50, 2) if sma_50 else None,
                    'volume': latest_volume,
                    'avg_volume_20': int(avg_volume),
                    'volume_spike': round(volume_spike, 2),
                    'distance_from_high': round((latest_close - high_52w) / high_52w * 100, 2),
                    'distance_from_low': round((latest_close - low_52w) / low_52w * 100, 2)
                }
    except Exception as e:
        return {'symbol': symbol, 'error': str(e)}
    
    return None

def screen_stocks():
    """Screen stocks for technical setups"""
    print(f"[{datetime.now()}] Starting technical screen...")
    
    # Stock universe (can be expanded)
    universe = [
        # Tech
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA', 'NFLX', 'AMD', 'INTC',
        # Finance
        'JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'SOFI', 'COIN', 'HOOD',
        # Growth
        'PLTR', 'SNOW', 'CRWD', 'DDOG', 'NET', 'OKTA', 'ZM', 'DOCU', 'SHOP',
        # Energy
        'XOM', 'CVX', 'COP', 'EOG', 'SLB', 'OXY',
        # Healthcare
        'JNJ', 'PFE', 'UNH', 'ABBV', 'LLY', 'MRK',
        # Consumer
        'AMZN', 'WMT', 'HD', 'COST', 'NKE', 'SBUX', 'MCD',
        # Industrials
        'BA', 'CAT', 'GE', 'RTX', 'LMT', 'UPS'
    ]
    
    results = {
        'breakout_candidates': [],
        'breakdown_candidates': [],
        'oversold_bounce': [],
        'volume_spikes': [],
        'near_52w_high': [],
        'near_52w_low': []
    }
    
    scanned = 0
    for symbol in universe:
        data = fetch_stock_data(symbol)
        scanned += 1
        
        if data and 'error' not in data:
            price = data['price']
            change = data['change_pct']
            vol_spike = data['volume_spike']
            dist_high = data['distance_from_high']
            dist_low = data['distance_from_low']
            
            # Filters
            if price > 5:  # Minimum price
                # Breakout: Price above SMA 20, positive momentum, volume
                if change > 2 and vol_spike > 1.5 and data['sma_20'] and price > data['sma_20']:
                    results['breakout_candidates'].append(data)
                
                # Breakdown: Below SMA 20, negative, volume
                if change < -2 and vol_spike > 1.5 and data['sma_20'] and price < data['sma_20']:
                    results['breakdown_candidates'].append(data)
                
                # Oversold bounce: Near 52w low but bouncing
                if dist_low > -10 and change > 1:
                    results['oversold_bounce'].append(data)
                
                # Volume spike
                if vol_spike > 2:
                    results['volume_spikes'].append(data)
                
                # Near 52w high
                if dist_high > -5:
                    results['near_52w_high'].append(data)
                
                # Near 52w low
                if dist_low < 10:
                    results['near_52w_low'].append(data)
    
    # Save results
    screen_data = {
        'scan_time': datetime.now().isoformat(),
        'scanned_count': scanned,
        'results': results
    }
    
    output_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site/data/technical')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"technical_screen_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w') as f:
        json.dump(screen_data, f, indent=2)
    
    print(f"Saved to {filepath}")
    print(f"Scanned {scanned} stocks")
    print(f"Breakouts: {len(results['breakout_candidates'])}")
    print(f"Breakdowns: {len(results['breakdown_candidates'])}")
    print(f"Oversold: {len(results['oversold_bounce'])}")
    print(f"Volume spikes: {len(results['volume_spikes'])}")
    
    return screen_data

if __name__ == '__main__':
    screen_stocks()
