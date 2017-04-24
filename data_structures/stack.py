#!/usr/bin/python


# chapter 10.1
class Stack():
    def __init__(self, n):
        self._stack = [None] * n
        self._top = 0


    def stack_empty(self):
        return self._stack == 0


    def push(self, a):
        self._stack[self._top] = a
        self._top += 1


    def pop(self):
        if self.stack_empty():
            raise LookupError
        else:
            self._top -= 1
            return self._stack[self._top]


if __name__ == "__main__":
    # exercises 10.1-1
    stack = Stack(6)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    print(stack._stack, stack._top)
    stack.pop()
    print(stack._stack, stack._top)
    stack.push(8)
    print(stack._stack, stack._top)
    stack.pop()
    print(stack._stack, stack._top)
