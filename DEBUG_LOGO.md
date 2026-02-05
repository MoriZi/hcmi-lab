# Logo Debugging Guide

## How to Open Browser DevTools

**Chrome/Edge:**
- Press `F12` or `Cmd+Option+I` (Mac) / `Ctrl+Shift+I` (Windows)
- Or right-click → "Inspect"

**Firefox:**
- Press `F12` or `Cmd+Option+I` (Mac) / `Ctrl+Shift+I` (Windows)

**Safari:**
- Enable Developer menu: Preferences → Advanced → "Show Develop menu"
- Then `Cmd+Option+I`

---

## 1. Console Tab (JavaScript Errors)

**What to look for:**
- Red error messages
- Any warnings about images not loading
- JavaScript errors related to logo injection

**What to share:**
- Copy any red error messages
- Screenshot of the Console tab if there are errors

**Steps:**
1. Open DevTools → Click "Console" tab
2. Refresh the page (`Cmd+R` or `Ctrl+R`)
3. Look for any red error messages
4. Copy and paste any errors you see

---

## 2. Network Tab (File Loading)

**What to look for:**
- Check if logo files are loading (200 = success, 404 = not found)
- See what path the browser is trying to load
- Check the actual URL being requested

**What to share:**
- Screenshot of Network tab filtered by "img" or "media"
- List of any 404 errors for logo/icon files
- The actual URL paths being requested

**Steps:**
1. Open DevTools → Click "Network" tab
2. Filter by "Img" or type "icon" or "logo" in the filter box
3. Refresh the page (`Cmd+R` or `Ctrl+R`)
4. Look for:
   - `icon.png` or `icon_hu_*.png` files
   - `hcmiLogo.png` files
   - Check status codes (200 = OK, 404 = Not Found, etc.)
5. Click on any logo-related files to see:
   - Request URL (what path was requested)
   - Response (if it loaded)
   - Headers (content type, etc.)

---

## 3. Elements/Inspector Tab (HTML Structure)

**What to look for:**
- The actual HTML structure of the navbar
- What `<img>` tags exist (if any)
- The `src` attribute of any logo images
- CSS classes on navbar elements

**What to share:**
- Screenshot of the navbar HTML structure
- Copy the HTML of the navbar-brand element
- The `src` attribute of any logo images you see

**Steps:**
1. Open DevTools → Click "Elements" (Chrome) or "Inspector" (Firefox) tab
2. Click the "Select element" tool (cursor icon in top-left)
3. Click on the navbar area (where logo should be)
4. Look for:
   - `<a class="navbar-brand">` element
   - Any `<img>` tags inside it
   - The `src` attribute of images
5. Right-click the navbar-brand element → "Copy" → "Copy outerHTML"
6. Share that HTML code

---

## 4. Application Tab (Cached Files)

**What to look for:**
- Cached versions of old logo files
- Service worker cache (if any)

**Steps:**
1. Open DevTools → Click "Application" tab (Chrome) or "Storage" tab (Firefox)
2. Look under "Cache Storage" or "Images"
3. Check if old icon files are cached
4. You can clear cache here: Right-click → "Clear"

---

## Quick Checklist - What to Share:

1. **Console errors:** Any red error messages
2. **Network tab screenshot:** Filter by "img" showing logo file requests
3. **HTML structure:** Copy the `<a class="navbar-brand">` element HTML
4. **Image URLs:** The actual `src` attribute of any logo images
5. **404 errors:** Any files that return 404 (not found)

---

## Example of What to Share:

```
Console Errors:
- (none, or paste any errors here)

Network Tab - Logo Files:
- /images/icon.png - Status: 200 OK
- /media/icon_hu_b2d7953d71c2c6f3.png - Status: 404 Not Found

Navbar HTML:
<a class="navbar-brand" href="/">
  HCMI Lab
</a>
(no <img> tag found)

Image src attributes:
- (none found, or paste the src here)
```

---

## Quick Fixes to Try:

1. **Hard refresh:** `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
2. **Clear cache:** DevTools → Application → Clear storage → Clear site data
3. **Disable cache:** DevTools → Network tab → Check "Disable cache" checkbox
4. **Restart Hugo:** Stop and restart your Hugo server

