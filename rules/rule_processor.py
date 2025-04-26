from .data import feminine_rules

def process_rule(word, rules):
    for suffix, min_stem_len, replacement in rules:
        if word.endswith(suffix):
            stem = word[:-len(suffix)]
            if len(stem) >= min_stem_len:
                return stem + replacement
    return word

def ends_with_s(word):
    return word.endswith('s')

def is_feminine(word):
    return any(word.endswith(suffix) for suffix, _, _ in feminine_rules)