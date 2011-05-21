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
traditional type of search engine is to calculate on the authority of content source,
like pagerank, hits, is the kind of algorithm.
the social media rightnow use a different approach,
use the connection of the user and content to different and customize the search results,
That is, use the user's personal factor "connection" instead of authority of all majority.  

The good part is: with the user profile and friends, we can better find the 
result that user might want,
The bad part is: more algorithm, the result might be narrow in small group of content  

The combination of these two part should be the future of search  

+ Library knowledge vs Street knowledge  
The authority rank search is more like library, the content is ranked by how many  
other book refering them and how many reader borrow them  
The social search is more like street knowledge, you ask your friends for the opition, your friends
should have simular kind of interest with you, 
and you can also heard of the reputation amounts your friend  

+ Facebook like button in search and +1 button  
The facebook like button can be a new ranking element for social search,
google saw it's potential and give out the +1 button for there own searching  

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

Taste graph

Teste graph build the web under the items, run on a super computer and written in 27000 c codes
http://blog.hunch.com/wp-content/uploads/2011/05/110509-HUNCH-TASTEGRAPH_800px_v2.png
Data:
use Teach Hunch About You question to predict your interest
item rating on Hunch.com
facebook likes
checkin data from 4sq and facebook
social connection on facebook and twitter
hunch.com/goodies to test the Teste graph for gift recommendation

using c and assembly to calculate the algorithm matrix in cycle which is overwhelming the 
normal linear algebra

+ Google Social Search  
http://www.google.com/s2/u/0/search/social

google social search 
it will search on your twitter,flicker,gmail,blogger(if you have) and google reader 
to gain your social graph, and provide the social results with the connection data with that source
eg. link XXX - by James - you follow him on twitter

4. Social Search and recommendation system  

Social search has the same way of recommendation system, that is,
It can use your background to find the content you may like, and have different ranking on content.
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
