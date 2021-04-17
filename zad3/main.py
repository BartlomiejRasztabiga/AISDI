import timeit

import numpy as np

from trees import BST, AVL

num_of_repetitions = 3  # num of repetitions to get avg time


def main():
    tree_creation_results = compare_tree_creation()

    print(tree_creation_results)


def compare_tree_creation():
    results = {}
    count = [(n + 1) * 1000 for n in range(10)]

    for n in count:
        content = np.random.randint(low=1, high=10000, size=n).tolist()

        bst_results = run_bst_tree_creation(content)
        avl_results = run_avl_tree_creation(content)

        results[n] = (bst_results, avl_results)

    return results


def run_bst_tree_creation(content):
    timer = timeit.Timer(lambda _content=content: BST(lst=_content))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def run_avl_tree_creation(content):
    timer = timeit.Timer(lambda _content=content: AVL(lst=_content))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


if __name__ == "__main__":
    main()
