def generate_substrings(text, length):
    """Generuje wszystkie podciągi text o długości length.
    Np. `generate_substrings("abcdef", 3)`:
    - 0, abc
    - 1, bcd
    - 2, cde
    - 3, def
    """
    substrings = []
    for index in range(0, len(text) - length + 1):
        substrings.append((index, text[index:index + length]))
    return substrings


def find_naive(string, text):
    """
    Naive
    Parameters:
        string (str): szukany napis
        text (str): przeszukiwany tekst
    Returns:
        (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    found = []
    for (index, substring) in generate_substrings(text, len(string)):
        if substring == string:
            found.append(index)
    return found


def find_kmp(string, text):
    """
    Knuth-Morris-Pratt
    Parameters:
        string (str): szukany napis
        text (str): przeszukiwany tekst
    Returns:
        (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    pass


def find_kr(string, text):
    """
    Karp-Rabin
    Parameters:
        string (str): szukany napis
        text (str): przeszukiwany tekst
    Returns:
        (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    pass
