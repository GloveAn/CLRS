#!/usr/bin/python
# Θ(n^2)


# exercises 2.2-2
def selection_sort(A):
    for i in range(len(A)-1):
        m = i
        for j in range(i + 1, len(A)):
            if A[m] > A[j]:
                m = j
        A[i], A[m] = A[m], A[i]


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    selection_sort(A)
    print(A)
