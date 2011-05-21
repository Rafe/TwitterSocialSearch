from node import Node

class Graph:

  def __init__(self,filename):
    file = open(filename)
    self.nodes = {}
    
    for line in file:
      data = line.split(" ")
      self.nodes[int(data[0])] = Node(int(data[0]),int(data[1]),int(data[2]))

if __name__ == "__main__":
  g = Graph("mygraph.dat")
