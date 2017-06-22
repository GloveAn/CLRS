#!/usr/bin/python
from random import randint
from math import floor
from functools import partial

import sys
sys.path.append("../data_structures/")

from heap import Heap


def default_key(key): return key


# chapter 2.1
def insertion_sort(A, key=default_key):
    """ Ω(n) ~ O(n^2) """
    for j in range(1, len(A)):
        tmp = A[j]
        k = key(A[j])
        # insert A[j] into the sorted sequence A[0 .. j - 1]
        i = j - 1
        while i >= 0 and key(A[i]) > k:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = tmp


# exercises 2.2-2
def selection_sort(A, key=default_key):
    """ Θ(n^2) """
    for i in range(len(A)-1):
        m = i
        for j in range(i + 1, len(A)):
            if key(A[m]) > key(A[j]):
                m = j
        A[i], A[m] = A[m], A[i]


# exercises 2.3-4
def insertion_sort_recursive(A, key=default_key):
    def insert_recursive(A, j):
        if j > 1:
            insert_recursive(A, j - 1)
        tmp = A[j]
        k = key(A[j])
        i = j - 1
        while i >= 0 and key(A[i]) > k:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = tmp


    insert_recursive(A, len(A) - 1)


# problem 2-2
def bubble_sort(A, key=default_key):
    """ Θ(n^2) """
    for i in range(len(A) - 1):
        for j in reversed(range(i + 1, len(A))):
            if key(A[j]) < key(A[j - 1]):
                A[j], A[j - 1] = A[j - 1], A[j]


def partition(A, p, r, key):
    x = key(A[r])
    i = p

    for j in range(p, r):
        if key(A[j]) <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]

    return i


# chapter 2.3
def merge_sort_sentinels(A, key=default_key):
    def merge(A, p, q, r):
        """ A[p, q) + A[q, r) -> A[p, r) """
        INFINITY = 0xFFFFFFFF

        n1 = q - p
        n2 = r - q
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        L[ : n1] = A[p : p + n1]
        R[ : n2] = A[q : q + n2]
        L[n1] = INFINITY
        R[n2] = INFINITY

        i = 0
        j = 0
        for k in range(p, r):
            if key(L[i]) <= key(R[j]):
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1


    def merge_recursively(A, p, r):
        if p < r - 1:
            q = (p + r) // 2
            merge_recursively(A, p, q)
            merge_recursively(A, q, r)
            merge(A, p, q, r)


    merge_recursively(A, 0, len(A))


# exercises 2.3-2
def merge_sort(A, key=default_key):
    def merge(A, p, q, r):
        """ A[p, q) + A[q, r) -> A[p, r) """
        n1 = q - p
        n2 = r - q
        L = [0] * n1
        R = [0] * n2

        L[ : n1] = A[p : p + n1]
        R[ : n2] = A[q : q + n2]

        i = 0
        j = 0
        k = p

        while i < n1 and j < n2:
            if key(L[i]) <= key(R[j]):
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k += 1
        while i < n1:
            A[k] = L[i]
            k += 1
            i += 1
        while j < n2:
            A[k] = R[j]
            k += 1
            j += 1


    def merge_recursively(A, p, r):
        if p < r - 1:
            q = (p + r) // 2
            merge_recursively(A, p, q)
            merge_recursively(A, q, r)
            merge(A, p, q, r)


    merge_recursively(A, 0, len(A))


# chapter 6.4
def heap_sort(A, key=default_key):
    """ Θ(nlgn) """
    heap = Heap(A, key=key)
    for i in reversed(range(1, heap._heap_size)):
        heap._heap[0], heap._heap[i] = heap._heap[i], heap._heap[0]
        heap._heap_size -= 1
        heap._heapify(0)
    return heap._heap


# exercises 7.1-2
def modified_partition(A, p, r, key):
    x = key(A[r])
    i = p
    count = 0

    for j in range(p, r):
        if key(A[j]) <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
            if key(A[j]) == x:
                count += 1

    if count == (r - p + 1):
        return (r + p) // 2
    else:
        A[i], A[r] = A[r], A[i]
        return i


# chapter 7.3
def randomozed_partition(A, p, r, key):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r, key)


