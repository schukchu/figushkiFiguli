schlon = (3 * (16 ** 2018)) - (2 * (8 ** 1028)) - (3 * (4 ** 1100)) - (2 ** 1050) - 2022
low = 0
while schlon != 0:
    low = low + (  schlon % 4 == 3)
    schlon = schlon // 4
print(low)
