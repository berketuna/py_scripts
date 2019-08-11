def anti_vowel(text):
  text = str(text)
  for i in range(len(text)):
    if text[i] == "a" or text[i] == "A"or \
       text[i] == "e" or text[i] == "E" or \
       text[i] == "i" or text[i] == "I" or \
       text[i] == "o" or text[i] == "O" or \
       text[i] == "u" or text[i] == "U":
      text[i] = text.replace(text[i] , "")
  return text

txt = "Hey You!"
txt_new = anti_vowel(txt)
print txt_new
