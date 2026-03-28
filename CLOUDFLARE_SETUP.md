# Cloudflare Pages Setup

## Option A: Git Integration (Auto-deploy)
**URL:** https://dash.cloudflare.com/ → Pages → Create project

**Steps:**
1. Connect GitHub account
2. Select `Stock-Scanner-Site` repo
3. Build settings:
   - Framework: Jekyll
   - Build command: `jekyll build`
   - Build output: `_site`
4. Deploy

**Note:** If Git connection fails again, try:
- Different browser (Chrome incognito)
- Clear cookies for cloudflare.com and github.com
- Or use Option B below

---

## Option B: Direct Upload (API Access)
**Best for automation** — I can deploy via API without Git

**Steps:**
1. Create Pages project manually
2. Get API token from Cloudflare
3. I use API to upload files directly
4. Auto-deploys on every update

**Advantages:**
- No Git OAuth issues
- I control deployments
- Works with my cron jobs

---

## Option C: Workers + KV (Advanced)
Serve site from Cloudflare Workers with KV storage
- Very fast
- Programmatic access
- More complex setup

---

## Recommendation: Try Option A First

Go to https://dash.cloudflare.com/ and try creating a Pages project again.

**If Git fails again** → we'll use Option B (API upload)

**Ready to try?** Let me know if Git connects or if you need the API approach.
