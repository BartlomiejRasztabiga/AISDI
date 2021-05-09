import codecs
import os
import timeit

import matplotlib.pyplot as plt
import numpy as np

from heap import BinaryHeap, TernaryHeap, QuarternaryHeap

num_of_repetitions = 100  # num of repetitions to get avg time
results_folder = "results"


def main():
    results_str = "Wyniki pomiarów:\n\n"

    results_str += "Tworzenie kopców z n elementów:\n"
    tree_creation_results = compare_heap_creation()
    tree_str = format_results(tree_creation_results)
    results_str += tree_str + "\n\n"

    plot_all_heaps_creation(tree_creation_results)
    plot_individual_heaps_creation(tree_creation_results)

    print(results_str)
    with codecs.open(os.sep.join([results_folder, "results.txt"]), "w", "utf-8") as file:
        file.write(results_str)


def format_results(results):
    return "\n".join([
        f"{count}:\t2-ary: {round(result[0], 7)}s\t\t3-ary: {round(result[1], 8)}s\t\t4-ary: {round(result[2], 8)}s"
        for count, result in results.items()
    ])


def plot_all_heaps_creation(results):
    plt.clf()
    plt.plot(results.keys(), results.values())

    plt.xlabel('amount of elements in the input data')
    plt.ylabel('time (s)')
    plt.title('Time needed to create a heap from n elements')
    plt.xticks(list(results.keys()))
    plt.legend(('2-ary', '3-ary', '4-ary'))
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_heap_creation.png"]))


def plot_individual_heaps_creation(results):
    binary = {key: value[0] for key, value in results.items()}
    ternary = {key: value[1] for key, value in results.items()}
    quaternary = {key: value[2] for key, value in results.items()}

    plot_2ary_heap_creation(binary)
    plot_3ary_heap_creation(ternary)
    plot_4ary_heap_creation(quaternary)


def plot_2ary_heap_creation(results):
    plt.clf()
    plt.plot(results.keys(), results.values(), label='2-ary')

    plt.xlabel('amount of elements in the input data')
    plt.ylabel('time (s)')
    plt.title('Time needed to create a heap from n elements')
    plt.xticks(list(results.keys()))
    plt.legend()
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_2ary_heap_creation.png"]))


def plot_3ary_heap_creation(results):
    plt.clf()
    plt.plot(results.keys(), results.values(), label='3-ary')

    plt.xlabel('amount of elements in the input data')
    plt.ylabel('time (s)')
    plt.title('Time needed to create a heap from n elements')
    plt.xticks(list(results.keys()))
    plt.legend()
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_3ary_heap_creation.png"]))


def plot_4ary_heap_creation(results):
    plt.clf()
    plt.plot(results.keys(), results.values(), label='4-ary')

    plt.xlabel('amount of elements in the input data')
    plt.ylabel('time (s)')
    plt.title('Time needed to create a heap from n elements')
    plt.xticks(list(results.keys()))
    plt.legend()
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_4ary_heap_creation.png"]))


def compare_heap_creation():
    results = {}
    count = [(n + 1) * 1000 for n in range(10)]
    for n in count:
        content = generate_input_data(n)

        binary_results = run_heap_creation(BinaryHeap, content)
        ternary_results = run_heap_creation(TernaryHeap, content)
        quaternary_results = run_heap_creation(QuarternaryHeap, content)
        results[n] = (binary_results, ternary_results, quaternary_results)

    return results


def run_heap_creation(heap_class, content):
    timer = timeit.Timer(create_heap(heap_class, content))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def create_heap(heap_class, content):
    def _create_heap():
        heap = heap_class()
        for item in content:
            heap.push(item)

    return _create_heap


def generate_input_data(size):
    return np.random.randint(low=1, high=10000, size=size).tolist()


if __name__ == "__main__":
    main()
