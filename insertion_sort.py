#!/usr/bin/python
# Ω(n) ~ O(n^2)


# chapter 2.1
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted sequence A[0 .. j - 1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


# exercises 2.3-4
def insertion_sort_recursion(A):
    def insert_recursively(A, j):
        if j > 1:
            insert_recursively(A, j - 1)
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


    insert_recursively(A, len(A) - 1)


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    insertion_sort(A)
    print(A)
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    insertion_sort_recursion(A)
    print(A)
