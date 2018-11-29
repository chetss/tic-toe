# '''
# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print(f'Blu is a {blu.species}')
# print("Woo is also a {}".format(woo.__class__.species))

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print(f"{blu.name} is {blu.age} years old")
# print("{} is {} years old".format( woo.name, woo.age))

# '''

# class Computer:

#     __test = 10

#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# print(c.test)

# # change the price
# c.__maxprice = 1000
# c.sell()

# # using setter function
# c.setMaxPrice(1000)
# c.sell()

from collections import deque

queue = deque([1,2,3,4,5])
print(queue)