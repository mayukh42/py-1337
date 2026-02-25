import sys
from adt.tree import *
from tests.utils import *

'''
                    4
            2               6
        1       3       5       7
'''
def test_tree():
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
    print(t)
    print("in", t.inorder())
    print("pre", t.preorder())
    print("post", t.postorder())

    print("bfs", t.bfs())
    print("dfs", t.dfs())
    print("dfs_post", t.dfs_post())
    print("dfs_in", t.dfs_in())
    print("dfs_post_2sp", t.dfs_post_2sp())


if __name__ == '__main__':
    # valid = valid_args(sys.argv, 1, "python tests/dp/lcp.py inp_file.json")
    # if not valid:
    #     sys.exit(1)

    # data = get_input(sys.argv[1])
    test_tree()
