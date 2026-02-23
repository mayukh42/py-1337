import sys, json
from tests.utils import *
from dp.maxsum_subarr import *


def test_kadane(data):
    for inp in data:
        xs = inp["arr"]
        es, best = kadane_empty(xs)
        print(xs, es, best, "pass" if es == inp["expect"] and best == inp["sum"] else "fail")



if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/adt/heap.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    test_kadane(data["maxsum_subarr"])