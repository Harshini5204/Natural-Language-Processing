import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
data="This is a program"
stopword=set(stopwords.words('english'))
words=word_tokenize(data.lower())
words_filtered=[]
for w in words:
    if w not in stopword:
        words_filtered.append(w)
        print("Original Words:\n", words)
        print("Stopwords:\n", stopword)
        print("Filtered Words:\n", words_filtered) 
