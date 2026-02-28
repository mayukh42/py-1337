

''' Union Find Data Structure
    Disjoint Sets

    methods: union, find, contains
'''
class UFNode(object):
    # singleton set of object o
    def __init__(self, o):
        self.parent = self
        self.val = o
        self.rank = 0
    
    def __str__(self) -> str:
        return f"{self.val}, p={self.parent.val},r={self.rank}"
    
    def link(self, other):
        newpar = None
        if self.rank > other.rank:
            other.parent = self
            newpar = self
            # ranks don't change
        else:
            # self.rank <= ufs2.rank
            self.parent = other
            newpar = other
            if self.rank == other.rank:
                other.rank += 1
        return newpar
    
    # path compression - parent is one node away, so we use if instead of while
    def find(self):
        # find root of self
        curr = self
        if curr != curr.parent:
            # print(curr.val)
            curr = curr.parent
        return curr
    
    def union(self, other):
        par = self.find()
        otherpar = other.find()
        newpar = par.link(otherpar)
        return newpar
    
    def contains(self, other):
        return self.parent.val == other.parent.val
    
    def is_singleton(self):
        # print(self.val, self.rank)
        return self.val == self.parent.val and not self.rank
