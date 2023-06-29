import numpy as np
''' For user input use this code snippet 
-->
print('Enter the order of the array')
M, N =input().split()  # M ->rows & N->columns
print('Enter the elements')
arr1 = np.array([input().split() for _ in M], int)
arr2 = np.array([input().split() for _ in M], int)
<--
'''
# for practising purpose I am taking two defined arrays

arr1 = [[1, 2],
        [3, 4],
        [1, 2]]

arr2 = [[5, 6],
        [7, 8],
        [3, 4]]


# printing the sum of elements in the same matrix
print(np.sum(arr1, axis=0))
print(np.sum(np.sum(arr1, axis=0), axis=0))

# printing the product of the elements in the same matrix
print(np.prod(arr1, axis=0))
print(np.prod(np.prod(arr1, axis=0), axis=0))

# for addition of two arrays
# axis 0 indicates to perform addition with same position elements in the next matrix.
print(np.sum([arr1, arr2], axis=0))
# axis 1 indicates to perform addition with the all element in the same column of the same matrix.
print(np.sum([arr1, arr2], axis=1))

# for subtraction of the two matrixes
print(np.subtract(arr1, arr2))

# for multiplication for two matrixes
print(np.multiply(arr1, arr2))  #this operation will just print a matix in which the element at a position is equal to the product of the elements of two matrices

# for division of two matrices
print(np.divide(arr1, arr2))

# for floor division of thw matrices
print(np.floor_divide(arr1, arr2))

# for mod apply mod operation on two matrices
print(np.mod(arr1,arr2))

# for power of the two matrices
print(np.power(arr1, arr2)) #this will print the array in which the elements are the remainder of (arr1[i][j])**(arr2[i][j])

'''
These are the most basic mathematical operations on two matrices using numpy module.
'''