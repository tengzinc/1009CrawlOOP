import config as c
from Database import Db
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
from GUI import GUI

print("Start")
db = Database(c.host, c.user, c.password, c.database)
reddit = RedditCrawler("Crimes", c.reddit_id, c.reddit_secret)
twitter = TwitterCrawler(c.consumer_key, c.consumer_secret,
                         c.access_token, c.access_token_secret)
ui = GUI(db, reddit, twitter)
ui.root.mainloop()
db.disconnect()
