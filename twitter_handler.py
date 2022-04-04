from dotenv import load_dotenv
import os
import tweepy
from datetime import datetime
load_dotenv()


def update_displayname(name):
    api_key = os.environ.get('api_key', None)
    api_key_secret = os.environ.get('api_key_secret', None)
    access_token = os.environ.get('access_token', None)
    access_token_secret = os.environ.get('access_token_secret', None)


    auth = tweepy.OAuth1UserHandler(
    api_key, api_key_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)

    api.update_profile(name=name)

    print(f"displayname updated at: {datetime.now().strftime('%Y-%m-%d %H:%M')}")