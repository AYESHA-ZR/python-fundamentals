#small data processing project
#student marks analyzer
marks = [10,33,40,50,22,83,33,95,50,10,70,88,90]
print("marks = ",marks)
unique = set(marks)
print("unique marks = ",unique)

#max without using max function
highest = marks[0]
for i in marks:
    if i>highest:
        highest=i
print("maximum marks = ",highest)

#minimum without using min function
lowest = marks[0]
for i in marks:
    if i<lowest:
        lowest =i
print("minimum marks = ",lowest)

# highest marks
high_marks = [num for num in marks if num>=80]
print("highest marks = ",high_marks)

# average without using sum function
total = 0
for i in marks:
    total= total+i
    
avg = total/len(marks)
print("average = ",avg)

mark_dict = {}
mark_dict["Marks"] = marks
mark_dict["Unique"] =unique
mark_dict["MAX"] = highest
mark_dict["MIN"] = lowest
mark_dict["High_marks"] = high_marks
mark_dict["AVG"] = avg
print(" marks dictionary = ",mark_dict)
