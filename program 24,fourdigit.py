start = int(input("enter starting numbers :"))
end = int(input("enter ending numbers: "))

for n in range(start, end + 1):
    if 1000 <= n <= 9999:
        s = str(n)

        if all(int(d) % 2 == 0 for d in s):
            root = int(n ** 0.5)

            if root * root == n:
                print(n)
