# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stemmer_pt_br import stemmer_pt_br
import json
from utils.string_utils import tokenize, create_word_mappings, encode_words, decode_indices

stop_words = []
with open("stop_words.json", "r", encoding="utf-8") as file:
    stop_words = json.load(file)
    stop_words = set(stop_words)

sample_text = """
Cantei, cantaremos, cantavam, cantando, cantarão!
Falava, falaram, falando, falaríamos.
Vendemos, venderiam, venderão, vendendo.
Corriam, correrei, correriam, correndo.
Abriram, abrirei, abririam, abrindo.
"""


def main():
    tokens = tokenize(sample_text, stop_words=stop_words)
    stems = [stemmer_pt_br(word) for word in tokens]
    unique_stems = sorted(set(stems))

    word2idx, idx2word = create_word_mappings(unique_stems)
    
    corpus_encoded = encode_words(stems, word2idx)
    corpus_decoded = decode_indices(corpus_encoded, idx2word)

    print("Tokens:", tokens)
    print("Stems:", stems)
    print("Word2Idx:", word2idx)
    print("Encoded corpus:", corpus_encoded)
    print("Decoded back:", corpus_decoded)


if __name__ == "__main__":
    main()