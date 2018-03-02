import tweepy
from textblob import TextBlob

import csv

consumer_key = 'vNJt8x5FbY8sVvh8fdgSOcGwe'
consumer_secret = 'isEHhqcsdvyAkXpSdW7JWMnZFKdVqXENiRjYxeeDPUGBBCjUQ7'

access_token = '968800004780404736-kH8Yfoyt0OeBmI992aR2CYcbFIJTRJ1'
access_secret = '71JKil08Cau1h3WHUKACm4Y1pLbElSM5qOuCOM0fdsVvg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Modi', count=50)

with open('sentiments.csv', 'w') as csvfile:
	sentiment_writer = csv.writer(csvfile)
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		if analysis.sentiment.polarity > 0:
			sentiment_writer.writerow([tweet.text.encode("utf-8"), 'Positive'])
		else:
			sentiment_writer.writerow([tweet.text.encode("utf-8"), 'Negative'])
