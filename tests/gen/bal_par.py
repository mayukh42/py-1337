import sys, json
from gen.bal_par import is_balanced_par, is_balanced_by_count

def get_input(inp):
    with open(inp, 'r') as f:
        inps = json.load(f)
        return inps


if __name__ == '__main__':
    # print(sys.prefix)
    # print(sys.base_prefix)
    if len(sys.argv) < 2:
        print("no input file provided!")
        sys.exit(1)
    inps = get_input(sys.argv[1])

    print("all")
    for inp, want in inps["default"].items():
        res = is_balanced_par(inp)
        print(inp, res, "pass" if res == want else "fail")

    for inp, want in inps["simple"].items():
        res = is_balanced_par(inp)
        print(inp, res, "pass" if res == want else "fail")

    print("simple")
    for inp, want in inps["simple"].items():
        res = is_balanced_by_count(inp)
        print(inp, res, "pass" if res == want else "fail")
