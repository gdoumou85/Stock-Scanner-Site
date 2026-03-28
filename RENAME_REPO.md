# Rename Repository for AdSense

## Steps to Fix AdSense Verification

### Step 1: Create New Repository
1. Go to https://github.com/new
2. **Repository name:** `gdoumou85.github.io`
3. **Make it:** Public
4. **Add README:** No (we'll push everything)
5. Click **Create repository**

### Step 2: Update Local Git Remote
```bash
cd ~/.openclaw/workspace/projects/stock-scanner-site
git remote remove origin
git remote add origin git@github.com:gdoumou85/gdoumou85.github.io.git
```

### Step 3: Push to New Repo
```bash
GIT_SSH_COMMAND="ssh -i ~/.ssh/stock_scanner_deploy -o StrictHostKeyChecking=no" git push -u origin main
```

### Step 4: Enable GitHub Pages
1. Go to: https://github.com/gdoumou85/gdoumou85.github.io/settings/pages
2. **Source:** GitHub Actions
3. Save

### Step 5: Update Site URL
Update `_config.yml`:
```yaml
url: "https://gdoumou85.github.io"
baseurl: ""  # Remove the /Stock-Scanner-Site part
```

### Step 6: AdSense Verification
Now verify with: `https://gdoumou85.github.io`

---

## Result

**Old URL:** `https://gdoumou85.github.io/Stock-Scanner-Site/`  
**New URL:** `https://gdoumou85.github.io`

The new URL is clean and works with AdSense verification.

---

## Alternative: Keep Current Repo

If you don't want to rename, we can:
1. Create a simple index.html at the root (`gdoumou85.github.io` repo)
2. That file redirects to `/Stock-Scanner-Site/`
3. Put AdSense meta tag in the root index.html

**Which do you prefer?**
- A) Rename repo (cleaner URL)
- B) Create redirect page (keep current setup)
