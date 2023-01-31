import nltk
import numpy as np
#nltk.download('punkt')

# Importing a stemmer
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Function to tokenize the sentence
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Function to implement the notion of stemming
def stem(word):
    """words = ['organize', 'organizes', 'organizing']
    stemmend_words = [stem(w) for w in words]
    print(stemmend_words)"""
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag
