
from dataclasses import dataclass

@dataclass
class LLNode:
    val: object
    nxt: LLNode

    def __repr__(self) -> str:
        s = []
        curr = self
        while curr:
            s.append(curr.val)
            curr = curr.nxt
        return f"{s}"

    def __len__(self) -> int:
        n = 0
        curr = self
        # while curr or curr != None did not work. why?
        while curr is not None:
            n += 1
            curr = curr.nxt
        return n
    
    def __eq__(self, o) -> bool:
        curr = self
        oth = o
        while curr is not None and oth is not None:
            if curr.val != oth.val:
                return False
            curr = curr.nxt
            oth = oth.nxt
        if curr is not None or oth is not None:
            # lists are of different length
            return False
        return True

def create_list(items=[]):
    head = None
    curr = head
    for x in items:
        node = LLNode(x, None)
        if not head:
            head = node
            curr = head
        else:
            curr.nxt = node
            curr = curr.nxt
    return head
