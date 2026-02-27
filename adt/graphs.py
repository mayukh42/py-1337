
from dataclasses import dataclass

# graph adt

@dataclass
class AdjList():
    nodes: {}

    def __init__(self, adjlist):
        nodes = {}
        for node in adjlist.keys():
            nbrs = adjlist[node]
            nodes[int(node)] = nbrs
        self.nodes = nodes
    
    def __repr__(self) -> str:
        return f"{self.nodes}"
    
    def get_nodes(self):
        return self.nodes.keys()
    
    def get_neighbors(self, node):
        return self.nodes.get(node, None)

