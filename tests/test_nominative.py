import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rules.rule_processor import process_rule
from rules import data

class TestNominativeRules(unittest.TestCase):

    def test_nominative_rules(self):
        test_cases = [
            ("realizador", "realiz"),
            ("organizador", "organiz"),
            ("sapateiro", "sapat"),
            ("bondoso", "bond"),
            ("amigo", "amigo"),
            ("ator", "at"),
            ("diretor", "dire"),
            ("professor", "profes"),
            ("habilidoso", "habilid"),
            ("eficiente", "eficiente"),
            ("importante", "import"),
            ("amizadeiro", "amiz"),
            ("engenheiro", "engenh"),
            ("vitorioso", "vitori"),
            ("glorioso", "glori"),
            ("jangadeiro", "jang"),
            ("habilidoso", "habilid"),
            ("curioso", "curi"),
            ("amável", "am"),
            ("responsável", "respons"),
            ("padeiro", "pad"),
            ("bombeiro", "bomb"),
            ("generoso", "gener"),
            ("piedoso", "pied"),
        ]

        for word, expected_nominative in test_cases:
            with self.subTest(word=word):
                result = process_rule(word, data.nominative_rules)
                self.assertEqual(result, expected_nominative)

if __name__ == "__main__":
    unittest.main()