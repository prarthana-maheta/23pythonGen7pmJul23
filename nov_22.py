#
# # Collection modules:
# #
# # 1) Counter
# #
# # class collections.Counter([iterable-or-mapping])
#
#
# # A Python program to show different
# # ways to create Counter
# from collections import Counter
#
# # With sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
#                'B', 'A', 'C']))
#
# # with dictionary
# print(Counter({'A': 3, 'B': 5, 'C': 2}))
# #
# # # with keyword arguments
# print(Counter(A=3, B=5, C=2))


# OrderedDict()
# The Python OrderedDict() is similar to a dictionary
# object where keys maintain the order of insertion.
# If we try to insert key again, the previous value will be overwritten for that key.

# import collections
#
# d1 = collections.OrderedDict()
# B='B'
# d1['A'] = 10
# d1['C'] = 12
# d1['B'] = 11
# d1['D'] = 13
# d1[B] = 13
#
# for k, v in d1.items():
#     print(k, v)

#
# defaultdict()
# The Python defaultdict() is defined as a dictionary-like object.
# It is a subclass of the built-in dict class.
# It provides all methods provided by dictionary but takes the first argument as a default data type.

# from collections import defaultdict
# number = defaultdict()
# # number['one'] = 1
# number['two'] =2
# print(number['two'])

# deque()
# The Python deque() is a double-ended queue which allows us
# to add and remove elements from both the ends.
#
# Example
#
# from collections import deque
# list1 = ["x","y","z"]
# deq = deque(list1)
# print(deq)
# x=list1.pop(0)
# print(x)
# x=deq.remove("y")
# print(x)

# Chainmap Objects
# A chainmap class is used to groups multiple
# dictionary together to create a single list.
# The linked dictionary stores in the list and
# it is public and can be accessed by the map attribute. Consider the following example.

# from collections import ChainMap
# baseline = {'Name': 'Peter', 'Age': '14'}
# adjustments = {'age': '15', 'Roll_no': '0012'}
# adjustments=[1,2,3]
# baseline=[4,5,6]
# print(list(ChainMap(adjustments, baseline)))


# NamedTuple()
# # Python code to demonstrate namedtuple()
#
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', [ 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S)

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
print(S.age)


# datetime
# time
# math
# json
# regex

# pip
# pyautogui
# random
#
# try- except
# file handling
#
#
# database connection





