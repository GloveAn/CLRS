#!/usr/bin/python
from random import randint
from merge_sort import merge_sort


# chapter 5.3
def permute_by_sorting(A):
    B = A.copy()

    n = len(A)
    n3 = n * n * n
    P = [None] * n
    for i in range(n):
        P[i] = (randint(1, n3), i)
    merge_sort(P)
    for i in range(n):
        A[i] = B[P[i][1]]


# chapter 5.3
def randomize_in_place(A):
    n = len(A) - 1
    for i in range(n):
        r = randint(i, n)
        A[i], A[r] = A[r], A[i]


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    permute_by_sorting(A)
    print(A)
    randomize_in_place(A)
    print(A)
