# Array in numpy are better than lists because :
# Arrays are much faster than the lists in python,
# and they store homogeneous values in them,
# operations like arithmatic operations are made with each element,
# They store less space than the list.


# The general method to initialize an array is as follows:

# importing numpy module with name as "np"
import numpy as np

# Making an vector named as arr.
arr = np.array([1,2,3,4])

# arr has a 'numpy.ndarray'
print(type(arr))

# since it is one dimentional, therefore it is called as a vector. If it is two dimentional then it is called as a matrix, if it is 3 dimentional or more than three then it is commonly called as a tensor.
print(arr.ndim)

# shape is used to print the number of rows to columns in a tuple format.
print(arr.shape)

# A normal print of an array cna be done linke this.
print(arr) 

# We can made an array with all zeroes and ones like this ->
# the first argument denotes the shape of the array, and the second argument denotes the data type of the elements int the array.
print(np.zeros((2,3), dtype=int))
# like that we can create for ones also ->
print(np.ones((2,3), dtype=int))

# we can create an array with range of elements using the keyword arange()
print(np.arange(10))

# we can give an evenly spaced elements also suing the same keyword
print(np.arange(1,10,2))

# we can desire any number of elements in a given range with equal spacing between them->
print(np.linspace(1,10,5))

# sort keyword is used to sort the elements in an axis i.e., row wise in an array.
x = np.array([[3,2,5,1], [7,8,5,10]])
print(np.sort(x))

# print(np.argsort(x, axis=0))

# we can concatinate two arrays using concatinate keyword in numpy->
a = np.array([[10,2,5], [6,4,8]])
b = np.array([[9,11,2]])
print(np.concatenate((a,b), axis=0))

# Let us take a 3-Dimentional array
D3 = np.array([[[1,2,3,4],
                [5,6,7,8]],

                [[4,3,2,1],
                 [9,8,7,6]],

                 [[3,2,1,4],
                  [8,7,6,9]]])
# We can print the dimention of the array using .ndim keyword
print(D3.ndim)
# We can print the size of the array i.e., the number of elements in the whole array -> i.e., the product of elements in each array to the dimention of the array.
print(D3.size)
# We can print the shape of the array too.
print(D3.shape)  #Output will be (3, 2, 4) where 3 indicates the dimention of the array, 2 indicates number of rows in each dimention, 4 indicates the number of columns int each dimention.


# We can reshape the array using reshape keyword in the numpy.
arr = np.arange(10)
arr = arr.reshape(2,5)
print(arr)

# This is almost 50 to 60 percent everything about arrays in this module. 