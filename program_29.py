# Define a global empty dictionary. Iterate from 1 till 10 and fill the dictionary with the key as the number and value as the square of that number.

dic1={}
def Updatedictionary():
    for n in range(1,11):
        dic1.update({n: n**2})

Updatedictionary()
print(dic1)