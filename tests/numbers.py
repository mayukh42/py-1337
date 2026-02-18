import sys
from utils import *
from gen.numbers import *


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
        print(num, res, "pass" if res == inp["res"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/numbers.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    # test_digits(data["digits"])
    # test_numbers(data["digits"])
    test_confusing_naive(data["confusing"])
