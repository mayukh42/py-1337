import sys, json

''' Kadane's algo w/ empty array allowed (i.e. when no element selected, sum = 0)
'''
def kadane_empty(xs):
    best, curr = 0, 0
    j = -1
    for k in range(len(xs)):
        x = xs[k]
        if curr + x > 0: 
            curr += x
        else:
            curr = 0
        
        if curr > best:
            # change best and j
            best = curr
            j = k+1 # j is exclusive index of element selected
    
    i = -1
    calc = best
    for k in range(j-1, -1, -1):
        if calc > 0:
            i = k
            calc -= xs[k]
        else:
            break

    # print(best, i, j)
    if i == -1:
        # empty arr is better
        return [], 0
    return xs[i:j], sum(xs[i:j])
