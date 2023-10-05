import nltk
import numpy as np
from nltk import pos_tag, word_tokenize
from nltk.corpus import treebank
nltk.download('treebank')


def main():

    # 2.1
    tagged_sentences = treebank.tagged_sents()
    training_set = tagged_sentences[:3500]
    test_set = tagged_sentences[3500:]
    print("Number of training sentences: ", len(training_set))
    print("Number of test sentences: ", len(test_set), "\n")
    print("First sentence in test corpus: " + "\n" + str(test_set[0]) + "\n")

    # 2.2
    print("Tagging accuracies:\n-------------------")
    affix_tagger = nltk.AffixTagger(training_set)
    print("Affix tagger: ", round(affix_tagger.accuracy(test_set)*100, 2), "%")
    unigram_tagger = nltk.UnigramTagger(training_set)
    print("Unigram tagger: ", round(unigram_tagger.accuracy(test_set)*100, 2), "%")
    bigram_tagger = nltk.BigramTagger(training_set)
    print("Bigram tagger: ", round(bigram_tagger.accuracy(test_set)*100, 2), "%")
    trigram_tagger = nltk.TrigramTagger(training_set)
    print("Trigram tagger: ", round(trigram_tagger.accuracy(test_set)*100, 2), "%", "\n")
    # 2.3
    print("Tagging accuracies with backoff:\n--------------------------------")
    backoff_tagger = affix_tagger
    print("Affix tagger evaluation: ", round(backoff_tagger.accuracy(test_set)*100, 2), "%")
    backoff_tagger = nltk.UnigramTagger(training_set, backoff=backoff_tagger)
    print("Unigram tagger evaluation: ", round(backoff_tagger.accuracy(test_set)*100, 2), "%")
    backoff_tagger = nltk.BigramTagger(training_set, backoff=backoff_tagger)
    print("Bigram tagger evaluation: ", round(backoff_tagger.accuracy(test_set)*100, 2), "%")
    backoff_tagger = nltk.TrigramTagger(training_set, backoff=backoff_tagger)
    print("Trigram tagger evaluation: ", round(backoff_tagger.accuracy(test_set)*100, 2), "%", "\n")
    # 2.4
    # The reason for this is that the taggers without a backoff model are not able to tag words that are not in the
    # training set. This is because they do not have a fallback option. The backoff model is able to tag words that
    # are not in the training set because it has a fallback option. The backoff model is able to use the previous
    # tagger to tag words that are not in the training set. This is why the backoff model has a higher accuracy than
    # the taggers without a backoff model.
    # The reason why the BigramTagger without a backoff model has a lower accuracy than the corresponding tagger with
    # a backoff model is because the BigramTagger without a backoff model is not able to tag words that are not in the
    # training set.

    # 2.5: TODO: FINISH THIS

main()
