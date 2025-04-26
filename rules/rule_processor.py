def process_rule(word, rules):
    for suffix, min_stem_len, replacement in rules:
        if word.endswith(suffix):
            stem = word[:-len(suffix)]
            if len(stem) >= min_stem_len:
                return stem + replacement
    return word