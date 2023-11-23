# Public Members
# Public members (generally methods declared in a class) are accessible from outside the class.
# The object of the same class is required to invoke a public method.
# This arrangement of private instance variables and public methods ensures the principle of data encapsulation.
#
# All members in a Python class are public by default. Any member can be accessed from outside the class environment.

#
# class Student:
#     schoolName = 'XYZ School'  # class attribute
#
#     def __init__(self, name, age):
#         self.name = name  # instance attribute
#         self.age = age  # instance attribute
#
# std = Student("Steve", 25)
# print(std.schoolName)  #'XYZ School'
# print(std.name)  #'Steve'
# std.age = 20
# print(std.age)

#
# #
# # Protected Members
# # Protected members of a class are accessible from within the class and are also available to its sub-classes.
# # No other environment is permitted access to it. This enables specific resources of the parent class to be inherited by the child class.
# #
# # Python('s convention to make an instance variable protected is to add a prefix _ (single underscore) to it. '
# #        'This effectively prevents it from being accessed unless it is from within a sub-class.)
#
#


# class Student:
#     schoolName = 'XYZ School'  # protected class attribute
#
#     def __init__(self, name, age):
#         self._name = name  # protected instance attribute
#         self._age = age  # protected instance attribute
#
# std = Student("Swati", 25)
# print(std._name)
# # print(std._schoolName)
# std._school_name="123"
# print(std._school_name)
# std._name = 'Dipa'
# print(std._name)

#
#
#
#
# class Student:
# 	def __init__(self,name):
# 		self._name = name
# 	@property
# 	def name(self):
# 		return self._name
# 	@name.setter
# 	def name(self,newname):
# 		self._name = newname
#
# std = Student("Swati")
# # print(std.name)
#
# std.name = 'Dipa'
# print(std.name)
# print(std._name)
#

# # Private Members
# # Python doesn('t have any mechanism that effectively restricts access to any instance variable or method. '
# #              'Python prescribes a convention of prefixing the name of the variable/method with a single or'
# #              ' double underscore to emulate the behavior of protected and private access specifiers.)
# #
# # The double underscore __ prefixed to a variable makes it private.
# # It gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an AttributeError:
#
# class Student:
#     __schoolName = 'XYZ School'  # private class attribute
#
#     def __init__(self, name, age):
#         self.__name = name  # private instance attribute
#         self.__salary = age  # private instance attribute
#
#     def __display(self):  # private method
#         print('This is private method.')
#
# std = Student("Bill", 25)
# # print(std.__schoolName)  # AttributeError
# print(std.__name)  # AttributeError
# print(std.__display())  # AttributeError
#
# std = Student("Bill", 25)
# print(std._Student__name)  #'Bill'
#
# std._Student__name = 'Steve'
# print(std._Student__name)  #'Steve'
# std._Student__display()  #'This is private method.'


