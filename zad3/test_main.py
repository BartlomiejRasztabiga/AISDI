import pytest

from trees import BST, ItemNotFoundException


def test_insert_simple():
    tree = BST([10])
    tree.insert_node(0)
    tree.insert_node(20)

    assert len(tree) == 3
    assert tree.root.item == 10
    assert tree.root.left.item == 0
    assert tree.root.left.parent == tree.root
    assert tree.root.right.item == 20
    assert tree.root.right.parent == tree.root


def test_insert_with_duplicates():
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


def test_delete_left():
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


def test_delete_no_children():
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


def test_delete_single_node():
    tree = BST([10])

    tree.remove_node(10)

    assert len(tree) == 0
    assert tree.find_node(-10) is None


def test_delete_left_with_duplicates():
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


def test_delete_root():
    tree = BST([10])
    tree.insert_node(0)
    tree.insert_node(20)
    tree.insert_node(-5)
    tree.insert_node(15)
    tree.insert_node(1)
    tree.insert_node(-10)

    tree.remove_node(10)

    assert len(tree) == 6
    assert tree.root.item == 15


def test_delete_non_existing():
    tree = BST([10])
    tree.insert_node(0)
    tree.insert_node(20)
    tree.insert_node(-5)
    tree.insert_node(15)
    tree.insert_node(1)
    tree.insert_node(-10)

    with pytest.raises(ItemNotFoundException):
        tree.remove_node(100)


def test_print_tree():
    tree = BST([10])
    tree.insert_node(0)
    tree.insert_node(20)

    assert tree.__str__() == "\n    20\n  10\n    0\n\n"


def test_print_node():
    tree = BST([10])
    tree.insert_node(0)
    tree.insert_node(20)

    assert tree.root.__str__() == "  20\n10\n  0\n"


def test_contains_method():
    tree = BST([10])
    tree.insert_node(0)
    tree.insert_node(20)

    assert 0 in tree
