#   *args
# *args  → multiple positional arguments
# inside fuction ...tuple
def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total = total+num
    
    return total

print(calculate_sum(3,56,65,7,9))
print(calculate_sum(3,5))

        