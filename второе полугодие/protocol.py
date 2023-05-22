if all(i % y != 0 for y in range (2, math.isqrt(i))):
  - проверка на prime
import math

til = []
ter = []
for i in range(1050, 15000000):
    tre = str(i)
    if tre[0:2] == '12' and tre[-4:-5:-1] == '4' and tre[-1:-3:-1] == '56':
        print(i)
        if i%161==0:
            til.append(tre)
            ker = str(int(ter) / 161)
            ter = ter.append(ker)
til = til[::-1]
for tilt in til:
    print(tilt)
for tert in ter:
    print(tert)
