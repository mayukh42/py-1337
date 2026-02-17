import json, sys


def valid_args(args, num_args, usage="$ python prog arg1 arg2 ..."):
    print("number of args provided:", len(args))
    if len(args) < num_args + 1:
        print("invalid number of args; usage:", usage)
        return False
    return True


def get_input(inp):
    with open(inp, 'r') as f:
        data = json.load(f)
        return data

