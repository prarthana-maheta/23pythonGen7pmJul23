# Single inheritance in python
# Base class
# class Parent_class:
#     # Constructor
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def Employee_Details(self):
#         return self.id, self.name
#     def Employee_check(self):
#         if self.id > 500000:
#             return " Valid Employee "
#         else:
#             return " Invalid Employee "
# class Child_class(Parent_class):
#     def End(self):
#         print(" END OF PROGRAM ")
# Employee1 = Parent_class("Employee1", 600445)
# print(Employee1.Employee_Details(), Employee1.Employee_check())
# Employee2 = Child_class("Employee2", 198754)
# print(Employee2.Employee_Details(), Employee2.Employee_check())
# Employee2.End()


# Multiple Inhertiance
# class SuperClass1:
#     # features of SuperClass1
#
# class SuperClass2:
#     # features of SuperClass2
#
# class MultiDerived(SuperClass1, SuperClass2):
#     # features of SuperClass1 + SuperClass2 + MultiDerived class


# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")
#
# class WingedAnimal:
#     def mammal_info(self):
#         print("Winged animals can flap.")
#
# class Bat(Mammal, WingedAnimal):
#     pass
#
# # create an object of Bat class
# b1 = Bat()
#
# b1.mammal_info()
# b1.winged_animal_info()

# MRO

# class SuperClass1:
#     def info(self):
#         print("Super Class 1 method called")
#
# class SuperClass2:
#     def info(self):
#         super().info()
#
# class Derived(SuperClass2, SuperClass1):
#     pass
#
# d1 = Derived()
# d1.info()


# class A:
#     pass
# class B:
#     pass
# class C(A, B):
#     pass
# class D(B, A):
#     pass
# class E(C,D):
#     pass


# __mro__, mro()
# class A:
#     def myname(self):
#         print(" I am a class A")
# class B(A):
#     def myname(self):
#         print(" I am a class B")
# class C(B):
#     def myname(self):
#         print("I am a class C")
#     # classes ordering
# class D(C):
#     pass
# # it prints the lookup order
# # print(D.__mro__)
# print(C.mro())


# 111111
# class A:
#     def myyname(self):
#         print("I am a class A")
# class B(A):
#     def myname(self):
#         print("I am a class B")
# class C(A,B):
#     def myyname(self):
#         print("I am a class C")
# c = C()
# print(c.myname())


# 2222
# class A:
#       def __init__(self,name):
#           self.name=name
#       def __call__(self):
#           return self.name
#       def method(self):
#         print(f"A.method() called with {self.name}")
# class B:
#     def __init__(self, name):
#         super().__init__("XYZ")
#         self.name = name
#     def method(self):
#         print("B.method() called")
# class C(A, B):
#   pass
# class D(C):
#   pass
# d = D("PKM")
# print(d())
# d.method()


# Example: + Operator Overloading in Python
# To overload the + operator, we will need to implement __add__() function in the class.
#
# With great power comes great responsibility. We can do whatever we like inside
# this function. But it is more sensible to return the Point object of the coordinate sum.

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
#
# p1 = Point(1, 2)
# p2 = Point(2, 3)
#
# print(p1+p2)
#
# # Output: (3,5)

#
# Operator	Expression	Internally
# Addition	p1 + p2 	p1.__add__(p2)
# Subtraction	p1 - p2 	p1.__sub__(p2)
# Multiplication	p1 * p2 	p1.__mul__(p2)
# Power	p1 ** p2	 p1.__pow__(p2)
# Division	p1 / p2 	p1.__truediv__(p2)
# Floor Division	p1 // p2	 p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2	  p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	 p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	 p1.__rshift__(p2)
# Bitwise AND	p1 & p2	  p1.__and__(p2)
# Bitwise OR	p1 | p2  	p1.__or__(p2)
# Bitwise XOR	p1 ^ p2  	p1.__xor__(p2)
# Bitwise NOT	~p1	  p1.__invert__()


# Method overloading
# class Human:
#     def sayHello(self, name):
#         if name is not None:
#             print('Hello ' + name)
#         # else:
#         #    print ('Hello ')
#
#     def sayHello(self, name):
#         print('Hello ')
#         # return 1
#
# obj = Human()
# # print(obj.sayHello())
# print(obj.sayHello('Rambo'))


# class Base:
#   def method(self, param2):
#      print("cheeses",param2)
#
# class NotBase(Base):
#   def method(self):
#       super().method(param2="abc")
#       print("dill")
#
# obj = NotBase()
# obj.method()

# x=y=5,10
# res= x == y
# print(res)


# class University:
#     def __init__(self):
#         self.name = 'Yele University'
#         print("You are in University Class Constructor")
#     def disp(self):
#         print('You are in University class disp method')
# class College(University):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Yale School of Medicine'
#         print('You are in college Class Constructor')
#     def show(self):
#         print('College class instance method:', self.name)
# college = College()
# # college.show()
# college.disp()







# class Taxi:
#     def __init__(self, model, capacity, variant):
#         self.__model = model
#         self.__capacity = capacity
#         self.__variant = variant
#     def getModel(self):
#         return self.__model
#     def getCapacity(self):
#         return self.__capacity
#     def setCapacity(self, capacity):
#         self.__capacity = capacity
#     def getVariant(self):
#         return self.__variant
#     def setVariant(self, variant):
#         self.__variant = variant
# class Vehicle(Taxi):
#
#     def __init__(self, model, capacity, variant, color):
#         super().__init__(model, capacity, variant)
#         self.__color = color
#     def vehicleInfo(self):
#         return (self.getModel() + " " + self.getVariant()
#                 +" in " + self.__color + " with " + self.getCapacity() + " seats")
#
# # v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
# # print(v1.vehicleInfo())
# # print(v1.getModel())
# v2 = Vehicle("Fortuner", "7", "MT2755", "White")
# # print(v2.vehicleInfo())
# print(v2.getModel())
#
#