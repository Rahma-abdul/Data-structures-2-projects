from red_black_node import RBNode


class RBTree:
    root = None

    def __init__(self, root):
        self.root = root
        if root is None:
            self.size = 0
        else:
            self.size = 1

    def __search_inner(self, value, relative_root):
        # search the node with the value in parameter then returns the node parent and a flag=1 if found and 0 otherwise
        if relative_root is None:       # what the heck is that
            print("__________ search inner error __________")
            print("rel_root in the function is None")

        elif relative_root.value == value:
            return [relative_root, 1]
        elif relative_root.value > value:
            if relative_root.left is None:
                return [relative_root, 0]
            else:
                return self.__search_inner(value, relative_root.left)

        else:
            if relative_root.right is None:
                return [relative_root, 0]
            else:
                return self.__search_inner(value, relative_root.right)

    def search(self, value):
        return self.__search_inner(value, self.root)

    def __categories_by_level(self, node, depth, arr):
        if node is not None:
            arr[depth].append(node)
        if node.left is not None:
            self.__categories_by_level(node.left, depth+1, arr)
        if node.right is not None:
            self.__categories_by_level(node.right, depth+1, arr)

    def categories_by_level(self):
        # this function put every node with its siblings
        # return matrix first index is level second index is the node
        nodes_by_level = []
        for i in range(0, self.get_depth_naiveBST()):
            nodes_by_level.append([])

        self.__categories_by_level(self.root, 0, nodes_by_level)
        return nodes_by_level

    def print2DUtil(self, root, space):
        COUNT = [10]
        # Base case
        if root is None:
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        self.print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root)

        # Process left child
        self.print2DUtil(root.left, space)

    # Wrapper over print2DUtil()

    def print2D(self, root):

        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(root, 0)



    def traverse2(self):        # not completed
        # a traverse function closer to the visualized form of a tree
        # problem: spacing the child ,so it is in the correct place under their parents
        arr = self.categories_by_level()
        i = 0

        while i < len(arr):
            j = 0
            for x in range(0, len(arr)-i):
                print('\t', end='')
            while j < len(arr[i]):
                print(str(arr[i][j])+'\t', end='')
                j += 1
            print()
            i += 1
    def __traverse_inner(self, relative_root, depth):
        if relative_root is not None:
            for i in range(depth, 0, -1):
                print('\t', end='')
            print(relative_root)

        if relative_root.right is not None:
            self.__traverse_inner(relative_root.right, depth+1)
        if relative_root.left is not None:
            self.__traverse_inner(relative_root.left, depth+1)
        pass

    def traverse(self):
        print("Traversing tree:")

        self.__traverse_inner(self.root, 0)
        pass

    def get_depth_naiveBST(self):
        # print("\n\n")
        result = self.__get_depth_naiveBST(self.root, 1, 0)
        return result

    def __get_depth_naiveBST(self, rel_root, l, max_depth):
        if rel_root is None:
            return max_depth
        if rel_root.left is not None:
            # print(str(l+1)+'\t'+str(max_depth))
            if l+1 > max_depth:
                max_depth = self.__get_depth_naiveBST(rel_root.left, l + 1, l + 1)
            else:
                max_depth = self.__get_depth_naiveBST(rel_root.left, l + 1, max_depth)
        if rel_root.right is not None:
            # print(str(l + 1) + '\t' + str(max_depth))
            if l + 1 > max_depth:
                max_depth = self.__get_depth_naiveBST(rel_root.right, l + 1, l + 1)
            else:
                max_depth = self.__get_depth_naiveBST(rel_root.right, l + 1, max_depth)

        return max_depth

    def get_depth_RB(self):
        if self.root is None:
            return 0
        elif self.root.left is not None:
            return self.__get_depth_RB(self.root.left)

    def __get_depth_RB(self, rel_root):
        # if rel_root is None:
        #     return max_depth
        #
        # l += rel_root.black
        # if l > max_depth:
        #     max_depth = l
        # if rel_root.left is not None:
        #     # print(str(l) + '\t' + str(max_depth))
        #     max_depth = self.__get_depth_RB(rel_root.left, l, max_depth)
        # if rel_root.right is not None:
        #     # print(str(l) + '\t' + str(max_depth))
        #     max_depth = self.__get_depth_RB(rel_root.right, l, max_depth)
        #
        # return max_depth
        if rel_root.left is not None:
            return rel_root.black + self.__get_depth_RB(rel_root.left)
        else:
            return 0

    def insert_bst(self, node):
        self.size += 1
        if self.root is None:
            self.root = node
            if not node.isBlack():
                node.changeColor()
            return None
        self.__insert_bst(node, self.root)
        return None

    def __insert_bst(self, node, root):
        if root.value > node.value:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self.__insert_bst(node, root.left)
        elif root.value < node.value:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self.__insert_bst(node, root.right)

    def insert_rb_naive(self, value):

        search = self.search(value)
        if search[1] == 1:
            print("node already exists")
            return 0
        parent = search[0]
        node = RBNode(value, parent)

        if parent.value > value:
            parent.left = node
        else:
            parent.right = node

    def __traversal_properties(self, root, l, depth, flags):    # testing
        # leaf property is not checked because i have implemented the red black tree such that no leaf node exists
        # ( last parent = leaf node of standard RBTree
        # ____________ leaf property _____________
        # if root.right is None and root.left is None:
        #     if not root.isBlack:
        #         flags[0] = True

        # red property
        if not root.isBlack():
            if (root.parent is not None) and (not root.parent.isBlack()):
                flags[1] = True

        # depth property
        if root.isLeaf():
            if l != depth:
                flags[2] = True

        # common recursive block
        if root.left is not None:
            if root.left.isBlack():
                # print(l+1)
                self.__traversal_properties(root.left, l+1, depth, flags)
            else:
                # print(l)
                self.__traversal_properties(root.left, l, depth, flags)

        if root.right is not None:
            if root.right.isBlack():
                # print(l+1)
                self.__traversal_properties(root.right, l+1, depth, flags)
            else:
                # print(l)
                self.__traversal_properties(root.right, l, depth, flags)


    def check_traversal_properties(self):
        flags = [False, False, False]
        depth = self.get_depth_RB()
        if self.root is not None:
            self.__traversal_properties(self.root, self.root.black, depth, flags)
        return flags

    def check_red_black_tree(self):
        flags = [False, False, False, False]
        # [root property, leaf property, red property, depth property]
        # true means rule violated false means rule not violated
        if not self.root.isBlack():
            flags[0] = True

        flags = [flags[0]] + self.check_traversal_properties()[0:3]

        condition = False

        for i in range(0, 4):
            condition = condition or flags[i]

        if not condition:
            print("This is a correct red black tree")
            return True
        if flags[0]:
            print("Root property violated")
        if flags[1]:
            print("leaf property violated")
        if flags[2]:
            print("red property violated")
        if flags[3]:
            print("depth property violated")
        return False

    def get_total_size(self):
        return self.__get_total_size(self.root)

    def __get_total_size(self, rel_root):
        count = 0
        if rel_root is not None:
            count += 1
            if rel_root.left is not None:
                count += self.__get_total_size(rel_root.left)
            if rel_root.right is not None:
                count += self.__get_total_size(rel_root.right)
        return count

    def __red_property_violated(self, node):
        if not node.isBlack():
            if (node.parent is not None) and (not node.parent.isBlack()):
                return True

        a = False
        b = False
        if node.left is not None:
            a = self.__red_property_violated(node.left)
        if node.right is not None:
            b = self.__red_property_violated(node.right)
        return a or b

    def red_property_violated(self):
        return self.__red_property_violated(self.root)

    def root_property_violated(self):
        if self.root.black == 0:
            return True
        else:
            return False

    def rebalance(self, new_node):
        # if new_node.parent is None:
        #     return 'case ff'
        # if new_node.get_grand_parent() is None:
        #     new_node.parent.black = 1
        #     return 'case z'
        if new_node.get_uncle() is not None and new_node.get_uncle().black == 0:   # uncle is red
            new_node.parent.black = 1
            new_node.get_uncle().black = 1
            if self.root != new_node.get_grand_parent():
                new_node.get_grand_parent().black = 0
                if new_node.get_grand_parent().double_red_check():
                    self.rebalance(new_node.get_grand_parent())

        else:                                   # uncle is black
            new_node.rotate(self)

    def insert_RB_way(self, value):
        new_node = RBNode(value, None)
        self.insert_bst(new_node)
        if self.root is None:
            new_node.black = 1
            self.root = new_node

        elif new_node.double_red_check():
            self.rebalance(new_node)

    def __print_inorder(self, root):
        if root.left is not None:
            self.__print_inorder(root.left)

        print(root)
        if root.right is not None:
            self.__print_inorder(root.right)

    def print_inorder(self):
        self.__print_inorder(self.root)
