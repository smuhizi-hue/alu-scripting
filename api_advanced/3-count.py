#!/usr/bin/python3
"""
Module containing the count_words function that queries the Reddit API
recursively and counts keywords in hot post titles.
"""
import requests


def count_words(subreddit, word_list, instances={}, after=None):
    """
    Queries the Reddit API recursively, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    # Initialisation du dictionnaire d'instances au premier appel
    if not instances:
        for word in word_list:
            instances[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
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

            for post in children:
                title = post.get('data', {}).get('title', '').lower()
                # Découpage du titre par espaces pour isoler les mots exacts
                words_in_title = title.split()
                
                for word in instances.keys():
                    instances[word] += words_in_title.count(word)

            # Si une page suivante existe, on continue la récursion
            if after is not None:
                return count_words(subreddit, word_list, instances, after)
            
            # Condition de fin : tri et affichage des résultats
            # Tri principal : valeur décroissante (-x[1]), Tri secondaire : clé alphabétique (x[0])
            sorted_words = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
            
            for word, count in sorted_words:
                if count > 0:
                    print("{}: {}".format(word, count))
        else:
            return
    except Exception:
        return
