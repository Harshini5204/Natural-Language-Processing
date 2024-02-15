import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens
sample_input=[("Data alchemist sculpting insights from the digital ether"),
              ("Crafting algorithms, one byte at a time"),
              ("AI enthusiast on a mission.")]
for text in sample_input:
    print("orginal text:",text)
    word_tokens=tokenize_text(text)
    print(word_tokens)
