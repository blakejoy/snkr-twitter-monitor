import tweepy
from datetime import datetime
from tweepy.streaming import json
from tweet import Tweet
from discord_channel import send_embed
from config import USER_ID_LIST


class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("Connected to streaming API")

    def on_status(self, status):
        print(status.text)

    def on_data(self, raw_data):
        data = json.loads(raw_data)

        if "user" in data:
            print("Tweet from @{} found! - {}".format(data["user"]["screen_name"],str(datetime.now())))


            if not data["text"].startswith('RT @') and data["in_reply_to_status_id"] is None:
                if data["user"]["id_str"] in USER_ID_LIST:
                    if "media" not in data["entities"]:
                        tweet_id = data["id"]

                        text = data["text"]
                        username = data["user"]["screen_name"]
                        profile_img_url = data["user"]["profile_image_url"]
                        embed_url_list = data["entities"]["urls"]
                        link_to_tweet = "https://twitter.com/{}/status/{}".format(username, tweet_id)
                        image_url = ""

                        send_embed(Tweet(text, username, profile_img_url, embed_url_list, link_to_tweet, image_url))
                    elif "media" in data["entities"]:
                        tweet_id = data["id"]

                        text = data["text"]
                        username = data["user"]["screen_name"]
                        profile_img_url = data["user"]["profile_image_url"]
                        embed_url_list = data["entities"]["urls"]
                        link_to_tweet = "https://twitter.com/{}/status/{}".format(username,tweet_id)
                        image_url = data["entities"]["media"][0]["media_url"]

                        send_embed(Tweet(text,username,profile_img_url,embed_url_list,link_to_tweet,image_url))
                    else:
                        print("tweet not available")


            else:
                print("...oh it was a retweet or a reply")

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False