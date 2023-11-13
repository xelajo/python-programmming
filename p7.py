s1 = str(input("Enter a string : "))
fChar = s1[0]
s1 = s1.replace(fChar, '$')
s1 = fChar + s1[1:]
print(s1)