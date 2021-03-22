import sys


def main():
    if len(sys.argv) < 2:
        print("No file given.")
        exit(-1)
    else:
        filename = sys.argv[1]
        try:
            # main execution here
            pass
        except FileNotFoundError:
            print("Given file doesn't exist.")
            exit(-1)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    main()
