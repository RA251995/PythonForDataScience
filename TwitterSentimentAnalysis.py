import tweepy
from textblob import TextBlob

import csv

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECERT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('SEARCH_KEY', count=50)

with open('sentiments.csv', 'w') as csvfile:
	sentiment_writer = csv.writer(csvfile)
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		if analysis.sentiment.polarity > 0:
			sentiment_writer.writerow([tweet.text.encode("utf-8"), 'Positive'])
		else:
			sentiment_writer.writerow([tweet.text.encode("utf-8"), 'Negative'])
