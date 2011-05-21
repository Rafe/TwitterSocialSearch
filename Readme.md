Build Custom search engine
==============================

0.get twitter dataz  

using tweepy: https://github.com/joshthecoder/tweepy  
example: https://github.com/joshthecoder/tweepy-examples  

1.build social graph, user index,  
include:
userid, connection point(freq) 

connection points C():  
  1.follow  
  2.follow's follow  
  3.reply and message and mention  
  4.group  

auth score A():
  count by log_follower

2.solution  

Rank(Msg) = C(User|Author) * TimeFactor  
Rank(Query) = C(User|Author) * Relativity * Auth(Author)  

3.programming  

python, pylon on small web server to perform as web service.  
