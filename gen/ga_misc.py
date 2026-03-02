from adt.graphs import *
from math import inf

def create_adjlist_graph(data):
    gv = AdjList_Graph(data)
    return gv


def dijkstra_sp(graph, root):
    nodes = graph.get_node_labels()
    # dists = dict(map(lambda n: {n, inf}, nodes))
    dists = {x: inf for x in nodes}
    visited = {x: False for x in nodes}
    dists[root] = 0
    # visited[root] = True
    # print(nodes, dists, visited)

    for _ in nodes:
        min_dist = inf
        curr = None
        for i in nodes:
            if not visited[i] and dists[i] < min_dist:
                min_dist = dists[i]
                curr = i
        
        if curr == None:
            # none found in above loop, traversal is done
            break
        visited[curr] = True

        nbrs = graph.get_neighbor_labels(curr)
        for nbr, dist in nbrs.items():
            if visited[nbr]:
                continue
            ndist = dists[curr] + dist
            if ndist < dists[nbr]:
                dists[nbr] = ndist
        
    return dists


def bellman_ford_sp(graph, root):
    nodes = graph.get_node_labels()
    dists = {x: inf for x in nodes}
    dists[root] = 0
    # print(nodes, dists)

    for i in range(len(nodes) - 1):
        for curr in nodes:
            nbrs = graph.get_neighbor_labels(curr)
            for nbr, dist in nbrs.items():
                ndist = dists[curr] + dist
                if ndist < dists[nbr]:
                    dists[nbr] = ndist
    
    # run once more to detect cycles
    for curr in nodes:
        nbrs = graph.get_neighbor_labels(curr)
        for nbr, dist in nbrs.items():
            ndist = dists[curr] + dist
            if ndist < dists[nbr]:
                # cycle detected
                return dists, True

    return dists, False
