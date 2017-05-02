#!/usr/bin/python


class Node():
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None


    # chapter 12.3
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


    # chapter 12.3
    def _transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent


    # chapter 12.3
    def delete(self, z):
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = tree_minimum(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y


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
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


# chapter 12.2
def tree_search(x, k):
    while x is not None and k != x.data:
        if k < x.data:
            x = x.left
        else:
            x = x.right
    return x


# chapter 12.2
def tree_minimum(x):
    if x is None:
        return x
    while x.left is not None:
        x = x.left
    return x


# exercises 12.2-2
def tree_minimum_recursive(x):
    if x is None or x.left is None:
        return x
    else:
        return tree_minimum_recursive(x.left)


# chapter 12.2
def tree_maximum(x):
    if x is None:
        return x
    while x.right is not None:
        x = x.right
    return x


# exercises 12.2-2
def tree_maximum_recursive(x):
    if x is None or x.right is None:
        return x
    else:
        return tree_maximum_recursive(x.right)


# chapter 12.2
def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


# exercises 12.2-3
def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.parent
    while y is not None and x == y.left:
        x = y
        y = y.parent
    return y


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
    print(tree_search(tree.root, 3).data, tree_search(tree.root, 10))
    print(tree_minimum(tree.root).data, tree_maximum(tree.root).data)
    print(tree_minimum_recursive(tree.root).data, tree_maximum_recursive(tree.root).data)
    print(tree_successor(nodes[4]).data, tree_successor(nodes[7]))
    print(tree_predecessor(nodes[4]).data, tree_predecessor(nodes[1]))
