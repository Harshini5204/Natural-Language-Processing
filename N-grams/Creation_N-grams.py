import nltk
def word_ngrams(text, n):
 words = text.split()
 ngrams = nltk.ngrams(words, n)
 return [" ".join(ngram) for ngram in ngrams]
def character_ngrams(text, n):
 ngrams = nltk.ngrams(text, n)
 return ["".join(ngram) for ngram in ngrams]
text = input("Enter the input sentence :")
word_bigrams = word_ngrams(text, 2)
print("The Word NGrams :",word_bigrams)
char_trigrams = character_ngrams(text, 3)
print("The character NGrams :",char_trigrams)

