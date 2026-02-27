import sys
from tests.utils import *
from dp.rod_cut import *


def test_rod_cuts(data):
    for inp in data:
        l, ss = inp["length"], inp["sects"]
        if not ss or not l:
            print("no valid input; skipping")
            continue
        res = rod_cuts(ss, l)
        last = res.get(ss[-1], l).vl
        print(l, ss, last, "pass" if inp["res"] == last else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/rod_cut.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    test_rod_cuts(data["rod_cuts"])
