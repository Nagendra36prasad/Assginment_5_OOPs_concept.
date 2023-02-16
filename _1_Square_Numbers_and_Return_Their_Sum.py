# Challenge 1:Square Numbers and Return Their Sum
# properties and methods public
# Task 1 ---> Implement a constructor to initialize the values of three properties: x, y, and z
# Task 2 ---> Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum
class Point:
    def __init__(self, x, y, z):     # constructor
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2) # Square Numbers and Return Their Sum

point_obj = Point(1, 3, 5) #   object is created and take simple input 1,3,5
print(point_obj.sqSum())   #   we get output # 35  
