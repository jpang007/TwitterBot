#! python3
# TwitterBot.py is a bot that will automatically Retweet + Follow Giveaway Contests
# Notes to run this program you need to install Tweepy

import sys, tweepy, time, re, json #kivy
from tweepy import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from httplib import IncompleteRead

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

followers = api.friends_ids("pangjeremy0")
ToKillList = ["One Direction", "Beliebers", "Selena", "Gomez", "Beiber", "Justin"]

#Function to help kill followers to avoid hitting the limit
def KillFriends():
    # Lists out all friends in an array (sorted)

    #print len(followers)
    if (len(followers) > 3500):
        api.destroy_friendship(followers[-1])


#Listener Streaming to catch tweets
class MyStreamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        #Tweet_array = json.loads(status)['username']
        #print status
        #self.api = api

        KillFriends()

        username = status.user.screen_name
        tweet_data = status.id
        actualTweet = status.text

        if username != "pangjeremy0":
            try:
                for x in status.entities.get("user_mentions", [{}]):
                    BotFinderScreenName = x.get("screen_name",None)
                    BotFinderName = x.get("name",None)
                    BotFinderScreenName = BotFinderScreenName.upper()
                    BotFinderName.upper()
                    if ('BOT' in BotFinderScreenName or 'BOT' in BotFinderName):
                        print ("Detected Bot!")
                # Usually giveaways include a photo this is to help filter out the
                # "fake giveaway tweets"
                # Check tweet if there is a photo
                    else:
                        for x in status.entities.get("media",[{}]):
                            #checks if there is any media-entity
                            if x.get("type", None):
                                # photoCheck
                                if x.get("type", None) == "photo":
                                    print ("Success this tweet has a photo")
                                    print (actualTweet)
                                    actualTweet = actualTweet.upper()
                                    if (u'BESTFANARMY' in actualTweet or u'IHEARTAWARDS' in actualTweet or u'NOW' in actualTweet):
                                        print ("PLZ NO")
                                        print ("MUST SKIP")
                                    else:
                                        if (u'RETWEET' in actualTweet or u'RT' in actualTweet):
                                            print ("RT found")
                                            api.retweet(tweet_data)
                                        if (u'LIKE' in actualTweet or u'FAV' in actualTweet or u'FAVE' in actualTweet):
                                            print ("Like found")
                                            api.create_favorite(tweet_data)
                                        if (u'FOLLOW' or u'FLW' in actualTweet):
                                            print ("Follow found")
                                            api.create_friendship(status.user.screen_name)
                print ("(Need to Rest)")
                time.sleep(3)
            except tweepy.TweepError as e:
                print ("Error: Could not perform action")
                pass
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True #Continue Listening so keep true

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

#Function handles the authetification of Twitter
#We need api to be global so this funciton isn't used
def oauth_authenticate():

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        try:
            redirect_url = auth.get_authorization_url()
            #print redirect_url
        except tweepy.TweepError:
            print ('Error! Failed to get request token.')

        api = tweepy.API(auth)

        return api

def main():
    while True:
        try:
            #This handles Twitter authetification and the connection to Twitter Streaming API
            myStreamListener = MyStreamListener()
            #api = oauth_authenticate()
            myStream = tweepy.Stream(api.auth, myStreamListener)
            # Listening for new tweets
            myStream.filter(track=["Retweet to win"])
        except KeyboardInterrupt:
            # Or however you want to exit this loop
            myStream.disconnect()
            print ('\nBye!')
            break
        except:
            # Oh well, reconnect and keep trucking
            print ("Restarting")
            continue
    pass


main()
