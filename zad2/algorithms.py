from utils import merge


def merge_sort(arr):
    if len(arr) < 2:
        return arr  # already sorted

    mid_ix = len(arr) // 2

    left = merge_sort(arr[:mid_ix])
    right = merge_sort(arr[mid_ix:])
    return merge(left, right)


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)
