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
#     def winged_animal_info(self):
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
#         print("Super Class 2 method called")
#
# class Derived(SuperClass1, SuperClass2):
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
#
#
# class B(A):
#     def myname(self):
#         print(" I am a class B")
#
#
# class C(A):
#     def myname(self):
#         print("I am a class C")
#
#     # classes ordering
#
#
# class D(B, C):
#     pass
#
#
# # it prints the lookup order
# print(D.__mro__)
# print(C.mro())




# 111111
# class A:
#     def myname(self):
#         print("I am a class A")
#
#
# class B(A):
#     def myname(self):
#         print("I am a class B")
#
#
# class C(A):
#     def myname(self):
#         print("I am a class C")
#
#
# c = C()
# print(c.myname())


# 2222
# class A:
#   def method(self):
#     print("A.method() called")
#
# class B:
#   def method(self):
#     print("B.method() called")
#
# class C(A, B):
#   pass
#
# class D(C, B):
#   pass
#
# d = D()
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
#    def sayHello(self, name=None):
#       if name is not None:
#          print ('Hello ' + name)
#       else:
#          print ('Hello ')
# obj = Human()
# print(obj.sayHello())
# print(obj.sayHello('Rambo'))


# class Base:
#   def method(self, param2):
#      print("cheeses",param2)
#
# class NotBase(Base):
#   def method(self):
#       print("dill")
#
# obj = NotBase()
# obj.method()