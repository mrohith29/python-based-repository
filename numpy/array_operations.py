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

arr1 = [[1,2],
        [3,4],
        [1,2]]

arr2 = [[5,6],
        [7,8],
        [3,4]]


# printing the sum of elements in the same matrix
print(np.sum(arr1, axis=0))
print(np.sum(np.sum(arr1,axis=0),axis=0))

# printing the product of the elements in the same matrix
print(np.prod(arr1,axis=0))
print(np.prod(np.prod(arr1, axis=0), axis=0))

# for addition of two arrays 
print(np.sum([arr1, arr2], axis=0))  #axis 0 indicates to perform addition with same position elements in the next matrix.
print(np.sum([arr1, arr2], axis=1)) # axis 1 indicates to perform addition with the all element in the same column of the same matrix.

