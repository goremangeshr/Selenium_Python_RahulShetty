from OopsDemo import Calculator

class childimplementation(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2,4)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = childimplementation()
print(obj.getCompleteData())
