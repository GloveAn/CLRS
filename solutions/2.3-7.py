#!/usr/bin/python

import sys
sys.path.append("../algorithms")
from merge_sort import merge_sort
from binary_search import binary_search


def sum_ckeck_linear(A, x):
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


def sum_check_binary(A, x):
    merge_sort(A)
    for i in range(len(A)):
        j = binary_search(A, x - A[i])
        if i < j:
            return True
    return False


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(sum_ckeck_linear(A, 8))
    print(sum_ckeck_linear(A, 2))
    print(sum_check_binary(A, 8))
    print(sum_check_binary(A, 2))
