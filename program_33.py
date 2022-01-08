# Write a Python program to match key values in two dictionaries.
# a.Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# b.Expected output: key1: 1 is present in both x and y

Sampledictionary1= {'key1': 1, 'key2': 3, 'key3': 2}
Sampledictionary2={'key1': 1, 'key2': 2}

for (key, value) in set(Sampledictionary1.items()) & set(Sampledictionary2.items()):
    print("{}:{} is present in both dictionary".format(key,value))
