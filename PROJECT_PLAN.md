# Market Pulse Scanner - Project Plan

**Last Updated:** March 28, 2026
**Status:** Ready for Deployment

---

## 1. Project Overview

### Vision
Create an automated stock market analysis website that publishes daily research on selected tickers. The site combines AI-assisted analysis with market data to identify opportunities worth monitoring.

### Monetization
Google AdSense integration (Publisher ID: pub-4794018087983976)

### Key Principles
- **Transparency:** AI-assisted analysis, clearly disclosed
- **Quality over quantity:** Selective ticker picking, not spray-and-pray
- **Accessibility:** Plain language, no trader jargon
- **Multi-day tracking:** Tickers can be monitored for days, not just hours
- **Source diversity:** Multiple news sources, rotated periodically

---

## 2. Content Strategy

### Publishing Schedule (All times EST)

| Content | Time | Frequency | Description |
|---------|------|-----------|-------------|
| **Daily Market Brief** | 5:30 AM | Mon-Fri | Overnight recap, macro data, 5-6 tickers to watch |
| **Deep Dive #1** | 6:00 AM | Daily | First ticker full analysis |
| **Deep Dive #2** | 6:30 AM | Daily | Second ticker full analysis |
| **Deep Dive #3** | 7:00 AM | Daily | Third ticker full analysis |
| **Deep Dive #4** | 7:30 AM | Daily | Fourth ticker full analysis |
| **Deep Dive #5** | 8:00 AM | Daily | Fifth ticker full analysis |
| **Deep Dive #6** | 8:30 AM | As needed | Optional sixth ticker |
| **Hourly Update** | 9:30 AM - 4:00 PM | Every 1 hour | Live price action for active tickers |
| **Midday Wrap** | 12:30 PM | Daily | Morning performance summary |
| **Close Wrap** | 4:30 PM | Daily | Final numbers, tomorrow setup |

### Content Types

#### A. Daily Market Brief (5-7 min read)
**Sections:**
- Overnight global snapshot (US, Europe, Asia)
- Key macro data points
- Today's watchlist (6 tickers with 2-3 sentences each)
- Important events calendar
- Key support/resistance levels
- My take (1-2 paragraph summary)

**Tone:** Professional but accessible. Explain why things matter.

#### B. Ticker Deep Dive (4-5 min read)
**Sections:**
- Company basics (what they do)
- Why we are watching (the setup)
- Financial health (revenue, growth, profitability)
- What could go right (bull case)
- What could go wrong (bear case)
- Trade setup (entry, stop, targets)
- Monitoring plan (update frequency, key levels)

**Note:** Each ticker gets ONE deep dive post. Hourly updates link back to this.

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

## 3. Technical Setup

### Platform
- **Static Site Generator:** Jekyll
- **Hosting:** GitHub Pages (free)
- **Domain:** GitHub Pages subdomain initially, custom domain optional
- **Theme:** Custom dark financial theme (modern, mobile-first)

### Repository Structure
```
stock-scanner-site/
├── _config.yml              # Site config + AdSense ID
├── Gemfile                  # Dependencies
├── index.md                 # Homepage
├── performance.md           # Live tracker page
├── archive.md              # All posts archive
├── _posts/                 # All content (dated)
│   ├── YYYY-MM-DD-daily-brief.md
│   ├── YYYY-MM-DD-[ticker]-deep-dive.md
│   ├── YYYY-MM-DD-[ticker]-update-N.md
│   ├── YYYY-MM-DD-midday-wrap.md
│   └── YYYY-MM-DD-close-wrap.md
├── _layouts/               # Page templates
│   ├── default.html
│   ├── home.html
│   ├── post.html
│   └── page.html
├── _includes/              # Reusable components
│   ├── head.html
│   ├── header.html
│   ├── footer.html
│   ├── ad-top.html
│   ├── ad-incontent.html
│   └── ad-sidebar.html
└── assets/
    └── main.scss           # Custom dark theme
```

### AdSense Integration
- **Publisher ID:** pub-4794018087983976
- **Ad Types:** Display (horizontal), In-content (article), Sidebar (vertical)
- **Placement:** Non-intrusive, between sections, not disruptive

### Design Features
- Dark theme (easy on eyes, financial aesthetic)
- Card-based layouts
- Responsive (mobile-first)
- Clean tables for data
- Tag system for categorization
- Sticky navigation

---

## 4. Content Workflow

### My Daily Routine (Automated via Cron)

