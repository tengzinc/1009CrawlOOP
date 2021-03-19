from Crawler import Crawler
import tweepy
from tweepy import TweepError
import re
import config as c


class TwitterCrawler(Crawler):
    """
    A class to represent twitter Crawler

    ...
    Attributes
    ----------
    Auth : Object
        Initialize twitter Connection using tweepy
    API : Object
        Initialize tweepy API

    Methods
    -------
    crawl():
        Crawl Singapore crimes related data from twitter.
    """

    def __init__(self, consumer_key, consumer_secret, access_token, token_secret):
        """
        Constructs all the necessary attributes for Tweepy a library to crawl from twitter, and initialize connection to twitter API

        Parameters
        ----------
            Consumer_Key: str
                The API key that twitter issues to the consumer
            Consumer_secret: str
                The password that is used to request access to twitter
            access_token: str
                is issued to the consumer by twitter to allow access priviledge
            token_secret
                is the access token secret that is use along with the access token 
        """
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    # Crawl function
    def crawl(self, db):
        """
        Crawl Singapore crimes related data from Twitter.

        Parameters
        ----------
        db: Database object
            Initialize connection to MySQL Database and inserting data

        Returns
        -------
        None
        """
        try:
            print("Crawling Twitter now...")
            keys = "(charged OR jail OR arrested OR sentenced) AND singapore"
            for tweet in tweepy.Cursor(self.api.search, lang="en", tweet_mode="extended", q=keys+'-filter:retweets').items():
                db.insert("tweet", str(tweet.user.screen_name),
                          re.sub(r"http\S+", "", tweet.full_text), tweet.favorite_count, tweet.created_at, tweet.retweet_count)
        except TweepError as terr:
            print("Wrong Twitter authentication details!\n", terr)
        except Exception as e:
            print("Unable to connect to database!\n", e)
