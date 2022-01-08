#Create a function which takes a value. Define a global dictionary. The function should be able to display a statement whether the passed value is in the dictionary or not.

color_list_1 = set(["White", "Black", "Red"])

def checkvalue(value):
    result=(lambda value:True if value in color_list_1 else False)
    print(result(value))

checkvalue("White")