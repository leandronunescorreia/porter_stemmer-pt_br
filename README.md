###### porter_stemmer-pt_br

Porter Stemmer for Brazilian Portuguese  - This project implements a simplified version of the Porter stemming algorithm adapted for Brazilian Portuguese (pt-BR).

## **Porter Stemmer for Brazilian Portuguese**

The main goal is to reduce words to their stems by systematically removing plural, verbal, augmentative, diminutive, adverbial, and nominal suffixes, without considering grammatical context or producing linguistically correct lemmas.

The project follows clean code practices and is modularized into distinct components:

* **Rules** : Organized sets of suffix removal rules for different grammatical categories.
* **Utilities** : Text normalization (accent and punctuation removal) and rule processing helpers.
* **Stemmer Core** : Orchestrates the stemming process through sequential application of rule sets.
* **Examples and Tests** : Demonstrates usage and ensures correctness with automated testing.

This stemmer is lightweight, fast, and designed for tasks such as information retrieval, text classification, and natural language processing pipelines involving Portuguese texts.

###### References:

About Porter algorithm:
[Felipe Nunes Flores - Avaliando o Impactor da Qualidade de um algoritmo de Stemming na recuperação de informações](https://lume.ufrgs.br/bitstream/handle/10183/18532/000730582.pdf?sequence=1)



[Alexandre Ramos Coelho = Stemming para a Língua portuguesa](https://lume.ufrgs.br/bitstream/handle/10183/23576/000597277.pdf?sequence=1)


Portuguese grammar:
[About portuguese prefixes and sufixes](https://www.educamaisbrasil.com.br/enem/lingua-portuguesa/prefixo-e-sufixo)
