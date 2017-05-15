#!/usr/bin/python


class Node():
    def __init__(self, data):
        self.data = data

        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.nil = None


    # chapter 12.3
    def insert(self, z):
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is self.nil:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z


    # chapter 12.3
    def _transplant(self, u, v):
        if u.parent is self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not self.nil:
            v.parent = u.parent


    # chapter 12.3
    def delete(self, z):
        if z.left is self.nil:
            self._transplant(z, z.right)
        elif z.right is self.nil:
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y


    # chapter 12.2
    def search(self, x, k = None):
        if k is None:
            k = x
            x = self.root

        while x is not self.nil and k != x.data:
            if k < x.data:
                x = x.left
            else:
                x = x.right
        return x


    # chapter 12.2
    def minimum(self, x = None):
        if x is None:
            x = self.root

        if x is self.nil:
            return x
        while x.left is not self.nil:
            x = x.left
        return x


    # chapter 12.2
    def maximum(self, x = None):
        if x is None:
            x = self.root

        if x is self.nil:
            return x
        while x.right is not None:
            x = x.right
        return x


    # chapter 12.2
    def successor(self, x = None):
        if x is None:
            x = self.root

        if x.right is not self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y is not self.nil and x == y.right:
            x = y
            y = y.parent
        return y


    # exercises 12.2-3
    def predecessor(self, x = None):
        if x is None:
            x = self.root

        if x.left is not self.nil:
            return tree_maximum(x.left)
        y = x.parent
        while y is not self.nil and x == y.left:
            x = y
            y = y.parent
        return y


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


# chapter 12.1
def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.data)
        inorder_tree_walk(x.right)


# exercises 12.1-3
def inorder_tree_nonrecursive(x):
    previous = x.parent  # root.parent == None
    current = x

    while current:
        if previous == current.parent:
            previous = current
            if current.left:
                current = current.left
            else:
                print(current.data)

                if current.right:
                    current = current.right
                else:
                    current = current.parent
        elif previous == current.left:
            previous = current

            print(current.data)

            if current.right:
                current = current.right
            else:
                current = current.parent
        else:
            previous = current
            current = current.parent


# exercises 12.1-4
def preorder_tree_walk(x):
    if x is not None:
        print(x.data)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)


# exercises 12.1-4
def postorder_tree_walk(x):
    if x is not None:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.data)


# chapter 12.2
def tree_search_recursive(x, k):
    if x is None or k == x.data:
        return x
    if k < x.data:
        return tree_search_recursive(x.left, k)
    else:
        return tree_search_recursive(x.right, k)


# exercises 12.2-2
def tree_minimum_recursive(x):
    if x is None or x.left is None:
        return x
    else:
        return tree_minimum_recursive(x.left)


# exercises 12.2-2
def tree_maximum_recursive(x):
    if x is None or x.right is None:
        return x
    else:
        return tree_maximum_recursive(x.right)


if __name__ == "__main__":
    nodes = [Node(i) for i in range(8)]
    tree = BinarySearchTree()
    tree.insert(nodes[3])
    tree.insert(nodes[2])
    tree.insert(nodes[1])
    tree.insert(nodes[5])
    tree.insert(nodes[4])
    tree.insert(nodes[6])
    tree.insert(nodes[7])

    inorder_tree_walk(tree.root)
    print()
    inorder_tree_nonrecursive(tree.root)
    print(tree_search_recursive(tree.root, 3).data, tree_search_recursive(tree.root, 10))
    print(tree.search(3).data, tree.search(10))
    print(tree.minimum().data, tree.maximum().data)
    print(tree_minimum_recursive(tree.root).data, tree_maximum_recursive(tree.root).data)
    print(tree.successor(nodes[4]).data, tree.successor(nodes[7]))
    print(tree.predecessor(nodes[4]).data, tree.predecessor(nodes[1]))
