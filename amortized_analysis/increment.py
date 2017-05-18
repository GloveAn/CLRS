#!/usr/bin/python
# chapter 17.3


def increment(A):
    i = 0
    while i < len(A) and A[i] == 1:
        A[i] = 0
        i = i + 1
    if i < len(A):
        A[i] = 1


if __name__ == "__main__":
    A = [0] * 8
    for _ in range(17):
        for i in reversed(range(8)):
            print(A[i], end=' ')
        print()
        increment(A)
