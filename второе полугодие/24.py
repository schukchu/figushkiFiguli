k = 0
km = 0
with open ('24.txt') as f:
    lot = f.readline.replace('C', 'S').replace('F', 'S').replace('D', 'S')
    lot = lot.replace('A', 'G').replace('O', 'G')
    lot = lot.replace('SG', '*')
    for i in lot:
      if i = '*':
        k += 1
        km = max(k, km)
      else: 
        k = 0
    print(km)
