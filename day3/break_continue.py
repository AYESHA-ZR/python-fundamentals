
# Write a program that keeps asking the user to enter numbers.

# If the user enters a positive number, print it.
# If the user enters 0, stop the loop.
# You can assume the user won't enter negative numbers.

while True:
    num = int(input("enter a number = "))
    if num==0:
        break
    print(num)
    
# Write a program that prints numbers from 1 to 10, but skips even numbers.
#using for loop
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
# using while loop
i = 1
while i<11:
    if i%2==0:
        i = i+1
        continue
    print(i)
    i =i+1