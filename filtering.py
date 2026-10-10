import numpy as np

ages = np.array([[18, 20, 45, 47, 58, 68, 94, 75, 15, 14, 10]])

teneger = ages[ages < 18]
print(teneger)
adult = ages[(ages >= 18) & (ages <= 50)]
print(adult)
sinior = ages[ages > 50]
print(sinior)
evens = ages[ages % 2 == 0]
print(evens)
odd = ages[ages % 2 != 0]
print(odd)
preserve = np.where(ages > 18, ages, 0)
print(preserve)
