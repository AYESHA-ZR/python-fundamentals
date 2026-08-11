#list practice

#find the largest number
numbers = [23,34,23,78,36,67,11,90]
# print("largest number =",max(numbers))
largest = numbers[0]
for i in numbers:
    if i>largest:
        largest = i
        
print("largest number is", largest)

#find the sum
# print('sum of numbers is ',sum(numbers))
total = 0
for i in numbers:
    total= total +i
print("sum = ", total)

#count even numbers
even_count= 0
for i in numbers:
    if i%2==0:
        even_count+=1
print("total even numbers is ",even_count)

