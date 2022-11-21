import math

def reshulya():
    command = int(input(" If you не говорите по-английски, введите текст в кавычках (да, я дуралей)"
                        " \n Please input the type of problem with a number: \n"
                        " 1 - Text problem \n"
                        " 2 - Picture problem \n"
                        " 3 - Sound problem \n If a variable is unknown, enter 0 \n"
                        " All inputs are considered to be in bits \n"))
    if command == 1 or command == 2:
        N = int(input("Power of the alphabet(number of colours): "))
        I = int(input("Informational weight of the message: "))
        i = int(input("Informational weight of a single character/pixel: "))
        k1 = int(input("If this is the only number of characters, press enter for k2 and k3\n"
                       "The first number of characters (number of characters in a line): "))
        k2 = int(input("The second number of charcters(number of lines): "))
        k3 = int(input("The third number of characters(number of pages): "))
        if k2 == 0:
            k = k1
        elif k3 == 0:
            k = k1 * k2
        else:
            k = k1 * k2 * k3
        if i == 0:
            if N > 1:
                i = math.ceil(math.log(N,2))
            print ("i = " + str(i))
        if k == 0:
            try:
                k = I / i
            except ZeroDivisionError:
                k = 1
            if k > 0:
                print ("k =" + str(k))
        if N == 0:
            N = pow(2,i)
            print("N = " + str(N))
        if I == 0:
            try:
                I = k * i
            except ZeroDivisionError:
                I = 1
            if I > 0:
                print("I = " + str(I))
    if command == 0:
        print("Так нельзя, дурашка")
    if command == 3:
        N = int(input("коло-во уровней дискретизации"))
        i = int(input("глубюина звука"))
        D = int(input("частота дискретизации"))
        T = int(input("Длительность файла"))
        V = int(input("объём звукогого файла"))
        k = int(input("кол-во каналов(моно = 1, стерео = 2)"))
        if k != 2:
            k = 1
        if N != int("") and i == int(""):
            i = math.ceil(math.log(N, 2))
            print("i = " + str(i))
        else:
            try:
                i = V / D / k / T
            except ZeroDivisionError:
                i = 1
            print("i = " + str(i))
        if N == 0:
            N = pow(2, i)
            print("N = " + str(N))
        if D == 0:
            try:
                D = V / k / i / T
            except ZeroDivisionError:
                D = 1
            print("D = " + str(D))
        if T == 0:
            try:
                T = V / k / i / D
            except ZeroDivisionError:
                T = 1
            print("T = " + str(T))
        if k == 0:
            try:
                k = V / D / i / T
            except ZeroDivisionError:
                k = 1
            print("k = " + str(k))
        if V == 0:
            try:
                V = D * k * i * T
            except ZeroDivisionError:
                V = 1
            print("V = " + str(V))
            print('See you later alligator')
