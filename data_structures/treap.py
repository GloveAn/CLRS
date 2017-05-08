#!/usr/bin/python
# problem 13-4
from random import random


class Node():
    def __init__(self, data):
        self.data = data
        self.priority = random()
        self.left = None
        self.right = None


class Treap():
    # NOTE: Treap can be inherited from Binary Search Tree
    def __init__(self):
        self.root = None


    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x


    def _balance(self, x):
        while x is not None:
            if x.left and x.priority > x.left.priority:
                self._right_rotate(x)
            elif x.right and x.priority > x.right.priority:
                self._left_rotate(x)
            x = x.parent


    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

        self._balance(z.parent)


    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent


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
