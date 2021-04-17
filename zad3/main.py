import timeit

import numpy as np

from trees import BST, AVL

num_of_repetitions = 3  # num of repetitions to get avg time


def main():
    #tree_creation_results = compare_tree_creation()

    #print(tree_creation_results)
    print(compare_node_removal())


def compare_tree_creation():
    results = {}
    count = [(n + 1) * 1000 for n in range(10)]
    for n in count:
        content = generate_input_data(n)

        bst_results = run_bst_tree_creation(content)
        avl_results = run_avl_tree_creation(content)

        results[n] = (bst_results, avl_results)

    return results


def compare_node_removal():
    results = {}
    count = [(n + 1) * 100 for n in range(50)]
    for n in count:
        # constant amount of input elements throughout all tests
        content = generate_input_data(10000)

        # bst_results = run_node_removal(BST, content, n)
        avl_results = run_node_removal(AVL, content, n)
        results[n] = avl_results

    return results


def run_node_removal(tree_class, content, count):
    time = 0

    for _ in range(num_of_repetitions):
        tree = tree_class(content)
        nodes_to_remove = content[:count]
        timer = timeit.Timer(lambda _tree=tree: _tree.remove_nodes(nodes_to_remove))
        time += timer.timeit(1)

    return time / num_of_repetitions


def run_bst_tree_creation(content):
    timer = timeit.Timer(lambda _content=content: BST(lst=_content))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def run_avl_tree_creation(content):
    timer = timeit.Timer(lambda _content=content: AVL(lst=_content))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def generate_input_data(size):
    return np.random.randint(low=1, high=10000, size=size).tolist()


if __name__ == "__main__":
    main()
