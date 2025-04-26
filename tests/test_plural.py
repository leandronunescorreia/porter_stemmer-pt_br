import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rules.rule_processor import process_rule
from rules import data

class TestPluralRules(unittest.TestCase):
    def test_plural_to_singular(self):
        test_cases = [
            ("meninas", "menina"),
            ("ações", "ação"),
            ("peões", "peão"),
            ("leões", "leão"),
            ("pães", "pão"),
            ("canais", "canal"),
            ("papéis", "papel"),
            ("reis", "rei"),
            ("faróis", "farol"),
            ("fuzis", "fuzil"),
            ("móveis", "móvel"),
            ("carros", "carro"),
            ("anzóis", "anzol"),
        ]

        for plural, expected_singular in test_cases:
            with self.subTest(plural=plural):
                result = process_rule(plural, data.plural_rules)
                self.assertEqual(result, expected_singular)

if __name__ == "__main__":
    unittest.main()