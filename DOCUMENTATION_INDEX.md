# Market Pulse Scanner - Complete Documentation Index

**Last Updated:** March 28, 2026  
**Status:** Ready for Launch

---

## 📚 Documentation Files

### Core Documentation
| File | Purpose | Location |
|------|---------|----------|
| **PROJECT_PLAN.md** | Complete project overview, strategy, workflows | `/PROJECT_PLAN.md` |
| **DAILY_TIMELINE.md** | Hour-by-hour daily schedule | `/DAILY_TIMELINE.md` |
| **DEPLOYMENT.md** | GitHub credentials, deployment commands | `/DEPLOYMENT.md` |
| **README.md** | Basic project intro | `/README.md` |

### Content Templates
| File | Purpose | Location |
|------|---------|----------|
| **daily-brief-template.md** | 5:30 AM market brief | `/_templates/` |
| **company-deep-dive.md** | Full fundamental analysis | `/_templates/` |
| **hourly-update.md** | Live ticker updates | `/_templates/` |
| **midday-wrap.md** | 12:30 PM summary | `/_templates/` |
| **close-wrap.md** | 4:30 PM end of day | `/_templates/` |
| **week-in-review.md** | Saturday weekly summary | `/_templates/` |
| **week-ahead-preview.md** | Sunday preview | `/_templates/` |
| **market-holiday.md** | Holiday notices | `/_templates/` |

### Automation Scripts
| File | Purpose | Schedule |
|------|---------|----------|
| **run_all.sh** | Master data collection script | 4:00 AM EST (Mon-Fri) |
| **market_scan.py** | Futures, VIX, sectors, indices | 4:00 AM EST |
| **news_scan_v2.py** | Headlines, sentiment, signals | 4:05 AM EST |
| **technical_screen.py** | 80+ stocks technical scan | 4:10 AM EST |
| **generate_week_review_v2.py** | Saturday narrative review | Manual (Saturday) |

### Data Storage
```
data/
├── market/          # Daily market scans
├── news/            # News signals and headlines  
├── technical/       # Technical screens
└── archive/         # Weekly archived data
```

### Site Structure
```
stock-scanner-site/
├── _config.yml              # Site configuration
├── _posts/                  # Published articles
├── _layouts/                # Page templates
├── _includes/               # Header, footer, ads
├── _templates/              # Article templates
├── assets/
│   └── main.scss           # FT-inspired theme
├── scripts/                 # Data collection
└── data/                    # Market data
```

---

## 🎯 Quick Reference: What Happens When

### Weekdays (Monday-Friday)
| Time (EST) | Event | Output |
|------------|-------|--------|
| **4:00 AM** | Cron runs: Data collection | 3 JSON files saved |
| **4:15 AM** | **I analyze data** | Select 4 tickers |
| **5:00 AM** | Publish Daily Brief | 1 article |
| **5:15-9:00 AM** | Write 4 Deep Dives | 4 articles (1 every 45 min) |
| **9:30 AM** | Markets open | — |
| **9:35 AM-3:30 PM** | Hourly monitoring | 0-2 update articles |
| **12:45 PM** | Publish Midday Wrap | 1 article |
| **4:30 PM** | Publish Close Wrap | 1 article |
| **Total** | — | **7-11 articles/day** |

### Weekend
| Day | Event | Output |
|-----|-------|--------|
| **Saturday** | Week in Review | 1 narrative article |
| **Sunday** | Week Ahead Preview | 1 preview article |

### Market Holidays
| Event | Output |
|-------|--------|
| Markets closed | Holiday greeting post |

---

## 🔄 Complete Workflow

### Pre-Market (4:00 AM - 9:30 AM EST)

**Step 1: Data Collection (Automated)**
- `run_all.sh` executes
- Fetches futures, news, technical screens
- Saves to `data/` directory

**Step 2: Analysis (4:15 AM - 4:45 AM)**
- I review market data (bias: bullish/bearish?)
- I review news signals (catalysts? earnings?)
- I review technical screens (setups)
- **Decision:** Select 4 tickers

**Step 3: Write Daily Brief (4:45 AM - 5:00 AM)**
- Summarize overnight action
- Present 4 selected tickers
- Explain why each chosen

**Step 4: Write Deep Dives (5:15 AM - 9:00 AM)**
- For each of 4 tickers:
  - Research company (what they do)
  - Analyze financials (revenue, margins, debt)
  - Review recent developments
  - Technical analysis
  - Investment thesis (bull/bear cases)
  - Trade setup (entry, stop, targets)
- Publish immediately when done

### Market Hours (9:30 AM - 4:00 PM EST)

**Hourly Monitoring**
- Check prices on 4 tickers
- Scan for news
- **Only publish if:** >2% move OR breaking news

**Scheduled Posts**
- 12:30 PM: Midday Wrap
- 4:30 PM: Close Wrap

### Weekend

**Saturday**
- Archive week's data
- Generate Week in Review (narrative style)
- Honest performance review + lessons learned

**Sunday**
- Week Ahead Preview
- Economic calendar
- Earnings schedule
- Key levels for week

---

## 📝 Content Types Explained

### Daily Market Brief
**When:** 5:30 AM EST  
**Length:** 5-6 min read  
**Content:** Overnight markets, macro data, 4-6 tickers to watch  
**Tone:** Professional, sets the stage for the day

### Company Deep Dive
**When:** 6:00-9:00 AM EST (one every 45 min)  
**Length:** 8-12 min read  
**Content:** Full company analysis (business, financials, technicals, thesis)  
**Tone:** Educational, makes readers feel like experts

