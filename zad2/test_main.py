from algorithms import merge_sort, quick_sort, bubble_sort, insertion_sort


def test_merge_sort_numbers():
    assert merge_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
                      ) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]


def test_merge_sort_strings():
    assert merge_sort(["C59OK", "5QV09", "TCNId", "ne58v", "ges28", "EzMbM", "qdPku", "ltinw", "Nt1Rj", "nSb8R"]
                      ) == ["5QV09", "C59OK", "EzMbM", "Nt1Rj", "TCNId", "ges28", "ltinw", "nSb8R", "ne58v", "qdPku"]


def test_quick_sort_numbers():
    assert quick_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
                      ) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]


def test_quick_sort_strings():
    assert quick_sort(["C59OK", "5QV09", "TCNId", "ne58v", "ges28", "EzMbM", "qdPku", "ltinw", "Nt1Rj", "nSb8R"]
                      ) == ["5QV09", "C59OK", "EzMbM", "Nt1Rj", "TCNId", "ges28", "ltinw", "nSb8R", "ne58v", "qdPku"]


def test_bubble_sort_numbers():
    assert bubble_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
                      ) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]


def test_bubble_sort_strings():
    assert bubble_sort(["C59OK", "5QV09", "TCNId", "ne58v", "ges28", "EzMbM", "qdPku", "ltinw", "Nt1Rj", "nSb8R"]
                      ) == ["5QV09", "C59OK", "EzMbM", "Nt1Rj", "TCNId", "ges28", "ltinw", "nSb8R", "ne58v", "qdPku"]


def test_insertion_sort_numbers():
    assert insertion_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
                      ) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]


def test_insertion_sort_strings():
    assert insertion_sort(["C59OK", "5QV09", "TCNId", "ne58v", "ges28", "EzMbM", "qdPku", "ltinw", "Nt1Rj", "nSb8R"]
                      ) == ["5QV09", "C59OK", "EzMbM", "Nt1Rj", "TCNId", "ges28", "ltinw", "nSb8R", "ne58v", "qdPku"]
