import sys
from adt.tree import *
from adt.graphs import AdjList
from tests.utils import *

'''
                    4
            2               6
        1       3       5       7
'''
def get_tree():
    t = BTNode(4).add_left(
            BTNode(2).add_left(
                BTNode(1)
            ).add_right(
                BTNode(3)
            )
        ).add_right(
            BTNode(6).add_left(
                BTNode(5)
            ).add_right(
                BTNode(7)
            )
        )
    return t

def test_tree():
    t = get_tree()
    print(t)
    print("in", t.inorder())
    print("pre", t.preorder())
    print("post", t.postorder())

    print("bfs", t.bfs())
    print("dfs", t.dfs())
    print("dfs_post", t.dfs_post())
    print("dfs_in", t.dfs_in())
    print("dfs_post_2sp", t.dfs_post_2sp())

def test_tree_by_create(data):
    for inp in data:
        al = AdjList(inp["adjlist"])
        bt = bst_from_adjlist(al, inp["root_node"])
        print(bt)


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/lcp.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    # test_tree()
    test_tree_by_create(data["binary_tree"])
