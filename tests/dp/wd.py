import sys
from tests.utils import *
from dp.wd import *


def test_lev_wd(data):
    print("lev")
    for inp in data:
        first, second = inp["first"], inp["second"]
        # if first != "ca":
        #     continue
        res = lev_wd(first, second)
        cost = res.vl
        print(first, second, res, "pass" if inp["cost"] == cost else "fail")


def test_dam_lev_wd(data):
    print("dam_lev")
    for inp in data:
        first, second = inp["first"], inp["second"]
        # if first != "ca":
        #     continue
        res = dam_lev_wd(first, second)
        cost = res.vl
        print(first, second, res, "pass" if inp["cost"] == cost else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/lc.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    test_lev_wd(data["lev"])
    test_dam_lev_wd(data["dam_lev"])

