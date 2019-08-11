def reverse(text):
    rev_str = ""
    for i in range(len(text)):
        rev_str += text[-1-i]
    return rev_str

while True:
    word = raw_input("Enter a word: ")
    if word == "exit":
        break
    reversed = reverse(word)
    print reversed
