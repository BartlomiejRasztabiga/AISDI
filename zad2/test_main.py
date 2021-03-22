from algorithms import merge_sort, quick_sort


def test_merge_sort_numbers():
    assert merge_sort([3, 5, 1]) == [1, 3, 5]


def test_merge_sort_strings():
    assert merge_sort(["gfd", "aba", "dsa"]) == ["aba", "dsa", "gfd"]


def test_quick_sort_numbers():
    assert quick_sort([3, 5, 1]) == [1, 3, 5]


def test_quick_sort_strings():
    assert quick_sort(["gfd", "aba", "dsa"]) == ["aba", "dsa", "gfd"]
