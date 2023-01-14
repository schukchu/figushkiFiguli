from itertools import product
c = 0
p = product("АБВ", repeat = 4)
for a in p:
    c += 1
l = product("АБВ", repeat=5)
for x in l:
    c = c +1
print(c)
