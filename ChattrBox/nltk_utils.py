import nltk
#nltk.download('punkt')

# Importing a stemmer
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Function to tokenize the sentence
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Function to implement the notion of stemming
def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    pass


words = ['organize', 'organizes', 'organizing']
stemmend_words = [stem(w) for w in words]
print(stemmend_words)