# Define a global dictionary. Iterate through it and print the key and value of it separately in the following format.
#     a.Key is <key> and Value is <value>.
#     The loop statement should be enough to extract key and value, so don't use the "get" method or [] to extract the value from the dictionary.

Dic = {1:10, 2:20,3:30, 4:40,5:50, 6:60}
for key,value in Dic.items():
  print("Key is <",key,"> Value is <",value,">")