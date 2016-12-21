#! python3
# TwitterBot.py is a something
# Notes to run this program you need to install Tweepy

import sys, tweepy, kivy
from tweepy import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.button import Button

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

class TestApp(App):
    def build(self):
        return Button(text= "Hello world")

class MyStreamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)

        # There are many options in the status object,
        # hashtags can be very easily accessed.
        #for hashtag in status.entries['hashtags']:
        #    print(hashtag['text'])

        #return true

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

def oauth_authenticate():

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        try:
            redirect_url = auth.get_authorization_url()
            print redirect_url
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'

        api = tweepy.API(auth)

        return api

def main():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    myStreamListener = MyStreamListener()
    api = oauth_authenticate()
    myStream = tweepy.Stream(api.auth, myStreamListener)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    myStream.filter(track=['#Giveaway'])

    #results = api.search(q="#Giveaway")

    #for result in results:
    #    print result.text

    public_tweets = api.home_timeline()
    #for tweet in public_tweets:
    #    print tweet.text


main()
