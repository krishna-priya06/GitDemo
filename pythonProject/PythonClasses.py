class calculator():
    num=100 #class variables_these are static in the class
    def __init__(self,a,b):
        print("now I am executed automatically upon object creation for the class")
        self.firstnumber =a
        self.secondnumber = b
    def getData(self):
        print("I am now executing as a method in calculator class")

    def summation(self):
        return(self.firstnumber+self.secondnumber)
    def multiplication(self):
        return(self.firstnumber*self.secondnumber)
obj=calculator(2,3)
obj.getData()
print(obj.num)
print(obj.summation())
print(obj.multiplication())

obj1=calculator(4,5)
obj1.getData()
print(obj1.num)
print(obj1.summation())
print(obj1.multiplication())

class calculators():
    num=100 #class variables_these are static in the class
    # def __init__(self,a,b):
    #     print("now I am executed automatically upon object creation for the class")
    #     self.firstnumber =a
    #     self.secondnumber = b
    def getData(self):
        print("I am now executing as a method in calculator class")

    def summation(self,a,b):
        return(a+b)
    def multiplication(self,c,d):
        return(c*d)
obj=calculators()
obj.getData()
print(obj.num)
print(obj.summation(2,3))
print(obj.multiplication(4,5))

obj1=calculators()
obj1.getData()
print(obj1.num)
print(obj1.summation(5,6))
print(obj1.multiplication(9,8))
print (calculator.num)

