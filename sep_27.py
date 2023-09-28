# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.

# 1)Single Inheritance:

# class ParentClass:
#     def display(self,name):
#         return f"My name is {name}"
#
# class ChildClass(ParentClass):
#     pass
#
# a=ChildClass()
# # b=a.display("PKM")
# print(a.display("PKM"))

# 2)Multilevel Inhertiance:

# class SuperClass:
#     # Super class code here
#
# class DerivedClass1(SuperClass):
#     # Derived class 1 code here
#
# class DerivedClass2(DerivedClass1):
    # Derived class 2 code here

# 3) Multiple INheritance:
# class MostParentClass:
#     pass
#
# class ParentClass:
#     pass
#
# class ChildSubClass(MostParentClass,ParentClass)
#     pass



# Create a class named Person, with firstname and lastname properties, and a printname method:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def __call__(self):
#         print("call")
#     def printname(self):
#         print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()
# x()

# Create a class named Student, which will inherit the properties and methods from the Person class:

# class Student(Person):
#     pass
#
# a=Student("abc","ayz")
# a()

# x = Student("Mike", "Olsen")
# x.printname()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self,firstname,lastname):
#         super().__init__(firstname,lastname)
#         self.firstname="PKM"
#         self.lastname="PKM"
#
#     def print2(self):
#         print(self.firstname, self.lastname)
#       # pass
# # Use the Student class to create an object, and then execute the printname method:
# x = Student("Mike", "Olsen")
# x.printname()
# class Polygon:
#     # Initializing the number of sides
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#     def inputSides(self):
#         self.sides = [1,2,3]
#     # method to display the length of each side of the polygon
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
# class Triangle(Polygon):
#     # Initializing the number of sides of the triangle to 3 by
#     # calling the __init__ method of the Polygon class
#     def __init__(self):
#         Polygon.__init__(self,3)
#     def findArea(self):
#         a, b, c = self.sides
#         super().dispSides()
#         # calculate the semi-perimeter
#         # s = (a + b + c) / 2
#         # Using Heron's formula to calculate the area of the triangle
#         # area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         # print('The area of the triangle is %0.2f' %area)
# # Creating an instance of the Triangle class
# t = Triangle()
# # Prompting the user to enter the sides of the triangle
# t.inputSides()
# # Displaying the sides of the triangle
# t.dispSides()
# # Calculating and printing the area of the triangle
# t.findArea()



# Method overriding
# However, what if the same method is present in both the superclass and subclass?
#
# In this case, the method in the subclass overrides the method in the superclass. This concept is known as method overriding in Python.

# class Animal:
#     # attributes and method of the parent class
#     name = ""
#
#     def eat(self):
#         print(f"I can eat name")

# inherit from Animal
# class Dog(Animal):
#     # override eat() method
#     super.eat()
#     # def eat(self):
#     #     super().eat()
#     #     print("I like to eat bones")
#
# # create an object of the subclass
# labrador = Dog()
# # # call the eat() method on the labrador object
# labrador.eat("apple")



# how to overcome
#
#
# class Animal:
#     name = ""
#
#     def eat(self):
#         print("I can eat")
#
#
# # inherit from Animal
# class Dog(Animal):
#
#     # override eat() method
#     def eat(self):
#         # call the eat() method of the superclass using super()
#         super().eat()
#
#         print("I like to eat bones")
#
#
# # create an object of the subclass
# labrador = Dog()
#
# labrador.eat()