# students = {'Aex':{'class':'V', 'roll_id':2}, 'Puja':{'class':'V',’roll_id':3}}
# a.Using the above dictionary, print the following output.
#     i.Aex
#     ii.class : V
#     iii.roll_id : 2
#     iv.Puja
#     v.class : V
#     vi.roll_id : 3
students = {'Aex':{'class':'V', 'roll_id':2},
            'Puja':{'class':'V','roll_id':3}}

for key,value in students.items():
    print(key)
    for key1,value1 in value.items():
        print(key1,":",value1)



