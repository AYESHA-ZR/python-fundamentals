numbers = [1,2,3,4,5,6]
print("orignal list = ",numbers)
# . A list containing the squares
squares = [num**2 for num in numbers]
print("squares = ",squares)
# A list containing only even numbers
even = [num for num in numbers if num%2==0]
print("even = ",even)