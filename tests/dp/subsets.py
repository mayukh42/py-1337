import sys, json
from tests.utils import *
from dp.subsets import *


def test_subsets(data):
    for inp in data:
        s = inp["input"]
        reset_metrics()
        ss = subsets(s)
        print(s, json.dumps(ss), "calls", metrics(), "pass" if len(ss) == inp["expected"]["number"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/dp/subsets.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    test_subsets(data["subsets"])