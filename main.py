import tweepy
import urllib3
import logging
from config import *
from stream_listener import MyStreamListener


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth,timeout=60)



if __name__ == '__main__':
    urllib3.disable_warnings()
    print("Setting up stream.....")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener,tweet_mode='extended')

    #input twitter ids for all accounts that need to be streamed
    #right now its nike,finishline,ubiq,sheikh,snkr_twtr,solelinks,jtknotify,sneaksnstuff
    print("Stream started.....")


    myStream.filter(follow=USER_ID_LIST,async=True)

