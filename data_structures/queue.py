#!/usr/bin/python


# chapter 10.1
class Queue():
    def __init__(self, n):
        self._queue = [None] * n
        self._head = 0
        self._tail = 0


    def enqueue(self, a):
        # exercises 10.1-4
        if (self._tail + 1) % len(self._queue) == self._head:
            raise LookupError

        self._queue[self._tail] = a
        if self._tail == len(self._queue):
            self._tail = 0
        else:
            self._tail += 1


    def dequeue(self):
        if self._tail == self._head:
            raise LookupError

        x = self._queue[self._head]
        if self._head == len(self._queue):
            self._head = 0
        else:
            self._head += 1
        return x


# exercises 10.1-5
class Deque():
    def __init__(self, n):
        self._deque = [None] * n
        self._head = 0
        self._tail = 0


    def push_front(self, a):
        if (self._tail + 1) % len(self._deque) == self._head:
            raise LookupError

        self._head = (self._head - 1) % len(self._deque)
        self._deque[self._head] = a


    def push_back(self, a):
        if (self._tail + 1) % len(self._deque) == self._head:
            raise LookupError

        self._deque[self._tail] = a
        self._tail = (self._tail + 1) % len(self._deque)


    def pop_front(self):
        if self._tail == self._head:
            raise LookupError

        x = self._deque[self._head]
        self._head = (self._head + 1) % len(self._deque)
        return x


    def pop_back(self):
        if self._tail == self._head:
            raise LookupError

        self._tail = (self._tail - 1) % len(self._deque)
        return self._deque[self._tail]


if __name__ == "__main__":
    # exercises 10.1-3
    queue = Queue(6)
    queue.enqueue(4)
    queue.enqueue(1)
    queue.enqueue(3)
    print(queue._queue, queue._head, queue._tail)
    queue.dequeue()
    print(queue._queue, queue._head, queue._tail)
    queue.enqueue(8)
    print(queue._queue, queue._head, queue._tail)
    queue.dequeue()
    print(queue._queue, queue._head, queue._tail)
