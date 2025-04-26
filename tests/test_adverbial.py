import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rules.rule_processor import process_rule
from rules import data

class TestAdverbialRules(unittest.TestCase):
    def test_adverbial_to_base(self):
        test_cases = [
            ("rapidamente", "rapida"),
            ("lentamente", "lenta"),
            ("felizmente", "feliz"),
            ("claramente", "clara"),
            ("facilmente", "facil"),
            ("imperativamente", "imperativa"),
            ("empoderadamente", "empoderada"),
        ]

        for adverbial, expected_base in test_cases:
            with self.subTest(adverbial=adverbial):
                result = process_rule(adverbial, data.adverbial_rules)
                self.assertEqual(result, expected_base)

if __name__ == "__main__":
    unittest.main()