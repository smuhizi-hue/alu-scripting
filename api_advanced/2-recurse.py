#!/usr/bin/python3
"""
Module containing the recurse function that queries the Reddit API recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing the titles
    of all hot articles for a given subreddit.
    
    If no results are found for the given subreddit, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    # Ajout des paramètres de pagination pour la requête
    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get('data', {})
            after = data.get('after', None)
            children = data.get('children', [])
            
            # Ajoute les titres de la page actuelle à notre liste accumulée
            for post in children:
                hot_list.append(post.get('data', {}).get('title'))
            
            # Condition d'arrêt : s'il n'y a plus de page suivante ('after' est None)
            if after is None:
                return hot_list
            
            # Appel récursif avec le nouveau pointeur 'after'
            return recurse(subreddit, hot_list, after)
        else:
            return None
            
    except Exception:
        return None
