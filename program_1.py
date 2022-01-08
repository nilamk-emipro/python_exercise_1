#Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a
#list and a tuple with those numbers.
#a.Sample data : 3, 5, 7, 23
#b.Output :
#c.List : ['3', ' 5', ' 7', ' 23']
#d.Tuple : ('3', ' 5', ' 7', ' 23')


values = input("Input some value with comma seprated : ")
print('Data :' ,values)
list = values.split(",")
print('List : ',list)
tuple = tuple(list)
print('Tuple : ',tuple)