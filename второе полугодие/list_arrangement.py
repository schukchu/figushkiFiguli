unt = [5, 2, 6, 4, 4, 3]
fef = 0
for i in range (len(unt)-1):
    for i in range (len(unt)-1):
        if unt[i+1] < unt[i]:
            print("Start " + str(unt[i]) + str(unt[i+1]))
            fef = unt[i]
            unt[i] = unt[i+1]
            unt[i+1] = fef
            print("Done " + str(unt[i]) + str(unt[i+1]))
print(unt)
