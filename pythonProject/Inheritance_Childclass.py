from OOPS_Concepts_Constructor import Calculator

class ChildImpl(Calculator):
    num2 =200
    def __init__(self,a,b):
        Calculator.__init__(self,a,b)
    def getChildData(self):
        return self.num2+Calculator.num+Calculator.summation(self)

obj =ChildImpl(2,3)
print(obj.getChildData())