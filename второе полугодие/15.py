surplus = 8 + 3 * 15 + 5 * 15 * 15 + 2 * 15 * 15 * 15 + 2 * 15 * 15 * 15 * 15
addict = 0
for x in range (0, 14):
    addict = x * 15 + x * 15 * 15 * 15
    if (addict + surplus) % 14 == 0:
        print((addict + surplus)/14)
