#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return the top ten titles for a given subreddit.
    Return None if an invalid subreddit is given.
    """
    # Set up headers with a user agent to avoid getting blocked
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers).json()
    top_ten = response.get('data', {}).get('children', [])

    # If top_ten is empty, print None and return
    if not top_ten:
        print(None)
        return

    # Print the titles of the top ten posts
    for post in top_ten:
        print(post.get('data').get('title'))
