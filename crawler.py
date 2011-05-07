import time
from getpass import getpass
from tweepy import *

import setting

consumer_token = setting.consumer_token
consumer_secret = setting.consumer_secret
key = setting.user_key 
secret = setting.user_token

auth = OAuthHandler(consumer_token,consumer_secret)

auth.set_access_token(key,secret)

api = API(auth)
timeline =  api.user_timeline("gugod")

for twit in timeline:
  print "%s twit : %s" %(twit.user.name,twit.text)

