# Market Pulse Scanner - Project Plan

**Last Updated:** March 28, 2026  
**Status:** Ready for Launch

---

## 1. Project Overview

### Vision
Create an automated stock market analysis website that publishes daily research on selected tickers. The site combines AI-assisted analysis with market data to identify opportunities worth monitoring.

### Core Value Proposition
**"Informed Commentary for Discerning Investors"**

Every article makes readers feel smarter about the companies and markets they're following. Deep dives include full fundamental analysis - what the company does, its business model, financial health, and why it matters.

### Monetization
Google AdSense integration (Publisher ID: pub-4794018087983976)

### Key Principles
- **Transparency:** AI-assisted analysis, clearly disclosed
- **Quality over quantity:** Selective ticker picking, not spray-and-pray
- **Accessibility:** Plain language, no trader jargon
- **Educational:** Deep dives explain companies thoroughly
- **Multi-day tracking:** Tickers can be monitored for days, not just hours
- **Source diversity:** Multiple news sources, rotated periodically

---

## 2. Content Strategy

### Publishing Schedule (All times EST)

| Content | Time | Frequency | Description |
|---------|------|-----------|-------------|
| **Daily Market Brief** | 5:30 AM | Mon-Fri | Overnight recap, macro data, 4-6 tickers to watch |
| **Company Deep Dive #1** | 6:00 AM | Daily | Full fundamental + technical analysis of first ticker |
| **Company Deep Dive #2** | 6:45 AM | Daily | Full analysis of second ticker |
| **Company Deep Dive #3** | 7:30 AM | Daily | Full analysis of third ticker |
| **Company Deep Dive #4** | 8:15 AM | Daily | Full analysis of fourth ticker |
| **Hourly Update** | 9:35 AM - 4:00 PM | Every 1 hour | Live price action for active tickers |
| **Midday Wrap** | 12:30 PM | Daily | Morning performance summary |
| **Close Wrap** | 4:30 PM | Daily | Final numbers, tomorrow setup |

### Content Types

#### A. Daily Market Brief (5-6 min read)
**Sections:**
- Overnight global snapshot (US, Europe, Asia)
- Key macro data points
- Today's watchlist (4-6 tickers with 2-3 sentences each)
- Important events calendar
- Key support/resistance levels
- My take (1-2 paragraph summary)

**Tone:** Professional but accessible. Explain why things matter.

#### B. Company Deep Dive (8-12 min read) ← **ENHANCED**
**Sections:**

**1. Company Overview (What They Do)**
- Business model in plain English
- Main products/services
- How they make money
- Competitive position
- Recent strategic developments

**2. Financial Health Check**
- Revenue and growth trends
- Profitability metrics
- Balance sheet strength (cash, debt)
- Key ratios (P/E, P/S, margins)
- Comparison to competitors

**3. Recent Developments**
- Last earnings call highlights
- Recent news affecting the business
- Management guidance
- Analyst sentiment changes

**4. Technical Setup**
- Current price action
- Key levels (support/resistance)
- Volume trends
- Chart patterns

**5. Investment Thesis**
- Why we're watching NOW
- Bull case (what could go right)
- Bear case (what could go wrong)
- Risk factors

**6. Trade Setup**
- Entry zone
- Stop loss
- Price targets
- Position sizing guidance
- Timeframe

**Tone:** Educational and thorough. Make the reader feel like an expert on this company.

#### C. Hourly Update (1-2 min read)
**Sections:**
- Current price + change
- Day range
- Volume vs average
- What is happening (news/flow)
- My take (2-3 sentences)
- Next update time

**Tone:** Quick, punchy, actionable.

#### D. Midday Wrap (3 min read)
**Sections:**
- Morning summary
- Watchlist performance table
- What is working
- What is not working
- Afternoon outlook

#### E. Close Wrap (3 min read)
**Sections:**
- Final market numbers
- Watchlist final results
- Winners/losers analysis
- Overnight watch (Asia, events)
- Tomorrow's setup (key levels)

---

## 3. Data Workflow

### 4:00 AM - Data Collection (Automated)
**Scripts run:**
1. `market_scan.py` - Futures, VIX, sectors, indices
2. `news_scan_v2.py` - Headlines, signals, earnings
3. `technical_screen.py` - 80+ stocks screened

**Output:** JSON files in `data/` directory

### 4:15-5:00 AM - Analysis (Manual)
**I review:**
- Market data (direction bias)
- News signals (catalysts, earnings)
- Technical setups (breakouts, breakdowns)

**I select:** 4 tickers for deep dives
**Criteria:**
- Strong news catalyst + good technical setup
- OR: Compelling fundamental story + technical entry
- Mix of bullish and bearish setups
- Diverse sectors when possible

### 5:00-5:30 AM - Write Daily Brief
- Summarize overnight action
- Present 4 selected tickers
- Explain why each was chosen

