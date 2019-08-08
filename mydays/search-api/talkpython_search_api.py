import requests

def search_episodes(query):
    """Return a set of JSON results based on the given query using the TalkPython podcast API"""
    query_params = {'q':query}
    req = requests.get("https://search.talkpython.fm/api/search", query_params)
    return req.json()
