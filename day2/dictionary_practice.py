#dictionary practice
student = { "name": "ayesha",
           "age": 20,
           "marks":86}
#print student name
print("name = ",student["name"])
#print student marks
print("marks = ",student["marks"])
#update marks 
student["marks"]= 90
#add a new key
student["grade"] = "A"
#print all keys and values using items()
for keys,values in student.items():
    print(keys," : ",values)
    
