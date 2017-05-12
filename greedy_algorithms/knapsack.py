#!/usr/bin/python
# chapter 16.2


# exercises 16.2-2
def knapsack01(v, w, W):
    """ idea
    DP[i, j] = max{ DP[i-1, j], DP[i-1, j-w(i)] + v(i) }
        i: the i-th item
        j: how much weight we have in the knapsack
    """
    n = len(v)

    c = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(W + 1)] for _ in range(n)]

    for i in range(n):
        for j in range(W + 1):
            c[i + 1][j] = c[i][j]
            s[i][j] = j
            if j - w[i] >= 0:
                t = c[i][j - w[i]] + v[i]
                if t > c[i + 1][j]:
                    c[i + 1][j] = t
                    s[i][j] = j - w[i]

    return (c, s)


if __name__ == "__main__":
    v = [60, 100, 120]
    w = [10, 20, 30]

    (c, s) = knapsack01(v, w, 50)
    print(c[-1][-1])

    choice = []
    j = 50
    for i in reversed(range(len(s))):
        if s[i][j] != j:
            j = s[i][j]
            choice.append(i + 1)
    choice.reverse()
    print(choice)
