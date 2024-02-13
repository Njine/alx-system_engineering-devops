#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def add_title(hot_list, hot_posts):
    """Adds item into a list"""
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API recursively"""
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # If the request fails, return None
    if response.status_code != 200:
        return None

    # Extract data from the response
    data = response.json()['data']
    hot_posts = data['children']
    add_title(hot_list, hot_posts)
    after = data['after']

    # If no more posts to fetch, return the hot_list
    if not after:
        return hot_list

    # Recursively call the function to fetch more posts
    return recurse(subreddit, hot_list=hot_list, after=after)


# Check if the code meets the requirements
if __name__ == '__main__':
    result = recurse(sys.argv[1])
    if result is not None:
        print(len(result))
    else:
        print("None")
