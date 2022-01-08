#Write a Python program to count the number occurrences of a specific character in a string.

string = input("Enter any string: ")
char=input("Enter specific charater: ")
totalcount=(lambda string,char: len([c for c in string if c in char]))
print(totalcount(string,char))

# totalcount=(lambda string,char: [c for c in string if c in char])
# print(totalcount(string,char))
