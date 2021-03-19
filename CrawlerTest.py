import config as c
import unittest
import RedditCrawler
import TwitterCrawler
from Database import Database

db = Database(c.host,c.user,c.password,c.database)
class CrawlerTest(unittest.TestCase):
    def test_Invalid_DatabaseConnection(self):
        self.assertTrue(Database("wrong","wrong","wrong","wong"))

    def test_Invalid_RedditAuthentication(self):
        r = RedditCrawler.RedditCrawler("crimes","id","secret")
        self.assertRaises(Exception, r.crawl(db))
    
    def test_Invalid_TwitterAuthentication(self):
        t = TwitterCrawler.TwitterCrawler("wrong_key","wrong_secret","wrong_token","wrong_tokensecret")
        self.assertRaises(Exception, t.crawl(db))
    
    def test_Valid_DatabaseConnection(self):
        self.assertTrue(db)

    def test_Valid_RedditAuthentication(self):
        r = RedditCrawler.RedditCrawler("crimes",c.reddit_id,c.reddit_secret)
        # Test crawling one item in Reddit
        self.assertRaises(Exception, print(list(r.reddit.subreddit('all').top(limit=1)).pop().title))
    
    def test_Valid_TwitterAuthentication(self):
        t = TwitterCrawler.TwitterCrawler(c.consumer_key,c.consumer_secret,c.access_token,c.access_token_secret)
        tweepy = TwitterCrawler.tweepy
        api = t.api
        # Test crawling one item in Twitter
        self.assertRaises(Exception, print(list(tweepy.Cursor(api.search, q="a").items(1)).pop().text))

if __name__ == '__main__':
    unittest.main()