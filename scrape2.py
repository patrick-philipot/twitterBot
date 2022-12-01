'''Scraping Twitter'''
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "pcsoft femme"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username,tweet.content])

df = pd.DataFrame(tweets, columns=['Date','Username','Content'])
print(df)