# First import the numpy module with name np
import numpy as np

# initialise an array arr 
arr = np.array([[5,4,3,20], 
                [9,4,6,7]])
print(arr[1][1]) #this prints the element in the second row second column.

print(arr[arr<19], arr[arr<19].ndim, arr[arr<19].size) #This returns a one dimentional array with all the numbers form the array arr which satisfies the condition i.e., arr<19.

# Like that we can give any condition like that.
# for example
new_arr = np.array([[1,2,3,4,5,6,7,8,9,10]])
elements_divisible_by_2 = new_arr[new_arr%2 == 0]
print(elements_divisible_by_2)

# *****
elements_in_range_from_3_to_8 = new_arr[(new_arr>3) & (new_arr<=8)]
print(elements_in_range_from_3_to_8)

# we can also replace the elemets in the array by bool using specific conditions.
# *****
element_greater_than_5 = (new_arr>5) | (new_arr == 5)
print(element_greater_than_5)

# We can print the index of the numbers which satisfies the given condition.
indexes_of_numbers_lessthan_8_and_greaterthan_5 = np.nonzero((arr>5) & (arr<8))
print(indexes_of_numbers_lessthan_8_and_greaterthan_5)  # the out put will be (array([1, 1], dtype=int64), array([2, 3], dtype=int64)) where the first array indicates the row number and the second array indicates the column element of the element in the array.

# We can zip the coordinates also.
list_of_coordinates = list(zip(indexes_of_numbers_lessthan_8_and_greaterthan_5[0], indexes_of_numbers_lessthan_8_and_greaterthan_5[1]))
for i in list_of_coordinates:
    print(i)

# we can print the elements also.
print(arr[indexes_of_numbers_lessthan_8_and_greaterthan_5])
print(new_arr[element_greater_than_5])

# If the condition doesn't match any element then it will return an empty list.
no_element = np.nonzero(arr>100) 
print(no_element)

np_element = arr>100 # this will return a matix with bool.
print(np_element)