import hashlib
from sklearn.feature_extraction import DictVectorizer
from collections import Counter

MAX_CHARS = 521
MAX_BIGRAMS = 1031
MAX_TRIGRAMS = 1031

MAXES = [MAX_CHARS, MAX_BIGRAMS, MAX_TRIGRAMS]

# v = joblib.load('dict_vectorizer_model.pkl')

MAX_SHIFT = []
for i in range(len(MAXES)):
    MAX_SHIFT += [sum(MAXES[:i])]

def shift_keys(dicts, MAX_SHIFT):
    new_dict = {}
    dicts = list(dicts)
    new_dict.update(dicts[0].items())
    new_dict.update({k + MAX_SHIFT[1]: v for k, v in dicts[1].items()})
    new_dict.update({k + MAX_SHIFT[2]: v for k, v in dicts[2].items()})
    return new_dict

def reproducible_hash(string):
    """
    reproducible hash on any string
    
    Arguments:
       string: python string object
    
    Returns:
       signed int64
    """
    
    # We are using MD5 for speed not security.
    h = hashlib.md5(string.encode("utf-8"), usedforsecurity=False)
    return int.from_bytes(h.digest()[0:8], 'big', signed=True)

def ngrams(sentence, n=1, lc=True):
    ngram_l = []
    if lc:
        sentence.lower()
    for i in range(len(sentence) - n + 1):
        ngram_l.append(sentence[i:i+n])
    return ngram_l

def all_ngrams(sentence, max_ngram=3, lc=True):
    all_ngram_list = []
    for i in range(1, max_ngram + 1):
        all_ngram_list += [ngrams(sentence, n=i, lc=lc)]
    return all_ngram_list

def hash_ngrams(ngrams, modulos):
    hash_codes = []
    chars = [reproducible_hash(i) % MAX_CHARS for i in ngrams[0]]
    bigrams = [reproducible_hash(i) % MAX_BIGRAMS for i in ngrams[1]]
    trigrams = [reproducible_hash(i) % MAX_TRIGRAMS for i in ngrams[2]]
    hash_codes = [chars, bigrams, trigrams]
    return hash_codes

def calc_rel_freq(codes):
    cnt = Counter(codes)
    cnt = Counter({k: v / total for total in (sum(cnt.values()),) for k, v in cnt.items()})
    return cnt

def build_freq_dict(sentence, MAXES=MAXES, MAX_SHIFT=MAX_SHIFT):
    hngrams = hash_ngrams(all_ngrams(sentence), MAXES)
    fhcodes = map(calc_rel_freq, hngrams)
    return shift_keys(fhcodes, MAX_SHIFT)

def transform_sentence(sentence: str, dict_vectorizer_model: DictVectorizer):
    vectorized_dict = build_freq_dict(sentence)
    return dict_vectorizer_model.transform([vectorized_dict])

