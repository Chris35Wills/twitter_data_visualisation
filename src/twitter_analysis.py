##############
# twitter_data_download.py
# 
# Reads twitter data queried by hashtag and date, writing this to a csv.
#
# Resultant .csv is then sent to spinning_globe.py
#
# Some help: #See here: http://stackoverflow.com/questions/26205102/making-very-specific-time-requests-to-the-second-on-twitter-api-using-python
# 
# TO DO: 
#   try/except for encoding errors
#   convert this to module
#   call module by master.py
#
# @Chris, Jenny and James
##############

import tweepy
from tweepy import OAuthHandler
import numpy as np 
import csv
import twython as twy
from tweepy import Stream
from tweepy.streaming import StreamListener

def set_twitter_keys(con_key, con_sec, acc_tok, acc_tok_sec):
    auth = tweepy.OAuthHandler(con_key, con_sec)
    auth.set_access_token(acc_tok, acc_tok_sec)
    api = tweepy.API(auth)

    return api

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

######

csvfile=open("europe_tweets_ny2016.csv", "w")
csvWriter=csv.writer(csvfile)

longitude_list = np.arange(-180, 190, 10)
latitude_list = np.arange(-90, 100, 10)

for tweet in tweepy.Cursor(api.search, geocode="52,0,100mi", q="#2016 AND since:2015-12-31 AND until:2016-01-01").items():
    if tweet.coordinates != None:
        #print(tweet.created_at, tweet.text, tweet.coordinates)
        #csvWriter.writerow([tweet.created_at, tweet.text.encode(encoding='utf-8', errors='ignore'), tweet.coordinates])
        print(tweet.created_at, tweet.coordinates)
        csvWriter.writerow([tweet.created_at, tweet.coordinates])




