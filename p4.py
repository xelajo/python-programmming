n = int(input("Enter the numbers of values: "))
a = []
for i in range (0, n):
    c = int(input("Enter the value: "))
    if c >100:
        a.append("over")
    else:
        a.append(c)
print(a)