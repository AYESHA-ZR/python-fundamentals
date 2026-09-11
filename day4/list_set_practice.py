#List Manipulation
numbers = [10, 20, 30, 40, 50]
print(numbers)
# Add 60 to the end.
numbers.append(60)
# Add 5 at index 0.
numbers.insert(0,5)
# Remove 30.
numbers.remove(30)
# Remove the last element.
numbers.pop()
# Sort the list.
numbers.sort()
# Print the final list.
print("final list  = ",numbers)
# Print the length of the list.
print("length of the list = ",len(numbers))

#Write a program that finds the duplicate numbers.
numbers = [10,20,20,30,40,30,50,60,77,50]
duplicates =[]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
    else:
        duplicates.append(num)
print("duplicated values :", duplicates)
print("unique values :",unique)

#set
# remove duplication using set
numbers = [10,20,30,10,20,50,60]
print(numbers)
unique = set(numbers)
unique_list  = list(unique)
print(unique_list)

#Set Operations
# 1.union
a = {2,3,4,5,8}
b = {9,8,7,6,5}
union = a|b
print("union",union)
# 2.intersection
inter = a & b
print("intersection = ",inter)
# a-b
sub = a-b
print("a-b = ",sub)

