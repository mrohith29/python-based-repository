# First import the numpy module as np.
import numpy as np

a = np.arange(10)
print(a.shape)

# We can convert from one dimention to two dimention, two dimention to three dimention, two dimention two three dimention.
a = a[np.newaxis, :]
print(a.shape)
print(a)


b = np.array([[1,2,3,4]])
print(b.shape)
b = np.expand_dims(b, axis=1)
print(b.shape)
print(b)
