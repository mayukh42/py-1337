import sys, json
from tests.utils import *
from gen.ga_misc import *


def test_create_graphs(data):
    for inp in data:
        graph = create_adjlist_graph(inp["adjlist"])
        print(graph)
        print(graph.get_node_labels())

        for label in inp["ops"]:
            print(label, graph.get_node(label))
            nbrs = graph.get_neighbor_labels(label)
            print(label, nbrs)
            for nbr in nbrs:
                print(nbr, graph.get_node(nbr))


def test_dijkstra_sp(data):
    for inp in data:
        g = create_adjlist_graph(inp["adjlist"])
        r = inp["root"]
        sp = dijkstra_sp(g, r)
        print(g, r, json.dumps(sp), "pass" if sp == inp["sps"] else "fail")


def test_bellman_ford_sp(data):
    for inp in data:
        g = create_adjlist_graph(inp["adjlist"])
        r = inp["root"]
        sp, has_cycle = bellman_ford_sp(g, r)
        print(g, r, has_cycle, json.dumps(sp), "pass" if sp == inp["sps"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/ga_misc.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    # test_create_graphs(data["dijkstra"])
    # test_dijkstra_sp(data["dijkstra"])
    test_bellman_ford_sp(data["bellman_ford"])

