# error handling
# try/except
try:
    age = int(input("Enter your age = "))
    print("age = ",age)
except ValueError:
    print("enter a valid number.")
    
# Create a program that asks the user for two numbers and divides them.

# Take two inputs.
# Convert them to integers.
# Divide the first by the second.
# Handle invalid input using try/except.
# Also handle division by zero.

num1 = int(input("enter first number = "))
num2 = int(input("enter second number = "))
try:
    num1 = int(input("enter first number = "))
    num2 = int(input("enter second number = "))

    div = num1/num2
    print(num1," / ",num2," = ",div)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("cannot divided by zero.")
    
# Ask the user for a number. If they enter something invalid, don't crash—ask again.
while True:
    try:
        num = int(input("Enter a number = "))
        print("you entered = ",num)
        break
    except ValueError:
        print("invalid input ...try again....")
        