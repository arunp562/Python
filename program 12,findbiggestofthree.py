a = int(input("enter first number :"))
b = int(input("enter first number :"))
c = int(input("enter first number :"))

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

print("biggest of three is :",biggest)
