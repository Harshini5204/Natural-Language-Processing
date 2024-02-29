import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def pos_tagging(text):
 words = word_tokenize(text)
 pos_tags = nltk.pos_tag(words)
 return pos_tags
example_text = "Dark chocolate contains lots of antioxidants that help the cardiovascular system by reducing blood pressure." \
      "Dark chocolate has more cacao and less sugar than other chocolates."
pos_tags = pos_tagging(example_text)
for word, pos_tag in pos_tags:
 print(f"Word: {word}, POS Tag: {pos_tag}")

