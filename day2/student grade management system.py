#student grade managment system
student = {}
name = input("enter student name = ")
marks = list()
marks.append(int(input("enter python marks = ")))
marks.append(int(input("enter maths marks = ")))
marks.append(int(input("enter english marks")))

print("NAME = ",name)

#total marks
total = 0
for i in marks:
    total= total+i
print("TOTAL = ",total)

#average
avg =total/len(marks)
print("AVERAGE = ",avg)

#grade
if avg>=90:
    grade = "A+"
elif avg>=80:
    grade = "A"
elif avg>=70:
    grade = "B"
elif avg>=60:
    grade = "C"
else:
    grade = "D"
    
print("GRADE = ",grade)

student["name"] = name
student["marks"] = marks
student["total"] = total
student["average"] = avg
student["grade"] = grade
print("dictionary\n ",student)

