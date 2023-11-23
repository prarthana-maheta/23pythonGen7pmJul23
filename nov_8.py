# Abstraction:
# from abc import ABC
#
# from abc import ABC, abstractmethod
#
#
# class DemoClass(ABC):
#     @abstractmethod
#     def method1(self):
#         print("abstract method")
#         return
#
#     def method2(self):
#         print("concrete method")
#
#
# class concreteclass(DemoClass):
#     # def method1(self):
#     #     super().method1()
#     #     return
#     def method2(self):
#         print("2")
#         super().method2()
#         return
#
#
# obj = concreteclass()
# # obj.method1()
# obj.method2()

import abc
from abc import ABC, abstractmethod
from abc import *
# from aug_2.fun1 import var1

class Prepbytes(ABC):
    # an abstract method
    @abc.abstractproperty
    def abstract_method(self):
        print("The abstract method")

    # a normal method
    def normal_method(self):
        print("The normal method")

class A(Prepbytes):
    @property
    def abstract_method(self):
        super().abstract_method()
        print("in ab")

a=A()
print(a.abstract_method)

#
#
# import abc
# from abc import ABC, abstractmethod
# class Color(ABC):
#     def __init__(self, color):
#         self.color = color
#     # an abstract method
#     @abstractmethod
#     def print_color(self):
#         pass
# class Green(Color):
#     def __init__(self):
#         super().__init__("Green")
#     # @property
#     # def print_color(self):
#     #     return self.color
#
# obj = Green()
# print("The color is " + obj.color)
# print(obj.print_color())
#print_color
#
#
#
#
#
#

# import abc
# from abc import ABC, abstractmethod
#
# class SuperClass(ABC):
#     @abstractmethod
#     def my_method(self):
#         print("The abstract superclass")
#
#
#
# class SubClass(SuperClass):
#     def my_method(self):
#         super().my_method()
#         print("The subclass")
#
# obj=SubClass()
# obj.my_method()
