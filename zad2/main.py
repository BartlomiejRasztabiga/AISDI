import sys
import timeit
import algorithms


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

    count = [100, 1000, 10000, 100000]
    for n in count:
        print("Results for {} words: {}".format(n, run_algorithms(lines, n)))

    # TODO add chart here


def run_algorithms(lines, n):
    arr = get_first_n_words(lines, n)

    algorithm_functions = ["merge_sort", "quick_sort"]  # TODO add other algorithms
    num_of_repetitions = 1000  # num of repetitions to get avg time
    time_results = {}

    for algorithm in algorithm_functions:
        timer = timeit.Timer(lambda _algorithm=algorithm: run_algorithm(_algorithm, arr))
        time = timer.timeit(num_of_repetitions)
        time_results[algorithm] = time / num_of_repetitions

    return time_results


def run_algorithm(algo_name, arr):
    algo_to_run = getattr(algorithms, algo_name)
    result = algo_to_run(arr)
    return result


def get_first_n_words(lines, n):
    selected_words = []

    # TODO refactor to list comprehension?
    for line in lines:
        for word in line.strip().split():
            if len(selected_words) >= n:
                return selected_words
            selected_words.append(word)

    return selected_words


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    main()
