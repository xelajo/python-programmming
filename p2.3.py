V = ['A','a','E','e','I','i','O','o','U','u']
word = input("Enter the word: ")
s = [i for i in word if i in V]
u = [i for i in word if i not in V]
print("Vowels: ",s)
print("Consonants: ",u)



