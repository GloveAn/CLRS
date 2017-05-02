#!/usr/bin/python


RED = 1
BLACK = 0


class Node():
    def __init__(self, data, color=RED, parent=None):
        self.data = data
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None


class RedBlackTree():
    # chapter 13.1
    def __init__(self):
        self.nil = Node(None, BLACK)
        self.root = self.nil
        self.root.parent = self.nil


    # chapter 13.2
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    # exercises 13.2-1
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x


    # chapter 13.3
    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self._insert_fixup(z)


    # chapter 13.3
    def _insert_fixup(self, z):
        """ https://www.youtube.com/watch?v=FNeL18KsWPc """
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    # re-coloring is enough
                    z.parent.color = BLACK              # case 1
                    y.color = BLACK                     # case 1
                    z.parent.parent.color = RED         # case 1
                    z = z.parent.parent                 # case 1
                else:
                    if z == z.parent.right:
                        # zig-zag case
                        z = z.parent                    # case 2
                        self._left_rotate(z)             # case 2
                    # straight line case
                    z.parent.color = BLACK              # case 3
                    z.parent.parent.color = RED         # case 3
                    self._right_rotate(z.parent.parent)  # case 3
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.root.color = BLACK


    # chapter 13.4
    def _transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def _minimum(self, x):
        if x is self.nil:
            return x
        while x.left is not self.nil:
            x = x.left
        return x


    # chapter 13.4
    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent = z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self._delete_fixup(x)


    def _delete_fixup(self, x):
        pass


def tree_minimum(x):
    if x is :
        return x
    while x.left is not None:
        x = x.left
    return x


if __name__ == "__main__":
    from binary_search_tree import preorder_tree_walk, inorder_tree_walk

    tree = RedBlackTree()
    tree.insert(Node(41))
    tree.insert(Node(38))
    tree.insert(Node(31))
    tree.insert(Node(12))
    tree.insert(Node(19))
    tree.insert(Node(8))

    preorder_tree_walk(tree.root)
    print()
    inorder_tree_walk(tree.root)
