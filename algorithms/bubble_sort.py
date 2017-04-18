#!/usr/bin/python
# Θ(n^2)


# problem 2-2
def bubble_sort(A):
    for i in range(len(A) - 1):
        for j in reversed(range(i + 1, len(A))):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    bubble_sort(A)
    print(A)
