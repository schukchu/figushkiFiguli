def resulter():
 command = input("Please input the type of problem with a number: \n 1 - Text problem \n 2 - Picture problem \n 3 - Sound problem \n")
 match command:
     case 1 or 2:
      N = int(input())
      I = int(input())
      i = int(input())
      k1 = int(input())
      k2 = int(input())
      k3 = int(input())
      if k2 == int(""):
          k = k1
      elif k3 == int(""):
          k = k1 * k2
      else:
          k = k1 * k2 * k3
      case i == int(""):
         while N > 0:
             N = N // 2
             i = i + 1
         print (i)
      case k == int(""):
         k = I / i
         print (k)
      case N == int(""):
         N = pow(2,i)
         print(N)
      case I == int(""):
         I = K * i
         print(I)
     case 3:
         N = int(input("коло-во уровней дискретизации"))
         i = int(input("глубюина звука"))
         D = int(input("частота дискретизации"))
         T = int(input("Длительность файла"))
         V = int(input("объём звукогого файла"))
         k = int(input("кол-во каналов(моно = 1, стерео = 2)"))
         if N != int("") and i == int(""):
             while N > 0:
                 N = N // 2
                 i = i + 1
             print(i)
         else:
             i = V / D / k / T
             print(i)
         if N == int(""):
             N = pow(2,i)
             print(N)
         if D == int(""):
             D = V / k / i / T
             print(D)
         if T == int(""):
             T = V / k / i / D
             print(T)
         if k == int(""):
             k = V / D / i / T
             print(k)
         if V == int(""):
             V = D * k * i * T
             print(V)
         print('See you later alligator')
     case other:
      print("Try another")
