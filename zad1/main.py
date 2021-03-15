import os
import re
import sys
from string import ascii_letters

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
allowed_chars = ascii_letters + ' '


def file_to_morse(filename):
    lines = read_file(filename)
    return strings_to_morse(lines)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def strings_to_morse(strings):
    return os.linesep.join(map(string_to_morse, strings))


def string_to_morse(string):
    string = filter_allowed_chars(string)
    string = remove_extra_spaces(string)
    return " ".join(map(char_to_morse, string))


def filter_allowed_chars(string):
    return "".join(filter(lambda x: x in allowed_chars, string))


def remove_extra_spaces(string):
    return re.sub(' +', ' ', string)


def char_to_morse(char):
    char_upper = char.upper()
    if char_upper.isspace():
        return '/'
    if char_upper in alphabet:
        return alphabet[char_upper]
    else:
        return ''


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No file given.")
        exit(-1)
    else:
        filename = sys.argv[1]
        try:
            morse = file_to_morse(filename)
            print(morse)
        except FileNotFoundError:
            print("Given file doesn't exist.")
            exit(-1)
