import numpy as np

array = np.array([1, 2, 3, 4, 5])  # create a numpy array one dimension array

print(array.dtype)  # check data type of array
print(array.shape)  # check shape of array
print(array.ndim)  # check number of dimensions of array
print(array.size)  # check total number of elements in array
print(array.itemsize)  # check size of one element in bytes
print(array.nbytes)  # check total size of array in bytes

array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # create a numpy array two dimension array

array_3d = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])  # create a numpy array three dimension array
