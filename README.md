# 📸 Instagram Followers/Following Comparator

A simple, zero-dependency Python tool designed to compare two lists of usernames (like your Instagram followers and following lists) to quickly identify who you follow that isn't following you back.

---

## ✨ Features
- **Simple Comparison:** Compares two plain text files line-by-line.  
- **Find Non-Followers:** Specifically identifies accounts you are following that do not follow you back.  
- **Clean Output:** Generates a new, clean text file with the list of identified accounts.  
- **No External Libraries:** Built using only standard Python functionality.  

---

## 📦 Requirements
- Python 3.6+  
- Two plain text files containing one Instagram username per line:  
  - `following.txt` (Accounts you follow)  
  - `followers.txt` (Accounts that follow you)  

---

## 🚀 Usage

### Step 1: Generate Your Username Lists
You need to scrape your followers and following lists from Instagram. This usually requires a browser extension or a specific JavaScript snippet run in the Developer Console.

1. Open Instagram in a desktop browser and go to your profile.  
2. Open your **Following** list and scroll down until all accounts are loaded.  
3. Open the Developer Console (usually by pressing F12 or Right-click → Inspect → Console).  
4. Run the following JavaScript scraper to copy the list of usernames to your clipboard:

```javascript
(() => {
  const modal = document.querySelector('div[role="dialog"]');
  if (!modal) {
    console.error("⚠️ Open your Followers/Following list (modal) first and try again.");
    return;
  }

  // Only grab spans that have the "_ap3a" class (username spans)
  const spans = Array.from(modal.querySelectorAll('span._ap3a'));
  const results = spans.map(s => s.textContent.trim()).filter(Boolean);

  // Copy plain usernames to clipboard
  copy(results);
  console.log("✅ Copied", results.length, "usernames to clipboard. Paste into Excel or a text file.");
})();
````
5. Paste the content into a new file named `following.txt`.  
6. Repeat the process for your **Followers** list and save the content into a file named `followers.txt`.  
> **Note:** Each file (`following.txt` and `followers.txt`) should contain one username per line.  

---

### Step 2: Run the Script
1. **Preparation:** Ensure the three core files—the Python script (`comparator.py`), your list of accounts you follow (`following.txt`), and your list of followers (`followers.txt`)—are all located in the same folder.  
2. **Open and Navigate:**  
   - Open your Terminal (macOS/Linux) or Command Prompt / PowerShell (Windows).  
   - Use the `cd` command to navigate to the exact directory where you placed the files.  
   - Example: `cd ~/Desktop/InstaCheck`  
3. **Execute the Comparator:** Run the script using Python:  
   ```bash
   python comparator.py```

---

### Step 3: View Results

The script will automatically generate a new file in the same directory:

- `not_following_back.txt`: A clean, sorted list of accounts you follow that are not following you back.

---
Author: Zemague  
Date: 02/10/2025
---

