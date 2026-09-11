#Practice:

# Problem 1: Create a function that takes two numbers and returns their sum.

def add(a,b):
    return a+b

n1= int(input("enter first number :"))
n2 = int(input("enter second number :"))
print ("sum = ", add(n1,n2))

# Problem 2: Create a function that checks whether a number is even or odd.
def check(n):
    if n%2==0:
        print("even number")
    else:
        print("odd number")
        
num = int(input("enter a number = "))
check(num)

# Problem 3: Create a function that takes a string and returns the number of vowels.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

s = input("Enter a string: ")
print("Vowels =", count_vowels(s))