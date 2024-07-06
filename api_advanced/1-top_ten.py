#!/usr/bin/python3
# """Script that fetch 10 hot post for a given subreddit."""
# import requests


# def top_ten(subreddit):
#     """Return number of subscribers if @subreddit is valid subreddit.
#     if not return 0."""

#     headers = {'User-Agent': 'MyAPI/0.0.1'}
#     subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
#     response = requests.get(subreddit_url, headers=headers)

#     if response.status_code == 200:
#         json_data = response.json()
#         for i in range(10):
#             print(
#                 json_data.get('data')
#                 .get('children')[i]
#                 .get('data')
#                 .get('title')
#             )
#     else:
#         print(None)

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}/hot.json"
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        for i in range(min(10, len(posts))):
            print(posts[i].get('data', {}).get('title', 'No title'))
    else:
        print(None)
