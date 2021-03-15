import os
from main import char_to_morse, string_to_morse, strings_to_morse


def test_char_to_morse():
    assert char_to_morse('w') == '.--'
    assert char_to_morse('e') == '.'
    assert char_to_morse('i') == '..'
    assert char_to_morse('t') == '-'
    assert char_to_morse('i') == '..'
    assert char_to_morse(' ') == '/'
    assert char_to_morse('p') == '.--.'
    assert char_to_morse('w') == '.--'


def test_string_to_morse():
    assert string_to_morse(
        'Ala ma kota') == r'.- .-.. .- / -- .- / -.- --- - .-'
    assert string_to_morse('a12b 3 c') == r'.- -... / -.-.'


def test_strings_to_morse():
    input_text = [
        'Ala ma kota',
        'a kot ma Ale',
        'a12b 3 c'
    ]
    desired_output = os.linesep.join([
        '.- .-.. .- / -- .- / -.- --- - .-',
        '.- / -.- --- - / -- .- / .- .-.. .',
        '.- -... / -.-.'
    ])
    assert strings_to_morse(input_text) == desired_output
