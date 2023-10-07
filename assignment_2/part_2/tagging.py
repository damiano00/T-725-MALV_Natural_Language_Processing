import nltk
from nltk.corpus import treebank

nltk.download('treebank')

taggers = [nltk.AffixTagger, nltk.UnigramTagger, nltk.BigramTagger, nltk.TrigramTagger]
tagged_sentences = treebank.tagged_sents()
training_set = tagged_sentences[:3500]
test_set = tagged_sentences[3500:]


def run_tagger(tagger, train_set, testing_set, backoff_tagger=None):
    """
    This function trains a tagger on the training set and evaluates it on the test set
    :param tagger: tagger from nltk to be used to tag the sentences
    :param train_set: the training set to train the tagger on
    :param testing_set: the test set to evaluate the tagger on
    :param backoff_tagger: the tagger to be used as backoff, if None, no backoff is used
    :return: the trained tagger
    """
    tagger = tagger(train_set, backoff=backoff_tagger)
    print(tagger.__class__.__name__ +" evaluation:", round(tagger.accuracy(testing_set) * 100, 2), "%")
    return tagger


def evaluate(results, expected):
    """
    For each sentence in the test set, this function compares the results of the default tagger with the expected
    :param results: The results of the default tagger
    :param expected: The expected results
    :return: The accuracy of the default tagger
    """
    correct = 0
    total = 0
    for i in range(len(results)):
        for j in range(len(results[i])):
            if results[i][j][1] == expected[i][j][1]:
                correct += 1
            total += 1
    return correct / total


def main():
    # 2.1
    print("Number of training sentences: ", len(training_set))
    print("Number of test sentences: ", len(test_set), "\n")
    print("First sentence in test corpus: " + "\n" + str(test_set[0]) + "\n")

    # 2.2
    print("Tagging accuracies:\n-------------------")
    for tagger in taggers:
        run_tagger(tagger, training_set, test_set)

    # 2.3
    print("\nTagging accuracies with backoff:\n--------------------------------")
    curr_tagger = None
    for tagger in taggers:
        curr_tagger = run_tagger(tagger, training_set, test_set, curr_tagger)

    # 2.4 --> read report

    # 2.5
    sentences_to_tag = []
    for sentence in test_set:
        words_in_sentence = [word_info[0] for word_info in sentence]
        sentences_to_tag.append(words_in_sentence)
    default_tagger_results = nltk.pos_tag_sents(sentences_to_tag)
    print("\nAccuracy of the default tagger in NLTK: ", round(evaluate(default_tagger_results, test_set) * 100, 2), "%")


main()
