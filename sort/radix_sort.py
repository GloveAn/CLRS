#!/usr/bin/python
import sys
sys.path.append("../assumptions")
from counting_sort import counting_sort
from pair import Pair


class RadixPair(Pair):
    order = 0
    def __init__(self, key, value=None):
        Pair.__init__(self, key, value)

        self._digits = self._split_key()


    def __len__(self):
        return len(self._digits)


    def __int__(self):
        if RadixPair.order < len(self._digits):
            return self._digits[RadixPair.order]
        else:
            return 0


    def key(self, k=None):
        if k:
            self._key = k
        else:
            return int(self)


    def _split_key():
        # self._digits = []
        raise NotImplementedError


# chapter 8.3
def radix_sort(A):
    d = 0
    for a in A:
        if d < len(a):
            d = len(a)

    for i in range(d):
        RadixPair.order = i
        counting_sort(A)


# exercises 8.3-1
if __name__ == '__main__':
    class CharRadixPair(RadixPair):
        def _split_key(self):
            return [ord(c) - ord('A') for c in reversed(self._key)]


    A = [
        "COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB",
        "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOW"]
    for i in range(len(A)):
        A[i] = CharRadixPair(A[i])
    radix_sort(A)
    print(A)
