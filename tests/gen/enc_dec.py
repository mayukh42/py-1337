from gen.enc_dec import decode
import sys, json

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
        dec_str = decode(inp["enc"])
        print(inp["enc"], dec_str, "pass" if dec_str == inp["dec"] else "fail")
