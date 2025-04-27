import sys
import os
import re
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stemmer_pt_br import stemmer_pt_br
from utils.string_utils import tokenize, create_word_mappings, encode_words, decode_indices

import numpy as np
from numpy.linalg import norm
from collections import Counter

def word_to_char_vector(word, alphabet):
    counter = Counter(word)
    return np.array([counter.get(c, 0) for c in alphabet])


def cosine_similarity(v1, v2):
    if norm(v1) == 0 or norm(v2) == 0:
        return 0.0
    return np.dot(v1, v2) / (norm(v1) * norm(v2))


alphabet = list("abcdefghijklmnopqrstuvwxyzáàãâéêíóôõúç")

# Suas palavras stemmizadas
stems = ['cant', 'canta', 'corre', 'correr', 'abr', 'abri']

# Criar vetor para cada palavra
vectors = {word: word_to_char_vector(word, alphabet) for word in stems}

query_word = "cantar"
query_stem = stemmer_pt_br(query_word)  # aplica seu stemmer

query_vector = word_to_char_vector(query_stem, alphabet)

# Similaridade
# Comparar "cantar" com todos os registro, uma busca não otimizada
similarities = []
for word, vec in vectors.items():
    score = cosine_similarity(query_vector, vec)
    similarities.append((word, score))

# Ordenar por mais parecido
similarities.sort(key=lambda x: -x[1])

for word, score in similarities:
    print(f"{word} ({score:.2f})")
