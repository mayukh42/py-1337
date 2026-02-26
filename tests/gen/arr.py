from gen.arr import *
from tests.utils import *
import sys


def test_merge_overlap_intervals(data):
    for inp in data:
        res = merge_overlap_intervals(inp["intvs"])
        print(res, "pass" if res == inp["res"] else "fail")


def test_insert_intervals(data):
    for inp in data:
        res = insert_interval(inp["intvs"], inp["elem"])
        print(res, "pass" if res == inp["res"] else "fail")


def test_next_higher(data):
    for inp in data:
        res = next_higher(inp["xs"])
        print(inp["xs"], res, "pass" if res == inp["res"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/intervals.py inp_file.json")
    if not valid:
        sys.exit(1)
    
    data = get_input(sys.argv[1])

    # test_merge_overlap_intervals(data["intervals"])
    # test_insert_intervals(data["insert"])
    test_next_higher(data["next_higher"])
