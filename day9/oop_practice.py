# oop practice
class Student:
    university = "National University of Pakistan"
    def study(self):
        print(self.name ," is studying normally..")
    def __init__(self,name,age,department,marks): # this is constructor
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks
        
    def display_info(self):    #self current object ko refer krta hyy..
        print(self.university)
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("department = ",self.department)
        print("marks = ",self.marks)
        
    def check_result(self):
        if self.marks>=50:
            print(self.name," = Pass")
        else:
            print(self.name," = fail")
            
class Graduated_student(Student):
    pass
    def study(self):
        print(self.name," is studying at an advanced level...")
    def graduated(self):
        print("student are graduated..")
   
# comon function
def show_study(student):
    student.study()
    
student1 = Graduated_student("Ayesha", 23, "CS", 89)
show_study(student1)
student1.display_info()  # parent method
student1.check_result()  # parent method
student1.graduated()  # child method
print("\n\n")

Student2 = Student("maria",22,"physics",78)
show_study(Student2) 
Student2.display_info()  # parent method
Student2.check_result()  # parent method
print()

