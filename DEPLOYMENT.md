# Deployment Configuration

**Generated:** March 28, 2026

---

## Repository Details

| Setting | Value |
|---------|-------|
| **GitHub Username** | gdoumou85 |
| **Repository Name** | Stock-Scanner-Site |
| **Repository URL** | https://github.com/gdoumou85/Stock-Scanner-Site |
| **SSH Key File** | ~/.ssh/stock_scanner_deploy |
| **SSH Key Type** | ed25519 |
| **SSH Public Key** | ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAPrGHxJYkYIpm4OvguRQWJymXiLWoiz1IvCyZ0WPJc6 stock-scanner-deploy |

---

## Site URLs

| Environment | URL |
|-------------|-----|
| **GitHub Pages Site** | https://gdoumou85.github.io/Stock-Scanner-Site/ |
| **Custom Domain** | (not configured - optional) |

---

## AdSense Configuration

| Setting | Value |
|---------|-------|
| **Publisher ID** | pub-4794018087983976 |
| **Status** | Pending first pageview verification |

---

## Deployment Commands

### Push Updates
```bash
cd ~/.openclaw/workspace/projects/stock-scanner-site
GIT_SSH_COMMAND="ssh -i ~/.ssh/stock_scanner_deploy -o StrictHostKeyChecking=no" git push origin main
```

### Force Push (if needed)
```bash
cd ~/.openclaw/workspace/projects/stock-scanner-site
GIT_SSH_COMMAND="ssh -i ~/.ssh/stock_scanner_deploy -o StrictHostKeyChecking=no" git push -f origin main
```

---

## GitHub Pages Settings

**Enabled:** Yes
**Source:** main branch / (root)
**Build Status:** Auto-builds on every push

---

## Future Update Workflow

1. **Local Changes:** Edit files in `~/.openclaw/workspace/projects/stock-scanner-site/`
2. **Commit:** `git add . && git commit -m "Description of changes"`
3. **Push:** Use SSH command above
4. **Verify:** Check https://gdoumou85.github.io/Stock-Scanner-Site/ (takes 1-2 minutes)

---

## Important Notes

- **SSH Key Location:** `~/.ssh/stock_scanner_deploy` (private) and `~/.ssh/stock_scanner_deploy.pub` (public)
- **Deploy Key on GitHub:** Located at Repository Settings → Deploy keys
- **Write Access:** Enabled (required for pushing)
- **Theme:** Jekyll with custom dark financial theme
- **Build Time:** Typically 1-2 minutes after push

---

## Troubleshooting

**If push fails:**
- Check SSH key exists: `ls ~/.ssh/stock_scanner_deploy`
- Verify deploy key is still active on GitHub
- Try force push if non-fast-forward rejected

**If site doesn't update:**
- Check GitHub Actions tab for build errors
- Verify Pages settings haven't changed
- Clear browser cache (hard refresh)

---

*Keep this file secure - it contains deployment credentials.*