**5:00 AM EST - Pre-Market Prep**
1. Fetch futures data (S&P, Nasdaq, Dow)
2. Scan overnight news (Bloomberg, Reuters, CNBC)
3. Review Asian/European market closes
4. Check economic calendar for the day
5. Scan 50+ tickers for technical setups

**5:00-5:30 AM EST - Write Daily Brief**
- Summarize global markets
- Select 5-6 tickers for the day
- Write macro analysis
- Publish post

**5:30-8:30 AM EST - Deep Dives (One by One)**
For each selected ticker:
1. Research company fundamentals
2. Check recent news
3. Analyze technical levels
4. Write deep dive post
5. Publish immediately (don't batch)
6. Move to next ticker

**9:30 AM EST - Market Open**
- Begin hourly monitoring
- Check price action on all active tickers
- Scan for news flow

**9:35 AM, 10:35 AM, 11:35 AM... - Hourly Updates**
- Write update if significant move (>1%) or news
- Skip if quiet ("no update" is okay)
- Focus on actionable insights

**12:30 PM EST - Midday Wrap**
- Summarize morning performance
- Identify winners/losers
- Set afternoon expectations

**4:30 PM EST - Close Wrap**
- Final numbers for all tickers
- Day summary
- Tomorrow preview

**Post-Close:**
- Update performance tracker
- Prep for next day

### Multi-Day Monitoring
Some tickers will be tracked for multiple days:
- SOFI (current position) - ongoing
- Earnings plays - 2-3 days
- Technical setups - until target hit or stop triggered

**How it works:**
- First day: Full deep dive + hourly updates
- Subsequent days: Brief morning check-in + hourly updates
- New deep dive only if thesis changes significantly

---

## 5. Ticker Selection Criteria

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
2. Identify 10-15 candidate tickers
3. Rank by setup quality
4. Select top 5-6
5. Ensure diversity (don't pick 6 tech stocks)

---

## 6. News Sources

### Primary Sources
- Bloomberg
- Reuters
- CNBC
- Wall Street Journal
- Financial Times
- Benzinga
- MarketWatch
- Seeking Alpha

### Rotation
- Check new sources every few days
- Add promising ones to rotation
- Drop ones with poor accuracy or paywalls

### Source Attribution
Every headline gets linked to source. Build trust through transparency.

---

## 7. Performance Tracking

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

## 8. Risk Management

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

## 9. Current Status

### ✅ Completed
- [x] Jekyll site structure
- [x] Custom dark theme
- [x] All content templates
- [x] AdSense integration
- [x] Sample posts for all types
- [x] Performance tracker page
- [x] Navigation and layout

### 🔄 Next Steps
- [ ] Create GitHub repository
- [ ] Push files to repo
- [ ] Enable GitHub Pages
- [ ] Configure custom domain (optional)
- [ ] Set up cron jobs for automated publishing
- [ ] Test first daily brief manually
- [ ] Launch

---

## 10. Future Enhancements (Post-Launch)

### Phase 2 Ideas
- Email newsletter (daily brief delivered)
- Twitter/X bot (auto-post alerts)
- Discord community
- Mobile app
- Real-time price widgets
- Backtesting system
- More sectors (crypto, forex, international)

### Phase 3 Ideas
- Premium tier (no ads, early access)
- User watchlists
- Alert notifications
- Portfolio tracking
- Options flow analysis

---

## 11. Questions & Decisions Log

### Decisions Made
| Date | Decision | Rationale |
|------|----------|-----------|
| Mar 28 | Use Jekyll + GitHub Pages | Free, reliable, easy to update via git |
| Mar 28 | 5:30 AM EST publish time | 2 hours before market open, allows digestion |
| Mar 28 | Hourly updates (not 30-min) | Quality over quantity, less noise |
| Mar 28 | Multi-day monitoring | Real positions take time to develop |
| Mar 28 | Plain language tone | Accessible to non-traders |
| Mar 28 | 5-6 tickers per day | Manageable workload, focused coverage |

### Open Questions
- Should we add a weekend weekly review post?
- Do we want email subscriptions?
- Should we track paper trades vs just analysis?
- What happens to old posts? (Archive vs delete?)

---

## 12. Contact & Maintenance

**Site Owner:** George  
**AI Assistant:** Main Assistant  
**Update Frequency:** Daily during market hours  
**Maintenance:** Review and adjust monthly  

---

*This document will be updated as the project evolves.*
