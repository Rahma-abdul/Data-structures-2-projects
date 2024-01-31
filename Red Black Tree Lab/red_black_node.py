import copy
import traceback


class RBNode:
    value = 0
    right = None
    left = None
    parent = None
    black = 0

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def get_grand_parent(self):
        if self.parent is None:
            pass
        if self.parent.parent is None:
            pass
        else:
            return self.parent.parent

    def get_uncle(self):
        if self.parent is None:
            return 0
        if self.parent.parent is None:
            return 0
        elif self.parent.value < self.parent.parent.value:
            return self.parent.parent.right
        else:
            return self.parent.parent.left

    def isRoot(self):
        if self.parent is None:
            return True
        else:
            return False
    def isBlack(self):
        if self.black == 0:
            return False
        else:
            return True

    def isDoubleBlack(self):
        if self.black == 2:
            return True
        else:
            return False

    def changeColor(self):
        if self.black == 0:
            self.black = 1
        elif self.black == 1:
            self.black = 0
        else:
            print("can't recolor double black node")

    def __str__(self):
        if self.isBlack():
            return f"{self.value} , Black"
        else:
            return f"{self.value} , Red"

    def isRight(self):
        if self.parent is None:
            return True
        if self.parent.right is not None:
            if self.parent.right.value == self.value:
                return True
        else:
            return False

    def isLeft(self):
        if self.parent is None:
            return True
        if self.parent.left is not None:
            if self.parent.left.value == self.value:
                return True
        else:
            return False

    def isInline(self):
        # if self.parent is None:
        #     return True
        if self.isRight() and self.parent.isRight():
            return True
        elif self.isLeft() and self.parent.isLeft():
            return True
        else:
            return False

    def isLeaf(self):
        if self.right is None and self.left is None:
            return True
        return False

    def getPredecessor(self):
        if self.left is not None:
            root = self.left
            while root.right is not None:
                root = root.right
            return root
        return None

    def rotate(self, tree):
        grandParent = self.get_grand_parent()
        y = copy.copy(self.parent)
        z = copy.copy(self.get_grand_parent())
        # sibling = self.get_sibling()

        # if z is None:
        #     y.changeColor()
        #     return 'z is None'

        if not self.isInline():
            if y.value < self.value:
                # y.left = self
                # y.right = None
                y.left_rotate(tree)
            else:
                y.right_rotate(tree)
                # y.right = self
                # y.left = None
            # temp = y.value
            # y.value = self.value
            # self.value = temp
            temp = y
            y = self
            self = temp
            if y.isRight():
                z.right = y
            else:
                z.left = y
        y.changeColor()
        z.changeColor()
        if z.parent is not None:                             # replace y with the grandparent z
            if z.isRight():
                self.get_grand_parent().parent.right = y
                # z.parent.right = self.parent
            else:
                self.get_grand_parent().parent.left = y
                # z.parent.left = y
            # self.parent.parent = z.parent

        if y.isRight():
            z.right = y.left
            y.left = z

            # if self.get_sibling() is not None:
            #     z.right = sibling

        elif y.parent is not None:
            z.left = y.right
            y.right = z
            # if self.get_sibling() is not None:
            #     z.left = sibling
        if z.parent is None:
            y.parent = None
            tree.root = y
        z.parent = y

        # if y.isRight():
        #     z.left_rotate(tree)
        # else:
        #     z.right_rotate(tree)
        # y = z.parent

        if self.get_grand_parent() is not None:
            y.parent = self.get_grand_parent().parent
        self.parent = y

    def get_sibling(self):
        if self.isRight():
            return self.parent.left
        else:
            return self.parent.right

    def double_red_check(self):     # check red property for node and its parent
        if self.black != 0:
            return False
        elif self.parent is not None and self.parent.black != 0:
            return False
        else:
            return True

    def left_rotate(self, tree):
        y = self.right
        self.right = y.left
        if y.left is not None:
            y.left.parent = self

        y.parent = self.parent
        if self.parent is None:
            tree.root = y
        elif self.isLeft():
            self.parent.left = y
        else:
            self.parent.right = y
        y.left = self
        self.parent = y
        # print('###############')
        # tree.print2D(self.parent)
        # print('###############')

    def right_rotate(self, tree):
        y = self.left
        self.left = y.right
        if y.right is not None:
            y.right.parent = self

        y.parent = self.parent
        if self.parent is None:
            tree.root = y
        elif self.isRight():
            self.parent.right = y
        else:
            self.parent.left = y
        y.right = self
        self.parent = y
        # print('###############')
        # tree.print2D(self.parent)
        # print('###############')
