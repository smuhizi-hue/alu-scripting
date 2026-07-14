#!/usr/bin/python3
"""Module that queries the Reddit API."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x1.hot.posts:v1.0.0 (by /u/your_username)"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json()["data"]["children"]
    except (KeyError, ValueError):
        print(None)
        return

    if not results:
        print(None)
        return

    for post in results:
        print(post["data"]["title"])
