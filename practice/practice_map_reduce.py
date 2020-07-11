# MAP
def fahrenheit(celsius):
    return (9/5) * celsius + 32
temps = [0, 22, 40.1, 100]
print(f"Example 1.1: {list(map(fahrenheit, temps))}")
print(f"Example 1.2: {list(map(lambda celsius: (9/5) * celsius + 32, temps))}")

l1 = [1, 3, 5]
l2 = [2, 6, 8]
l3 = [10, 20, 45]
print(f"Example 1.3: {list(map(lambda x,y,z: x*y*z, l1, l2, l3))}")

# REDUCE
from functools import reduce
lst = [47, 11, 99, 42, 17]
print(reduce(lambda x, y: x*y, lst))
# max() implementation via the reduce()
print(reduce(lambda a, b: a if a > b else b, lst))



