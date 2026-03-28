#!/bin/bash
# Master Data Collection Script
# Runs all scans in sequence and generates template

echo "======================================"
echo "Market Pulse Scanner - Daily Data Run"
echo "Started: $(date)"
echo "======================================"
echo ""

cd ~/.openclaw/workspace/projects/stock-scanner-site

# Run market scan
echo "[1/4] Running market-wide scan..."
python3 scripts/market_scan.py
echo ""

# Run news scan
echo "[2/4] Running news aggregation..."
python3 scripts/news_scan.py
echo ""

# Run technical screen
echo "[3/4] Running technical screen..."
python3 scripts/technical_screen.py
echo ""

# Generate template
echo "[4/4] Generating Daily Brief template..."
python3 scripts/generate_brief.py
echo ""

echo "======================================"
echo "Data collection complete!"
echo "Time: $(date)"
echo "======================================"
echo ""
echo "Data saved to:"
echo "  - data/market/"
echo "  - data/news/"
echo "  - data/technical/"
echo ""
echo "Template ready for AI analysis in _posts/"
