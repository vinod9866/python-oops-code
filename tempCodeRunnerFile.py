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