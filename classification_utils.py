import regex_utils as ru
import numpy as np
import pickle

# Word frequencies 
def get_word_frequencies() -> tuple[dict[str, int], int]:
    _frequencies = {}
    with open('word_frequencies.pickle', 'rb') as handle:
        _frequencies = pickle.load(handle)
    _max_frequency = max(_frequencies.values())
    return _frequencies, _max_frequency


def relative_word_frequency(word: str, frequencies: dict[str, int], max_frequency: int) -> float:
    return frequencies[word] / max_frequency

def line_to_datapoint(line: str, frequencies: dict[str, int], max_frequency: int):
    return np.array([[
        ru.punctuation_after_first_word(line),
        ru.square_bracket(line),
        ru.square_bracket_with_punctuation(line),
        ru.parentheses(line),
        ru.parentheses_with_punctuation(line),
        ru.category_word(line),
        relative_word_frequency(ru.words_in_line(line)[0].lower(), frequencies, max_frequency),
    ]])

