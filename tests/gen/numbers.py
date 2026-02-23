import sys
from tests.utils import *
from gen.numbers import *
from datetime import datetime


def test_digits(data):
    for inp in data:
        n = inp["num"]
        ds = digits(n)
        print(n, ds, "pass" if ds == inp["digits"] else "fail")

def test_numbers(data):
    for inp in data:
        ds = inp["digits"]
        n = number(ds)
        print(ds, n, "pass" if n == inp["num"] else "fail")

def test_confusing_naive(data):
    for inp in data:
        num = inp["num"]
        res = confusing_naive(num)
        print(num, "pass" if res == inp["res"] else "fail")

def test_combine(data):
    for inp in data:
        cmb = combine_digits(inp["p"], inp["n"], inp["ds"], inp["lmt"])
        print(cmb, "pass" if cmb == inp["res"] else "fail")

def test_cross_combine(data):
    for inp in data:
        res = cross_combine(inp["xs"], inp["ys"])
        print(res, len(res), "pass" if res == inp["res"] else "fail")

def test_confusing(data):
    for inp in data:
        res = confusing(inp["num"])
        print(inp["num"], "pass" if res == inp["res"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/numbers.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    # test_digits(data["digits"])
    # test_numbers(data["digits"])
    # test_combine(data["combine"])
    # test_cross_combine(data["cross_combine"])

    # time test
    start = datetime.now()
    test_confusing_naive(data["confusing"])
    end = datetime.now()
    print("time taken for confusing_naive:", (end - start).microseconds, "microsec")

    start = datetime.now()
    test_confusing(data["confusing"])
    end = datetime.now()
    print("time taken for confusing:", (end - start).microseconds, "microsec")
