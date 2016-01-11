##############
# twitter_data_download.py
#
# Chris, Jenny and James
##############

# pythonanywhere

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'MJOPjF4zrokMJ6Ny8akwATv5U'
consumer_secret = 'uvIYQynJsjJnpFr1vt8csYbXQZkXaihFO33H1QLdy0Xyk70Aj9'
access_token = '2177728242-S1OnPiPBQLYOQOWVLOfPkAXQs85OdfQXsp943F8'
access_token_secret = '3KV57U9w6CONmmCV6UL7vy3Yw34LQ9j16175bkc67W7HG'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	try:
		print(tweet.text)
	except UnicodeEncodeError:
		print("XXX")




