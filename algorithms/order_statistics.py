#!/usr/bin/python


# chapter 9.1
def minimum(A):
    m = A[0]
    for i in range(1, len(A)):
        if m > A[i]:
            m = A[i]
    return m


def maximum(A):
    m = A[0]
    for i in range(1, len(A)):
        if m < A[i]:
            m = A[i]
    return m


if __name__ == "__main__":
    A = [3, 1, 4, 1, 5, 9, 2, 6]
    print(minimum(A), maximum(A))
