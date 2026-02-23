
m_recurs_calls = 0

def add_metrics():
    global m_recurs_calls
    m_recurs_calls += 1


def reset_metrics():
    global m_recurs_calls
    m_recurs_calls = 0


def metrics():
    global m_recurs_calls
    return m_recurs_calls


def subsets(ss):
    add_metrics()
    ''' given a set of length n, return all its subsets

        at each recursion level, subsets are partitioned into two, one contains left, another doesn't contain left, i.e. 2 branches of recursion. total tree depth ~ n, so O(2^n)

        the program halts because at every recursion, we reduce the size of input.

        O(2^n), depth: n + 1, 1 for the base case
        recursion tree:
    '''
    if len(ss) == 0:
        return [""]
    left, right = ss[0], ss[1:]
    # print("recursion", m_recurs_calls, left, ",", right)
    rs = subsets(right)
    return [left + r for r in rs] + rs

