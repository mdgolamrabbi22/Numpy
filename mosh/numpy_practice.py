import numpy as np

student = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(student.shape)

print(student.reshape(2, 6))  # row, column
print(student.reshape(2, 2, 3))  # layer, row, column