### Hourly Update
**When:** As needed (9:35 AM - 3:30 PM)  
**Length:** 1-2 min read  
**Content:** Price action, news, quick take  
**Tone:** Quick, punchy, actionable

### Midday Wrap
**When:** 12:30 PM EST  
**Length:** 3 min read  
**Content:** Morning performance, winners/losers, afternoon outlook  
**Tone:** Summary, forward-looking

### Close Wrap
**When:** 4:30 PM EST  
**Length:** 3 min read  
**Content:** Final numbers, day summary, tomorrow setup  
**Tone:** Recap, sets up next day

### Week in Review (Saturday)
**When:** 10:00 AM EST Saturday  
**Length:** 8-10 min read  
**Content:** Week's themes, our performance, lessons learned  
**Tone:** Narrative, reflective, honest

### Week Ahead Preview (Sunday)
**When:** 10:00 AM EST Sunday  
**Length:** 5-6 min read  
**Content:** Economic calendar, earnings, key levels, themes to watch  
**Tone:** Preview, preparatory

---

## 🎨 Design System

**Colors (FT-Inspired):**
- Header: `#9b1648` (Magenta)
- Background: `#fff1e5` (Salmon/Cream)
- Text: `#333333` (Dark)
- Accent: `#0d7680` (Teal)
- Green: `#00875f`
- Red: `#cc0000`

**Typography:**
- Headings: Georgia, serif
- Body: Georgia, serif  
- UI elements: System sans-serif

**Layout:**
- Max width: 1200px
- Main content: ~800px
- Sidebar: 300px
- Mobile: Single column

---

## 🚀 Deployment

**Live Site:** https://gdoumou85.github.io/Stock-Scanner-Site/

**Repository:** https://github.com/gdoumou85/Stock-Scanner-Site

**Update Process:**
1. Edit files locally
2. `git add .`
3. `git commit -m "Description"`
4. `git push origin main`
5. GitHub Actions builds and deploys (1-2 minutes)

---

## 💰 Monetization

**AdSense ID:** pub-4794018087983976  
**Placements:**
- Between Daily Brief sections
- In-content on long articles
- Sidebar (desktop only)

---

## ⚙️ Cron Jobs

**Active:**
- `b6fae2aa-b933-416a-8c53-3b1ca5ace780` — Daily data collection, 4:00 AM EST Mon-Fri

**Removed (old SOFI jobs):**
- SOFI price alerts (removed)
- SOFI news monitor (removed)
- Opportunity watchlist (removed)

---

## 📊 Data Workflow

### Collection (4:00 AM EST)
**Scripts:** `run_all.sh`
- `market_scan.py` — 15 tickers (futures, sectors, indices)
- `news_scan_v2.py` — Headlines, sentiment, signals
- `technical_screen.py` — 80+ stocks screened

**Output:** 3 JSON files in `data/[market|news|technical]/`

### Analysis (4:15 AM)
**I read:**
- `data/market/latest.json` — Market direction
- `data/news/latest.json` — Catalysts, signals
- `data/technical/latest.json` — Screened setups

**I decide:** 4 tickers for deep dives

### Archival (Saturday)
**Script:** `generate_week_review_v2.py`
- Reads week's data
- Calculates performance
- Generates narrative review
- Archives to `data/archive/week_YYYYMMDD/`

---

## 🎯 Success Metrics

### Content
- 7-11 articles per trading day
- 2 weekend articles
- Win rate tracked honestly
- Quality over quantity

### Technical
- Site uptime: 99%+
- Build time: <2 minutes
- Page load: <2 seconds

### Business
- AdSense impressions
- Reader engagement (time on site)
- Return visitors

---

## 🔄 Maintenance Schedule

**Daily:**
- Content creation (5 hours active work)
- Data monitoring during market hours

**Weekly:**
- Saturday: Archive data, publish review
- Sunday: Publish preview

**Monthly:**
- Review performance metrics
- Refine ticker selection criteria
- Update templates if needed
- Archive old posts

---

## 📝 Change Log

| Date | Change | Notes |
|------|--------|-------|
| Mar 28 | Initial setup | Site created, theme applied |
| Mar 28 | Data pipeline | Scripts created, cron job added |
| Mar 28 | Weekend content | Week in Review, Week Ahead templates |
| Mar 28 | Documentation | All docs written and organized |

---

## ❓ Frequently Asked Questions

**Q: Why 4 tickers per day, not 6?**  
A: Quality over quantity. 45 minutes per deep dive allows proper research.

**Q: Why US markets?**  
A: Most liquid, best data availability, free APIs work well.

**Q: What if no good setups?**  
A: Publish fewer tickers or focus on market analysis. Never force trades.

**Q: How do you handle earnings?**  
A: Earnings plays are high priority if technical setup aligns.

**Q: What about short selling?**  
A: Always include at least one bearish/short candidate when market conditions warrant.

---

## 🎓 Learning Resources

**For Readers:**
- Educational deep dives explain companies thoroughly
- Glossaries for technical terms
- Risk management emphasized

**For Development:**
- Jekyll documentation: https://jekyllrb.com/
- GitHub Pages: https://pages.github.com/
- Yahoo Finance API (unofficial)

---

## 📞 Contact

**Site:** Market Pulse Scanner  
**Owner:** George  
**AI Assistant:** Main Assistant  
**Email:** [Set up if needed]

---

*This documentation will be updated as the project evolves.*

**Last Updated:** March 28, 2026
