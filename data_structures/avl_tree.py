#!/usr/bin/python
# problem 13-3
# material: https://www.youtube.com/watch?v=FNeL18KsWPc
# !! under construction

class Node():
    def __init__(self, data, hight=0, parent=None):
        self.data = data
        self.hight = hight  # length of highest path from it down to a leaf
        self.parent = parent
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self):
        self.root = None


    def _left_rotate(x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        else x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def _right_rotate(y):
        x = y.left
        y.left = x.right
        if x.right != None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = y
        x.right = y
        y.parent = x


    def _balance(x):
        while x is not None:
            x_left_height = 0
            x_right_height = 0
            if x.left is not None:
                x_left_height = x.left.height
            if x.right is not None:
                x_right_height = x.right.height

            if x_left_height - x_right_height > 1:
                y = x.left
                y_left_height = 0
                y_right_height = 0
                if y.left is not None:
                    y_left_height = y.left.height
                if y.right is not None:
                    y_right_height = y.right.height

                if y_left_height > y_right_height:
                    self._right_rotate(x)
                else:
                    self._left_rotate(y)
                    self._right_rotate(x)
            elif x_right_height - x_left_height > 1:
                y = x.right
                y_left_height = 0
                y_right_height = 0
                if y.left is not None:
                    y_left_height = y.left.height
                if y.right is not None:
                    y_right_height = y.right.height

                if y_left_height < y_right_height:
                    self._left_rotate(x)
                else:
                    self._right_rotate(y)
                    self._left_rotate(x)
            else:
                pass

            x = x.parent


    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if x.data < z.data:
                x = x.right
            else:
                x = x.left
        z.parent = y
        if y is None:
            self.root = z
        elif y.data < z.data:
            y.right = z
        else:
            y.left = z

        self._balance(y);
