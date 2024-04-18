import string
import random
from nltk.corpus import brown


# nltk.download()


# 1-Apply data preprocessing:
def dataPreprocessing(corpus):
    preprocessingData = []
    for sentence in corpus:
        # Tokenize sentences into words (Word Tokenization)
        # tokens = nltk.word_tokenize(sentence)

        # Remove punctuation marks from sentence
        sentence = [word.translate(str.maketrans('', '', string.punctuation)) for word in sentence]

        # Convert all words to lowercase.
        sentence = [word.lower() for word in sentence]

        preprocessingData.append(sentence)
    return preprocessingData


# 2-Build N-gram model:
def n_gramModel(sentences, n):
    ngram_model = {}
    for sentence in sentences:
        ngrams_list = [(sentence[i:i + n]) for i in range(len(sentence) - n + 1)]
        for ngram in ngrams_list:
            context = tuple(ngram[:-1])
            word = ngram[-1]
            if context in ngram_model:
                ngram_model[context].append(word)
            else:
                ngram_model[context] = [word]
    return ngram_model


# 3-Sentence Generator:
def sentenceGenerator(ngram_model, n, max_len):
    sentence = random.choice(list(ngram_model.keys()))
    while len(sentence) < max_len:
        context = tuple(sentence[-(n - 1):])
        if context in ngram_model:
            next_word = random.choice(ngram_model[context])
            sentence += (next_word,)
        else:
            break
    generated_sentence = ' '.join(sentence)
    return generated_sentence


m = int(input("Enter Number of sentences to be generated: "))
n = int(input("Enter 2 for bigram – 3 for trigram: "))
maxLen = int(input("Enter Max number of words in sentence generated : "))
corpus = brown.sents()

dataPreprocessing = dataPreprocessing(corpus)

n_gramModel = n_gramModel(dataPreprocessing, n)

# Output
for i in range(m):
    print(f"Sentence {i + 1}: {sentenceGenerator(n_gramModel, n, maxLen)}")
    sentence = sentenceGenerator(n_gramModel, n, maxLen)