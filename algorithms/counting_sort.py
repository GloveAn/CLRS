#!/usr/bin/python
# Θ(n + k)


# chapter 8.2
def counting_sort(A):
    k = int(max(A))
    B = [0] * len(A)
    C = [0] * (k + 1)

    for a in A:
        i = int(a)
        C[i] += 1
    # C[i] now contains the number of elements equal to i

    C[k] = len(A) - C[k]
    for i in reversed(range(k)):
        C[i] = C[i + 1] - C[i]
    # C[i] now contains the number of elements less than i

    for a in A:
        i = int(a)
        B[C[i]] = a
        C[i] += + 1

    A[:] = B[:]


# exercises 8.2-4
class RangeQuery():
    def __init__(self, A):
        self._data_base = self._preprocess(A)
        self._max = len(self._data_base) - 1


    def _preprocess(self, A):
        k = int(max(A))
        C = [0] * (k + 1)

        for a in A:
            i = int(a)
            C[i] = C[i] + 1

        for i in range(1, k + 1):
            C[i] = C[i] + C[i - 1]

        return C


    def count(self, a, b):
        if b > self._max: b = self._max
        if a < 0:
            return self._data_base[b]
        else:
            return self._data_base[b] - self._data_base[a - 1]


if __name__ == "__main__":
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    counting_sort(A)
    print(A)

    rq = RangeQuery(A)
    print("[-1, 100]:", rq.count(-1, 100))
    print("[2, 4]:", rq.count(2, 4))
