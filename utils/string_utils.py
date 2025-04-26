import unicodedata
import string

def remove_accents_and_punctuation(word):
    word = ''.join(
        char for char in unicodedata.normalize('NFD', word)
        if unicodedata.category(char) != 'Mn'
    )
    word = ''.join(char for char in word if char not in string.punctuation)
    return word

def tokenize(text, punctuation=string.punctuation, stop_words=None):
    text = text.lower()
    text = text.translate(str.maketrans('', '', punctuation))
    tokens = text.split()
    return [t for t in tokens if t not in stop_words]

def create_word_mappings(unique_stems):
    word2idx = {word: idx for idx, word in enumerate(unique_stems)}
    idx2word = {idx: word for word, idx in word2idx.items()}
    return word2idx, idx2word

def encode_words(words, word2idx):
    return [word2idx[word] for word in words]

def decode_indices(indices, idx2word):
    return [idx2word[idx] for idx in indices]
