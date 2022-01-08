# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Don’t use static value for 11-20, 21-30, 31-40. Access the fifth value of each key from the dictionary.
# a.Expected Output
#     i.First
#         1.x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
#         2.y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
#         3.z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
#     ii.Second
#         1.15
#         2.25
#         3.35

dic={}
list1=input("enter 10 digit value for x :").split(",")
list2=input("enter 10 digit value for y :").split(",")
list3=input("enter 10 digit value for z :").split(",")
# dic.update({'x': list1})
# dic.update({'y': list2})
# dic.update({'z': list3})
# #print(dic)
# print("{} has value {}".format(list(dic.keys())[0],list(dic.values())[0]))
# print("{} has value {}".format(list(dic.keys())[1],list(dic.values())[1]))
# print("{} has value {}".format(list(dic.keys())[2],list(dic.values())[2]))
# print(list(dic.values())[0][4])
# print(list(dic.values())[1][4])
# print(list(dic.values())[2][4])
from operator import itemgetter
itemget= itemgetter(4)
print(itemget(list1))
print(itemget(list2))
print(itemget(list3))


