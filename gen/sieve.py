
import json, math, sys

''' genids_batch()
    calculates standard deviation per batch of 100 integers
    when using Sieve of Eratosthenes (in reverse) 
    for a distributed id generator (multi-master replication)

    the sieve finds whether a number in batch divides by any of the IDs, starting from last (highest), if a lower divisor exists it is delegated to be counted with that instead. 
    E.g. for 35, it first divides by 7 but again divides by 5, so 35 is in the count of 5, not 7, so as to uniformly distribute the generated numbers
'''

IDs = [1, 2, 3, 5, 7]
BATCH_SIZE = 100

def genids_batch(start, end):
    counts_batch = {}
    n = start
    max_idx = len(IDs)-1
    while n < end:
        for i in range(max_idx, -1, -1):
            _id = IDs[i]
            count = 0
            if n % _id == 0:
                # check if others in IDs greater than this are to be delegated to
                tbd = False
                for j in range(i+1, max_idx+1):
                    # safe; this loop wont run for any index higher than max_idx
                    idj = IDs[j]
                    if n % idj == 0:
                        tbd = True
                        break
                if not tbd:
                    count += 1
                    if _id in counts_batch:
                        counts_batch[_id] += 1
                    else:
                        counts_batch[_id] = 1
        n += 1
    return counts_batch


def genids(max=BATCH_SIZE):
    max_batches = max/BATCH_SIZE
    b = 0
    counts = {}
    while b < max_batches:
        start, end = b*100, (b+1)*100
        counts_batch = genids_batch(start, end)
        counts[b] = counts_batch
        b += 1
    return counts


def stddev(xs=[]):
    varN, n = 0, len(xs)
    if n == 0:
        return 0
    mean = sum(xs)/n
    for i in xs:
        varN += (i-mean)**2
    var = varN/n
    return math.sqrt(var)


def stddev_all(counts):
    sd = {}
    for b in counts:
        xs = list(counts[b].values())
        sd[b] = stddev(xs)
    return sd


if __name__ == '__main__':
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
