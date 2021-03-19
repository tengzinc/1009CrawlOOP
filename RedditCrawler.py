import praw
from prawcore import ResponseException
from datetime import datetime
from Crawler import Crawler


class RedditCrawler(Crawler):
    """
    A class to represent Reddit Crawler

    ...
    Attributes
    ----------
    Reddit : Object
        Initialize Reddit Connection using PRAW

    Methods
    -------
    crawl():
        Crawl Singapore crimes related data from Reddit.
    """

    def __init__(self, topic, clientId, secret):
        """
        Constructs all the necessary attributes for Reddit Crawler, and initialize connection to Reddit API

        Parameters
        ----------
            topic: str
                The topic for the Web Crawler (can be any words)
            clientId: str
                Authentication id, visit https://www.reddit.com/prefs/apps to register and receive the "client id"
            secret: str
                Visit the website to register to receive String "client secret".
        """
        self.reddit = praw.Reddit(
            client_id=clientId,
            client_secret=secret,
            user_agent=topic,
        )

    def crawl(self, db):
        """
        Crawl Singapore crimes related data from Reddit.

        Parameters
        ----------
        db: Database object
            Initialize connection to MySQL Database and inserting data

        Returns
        -------
        None
        """
        try:
            print("Crawling Reddit now...")
            subreddit = self.reddit.subreddit('Singapore')
            for post in subreddit.search("jail OR charged OR arrested OR sentenced", limit=None):
                post.comments.replace_more(limit=None)
                comment = post.comments.list()
                db.insert("post", str(post.author), str(post.title), str(post.score),
                          datetime.utcfromtimestamp(post.created_utc), len(comment))
        except ResponseException as rerror:
            print("Wrong Reddit authentication details\n", rerror)
        except Exception as e:
            print("Unable to connect to the database\n", e)
