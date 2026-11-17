numbers = list(map(int, input("enter numbers :").split()))
               
odd = []

for x in numbers:
    if x % 2 != 0:
        odd.append(x)

print("list after removing even numbers :",odd)
