#!/usr/bin/python
# Θ(nlgn)
import sys
sys.path.append("../data_structures/")
from heap import MaxHeap, MinHeap


# chapter 6.4
def heap_sort(A, Heap=MaxHeap):
    heap = Heap(A)
    for i in reversed(range(1, heap._heap_size)):
        heap._heap[0], heap._heap[i] = heap._heap[i], heap._heap[0]
        heap._heap_size -= 1
        heap._heapify(0)
    return heap._heap


if __name__ == "__main__":
    A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print(heap_sort(A))
    print(heap_sort(A, MinHeap))
