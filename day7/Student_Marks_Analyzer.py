# student marks analyzer
marks = [34,90,78,67,89,91,98,87,54,23,45]
print("original marks = ",marks)
# 70+ marks
marks_above_70 = [num for num in marks if num>=70]
print("greater than 70 marks = ",marks_above_70)

# add 5 in each marks
updated_marks = list(map(lambda num:num+5,marks))
print("udated marks = ",updated_marks)

# greater than 90 using filter
marks_above_90 = list(filter(lambda num:num>=90,marks))
print("filtered marks (greater than 90) = ",marks_above_90)

# acsending marks
acs = sorted(marks)
print("ascending marks = ",acs)

# descending marks
dsc = sorted(marks,reverse=True)
print("descending marks  = ",dsc)

from functools import reduce
# total using reduce()
total = reduce(lambda a,b:a+b,marks)
print("total marks  = ",total)
avg = total/len(marks)
print("average marks = ",avg)