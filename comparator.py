def load_list_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

def main():
    # Input files
    following_file = "following.txt"  # the accounts you follow
    followers_file = "followers.txt"  # the accounts who follow you

    # Load sets
    following = load_list_from_file(following_file)
    followers = load_list_from_file(followers_file)

    # Compute difference
    not_following_back = sorted(following - followers)

    # Save to file
    with open("not_following_back.txt", "w", encoding="utf-8") as f:
        for user in not_following_back:
            f.write(user + "\n")

    # Print summary
    print(f"Found {len(not_following_back)} accounts you follow who don't follow back.")
    print("Saved to not_following_back.txt")

if __name__ == "__main__":
    main()
