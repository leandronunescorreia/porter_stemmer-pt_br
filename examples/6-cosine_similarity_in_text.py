# -*- coding: utf-8 -*-
import sys
import os
import re
import json
import numpy as np
from collections import Counter
from numpy.linalg import norm

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stemmer_pt_br import stemmer_pt_br
from utils.string_utils import tokenize, create_word_mappings, encode_words, decode_indices

# --- Preparação stopwords ---
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

# Gerar vetor de caracteres
def word_to_char_vector(word, alphabet):
    counter = Counter(word)
    return np.array([counter.get(c, 0) for c in alphabet])

# Similaridade de cosseno
def cosine_similarity(v1, v2):
    if norm(v1) == 0 or norm(v2) == 0:
        return 0.0
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

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

    # --- NOVO: criar vetores dos stems ---
    alphabet = list("abcdefghijklmnopqrstuvwxyzáàãâéêíóôõúç")
    stem_vectors = {word: word_to_char_vector(word, alphabet) for word in unique_stems}

    return all_tokens, all_stems, word2idx, idx2word, encoded_lines, stem_vectors

def find_similar_stems(phrase, stem_vectors, threshold=0.7):
    alphabet = list("abcdefghijklmnopqrstuvwxyzáàãâéêíóôõúç")
    tokens = re.sub(r'[^a-zà-ú\s]', '', phrase.lower()).split()
    
    all_similar_stems = set()
    
    for token in tokens:
        stem = stemmer_pt_br(token)
        query_vector = word_to_char_vector(stem, alphabet)
        
        for word, vector in stem_vectors.items():
            score = cosine_similarity(query_vector, vector)
            if score >= threshold:
                all_similar_stems.add(word)
    
    return list(all_similar_stems)

def search_in_encoded_lines_multiple_stems(stems_list, word2idx, encoded_lines, lines_text_original):
    # Converte stems para indices
    query_indices = [word2idx[stem] for stem in stems_list if stem in word2idx]

    results = []

    for i, line in enumerate(encoded_lines):
        if any(idx in line for idx in query_indices):
            results.append((i, lines_text_original[i].strip()))

    return results

# --- Programa Principal ---

def main():
    text_lines = read_text_file_lines("examples/legiao.txt")

    tokens, stems, word2idx, idx2word, encoded_lines, stem_vectors = build_corpus_per_line(text_lines)

    # Pesquisa
    while True:
        query = input("\nDigite sua busca (ou 'quit' para sair): ").strip()
        if query.lower() == "quit":
            print("Encerrando busca...")
            break
        print(f"\nBuscando por: '{query}'...\n")

        similar_stems = find_similar_stems(query, stem_vectors, threshold=0.9)

        if not similar_stems:
            print("Nenhuma palavra semelhante encontrada no corpus.")
            return

        print(f"Stems semelhantes encontrados: {similar_stems}")

        matches = search_in_encoded_lines_multiple_stems(similar_stems, word2idx, encoded_lines, text_lines)

        if matches:
            print(f"\nResultados encontrados:")
            for line_num, line_text in matches:
                print(f"Linha {line_num}: {line_text}")
        else:
            print("Nenhum resultado encontrado.")

if __name__ == "__main__":
    main()
