# Define a global dictionary. Iterate through that dictionary and print the output in the following format.
# a.Sample Output
#     i.a -- 2
#     ii.x -- 8
#     iii.z -- 1

dic1 = {'a': 2,'x': 8,'z':1}

def func():
   for key, value in dic1.items():
      print(key, ' -- ', value)

func()