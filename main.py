import os
import sys
from rules import data
from rules.rule_processor import process_rule, ends_with_s, is_feminine


def main():
    words = ["meninas","bibliotecária", "dentista"]

    for word in words:
        if ends_with_s(word):
            singular_word = process_rule(word, data.plural_rules)
            print(f"singular of {word}: {singular_word}")

        if is_feminine(word):
            masculine_word = process_rule(word, data.feminine_rules)
            print(f"masculine of {word}: {masculine_word}")

if __name__ == "__main__":
    main()