# Write a Python program to test whether a passed letter is a vowel or not.
vowellist = ['a','e','i','o','u','A','E','I','O','U']
string=input("Insert Any letter: ")
Ans=(lambda vowel : "letter is vowel" if vowel in vowellist else "letter is not vowel")
print(Ans(string))