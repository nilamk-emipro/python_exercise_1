#Write a Python program to concatenate all elements in a list into a string and return it.

from functools import reduce
Numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
string = ['g','o', 'o', 'd', 'm', 'o', 'r', 'n', 'i', 'n','g']
# ReduceValue=reduce(lambda a,b:a+b ,Numbers)
# print(ReduceValue)
# print(reduce(lambda a,b:a+b ,string))

print(' '.join(Numbers))
print(''.join(string))