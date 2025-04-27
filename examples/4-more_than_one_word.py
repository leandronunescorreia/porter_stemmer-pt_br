import sys
import os
import re
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stemmer_pt_br import stemmer_pt_br
from utils.string_utils import tokenize, create_word_mappings, encode_words, decode_indices

# --- Carregar stopwords ---
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

def search_by_phrase(phrase, word2idx, encoded_lines, idx2word, lines_text_original, mode="OR"):
    # Tokenizar a frase de consulta
    tokens = re.sub(r'[^a-zà-ú\s]', '', phrase.lower()).split()
    stems = [stemmer_pt_br(token) for token in tokens]

    # Verificar se existem stems válidos
    valid_stems = [stem for stem in stems if stem in word2idx]
    if not valid_stems:
        print("Nenhuma palavra da frase encontrada no corpus.")
        return []

    query_indices = [word2idx[stem] for stem in valid_stems]

    results = []

    for i, line in enumerate(encoded_lines):
        if mode == "OR":
            if any(idx in line for idx in query_indices):
                results.append((i, lines_text_original[i].strip()))
        elif mode == "AND":
            if all(idx in line for idx in query_indices):
                results.append((i, lines_text_original[i].strip()))
        else:
            raise ValueError(f"Modo '{mode}' inválido. Use 'OR' ou 'AND'.")

    return results

# --- Programa Principal ---

def main():
    # --- Ler texto ---
    text_lines = read_text_file_lines("examples\legiao.txt")  # <-- seu arquivo aqui

    # --- Construir o corpus ---
    tokens, stems, word2idx, idx2word, encoded_lines = build_corpus_per_line(text_lines)

    # --- Fazer busca ---
    query_phrase = input("\nDigite a frase para buscar: ")

    # --- Escolher modo de busca ---
    mode = input("Modo de busca ('OR' ou 'AND'): ").strip().upper()
    if mode not in {"OR", "AND"}:
        mode = "OR"  # fallback padrão

    matches = search_by_phrase(query_phrase, word2idx, encoded_lines, idx2word, text_lines, mode=mode)

    # --- Mostrar resultados ---
    if matches:
        print(f"\nEncontrado {len(matches)} linha(s):")
        for line_num, line_text in matches:
            print(f"Linha {line_num}: {line_text}")
    else:
        print("Nenhum resultado encontrado.")

if __name__ == "__main__":
    main()
