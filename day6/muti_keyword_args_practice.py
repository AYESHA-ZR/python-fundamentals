# **kwargs → multiple keyword arguments
# inside function ....dictionary
def student_info(**details):
    for keys, values in details.items():
        print(keys," : ",values)
    
student_info(Name =" Ayesha",age=20,Department="CS",GPA=3.45)