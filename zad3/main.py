import timeit

import codecs
import numpy as np
import os
import matplotlib.pyplot as plt

from trees import BST, AVL

num_of_repetitions = 10  # num of repetitions to get avg time
results_folder = "results"


def main():
    results_str = "Wyniki pomiarów:\n\n"

    results_str += "Tworzenie drzew z n elementów:\n"
    tree_creation_results = compare_tree_creation()
    tree_str = format_results(tree_creation_results)
    results_str += tree_str + "\n\n"

    plot_tree_creation(tree_creation_results)

    results_str += "Usuwanie n elementów z drzewa o 10000 elementach:\n"
    node_removal_results = compare_node_removal()
    node_str = format_results(node_removal_results)
    results_str += node_str + "\n\n"

    plot_node_removal(node_removal_results)

    results_str += "Wyszukiwanie n elementów w drzewie o 10000 elementach:\n"
    node_finding_results = compare_node_finding()
    node_str = format_results(node_finding_results)
    results_str += node_str

    plot_node_finding(node_finding_results)

    print(results_str)
    with codecs.open(os.sep.join([results_folder, "results.txt"]), "w", "utf-8") as file:
        file.write(results_str)


def format_results(results):
    return "\n".join([
        f"{count}:\tBST: {round(result[0], 7)}s\t\tAVL: {round(result[1], 8)}s"
        for count, result in results.items()
    ])


def plot_tree_creation(results):
    plt.clf()
    plt.plot(results.keys(), results.values(), label=('BST', 'AVL'))

    plt.xlabel('amount of elements in the input data')
    plt.ylabel('time (s)')
    plt.title('Time needed to create a tree from n elements')
    plt.xticks(list(results.keys()))
    plt.legend()
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_tree_creation.png"]))


def plot_node_removal(results):
    plt.clf()
    plt.plot(results.keys(), results.values(), label=('BST', 'AVL'))

    plt.xlabel('amount of removed elements')
    plt.ylabel('time (s)')
    plt.title('Time needed to remove n elements from a 10k-element tree')
    plt.xticks(list(results.keys())[1::2])
    plt.legend()
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_node_removal.png"]))


def plot_node_finding(results):
    plt.clf()
    plt.plot(results.keys(), results.values(), label=('BST', 'AVL'))

    plt.xlabel('amount of elements searched for')
    plt.ylabel('time (s)')
    plt.title('Time needed to find n elements in a 10k-element tree')
    plt.xticks(list(results.keys()))
    plt.legend()
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_node_finding.png"]))


def compare_tree_creation():
    results = {}
    count = [(n + 1) * 1000 for n in range(10)]
    for n in count:
        content = generate_input_data(n)

        bst_results = run_tree_creation(BST, content)
        avl_results = run_tree_creation(AVL, content)
        results[n] = (bst_results, avl_results)

    return results


def run_tree_creation(tree_class, content):
    timer = timeit.Timer(lambda: tree_class(lst=content))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def compare_node_removal():
    results = {}
    count = [(n + 1) * 250 for n in range(20)]
    # constant amount of input elements throughout all tests
    content = generate_input_data(10000)
    for n in count:
        bst_time = 0
        avl_time = 0
        for _ in range(num_of_repetitions):
            bst_time += run_node_removal(BST, content, n)
            avl_time += run_node_removal(AVL, content, n)

        results[n] = (bst_time / num_of_repetitions, avl_time / num_of_repetitions)

    return results


def run_node_removal(tree_class, content, count):
    tree = tree_class(content)
    nodes_to_remove = content[:count]
    timer = timeit.Timer(lambda: tree.remove_nodes(nodes_to_remove))
    return timer.timeit(1)


def compare_node_finding():
    results = {}
    count = [(n + 1) * 1000 for n in range(10)]
    content = generate_input_data(10000)
    for n in count:
        to_find = content[:n]

        bst_results = run_node_finding(BST, content, to_find)
        avl_results = run_node_finding(AVL, content, to_find)
        results[n] = (bst_results, avl_results)

    return results


def run_node_finding(tree_class, content, to_find):
    tree = tree_class(content)
    timer = timeit.Timer(lambda: [tree.find_node(x) for x in to_find])
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def generate_input_data(size):
    return np.random.randint(low=1, high=10000, size=size).tolist()


if __name__ == "__main__":
    main()
