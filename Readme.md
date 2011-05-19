+ Build Custom search engine
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

2.solution  

Rank(Msg) = C(User|Author) * TimeFactor  
Rank(Query) = C(User|Author) * Relativity * Auth(Author)  

3.programming  

python, pylon on small web server to perform as web service.  


Draft
======================================
1.introduction:  
Social Search is a new topic of how search engine provide personal result for query 
or topic based on user's profile and connection on social website like twitter,facebook or LinkedIn

2.authority vs connection

3.Social search in work:

+ Aardvark:  
Aardvark is a new type of social search engine, which the target is to find the right person to 
answer your question,
the structure use the social crawler to craw on user's connectivity and profile to find:
1. the connection 
2. the background of people -
  include location,school,website...
Therefore the system can calculate the chance that a user may know the knowledge,

using the algorithm: P(q|U) = C(U1|U2) * P(U2|Topic) * A(U2)

C is decided by social graph  
P is decided by the background and past record of answering question and location and group  
A is the available rate  

+ Facebook Edgerank  

Edgerank is another social ranking algorithm that rank the message on user's news feed

the algorithm is:
Rank(msg) = C(U1|U2) * Edge(Msg) * TimeFactor

C is decided by the connection and pass interaction record, so if 
you talk to your friend regular or press like on his message all the time, 
his status message will have higher potential to get higher score on your newsfeed,
Edge is the type score of your message, like "like","share",photo,comment
will have different score.
TimeFactor is decided by time pass 

+ Hunch  

+ Google Social Search  

the information of google social search and algorithm is not clear,  
but it will search on your twitter follower and 
gmail to gain your social graph, also use the simularity to rank the result(not sure)

5. Social Search and recommendation system  

Social Search in some way is pretty close to recommendation system,
It can use your background to find the content you may like, and have different ranking on 
content.
and the ranking is based on large datas and machine learning based on large data.

simularity is:  
most of your friends like, or group like, or person with simular background like,
you will have higher persontage to like it too.                          

So the simularity search algorithm should be:  
R(Query) = Auth(Result)*Sim(Result|Topic)*C(Result|Author)*Rel(Query|Result)

5.Implement Twitter Timeline with social ranking and simularity system:  

  1. social crawling: building graph  
      find one level result:get friend of friends 
      find group
      update with your interaction with user like retweet , mention or reply
  2. analysis edgetype, like retweet, reply and trend will have different level of edgescore  
  3. user authority: user rank : easy to find by how many follower  
  4. Ranking message on your timeline  

6.conclusion:  
  social search should become an important factor in social media and recommendation system
  but I doesn't nessassarily better than traditional pagerank method.
  We still need development on this area.  
