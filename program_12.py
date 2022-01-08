# Define a global dictionary with key & values. Iterate through it and print the key and value of it separately in the following format.
# a.WritKey is <key> and Value is <value>

Dic = {1:10, 2:20,3:30, 4:40,5:50, 6:60}
for key,value in Dic.items():
  print("Key is",key,"Value is",value)