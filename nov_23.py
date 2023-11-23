# import the time module


import time

# get the current time in seconds since the epoch
# seconds = time.time()
#
# print("Seconds since epoch =", seconds)

# Output: Seconds since epoch = 1672214933.6804628




# Python time.localtime() Function
# The localtime() function takes the number of seconds passed since epoch as
# an argument and returns struct_time (a tuple containing 9 elements corresponding to struct_time) in local time.
#
# import time
#
# result = time.localtime(time.time())
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)


# Python time.asctime() Function
# In Python, the asctime() function takes struct_time as an argument and returns a string representing it.
#
# Similar to mktime(), the time_tuple has the following structure:
#
# import time
#
# t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
#
# result = time.asctime(t)
# print("Result:", result)

# Output: Result: Fri Dec 28 08:44:04 2022

#
# Python time.strftime() Function
# The strftime() function takes struct_time (or tuple corresponding to it)
# as an argument and returns a string representing it based on the format code used. For example,


# import time
# #
# named_tuple = time.localtime(0) # get struct_time
# # named_tuple ='12/12/12 12:12:12'
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# time.sleep(5)
#
# print(named_tuple)
# print(time_string)


# DATETIME

import datetime

# get the current date and time
# now = datetime.datetime.now()
# print(now)
#
# start_time=datetime.datetime.now()
# print(datetime.datetime.now - start_time)



import datetime

# get current date
# current_date = datetime.date.today()
#
# print(current_date)


# import datetime
#
# print(dir(datetime))
# # start_time=datetime.time.now()
#
# import datetime
#
# d = datetime.date(2022,3,3)
# print(d)


# from datetime import time
#
# a = time(25)
# print(a)
# print("Hour =", a.hour)
# print("Minute =", a.minute)
# print("Second =", a.second)
# print("Microsecond =", a.microsecond)
#
# from datetime import datetime
#
# a = datetime(2022, 12, 28, 23, 55, 59, 342380)
#
# print("Year =", a.year)
# print("Month =", a.month)
# print("Hour =", a.hour)
# print("Minute =", a.minute)
# print("Timestamp =", a.timestamp())


# from datetime import datetime
#
# # current date and time
# now = datetime.now()
# print(now)
# t = now.strftime("%H:%M:%S")
# print("Time:", t)
# #
# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# # # mm/dd/YY H:M:S format
# print("s1:", s1)
# #
# s2 = now.strftime("%d/%m/%y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s2:", s2)

#
from datetime import datetime

# date_string =
# print("date_string =", date_string)

# use strptime() to create date object
date_object = datetime.strptime("25 December, 2022", "%d %B, %Y")

print("date_object =", date_object)

start_time=time.time()
for i in range(1,100):
    time.sleep(1)
    print(i*i)
print(time.time()-start_time)

