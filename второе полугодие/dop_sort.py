a = ["4","6","9"]
print(a[0])
print(list(c for c in a))
print(list((a[i] for i in range(len(a)))))
print(*a,sep='\n')
for i in a:
    print(i)
for i in range(len(a)):
    print(i)
