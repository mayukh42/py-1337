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

