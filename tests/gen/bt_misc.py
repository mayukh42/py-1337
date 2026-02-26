import sys
from tests.utils import *
from gen.bt_misc import *


def create_tree():
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


def test_lca(data):
    t = create_tree()
    print(t)
    for inp in data:
        n1 = BTNode(inp["n1"])
        n2 = BTNode(inp["n2"])
        res = lca(t, n1, n2)
        if res != None:
            res_v = res.val
        else:
            res_v = res
        print(n1.val, n2.val, res_v, "pass" if res_v == inp["res"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/bt_misc.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    test_lca(data["lca"])
