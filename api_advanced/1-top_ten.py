#!/usr/bin/python3
"""Script that fetches the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = (
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    )

    try:
        response = requests.get(subreddit_url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            if not posts:
                print(None)
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
