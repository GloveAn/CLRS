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
    pass


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
