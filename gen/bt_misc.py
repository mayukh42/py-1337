from adt.tree import *

def lca(root, n1, n2):
    if root == None:
        return root
    if n1.val <= root.val and n2.val >= root.val:
        # root is the lca
        return root
    elif n1.val <= root.val and n2.val <= root.val:
        # go left
        return lca(root.left, n1, n2)
    else:
        # go right
        return lca(root.right, n1, n2)
