from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
sentence = "Thinking logically is basically good thing."
words = word_tokenize(sentence)
for word in words:
 stemmed_word = ps.stem(word)
 print(word, ":", stemmed_word)
