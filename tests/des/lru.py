
import sys
from tests.utils import *
from des.lru import LRU

def test_lru(data):
    for inp in data:
        arr = inp["objects"]
        cache = LRU(inp["max_len"])
        for k, v in arr.items():
            cache.add(k, v)
            print(cache)
        
        for op in inp["ops"]:
            # execute ops
            if "get" in op:
                # not using eval
                o = cache.get(op["get"])
                print(cache, o, "pass" if o == op["res"] else "fail")
            elif "add" in op:
                for k, v in op["add"].items():
                    o = cache.add(k, v)
                    print(cache, o, "pass" if o == op["res"] else "fail")


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/double_ll.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    test_lru(data["lru"])
