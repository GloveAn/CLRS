#!/usr/bin/python
# problem 13-4
from random import random
import binary_search_tree


class Node(binary_search_tree.Node):
    def __init__(self, data):
        super().__init__(data)
        self.priority = random()


class Treap(binary_search_tree.BinarySearchTree):
    def __init__(self):
        super().__init__()


    def _balance(self, x):
        while x is not self.nil:
            if x.left and x.priority > x.left.priority:
                self._right_rotate(x)
            elif x.right and x.priority > x.right.priority:
                self._left_rotate(x)
            x = x.parent


    def insert(self, z):
        super().insert(z)

        self._balance(z.parent)


    def delete(self, z):
        # rotate 'z' to the leaf and delete it
        while z.left is not None and z.right is not None:
            if z.left.priority > z.right.priority:
                self._left_rotate(z)
            else:
                self._right_rotate(z)
        if z.left is None:
            self._transplant(z, z.right)
        else:
            self._transplant(z, z.left)


    def _validate(self, x):
        if x is None: return

        if x.left is not None:
            self._validate(x.left)
            assert x.left.priority > x.priority, "oops"
        if x.right is not None:
            self._validate(x.right)
            assert x.right.priority > x.priority, "oops"


if __name__ == '__main__':
    import sys
    from random import randint
    sys.path.append("../algorithms")
    from random_permutation import randomize_in_place


    def preorder_tree_walk(x):
        if x is not None:
            print(x.data, x.priority)
            preorder_tree_walk(x.left)
            preorder_tree_walk(x.right)
        else:
            print(None)


    treap = Treap()
    nodes = [Node(i) for i in range(20)]

    randomize_in_place(nodes)
    for node in nodes:
        treap.insert(node)
        try:
            treap._validate(treap.root)
        except AssertionError as ae:
            preorder_tree_walk(treap.root)

    randomize_in_place(nodes)
    for node in nodes:
        treap.delete(node)
        try:
            treap._validate(treap.root)
        except AssertionError as ae:
            preorder_tree_walk(treap.root)
