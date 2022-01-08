#Write a Python program to count the number of strings in a list where the string length is 2 or more and the first and last character are the same from a given list of strings.

# def fun(value):
#   count = 0
#   for word in value:
#     if len(word) > 1 and word[0] == word[-1]:
#       count += 1
#   return count
# print(fun(['abc', 'xyz', 'aba', '1221']))

list1=['abc', 'aba', 'xyx', 'ajsg','aa']
total=(lambda list1: len([char for char in list1 if len(char)>2 and char[0]==char[-1] ]))
print(total(list1))
