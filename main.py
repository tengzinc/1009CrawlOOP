import config as c
from Database import Database
from RedditCrawler import RedditCrawler
from socialMediaObjectCreator import socialMedia
from TwitterCrawler import TwitterCrawler
from GUI import GUI





# print("Start")
# db = Database(host,user,password,database)
# # db.createTable()
# # rcrawl = RedditCrawler("Crimes", "zSqCr7ZeezCMgQ","-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
# # rcrawl.crawl(db)
# # tcrawl = TwitterCrawler(consumer_key, consumer_secret,access_token, access_token_secret)
# # tcrawl.crawl(db)
# # readReddit= readDatabase(db,"reddit")
# # print("REDDIT SENTIMENT = ",readReddit.readSentiment())

# twitterObject= socialMedia(db,"twitter")
# print("\treadTwitter")
# print("Twitter Sentiment score  :",twitterObject.getSentimentScore())
# print("Twitter Sentiment        :",twitterObject.getSentiment())
# print("Twitter Crime Count      :",twitterObject.getCrimeScore())

# print("\n\n")
# redditObject= socialMedia(db,"reddit")
# print("\treadReddit")
# print("Reddit Sentiment score  :",redditObject.getSentimentScore())
# print("Reddit Sentiment        :",redditObject.getSentiment())
# print("Reddit Crime Count      :",redditObject.getCrimeScore())



# #keyword = "kill"
# #db.search(keyword)
db = Database(c.host, c.user, c.password, c.database)
reddit = RedditCrawler("Crimes", c.reddit_id, c.reddit_secret)
twitter = TwitterCrawler(c.consumer_key, c.consumer_secret, c.access_token, c.access_token_secret)
ui = GUI(db, reddit, twitter)
ui.root.mainloop()
db.disconnect()
