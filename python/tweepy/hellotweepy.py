import tweepy
import sys

consumer_key = 'S7VeMTQn9updLIvdbKieSHObe';
consumer_secret = 'v8glYYKNYvh9uACiBGNMPdqzjbIap2CIUaYfZqKr3SHxSZaDtv';
access_token = '21228833-i9JQK8i4atad7G0yUecfp82PTY4T8pCm8PgTmWuUj';
access_token_secret = 'cR1RgikpfbuxrDr1Fj6YI8B8hOWtWXJ9M9EQCyqXLhemT';

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
  if getattr(tweet, '%s' % sys.argv[1]) is not None:
    print getattr(tweet, '%s' % sys.argv[1])
