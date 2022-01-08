#Write a Python program to clone or copy a list.

list1=[1,2,3,4,5,6,7]
list2=list1.copy()
print(list1)
print(list2)
list1[0]='A'
print(list1)
print(list2)