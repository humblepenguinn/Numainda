import os
import tweepy


class TwitterBot:
    def __init__(self):
        self.api = TwitterBot.authenticate()
    
    # Entry point for the Twitter bot
    def start(self):
        pass
    
    def authenticate() -> tweepy.API:
        auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN'))
        
        api = tweepy.API(auth)
        
        try:
            api.verify_credentials()
            print("Authentication was successful!")
        except Exception as e:
            print(f"Authentication failed: {e}")
            
        return api
    
    def post_tweet(self, tweet):
        self.api.update_status(tweet)
        return True
    
    def get_all_mentions(self):
        return self.api.mentions_timeline()