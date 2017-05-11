#!/usr/bin/python
# chapter 15.5
import sys


def optimal_bst(p, q):
    INFINITY = sys.float_info.max

    n = len(p)
    e = [[INFINITY for i in range(n + 1)] for j in range(n + 1)]
    w = [[INFINITY for i in range(n + 1)] for j in range(n + 1)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i, j):
                t = e[i][r] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j - 1] = r

    return (e, root)


# exercises 15.5-1
def construct_optimal_bst(root):
    def construct_optimal_bst_aux(root, i, j, k):
        if i <= j:
            if j < k:
                print("k", root[i][j] + 1, " is the left child of k", k + 1, sep='')
            else:
                print("k", root[i][j] + 1, " is the right child of k", k + 1, sep='')
            k = root[i][j]
            construct_optimal_bst_aux(root, i, k - 1, k)
            construct_optimal_bst_aux(root, k + 1, j, k)
        else:
            if j < k:
                print("d", i, " is the left child of k", k + 1, sep='')
            else:
                print("d", i, " is the right child of k", k + 1, sep='')


    i = 0
    j = len(root[0]) - 1
    k = root[0][j]

    if i - 1 < j:
        print("k", k + 1, " is the root", sep='')
    construct_optimal_bst_aux(root, i, k - 1, k)
    construct_optimal_bst_aux(root, k + 1, j, k)


if __name__ == "__main__":
    p = [0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    (e, root) = optimal_bst(p, q)
    construct_optimal_bst(root)
