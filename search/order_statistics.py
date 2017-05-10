#!/usr/bin/python
import sys
sys.path.append("../sort")
from quick_sort import partition, randomozed_partition


# chapter 9.1
def minimum(A):
    m = A[0]
    for i in range(1, len(A)):
        if m > A[i]:
            m = A[i]
    return m


def maximum(A):
    m = A[0]
    for i in range(1, len(A)):
        if m < A[i]:
            m = A[i]
    return m


# exercises 9.1-1
def second_smallest(A):
    def second_smallest_recursive(A, i, j):
        if i < j - 1:
            m = (i + j) >> 1
            left_min, left_over = second_smallest_recursive(A, i, m)
            right_min, right_over = second_smallest_recursive(A, m, j)

            if left_min < right_min:
                left_over.append(right_min)
                return left_min, left_over
            else:
                right_over.append(left_min)
                return right_min, right_over
        else:
            return A[i], []


    all_min, all_over = second_smallest_recursive(A, 0, len(A))
    sencond_min = all_over[0]
    for i in range(1, len(all_over)):
        if sencond_min > all_over[i]:
            sencond_min = all_over[i]

    return all_min, sencond_min


# exercises 9.1-2
def min_max(A):
    mi = A[0]
    ma = A[0]

    n = len(A)
    i = 2

    while i < n:
        a, b = (A[i - 1], A[i]) if A[i - 1] < A[i] else (A[i], A[i - 1])
        mi = mi if mi < a else a
        ma = ma if ma > b else b

        i += 2

    if not n & 1:
        n -= 1
        mi = mi if mi < A[n] else A[n]
        ma = ma if ma > A[n] else A[n]

    return mi, ma


# chapter 9.2
def randomized_select(A, i, partition=randomozed_partition):
    def select_recursive(A, p, r, i):
        if p == r:
            return A[p]

        q = partition(A, p ,r)
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

            q = partition(A, p, r)
            k = q - p
            if i == k:
                return A[q]
            elif i < k:
                r = q - 1
            else:
                p = q + 1
                i = i - k -1


    return select(A, 0, len(A) - 1, i)


if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    print(minimum(A), maximum(A))
    print(*second_smallest(A))
    print(*min_max(A))
    print(randomized_select(A, 3))
