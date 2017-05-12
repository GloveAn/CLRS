#!/usr/bin/python
# chapter 16.1


def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k]:
        m += 1
    l = [k + 1]
    if m < n:
        l.extend(recursive_activity_selector(s, f, m, n))
    return l


def greedy_activity_selector(s, f):
    n = len(s)
    A = [1]
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m + 1)
            k = m
    return A


if __name__ == "__main__":
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    print(recursive_activity_selector(s, f, 0, len(s)))
    print(greedy_activity_selector(s, f))
