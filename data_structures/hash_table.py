#!/usr/bin/python
import sys
sys.path.append("../assumptions")
from pair import Pair


class Hash():
    def search(self, k):
        raise NotImplementedError


    def insert(self, x):
        raise NotImplementedError


    def delete(self, x):
        raise NotImplementedError


# chapter 11.1
class DirectAddressHash(Hash):
    def __init__(self, u):
        self._table = [None] * u


    def search(self, k):
        return self._table[k]


    def insert(self, x):
        self._table[x.key()] = x


    def delete(self, x):
        self._table[x.key()] = None


# chapter 11.2
class ChainedHash(Hash):
    def __init__(self, u, h):
        self._table = [None] * u
        self._hash = h


    def insert(self, x):
        self._table[self._hash(x.key())].append(x)


    def search(self, k):
        for kv in self._table[self._hash(k)]:
            if kv.key() == k:
                return kv
        return None


    def delete(self, x):
        try:
            self._table[self._hash(x.key())].remove(x)
        except:
            pass
