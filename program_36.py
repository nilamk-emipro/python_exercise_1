# Write a Python program to filter the height and width of students, which are stored in a dictionary. Height >= 6ft and Weight>= 70kg:
#     a.Original Dictionary: {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
#     b.Output : {'Cierra Vega': (6.2, 70)}

Dictionary= {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

for (key,value) in Dictionary.items():
    # print(value[0])
    # print(value[1])
    if value[0]>=6 and value[1]>=70:
        print(key,value)

#print(Dictionary)