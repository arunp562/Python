list1 = list(map(int, input("enter first list ; ").split()))
list2 = list(map(int, input("enter first list ; ").split()))

if len(list1) == len(list2):
    print("lists have same length")
else:
    print("lists have different lenght")

sum1 = sum(list1)
sum2 = sum(list2)

if sum1 == sum2:
    print("same sum")
else:
    print("have different sum")

if any(value in list2 for value in list1):
    print("have values common")
else:
    print("no values common")


