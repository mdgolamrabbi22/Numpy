import numpy as np

# Problem 1

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array)

# Problem 2

# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)

# Problem 3

# print(array[0:: 2])
# print(array[1::2])


# Problem 4

add = array + 5
mul = array * 2
sub = array - 3

# print(add)
# print(sub)
# print(mul)

# Problem 5

data_sum = array.sum()
data_mean = array.mean()
data_min = array.min()
data_max = array.max()
# print(data_sum)
# print(data_mean)
# print(data_min)
# print(data_max)

# Problem 6

new_array = np.array([5, 10, 15, 20, 25, 30, 35, 40])
# print(new_array[0])
# print(new_array[-1])
# print(new_array[:4])
# print(new_array[3:7])

# Problem 7 3 জন ছাত্রের 3টি subject-এর marks দিয়ে 3×3 array তৈরি করো।
# তারপর shape, total element এবং প্রত্যেক row-এর marks print করো।

student_mark = np.array([[100, 80, 95],
                         [80, 95, 78],
                         [78, 98, 87]])

# print(student_mark.ndim)
# print(student_mark.shape)
# print(student_mark.size)
# print(student_mark[0])
# print(student_mark[1])
# print(student_mark[2])

# Problem 8 প্রতিটি ছাত্রের Total ও Average

student1_TotalMark = student_mark[0].sum()
student1_Avg = student_mark[0].mean()

student2_TotalMark = student_mark[1].sum()
student2_Avg = student_mark[1].mean()

student3_TotalMark = student_mark[2].sum()
student3_Avg = student_mark[2].mean()

print(student1_TotalMark)
print(student1_Avg)

print(student2_TotalMark)
print(student2_Avg)

print(student3_TotalMark)
print(student3_Avg)
