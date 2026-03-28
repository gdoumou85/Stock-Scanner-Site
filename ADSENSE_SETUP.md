# AdSense Setup Instructions

**Publisher ID:** pub-4794018087983976  
**Status:** Code installed, awaiting AdSense approval and slot creation

---

## Step 1: Verify Your Site in AdSense

1. Go to https://www.google.com/adsense
2. Sign in with your Google account
3. Click "Add site" 
4. Enter: `https://gdoumou85.github.io/Stock-Scanner-Site/`
5. Follow verification steps (add meta tag or HTML file)

---

## Step 2: Create Ad Slots

Once verified, create these ad units:

### Ad Unit 1: Top Banner
- **Name:** Top Banner - Homepage
- **Type:** Display
- **Size:** Responsive (auto)
- **Ad slot ID:** Copy this ID and replace `TOP_BANNER_SLOT` in `_includes/ad-top.html`

### Ad Unit 2: In-Content
- **Name:** In-Content - Articles  
- **Type:** In-article
- **Size:** Responsive
- **Ad slot ID:** Copy this ID and replace `IN_CONTENT_SLOT` in `_includes/ad-incontent.html`

### Ad Unit 3: Sidebar (Optional)
- **Name:** Sidebar - Desktop
- **Type:** Display
- **Size:** 300x600 or Responsive
- **Ad slot ID:** Copy and create `_includes/ad-sidebar.html`

---

## Step 3: Update Code with Real Slot IDs

After creating ad units, update these files:

**File:** `_includes/ad-top.html`
```html
data-ad-slot="ca-pub-4794018087983976"  <!-- Replace with your slot ID -->
```

**File:** `_includes/ad-incontent.html`
```html
data-ad-slot="ca-pub-4794018087983976"  <!-- Replace with your slot ID -->
```

---

## Step 4: Submit for Review

1. In AdSense, submit site for review
2. Wait 1-2 weeks for approval
3. Once approved, ads will start showing

---

## Current Status

✅ **Code installed** - AdSense script in head  
✅ **Publisher ID configured** - pub-4794018087983976  
⏳ **Awaiting:** Site verification  
⏳ **Awaiting:** Ad slot creation  
⏳ **Awaiting:** AdSense approval  

---

## Where Ads Appear

**Daily Brief:**
- After introduction paragraph (in-content)
- Before conclusion (in-content)

**Deep Dives:**
- After company overview (in-content)
- Before trade setup section (in-content)

**Weekend Articles:**
- After first section (in-content)
- Before conclusion (in-content)

**Homepage:**
- Sidebar (desktop only)

---

## Ad Placement Strategy

- **Non-intrusive** - Between content sections
- **Natural breaks** - Where reader pauses
- **No popups** - Clean reading experience
- **Responsive** - Works on mobile/desktop

---

## Notes

- Don't click your own ads (violates terms)
- Keep content high quality (required for approval)
- Review takes 1-14 days typically
- Can launch site now, ads appear after approval

---

**Next Steps:**
1. Verify site in AdSense
2. Create ad units
3. Update slot IDs in code
4. Submit for review
5. Launch content
