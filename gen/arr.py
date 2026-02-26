
''' intervals (a,b) and (c,d) overlap if b >= c. for such elements, return (a,d) in the new list
    intervals: array of tuples [(a,b), ...]

    is_sorted flag is an OPT for the insert_interval function
'''
def merge_overlap_intervals(intervals, is_sorted=False):
    # first, sort array by start element of each interval
    if not is_sorted:
        si = sorted(intervals, key=lambda t: t[0])
    else:
        si = intervals
    # second, create merged list one by one
    merged = []
    for t in si:
        if merged and t[0] <= merged[-1][1]:
            # compare with prev element and merge with curr if required
            last = merged[-1]
            last[1] = max(t[1], last[1])
            merged[-1] = last
        else:
            # non-overlapping, or first element, add it
            merged.append(t)
            
    return merged


def insert_interval(intervals, elem):
    # find position of elem in intervals (sorted) and insert it
    p = 0
    for i in range(len(intervals)-1):
        t1 = intervals[i]
        t2 = intervals[i+1]
        if elem[0] >= t1[0] and elem[0] <= t2[0]:
            # elem should be inserted between i and i+1
            p = i
    new = intervals[:p+1] + [elem] + intervals[p+1:]
    # print(new)
    return merge_overlap_intervals(new, is_sorted=True)

''' next_higher()
    find next higher element in order, in an array. -1 if none exist for that element
'''
def next_higher(xs):
    s = []
    res = [-1 for x in xs]
    for i in range(len(xs)):
        print(i, s)
        while (s and xs[i] > xs[s[-1]]):
            top = s.pop()
            res[top] = xs[i]
        if (not s) or (s and xs[i] <= xs[s[-1]]):
            s.append(i)
    print("stack", s)
    return res
