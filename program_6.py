#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

from functools import reduce

Numbers = [10, 11, 10]
sum=reduce(lambda a,b: a+b ,Numbers)
result=(lambda a: a*3 if all(no == Numbers[0] for no in Numbers) else a)

print(result(sum))

x = (lambda a: a*3 if any(no == Numbers[0] for no in Numbers) else 0)
print(x)
