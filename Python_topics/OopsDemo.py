
class Calculator:
    num =100        # Class variable

    def __init__(self,a,b):
        self.firstNumber = a            #instance variables declared inside the constructor
        self.secondNumber = b           #instance variables declared inside the constructor
        print("I am called automatically when object is created")

    def getData(self):
        print("existing method")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num   


obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())
