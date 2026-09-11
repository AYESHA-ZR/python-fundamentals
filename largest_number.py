#largest of three nunmber
num1 = int(input("enter firstnumber: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
if num1>=num2 and num1>=num3:
    print(num1," is a largest number")
elif num2>=num1 and num2>=num3:
    print(num2," is a largest number")
else:
    print(num3," is a largest number")
    
