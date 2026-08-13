#dictionary practice deeply
student = {
    "name":"ayesha",
    "rollNo":24,
    "age": 22,
    "dep":"CS",
    "gpa":3.22
}
print(student.keys())
print(student.values())
print(student.items())
print("name ",student.get("name"))
print(student.get("email"))

# dictionary modification
student["gpa"] = 3.45
student["email"] = "ayesha@gmail.com"

student.pop("age")
print(student)
print("email exist = ","email" in student )
