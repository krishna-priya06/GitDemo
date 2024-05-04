from PythonClasses import calculator


class childclassy(calculator):
    x=500
    def __init__(self,a,b):
        calculator.__init__(self,a,b)
    def allaccounts(self):
        print("the calculation of all accounts is:")
        return self.x+self.num+self.summation()
y=childclassy(2,3)
print(y.allaccounts())
