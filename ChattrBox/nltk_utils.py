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

# Function to return a bag of words array
def bag_of_words(tokenized_sentence, all_words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence] # Stemming the words in the tokenized sentence
    bag = np.zeros(len(all_words), dtype=np.float32) # Creating a bag and initializing 0 for each word
    # Iterating through all the words
    for idx, w in enumerate(all_words):
        # Iterating through each of the word in the tokenized sentence
        if w in tokenized_sentence:
            bag[idx] = 1.0 # Assigning 1 to the word that contains in the tokenized sentence

    return bag


sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bag = bag_of_words(sentence, words)
print(bag)