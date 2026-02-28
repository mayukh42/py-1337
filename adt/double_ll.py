from collections import deque
from dataclasses import dataclass

@dataclass
class DoubleLL:
    ll: []
    cap: int
    size: int   # also the next available index to add

    def __init__(self, arr, max_len=10):
        self.ll = deque(arr, max_len)
        self.cap = max_len
        self.size = len(self.ll)
    
    def __repr__(self) -> str:
        return f"size={self.size}: {self.ll})"
    
    def items(self):
        return list(self.ll)
    
    def insert(self, i, o):
        try:
            if self.size < self.cap:
                if i == self.size:
                    self.ll.append(o)
                else:
                    self.ll.insert(i, o)
                self.size += 1
        except Exception as e:
            print("no space for new elements")
        return self
    
    def add(self, o):
        return self.insert(self.size, o)
    
    ''' remove(n): 
        implement delete(d, n): 
            abcde.rotate(-2) -> cdefab
            cdefab.popleft() -> c, defab (to be removed)
            defab.rotate(2) -> abdef, done
    '''
    def remove(self, i):
        e = None
        if not self.size:
            return e, self
        try:
            if i == 0:
                e = self.ll.popleft()
            elif i == self.size - 1:
                e = self.ll.pop()
            else:
                self.ll.rotate(-i)
                e = self.ll.popleft()
                self.ll.rotate(i)
        except Exception as ex:
            print(ex)
        if e:
            self.size = max(self.size - 1, 0)
        return e, self

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
