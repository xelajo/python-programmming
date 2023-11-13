c_yr = int(input("Enter the current year: "))
f_yr = int(input("Enter the final year: "))
print("The leap years are:")
for i in range (c_yr,f_yr+1):
    if (i%4==0) and (i%100!=0) or (i%400==0):
        print(i)