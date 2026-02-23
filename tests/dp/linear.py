import sys
from tests.utils import *
from dp.linear import *
from datetime import datetime


def test_fib(data):
    for inp in data:
        n = inp["n"]
        f = fib(n)
        print(n, f, "pass" if f == inp["f"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/fib.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    test_fib(data["fib"])

