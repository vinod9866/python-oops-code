class Person:
    age = 20
    def walk(self):
        print("person is walking")
    def read(self):
        print("Person is reading")
class Human:
    Dna = "X11355"
    def dna(self):
        print("Human DNA")
    def read(self):
        print("Human is reading")
    def write(self):
        print("Human is writing")
    
class Student(Person,Human):
    rno=15
    def write(self):
        print("Student is writing")
        
obj=Student()
obj.read()
obj.write()

