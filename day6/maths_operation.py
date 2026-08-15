# basic maths operations
def add(*numbers):
    total = 0
    for num in numbers:
        total+=num
    return total

def sub(*numbers):
    sub = numbers[0]
    for num in numbers[1:]:
        sub = sub-num
    return sub

def mul(*numbers):
    mul = 1
    for num in numbers:
        mul = mul*num
    return mul

# if __name__ == "__main__":
if __name__ == "__main__":
    print("Testing maths operations")
    print("Addition =", add(10, 5))
    print("Subtraction =", sub(10, 5))
    print("Multiplication =", mul(10, 5))