#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            if not hot_posts:
                print(None)
            for post in hot_posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
