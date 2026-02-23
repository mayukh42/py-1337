
import math

'''
    the priority queue (heap) adt
    operations:
        get-max O(1)
        extract-max O(lg n)
        insert one element O(lg n)
        insert n elements O(n.lg n)
'''

class Heap(object):
    def __init__(self, size):
        # index 0 is unused
        # size should be nearest power of 2 above provided value
        p2 = int(math.log2(size)) + 1
        self.xs = [0 for x in range(1 << p2)]
        self.size = (1 << p2) - 1
        self.start = 1
        self.end = 1
    
    def __str__(self):
        return f"{self.xs[1:]}, length={self.end-1}, size={self.size}"
    
    def is_full(self):
        return self.end == self.size
    
    def is_empty(self):
        return self.end == 1

    def get_max(self):
        return self.xs[self.start]
    
    def swap(self, i, j):
        if i < self.start or j > self.end:
            raise Exception("Index out of bounds!")
        self.xs[i], self.xs[j] = self.xs[j], self.xs[i]
        return self.xs[i], self.xs[j]
    
    def extract_max(self):
        e = self.get_max()
        self.xs[self.start] = 0
        i = self.start
        # bubble down ops
        while i < self.end:
            j = i << 1
            k = j + 1
            if j > self.end or k > self.end:
                break
            if self.xs[j] > self.xs[k]:
                self.swap(i, j)
                i = j
            else:
                self.swap(i, k)
                i = k
        # shift elements if i < self.end
        if i < self.end:
            while i < self.end:
                self.swap(i, i+1)
                i += 1
        # at this point, i = self.end, which is blank. 
        self.end -= 1
        return e
    
    def insert(self, e):
        if self.is_full():
            raise Exception("heap is full. resize it first!")
        self.xs[self.end] = e
        i = self.end
        self.end += 1
        # bubble up ops
        while i > self.start:
            j = int(i/2)
            # print(i, j, self.xs)
            if j < self.start:
                break
            if self.xs[i] > self.xs[j]:
                # swap i, j
                self.swap(i, j)
                i = j
            else:
                break
        return i
    
    def resize(self):
        # resize to double; we need to skip index 0 only the first time, so now it is just double self.size
        # TODO: this can be automated in insert()
        self.xs += [0 for x in range(self.size)]
        self.size *= 2


''' heapsort(): 
    use priority queue to sort a list of elements
    O(n.lg n) because the heap creation is largest complexity
'''
def heapsort(xs):
    h = Heap(len(xs))
    for x in xs:
        h.insert(x)
    
    ys = []
    while not h.is_empty():
        ys.append(h.extract_max())
    
    return ys


