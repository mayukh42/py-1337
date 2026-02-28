from adt.double_ll import *
from tests.utils import *
import sys


def test_double_ll(data):
    for inp in data:
        d_ll = DoubleLL(inp["arr"], inp["max_len"])
        print(d_ll, "pass" if d_ll.items() == inp["items"] else "fail")

        d_ll.add("l")
        print("added\n", d_ll)
        
        d_ll.insert(8, "m")
        print("inserted\n", d_ll)

        d_ll.remove(3)
        print("removed\n", d_ll)


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/double_ll.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    test_double_ll(data["double_ll"])
