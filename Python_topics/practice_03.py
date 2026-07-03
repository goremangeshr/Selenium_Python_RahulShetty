#
#
# class BasicCalculator():
#
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#
#     def getData(self):
#         print("print method class")
#
#     def Addition(self):
#         return "Addition", self.a + self.b
#
#     def Subtraction(self):
#         return "Subtraction", self.a - self.b
#
#     def Multiplication(self):
#         return "Multiplication", self.a * self.b
#
#     def Division(self):
#         return "Division", self.a / self.b
#
# obj = BasicCalculator(10,5)
# obj.getData()
# print(obj.Addition())
#
# obj1 = BasicCalculator(10,5)
# obj1.getData()
# print(obj1.Addition())
#
# obj2 = BasicCalculator(10,5)
# obj2.getData()
# print(obj2.Addition())
#
# obj3 = BasicCalculator(10,5)
# obj3.getData()
# print(obj3.Addition())

##################################################

# def GreetUser(username):
#     print(f"Hello, {username}!, welcome to the python course")
#
# GreetUser("Mangesh")

def CalculateAverage(num1, num2, num3):

    average = (num1 + num2 + num3) / 30
    return average

result = CalculateAverage(10,20,30)
print(f"average of {10},{20},{30} is {result}")
