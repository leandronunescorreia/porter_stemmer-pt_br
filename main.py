import os
import sys
from rules import data
from rules import rule_processor


def main():
    words = ["meninas","bibliotecária", "dentista"]

    for word in words:
        singular_word = rule_processor.process_rule(word, data.plural_rules)
        print(f"singular of {word}: {singular_word}")

        masculine_word = rule_processor.process_rule(word, data.feminine_rules)
        print(f"masculine_word of {word}: {masculine_word}")

if __name__ == "__main__":
    main()