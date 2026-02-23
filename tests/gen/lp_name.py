import sys, json
from gen.lp_name import is_long_pressed


def get_input(inp):
    with open(inp, 'r') as f:
        inps = json.load(f)
        return inps


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("no input file provided!")
        sys.exit(1)
    inps = get_input(sys.argv[1])

    for inp in inps:
        name, typed, expect = inp["name"], inp["typed"], bool(inp["expect"])
        res = is_long_pressed(name, typed)
        print(name, typed, res, "pass" if res == expect else "fail")
