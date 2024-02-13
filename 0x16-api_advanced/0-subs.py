#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    Return 0 if an invalid subreddit is given.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set up headers with a user agent to avoid getting blocked
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Send GET request to Reddit API
    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers')

    # If subscribers is not found, return 0
    if not subscribers:
        return 0

    return subscribers
