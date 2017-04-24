#!/usr/bin/python


class Node():
    def __init__(self, e):
        self.data = e
        self.prev = self
        self.next = self


    def __eq__(self, b):
        return self.data == b


# chapter 10.2
# circular, doubly linked list with a sentinel
class List():
    def __init__(self):
        self._head = Node(None)


    def search(self, k):
        x = self._head.next
        while x != self._head and x != k:
            x = x.next
        return x


    # exercises 10.2-4
    def search_modified(self, k):
        self._head.data = k
        x = self._head.next
        while x != k:
            x = x.next
        if x == self._head:
            return None
        else:
            return x


    def insert(self, x):
        x.next = self._head.next
        self._head.next.prev = x
        self._head.next = x
        x.prev = self._head


    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev


if __name__ == "__main__":
    link = List()
    link.insert(Node(1))
    link.insert(Node(4))
    link.insert(Node(16))
    link.insert(Node(9))
    link.insert(Node(25))

    link._head.data = "G"
    x = link._head.next
    while x != "G":
        print(x.data, end=' ')
        x = x.next
    print()

    x = link.search(1)
    link.delete(x)

    link._head.data = "G"
    x = link._head.next
    while x != "G":
        print(x.data, end=' ')
        x = x.next
    print()
