def _merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr  # already sorted

    mid_ix = len(arr) // 2

    left = merge_sort(arr[:mid_ix])
    right = merge_sort(arr[mid_ix:])
    return _merge(left, right)


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)
