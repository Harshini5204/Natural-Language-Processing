import re
def detect_word_pattern(p,t):
  matches=re.findall(p,t)
  if(matches):
    print("word pattern detected")
    for i in matches:
      print(i)
  else:
    print("no word pattern detected")
    sample_inputs=[("[0-9]+","I have 99999 chocolates"),
                   ('[a-z A-Z]+','Chocolates'),
                   ('[A-Z][a-z]+','harshini'),
                   ('[aeiouAEIOU]+','Handkerchief'),
                   ('[0-9]{2}-[0-9]{2}-[0-9]{4}','05-02-2004'),
                   ('[a-z 0-9]+@[a-z]+.com','bharshini2004@gmail.com')]
    for p,t in sample_inputs:
      print("pattern:",p)
      print("text:",t)
      detect_word_pattern(p,t)
      print()

