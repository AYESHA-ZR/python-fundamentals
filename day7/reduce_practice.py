# reduce() practice
numbers = [45,67,45,23]
from functools import reduce

def add(a,b):
    return a+b
total =reduce(add,numbers)
print(total)

# use lamba
total = reduce(lambda a,b:a+b,numbers)
print(total)
