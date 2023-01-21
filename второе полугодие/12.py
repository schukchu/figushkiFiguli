cod = str("8"*86)
while cod.count("8888")>=1 or cod.count("1111")>=1:
    if cod.count("1111")>=1:
        cod = cod.replace("1111", "8", 1)
    else:
        cod = cod.replace("8888", "11", 1)
print(cod)

from math import*
for n in range (0,200):
    col = 4 * n + 117
    tun = 0
    for x in range (1, 2000):
        if col % x  == 0:
            tun += 1
    if tun == 2:
        print(n)
