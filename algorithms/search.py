#!/usr/bin/python

from sort import default_key
from sort import randomozed_partition


# exercises 2.3-5
def binary_search(A, v, key=default_key):
    """ Ω(1) ~ O(lgn) """
    i = 0
    j = len(A) - 1

    while i <= j:
        m = (i + j) // 2

        if key(A[m]) == key(v):
            return m
        elif key(A[m]) < key(v):
            i = m + 1
        else:
            j = m - 1

    return -1


# exercises 2.3-5
def binary_search_recursion(A, v, key=default_key):
    def search_recursively(A, i, j):
        if i > j:
            return -1

        m = (i + j) // 2

        if key(A[m]) == key(v):
            return m
        elif key(A[m]) < key(v):
            return search_recursively(A, m + 1, j)
        else:
            return search_recursively(A, i, m - 1)


    return search_recursively(A, 0, len(A) - 1)


# chapter 9.1
def minimum(A, key=default_key):
    m = 0
    for i in range(1, len(A)):
        if key(A[m]) > key(A[i]):
            m = i
    return A[m]


def maximum(A, key=default_key):
    m = 0
    for i in range(1, len(A)):
        if key(A[m]) < key(A[i]):
            m = i
    return A[m]


# exercises 9.1-1
def second_smallest(A, key=default_key):
    def second_smallest_recursive(A, i, j, key=key):
        if i < j - 1:
            m = (i + j) >> 1
            left_min, left_over = second_smallest_recursive(A, i, m)
            right_min, right_over = second_smallest_recursive(A, m, j)

            if key(left_min) < key(right_min):
                left_over.append(right_min)
                return left_min, left_over
            else:
                right_over.append(left_min)
                return right_min, right_over
        else:
            return A[i], []


    all_min, all_over = second_smallest_recursive(A, 0, len(A))
    sencond_min = minimum(all_over, key=key)

    return all_min, sencond_min


# exercises 9.1-2
def min_max(A, key=default_key):
    mi = 0
    ma = 0

    n = len(A)
    i = 2

    while i < n:
        a, b = (i - 1, i) if key(A[i - 1]) < key(A[i]) else (i, i - 1)
        mi = mi if key(A[mi]) < key(A[a]) else a
        ma = ma if key(A[ma]) > key(A[b]) else b

        i += 2

    if not n & 1:
        n -= 1
        mi = mi if key(A[mi]) < key(A[n]) else n
        ma = ma if key(A[ma]) > key(A[n]) else n

    return A[mi], A[ma]


# chapter 9.2
def randomized_select(A, i, key=default_key, partition=randomozed_partition):
    def select_recursive(A, p, r, i):
        if p == r:
            return A[p]

        q = partition(A, p ,r, key)
        k = q - p
        if i == k:
            return A[q]
        elif i < k:
            return select_recursive(A, p, q - 1, i)
        else:
            return select_recursive(A, q + 1, r, i - k - 1)


    def select(A, p, r, i):
        while True:
            if p == r:
                return A[p]

            q = partition(A, p, r, key)
            k = q - p
            if i == k:
                return A[q]
            elif i < k:
                r = q - 1
            else:
                p = q + 1
                i = i - k -1


    return select(A, 0, len(A) - 1, i)


if __name__ == '__main__':
    A = [1, 3, 5, 7, 9]
    print(binary_search(A, 3))
    print(binary_search(A, 4))
    print(binary_search_recursion(A, 3))
    print(binary_search_recursion(A, 4))

    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    print(minimum(A), maximum(A))
    print(*second_smallest(A))
    print(*min_max(A))
    print(randomized_select(A, 3))
