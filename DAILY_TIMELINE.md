# Daily Timeline - Market Pulse Scanner

**Complete workflow from data collection to close**

---

## 📅 Full Day Schedule (EST)

### PRE-MARKET (Data Collection & Analysis)

| Time | Task | Duration | Who |
|------|------|----------|-----|
| **4:00 AM** | Cron triggers: run_all.sh executes | 15 min | Automated |
| | • market_scan.py | 5 min | Script |
| | • news_scan_v2.py | 5 min | Script |
| | • technical_screen.py | 5 min | Script |
| **4:15 AM** | Data saved to data/ directory | — | System |
| **4:15-4:45 AM** | **I analyze data** | 30 min | AI (me) |
| | • Review futures/VIX data | 5 min | |
| | • Review news signals | 10 min | |
| | • Review technical screens | 10 min | |
| | • Decision: Select 4 tickers | 5 min | |
| **4:45-5:00 AM** | **Write Daily Market Brief** | 15 min | AI (me) |
| **5:00 AM** | Publish Daily Brief | Instant | Git push |
| **5:00-5:15 AM** | Buffer/Review | 15 min | — |

---

### MORNING (Deep Dives)

| Time | Task | Duration | Output |
|------|------|----------|--------|
| **5:15 AM** | **DEEP DIVE #1** | 45 min | Article published |
| | • Research company (what they do) | 10 min | |
| | • Analyze financials | 10 min | |
| | • Review recent news/developments | 5 min | |
| | • Technical analysis | 10 min | |
| | • Write article | 10 min | |
| **6:00 AM** | Publish Deep Dive #1 | Instant | Git push |
| **6:00-6:15 AM** | Buffer/Prep next | 15 min | — |
| **6:15 AM** | **DEEP DIVE #2** | 45 min | Article published |
| **7:00 AM** | Publish Deep Dive #2 | Instant | Git push |
| **7:00-7:15 AM** | Buffer/Prep next | 15 min | — |
| **7:15 AM** | **DEEP DIVE #3** | 45 min | Article published |
| **8:00 AM** | Publish Deep Dive #3 | Instant | Git push |
| **8:00-8:15 AM** | Buffer/Prep next | 15 min | — |
| **8:15 AM** | **DEEP DIVE #4** | 45 min | Article published |
| **9:00 AM** | Publish Deep Dive #4 | Instant | Git push |

**Total pre-market: 5 hours (4:00 AM - 9:00 AM)**
**Published: 1 Daily Brief + 4 Deep Dives**

---

### MARKET HOURS (Monitoring & Updates)

| Time | Task | Duration | Output |
|------|------|----------|--------|
| **9:30 AM** | Markets open | — | — |
| **9:35 AM** | Check all 4 tickers | 5 min | Internal notes |
| | • Price vs open | | |
| | • Volume check | | |
| | • Quick news scan | | |
| **10:00 AM** | Monitor | 5 min | If significant: publish update |
| **10:30 AM** | Monitor | 5 min | If significant: publish update |
| **11:00 AM** | Monitor | 5 min | If significant: publish update |
| **11:30 AM** | Monitor | 5 min | If significant: publish update |
| **12:00 PM** | Monitor | 5 min | If significant: publish update |
| **12:30 PM** | **Write Midday Wrap** | 15 min | Article published |
| **12:45 PM** | Publish Midday Wrap | Instant | Git push |
| **1:00 PM** | Monitor | 5 min | If significant: publish update |
| **1:30 PM** | Monitor | 5 min | If significant: publish update |
| **2:00 PM** | Monitor | 5 min | If significant: publish update |
| **2:30 PM** | Monitor | 5 min | If significant: publish update |
| **3:00 PM** | Monitor | 5 min | If significant: publish update |
| **3:30 PM** | Monitor | 5 min | If significant: publish update |
| **4:00 PM** | Markets close | — | — |

---

### POST-MARKET (Summary & Prep)

| Time | Task | Duration | Output |
|------|------|----------|--------|
| **4:00-4:15 PM** | Wait for final prices | 15 min | — |
| **4:15 PM** | **Write Close Wrap** | 15 min | Article published |
| **4:30 PM** | Publish Close Wrap | Instant | Git push |
| **4:30-5:00 PM** | Final review & archive | 30 min | System |
| | • Archive data to data/archive/ | | |
| | • Update performance tracker | | |
| | • Prep tomorrow's notes | | |

**Total market hours: 7 hours (9:30 AM - 4:30 PM)**
**Published: Midday Wrap + Close Wrap (plus any hourly updates)**

---

## 📊 Daily Summary

### Content Published
| Type | Count | Time |
|------|-------|------|
| Daily Market Brief | 1 | 5:00 AM |
| Company Deep Dives | 4 | 6:00-9:00 AM |
| Hourly Updates | 0-6 | 9:35 AM-3:30 PM (as needed) |
| Midday Wrap | 1 | 12:45 PM |
| Close Wrap | 1 | 4:30 PM |
| **TOTAL** | **7-13 articles** | — |

### Time Investment
| Phase | Duration | My Involvement |
|-------|----------|----------------|
| Data Collection | 15 min | Automated (cron) |
| Analysis & Writing | 3.5 hours | Active (me) |
| Market Monitoring | 1 hour | Active (me, every 30 min) |
| Post-Market | 30 min | Active (me) |
| **TOTAL** | **~5 hours** | — |

---

## 🔔 Alert Schedule

### Automated
- **4:00 AM EST (Mon-Fri):** Data collection cron job

### Manual (by me)
- **Hourly checks:** 9:35 AM, 10:00 AM, 10:30 AM, 11:00 AM, 11:30 AM, 12:00 PM, 1:00 PM, 1:30 PM, 2:00 PM, 2:30 PM, 3:00 PM, 3:30 PM

**Only publish if:**
- Price moves >2%
- Breaking news on monitored ticker
- Technical level hit

---

## 📁 Files Created Daily

### Data Files (4:00 AM)
```
data/market/market_scan_YYYYMMDD_0400.json
data/news/news_signals_YYYYMMDD_0405.json
data/technical/technical_screen_YYYYMMDD_0410.json
```

### Article Files
```
_posts/YYYYMMDD-daily-brief.md
_posts/YYYYMMDD-[ticker1]-deep-dive.md
_posts/YYYYMMDD-[ticker2]-deep-dive.md
_posts/YYYYMMDD-[ticker3]-deep-dive.md
_posts/YYYYMMDD-[ticker4]-deep-dive.md
_posts/YYYYMMDD-midday-wrap.md
_posts/YYYYMMDD-close-wrap.md
_posts/YYYYMMDD-[ticker]-update-1.md (if needed)
_posts/YYYYMMDD-[ticker]-update-2.md (if needed)
...
```

---

## 🎯 Example Day (Monday, March 31)

**4:00 AM** - Scripts run, data collected
**4:15 AM** - I start analyzing
**4:45 AM** - Selected: SOFI, NVDA, XOM, PLTR
**5:00 AM** - Daily Brief published
**6:00 AM** - SOFI Deep Dive published
**7:00 AM** - NVDA Deep Dive published  
**8:00 AM** - XOM Deep Dive published
**9:00 AM** - PLTR Deep Dive published
**9:30 AM** - Markets open
**9:35 AM** - Check: SOFI up 1%, NVDA flat, others quiet - no update
**10:30 AM** - Check: NVDA down 3% - PUBLISH UPDATE
**12:45 PM** - Midday Wrap published
**4:30 PM** - Close Wrap published
**5:00 PM** - Day complete

---

**Ready to launch?**
