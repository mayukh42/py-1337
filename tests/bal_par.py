import sys, json
from gen.bal_par import is_balanced_par

def get_input(inp):
    with open(inp, 'r') as f:
        inps = json.load(f)
        return inps


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("no input file provided!")
        sys.exit(1)
    inps = get_input(sys.argv[1])

    for inp, want in inps.items():
        res = is_balanced_par(inp)
        print(inp, res, "pass" if res == want else "fail")
