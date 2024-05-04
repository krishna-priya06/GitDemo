class Calculator:
    num = 100

    def __init__(self):
        print("Hi I am the default constructor")  # defaultconstructor
        # self.firstvariable = a
        # self.secondvariable = b

    def getdata(self):
        print(" I am now executing as a method in class",self.firstvariable)

    def summation(self,a,b):
        self.firstvariable = a
        self.secondvariable = b
        return self.firstvariable + self.secondvariable

obj = Calculator()  # syntax to create object in class
print(obj.summation(8,3))
obj.getdata() #to run the getdata method in class i.e., calculator
print(obj.num)



