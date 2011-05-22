from graph import Graph
from node import DEFAULT_SCORE
from tweepy import *  
import setting
import time
import datetime
import math

class SocialRanker:
  def __init__(self):
    self.graph = Graph("mygraph.dat")
    self.ids = self.graph.nodes.keys()
    auth = OAuthHandler(setting.consumer_token,
                        setting.consumer_secret)
    auth.set_access_token(setting.user_key,setting.user_secret)
    self.api = API(auth)

  def score(self,id):
    if id in self.ids:
      node = self.graph.nodes[id]
      return (node.score,node.followers_count)
    else: return (DEFAULT_SCORE,DEFAULT_SCORE)

  def edgeScore(self,tweet):
    return 1

  def timeFactor(self,tweet):
    tweetTime = time.mktime(tweet.created_at.timetuple())
    return math.log(tweetTime)

  def rankTimeline(self):
    self.now = time.mktime(datetime.datetime.now().timetuple())
    self.timeline = self.api.home_timeline(count = 100)
    self.scores = {}
    for tweet in self.timeline:
      score = self.score(tweet.user.id)[0] * self.edgeScore(tweet) * self.timeFactor(tweet)
      self.scores[score] = tweet

  def showTimeline(self):
    ids = sorted(self.scores,reverse=True)
    for id in ids:
      try:
        tweet = self.scores[id]
        print "%s Tweet: %s \n with score %f" %(tweet.user.name,tweet.text,id)
      except:
        pass

if __name__ == "__main__":
  rank = SocialRanker()
  rank.rankTimeline()
  rank.showTimeline()
