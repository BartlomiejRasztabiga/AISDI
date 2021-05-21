import codecs
import os
import timeit

import matplotlib.pyplot as plt

from algorithms import find_naive, find_kmp, find_kr

num_of_repetitions = 10  # num of repetitions to get avg time
results_folder = "results"


def main():
    results_str = "Wyniki pomiarów:\n\n"

    substring_find_results = compare_algorithms()
    results_str += "Szukanie n słów w tekście:\n"
    results_str += format_results(substring_find_results) + "\n\n"

    plot_all_algorithms(substring_find_results)

    with codecs.open(os.sep.join([results_folder, "results.txt"]), "w", "utf-8") as file:
        file.write(results_str)


def format_results(results):
    return "\n".join([
        f"{count}:\tNaive: {round(result[0], 7)}s\t\tKMP: {round(result[1], 8)}s\t\tKR: {round(result[2], 8)}s"
        for count, result in results.items()
    ])


def plot_all_algorithms(results):
    plt.clf()
    plt.plot(results.keys(), results.values())

    plt.xlabel('amount of elements in the input data')
    plt.ylabel('time (s)')
    plt.title('Time needed to find n strings in text')
    plt.xticks(list(results.keys()))
    plt.legend(('Naive', 'KMP', 'KR'))
    plt.grid()
    plt.savefig(os.sep.join([results_folder, "graph_substring_find.png"]))


def compare_algorithms():
    results = {}
    count = [n * 100 for n in range(1, 11)]  # pan tadeusz has 68 682 words
    for n in count:
        content = generate_input_data(n)

        naive_results = run_find_substrings(find_naive, content)
        kmp_results = run_find_substrings(find_kmp, content)
        kr_results = run_find_substrings(find_kr, content)
        results[n] = (naive_results, kmp_results, kr_results)

    return results


def run_find_substrings(find_function, text):
    timer = timeit.Timer(find_substrings(find_function, text))
    time = timer.timeit(num_of_repetitions)
    return time / num_of_repetitions


def find_substrings(find, text):
    def _find_substrings():
        for word in text:
            find(word, text)

    return _find_substrings


def generate_input_data(size):
    lines = read_file("pan-tadeusz.txt")
    first_n_words = get_first_n_words(lines, size)

    return first_n_words


def get_first_n_words(lines, n):
    selected_words = []

    for line in lines:
        for word in line.strip().split():
            if len(selected_words) >= n:
                return " ".join(selected_words)
            selected_words.append(word)

    return " ".join(selected_words)


def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.readlines()


if __name__ == "__main__":
    main()
