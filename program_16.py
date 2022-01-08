# Write a Python program to display your details like name, age, address in three different lines.
# a.Expected Output
#     i.Name : Joseph Moscot
#     ii.Age : 39
#     iii.Address : Bohemian Street, Lane 3, Grex County

class Person:
  def __init__(self, name, age,address):
    self.name = name
    self.age = age
    self.address=address

  def printdetails(self):
    print("Name :" , self.name)
    print("Age :" , self.age)
    print("Address :" , self.address)

p1 = Person("Joseph Moscot", "39","Bohemian Street, Lane 3, Grex County")
p1.printdetails()

# name = input("Enter your name:")
# age = input("Enter your age:")
# Address = input("Enter your Address:")
#
# p1 = Person(name,age,Address)
# p1.printdetails()