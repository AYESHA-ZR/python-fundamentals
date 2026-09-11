# calculaltor function
def calculator(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    try:
        div= a/b
    except ZeroDivisionError:
        div = "can't divide by zero...."
    
    return add,sub,mul,div

num1 = int(input("enter fisrt number = "))
num2  = int(input("enter second number = "))
add, sub, mul, div = calculator(num1, num2)

print("Addition =", add)
print("Subtraction =", sub)
print("Multiplication =", mul)
print("Division =", div)