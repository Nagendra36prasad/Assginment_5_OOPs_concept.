# Challenge 2: Implement a Calculator Class
# Write a Python class called Calculator by completing the tasks
# Implement an initializer to initialize the values of num1 and num2. 
# Methods add(), multiply(), subtract(), divide().

class Calculator:
    def __init__(self, num1, num2):   # constructor
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero"
        return self.num2 / self.num1

obj = Calculator(10, 94)    #   object is created and take simple input no1=10,no2=94
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())
