#!/usr/bin/python3
"""
Module containing the top_ten function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Le checker requiert une vérification stricte du code 200
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            
            for post in children:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
