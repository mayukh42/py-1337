import sys
from tests.utils import *
from adt.item import Item
from dp.knap import *


def test_knap(data):
    for inp in data:
        target = inp["target"]
        items = list(map(lambda x: Item(x["lb"], x["wt"], x["vl"]), inp["items"]))
        res = knap(items, target)
        val = res.vl
        items = set(map(lambda x: x.l, res.xs))
        print(res, "pass" if val == inp["res"]["val"] and items == set(inp["res"]["items"]) else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/knap.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    test_knap(data["knap"])