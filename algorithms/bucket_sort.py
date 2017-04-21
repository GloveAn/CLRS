#!/usr/bin/python
from math import floor
from insertion_sort import insertion_sort


# chapter 8.4, exercises 8.4-1
def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for a in A:
        B[floor(a)].append(a)
    for b in B:
        insertion_sort(b)

    c = 0
    for b in B:
        for i in b:
            A[c] = i
            c += 1


if __name__ == "__main__":
    A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
    bucket_sort(A)
    print(A)
