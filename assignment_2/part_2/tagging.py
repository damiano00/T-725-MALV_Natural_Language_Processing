import nltk
from nltk.corpus import treebank
nltk.download('treebank')

def main():

    tagged_sentences = treebank.tagged_sents()
    training_set = tagged_sentences[:3500]
    test_set = tagged_sentences[3500:]
    print("Training set count: ", len(training_set))
    print("Test set count: ", len(test_set))
    first_sentence = ""
    for word in training_set[0]:
        first_sentence += word[0] + " "
    print("First sentence in the training set: ", first_sentence)

    affix_tagger = nltk.AffixTagger(training_set)
    print("Affix tagger evaluation: ", affix_tagger.accuracy(test_set))
    unigram_tagger = nltk.UnigramTagger(training_set)
    print("Unigram tagger evaluation: ", unigram_tagger.accuracy(test_set))
    bigram_tagger = nltk.BigramTagger(training_set)
    print("Bigram tagger evaluation: ", bigram_tagger.accuracy(test_set))


main()
