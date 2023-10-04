from nltk import ConditionalFreqDist, bigrams
from nltk.corpus.reader import TaggedCorpusReader
from nltk.probability import FreqDist


def main():
    mim_gold = TaggedCorpusReader("./", "MIM-GOLD.sent")

    print("\nNumber of sentences: ", len(mim_gold.sents()))

    print("Sentence no. 100:")
    sent_100 = ""
    sentence = mim_gold.sents()[99]
    for words in sentence:
        sent_100 += words + " "
    print(sent_100)

    print("\nNumber of tokens: ", len(mim_gold.words()))

    print("Number of types:", len(set(mim_gold.words())), "\n")

    print("The 10 most frequent tokens:")
    most_common_10 = FreqDist(mim_gold.words()).most_common(10)
    for token in most_common_10:
        print(token[0], "=>", token[1])

    print("\nThe 20 most frequent PoS tags:")
    pos_tag_freq = FreqDist(tag for word, tag in mim_gold.tagged_words())
    for tag, count in pos_tag_freq.most_common(20):
        print(f"{tag} => {count}")

    print("\nThe 10 most frequent tags that can follow the tag ’af’:")
    types = []
    for sentence in mim_gold.tagged_sents():
        for word in sentence:
            types.append(word[1])
    tag_bigrams = bigrams(types)
    cfd = ConditionalFreqDist(tag_bigrams)
    tags_following_af = cfd['AF'].most_common(10)
    for tag in tags_following_af:
        print(tag[0], "=>", tag[1])


main()
