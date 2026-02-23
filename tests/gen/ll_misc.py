from gen.ll_misc import *
from adt.ll import create_list
from tests.utils import *
import sys


def test_move(data):
    print("move")
    for inp in data:
        l1 = create_list(inp["list1"])
        l2 = create_list(inp["list2"])
        r1, r2 = move(l1, l2)
        res1, res2 = create_list(inp["res1"]), create_list(inp["res2"])
        print(r1, r2, 
            "pass" if r1 == res1 and r2 == res2 else "fail"
        )


def test_reverse(data):
    print("reverse")
    for inp in data:
        l1 = create_list(inp["list1"])
        r1, l1 = reverse(l1, None)
        res1 = create_list(inp["res1"])
        print(l1, r1, "pass" if r1 == res1 else "fail"
        )


def test_reverse_arrows(data):
    print("reverse_arrows")
    for inp in data:
        l1 = create_list(inp["list1"])
        head, tail = reverse_arrows(l1)
        res1 = create_list(inp["res1"])
        print(tail, head, "pass" if head == res1 else "fail"
        )


def test_reverse_k(data):
    print("reverse_k")
    for inp in data:
        l1 = create_list(inp["list1"])
        r1 = reverse_k(l1, inp["k"])
        res1 = create_list(inp["res1"])
        print(r1, "k =", inp["k"], "pass" if r1 == res1 else "fail"
        )


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/ll_misc.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    # test_move(data["move"])
    # test_reverse(data["reverse"])
    # test_reverse_arrows(data["reverse"])
    test_reverse_k(data["reverse_k"])
