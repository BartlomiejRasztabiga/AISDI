import sys
import timeit
import algorithms
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) < 2:
        print("No file given.")
        exit(-1)
    else:
        filename = sys.argv[1]
        try:
            compare_algorithms(filename)
        except FileNotFoundError:
            print("Given file doesn't exist.")
            exit(-1)


def compare_algorithms(filename):
    lines = read_file(filename)

    # 1000, 2000, ..., 10000
    count = [(n + 1) * 1000 for n in range(10)]
    times = {}

    for n in count:
        results = run_algorithms(lines, n)
        print("Results for {} words: {}".format(n, results))
        for algorithm, time in results.items():
            if algorithm not in times.keys():
                times[algorithm] = []
            times[algorithm].append(time)

    for algorithm, results in times.items():
        plt.plot(count, results, label=algorithm)

    plt.xlabel('list length (words)')
    plt.ylabel('time (s)')
    plt.title('Time needed for each algorithm to sort n elements')
    plt.xticks(count)
    plt.legend()
    plt.grid()
    plt.savefig('graph.png')


def run_algorithms(lines, n):
    arr = get_first_n_words(lines, n)

    algorithm_functions = ["merge_sort", "quick_sort", "bubble_sort", "selection_sort"]
    num_of_repetitions = 3  # num of repetitions to get avg time
    time_results = {}

    for algorithm in algorithm_functions:
        timer = timeit.Timer(lambda _algorithm=algorithm: run_algorithm(_algorithm, arr[:]))
        time = timer.timeit(num_of_repetitions)
        time_results[algorithm] = time / num_of_repetitions

    return time_results


def run_algorithm(algo_name, arr):
    algo_to_run = getattr(algorithms, algo_name)
    result = algo_to_run(arr)
    return result


def get_first_n_words(lines, n):
    selected_words = []

    for line in lines:
        for word in line.strip().split():
            if len(selected_words) >= n:
                return selected_words
            selected_words.append(word)

    return selected_words


def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.readlines()


if __name__ == "__main__":
    main()
