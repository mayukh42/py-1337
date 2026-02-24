
BOGUS = '|'

def add_bogus(ss, b=BOGUS):
    if b in ss:
        raise Exception(f"invalid bogus char {b}")
    ss_ = b
    for s in ss:
        ss_ += s + b
    return ss_


''' Manacher's Longest Common Palindrome algorithm

    O(n) because c monotonically increases within the nested loops B and C, instead of being a cross product of index vectors

    ex. 
    malayalam -> |m|a|l|a|y|a|l|a|m| 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [0, 1, 0, 1, 0, 3, 0, 1, 0, 9, 0, 1, 0, 3, 0, 1, 0, 1, 0]
    ['malayalam']

'''
def manacher(ss):
    if len(ss) <= 1:
        return [ss]
    
    ss_ = add_bogus(ss)
    n = len(ss_)
    memo = [0 for x in range(len(ss_))]
    # print(ss, ss_, memo)

    c, r = 0, 0
    while c < n:    # loop A, main loop
        while c - (r+1) >= 0 \
            and c + (r+1) < n \
            and ss_[c - (r+1)] == ss_[c + (r+1)]:    # loop B
            r += 1

        # add to memo for c, capture this c in another var only then consider it "seen"
        memo[c] = r
        old_c = c
        old_r = r

        c += 1
        r = 0
        while c <= old_c + old_r:   # loop C; check if a greater palin can be found after the obvious mirror calc in loop B, utilizing the calc so far (stored in memo)
            mr_c = old_c - (c - old_c)
            mr_r = old_c + old_r - c

            if memo[mr_c] < mr_r:
                # c has same size palin as that centered on mr_c, since it is a substring mirror of a palin already at old_c
                memo[c] = memo[mr_c]
                c += 1
            elif memo[mr_c] > mr_r:
                # c cannot have a palin > mr_r else old_c would have a higher radius palin
                memo[c] = mr_r
                c += 1
            else:
                # memo[mr_c] == mr_r, so we dont have exact estimate for palin size at c, but it should be at least mr_r. so increase r instead, which will ensure we check for that only in loop B, in next iter of loop A. IOW, we keep adding r if required through loop B, only then add it to memo[c]
                r = mr_r
                # all cases checked; c cannot increase further, so
                break

    # print(memo)

    # reconstruct actual palin
    max_idxs = []
    max_r = max(memo)
    for i in range(len(memo)):
        if memo[i] == max_r:
            max_idxs.append(i)
    
    # max_idxs has the indexes in processed string that have longest palins. index j in processed string = index j/2 in actual string
    largest = []
    for j in max_idxs:
        # in original string, center of palin is at j/2
        ci = j >> 1
        # in original string, radius of palin is memo[j]/2 + 1, similar to how we calculated range in loop B
        r = memo[j] >> 1
        largest.append(ss[ci - r:ci + r +1])       

    return largest
