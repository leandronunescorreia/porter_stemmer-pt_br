import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rules.rule_processor import process_rule
from rules import data

class TestVerbalRules(unittest.TestCase):
    
    def test_verbal_of_preterito_imperfeito_subjuntivo(self):
        preterito_imperfeito_subjuntivo = [
            ("amássemo", "am"), 
            ("cantássemo", "cant"),
            ("falássemo", "fal"),
            ("vendêssemo", "vend"),
            ("comêssemo", "com"),
            ("perdêssemo", "perd"),
            ("partíssemo", "part"),
            ("abríssemo", "abr"),
            ("assistíssemo", "assist"),
            ("vivêssemo", "viv"),
            ("tivéssemo", "tivéss"),
            ("pudéssemo", "pudéss"),
            ("soubéssemo", "soubéss"),
            ("quiséssemo", "quiséss"),
            ("vissemo", "viss"),
            ("disséssemo", "disséss"),
            ("fôssemo", "fôss"),
            ("trouxéssemo", "trouxéss"),
            ("ouvíssemo", "ouv"),
            ("servíssemo", "serv"),
            ("vestíssemo", "vest"),
            ("preferíssemo", "prefer"),
            ("subíssemo", "sub"),
            ("corrêssemo", "corr"),
            ("entendêssemo", "entend"),
            ("esquecêssemo", "esquec"),
            ("crescessemo", "crescess"),
            ("recebêssemo", "receb"),
            ("existíssemo", "exist"),
            ("resolvêssemo", "resolv")
        ]

        for verbal, expected_base in preterito_imperfeito_subjuntivo:
            with self.subTest(verbal=verbal):
                result = process_rule(verbal, data.verbal_rules)
                self.assertEqual(result, expected_base, f"Failed for verbal: {verbal}")


    def test_verbal_of_futuro_do_presente(self):
        futuro_presente = [
            ("cantarei", "cant"),
            ("vencerei", "venc"), 
            ("partirei", "part"),
            ("amarão", "am"),
            ("comerão", "com"), 
            ("partirão", "part"),
            ("trabalharei", "trabalh"),
            ("correrei", "corr"),
            ("subirei", "sub"),
            ("falarei", "fal"),
            ("beberei", "beb"),
            ("assistirei", "assist"),
            ("chegarei", "cheg"),
            ("resolverei", "resolv"),
            ("escreverei", "escrev"),
            ("andarei", "and"),
            ("venderei", "vend"),
            ("abrirei", "abr"),
            ("perdoarei", "perdo"),
            ("entenderei", "entend"),
            ("sorrirei", "sorr"),
            ("construirei", "constru"),
            ("gritarei", "grit"),
            ("navegarei", "naveg"),
            ("pedirei", "ped"),
            ("escolherei", "escolh"), 
            ("defenderei", "defend"),
            ("voltarei", "volt"),
            ("desistirei", "desist"), 
            ("votarei", "vot")
        ]

        for verbal, expected_base in futuro_presente:
            with self.subTest(verbal=verbal):
                result = process_rule(verbal, data.verbal_rules)
                self.assertEqual(result, expected_base, f"Failed for verbal: {verbal}")                


    def test_verbal_of_futuro_do_subjuntivo(self):
        futuro_subjuntivo = [
            ("amarem", "am"),
            ("falarem", "fal"),
            ("venderem", "vend"),
            ("partirem", "part"),
            ("abrirem", "abr"),
            ("correrem", "corr"),
            ("escreverem", "escrev"),
            ("subirem", "sub"),
            ("servirem", "serv"),
            ("ouvirem", "ouv"),
            ("chegarem", "cheg"),
            ("resolverem", "resolv"),
            ("entenderem", "entend"),
            ("preferirem", "prefer"),
            ("vestirem", "vest"),
            ("existirem", "exist"),
            ("rirem", "rir"), 
            ("sorrirem", "sorr"),
            ("irem", "ir"),
            ("estiverem", "estiv"),
            ("puderem", "pud"),
            ("souberem", "soub"),
            ("quiserem", "quis"),
            ("vierem", "vier"),
            ("caírem", "caír"),
            ("lerem", "ler"),
            ("conhecerem", "conhec"),
            ("perderem", "perd"),
            ("correrem", "corr"),
            ("viverem", "viv")
        ]

        for verbal, expected_base in futuro_subjuntivo:
            with self.subTest(verbal=verbal):
                result = process_rule(verbal, data.verbal_rules)
                self.assertEqual(result, expected_base, f"Failed for verbal: {verbal}")

    def test_verbal_of_preterito_perfeito(self):
        preterito_perfeito = [
            ("amaram", "am"),
            ("cantaram", "cant"),
            ("falaram", "fal"),
            ("venderam", "vend"),
            ("comeram", "com"),
            ("perderam", "perd"),
            ("partiram", "part"),
            ("abriram", "abr"),
            ("assistiram", "assist"),
            ("viveram", "viv"),
            ("tiveram", "tiv"),
            ("puderam", "pud"),
            ("souberam", "soub"),
            ("quiseram", "quis"),
            ("viram", "vir"),
            ("disseram", "diss"),
            ("foram", "for"),
            ("trouxeram", "troux"),
            ("ouviram", "ouv"),
            ("serviram", "serv"),
            ("vestiram", "vest"),
            ("preferiram", "prefer"),
            ("subiram", "sub"),
            ("correram", "corr"),
            ("entenderam", "entend"),
            ("esqueceram", "esquec"),
            ("cresceram", "cresc"),
            ("receberam", "receb"),
            ("existiram", "exist"), 
            ("resolveram", "resolv"),
        ]

        for verbal, expected_base in preterito_perfeito:
            with self.subTest(verbal=verbal):
                result = process_rule(verbal, data.verbal_rules)
                self.assertEqual(result, expected_base, f"Failed for verbal: {verbal}")



    def test_verbal_of_gerundio(self):
        gerundio = [
            ("amando", "am"),
            ("falando", "fal"),
            ("vendendo", "vend"),
            ("comendo", "com"),
            ("partindo", "part"),
            ("abrindo", "abr"),
            ("correndo", "corr"),
            ("escrevendo", "escrev"),
            ("subindo", "sub"),
            ("servindo", "serv"),
            ("ouvindo", "ouv"),
            ("chegando", "cheg"),
            ("resolvendo", "resolv"),
            ("entendendo", "entend"),
            ("preferindo", "prefer"),
            ("vestindo", "vest"),
            ("existindo", "exist"),
            ("rindo", "rindo"),
            ("sorrindo", "sorr"), 
            ("caindo", "caindo"),
            ("lendo", "lendo"),
            ("conhecendo", "conhec"),
            ("perdendo", "perd"),
            ("vivendo", "viv"),
            ("fazendo", "faz"),
            ("dizendo", "diz"), 
            ("trazendo", "traz"),
            ("podendo", "pod"),
            ("sabendo", "sab"),
            ("querendo", "quer")
        ]

        for verbal, expected_base in gerundio:
            with self.subTest(verbal=verbal):
                result = process_rule(verbal, data.verbal_rules)
                self.assertEqual(result, expected_base, f"Failed for verbal: {verbal}")    



    def test_verbal_of_condicional(self):
        condicional = [
            ("amariam", "am"), 
            ("falariam", "fal"),
            ("venderiam", "vend"),
            ("partiriam", "part"),
            ("abririam", "abr"), 
            ("correriam", "corr"),
            ("escreveriam", "escrev"),
            ("subiriam", "sub"), 
            ("serviriam", "serv"),
            ("ouviriam", "ouv"),
            ("chegariam", "cheg"),
            ("resolveriam", "resolv"),
            ("entenderiam", "entend"), 
            ("prefeririam", "prefer"), 
            ("vestiriam", "vest"),
            ("existiriam", "exist"),
            ("riríamo", "rir"),
            ("sorriríamo", "sorr"),
            ("iríamo", "irí"),
            ("estaríamo", "est"), 
            ("poderíamo", "pod"),
            ("saberíamo", "sab"),
            ("quereríamo", "quer"),
            ("viríamo", "vir"),
            ("cairíamo", "ca"),
            ("leríamo", "ler"), 
            ("conheceríamo", "conhec"),
            ("perderíamo", "perd"),
            ("correríamo", "corr"),
            ("viveríamo", "viv")
        ]

        for verbal, expected_base in condicional:
            with self.subTest(verbal=verbal):
                result = process_rule(verbal, data.verbal_rules)
                self.assertEqual(result, expected_base, f"Failed for verbal: {verbal}")   


if __name__ == "__main__":
    unittest.main()