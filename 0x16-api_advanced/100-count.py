#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if instances is None:
        instances = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = title.count(word.lower())
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if not instances:
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)


# Check if the code meets the requirements
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>"
              .format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
