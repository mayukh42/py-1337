import sys, json
from tests.utils import *
from gen.sieve import *


if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/gen/sieve.py N [log_mode]")
    if not valid:
        sys.exit(1)

    # data = get_input(sys.argv[1])
    print(IDs)
    N = 500
    if len(sys.argv) >= 2:
        N = int(sys.argv[1])

    mode = 'info'
    if len(sys.argv) >= 3:
        mode = sys.argv[2]

    counts = genids(N)
    if mode == 'debug':
        print(json.dumps(counts, indent=2))

    sd_all = stddev_all(counts)
    print(json.dumps(sd_all, indent=2))
