# Challenge 3: Implement the Complete Student Class
# Task1 --->Implement the following "properties" as private:
# name
# rollNumber

# Task2 --->Include the following methods to get and set the 'private properties' above:
# getName()
# setName()
# getRollNumber()
# setRollNumber()

class Student:
    def __init__(self):
        self.__name = ""             # private by prefixing its name with two underscores.
        self.__rollNumber = ""       

    def display(self):
        return f"name:{self.__name} \nroll number:{self.__rollNumber}"

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

student = Student()
student.display()
student.setName("Nagendra prasad R")
student.setRollNumber("12345")
print(student.getName())       # output: Nagendra Prasad R
print(student.getRollNumber()) # output: 12345
