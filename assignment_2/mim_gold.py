
"""
In this part, you use Python and NLTK to process a Part-of-Speech tagged Icelandic corpus, the Icelandic Gold
Standard; MIM-GOLD1. A preprocessed version of MIM-GOLD containing one sentence per line (with “/” between
tokens and tags) is available as the file MIM-GOLD.sent in the zip file linked the assignment description.2
This part is divided into the subparts described below, but you should return a single Python program,
mim_gold.py, which includes all the code needed for carrying out these tasks.

1.Read in MIM-GOLD using the class TaggedCorpusReader, display the number of sentences, and display the individual
tokens of sentence n 100.
2. Display the number of tokens and the number of types in MIM-GOLD.
3. Display the 10 most frequent tokens in MIM-GOLD using the class FreqDist.
4. Display the 20 most frequent tags in MIM-GOLD using the class FreqDist.
5. Generate tag bigrams and use the class ConditionalFreqDist to print out the 10 most frequent tags that can
follow the tag ’af’ (this tag denotes a preposition).
"""
from nltk import ConditionalFreqDist
from nltk.corpus.reader import TaggedCorpusReader


def main():
    corpus_root = './MIM-GOLD.sent'
    TaggedCorpusReader(corpus_root, '.*').words()
    print("Number of sentences: ", len(TaggedCorpusReader(corpus_root, '.*').sents()))
    print("Tokens of sentence 100: ", TaggedCorpusReader(corpus_root, '.*').sents()[100])
    print("Number of tokens: ", len(TaggedCorpusReader(corpus_root, '.*').words()))
    print("Number of types: ", len(set(TaggedCorpusReader(corpus_root, '.*').words())))
    print("10 most frequent tokens: ", TaggedCorpusReader(corpus_root, '.*').words())
    print("20 most frequent tags: ", TaggedCorpusReader(corpus_root, '.*').tagged_words())

