#!/usr/bin/python
# chapter 16.3
import sys
sys.path.append("../assumptions")
sys.path.append("../data_structures")
sys.path.append("../tree")
import pair
from heap import PriorityQueue, MinHeap
import binary_search_tree


class Node(pair.Pair, binary_search_tree.Node):
    def __init__(self, key, value=None):
        pair.Pair.__init__(self, key, value)
        binary_search_tree.Node.__init__(self, (key, value))


def huffman(C):
    n = len(C)
    Q = PriorityQueue(C, MinHeap)
    for i in range(n - 1):
        x = Q.extract_min()
        y = Q.extract_min()
        z = Node(x.key() + y.key())
        z.left = x
        z.right = y
        Q.insert(z)
    return Q.extract_min()


if __name__ == "__main__":
    c = ["a", "b", "c", "d", "e", "f", "g", "h"]
    f = [1, 1, 2, 3, 5, 8, 13, 21]

    for i in range(len(c)):
        c[i] = Node(f[i], c[i])
    binary_search_tree.preorder_tree_walk(huffman(c))
