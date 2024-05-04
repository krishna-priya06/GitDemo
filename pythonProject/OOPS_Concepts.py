class Calculator:
    num = 100

    def __init__(self):
        print ("Hi I am the default constructor")

    def getdata(self):
        print(" I am now executing as a method in class")


obj = Calculator()  # syntax to create object in class
obj.getdata() #to run the getdata method in class i.e., calculator
print(obj.num)



