# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Elements can be of different data types

'''
Creating a Tuple
'''

tuple = ()
# tuple = ("cat", [4,3,2], (1,2,3))
# tuple = 1234, 4321, 'hello!'
# tuple = 'hello',
# tuple = ('hello' ,)
# tuple = ('hello')
# print(tuple)

'''
Access Tuple Elements
'''
# tuple = (1234, 4321, 'hello!')
# print(tuple[0])
# print(tuple[-1])
# print(tuple[2])

'''
Slicing Tuples in Python
'''
# fruits = ('orange', 'apple','pear','grapes','banana')
# print(fruits[:])
# print(fruits[2:5])
# print(fruits[:-2])
# print(fruits[:2])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])

'''
Changing a tuple
'''
# fruits = ('orange', 'apple','pear','grapes','banana')
# fruits[0] = 'pear' #TypeError because tuple cannot be changed once its created

'''
Deleting a Tuple
'''

# fruits = ('orange', 'apple','pear','grapes','banana')
# del fruits[0]
# print(fruits) #can't change a tuple once it's created,but you can delete the entire tuple

'''
Type Methods
'''
# print(dir(tuple))

# fruits = ('orange','orange', 'apple','pear','grapes','banana')
# print(fruits.count('orange'))
# print(fruits.index('apple'))

