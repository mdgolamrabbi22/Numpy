import numpy as np

array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 1)
# print(array * 2)
# print(array / 3)
# print(array ** 4)
# print(array // 4)

array_2 = np.array([4, 5, 6])

# print(array + array_2)
# print(array - array_2)
# print(array * array_2)
# print(array / array_2)
# print(array ** array_2)

floor_array = np.array([2.3, 4.5, 6.8])
# print(np.ceil(floor_array))
# print(np.floor(floor_array))
# print(np.round(floor_array))
# print(np.sqrt(floor_array))

# Exercise

radious = np.array([1, 2, 3])
rec = np.pi * radious ** 2
# print(rec)


# compariosn operator

scores = np.array([100, 65, 48, 12, 78, 80])

print(scores == 100)
print(scores >= 80)
print(scores <= 40)
