# Write a Python program to drop empty(None) Items from a given Dictionary.
#     a.Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
#     b.New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}
dict1={}
Dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None}
#filtervalue=filter((lambda k:k==None),Dictionary)
for (key,value) in Dictionary.items():
    if(value is not None):
        dict1.update({key:value})

print(dict1)
#dict1 = {key:value for (key, value) in Dictionary.items() if value is not None}