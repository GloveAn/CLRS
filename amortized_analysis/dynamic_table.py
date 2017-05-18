#!/usr/bin/python
# chapter 17.4


class DynamicTable():
    def __init__(self):
        self._size = 0
        self._num = 0
        self._table = None


    def insert(self, x):
        if self._size == 0:
            self._table = [None]
            self._size = 1
        if self._num == self._size:
            new_table = [None] * (self._size * 2)
            for i in range(self._size):
                new_table[i] = self._table[i]
            self._table = new_table
            self._size = 2 * self._size
        self._table[self._num] = x
        self._num = self._num + 1


    def delete(self):
        self._num = self._num - 1
        x = self._table[self._num]
        if self._num * 4 <= self._size:
            new_table = [None] * (self._size // 2)
            for i in range(self._num):
                new_table[i] = self._table[i]
            self._table = new_table
            self._size = self._size // 2
        return x


if __name__ == "__main__":
    t = DynamicTable()
    for i in range(10):
        t.insert(i)
    print(t._size, t._num, t._table)
    for i in range(10):
        x = t.delete()
        print(x, end=' ')
    print(t._table)
    print(t._size, t._num)
