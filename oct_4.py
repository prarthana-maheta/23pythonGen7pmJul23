# class Vehicle:
#
#     name="BMW"
#     def __call__(self, *args, **kwargs):
#         name="FERRARI"
#         return name
#     def __str__(self):
#         name="AUDI"
#         return name
#     def __init__(self):
#         self.name="MERCEDES"
#     def display(self):
#         self.name="HONDA"
#         return self.name
#
# v=Vehicle()
# print(v.name)
# print(v())

# num=4
# i=1
#
# if num%i == 0:
#     print(num%i)
#     i+=1
#     print(i)
#     if i == 1:
#         print("Prime")

# print([1,2,3]+[1,2,3])
# [1,1]
# [1,2,1]
# [1,,3,1]
# [1,2,4,4,1]
# [1,3,6,8,5,1]
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)


# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is
# derived from a single parent class. In other words, we can say one parent class and multiple child classes

# class Vehicle:
#     def info(self):
#         print("This is Vehicle")
#
# class Car(Vehicle):
#     def car_info(self, name):
#         print("Car name is:", name)
#
# class Truck(Vehicle):
#     def info(self, name="CITY"):
#         super().info()
#         print("Truck name is:", name)
# # obj1 = Car()
# # obj1.info()
# # obj1.car_info('BMW')
#
# obj2 = Truck()
# obj2.info()
# obj2.info('Ford')




# Hybrid Inheritance
# When inheritance is consists of multiple types or
# a combination of different inheritance is called hybrid inheritance.
#
# class Vehicle:
#     def __init__(self):
#         print("inside init")
#         self.v="NOOO"
#     def vehicle_info(self):
#         print("Inside Vehicle class",self.v)
# class Car(Vehicle):
#     def vehicle_info(self):
#         self.v="YESS"
#         print("Inside Car class",self.v)
# class Truck(Vehicle):
#     def car_info(self):
#         print("Inside Truck class",self.v)
# # Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def car_infoo(self):
#         print("Inside SportsCar class")
# # create object
# s_car = SportsCar()
# # s_car.vehicle_info()
# s_car.vehicle_info()
# s_car.sports_car_info()





# class method
# class methods demo

# class Student:
#     # class variable
#     school_name = 'ABC School'
#
#     # constructor
#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age
#
#     # instance method
#     @classmethod
#     def show(cls,name):
#         # access instance variables and class variables
#         print('Student:',name)
#
#     # instance method
#     def change_age(self, new_age):
#         # modify instance variable
#         self.age = new_age
#
#     # class method
#     @classmethod
#     def modify_school_name(cls,new_name):
#         # modify class variable
#         cls.school_name = new_name
#         print(cls.school_name)
#         cls.show(new_name)
#
# s1 = Student("Harry", 12)

# call instance methods
# s1.show()
# s1.change_age(14)

# call class method
# Student.modify_school_name('XYZ School')
# call instance methods
# s1.show()



# static method:
#
# Static methods are a special case of methods. Sometimes, you’ll write code that belongs to a class,
#     but that doesn’t use the object itself at all. It is a utility method and doesn’t
# need an object (self parameter) to complete its operation. So we declare it as a static method.
# Also, we can call it from another method of a class.

#
# class Employee(object):
#
#     def __init__(self, name, salary, project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
#
#     # @staticmethod
#     def gather_requirement(project_name):
#         if project_name == 'ABC Project':
#             requirement = ['task_1', 'task_2', 'task_3']
#         else:
#             requirement = ['task_1']
#         return requirement
# #
#     # instance method
#     def work(self):
#         # call static method from instance method
#         requirement = self.gather_requirement(self.project_name)
#         for task in requirement:
#             print('Completed', task)
#
# emp = Employee('Kelly', 12000, 'ABC Project')
# emp.work()
# print(Employee.gather_requirement("ABC Project"))


#
# 3 type methods


# Difference #1: Primary Use
#
# Class method Used to access or modify the class state. It can modify the class state by changing the
# value of a class variable that would apply across all the class objects.
#
# The instance method acts on an object’s attributes. It can modify the object state by
# changing the value of instance variables.
# Static methods have limited use because they don’t have access to the attributes of an object
#
# (instance variables) and class attributes (class variables). However,
# they can be helpful in utility such as conversion form one type to another.


#
# Difference #2: Method Defination
#
# All three methods are defined inside a class, and it is pretty similar to defining a regular function.
#
# Any method we create in a class will automatically be created as an instance method.
# We must explicitly tell Python that it is a class method or static method.
#
# Use the @classmethod decorator or the classmethod() function to define the class method
# Use the @staticmethod decorator or the staticmethod() function to define a static method.

# class Student:
#     # class variables
#     school_name = 'ABC School'
#     # constructor
#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age
#     # instance variables
#     def show(self):
#         print(self.name, self.age, Student.school_name)
#     @classmethod
#     def change_School(cls, name):
#         print(self.name)
#         cls.school_name = name
#         print(cls.school_name)
#         cls.show()
#     @staticmethod
#     def find_notes(subject_name):
#         print(school_name)
#         return ['chapter 1', 'chapter 2', 'chapter 3']
#
# # print(Student.find_notes('python'))
# s1=Student('pkm','50')
# # s1.show()
# s1.change_School('Royal')
# Student.change_School('Rooooyal')

# Student.show(self=self)
# Difference #3: Method Call
# Class methods and static methods can be called using ClassName or by using a class object.
# The Instance method can be called only using the object of the class.

# Difference #4: Attribute Access
# Both class and object have attributes. Class attributes include class variables,
# and object attributes include instance variables.
#
# The instance method can access both class level and object attributes. Therefore, It can modify the object state.
# Class methods can only access class level attributes. Therefore, It can modify the class state.
# A static method doesn’t have access to the class attribute and instance attributes.
# Therefore, it cannot modify the class or object state.

# class Student:
#     # class variables
#     school_name = 'ABC School'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # instance method
#     def show(self):
#         # access instance variables
#         print('Student:', self.name, self.age)
#         # access class variables
#         print('School:', self.school_name)
#
#     @classmethod
#     def change_School(cls, name):
#         # access class variable
#         print('Previous School name:', cls.school_name)
#         cls.school_name = name
#         print('School name changed to', Student.school_name)
#
#     @staticmethod
#     def find_notes(subject_name):
#         # can't access instance or class attributes
#         return ['chapter 1', 'chapter 2', 'chapter 3']
#
# # create object
# jessa = Student('Jessa', 12)
# # call instance method
# jessa.show()
#
# # call class method
# Student.change_School('XYZ School')


# Difference #5: Class Bound and Instance Bound
# An instance method is bound to the object, so we can access them using the object of the class.
# Class methods and static methods are bound to the class. So we should access them using the class name.
#
#
# class Student:
#     def __init__(self, roll_no): self.roll_no = roll_no
#
#     # instance method
#     def show(self):
#         print('In Instance method')
#
#     @classmethod
#     def change_school(cls, name):
#         print('In class method')
#
#     @staticmethod
#     def find_notes(subject_name):
#         print('In Static method')
#
#
# # create two objects
# jessa = Student(12)
#
# # instance method bound to object
# print(jessa.show)
#
# # class method bound to class
# print(jessa.change_school)
#
# # static method bound to class
# print(jessa.find_notes)
