# Naive

def generate_substrings(text, length):
    """Generates all substrings of ``text`` of ``length``.
    For example: `generate_substrings("abcdef", 3)`:
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
        string (str): substring to be found
        text (str): text to be searched
    Returns:
        (list): List of positions in ascending order of staring indexexs of ``string`` in``text``.
    """
    found = []
    for (index, substring) in generate_substrings(text, len(string)):
        if substring == string:
            found.append(index)
    return found


# Knuth-Morris-Pratt

def kmp_build_partial_match_table(pattern):
    """
    Builds a partial match table for the KMP algorithm on a pattern.
    """
    table = [0]
    matching_prefix_length = 0
    pattern_char_index = 1

    while pattern_char_index < len(pattern):
        if pattern[matching_prefix_length] == pattern[pattern_char_index]:
            # Prefix-suffix match continues
            matching_prefix_length += 1
        elif matching_prefix_length > 0:
            # Prefix-suffix match broken - and backtracking is possible
            # Backtracking shouldn't cause the pattern_idx to move, since we need to check if (now shorter) pattern still holds.
            matching_prefix_length = table[matching_prefix_length - 1]
            continue

        table.append(matching_prefix_length)
        pattern_char_index += 1

    return table


def find_kmp(string, text):
    """
    Knuth-Morris-Pratt
    Parameters:
        string (str): substring to be found
        text (str): text to be searched
    Returns:
        (list): List of positions in ascending order of staring indexexs of ``string`` in``text``.
    """
    substr_len = len(string)

    kmp_table = kmp_build_partial_match_table(string)
    matches = []

    matched_chars = 0
    text_offset = 0

    while text_offset < len(text):
        if text[text_offset] == string[matched_chars]:
            # Move pointers to the text and pattern
            matched_chars += 1
            text_offset += 1

            # Full match
            if matched_chars == substr_len:
                matches.append(text_offset - substr_len)
                # Backtrack to properly check for overlapping matches
                matched_chars = kmp_table[-1]

        elif matched_chars > 0:
            # Failed to match a character and backtracking is possible - decrease matched_chars.
            # However text_offset stays unchanged, as we need to check if the text still matches the (now shorter) pattern.
            matched_chars = kmp_table[matched_chars - 1]

        else:
            # Mismatched chars at the start of the substring - no backtracking possible - move to the next char in text.
            text_offset += 1

    return matches


# Karp-Rabin

KR_HASH_ALPHABET_SIZE = 256
KR_HASH_MODULUS = 101


def kr_initial_hash(word):
    """
    Calculates hash of a string.
    """
    _hash = 0
    for char in map(ord, word):
        _hash = (_hash * KR_HASH_ALPHABET_SIZE + char) % KR_HASH_MODULUS
    return _hash


def kr_rolling_hash(text, window_size):
    """
    Calculates a rolling hash of a string.
    https://en.wikipedia.org/wiki/Rolling_hash

    An iterator over all substrings of text of size window_size.

    Yields 3-element tuples:
    1. Index of generated substring in text
    2. The hash (as defined in kr_initial_hash)
    3. The substring itself
    """
    first_char_factor = KR_HASH_ALPHABET_SIZE ** (window_size - 1) % KR_HASH_MODULUS

    _hash = kr_initial_hash(text[:window_size])
    max_start_index = len(text) - window_size

    for i in range(max_start_index + 1):
        yield i, _hash, text[i:i + window_size]

        if i != max_start_index:
            # Update the rolling hash
            _hash = ((_hash - ord(text[i]) * first_char_factor) * KR_HASH_ALPHABET_SIZE + ord(
                text[i + window_size])) % KR_HASH_MODULUS


def find_kr(string, text):
    """
    Karp-Rabin
    Parameters:
        string (str): substring to be found
        text (str): text to be searched
    Returns:
        (list): List of positions in ascending order of staring indexexs of ``string`` in``text``.
    """
    if not string:
        print('DUPA')
        return list(range(len(text) + 1))

    string_hash = kr_initial_hash(string)

    return [
        i for (i, text_hash, possible_match) in kr_rolling_hash(text, len(string))
        if text_hash == string_hash and possible_match == string
    ]
