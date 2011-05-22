import time
from getpass import getpass
from tweepy import *
import setting
import time
import math
from node import Node

REQUEST_INTERVAL = 1

class SocialCrawler:
  
  def __init__(self):
    self.graph = {}
    self.path = []
    auth = OAuthHandler(setting.consumer_token,
                        setting.consumer_secret)
    auth.set_access_token(setting.user_key,setting.user_secret)
    self.api = API(auth)

  def timeline(self):
    return self.api.home_timeline(count = 100)

  def count(self):
    return len(self.graph)

  def addRetweets(self):
    self.retweets = self.api.retweeted_by_me(count = 100,trim_user = False,include_entities = True)
    retweets_count = {}

    for retweet in self.retweets:
      id = retweet.user.id 
      if id in retweets_count:
        retweets_count[id] += 1
      else:
        retweets_count[id] = 1
    
    for id in retweets_count:
      if id in self.graph:
        self.graph[id].score += math.log(retweets_count[id])

  def buildGraph(self,id=0):
    followers = []
    if id == 0:
      followers = self.api.friends()
    elif not id in self.path:
      followers = self.api.friends(id)
    else:
      print "exit"
      return

    self.path.append(id)

    time.sleep(REQUEST_INTERVAL)

    for follower in followers:
      try:
        if not follower.id in self.graph:
          self.graph[follower.id] = Node(follower.id,1,follower.followers_count)
        else:
          self.graph[follower.id].score += 0.35
      except Exception as e:
        print e
    print self.graph

    for id in self.graph:
      self.buildGraph(id)

  def writeGraph(self,filename):
    file = open(filename,"w")
    for id in self.graph:
      try:
        item = self.graph[id]
        file.write("%d %d %d\n" %(id,item.score,item.followers_count) )
      except Exception as e:
        print e
    file.close

if __name__ == "__main__":

  crawler = SocialCrawler()
  crawler.buildGraph()
  crawler.addRetweets()
