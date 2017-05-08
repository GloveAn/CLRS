#!/usr/bin/python
# chapter 15.1


def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [-1] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return (r, s)


def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n], end=" ")
        n = n - s[n]


# exercises 15.1-3
def cost_rod_cut(p, n, c):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        r[j] = p[j]
        for i in range(1, j + 1):
            r[j] = max(r[j], p[i] + r[j - i] - c)
    return r[n]


# exercises 15.1-5
def fibonacci(n):
    a = 1
    b = 0
    while n:
        b = a + b
        a, b = b, a
        n -= 1
    return a


if __name__ == "__main__":
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for i in range(1, len(p)):
        print(cut_rod(p, i))
        print(memoized_cut_rod(p, i))
        print(bottom_up_cut_rod(p, i))

    for i in range(1, len(p)):
        print_cut_rod_solution(p, i)
        print()

    for i in range(10):
        print(fibonacci(i))
