from adt.double_ll import *
from datetime import datetime
from dataclasses import dataclass
import time

@dataclass
class DeqItem():
    k: str
    o: object
    
    def __repr__(self) -> str:
        return f"({self.k}: {self.o})"


class LRU(object):
    # head: lru, tail: mru
    def __init__(self, capacity):
        self.deq = DoubleLL([], capacity)
        self.capacity = capacity
        # {cache_key: (last_modified, deq_idx)}
        self.keymap = {}

    def __str__(self) -> str:
        return f"{self.capacity}: {self.elements()}"

    def get_size(self):
        return self.deq.get_size()
    
    def elements(self):
        return self.deq.items()

    def add(self, key, o):
        # if full, evict lru
        e = None
        try:
            if self.get_size() == self.capacity:
                ko = self.evict()
                # maintain invariant
                v = self.keymap.pop(ko.k)
                e = ko.o
                print("evicted", ko, v)
            # add to tail
            self.deq = self.deq.add(DeqItem(key, o))
            size = self.get_size()
            self.keymap[key] = [int(time.time()), size - 1]
            return e
        except Exception as e:
            print(e)
    
    def get(self, key):
        if key not in self.keymap:
            return None
        val = self.keymap[key]
        # the key is accessed, so remove and put it back at last index to maintain lru invariant
        ko, self.deq = self.deq.remove(val[1])
        # print(key, val, ko, self.elements())
        self.add(key, ko.o)
        return ko.o
    
    def evict(self):
        # lru: remove from head
        ko, self.deq = self.deq.remove(0)
        return ko
    
    def delete(self, key):
        if key not in self.keymap:
            return None
        v = self.keymap.pop(key)
        ko, self.deq = self.deq.remove(v[1])
        print("deleted", ko, v)
        return ko.o