### 6:00-8:15 AM - Write Deep Dives
**For each ticker (45 min each):**
1. Research company (10 min)
2. Analyze financials (10 min)
3. Review recent news (5 min)
4. Technical analysis (10 min)
5. Write article (10 min)
6. Publish immediately

### 9:30 AM-4:00 PM - Hourly Monitoring
**Check every hour:**
- Prices for active tickers
- News flow
- Publish updates if significant (>2% move or news)

---

## 4. Technical Setup

### Platform
- **Static Site Generator:** Jekyll
- **Hosting:** GitHub Pages
- **Domain:** gdoumou85.github.io/Stock-Scanner-Site/
- **Theme:** FT-inspired (salmon/cream with magenta header)

### Repository Structure
```
stock-scanner-site/
├── _config.yml              # Site config + AdSense ID
├── _posts/                 # All content (dated)
│   ├── YYYY-MM-DD-daily-brief.md
│   ├── YYYY-MM-DD-[ticker]-deep-dive.md
│   ├── YYYY-MM-DD-[ticker]-update-N.md
│   ├── YYYY-MM-DD-midday-wrap.md
│   └── YYYY-MM-DD-close-wrap.md
├── _layouts/               # Page templates
├── _includes/              # Reusable components
├── assets/                 # CSS, JS
├── scripts/                # Data collection
│   ├── market_scan.py
│   ├── news_scan_v2.py
│   ├── technical_screen.py
│   └── run_all.sh
└── data/                   # Historical data
    ├── market/
    ├── news/
    ├── technical/
    └── archive/
```

### AdSense Integration
- **Publisher ID:** pub-4794018087983976
- **Ad Types:** Display (horizontal), In-content, Sidebar
- **Placement:** Non-intrusive, between sections

---

## 5. Data Collection Scripts

### A. Market Scan (market_scan.py)
**Runs:** 4:00 AM
**Fetches:**
- Futures (S&P, Nasdaq, Dow)
- VIX
- Sector ETFs (XLF, XLK, XLE, etc.)
- Commodities (Oil, Gold)
- Dollar Index

**Output:** `data/market/market_scan_YYYYMMDD_HHMM.json`

### B. News Scan v2 (news_scan_v2.py)
**Runs:** 4:05 AM
**Fetches:**
- Yahoo Finance headlines
- Reddit WSB trending
- Analyst upgrades/downgrades
- SEC filing alerts

**Signal Extraction:**
- Bullish/bearish keyword detection
- Sentiment scoring
- Earnings detection
- Insider trading alerts

**Output:** `data/news/news_signals_YYYYMMDD_HHMM.json`

### C. Technical Screen (technical_screen.py)
**Runs:** 4:10 AM
**Screens:** 80+ stocks
**Criteria:**
- Breakout candidates (>2%, volume spike, above MA)
- Breakdown candidates (<-2%, volume spike, below MA)
- Oversold bounces (near 52w low, positive momentum)
- Volume spikes (>2x average)
- Near 52w high/low

**Output:** `data/technical/technical_screen_YYYYMMDD_HHMM.json`

### D. Master Script (run_all.sh)
**Runs all three in sequence**

---

## 6. My Article Generation Process

### Step 1: Data Analysis (4:15-4:45 AM)
**Review:**
- `data/market/latest.json` - Market direction
- `data/news/latest.json` - Signals and catalysts
- `data/technical/latest.json` - Screened stocks

**Decision Matrix:**
```
IF stock in technical_screen.breakout AND
   news_signals.strong_buy.contains(stock):
    → SELECT for bullish deep dive

IF stock in technical_screen.breakdown AND
   news_signals.avoid.contains(stock):
    → SELECT for bearish/short deep dive

IF stock in technical_screen.oversold AND
   news_signals.buy.contains(stock):
    → SELECT for bounce play
```

### Step 2: Select 4 Tickers (4:45 AM)
**Priorities:**
1. Highest conviction setup (strong news + strong technical)
2. Earnings play (if applicable)
3. Contrarian opportunity (oversold quality name)
4. Momentum continuation or reversal

**Mix:** At least one bearish/short candidate

### Step 3: Research Each Ticker (6:00-8:15 AM)
**For each selected ticker:**
1. **Company research** - What do they do? Business model?
2. **Financial analysis** - Revenue growth, margins, balance sheet
3. **Competitive position** - Market share, moat
4. **Recent developments** - Last earnings, guidance, news
5. **Technical analysis** - Price action, levels
6. **Write** - Educational deep dive article

### Step 4: Publish (Throughout morning)
- Publish each deep dive as completed
- Don't batch - continuous flow

### Step 5: Market Hours Monitoring (9:30 AM-4:00 PM)
- Hourly price checks
- News scanning
- Updates if significant

