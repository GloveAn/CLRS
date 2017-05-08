#!/usr/bin/python
# chapter 15.2


def matrix_chain_order(p):
    INFINITY = 0x7FFFFFFF

    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = INFINITY
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return (m, s)


def print_optimal_parents(s, i, j):
    if i == j:
        print("A", i, sep='', end='')
    else:
        print("(", end='')
        print_optimal_parents(s, i, s[i][j])
        print_optimal_parents(s, s[i][j] + 1, j)
        print(")", end='')


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    (r, s) = matrix_chain_order(p)
    print_optimal_parents(s, 0, 5)
    print()
