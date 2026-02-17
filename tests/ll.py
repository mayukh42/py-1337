from adt.ll import *
from utils import *
import sys


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/ll.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    for inp in data:
        l1 = create_list(inp["vals"])
        if l1:
            print(l1, "pass" if len(l1) == inp["len"] else "fail")
        else:
            # empty list creates a None LL, whose length = 0
            print(l1, "pass")
