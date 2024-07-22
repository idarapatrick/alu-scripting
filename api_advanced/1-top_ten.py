#!/usr/bin/python3
"""Function to print hot post on a given Reddit subreddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://reddit.com/r/{}.json".format(subreddit)
    headers = {
        "User-Agent": "MyAPI/0.0.1"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
