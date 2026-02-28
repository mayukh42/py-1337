from adt.mat import Mat
from adt.item import DPTCell

''' rod_cuts(l, c)
    find all the ways by which the rod of length l can be cut using sects of various length
    length: int
    sects: [int] in increasing order

    e.g. length = 10
    sects = [1,2,3]
    = = = = = = = = = = -> 1x10
    == = = = = = = = = = -> 2x1, 1x9
    ...
    === === === = -> 3x1, 1x1

    full dp table: 
                        length
    s   0   1   2   3   4   5   6   7   8   9   10
    e1  0   1   2   3   4   5   6   7   8   9   10
    c2  0   1   3   5   9   12  18  22  30  35  45
    t3  0   1   3   6   11  16  26  35  48  64  83

    related problems
    partition a number into multiples of 1 or more numbers 
    climbing stairs - up to n steps at a time
    eating choco bar - up to n bites at a time
    etc.
'''
def rod_cuts(sects, length):
    if not length or not sects:
        return None
    r, c = len(sects) + 1, length + 1
    max_sect = sects[-1]

    # DPTCell: number of sects, actual sects
    dpt = Mat(r, c, DPTCell(0, []))
    for i in sects:
        for j in range(1, c):
            if i == 1:
                # trivial solution
                dpt.set(i, j, DPTCell(j, [f"{i}x{j}"]))
                continue
            acc = i
            # add all from previous row, i.e. not using i at all
            d_acc = dpt.get(i-1, j)
            while acc <= j:
                # using acc
                d_acc = d_acc.add(DPTCell(int(acc/i), [f"{i}x{int(acc/i)}"]))
                # not using acc
                rem = max(j - acc, 0)
                d_rem = dpt.get(i-1, rem)
                # combine
                d_acc = d_acc.add(d_rem)
                # move to next multiple of i
                acc += i

            dpt.set(i, j, d_acc)
    return dpt
