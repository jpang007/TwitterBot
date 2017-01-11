#! python3
# TwitterBot.py is a bot that will automatically Retweet + Follow Giveaway Contests
# Notes to run this program you need to install Tweepy

import sys, tweepy, time, re, json #kivy
from tweepy import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#from kivy.app import App
#from kivy.uix.button import Button

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""
strtweet = ""
Tweet_array = []

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        #Tweet_array = json.loads(status)['username']
        #print status
        #self.api = api

        username = status.user.screen_name
        tweet_data = status.id
        if username != "pangjeremy0":
            try:
                api.retweet(tweet_data)
                api.create_friendship(status.user.screen_name)
            except tweepy.TweepError as e:
                print "Error: Could not perform action"
                pass
            #print "Holding"
        print tweet_data
        print status.text
        #print status
        #api.retweet()
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True #Continue Listening so keep true

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

def oauth_authenticate():

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        try:
            redirect_url = auth.get_authorization_url()
            #print redirect_url
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'

        api = tweepy.API(auth)

        return api

def main():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    myStreamListener = MyStreamListener()
    #api = oauth_authenticate()
    myStream = tweepy.Stream(api.auth, myStreamListener)
    # Listening for new tweets
    myStream.filter(track=["Retweet to win"], async=True)


    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nBye!'
        sys.exit()
