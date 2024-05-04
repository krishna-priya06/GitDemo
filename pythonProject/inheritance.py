from PythonClasses import calculator, calculators


class childimpl(calculator):
    num2 =200
    def getCompleteData(self):
        return (calculator.num+self.summation()+childimpl.num2)
obj=childimpl(2,3)
print(obj.getCompleteData())

class childimpl1(calculators):
    num3=150
    def mergeallthedata(self,a,b):
        print("I am merging all the data from calculators class and childimpl1")
        return(self.num+self.num3+self.summation(a,b))
obj2=childimpl1()
print(obj2.mergeallthedata(2,3))

