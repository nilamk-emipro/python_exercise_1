#Define a global dictionary. Define a function which takes 2 values 1st as key and 2nd as value. The function should add those key values to the global dictionary

dic1={}

def Updatedictionary(key,value):
    dic1.update({key: value})

Updatedictionary('a',1)
Updatedictionary('b',2)
print(dic1)