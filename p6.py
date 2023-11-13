list1 = [1, 2, 45, 78, 98]
list2 = [3, 6, 87, 9, 12, 5]
print("list1 : ", list1)
print("list2 : ", list2)

print("Length of list1 = ", len(list1))
print("Length of list2 = ", len(list2))

#a
if len(list1) == len(list2):
    print("Length of list are same")
else:
    print("Not same length")

#b
print("Sum of list1 = ", sum(list1))
print("Sum of list2 = ", sum(list2))

if sum(list1) == sum(list2):
    print("Sum of two lists are same")
else:
    print("Sum of list not same")

#c
check = any(item in list1 for item in list2)
print("Any value occur in both : ", check)