---

## 7. Ticker Selection Criteria

### No Hard Rules
Use judgment based on:
- Overnight news
- Technical setup
- Fundamental catalyst
- Sector rotation
- Market conditions

### Soft Guidelines
- **Market Cap:** Prefer >$500M (liquidity)
- **Price:** Prefer >$5 (avoid penny stocks)
- **Volume:** Prefer >1M daily average
- **Diversity:** Mix of sectors when possible
- **Risk levels:** Mix of conservative and speculative

### Selection Process
1. Scan futures/macro for sector themes
2. Identify 10-15 candidate tickers from technical screen
3. Rank by setup quality + news signals
4. Select top 4
5. Ensure diversity (don't pick 4 tech stocks)
6. Ensure at least one short/bearish candidate

---

## 8. News Sources

### Primary Sources
- Yahoo Finance (free API)
- Reddit (r/wallstreetbets)
- Benzinga (free tier)
- SEC EDGAR (RSS feeds)

### Rotation
- Check new sources every few days
- Add promising ones to rotation
- Drop ones with poor accuracy or paywalls

### Source Attribution
Every headline gets linked to source. Build trust through transparency.

---

## 9. Data Storage & Archival

### Daily Data
- Saved to `data/market/`, `data/news/`, `data/technical/`
- Keep 30 days locally
- Archive older data to `data/archive/`

### Historical Analysis
- Monthly review of performance
- Track win rates by setup type
- Refine selection criteria

### Article Archive
- All posts kept in `_posts/`
- Historical reference for patterns
- SEO value over time

---

## 10. Performance Tracking

### Metrics Tracked
- Entry price for each ticker
- Daily closing price
- High/low of day
- Change %
- Win/loss rate
- Average winner/loser size
- Overall expectancy

### Reporting
- Daily: Watchlist performance table
- Weekly: Summary stats
- Monthly: Historical review

### Transparency
- Show losers as well as winners
- Explain why thesis worked or failed
- Update historical accuracy honestly

---

## 11. Risk Management

### Disclaimers (On Every Page)
- "This is market analysis, not financial advice"
- "Past performance does not predict future results"
- "AI-assisted commentary, not human expert"
- "Do your own research before investing"

### Content Guidelines
- Never guarantee returns
- Always mention risks
- Position sizing recommendations (small positions)
- Stop loss suggestions

### AdSense Compliance
- No clickbait
- No misleading claims
- Quality content first
- Ad placement: Non-intrusive, between sections

---

## 12. Cron Jobs

### Data Collection
**Time:** 4:00 AM EST, Mon-Fri  
**Command:** `cd ~/.openclaw/workspace/projects/stock-scanner-site && ./scripts/run_all.sh`

### Other Reminders
- None currently (SOFI jobs removed)
- Manual monitoring during market hours

---

## 13. Current Status

### ✅ Completed
- [x] Jekyll site structure
- [x] FT-inspired theme (salmon/magenta)
- [x] All content templates
- [x] AdSense integration
- [x] Sample posts for all types
- [x] Performance tracker page
- [x] Navigation and layout
- [x] Data collection scripts
- [x] Cron job for 4:00 AM runs

### 🔄 Next Steps
- [ ] Test data scripts (run manually)
- [ ] Verify first daily brief generates correctly
- [ ] Launch first trading day
- [ ] Monitor and refine

---

## 14. Future Enhancements (Post-Launch)

### Phase 2 Ideas
- Email newsletter (daily brief delivered)
- Twitter/X bot (auto-post alerts)
- Discord community
- More data sources (premium APIs)
- Real-time price widgets

### Phase 3 Ideas
- Premium tier (no ads, early access)
- User watchlists
- Alert notifications
- Portfolio tracking
- Options flow analysis

---

## 15. Questions & Decisions Log

### Decisions Made
| Date | Decision | Rationale |
|------|----------|-----------|
| Mar 28 | Use Jekyll + GitHub Pages | Free, reliable, easy to update via git |
| Mar 28 | 5:30 AM EST publish time | 2 hours before market open |
| Mar 28 | FT-inspired color scheme | Distinctive, memorable, professional |
| Mar 28 | Deep dives include fundamentals | Makes readers feel smarter, better engagement |
| Mar 28 | 4 tickers per day (not 6) | Quality over quantity, 45 min per deep dive |
| Mar 28 | 4:00 AM data collection | Gives 1.5 hour analysis window before publish |

### Open Questions
- Weekend content? (Weekly review?)
- Historical data retention policy?
- When to archive old posts?

---

## 16. Contact & Maintenance

**Site Owner:** George  
**AI Assistant:** Main Assistant  
**Update Frequency:** Daily during market hours  
**Maintenance:** Review and adjust monthly  

---

*This document will be updated as the project evolves.*
