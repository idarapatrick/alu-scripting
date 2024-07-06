#!/usr/bin/python3
"""Script that fetches the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, print None."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return
        for i in range(min(10, len(posts))):
            print(posts[i].get('data', {}).get('title', 'No title'))
    else:
        print(None)
