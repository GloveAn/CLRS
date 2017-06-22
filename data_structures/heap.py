#!/usr/bin/python


def default_key(key): return key


class Heap():
    def __init__(self, A, key=default_key):
        self._heap = A
        self._heap_size = len(A)
        self._key = key
        self._build()


    def __len__(self):
        return self._heap_size


    def _heapify_recursive(self, i):
        l = i << 1
        l = l + 1
        r = l + 1
        largest = i

        if l < self._heap_size \
        and self._key(self._heap[l]) > self._key(self._heap[i]):
            largest = l
        if r < self._heap_size \
        and self._key(self._heap[r]) > self._key(self._heap[largest]):
            largest = r
        if largest != i:
            self._heap[i], self._heap[largest] = \
                self._heap[largest], self._heap[i]
            self._heapify(largest)


    # exercises 6.2-5
    def _heapify(self, i):
        while i < self._heap_size:
            l = i << 1
            l = l + 1
            r = l + 1
            largest = i

            if l < self._heap_size \
            and self._key(self._heap[l]) > self._key(self._heap[i]):
                largest = l
            if r < self._heap_size \
            and self._key(self._heap[r]) > self._key(self._heap[largest]):
                largest = r
            if largest == i:
                break
            else:
                self._heap[i], self._heap[largest] = \
                    self._heap[largest], self._heap[i]
                i = largest


    # chapter 6.3
    def _build(self):  # O(n)
        for i in reversed(range(self._heap_size >> 1)):
            self._heapify(i)


    def top(self):
        return self._heap[0]


    def extract_top(self):
        # if self._queue._heap_size < 1:
        #     raise IndexError
        top = self._heap[0]
        self._heap_size -= 1
        if self._heap_size:
            self._heap[0] = self._heap.pop()
            self._heapify(0)
        else:
            self._heap.pop()

        return top


    def change_item_origin(self, i, item):
        if i != self._heap_size:
            assert self._key(item) >= self._key(self._heap[i])
        self._heap[i] = item
        parent = (i - 1) >> 1
        while i > 0 \
        and self._key(self._heap[parent]) < self._key(self._heap[i]):
            self._heap[parent], self._heap[i] = \
                self._heap[i], self._heap[parent]
            i = parent
            parent = (i - 1) >> 1


    # exercises 6.5-6
    def change_item(self, i, item):
        if i != self._heap_size:
            assert self._key(item) >= self._key(self._heap[i])
        parent = (i - 1) >> 1
        while i > 0 and self._key(self._heap[parent]) < self._key(item):
            self._heap[i] = self._heap[parent]
            i = parent
            parent = (i - 1) >> 1
        self._heap[i] = item


    def insert(self, item):
        self._heap.append(item)
        self.change_item(self._heap_size, item)
        self._heap_size += 1


    # exercises 6.5-8
    def delete(self, i):
        key = self._heap[i]

        self._heap_size -= 1
        if self._heap_size > i:
            self._heap[i] = self._heap.pop()
            self._heapify(i)
        else:
            self._heap.pop()

        return key


if __name__ == "__main__":
    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    heap = Heap(A)
    heap.delete(3)
    heap.insert(10)
    for _ in range(len(A)):
        print(heap.extract_top(), end=" ")
    print()
