import os

outputdebug = True


class ItemNotFoundException(Exception):
    pass


def debug(msg):
    if outputdebug:
        print(msg)


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

    def rightmost_down(self):
        node = self
        while node.right:
            node = node.right
        return node

    def count_nodes(self):
        """
        Returns number of all descendants + 1
        """
        return 1 \
               + (self.left.count_nodes() if self.left else 0) \
               + (self.right.count_nodes() if self.right else 0)


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
        Inserts an item into a tree.
        If this item already existed, its duplicates count is incremented.
        Returns the Node associated with this item.
        """
        if self.root is None:
            self.root = TreeNode(item)
            return self.root

        branch = self.root
        node = self.root

        while branch is not None:
            node = branch

            if item < node.item:
                branch = node.left
            elif item > node.item:
                branch = node.right
            else:
                node.duplicates += 1
                return node

        new_node = TreeNode(item)
        new_node.parent = node

        if item < node.item:
            node.left = new_node
        else:
            node.right = new_node

        return new_node

    def remove_node(self, item):
        """
        Remove an element from a tree.
        If this item had duplicates, its duplicates count is decremented.
        Return parent of an un-linked node.
        """
        node = self.find_node(item)

        if node is None:
            raise ItemNotFoundException()

        # TODO: add comments about what's going on here
        # TODO: add utility methods
        if node.left and node.right:
            replacement = node.right.leftmost_down()
            lowest = replacement.parent

            if replacement.right:
                lowest = replacement.right
                self.replace_node(replacement, replacement.right)
            elif replacement.parent.left == replacement:
                replacement.parent.left = None
            else:
                replacement.parent.right = None

            node.item = replacement.item
            return lowest
        elif node.left:
            self.replace_node(node, node.left)
            return node.parent
        elif node.right:
            self.replace_node(node, node.right)
            return node.parent
        else:
            if node.parent is None:
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

            return node.parent

    def find_node(self, item):
        node = self.root

        while node is not None and node.item != item:
            if item < node.item:
                node = node.left
            elif item != node.item:
                node = node.right

        return node

    def replace_node(self, src, dest):
        """
        Moves src sub-tree to dest.
        """

        dest.parent = src.parent

        if src.parent is None:
            self.root = dest
        elif src.parent.left == src:
            src.parent.left = dest
        elif src.parent.right == src:
            src.parent.right = dest


class AVL(BST):
    pass


# Usage example
if __name__ == "__main__":
    pass
