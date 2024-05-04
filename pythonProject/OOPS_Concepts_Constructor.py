class Calculator:
    num = 100

    def __init__(self,a,b):
        print ("Hi I am the default constructor") #defaultconstructor
        self.firstvariable = a
        self.secondvariable = b

    def getdata(self):
        print(" I am now executing as a method in class")

    def summation(self):
        return self.firstvariable + self.secondvariable

obj = Calculator(2,3)  # syntax to create object in class
print(obj.summation()) # calling summation method and printing the result
obj.getdata() #to run the getdata method in class i.e., calculator
print(obj.num)




