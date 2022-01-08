#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

Number=int(input("Insert Any int Value: "))
#print((Number-17)*2 if Number>17 else abs(Number - 17))
Ans=(lambda num : (Number-17)**2 if Number>17 else abs(Number - 17))
print(Ans(Number))