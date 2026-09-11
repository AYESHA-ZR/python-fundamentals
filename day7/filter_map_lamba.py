# Filter Marks
# without using fiter function
marks = [34,56,7,85,33,77,88,99,66,78,97,23]
print("marks = ",marks)
high_M = [num for num in marks if num>=70]
print("greater than 70 marks = ",high_M)
# filter +normal function

def check_condition(num):
    return num>=70

high_marks  =list(filter(check_condition,marks))
print("high marks = ",high_marks)

# filter + lamba

high_marks = list(filter(lambda num:num>=70,marks))
print("higher marks = ",high_marks)
# map
marks = [34,56,7,85,33,77,88,99,66,78,97,23]
def add_five(num):
    return num+5

new_list = list(map(add_five,marks))
print("new list = ",new_list)

# lamba
# lamba is one line function
New_list = list(map(lambda num:num+5,marks))
print("updated list",New_list)