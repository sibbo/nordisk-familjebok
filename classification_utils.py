import regex_utils as ru
import numpy as np
import pickle

# Word frequencies 
_frequencies = {}
with open('word_frequencies.pickle', 'rb') as handle:
    _frequencies = pickle.load(handle)
_max_frequency = max(_frequencies.values())

def relative_word_frequency(word: str) -> float:
    return _frequencies[word] / _max_frequency

def line_to_datapoint(line: str):
    return np.array([[
        ru.punctuation_after_first_word(line),
        ru.square_bracket(line),
        ru.square_bracket_with_punctuation(line),
        ru.parentheses(line),
        ru.parentheses_with_punctuation(line),
        ru.category_word(line),
        relative_word_frequency(ru.first_word_in_line(line).lower()),
    ]])

