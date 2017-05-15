#!/usr/bin/python
# problem 13-3
import binary_search_tree


class Node(binary_search_tree.Node):
    def __init__(self, data):
        super().__init__(data)
        self.hight = 0  # length of highest path from it down to a leaf


class AVLTree(binary_search_tree.BinarySearchTree):
    def __init__(self):
        super().__init__()


    def _left_rotate(self, x):
        super()._left_rotate(x)

        self._update_height(x)
        self._update_height(x.parent)


    def _right_rotate(self, y):
        super()._right_rotate(y)

        self._update_height(y)
        self._update_height(y.parent)


    @staticmethod
    def _height(x):
        return x.height if x else -1


    @staticmethod
    def _update_height(x):
        x.height = max(AVLTree._height(x.left), AVLTree._height(x.right)) + 1


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
        super().insert(z)

        self._balance(z)


    def delete(self, z):
        x = z.parent  # record the parent of real deleted node
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)

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
