# Write a Python program to check whether a specified value is contained in a group of values.
# a.Test Data :
# b.3 -> [1, 5, 8, 3] : True
# c.-1 -> [1, 5, 8, 3] : False

list1 =[1,2,3,4,5]
#print("True" if 1 in list1 else "False")
result=(lambda a,list: True if a in list else False)
print(result(1,list1))

