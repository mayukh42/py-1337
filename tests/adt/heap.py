
import sys, json
from tests.utils import *
from adt.heap import *


def test_heap(data):
    for inp in data:
        xs, size = inp["values"], inp["size"]
        h = Heap(size)
        print("empty heap", h)

        for x in xs:
            h.insert(x)
        print("heap after all inserts", h)

        for i in range(len(xs)):
            e = h.extract_max()
            print(e, h)


def test_heapsort(data):
    for inp in data:
        xs = inp["values"]
        ys = heapsort(xs)
        print(xs, "\n", ys, sep="")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/adt/heap.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])

    test_heap(data["heap"])
    test_heapsort(data["heap"])
