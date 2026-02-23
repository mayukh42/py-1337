import sys
from tests.utils import *
from dp.lc_palin import *


def test_lc_palin(data):
    for inp in data:
        ss = inp["string"]
        res = manacher(ss)
        print(ss, res, "pass" if inp["res"] == res else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/linear.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    test_lc_palin(data["lc_palin"])