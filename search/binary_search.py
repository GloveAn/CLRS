#!/usr/bin/python
# Ω(1) ~ O(lgn)


# exercises 2.3-5
def binary_search(A, v):
    i = 0
    j = len(A) - 1

    while i <= j:
        m = (i + j) // 2

        if A[m] == v:
            return m
        elif A[m] < v:
            i = m + 1
        else:
            j = m - 1

    return -1


# exercises 2.3-5
def binary_search_recursion(A, v):
    def search_recursively(A, i, j):
        if i > j:
            return -1

        m = (i + j) // 2

        if A[m] == v:
            return m
        elif A[m] < v:
            return search_recursively(A, m + 1, j)
        else:
            return search_recursively(A, i, m - 1)


    return search_recursively(A, 0, len(A) - 1)


if __name__ == '__main__':
    A = [1, 3, 5, 7, 9]
    print(binary_search(A, 3))
    print(binary_search(A, 4))
    print(binary_search_recursion(A, 3))
    print(binary_search_recursion(A, 4))
