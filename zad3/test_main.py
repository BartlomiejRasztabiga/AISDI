import pytest

from trees import BST, AVL, ItemNotFoundException


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


class TestAVL:
    def test_insert_rotate_left_simple(self):
        tree = AVL([10])
        tree.insert_node(11)
        tree.insert_node(12)

        assert tree.root.item == 11
        assert tree.root.left.item == 10
        assert tree.root.right.item == 12

    def test_insert_rotate_right_simple(self):
        tree = AVL([12])
        tree.insert_node(11)
        tree.insert_node(10)

        assert tree.root.item == 11
        assert tree.root.left.item == 10
        assert tree.root.right.item == 12

    def test_insert_right_heavy(self):
        tree = AVL([1])
        tree.insert_node(2)
        tree.insert_node(3)
        tree.insert_node(4)
        tree.insert_node(5)
        tree.insert_node(6)
        tree.insert_node(7)

        assert tree.root.item == 4
        assert tree.root.left.item == 2
        assert tree.root.left.left.item == 1
        assert tree.root.left.right.item == 3
        assert tree.root.right.item == 6
        assert tree.root.right.left.item == 5
        assert tree.root.right.right.item == 7

    def test_insert_left_heavy(self):
        tree = AVL([7])
        tree.insert_node(6)
        tree.insert_node(5)
        tree.insert_node(4)
        tree.insert_node(3)
        tree.insert_node(2)
        tree.insert_node(1)

        assert tree.root.item == 4
        assert tree.root.left.item == 2
        assert tree.root.left.left.item == 1
        assert tree.root.left.right.item == 3
        assert tree.root.right.item == 6
        assert tree.root.right.left.item == 5
        assert tree.root.right.right.item == 7

    def test_insert_right_left_rotation(self):
        tree = AVL([3])
        tree.insert_node(5)
        tree.insert_node(4)

        assert tree.root.item == 4
        assert tree.root.left.item == 3
        assert tree.root.right.item == 5

    def test_insert_left_right_rotation(self):
        tree = AVL([5])
        tree.insert_node(3)
        tree.insert_node(4)

        assert tree.root.item == 4
        assert tree.root.left.item == 3
        assert tree.root.right.item == 5

    def test_delete_rotate_left(self):
        tree = AVL([1, 2, 3, 4])
        tree.remove_node(2)

        assert tree.root.item == 3
        assert tree.root.left.item == 1
        assert tree.root.right.item == 4

    def test_delete_rotate_right(self):
        tree = AVL([50, 40, 60, 30, 45, 55, 10])
        tree.remove_node(55)

        assert tree.root.item == 40
        assert tree.root.left.item == 30
        assert tree.root.left.left.item == 10
        assert tree.root.right.item == 50
        assert tree.root.right.left.item == 45
        assert tree.root.right.right.item == 60

    def test_delete_rotate_right2(self):
        tree = AVL([50, 40, 60, 45])
        tree.remove_node(60)

        assert tree.root.item == 45
        assert tree.root.left.item == 40
        assert tree.root.right.item == 50

    def test_delete_complex(self):
        tree = AVL([16, 5, 19, 2, 13, 18, 25, 4, 6, 15, 22, 10])
        tree.remove_node(18)

        assert tree.root.item == 13
        assert tree.root.left.item == 5
        assert tree.root.left.left.item == 2
        assert tree.root.left.left.right.item == 4
        assert tree.root.left.right.item == 6
        assert tree.root.left.right.right.item == 10
        assert tree.root.right.item == 16
        assert tree.root.right.left.item == 15
        assert tree.root.right.right.item == 22
        assert tree.root.right.right.left.item == 19
        assert tree.root.right.right.right.item == 25

    def test_delete_complex2(self):
        tree = AVL([0, 2, 4, 6, 8, 10, 12, 9])
        tree.remove_node(10)

        assert tree.root.item == 6
        assert tree.root.left.item == 2
        assert tree.root.left.left.item == 0
        assert tree.root.left.right.item == 4
        assert tree.root.right.item == 9
        assert tree.root.right.left.item == 8
        assert tree.root.right.right.item == 12
