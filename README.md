📸 Instagram Followers/Following Comparator

A simple, zero-dependency Python tool designed to compare two lists of usernames (like your Instagram followers and following lists) to quickly identify who you follow that isn't following you back.
✨ Features

    Simple Comparison: Compares two plain text files line-by-line.

    Find Non-Followers: Specifically identifies accounts you are following that do not follow you back.

    Clean Output: Generates a new, clean text file with the list of identified accounts.

    No External Libraries: Built using only standard Python functionality.

📦 Requirements

    Python 3.6+

    Two plain text files containing one Instagram username per line:

        following.txt (Accounts you follow)

        followers.txt (Accounts that follow you)

🚀 Usage
Step 1: Generate Your Username Lists

You need to scrape your followers and following lists from Instagram. This usually requires a browser extension or a specific JavaScript snippet run in the Developer Console, as detailed below.

    Open Instagram in a desktop browser and go to your profile.

    Open your Following list and scroll down until all accounts are loaded.

    Open the Developer Console (usually by pressing F12 or Right-click → Inspect → Console).

    Run your preferred JavaScript scraper to copy the list of usernames to your clipboard.

    Paste the content into a new file named following.txt.

    Repeat the process for your Followers list and save the content into a file named followers.txt.

    Note: Each file (following.txt and followers.txt) should contain one username per line.

Step 2: Place Files and Run

    Place the comparator.py script, following.txt, and followers.txt files in the same directory.

    Open your terminal or command prompt in that directory.

    Execute the script using Python:

    python comparator.py

Step 3: View Results

The script will automatically generate a new file in the same directory:

    not_following_back.txt: A list of accounts you follow that are not following you back.
