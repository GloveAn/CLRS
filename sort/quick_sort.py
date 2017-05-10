#!/usr/bin/python
# Ω(nlgn) ~ O(n^2)
from random import randint


def partition(A, p, r):
    x = A[r]
    i = p

    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]

    return i


# exercises 7.1-2
def modified_partition(A, p, r):
    x = A[r]
    i = p
    count = 0

    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
            if A[j] == x:
                count += 1

    if count == (r - p + 1):
        return (r + p) // 2
    else:
        A[i], A[r] = A[r], A[i]
        return i


# chapter 7.3
def randomozed_partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


# chapter 7.1
def quick_sort(A, partition=partition):
    def quick_sort_recursive(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quick_sort_recursive(A, p, q - 1)
            quick_sort_recursive(A, q + 1, r)


    quick_sort_recursive(A, 0, len(A) - 1)


# problems 7-1
def quick_sort_hoare(A):
    def hoare_partition(A, p, r):
        """ paper:
        http://dx.doi.org/10.1093/comjnl/5.1.10
        """
        x = A[p]
        i = p
        j = r

        while True:
            while A[j] > x:
                j -= 1
            while A[i] < x:
                i += 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                return j


    def quick_sort_recursive(A, p, r):
        if p < r:
            q = hoare_partition(A, p, r)
            quick_sort_recursive(A, p, q)
            quick_sort_recursive(A, q + 1, r)


    quick_sort_recursive(A, 0, len(A) - 1)


if __name__ == "__main__":
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A)
    print(A)
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A, partition=modified_partition)
    print(A)
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A, partition=randomozed_partition)
    print(A)
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort_hoare(A)
    print(A)
