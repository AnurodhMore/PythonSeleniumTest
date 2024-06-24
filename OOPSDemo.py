# class is a user-defined blueprint or prototype
# methods, class cariables, instance variables, constructor, etc

class Calculator:
    num = 100  # class  variable -> define e=immediately inside class

    def __init__(self,a,b):                   #Default Construtor Instancee variable -> defined inside constructor
        self.firstno = a  #store in instance variable firstno
        self.secondno = b  #store in instance variable secondno
        print("Called as soon as new object is created")

    def getData(self):          #  function used in class is called method
        print("Execute as a method in class")

    def summation(self):
        return self.firstno+self.secondno+Calculator.num


obj = Calculator(2,3)   # obj is an instance variable
obj.getData()
print(obj.summation())

obj1 = Calculator(4,7)   # obj is an instance variable
obj1.getData()
print(obj1.summation())













