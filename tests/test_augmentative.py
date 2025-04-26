import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rules.rule_processor import process_rule
from rules import data

class TestAugmentativeRules(unittest.TestCase):

    def test_augmentative_rules(self):
        test_cases = [
            ("grandíssimo", "grand"),
            ("amabilíssimo", "amabil"),
            ("fortíssimo", "fort"),
            ("altésimo", "alt"),
            ("paupérrimo", "paup"),
            ("carrinho", "carr"),
            ("pequeninho", "pequen"),
            ("coraçãozinho", "coração"),
            ("pequenaço", "pequen"),
            ("grandão", "grand"),
        ]

        for word, expected_augmentative in test_cases:
            with self.subTest(word=word):
                result = process_rule(word, data.augmentative_rules)
                self.assertEqual(result, expected_augmentative)

if __name__ == "__main__":
    unittest.main()