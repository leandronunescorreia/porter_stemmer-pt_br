# -*- coding: utf-8 -*-
import sys
import os
import re
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Imports que você já tem ---
from stemmer_pt_br import stemmer_pt_br
from utils.string_utils import tokenize, create_word_mappings, encode_words, decode_indices

# --- Carregar stopwords ---
stop_words = []
with open("stop_words.json", "r", encoding="utf-8") as file:
    stop_words = set(json.load(file))

# --- 1. Funções utilitárias ---

def read_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def build_corpus(text):
    tokens = tokenize(text, stop_words=stop_words)
    stems = [stemmer_pt_br(token) for token in tokens]
    unique_stems = sorted(set(stems))
    word2idx, idx2word = create_word_mappings(unique_stems)
    corpus_encoded = encode_words(stems, word2idx)
    return tokens, stems, word2idx, idx2word, corpus_encoded

def search_stem(query_word, word2idx, corpus_encoded):
    stem = stemmer_pt_br(query_word.lower())
    if stem not in word2idx:
        print(f"Stem '{stem}' not found in corpus.")
        return []

    idx = word2idx[stem]
    positions = [i for i, token_idx in enumerate(corpus_encoded) if token_idx == idx]
    return positions

# --- 2. Pipeline principal ---

def main():
    # --- Lendo arquivo texto ---
    text = read_text_file("examples\legiao.txt")  # <-- seu arquivo aqui!

    # --- Construindo corpus ---
    tokens, stems, word2idx, idx2word, corpus_encoded = build_corpus(text)

    # --- Pesquisa ---
    query = "cantar"  # Palavra para buscar
    print(f"Searching for: '{query}'...")

    positions = search_stem(query, word2idx, corpus_encoded)

    if not positions:
        print("No matches found.")
    else:
        print(f"Found {len(positions)} match(es) at positions: {positions}")
        for pos in positions:
            print(f"Word at position {pos}: '{tokens[pos]}' (stemmed: '{stems[pos]}')")

if __name__ == "__main__":
    main()
