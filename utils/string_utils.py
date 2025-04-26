import unicodedata
import string

def remove_accents_and_punctuation(word):
    word = ''.join(
        char for char in unicodedata.normalize('NFD', word)
        if unicodedata.category(char) != 'Mn'
    )
    word = ''.join(char for char in word if char not in string.punctuation)
    return word