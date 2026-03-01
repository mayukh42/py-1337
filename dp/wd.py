from adt.mat import Mat
from adt.item import DPTCell

''' Levenshtein's Word Distance
    dp algorithm
    r (row dimension): first
    c (col dimension): second
    dpt[i, j] = cost from r[i] to c[j]
        = min(
            dpt[i-1][j-1] + subcost, 
            dpt[i-1][j] + delcost,
            dpt[i][j-1] = inscost
        )
    where,
        if sub and r[i] == c[j] then subcost = 0
        else all cost = 1
'''

def lev_wd(first, second):
    r, c = len(first) + 1, len(second) + 1
    d0 = DPTCell(0, [])
    dpt = Mat(r, c, d0)
    for i in range(1, r):
        dpt.set(i, 0, DPTCell(i, ["d"]))
    for j in range(1, c):
        dpt.set(0, j, DPTCell(j, ["i"]))
    for i in range(1, r):
        for j in range(1, c):
            # using sorted to get the actual op instead of simply min(x, y, z)
            options = [
                (dpt.get(i-1, j-1), "s"),
                (dpt.get(i-1, j), "d"),
                (dpt.get(i, j-1), "i")
            ]
            options = sorted(options, key=lambda x: x[0].vl)
            cost = 1
            op = options[0][1]
            if op == "s" and first[i-1] == second[j-1]:
                # no cost for indentical char sub
                cost = 0
                op = "s0"   # special 0-cost sub
            # we also have which dpt cell to append to, at options[0][0]
            # print(i, j, options[0][0])
            dij = options[0][0].add(DPTCell(cost, [op]))
            dpt.set(i, j, dij)
            # print(dpt)
    return dpt.get(r-1, c-1)


''' Damerau-Levenshtein
    transposition: ca -> ac, then check cost

    TODO: WIP
'''
def dam_lev_wd(first, second):
    r, c = len(first) + 1, len(second) + 1
    d0 = DPTCell(0, [])
    dpt = Mat(r, c, d0)
    for i in range(1, r):
        dpt.set(i, 0, DPTCell(i, ["d"]))
    for j in range(1, c):
        dpt.set(0, j, DPTCell(j, ["i"]))
    for i in range(1, r):
        for j in range(1, c):
            # using sorted to get the actual op instead of simply min(x, y, z)
            options = [
                (dpt.get(i-1, j-1), "s"),
                (dpt.get(i-1, j), "d"),
                (dpt.get(i, j-1), "i")
            ]
            options = sorted(options, key=lambda x: x[0].vl)
            cost = 1
            op = options[0][1]
            if op == "s" and first[i-1] == second[j-1]:
                # no cost for indentical char sub
                cost = 0
                op = "s0"   # special 0-cost sub
            # check for transposition (ac -> ca)
            dij = options[0][0]
            if i > 1 and j > 1 and first[i-1] == second[j-2] and first[i-2] == second[j-1]:
                dij_t = dpt.get(i-2, j-2)
                op = "t"
                if dij_t.vl < dij.vl:
                    dij = dij_t
            dij = dij.add(DPTCell(cost, [op]))
            dpt.set(i, j, dij)
            # print(dpt)
    return dpt.get(r-1, c-1)
