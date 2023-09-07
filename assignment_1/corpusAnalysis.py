import nltk
import sys

from nltk import word_tokenize
from nltk.corpus import gutenberg

nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

with open("output.txt", "w") as f:
    # Read the text file
    text_file_name = sys.argv[1]
    print("Text: " + text_file_name)
    f.write("Text: " + text_file_name + "\n")
    corpus = gutenberg.words(sys.argv[1])

    # Tokenize the text
    tokens = word_tokenize(' '.join(corpus))
    print("Tokens: " + str(len(tokens)))
    f.write("Tokens: " + str(len(tokens)) + "\n")

    # Get the types
    types = set(tokens)
    print("Types: " + str(len(types)))
    f.write("Types: " + str(len(types)) + "\n")

    # Get the types excluding stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    types_excluding_stop_words = types - stop_words
    print("Types excluding stop words: " + str(len(types_excluding_stop_words)))
    f.write("Types excluding stop words: " + str(len(types_excluding_stop_words)) + "\n")

    # Get the 10 most common tokens
    fdist = nltk.FreqDist(tokens)
    print("10 most common tokens: " + str(fdist.most_common(10)))
    f.write("10 most common tokens: " + str(fdist.most_common(10)) + "\n")

    # Get the long types
    long_types = [word for word in types if len(word) > 13]
    print("Long types: " + str(long_types))
    f.write("Long types: " + str(long_types) + "\n")

    # Get the nouns ending in 'ation'
    nouns_ending_in_ation = [word for word in types if word.endswith('ation')]
    print("Nouns ending in 'ation': " + str(nouns_ending_in_ation))
    f.write("Nouns ending in 'ation': " + str(nouns_ending_in_ation) + "\n")
