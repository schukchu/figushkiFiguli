from itertools import*
for x in range (2,6):
   b = product('12', repeat=x)
   for i in b:
       a = 12
       prog = ''.join(i)
       for n in prog:
           if n == '1': a -= 1
           elif n == '2': a = a * 7
       if a == 489:
           print(prog)
