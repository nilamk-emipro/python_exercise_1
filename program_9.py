# Write a Program which takes a statement as input from the user and counts occurrences of each vowel in it.

vowel = ['a','e','i','o','u','A','E','I','O','U']
Sentence = input("Enter a statement: ")
totalvowel=(lambda Sentence,vowel: len([char for char in Sentence if char in vowel]))
print(totalvowel(Sentence,vowel))


