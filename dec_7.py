# import camelcase
#
# c = camelcase.CamelCase()
#
# txt = "hello world"
#
# print(c.hump(txt))

# import random
#
# list1=("1","meet",3,4,5,6,7,8,9)
# str1="meet"
# # random.shuffle(list1)
# print(list1)
# print(random.choice(list1))

# list1=[1-100]
# list2=[1,2,3,67,89,100]

# print({1,2,3,4,5})
# if 1 == '':
#     print("hello")
# else:
#     print("hii")
try:
    print(1+'2')
    if 1=='2':
        print("Hello",1+"2")
except SyntaxError as e:
    print("in")
    print(f"error occured in your code is:{e}")
except Exception as e:
    print("in except")
    print(f"error occured in your code is:{e}")

# finally:
#     print("yes in finally")

# try:
#   print("Hello",1+"2")
# except:
#   print("Something went wrong")