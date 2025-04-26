# -*- coding: utf-8 -*-
import sys
import os
import re
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stemmer_pt_br import stemmer_pt_br
from utils.string_utils import tokenize, create_word_mappings, encode_words, decode_indices

stop_words = []
with open("stop_words.json", "r", encoding="utf-8") as file:
    stop_words = set(json.load(file))

# --- Funções Utilitárias ---

def read_text_file_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()

def tokenize_line(line, stop_words):
    line = line.lower()
    line = re.sub(r'[^a-zà-ú\s]', '', line)
    tokens = line.split()
    return [t for t in tokens if t not in stop_words]

def build_corpus_per_line(lines):
    all_tokens = []
    all_stems = []

    for line in lines:
        tokens = tokenize_line(line, stop_words)
        stems = [stemmer_pt_br(token) for token in tokens]
        all_tokens.append(tokens)
        all_stems.append(stems)

    unique_stems = sorted(set(stem for stems in all_stems for stem in stems))
    word2idx, idx2word = create_word_mappings(unique_stems)

    encoded_lines = [encode_words(stems, word2idx) for stems in all_stems]

    return all_tokens, all_stems, word2idx, idx2word, encoded_lines

def search_in_encoded_lines(query_word, word2idx, encoded_lines, idx2word, lines_text_original):
    stem = stemmer_pt_br(query_word.lower())

    if stem not in word2idx:
        print(f"Stem '{stem}' not found in corpus.")
        return []

    idx = word2idx[stem]
    results = []

    for i, line in enumerate(encoded_lines):
        if idx in line:
            results.append((i, lines_text_original[i].strip()))  # linha e conteúdo

    return results

# --- Programa Principal ---

def main():
    text_lines = read_text_file_lines("examples\legiao.txt")  # seu arquivo real aqui

    tokens, stems, word2idx, idx2word, encoded_lines = build_corpus_per_line(text_lines)

    # Mostrando corpus codificado
    print("Corpus codificado por linhas:")
    for i, line in enumerate(encoded_lines):
        print(f"Linha {i}: {line}")

    # Pesquisa
    query = "coração"
    print(f"\nBuscando por: '{query}'...\n")

    matches = search_in_encoded_lines(query, word2idx, encoded_lines, idx2word, text_lines)

    if matches:
        for line_num, line_text in matches:
            print(f"Linha {line_num}: {line_text}")
    else:
        print("Nenhum resultado encontrado.")

if __name__ == "__main__":
    main()
