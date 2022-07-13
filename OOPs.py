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
    country = "GMD"
    __hello="vinod"
    # @with anythings is called decorator
    #static method doesn't have access to cls or obj variables
    #Static method knows nothing about the class and just deals with the parameters.
    @staticmethod 
    def Hello():
        print("hello")
    @classmethod
    def Myclass(cls,speed):
        print(cls.__hello)
        cls.__hello=speed
    def __init__(self):
        self.name = "serif"
        self.speed = 150
    def get(self):
        Car.Myclass(self.speed)
        return self.__hello
c1 = Car() #at this moment name=serif and speed=150
c1.name = "vinod" #from now name=vinod age=200
c1.speed = 200
print(c1.name,c1.speed)

'''types of methods:
    class-> Class method-> Used to access or modify the class state. 
            In method implementation,if we use only class variables,
            
            Static methods-> behaviour wont change irrespective of object calling

    object->instance methods->behaviour changes based on the object calling it
note: function which has 'self' they all are instance methods
'''
c1.Hello()

'''Access Modifiers - restrictions on visibility of attributes and methods
python - by default - no restrictions
    public - no restrictions -> without any - a=20
    private - full restrictions -> __a=20 (double underscore)
    protected - partial restrctions -> _a=20 (single underscore)

                within samecls  outsideofcls within derivedcls
    public          yes             yes         yes
    protected       yes             no          yes
    private         yes             no          no
'''
#Car.Myclass(333)
c1.Myclass(33333333)
print(c1.get())

#ex for class method returning object in final
from datetime import date
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student('Jessa', 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()

'''Inheritence
1.single level: parent to chlid syntx: class child(parent)
2.multiple: 2 or more parents to child syntx: class child(p1,p2)
3.multi level: a to b to c
4.hierarchical: parent to child1 and child2...
5.hybrid level: combination of above any two

'''

