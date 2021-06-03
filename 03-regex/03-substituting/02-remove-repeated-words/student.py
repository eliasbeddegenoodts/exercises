import re


def remove_repeated_words(string):
    return re.sub(r'([a-zA-Z]+)( \1)+', r'\1', string)
    # ( \1) = the same regex as the first one
    # \1 is equivalent to re.search(...).group(1), the first parentheses-delimited expression inside of the regex.
    # The first \1 means the first group - i.e. the first bracketed expression