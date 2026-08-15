# student record manger
student = {}
student["Name"] = input("Enter your name = ")
while True:
    try:
         student["Age"] =int(input("Enter your age = "))
         break
    except ValueError:
        print("invalid input.....try again.")

import json
student["department"] = input("Enter your department = ")
while True:
    try:
        student["GPA"] = float(input("Enter your GPA = "))
        break
    except ValueError:
        print("Invalid GPA... try again.")

with open("student_record.json","w") as file:
    json.dump(student,file,indent =4)

with open("student_record.json","r") as file:
    data = json.load(file)
    print(data)