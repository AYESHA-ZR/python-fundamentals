# Student CSV Analyzer
import csv

with open("student.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    marks =[]
    for row in reader:
        print(row[0],"..",row[3])
    
        M = int(row[3])
        if M>=80:
            print(row[0],"...",row[3])
        marks.append(M)
        
    # total marks
    from functools import reduce
    total = reduce(lambda a,b:a+b,marks)
    print("Total marks  = ",total)
    # average of marks
    avg = total/len(marks)
    print("average  = ",avg)
    
    # highest marks
    high_marks = max(marks)
    print("highest marks = ",high_marks)
    
    # sorting marks
    asc = sorted(marks)
    print("sorted marks = ", asc)
    
        
  
   