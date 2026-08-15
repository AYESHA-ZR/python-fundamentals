# json practice
student = {
    "name": "Ayesha",
    "age": 20,
    "department": "CS",
    "semester": 4,
    "gpa": 3.45
}
import json
with open("student.JSON","w") as file:
    json.dump(student,file,indent =4)

with open("student.JSON","r") as file:
    data  =json.load(file)
    print(data)

# json.dump() → Python → JSON file
# json.load() → JSON file → Python
