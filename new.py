class Person:
    def SetValue(self,name,age=23):#default argument age=23
        self.name = name
        self.age = age
    def GetValue(self):
        print(self.name,self.age)

name = input()
age = int(input())
p1 =  Person()
p1.SetValue(name,age)
p1.GetValue()

''' here see name and age are properties and we definitelu
    give it for every object, so here creating a 
    function for setting properties to the object is
    kind of double work thats why we came up with

    setting properties at the same time of
     creating or initilizing an object is called 
     constructer
'''

class Person:
    city ="Hyd"
    def __init__(self,name,age=25): #constructor
        self.name = name
        self.age = age #here if we pass age = 20 all objects will have age=20
    def GetValue(self):
        print(self.name,self.age)

name = input()
age = int(input())
p1 =  Person(name)#here hidden self object instance also be sent along with name argument #here we r not passing age so defaultlu age=25 from constructor
p1.GetValue()

'''constructor
        default: only self
        parameterized : arguments along with self
        starts with __ and ends with __ methods called dunder methods or function
'''

'''
    properties or attributes or data-members all same
    Attributes -> instance attributes -> object attributes -> diff for every object eg age=20 for ob1 and age=30 for obj2..
               -> class attributes -> class -> same for all objs's

    class attributes can be accessed by with
        -> Person.city or self.city
'''
#ex-1
class Dude:
    def setting(self):
        self.age=30
    def getting(self):
        print(self.age)
p1 = Dude()
p1.setting() # 
p1.getting() # will work
p2 = Dude()
p2.getting() # it wont work because no age initialization

#ex-2
class Car:
    def __init__(self):
        self.name = "serif"
        self.speed = 150
c1 = Car() #at this moment name=serif and speed=150
c1.name = "vinod" #from now name=vinod age=200
c1.speed = 200
print(c1.name,c1.speed)
