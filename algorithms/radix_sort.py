#!/usr/bin/python
from counting_sort import counting_sort


# chapter 8.3, exercises 8.3-1
def radix_sort(A):
    def counting_sort(A, d):  # char in string only
        B = [0] * len(A)
        C = [0] * 26

        for i in range(len(A)):
            C[ord(A[i][d]) - ord('A')] += 1
        C[25] = len(A) - C[25]
        for i in reversed(range(25)):
            C[i] = C[i + 1] - C[i]
        for i in range(len(A)):
            B[C[ord(A[i][d]) - ord('A')]] = A[i]
            C[ord(A[i][d]) - ord('A')] += 1

        for i in range(len(A)):
            A[i] = B[i]


    # Assum same length for strings in the list
    for i in reversed(range(len(A[0]))):
        counting_sort(A, i)


if __name__ == '__main__':
    A = [
        "COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB",
        "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOW"]
    print(A)
    radix_sort(A)
    print(A)
