#file handling
# Common modes
# Mode	Meaning
# "r"	Read
# "w"	Write — replaces existing content
# "a"	Append
# "x"	Create new file

# write in file
with open("student.txt","w") as file:
    file.write("name: AYESHA\n")
    file.write("Department: CS\n")
    file.write("Goal: ML Engineer\n")
  
# read in file

with open("student.txt","r") as file:
    data = file.read()
    print(data)
    
# append to the file

with open("student.txt","a") as file:
    file.write("semester: 4\n")
    
# read file line by line
with open("student.txt","r") as file:
    for line in file:
        print(line.strip())  # strip removes the extra whitespace/newline around the line

