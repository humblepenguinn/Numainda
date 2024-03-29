import os
from requests_oauthlib import OAuth1Session
import json


class Twitter:

    def __init__(self):
        self.api_key = os.environ.get('CONSUMER_KEY')
        self.api_secret = os.environ.get('CONSUMER_SECRET')
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
        
        self.oauth = OAuth1Session(
            self.api_key,
            client_secret=self.api_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret
        )

    def post_tweet(self, tweet):
    # Twitter API v2 endpoint for posting tweets
        url = 'https://api.twitter.com/2/tweets'


        payload = {
            'text': tweet
        }

        headers = {
            'Content-Type': 'application/json'
        }

        print(json.dumps(payload))  # Optional: For debugging

        response = self.oauth.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 201:  # Check for successful tweet creation
            return response.json()
        else:
            print("Tweet failed:", response.text)
            return None