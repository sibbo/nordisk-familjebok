import regex as re

# --- Data classification related regex functions ---
def __extract_feature_with_regex__(line:str, regex: str) -> int:
    return 1 if re.search(regex, line) else 0

def punctuation_after_first_word(line) -> int:  
    return __extract_feature_with_regex__(line, r"^[\p{L}'\-]+(?=,|\.)")

def square_bracket(line) -> int:
    return __extract_feature_with_regex__(line, r"^.{0,40}\[")

def square_bracket_with_punctuation(line) -> int:
    return __extract_feature_with_regex__(line, r"^.{0,40}\[.{1,20}?\](?=\,|\.)")

def parentheses(line) -> int:
    return __extract_feature_with_regex__(line, r"^.{0,40}\(")

def parentheses_with_punctuation(line) -> int:
    return __extract_feature_with_regex__(line, r"^.{0,40}\(.{1,20}?\)(?=\,|\.)")

def category_word(line) -> int: 
    return __extract_feature_with_regex__(line, r"^.{1,70},\s+\p{L}{1,11}\.")

# --- Other utility functions ---
                    
def words_in_line(line:str) -> list[str]:
    return re.findall(r"\p{L}+", line)

def get_headword_from_text(line: str) -> str:
    line = re.sub(r"\[[^\]]*\]|\([^)]*\)", '', line)
    search = re.search(r"^.{1,20}?[.,]", line)
    if search:
        return remove_trailing_punctuation(search[0])
    else:
        return remove_trailing_punctuation(words_in_line(line)[0])
    
def get_headword_from_index(line: str) -> str:
    line = re.sub(r"\[[^\]]*\]|\([^)]*\)", '', line)
    if re.search(r"[.,]", line):
        search = re.search(r"^.{1,20}?[.,]", line)
        if search:
            return remove_trailing_punctuation(search[0])
    if len(line) > 20: ## LA TILL DETTA
        return remove_trailing_punctuation(words_in_line(line)[0])
    return remove_trailing_punctuation(line)

def get_headword_no_closing_bold_tag(line: str) -> str:
    line = line[3:]
    closed = re.findall(r"^(.+?)<", line)
    if closed:
        text = closed[0]
        if len(text) <= 20:
            return remove_trailing_punctuation(text)
    return remove_trailing_punctuation(words_in_line(line)[0])
        
def remove_trailing_punctuation(line: str) -> str:
    return re.sub(r"[,.\s]*$", "", line)