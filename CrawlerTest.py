import config as c
import unittest
import RedditCrawler
import TwitterCrawler
from Database import Database


class CrawlerTest(unittest.TestCase):
    """
    A class used for unit testing
    '''
    Attributes
    ----------
    '''
    :Methods
    test_Invalid_DatabaseConnection():
        Test for invalid connection to database
    test_Invalid_RedditAuthentication():
        Test for invalid authentication to reddit
    test_Invalid_TwitterAuthentication():
        Test for invalid authentication to twitter
    test_Valid_DatabaseConnection():
        Test for valid connection to database
    test_Valid_RedditAuthentication():
        Test for valid authentication to reddit
    test_Valid_TwitterAuthentication():
        Test for valid authentication to twitter
    """
    def test_Invalid_DatabaseConnection(self):
        """
        Test for invalid connection to database
        :return:
        None
        """
        self.assertRaises(Exception, Database("wrong", "wrong", "wrong", "wong"))

    def test_Invalid_RedditAuthentication(self):
        """
        Test for invalid authentication to reddit
        :return:
        None
        """
        db = Database(c.host, c.user, c.password, c.database)
        r = RedditCrawler.RedditCrawler("crimes", "id", "secret")
        self.assertRaises(Exception, r.crawl(db))

    def test_Invalid_TwitterAuthentication(self):
        """
        Test for invalid authentication to twitter
        :return:
        None
        """
        db = Database(c.host, c.user, c.password, c.database)
        t = TwitterCrawler.TwitterCrawler("wrong_key", "wrong_secret", "wrong_token", "wrong_tokensecret")
        self.assertRaises(Exception, t.crawl(db))

    def test_Valid_DatabaseConnection(self):
        """
        Test for valid connection to database
        :return:
        None
        """
        self.assertRaises(Exception, Database(c.host, c.user, c.password, c.database))

    def test_Valid_RedditAuthentication(self):
        """
        Test for valid authentication to reddit
        :return:
        None
        """
        print("\nTesting valid Reddit Authentication:")
        r = RedditCrawler.RedditCrawler("crimes", c.reddit_id, c.reddit_secret)
        # Test crawling one item in Reddit
        self.assertRaises(Exception, print(list(r.reddit.subreddit('all').top(limit=1)).pop().title))

    def test_Valid_TwitterAuthentication(self):
        """
        Test for valid authentication to twitter
        :return:
        None
        """
        print("\nTesting valid Twitter Authentication:")
        t = TwitterCrawler.TwitterCrawler(c.consumer_key, c.consumer_secret, c.access_token, c.access_token_secret)
        tweepy = TwitterCrawler.tweepy
        api = t.api
        # Test crawling one item in Twitter
        self.assertRaises(Exception, print(list(tweepy.Cursor(api.search, q="a").items(1)).pop().text))


if __name__ == '__main__':
    unittest.main()