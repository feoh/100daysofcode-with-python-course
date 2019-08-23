from collections import namedtuple, Counter
import os
import re
from typing import List

import tweepy
import readability


def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exclude_replies=False, include_rts=True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)


Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_ACCOUNT = 'feoh'

TWITTER_KEY = os.environ['TWITTER_KEY']
TWITTER_SECRET = os.environ['TWITTER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
print(auth)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)
print(api)

tweets: List[Tweet] = list(get_tweets())

score_total = 0

for tweet in tweets:
    results = readability.getmeasures(tweet.text, lang='en')
    score = results['readability grades']['GunningFogIndex']
    print(f"Tweet Text: {tweet.text} Gunning Fog Score: {score}")
    score_total = score_total + score

average_score = score_total / len(tweets)
print(f"The average Gunning Fog Index Score for {len(tweets)} is {average_score}")
