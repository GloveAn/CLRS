#!/usr/bin/python
from math import floor
from insertion_sort import insertion_sort


# chapter 8.4, exercises 8.4-1
def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in A:
        B[floor(i)].append(i)
    for i in B:
        insertion_sort(i)

    c = 0
    for i in B:
        for j in i:
            A[c] = j
            c += 1


if __name__ == "__main__":
    A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
    bucket_sort(A)
    print(A)
