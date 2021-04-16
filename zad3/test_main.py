import pytest

from trees import BST, ItemNotFoundException


class TestBST:
    def test_insert_simple(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)

        assert len(tree) == 3
        assert tree.root.item == 10
        assert tree.root.left.item == 0
        assert tree.root.left.parent == tree.root
        assert tree.root.right.item == 20
        assert tree.root.right.parent == tree.root

    def test_insert_with_duplicates(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)
        tree.insert_node(20)

        assert len(tree) == 3
        assert tree.root.item == 10
        assert tree.root.left.item == 0
        assert tree.root.left.parent == tree.root
        assert tree.root.right.item == 20
        assert tree.root.right.duplicates == 1
        assert tree.root.right.parent == tree.root

    def test_delete_left(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)
        tree.insert_node(-5)
        tree.insert_node(15)
        tree.insert_node(1)
        tree.insert_node(-10)

        tree.remove_node(-5)

        assert len(tree) == 6
        assert tree.root.left.left.item == -10
        assert tree.find_node(-5) is None

    def test_delete_left_no_children(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)
        tree.insert_node(-5)
        tree.insert_node(15)
        tree.insert_node(1)
        tree.insert_node(-10)

        tree.remove_node(-10)

        assert len(tree) == 6
        assert tree.root.left.left.item == -5
        assert tree.find_node(-10) is None

    def test_delete_right_no_children(self):
        tree = BST([3])
        tree.insert_node(1)
        tree.insert_node(5)
        tree.insert_node(4)
        tree.insert_node(8)

        tree.remove_node(8)

        assert len(tree) == 4
        assert tree.root.right.right is None
        assert tree.find_node(8) is None

    def test_delete_single_node(self):
        tree = BST([10])

        tree.remove_node(10)

        assert len(tree) == 0
        assert tree.find_node(-10) is None

    def test_delete_left_with_duplicates(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)
        tree.insert_node(-5)
        tree.insert_node(15)
        tree.insert_node(1)
        tree.insert_node(-5)
        tree.insert_node(-10)

        tree.remove_node(-5)

        assert len(tree) == 6
        assert tree.root.left.left.item == -10
        assert tree.find_node(-5) is None

    def test_delete1(self):
        tree = BST([2])
        tree.insert_node(1)
        tree.insert_node(5)
        tree.insert_node(3)
        tree.insert_node(8)
        tree.insert_node(4)

        tree.remove_node(2)

        assert len(tree) == 5
        assert tree.root.item == 3

    def test_delete2(self):
        tree = BST([2])
        tree.insert_node(1)
        tree.insert_node(5)
        tree.insert_node(3)
        tree.insert_node(8)

        tree.remove_node(2)

        assert len(tree) == 4
        assert tree.root.item == 3

    def test_delete3(self):
        tree = BST([2])
        tree.insert_node(1)
        tree.insert_node(5)

        tree.remove_node(2)

        assert len(tree) == 2
        assert tree.root.item == 5

    def test_delete4(self):
        tree = BST([2])
        tree.insert_node(1)
        tree.insert_node(5)

        tree.remove_node(2)

        assert len(tree) == 2
        assert tree.root.item == 5

    def test_delete5(self):
        tree = BST([2])
        tree.insert_node(5)

        tree.remove_node(2)

        assert len(tree) == 1
        assert tree.root.item == 5

    def test_delete_non_existing(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)
        tree.insert_node(-5)
        tree.insert_node(15)
        tree.insert_node(1)
        tree.insert_node(-10)

        with pytest.raises(ItemNotFoundException):
            tree.remove_node(100)

    def test_print_tree(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)

        assert tree.__str__() == "\n    20\n  10\n    0\n\n"

    def test_print_node(self):
        tree = BST([10])
        tree.insert_node(0)
        tree.insert_node(20)

        assert tree.root.__str__() == "  20\n10\n  0\n"
