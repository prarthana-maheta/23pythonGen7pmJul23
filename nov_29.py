# math, json


# import math
#
# x = math.sqrt(27.5)
#
# print(x)
#
# dict1={2:math.sqrt(2)}
# print(dict1)


# import math
#
# x = math.ceil(1.4)
# y = math.floor(1.9)
#
# # print(round(1.4))
# print(x) # returns 2
# print(y) # returns 1


# import math
#
# x = math.pi
#
# print(x)

# import math
# x= abs(10)
# print(x)

# import json
#
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y)
# print(y["age"])


# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x,sort_keys=True,indent=10)
#
# # the result is a JSON string:
# print(y)


# regex

import re

txt = "The Spain"
x = re.findall(".*$", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("harsh", txt)
y = re.search("\s", txt)
print(len(x))
print(y)
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string


# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"


# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
#
# r"ain\b"
#
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
#
# r"ain\B"
#
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"