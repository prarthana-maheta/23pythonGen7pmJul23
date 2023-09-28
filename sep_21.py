# creating objects:
# p1 = MyClass()
# print(p1.x)
#
# The __init__() Function
# The examples above are classes and objects in their simplest form,
# and are not really useful in real life applications.
#
# To understand the meaning of classes we have to understand
# the built-in __init__() function.
#
# All classes have a function called __init__(),
# which is always executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:


# The self Parameter
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

# class Person:
#   def __init__(self):
#     # self.name = name
#     # self.age = age
#     # print(height)
#     self.height=[]
#     print(self.height)
#
#   def myfunc(self,height):
#     # print("Hello my name is " )
#     # print(self.name)
#     # self.height.append(150)
#     print(height)
#
#     # if 100 >= height:
#     #   print("height is low")
#
# p1 = Person()
# p1.myfunc(78)


# class Person:
#   def __init__(self, name, age):
#     self.name = 2.5
#     self.age = 50
#   def display(self,name):
#     # name="pkm"
#     print(self.name)
#
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.display("abc"))

#
# __call__ in Python
# Python has a set of built-in methods and __call__ is one of them.
# The __call__ method enables Python programmers to write classes where the instances
# behave like functions and can be called like a function. When the instance is called
# as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).


# class Example:
#     def __init__(self):
#         print("Instance Created")
#     # Defining __call__ method
#     def __call__(self):
#         print("Instance is called via special method")
#     def display(self):
#         print("in display method")
# # Instance created
# e = Example()
# # __call__ method will be calledpr
# print(e())
# # print(e())
#
#
class Product:
    # def __init__(self):
    #     print("Instance Created")
    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)
    def multi(self,a,b):
        print(a*b)
# Instance created
ans = Product()
# __call__ method will be called
# ans(10, 20)
demo = Product()
ans.multi(10,20)


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# The string representation of an object WITHOUT the __str__() function:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1)

# The string representation of an object WITH the __str__() function:

# class Person:
#   # def __init__(self, name, age):
#   #   self.name = name
#   #   self.age = age
#
#   # def __str__(self):
#   #   return f"aapne object call krvaya hai, methoda call kro"
#   def display(age):
#     return f"{age}"
#
# p1 = Person()
#
# print(p1)
# a=p1.display(46)
# print(a)

# Inheritance
#
# A-->B
#
# A--->B-->C
#
# a,b-->c
#
# A--->b,c-->d

