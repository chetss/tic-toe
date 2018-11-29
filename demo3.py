'''
from collections import deque

queue = deque([1,2,3,4,5])
queue.appendleft(8)
queue.append(10)

print(queue)

queue.popleft()
print(queue)

'''

# matrix = [
#      [1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#  ]

# print([[row[0] for row in matrix] for i in range(4)])
	
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# print([(a) for q,a in zip(questions,answers)])
# # print([[row[i] for row in matrix] for i in range(4)])
# print(sorted(questions))
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.sort())
# print(fruits)

# import timeit

# list1 = [1,2,2,3,3,4,4]

# timeit.timeit("""print(list1)""" ,number = 100000)

'''
class BaseClass:
    """A simple example class"""
    i = 12345
    
    def __init__(self):
    	print('init called Base')
    
    def f(self):
        return 'from Base Class'


class DrivedClass(BaseClass): 
	
	def __init__(self):
		BaseClass.__init__(self)
		print('init called drived')


	def f(self):
		return 'from Drived Class'
	
	def drivedFun(self):
		return 'drived fucntion'

class Box():
	"""docstring for Box"""
	def __init__(self):
		super(Box, self).__init__()

	def BoxDim():
		return 'box dimension'
		
d = DrivedClass()
print(d.f())
print(isinstance(Box(), BaseClass))
print(isinstance(d, DrivedClass))

'''
# class MyReverse():
# 	def __init__(self,data):
# 		self.data = data
# 		self.index = 0

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		print(f'self.index {self.index}')
# 		if self.index == len(self.data):
# 			raise StopIteration
# 		self.index = self.index + 1
# 		return self.data[self.index-1]

# obj2 = MyReverse('Box')

# for i in obj2:
# 	print(i)

'''
def reverse(data):
	for index in range(0,len(data),1):
		yield data[index]

print([element for element in reverse('span')])
'''

# import glob
# print(glob.glob('**'))

# import sys
# print(sys.stdout)

'''
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

zlib.decompress(t)

zlib.crc32(s)
'''
# import copy

# old_list = [1,2,3]
# new_list = copy.copy(old_list)

# old_list[0]= "9"

# print(old_list) 
# print(new_list) 


# important
# Copy And deepCopy only work on nested objects like nested list,nested dict , nested tuple

# import copy

# old_list = [[1,2,3]]
# new_list = copy.copy(old_list)

# old_list[0][0]= "9"

# print(old_list) 
# print(new_list)

# numberList = [1, 2, 3]
# strList = ['one', 'two', 'three']
# tempdict = {'name':'chetan','city':'pune'}
# print(tempdict)
# print(dict(zip(numberList,strList)))
# print({(s,y) for s,y in  zip(numberList,strList)})

'''
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name


obj1 = Person('King')
obj2 = Person('kong')
# print(obj1.name)
del obj1.name
# obj1.name('ofjungle')
obj1.name = 'ofjungle'
# print(obj1.name)
print(obj2.name)
'''