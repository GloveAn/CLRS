#!/usr/bin/python
# problem 13-3


class Node():
    def __init__(self, data):
        self.data = data
        self.hight = 0  # length of highest path from it down to a leaf
        self.parent = None
        self.left = None
        self.right = None


class AVLTree():
    # NOTE: AVL Tree can be inherited from Binary Search Tree
    def __init__(self):
        self.root = None


    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        self._update_height(x)
        self._update_height(y)


    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

        self._update_height(y)
        self._update_height(x)


    def _height(self, x):
        return x.height if x else -1


    def _update_height(self, x):
        x.height = max(self._height(x.left), self._height(x.right)) + 1


    def _balance(self, x):
        while x is not None:
            self._update_height(x)
            if self._height(x.left) > self._height(x.right) + 1:
                if self._height(x.left.left) >= self._height(x.left.right):
                    self._right_rotate(x)
                else:
                    self._left_rotate(x.left)
                    self._right_rotate(x)
            elif self._height(x.left) + 1 < self._height(x.right):
                if self._height(x.right.right) >= self._height(x.right.left):
                    self._left_rotate(x)
                else:
                    self._right_rotate(x.right)
                    self._left_rotate(x)

            x = x.parent


    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if x.data < z.data:
                x = x.right
            else:
                x = x.left
        z.parent = y
        if y is None:
            self.root = z
        elif y.data < z.data:
            y.right = z
        else:
            y.left = z

        self._balance(z)


    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent


    def _minimum(self, x):
        while x.left is not None:
            x = x.left
        return x


    def delete(self, z):
        x = z.parent  # record the parent of real deleted node
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)

            x = y

            if y.parent != z:
                x = y.parent

                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y

        self._balance(x)


    def _validate(self, x):
        if x is None: return

        self._validate(x.left) if x.left else None
        self._validate(x.right) if x.right else None

        assert abs(self._height(x.left) - self._height(x.right)) <= 1, "oops"
        self._update_height(x)


if __name__ == '__main__':
    import sys
    from random import randint
    sys.path.append("../algorithms")
    from random_permutation import randomize_in_place


    def preorder_tree_walk(x):
        if x is not None:
            print(x.data)
            preorder_tree_walk(x.left)
            preorder_tree_walk(x.right)
        else:
            print(None)


    tree = AVLTree()
    nodes = [Node(i) for i in range(20)]

    randomize_in_place(nodes)
    for node in nodes:
        tree.insert(node)
        try:
            tree._validate(tree.root)
        except AssertionError as ae:
            preorder_tree_walk(tree.root)

    randomize_in_place(nodes)
    for node in nodes:
        tree.delete(node)
        try:
            tree._validate(tree.root)
        except AssertionError as ae:
            preorder_tree_walk(tree.root)
