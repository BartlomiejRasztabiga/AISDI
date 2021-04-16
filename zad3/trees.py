import os


class ItemNotFoundException(Exception):
    pass


class TreeNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None
        self.balance = 0
        self.duplicates = 0

    def __str__(self):
        return self.string_representation(0)

    def string_representation(self, depth=0):
        representation = ""

        if self.right:
            representation += self.right.string_representation(depth + 2)

        representation += " " * depth + str(self.item) + os.linesep

        if self.left:
            representation += self.left.string_representation(depth + 2)

        return representation

    def leftmost_down(self):
        node = self
        while node.left:
            node = node.left
        return node

    # def rightmost_down(self):
    #     node = self
    #     while node.right:
    #         node = node.right
    #     return node

    def count_nodes(self):
        """
        Returns number of all descendants + 1
        """
        return 1 \
               + (self.left.count_nodes() if self.left else 0) \
               + (self.right.count_nodes() if self.right else 0)

    def has_both_children(self):
        """
        Returns True if node has both left and right children
        """
        return self.left and self.right

    def has_left_child(self):
        """
        Returns True if node has left child
        """
        return self.left is not None

    def has_right_child(self):
        """
        Returns True if node has right child
        """
        return self.right is not None

    def has_no_parent(self):
        """
        Returns True if node has no parent
        """
        return self.parent is None


class BST:
    def __init__(self, lst=None, root=None):
        self.root = root

        if lst is not None:
            for node in lst:
                self.insert_node(node)

    def __str__(self):
        return os.linesep + self.root.string_representation(depth=2) + os.linesep

    def __contains__(self, item):
        return self.find_node(item) is not None

    def __len__(self):
        return 0 if self.root is None else self.root.count_nodes()

    def insert_node(self, item):
        """
        Inserts new item into a tree.
        If this item already exists, then its duplicates count is incremented.
        Returns the Node associated with this item.
        """

        # if no root, set new root
        if self.root is None:
            self.root = TreeNode(item)
            return self.root

        branch = self.root
        node = self.root

        # find node which should be the parent of newly inserted node
        while branch is not None:
            node = branch

            if item < node.item:
                branch = node.left
            elif item > node.item:
                branch = node.right
            else:
                # if item already exists, increment duplicates count
                node.duplicates += 1
                return node

        # link new node to its parent
        new_node = TreeNode(item)
        new_node.parent = node

        if item < node.item:
            node.left = new_node
        else:
            node.right = new_node

        return new_node

    def remove_node(self, item):
        """
        Removes an element from the tree.
        If this item had duplicates, then its duplicates count is decremented.
        Returns parent of the deleted node.
        """
        node = self.find_node(item)

        # item not in the tree, throw exception
        if node is None:
            raise ItemNotFoundException()

        # node has both children, find replacement node
        # with smallest value in right sub-tree.
        # copy value from replacement node to node selected for deletion
        # and remove replacement node
        if node.has_both_children():
            replacement_node = node.right.leftmost_down()

            if replacement_node.has_right_child():
                self.replace_node(replacement_node, replacement_node.right)
            elif replacement_node.parent.left == replacement_node:
                replacement_node.parent.left = None
            else:
                replacement_node.parent.right = None

            node.item = replacement_node.item
            return node.parent
        elif node.has_left_child():
            self.replace_node(node, node.left)
            return node.parent
        elif node.has_right_child():
            self.replace_node(node, node.right)
            return node.parent
        else:
            if node.has_no_parent():
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

            return node.parent

    def find_node(self, item):
        """
        Returns node with given key (item). Returns None if not found.
        """
        node = self.root

        while node is not None and node.item != item:
            if item < node.item:
                node = node.left
            else:
                node = node.right

        return node

    def replace_node(self, src, dest):
        """
        Moves node from src to dest.
        """

        dest.parent = src.parent

        if src.has_no_parent():
            self.root = dest
        elif src.parent.left == src:
            src.parent.left = dest
        elif src.parent.right == src:
            src.parent.right = dest


class AVL(BST):
    pass

