#!/usr/bin/python
import binary_search_tree


RED = 1
BLACK = 0


class Node(binary_search_tree.Node):
    def __init__(self, data):
        super().__init__(data)
        self.color = RED


class RedBlackTree(binary_search_tree.BinarySearchTree):
    # chapter 13.1
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = BLACK

        self.root = self.nil
        self.root.parent = self.nil


    # chapter 13.3
    def insert(self, z):
        super().insert(z)

        z.left = self.nil
        z.right = self.nil
        self._insert_fixup(z)


    # chapter 13.3
    def _insert_fixup(self, z):
        """ https://www.youtube.com/watch?v=FNeL18KsWPc """
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    # re-coloring is enough
                    z.parent.color = BLACK               # case 1
                    y.color = BLACK                      # case 1
                    z.parent.parent.color = RED          # case 1
                    z = z.parent.parent                  # case 1
                else:
                    if z == z.parent.right:
                        # zig-zag case
                        z = z.parent                     # case 2
                        self._left_rotate(z)             # case 2
                    # straight line case
                    z.parent.color = BLACK               # case 3
                    z.parent.parent.color = RED          # case 3
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


    # chapter 13.4
    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
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
            self._delete_fixup(x)  # 'x' moves into 'y''s original position


    def _delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            # 'x' always points to a nonroot doubly black node
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK              # case 1
                    x.parent.color = RED         # case 1
                    self._left_rotate(x.parent)  # case 1
                    w = x.parent.right           # case 1
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED                # case 2
                    x = x.parent                 # case 2
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK     # case 3
                        w.color = RED            # case 3
                        self._right_rotate(w)    # case 3
                        w = x.parent.right       # case 3
                    w.color = x.parent.color     # case 4
                    x.parent.color = BLACK       # case 4
                    w.right.color = BLACK        # case 4
                    self._left_rotate(x.parent)  # case 4
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root


if __name__ == "__main__":
    from binary_search_tree import preorder_tree_walk, inorder_tree_walk

    tree = RedBlackTree()

    n41 = Node(41)
    n38 = Node(38)
    n31 = Node(31)
    n12 = Node(12)
    n19 = Node(19)
    n8 = Node(8)

    # exercises 13.3-2
    tree.insert(n41)
    tree.insert(n38)
    tree.insert(n31)
    tree.insert(n12)
    tree.insert(n19)
    tree.insert(n8)

    preorder_tree_walk(tree.root)
    print()
    inorder_tree_walk(tree.root)

    print()

    # exercises 13.4-3
    tree.delete(n8)
    tree.delete(n12)
    tree.delete(n19)
    tree.delete(n31)
    tree.delete(n38)
    tree.delete(n41)

    preorder_tree_walk(tree.root)
    print()
    inorder_tree_walk(tree.root)
