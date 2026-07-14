import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the 
    first 10 hot posts for a given subreddit.
    """
    url = f"https://reddit.com{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'limit': 10}

    try:
        # allow_redirects=False handles invalid subreddits that redirect to search
        response = requests.get(url, headers=headers, params=params, 
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            for post in data:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
            
    except Exception:
        print(None)
