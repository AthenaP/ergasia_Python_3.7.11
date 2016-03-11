import nltk

from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet

sentence1 = raw_input('Give first phrase')
sentence2 = raw_input('Give second phrase')

wordstagged1 = pos_tag(word_tokenize(sentence1))
wordstagged2 = pos_tag(word_tokenize(sentence2))

nounsandverbs1 = [word for word,pos in wordstagged1 \
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos == 'VB' or pos == 'VBZ')]
print nounsandverbs1


nounsandverbs2 = [word for word,pos in wordstagged2 \
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos == 'VB' or pos == 'VBZ')]
print nounsandverbs2

list = []

for word1 in nounsandverbs1:
    for word2 in nounsandverbs2:
        wordFromList1 = wordnet.synsets(word1)
        wordFromList2 = wordnet.synsets(word2)
        if wordFromList1 and wordFromList2:
            s = wordFromList1[0].wup_similarity(wordFromList2[0])
            list.append(s)

print(max(list))
