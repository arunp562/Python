word = input("enter a word ")
if len(word) >= 3:
    if word.endswith("ing"):
        word = word + "ly"

    else:
        word = word + "ing"

print("new word ",word)
