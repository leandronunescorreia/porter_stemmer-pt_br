import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from stemmer_pt_br import stemmer_pt_br

class TestStemmerPtBr(unittest.TestCase):
    def test_plural_words(self):
        self.assertEqual(stemmer_pt_br("carros"), "carr")
        self.assertEqual(stemmer_pt_br("casas"), "cas")

    def test_feminine_words(self):
        self.assertEqual(stemmer_pt_br("bonita"), "bonit")
        self.assertEqual(stemmer_pt_br("menina"), "menin")

    def test_adverbial_words(self):
        self.assertEqual(stemmer_pt_br("rapidamente"), "rapid")
        self.assertEqual(stemmer_pt_br("lentamente"), "lent")

    def test_augmentative_words(self):
        self.assertEqual(stemmer_pt_br("carrão"), "carr")
        self.assertEqual(stemmer_pt_br("casarão"), "cas")

    def test_nominative_words(self):
        self.assertEqual(stemmer_pt_br("amigos"), "amig")
        self.assertEqual(stemmer_pt_br("professores"), "profes")

    def test_verbal_words(self):
        self.assertEqual(stemmer_pt_br("cantando"), "cant")
        self.assertEqual(stemmer_pt_br("comendo"), "com")

    def test_vowel_removal(self):
        self.assertEqual(stemmer_pt_br("árvore"), "arvor")
        self.assertEqual(stemmer_pt_br("pássaro"), "passar")

    def test_remove_accents_and_punctuation(self):
        self.assertEqual(stemmer_pt_br("coração!"), "coracao")
        self.assertEqual(stemmer_pt_br("ação?"), "acao")

if __name__ == "__main__":
    unittest.main()