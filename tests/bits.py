from gen.bits import *
from utils import *
import sys


def test_binary(data):
    for inp in data:
        res = binary(inp["num"])
        print(inp["num"], "pass" if res == inp["res"] else "fail")


def test_count_set_bits(data):
    for inp in data:
        res = count_set_bits(inp["num"])
        print(inp["num"], res, "pass" if res == inp["count"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/bits.py inp_file.json")
    if not valid:
        sys.exit(1)
    
    data = get_input(sys.argv[1])

    # test_binary(data["binary"])
    test_count_set_bits(data["binary"])

