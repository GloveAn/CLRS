#!/usr/bin/python
# chapter 15.4


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    b = [[0 for _ in range(n)] for _ in range(m)]
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = "\\"
            elif c[i][j + 1] >= c[i + 1][j]:
                c[i + 1][j + 1] = c[i][j + 1]
                b[i][j] = "|"
            else:
                c[i + 1][j + 1] = c[i + 1][j]
                b[i][j] = "-"

    return (c, b)


def print_lcs(b, X, i, j):
    if i < 0 or j < 0:
        return
    if b[i][j] == "\\":
        print_lcs(b, X, i - 1, j - 1)
        print(X[i], end='')
    elif b[i][j] == "|":
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)


def print_lcs_modified(c, X, i, j):
    if i < 0 or j < 0:
        return
    if c[i][j] == c[i - 1][j]:
        print_lcs_modified(c, X, i - 1, j)
    elif c[i][j] == c[i][j - 1]:
        print_lcs_modified(c, X, i, j - 1)
    else:
        print_lcs_modified(c, X, i - 1, j - 1)
        print(X[i - 1], end='')


# exercises 15.4-4
def lcs_length_modified1(X, Y):
    m = len(X)
    n = len(Y)

    if m < n:
        m, n = n, m
        X, Y = Y, X

    c = [0] * (n + 1)
    d = [0] * (n + 1)

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                d[j + 1] = c[j] + 1
            elif c[j + 1] >= d[j]:
                d[j + 1] = c[j + 1]
            else:
                d[j + 1] = d[j]
        c, d = d, c

    return d[-1]


# exercises 15.4-4
def lcs_length_modified2(X, Y):
    m = len(X)
    n = len(Y)

    if m < n:
        m, n = n, m
        X, Y = Y, X

    c = [0] * (n + 1)

    for i in range(m):
        d = 0

        for j in range(n):
            c[j] = d

            if X[i] == Y[j]:
                d = c[j] + 1
            elif c[j + 1] >= d:
                d = c[j + 1]
            else:
                d = d

        c[-1] = d

    return c[-1]


# exercises 15.4-6
def longest_monotonically_increasing_subsequence(X):
    # http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    def binary_search(X, a):
        i = 0
        j = len(X) - 1

        while i <= j:
            m = (i + j) // 2

            if X[m] == a:
                return m
            elif X[m] < a:
                i = m + 1
            else:
                j = m - 1

        return j


    INFINITY = 0x7FFFFFFF

    m = len(X)
    B = [INFINITY] * m
    C = [None] * m

    B[0] = X[0]
    C[0] = [X[0]]
    L = 0

    for i in range(1, m):
        if X[i] < B[0]:
            B[0] = X[i]
            C[0] = [X[i]]
        else:
            j = binary_search(B, X[i])
            B[j + 1] = X[i]
            C[j + 1] = C[j] + [X[i]]
            if j == L:
                L += 1

    return C[L]


if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    (c, b) = lcs_length(X, Y)
    print_lcs(b, X, len(X) - 1, len(Y) - 1)
    print()
    print_lcs_modified(c, X, len(X), len(Y))
    print()
    print(lcs_length_modified1(X, Y))
    print(lcs_length_modified2(X, Y))
    X = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(longest_monotonically_increasing_subsequence(X))
