names = ["anu","arun","ravi","asha"]
count = 0
for name in names:
    for ch in name:
        if ch == 'a' or ch == 'A':
            count += 1
print("number of a :",count)
