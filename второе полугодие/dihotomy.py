a = [5, 24, 34, 36, 39, 40, 50]
a.reverse()
while True:
    print(a[0])
    if a[len(a)//2] < a[(len(a)//2)-1]:
        print("hello")
        a = a[(len(a)//2):]
    else:
        a = a[:(len(a)//2)]
    if len(a)==1:
        break;
print(a)
