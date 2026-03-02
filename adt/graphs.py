
from dataclasses import dataclass
from adt.mat import Mat

# graph adt

@dataclass
class Vertex():
    lbl: str
    prop: object
    meta: object

    def __init__(self, l, p, m):
        self.lbl = l
        self.prop = p
        self.meta = m

    def __repr__(self) -> str:
        return f"{self.lbl}: {self.prop}({self.meta})"

    def set_meta(self, meta):
        self.meta = meta
        return self
    
    def clear_meta(self):
        self.meta = None
        return self


@dataclass
class Edge():
    lbl: str
    src: Vertex
    dst: Vertex
    prop: object
    meta: object

    def __init__(self, l, u, v, p, m):
        self.lbl = l
        self.src = u
        self.dst = v
        self.prop = p
        self.meta = m
    
    def __repr__(self) -> str:
        return f"{self.l}: {self.src.lbl} -> {self.dst.lbl} ({self.prop}, {self.meta})"
    
    def set_meta(self, meta): 
        self.meta = meta
        return self

    def clear_meta(self):
        self.meta = None
        return self


@dataclass
class AdjList_Graph():
    # like a hashtable
    nodes: {}
    nmap: {}

    def __init__(self, adjlist):
        nodes = {}
        nmap = {}
        for node in adjlist.keys():
            if node not in nmap:
                # create Vertex
                v = Vertex(node, None, None)
                nmap[node] = v
            else:
                v = nmap[node]

            nbrs = adjlist[node]
            nbr_nodes = {}
            # create neighbor nodes if does not exist
            for n, d in nbrs.items():
                if n not in nmap:
                    u = Vertex(n, None, None)
                    nmap[n] = u
                else:
                    u = nmap[n]
                nbr_nodes[n] = d

            nodes[node] = nbr_nodes

        self.nodes = nodes
        self.nmap = nmap
    
    def __repr__(self) -> str:
        return f"{self.nodes}"
    
    def get_node_labels(self):
        return list(self.nodes.keys())
    
    def get_neighbor_labels(self, node):
        return self.nodes.get(node, None)
    
    def get_node(self, label):
        return self.nmap.get(label, None)


# @dataclass
# class AdjMat(self, edges)