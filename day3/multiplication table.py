#multiplication table
# Write a program that asks the user for a number and prints its multiplication table from 1 to 10.
n = int(input("enter number = "))
i = 1
print("TABLE OF ",n)
while i<11:
    print (n," X ",i," = ",n*i)
    i+=1
    