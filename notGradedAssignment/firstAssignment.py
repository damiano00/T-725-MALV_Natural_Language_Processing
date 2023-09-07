import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')

file_path = 'shakes.txt'

# How many times does the word ‘Macbeth’ appear in Shakespeare's works?

with open(file_path, 'r') as file:
    text = file.read()
    words = word_tokenize(text)
    target_word = 'Macbeth'
    word_count = words.count(target_word)
    print(f"1) The word '{target_word}' appears {word_count} times in the text.")

# Normalize all contractions in the following string: It’s true that he doesn’t know I’ve arrived

contractions_dict = {
    "it's": "it is",
    "doesn't": "does not",
    "I've": "I have"
}
input_phrase = "It’s true that he doesn’t know I’ve arrived"
for contraction, expanded_form in contractions_dict.items():
    input_phrase = input_phrase.replace(contraction, expanded_form)
print("2) Normalized phrase:", input_phrase)

# Stem all words in Shakespeare ending in -ed
with open(file_path, 'r') as file:
    text = file.read()

words = word_tokenize(text)
porter_stemmer = PorterStemmer()
stemmed_words = []
for word in words:
    if word.endswith("ed"):
        stemmed_words.append(porter_stemmer.stem(word))
    else:
        stemmed_words.append(word)
# stemmed_words = [porter_stemmer.stem(word) if word.endswith("ed") else word for word in words]
stemmed_text = ' '.join(stemmed_words)
with open('shakes_stemmed.txt', 'w') as file:
    file.write(stemmed_text)
print('3) done on stemmed_text.txt')
