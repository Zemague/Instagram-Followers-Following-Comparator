(() => {
  const modal = document.querySelector('div[role="dialog"]');
  if (!modal) {
    console.error("⚠️ Open your Followers list (modal) first and try again.");
    return;
  }

  // Only grab spans that have the "_ap3a" class (username spans)
  const spans = Array.from(modal.querySelectorAll('span._ap3a'));
  const results = spans.map(s => s.textContent.trim()).filter(Boolean);

  // Copy plain usernames to clipboard
  copy(results);
  console.log("✅ Copied", results.length, "usernames to clipboard. Paste into Excel or a text file.");
})();
