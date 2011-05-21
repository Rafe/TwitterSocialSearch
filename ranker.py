from graph import Graph
from node import DEFAULT_SCORE

class SocialRanker:
  def __init__(self):
    self.graph = Graph("mygraph.dat")
    self.ids = self.graph.nodes.keys()

  def score(self,id):
    if id in self.ids:
      node = self.graph.nodes[id]
      return (node.score,node.followers_count)
    else: return (DEFAULT_SCORE,DEFAULT_SCORE)

if __name__ == "__main__":
  rank = SocialRanker()
