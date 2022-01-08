# Write a Python program to check if all values are the same in a dictionary.
# a.Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
# b.Check all are 23 in the dictionary.
#     i.True
# c.Check all are 10 in the dictionary.
#     i.False
# d.Check if any one value in the dictionary is 25
# i.False

Dictionary={'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}

def checkvalue(value):
    result=(lambda value:True if value in Dictionary.values() else False)
    print(result(value))

checkvalue(23)
checkvalue(10)
checkvalue(25)