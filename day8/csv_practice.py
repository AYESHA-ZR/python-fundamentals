import csv
# read csv file
with open("student.csv","r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        
        print(row)

# access specific file of csv
with open("student.csv","r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row[0],"...",row[2])
        
# csv filtering
# students data for marks greater than 80 
with open("student.csv","r") as file:
    reader = csv.reader(file)
    next(reader)  #header skip
    for row in reader:
        marks = int(row[2])
        
        if marks>=80:
            print(row[0],"....",row[2])

# CSV data analysis
from functools import reduce
with open("student.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    marks = []
    for row in reader:
        marks.append(int(row[2]))
        
    total = reduce(lambda a,b:a+b,marks)
        
    avg = total/len(marks)
    print("total = ",total)
    print("average  = ",avg)
    
# write in csv file
students = [
    ["name","age","dep","marks"],
    ["ayesha",22,"cs",78],
    ["maria",23,"physics",67],
    ["mahnoor",24,"cs",89]
]
with open("student.csv","w",newline="") as file:
    writer  = csv.writer(file)
    writer.writerows(students)
#     writer.writerow()  → ek row
# writer.writerows() → multiple rows