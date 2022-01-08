#d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0} Sort this dictionary ascending and descending.
import operator

d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
print(sorted(d.items(),key=operator.itemgetter(1)))
print(sorted(d.items(),key=operator.itemgetter(1),reverse=True))

a_list = ["a", "b", "c"]
getter = operator.itemgetter(1, 2)
b_and_c = getter(a_list)

print(b_and_c)