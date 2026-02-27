
from dataclasses import dataclass
from collections import deque as Queue
from adt.graphs import AdjList

@dataclass
class BTNode:
    val: object
    left: BTNode
    right: BTNode

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def add_left(self, node):
        self.left = node
        return self
    
    def add_right(self, node):
        self.right = node
        return self
    
    def is_leaf(self):
        return self.left == None and self.right == None
    
    def __repr__(self) -> str:
        # even str() is a order traversal; here, pre-order
        return f"{self.val}: [{self.left}, {self.right}]"

    def inorder(self):
        left, right = [], []
        if self.left != None:
            left = self.left.inorder()
        if self.right != None:
            right = self.right.inorder()
        return left + [self.val] + right
    
    def preorder(self):
        left, right = [], []
        if self.left != None:
            left = self.left.preorder()
        if self.right != None:
            right = self.right.preorder()
        return [self.val] + left + right
    
    def postorder(self):
        left, right = [], []
        if self.left != None:
            left = self.left.postorder()
        if self.right != None:
            right = self.right.postorder()
        return left + right + [self.val]
    
    def bfs(self):
        # canonical breadth first search - doesn't need coloring like graphs, since trees are acyclic
        q = Queue([self])
        elems = []
        while len(q):
            node = q.popleft()
            elems.append(node.val)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        return elems

    def dfs(self):
        # pre-order in disguise
        s = list([self])
        elems = []
        while len(s):
            sp = s.pop()
            elems.append(sp.val)
            if sp.right != None:  # trick is to add right first, then left will be popped first
                s.append(sp.right)
            if sp.left != None:
                s.append(sp.left)
        return elems
    
    def dfs_post(self):
        # reverse of post traversal
        s = list([self])
        elems = []
        while len(s):
            node = s.pop()
            elems.append(node.val)
            if node.left != None:
                s.append(node.left)
            if node.right != None:
                s.append(node.right)
        return list(reversed(elems))

    ''' inorder using stack and no recursive fn
        e.g.
            2
        1       3
        recursive flow:
            process(left) + node.val + process(right)
        we simulate the same using stack, but in a tail-recursive way, i.e. when recursive call in the above expr reaches last element, the first 2 are completed and the call need not come back to that level.
        the equivalent of this in stack is that when we move to right child, there is nothing to be done for parent (i.e. already processed).
        in other words, there will be cases when stack is empty (all of left + curr processed) but stack ptr is not null, i.e. it points to the right child and tail-recursively moves on.
        therefore, we need to have a while loop that checks for either non-empty stack or non-null stack ptr
        note that stack ptr == null means we are on a leaf node and backtracking to parent. in this case, stack is non-empty because it at least contains the parent.
    '''    
    def dfs_in(self):
        s1 = []
        sp = self
        elems = []
        while len(s1) or sp != None:
            if sp != None:
                s1.append(sp)
                sp = sp.left
            else:
                sp = s1.pop()
                elems.append(sp.val)
                sp = sp.right
        return elems

    def dfs_post_2sp(self):
        s = []
        elems = []
        sp = self
        prev = None
        while len(s) or sp != None:
            if sp != None:
                s.append(sp)
                sp = sp.left
            else:
                # when sp = None, stack should be non-empty because the former means we have seen a leaf node, which means stack should have its parent at least
                top = s[-1]
                if top.right != None and top.right != prev:
                    sp = top.right
                else:
                    top = s.pop()
                    elems.append(top.val)
                    prev = top
        return elems


def bst_from_adjlist(adjlist, root_v):
    root = BTNode(root_v)
    nodes_map = {root_v: root}

    def get_node(val):
        if val not in nodes_map:
            btnode = BTNode(val)
            nodes_map[val] = btnode
        else:
            btnode = nodes_map[val]
        return btnode

    for node_v in adjlist.get_nodes():
        btnode = get_node(node_v)
        for nbr_v in adjlist.get_neighbors(node_v):
            nbrnode = get_node(nbr_v)
            # BST, no duplicates
            if nbr_v < node_v:
                btnode.add_left(nbrnode)
            elif nbr_v > node_v:
                btnode.add_right(nbrnode)
    return root


