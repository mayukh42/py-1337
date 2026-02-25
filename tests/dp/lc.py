import sys
from tests.utils import *
from dp.lcp import *
from dp.lcs import *


def test_lcp(data):
    for inp in data:
        ss = inp["string"]
        res = manacher(ss)
        print(ss, res, "pass" if inp["res"] == res else "fail")


def test_lcs_naive(data):
    for inp in data:
        s1, s2 = inp["s1"], inp["s2"]
        ss = lcs_naive(s1, s2)
        print(s1, s2, ss, "pass" if inp["res"] == len(ss) else "fail")


def test_lcs(data):
    for inp in data:
        s1, s2 = inp["s1"], inp["s2"]
        ss = lcs(s1, s2)
        lcs_ = ss.get(len(s1), len(s2))
        print(s1, s2, lcs_.vl, "".join(lcs_.xs), "pass" if lcs_.vl == inp["res"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/lc.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    # test_lcp(data["lcp"])
    # test_lcs_naive(data["lcs"])
    test_lcs(data["lcs"])


