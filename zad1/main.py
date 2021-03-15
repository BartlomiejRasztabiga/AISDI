import sys

alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}


def file_to_morse(filename):
    pass


def strings_to_morse(strings):
    pass


def string_to_morse(string):
    pass


def char_to_morse(char):
    char_upper = char.upper()
    if char_upper in alphabet:
        return alphabet[char_upper]
    else:
        return None


def read_file(filename):
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No filename given")
        exit(-1)
    else:
        filename = sys.argv[1]
        file_to_morse(filename)
