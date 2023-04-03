a = [5, 24, 34, 36, 39, 40, 50]
yn = 0
on = 0
for u in range(len(a)):
    print(a[u])
    if a[u] % 2 == 0:
        on += 1
    else:
        yn += 1
print(yn//2 + on//2)
