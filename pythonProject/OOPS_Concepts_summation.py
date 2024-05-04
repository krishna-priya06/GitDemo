class Calculator:
    num = 100

    def __init__(self):
        print ("Hi I am the default constructor") #defaultconstructor


    def getdata(self):
        print(" I am now executing as a method in class")

    def summation(self,a,b):
        self.firstvariable = a
        self.secondvariable = b
        c = self.firstvariable + self.secondvariable
        print (" the sum is",c)

obj = Calculator()  # syntax to create object in class
obj.summation(8,3)
obj.getdata() #to run the getdata method in class i.e., calculator
print(obj.num)



