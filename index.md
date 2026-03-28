---
layout: home
---

# Market Pulse Scanner

## Daily Market Analysis & Stock Monitoring

Welcome to Market Pulse. We publish daily market briefs at 5:30 AM EST, deep research on selected stocks throughout the morning, and hourly updates while markets are open.

---

## Latest Analysis

<ul class="post-list">
  {% for post in site.posts limit:10 %}
    <li>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <span class="post-meta">{{ post.date | date: "%B %d, %Y at %I:%M %p EST" }}</span>
      {%- if post.tags -%}
      <div class="post-tags">
        {%- for tag in post.tags limit:3 -%}
          <span class="tag">{{ tag }}</span>
        {%- endfor -%}
      </div>
      {%- endif -%}
    </li>
  {% endfor %}
</ul>

---

## What We Offer

**Daily Market Brief (5:30 AM EST)**
Overnight market recap, key headlines with sources, macro data, and 5-6 stocks to watch for the day.

**Deep Dive Research (6:00-8:30 AM EST)**
Detailed analysis of each selected ticker. Business overview, financial health, technical setup, and monitoring plan.

**Hourly Updates (9:30 AM - 4:00 PM EST)**
Price action, news flow, and analysis while markets are open.

**Midday & Close Wrap**
Morning performance review and end-of-day summary.

---

## Current Active Monitors

See our [Performance Tracker](/performance/) for real-time updates on all active positions.

---

*Last site update: {{ site.time | date: "%B %d, %Y" }}*

**Disclaimer:** This site provides market analysis for informational purposes only. It is not financial advice. Always do your own research before making investment decisions. Past performance does not guarantee future results.

---

*Powered by automated market scanning + AI-assisted commentary*
