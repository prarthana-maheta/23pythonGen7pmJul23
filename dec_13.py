#
#
# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)
import os

# f = open("1.text", "a")
# print(f.write(" meet, harsh"))
# f.close()

# read()
# write()
# open()
# close()

#
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("1.text", "r")
# data=f.read(2)
# print(data)
# f1= open("2.txt", "w")
# f1.write("hi ")

# os.remove('1.text')



# with open("1.txt","w") as f:
#     f.write("Hello World")


import pyautogui

pyautogui.screenshot("screenshot.png")
pyautogui.click("Ctrl")

