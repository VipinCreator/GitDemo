
class Student:
    id=1

    def __init__(self,name,age,a,b):
        self.name=name
        self.age=age
        self.a=a
        self.b=b



    def addStudent(self):
        print("Student added")
        print(self.a+self.b)

obj=Student("Vipin",23,2,6)
print(obj.name)
obj.addStudent()