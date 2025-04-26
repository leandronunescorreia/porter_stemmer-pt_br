import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rules.rule_processor import process_rule
from rules import data

class TestFeminineRules(unittest.TestCase):
    def test_feminine_to_masculine(self):
        test_cases = [
            ("menina", "menino"),
            ("bibliotecária", "bibliotecário"),
            ("dentista", "dentista"),
            ("anestesista", "anestesista"),            
            ("atriz", "ator"),
            ("leoa", "leão"),
            ("patroa", "patrão"),
            ("camponesa", "camponês"),
            ("formosa", "formoso"),
            ("rica", "rico"),
            ("amada", "amado"),
            ("querida", "querido"),
            ("linda", "lindo"),
            ("ativa", "ativo"),
            ("engenheira", "engenheiro"),
            ("irmã", "irmão"),
        ]

        for feminine, expected_masculine in test_cases:
            with self.subTest(feminine=feminine):
                result = process_rule(feminine, data.feminine_rules)
                self.assertEqual(result, expected_masculine)

if __name__ == "__main__":
    unittest.main()