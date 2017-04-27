#!/usr/bin/python


RED = 1
BLACK = 0


class Node():
    def __init__(self, data, color=RED, parent=None):
        self.data = data
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None
