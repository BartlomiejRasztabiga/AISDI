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
        return arr  # already sorted

    pivot = arr[0]
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + equal + quick_sort(greater)


def insertion_sort(arr):
    if len(arr) < 2:
        return arr  # already sorted

    for i in range(1, len(arr)):
        key = arr[i]
        pos = i - 1
        while pos >= 0 and key < arr[pos]:
            arr[pos + 1] = arr[pos]
            pos -= 1
        arr[pos + 1] = key
    return arr


def bubble_sort(arr):
    if len(arr) < 2:
        return arr  # already sorted

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