# chapter 7.1
def quick_sort(A, key=default_key, partition=partition):
    """ Ω(nlgn) ~ O(n^2) """
    def quick_sort_recursive(A, p, r):
        if p < r:
            q = partition(A, p, r, key)
            quick_sort_recursive(A, p, q - 1)
            quick_sort_recursive(A, q + 1, r)


    quick_sort_recursive(A, 0, len(A) - 1)


# problems 7-1
def quick_sort_hoare(A, key=default_key):
    def hoare_partition(A, p, r):
        """ paper:
        http://dx.doi.org/10.1093/comjnl/5.1.10
        """
        x = key(A[p])
        i = p
        j = r

        while True:
            while key(A[j]) > x:
                j -= 1
            while key(A[i]) < x:
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


# chapter 8.2
def counting_sort(A, key=default_key):
    """ Θ(n + k) """
    k = key(max(A, key=key))
    B = [0] * len(A)
    C = [0] * (k + 1)

    for a in A:
        i = key(a)
        C[i] += 1
    # C[i] now contains the number of elements equal to i

    C[k] = len(A) - C[k]
    for i in reversed(range(k)):
        C[i] = C[i + 1] - C[i]
    # C[i] now contains the number of elements less than i

    for a in A:
        i = key(a)
        B[C[i]] = a
        C[i] += + 1

    A[:] = B[:]


# chapter 8.3
def radix_sort(A, key=default_key):
    def radix_key(key, index, item):
        return key(item)[index]


    d = 0
    for a in A:
        if d < len(a):
            d = len(a)

    for i in range(d):
        counting_sort(A, key=partial(radix_key, key, i))


# chapter 8.4, exercises 8.4-1
def bucket_sort(A, key=default_key):
    n = len(A)
    B = [[] for _ in range(n)]

    for a in A:
        B[floor(key(a))].append(a)
    for b in B:
        insertion_sort(b, key)

    c = 0
    for b in B:
        for i in b:
            A[c] = i
            c += 1


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    bubble_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    insertion_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    selection_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    insertion_sort_recursive(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    quick_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    quick_sort(A, partition=modified_partition)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    quick_sort(A, partition=randomozed_partition)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    quick_sort_hoare(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    counting_sort(A)
    print(A)

    A = [
        "COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB",
        "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOW"]
    radix_sort(A, key=lambda x: [ord(i) - ord('A') for i in reversed(x)])
    print(A)

    A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
    bucket_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    merge_sort_sentinels(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    merge_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    heap_sort(A)
    print(A)


if __name__ == '__main__':
    from search import binary_search


    # exercises 2.3-7
    def sum_check_linear(A, x):
        """proof
        http://stackoverflow.com/a/40989918
        https://cs.stackexchange.com/a/1179
        """
        merge_sort(A)
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] == x:
                return True
            elif A[i] + A[j] > x:
                j -= 1
            else:
                i -= 1
        return False


    # exercises 2.3-7
    def sum_check_binary(A, x):
        merge_sort(A)
        for i in range(len(A)):
            j = binary_search(A, x - A[i])
            if i < j:
                return True
        return False


    A = [5, 2, 4, 6, 1, 3]
    print(sum_check_linear(A, 8))
    print(sum_check_linear(A, 2))
    print(sum_check_binary(A, 8))
    print(sum_check_binary(A, 2))


    # exercises 8.2-4
    class RangeQuery():
        def __init__(self, A):
            self._data_base = self._preprocess(A)
            self._max = len(self._data_base) - 1


        def _preprocess(self, A):
            k = int(max(A))
            C = [0] * (k + 1)

            for a in A:
                i = int(a)
                C[i] = C[i] + 1

            for i in range(1, k + 1):
                C[i] = C[i] + C[i - 1]

            return C


        def count(self, a, b):
            if b > self._max: b = self._max
            if a < 0:
                return self._data_base[b]
            else:
                return self._data_base[b] - self._data_base[a - 1]


    A = [5, 2, 4, 6, 1, 3]
    rq = RangeQuery(A)
    print("[-1, 100]:", rq.count(-1, 100))
    print("[2, 4]:", rq.count(2, 4))
