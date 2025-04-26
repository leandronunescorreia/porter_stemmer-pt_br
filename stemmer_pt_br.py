
from rules.rule_processor import process_rule, ends_with_s, is_feminine
from utils.string_utils import remove_accents_and_punctuation
from rules import data

def stemmer_pt_br(word):
    """
    Simple Portuguese stemmer for Brazilian Portuguese.
    This is a basic implementation and may not cover all cases.
    """
    if ends_with_s(word):
        word = process_rule(word, data.plural_rules)

    if is_feminine(word):
        word = process_rule(word, data.feminine_rules)

    word = process_rule(word, data.adverbial_rules)
    word = process_rule(word, data.augmentative_rules)

    old_word = word
    word = process_rule(word, data.nominative_rules)

    if word == old_word:
        old_word = word
        word = process_rule(word, data.verbal_rules)

        if word == old_word:
            word = process_rule(word, data.vowels_rules)

    word = remove_accents_and_punctuation(word)
    return word