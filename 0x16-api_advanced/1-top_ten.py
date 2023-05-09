#!/usr/bin/python3
"""
function thay queries the Reddit ApI and returns the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys

def top_ten(subreddit)
    """queries to Reddit Api"""
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    params = {
        'limit': 10
    }

     url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
     res = requests.get(url, 
                        headers=headers, 
                        params=params, 
                        allow_redirects=False)
     if res.status_code != 200:
         return 0
     dic = res.json()
     hot_posts = dic['data']['children']
     if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
