# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print (f'welcome {self.firstname} {self.lastname} of year {self.graduationyear}')

# x = Person("John", "Doe")
# x.printname()
# Student('John', 'Doe', 2020).welcome()

# mytuple = ("apple")
# myIt  = iter(mytuple)

# print(next(myIt))
# print(next(myIt))
# print(next(myIt))

# class myNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         if x <= 20:
#             self.a += 1
#         else:
#             raise StopIteration
#         return x


# myclass = myNumbers()
# myit = iter(myclass)

# for x in myit:
#  print(x)

# import datetime
# x = datetime.datetime.now()
# print(x.strftime('%c'))
# import math
# x = [2,3,4,5]
# print(math.ceil(1.5))
# print(math.pi)

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True, 
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=4, sort_keys=True))

# import re


# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())


# try:
#     f = open('mymod.py')
#     try:
#         f.write('Lorem Ipsum')
#     except:
#         print('Cannot write!!')
#     finally:
#         f.close()
# except:
#     print('Error opening file')

# price = 49
txt = "The price is {price} dollars"
print(txt.format(price=34))