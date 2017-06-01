#!/usr/bin/python


class Heap():
    def __init__(self, A):
        self._heap = A
        self._heap_size = len(A)
        self._build()


    def __len__(self):
        return self._heap_size


    def _heapify(self, i):
        raise NotImplementedError


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


    def change_key(self, i, key):
        raise NotImplementedError


    def insert(self, key):
        self._heap.append(key)
        self.change_key(self._heap_size, key)
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


class MinHeap(Heap):
    def __init__(self, A):
        Heap.__init__(self, A)
        self.decrease_key = self.change_key
        self.extract_min = self.extract_top


    # exercises 6.2-2
    def _heapify(self, i):
        l = i << 1
        l = l + 1
        r = l + 1
        smallest = i

        if l < self._heap_size and self._heap[l] < self._heap[i]:
            smallest = l
        if r < self._heap_size and self._heap[r] < self._heap[smallest]:
            smallest = r
        if smallest != i:
            self._heap[i], self._heap[smallest] = \
                self._heap[smallest], self._heap[i]
            self._heapify(smallest)


    def _heapify_iterative(self, i):
        while i < self._heap_size:
            l = i << 1
            l = l + 1
            r = l + 1
            smallest = i

            if l < self._heap_size and self._heap[l] < self._heap[i]:
                smallest = l
            if r < self._heap_size and self._heap[r] < self._heap[smallest]:
                smallest = r
            if smallest == i:
                break
            else:
                self._heap[i], self._heap[smallest] = \
                    self._heap[smallest], self._heap[i]
                i = smallest


    def change_key_origin(self, i, key):
        if i != self._heap_size:
            assert key <= self._heap[i], "new key is larger than current key"
        self._heap[i] = key
        parent = (i - 1) >> 1
        while i > 0 and self._heap[parent] > self._heap[i]:
            self._heap[parent], self._heap[i] = \
                self._heap[i], self._heap[parent]
            i = parent
            parent = (i - 1) >> 1


    def change_key(self, i, key):
        if i != self._heap_size:
            assert key <= self._heap[i], "new key is smaller than current key"
        parent = (i - 1) >> 1
        while i > 0 and self._heap[parent] > key:
            self._heap[i] = self._heap[parent]
            i = parent
            parent = (i - 1) >> 1
        self._heap[i] = key


# chapter 6.2
class MaxHeap(Heap):
    def __init__(self, A):
        Heap.__init__(self, A)
        self.increase_key = self.change_key
        self.extract_max = self.extract_top


    def _heapify(self, i):
        l = i << 1
        l = l + 1
        r = l + 1
        largest = i

        if l < self._heap_size and self._heap[l] > self._heap[i]:
            largest = l
        if r < self._heap_size and self._heap[r] > self._heap[largest]:
            largest = r
        if largest != i:
            self._heap[i], self._heap[largest] = \
                self._heap[largest], self._heap[i]
            self._heapify(largest)


    # exercises 6.2-5
    def _heapify_iterative(self, i):
        while i < self._heap_size:
            l = i << 1
            l = l + 1
            r = l + 1
            largest = i

            if l < self._heap_size and self._heap[l] > self._heap[i]:
                largest = l
            if r < self._heap_size and self._heap[r] > self._heap[largest]:
                largest = r
            if largest == i:
                break
            else:
                self._heap[i], self._heap[largest] = \
                    self._heap[largest], self._heap[i]
                i = largest


    def change_key_origin(self, i, key):
        if i != self._heap_size:
            assert key >= self._heap[i], "new key is smaller than current key"
        self._heap[i] = key
        parent = (i - 1) >> 1
        while i > 0 and self._heap[parent] < self._heap[i]:
            self._heap[parent], self._heap[i] = \
                self._heap[i], self._heap[parent]
            i = parent
            parent = (i - 1) >> 1


    # exercises 6.5-6
    def change_key(self, i, key):
        if i != self._heap_size:
            assert key >= self._heap[i], "new key is smaller than current key"
        parent = (i - 1) >> 1
        while i > 0 and self._heap[parent] < key:
            self._heap[i] = self._heap[parent]
            i = parent
            parent = (i - 1) >> 1
        self._heap[i] = key


# chapter 6.5
def PriorityQueue(A, Heap=MaxHeap):
    return Heap(A)


if __name__ == "__main__":
    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    queue = PriorityQueue(A)
    for _ in range(len(A)):
        print(queue.extract_top(), end=" ")
    print()
    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    queue = PriorityQueue(A, MinHeap)
    for _ in range(len(A)):
        print(queue.extract_top(), end=" ")
    print()

    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    queue = PriorityQueue(A)
    queue.insert(10)
    for _ in range(len(A)):
        print(queue.extract_top(), end=" ")
    print()
    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    queue = PriorityQueue(A, MinHeap)
    queue.insert(10)
    for _ in range(len(A)):
        print(queue.extract_top(), end=" ")
    print()

    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    heap = MaxHeap(A)
    heap.delete(3)
    for _ in range(len(A)):
        print(heap.extract_top(), end=" ")
    print()
    A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    heap = MinHeap(A)
    heap.delete(3)
    for _ in range(len(A)):
        print(heap.extract_top(), end=" ")
    print()
