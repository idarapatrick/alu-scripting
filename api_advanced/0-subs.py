# #!/usr/bin/python3
# """Return number of subscribers for a given subreddit"""
# import requests


# def number_of_subscribers(subreddit):
#     """Return the number of subscribers """
#     url = "https://www.reddit.com/r/{}/about.json" \
#         .format(subreddit)
#     headers = {'User-Agent': 'My User Agent 1.0'}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json().get('data') \
#             .get('subscribers')
#     return 0

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    return 0
