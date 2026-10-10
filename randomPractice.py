import numpy as np

# random number Generate

rng = np.random.default_rng()
# print(rng.integers(low=1, high=10, size=(3, 3)))
# print(np.random.uniform(low=-1, high=1, size=(2, 2)))

# array Shuffle

# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle((array))
# print(array)

# array Choice

fruits = np.array(["Banana", "apple", "licu", "pinaple"])
fruit = rng.choice(fruits, size=3)
print(fruit)
