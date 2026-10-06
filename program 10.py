word = input("enter a string")
first = word[0]
remaining = word[1:]

remaining = remaining.replace(first,'$')
result = first + remaining

print("result ",result)
