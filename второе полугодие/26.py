with open('26.txt') as f:
    data=[int(x) for x inf]
    li=sorted(s[1:],reverse=True)
    k = 1
    mel = li[0]
    for i in range(1,len(li)):
        if li[i]+3 <= mel:
            mel = li[i]
            k+=1
print(k,mel)
