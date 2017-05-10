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

        L[ : n1] = A[p : p + n1]
        R[ : n2] = A[q : q + n2]
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

        L[ : n1] = A[p : p + n1]
        R[ : n2] = A[q : q + n2]

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
    import sys
    sys.path.append("../search")
    from binary_search import binary_search


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
    merge_sort_sentinels(A)
    print(A)
    A = [5, 2, 4, 6, 1, 3]
    merge_sort(A)
    print(A)

    A = [5, 2, 4, 6, 1, 3]
    print(sum_check_linear(A, 8))
    print(sum_check_linear(A, 2))
    print(sum_check_binary(A, 8))
    print(sum_check_binary(A, 2))
