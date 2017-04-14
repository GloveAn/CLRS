#!/usr/bin/python
# Θ(nlgn)


# chapter 2.3
def merge_sort_sentinels(A):
    def merge(A, p, q, r):
        """ A[p, q) + A[q, r) -> A[p, r) """
        INFINITY = 0xFFFFFFFF

        n1 = q - p
        n2 = r - q
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        for i in range(n1):
            L[i] = A[p + i]
        for j in range(n2):
            R[j] = A[q + j]
        L[n1] = INFINITY
        R[n2] = INFINITY

        i = 0
        j = 0
        for k in range(p, r):
            if L[i] <= R[j]:
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
def merge_sort(A):
    def merge(A, p, q, r):
        """ A[p, q) + A[q, r) -> A[p, r) """
        n1 = q - p
        n2 = r - q
        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = A[p + i]
        for j in range(n2):
            R[j] = A[q + j]

        i = 0
        j = 0
        k = p

        while i < n1 and j < n2:
            if L[i] <= R[j]:
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


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    merge_sort_sentinels(A)
    print(A)
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    merge_sort(A)
    print(A)
