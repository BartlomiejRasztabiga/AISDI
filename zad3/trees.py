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

    def left_subtree_height(self) -> int:
        return self.left.height() if self.left else 0

    def right_subtree_height(self) -> int:
        return self.right.height() if self.right else 0

    def height(self) -> int:
        return 1 + max(self.left_subtree_height(), self.right_subtree_height())

    def calculate_balance(self) -> int:
        left_height = self.left_subtree_height()
        right_height = self.right_subtree_height()
        self.balance = right_height - left_height
        return self.balance

    def has_duplicates(self):
        """
        Returns True if node has duplicates
        """
        return self.duplicates > 0


class BST:
    def __init__(self, lst=None, root=None):
        self.root = root

        if lst is not None:
            for node in lst:
                self.insert_node(node)

    def __str__(self):
        return os.linesep + self.root.string_representation(depth=2) + os.linesep

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
        Returns parent of the deleted node or None if item had duplicates.
        """
        node = self.find_node(item)

        # item not in the tree, throw exception
        if node is None:
            raise ItemNotFoundException()

        # if node had duplicates, decrement count and return
        if node.has_duplicates():
            node.duplicates -= 1
            return None

        # node has both children, find replacement node
        # with smallest value in right sub-tree.
        # copy value from replacement node to node selected for deletion
        # and remove replacement node
        if node.has_both_children():
            replacement_node = node.right.leftmost_down()
            replacement_node_parent = replacement_node.parent

            # unlink replacement_node
            if replacement_node.has_right_child():
                replacement_node_parent = replacement_node.right
                self.replace_node(replacement_node, replacement_node.right)
            elif replacement_node.parent.left == replacement_node:
                replacement_node.parent.left = None
            else:
                replacement_node.parent.right = None

            # swap values of node and replacement node
            node.item = replacement_node.item
            node.duplicates = replacement_node.duplicates
            return replacement_node_parent
        # node has only left child
        # move sub-tree to node selected for deletion
        elif node.has_left_child():
            self.replace_node(node, node.left)
            return node.parent
        elif node.has_right_child():
            self.replace_node(node, node.right)
            return node.parent
        # node has no children
        # unlink it from the parent
        else:
            if node.has_no_parent():
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

            return node.parent

    def remove_nodes(self, items):
        for item in items:
            self.remove_node(item)

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
        Moves node's sub-tree from src to dest.
        """

        if dest:
            dest.parent = src.parent

        if src.has_no_parent():
            self.root = dest
        elif src.parent.left == src:
            src.parent.left = dest
        elif src.parent.right == src:
            src.parent.right = dest


class AVL(BST):
    def insert_node(self, item):
        new_node = super().insert_node(item)

        # if new node is unique, rebalance
        if not new_node.has_duplicates():
            self._rebalance_on_insert(new_node)

        return new_node

    def remove_node(self, item):
        removed_node_parent = super().remove_node(item)

        if removed_node_parent:
            previous_balance = removed_node_parent.balance

            removed_node_parent.calculate_balance()
            if previous_balance != 0 or removed_node_parent.balance not in {-1, 1}:
                self._rebalance_on_remove(removed_node_parent)

        return removed_node_parent

    def _rebalance_on_insert(self, node):
        if abs(node.balance) > 1:
            self._rebalance(node)
            return

        if node.parent:
            if node.parent.left == node:
                node.parent.balance -= 1
            else:
                node.parent.balance += 1

            if node.parent.balance != 0:
                self._rebalance_on_insert(node.parent)

    def _rebalance_on_remove(self, node):
        if abs(node.balance) > 1:
            new_root = self._root_after_rebalance(node)
            new_root_prev_balance = new_root.balance

            self._rebalance(node)
            if new_root_prev_balance == 0 and new_root.balance in {-1, 1}:
                return

            node = node.parent

        if node.parent:
            if node.parent.left == node:
                node.parent.balance += 1
            else:
                node.parent.balance -= 1

            if node.parent.balance != 0 or node.parent.balance not in {-1, 1}:
                self._rebalance_on_remove(node.parent)

    def _rebalance(self, node):
        if node.balance > 0:
            if node.right.balance < 0:
                self._rotate_right(node.right)
            self._rotate_left(node)
        elif node.balance < 0:
            if node.left.balance > 0:
                self._rotate_left(node.left)
            self._rotate_right(node)

    def _root_after_rebalance(self, node):
        """Returns the new root, which will replace `node` after `_rebalance(node)`"""
        if node.balance > 0:
            assert node.right
            if node.right.balance < 0:
                # R-L Rotation
                assert node.right.left
                return node.right.left
            else:
                # L Rotation
                return node.right

        else:
            assert node.left
            if node.left.balance > 0:
                # L-R Rotation
                assert node.left.right
                return node.left.right
            else:
                # R Rotation
                return node.left

    def _rotate_left(self, node):
        pivot = node.right

        self.replace_node(node.right, pivot.left)
        self.replace_node(node, pivot)

        pivot.left = node
        node.parent = pivot

        node.balance = node.balance - 1 - max(0, pivot.balance)
        pivot.balance = pivot.balance - 1 + min(0, node.balance)

    def _rotate_right(self, node):
        pivot = node.left

        self.replace_node(node.left, pivot.right)
        self.replace_node(node, pivot)

        pivot.right = node
        node.parent = pivot

        node.balance = node.balance + 1 - min(0, pivot.balance)
        pivot.balance = pivot.balance + 1 + max(0, node.balance)
