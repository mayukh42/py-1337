import sys
from tests.utils import *
from des.ufds import UFNode


def test_ufds(data):
    sa = UFNode("a")
    sb = UFNode("b")
    print(sa, sa.is_singleton())
    print(sb, sb.is_singleton())
    
    # union
    sab = sa.union(sb)
    print(sab, sa.is_singleton(), sb.is_singleton(), sab.is_singleton())
    sc = UFNode("c")
    sabc = sc.union(sab)
    print(sabc)

    # find
    fc = sc.find()
    print(fc)

    sd = UFNode("d")
    print(sabc.contains(sd))

    sabcd = sd.union(sabc)
    print(sabcd)

    fa = sa.find()
    print(fa)
    print(sabcd.contains(sd))

    fb = sb.find()
    print(fb)

    # TODO: input data



if __name__ == '__main__':
    valid = valid_args(sys.argv, 1, "python tests/des/ufds.py inp_file.json")
    if not valid:
        sys.exit(1)

    data = get_input(sys.argv[1])
    test_ufds(data["ufds"])
