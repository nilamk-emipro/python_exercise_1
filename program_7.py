# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

string=input("Insert Any string: ")
num=int(input("How many time copy that string: "))
copystring=(lambda str,no: str*no)
print(copystring(string,num))