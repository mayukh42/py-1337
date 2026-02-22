from adt.ll import LLNode


''' move(l1, l2)
    move first node of l2 to head of l1
    e.g. [1,2,3], [4,5] -> [4,1,2,3], [5]
    l1 can be null, but l2 cannot
'''
def move(l1, l2):
    head = l2
    l2 = l2.nxt
    head.nxt = l1
    l1 = head
    return l1, l2


''' reverse linked list recursively
    create 2 lists, iteratively put every element of given list at the front of that new list
    recursion is linear with only one branch - O(n)
'''
def reverse(rem, acc):
    if rem is not None:
        # here, acc is passed first because we want to move from l2 to l1, so acc = l1
        acc, rem = move(acc, rem)
        acc, rem = reverse(rem, acc)

    return acc, rem

''' reverse_arrows()
    in-place reverse linked list
'''
def reverse_arrows(head):
    prv = None
    curr = head
    newhead = None
    while curr is not None:
        nxt = curr.nxt
        if nxt is None:
            # curr is last element
            newhead = curr
        curr.nxt = prv
        prv = curr
        curr = nxt
    # return old head also, since it has been changed in place. it is the new tail
    # print(newhead, head)
    tail = None
    curr = newhead
    while curr is not None:
        tail = curr
        curr = curr.nxt
    return newhead, tail

# 1, 2, 3, 4, 5 -> 2, 1, 4, 3, 5
def reverse_k(head, k):
    if k < 2:
        # no change for k = 0 or k = 1
        return head
    curr = head
    newhead = None
    prev = None
    first_k = None
    prev_k = None
    # i == pos (index) of curr in list
    i = 0
    while curr is not None:
        i += 1
        if first_k is None:
            first_k = curr
        prev = curr
        curr = curr.nxt
        if not (i % k):
            # reverse [first_k:prev]
            prev.nxt = None
            # before reversing, nullify tail of last k-group
            if prev_k is not None:
                prev_k.nxt = None
            # print(i, prev.val, first_k.val, 
            #     curr.val if curr is not None else "")
            head_k, tail_k = reverse_arrows(first_k)
            # print(head_k, tail_k)
            if newhead is None:
                newhead = head_k
            if prev_k is not None:
                prev_k.nxt = head_k
            tail_k.nxt = curr
            prev_k = tail_k
            # print(head_k, tail_k)
            prev = None
            first_k = None
    return newhead

