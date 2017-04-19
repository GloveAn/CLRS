#!/usr/bin/python


# chapter 4.2
class MatrixBasic:
    def __init__(self, A):
        self._matrix = A
        self._length = len(A)


    def __add__(self, B):
        C = self._empty(self._length)
        for i in range(self._length):
            for j in range(self._length):
                C[i][j] = self._matrix[i][j] + B._matrix[i][j]
        return self.__class__(C)


    def __sub__(self, B):
        C = self._empty(self._length)
        for i in range(self._length):
            for j in range(self._length):
                C[i][j] = self._matrix[i][j] - B._matrix[i][j]
        return self.__class__(C)


    def __mul__(self, B):
        C = self._empty(self._length)
        for i in range(self._length):
            for j in range(self._length):
                for k in range(self._length):
                    C[i][j] += self._matrix[i][k] * B._matrix[k][j]
        return self.__class__(C)


    def __str__(self):
        max_element = self._matrix[0][0]
        min_element = self._matrix[0][0]
        for i in range(self._length):
            for j in range(self._length):
                if max_element < self._matrix[i][j]:
                    max_element = self._matrix[i][j]
                if min_element > self._matrix[i][j]:
                    min_element = self._matrix[i][j]
        width = max(len(str(max_element)), len(str(min_element)))

        string = []
        for i in range(self._length):
            r = ["%*d" % (width, e) for e in self._matrix[i]]
            string.append(" ".join(r))
        return "\n".join(string)


    def _empty(self, n):
        R = [None] * n
        for i in range(n):
            R[i] = [0] * n
        return R


# chapter 4.2
class MatrixDivideConquer(MatrixBasic):
    def __mul__(self, B):
        if self._length == 1:
            C = self.__class__([[self._matrix[0][0] * B._matrix[0][0]]])
        else:
            half = self._length >> 1

            A = self._partition(self)
            B = self._partition(B)
            L = [[None, None], [None, None]]

            L[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
            L[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
            L[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
            L[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]

            C = self._merge(L)

        return C


    def _partition(self, A):
        half = A._length >> 1
        R00 = self._empty(half)
        R01 = self._empty(half)
        R10 = self._empty(half)
        R11 = self._empty(half)

        L = [[None, None], [None, None]]

        for i in range(half):
            for j in range(half):
                R00[i][j] = A._matrix[i][j]
                R01[i][j] = A._matrix[i][j + half]
                R10[i][j] = A._matrix[i + half][j]
                R11[i][j] = A._matrix[i + half][j + half]
        L[0][0] = self.__class__(R00)
        L[0][1] = self.__class__(R01)
        L[1][0] = self.__class__(R10)
        L[1][1] = self.__class__(R11)

        return L


    def _merge(self, R):
        half = R[0][0]._length
        n = half << 1
        A = self._empty(n)
        for i in range(half):
            for j in range(half):
                 A[i][j] = R[0][0]._matrix[i][j]
                 A[i][j + half] = R[0][1]._matrix[i][j]
                 A[i + half][j] = R[1][0]._matrix[i][j]
                 A[i + half][j + half] = R[1][1]._matrix[i][j]

        return self.__class__(A)


# exercises 4.2-1, exercises 4.2-2
class MatrixStrassen(MatrixDivideConquer):
    def __mul__(self, B):
        if self._length == 1:
            C = self.__class__([[self._matrix[0][0] * B._matrix[0][0]]])
        else:
            A = self._partition(self)
            B = self._partition(B)
            C = [[None, None], [None, None]]
            S = [None] * 10
            P = [None] * 7

            S[0] = B[0][1] - B[1][1]
            S[1] = A[0][0] + A[0][1]
            S[2] = A[1][0] + A[1][1]
            S[3] = B[1][0] - B[0][0]
            S[4] = A[0][0] + A[1][1]
            S[5] = B[0][0] + B[1][1]
            S[6] = A[0][1] - A[1][1]
            S[7] = B[1][0] + B[1][1]
            S[8] = A[0][0] - A[1][0]
            S[9] = B[0][0] + B[0][1]

            P[0] = A[0][0] * S[0]
            P[1] = S[1] * B[1][1]
            P[2] = S[2] * B[0][0]
            P[3] = A[1][1] * S[3]
            P[4] = S[4] * S[5]
            P[5] = S[6] * S[7]
            P[6] = S[8] * S[9]

            C[0][0] = P[4] + P[3] - P[1] + P[5]
            C[0][1] = P[0] + P[1]
            C[1][0] = P[2] + P[3]
            C[1][1] = P[4] + P[0] - P[2] - P[6]

            C = self._merge(C)

        return C


# exercises 4.2-3
class Matrix(MatrixStrassen):
    def __mul__(self, B):
        if (self._length - 1) & self._length:
            A = self._padding(A)
            B = self._padding(B)
        A = MatrixStrassen(self._matrix)
        B = MatrixStrassen(B._matrix)

        C = A * B

        C = self.__class__(C._matrix)
        if (self._length - 1) & self._length:
            C = self._depadding(C)

        return C


    def _padding(self, A):
        # find next highest power of 2, proof
        # http://graphics.stanford.edu/~seander/bithacks.html#RoundUpPowerOf2
        n = self._length
        n -= 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        n += 1

        C = self._empty(n)
        for i in range(len(A)):
            for j in range(len(A)):
                C[i][j] = A._matrix[i][j]

        return self.__class__(C)


    def _depadding(self, A):
        C = self._empty(self._length)
        for i in range(self._length):
            for j in range(self._length):
                C[i][j] = A._matrix[i][j]

        return self.__class__(C)


if __name__ == "__main__":
    A = [[1,3],[7,5]]
    B = [[6,8],[4,2]]

    print(MatrixBasic(A) * MatrixBasic(B))
    print()
    print(MatrixDivideConquer(A) * MatrixDivideConquer(B))
    print()
    print(MatrixStrassen(A) * MatrixStrassen(B))
    print()
    print(Matrix(A) * Matrix(B))
