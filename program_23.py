# Write a Python program to sum all the items in a list
from functools import reduce
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda a,b:a+b ,Numbers))