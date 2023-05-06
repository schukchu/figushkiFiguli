1. Перебор списка (в том числе многомерного)
s = [bi,li,ti,li]
for i in s:
  print(i)
2. Генерация всех комбинаций
a = product('wefui', repeat=3)
3. Анализ пар в списке
s=[1,2,3,4,5]
for item in range (0, len(s)-1):
  if s[item] == s[item+1]
4. Сортировка перестановками
I
if s[item] == s[item+1]
II
a,b=b,a
5. Метод итераций или измерение на равноудаленных промежутках
with open('levoe.txt', 'r') as f:
    a = [int(x) for x in f]    
    cst = 0
    cst2 = 0
    
    if len(a) % 2 == 0:
        s =  int(len(a) / 2)
        for t in range(20):
            for i in range(s):
                cost += a[i+t]*i                
            for i in range(a, 2*a):
                cost += a[i+t]*s
                s -= 1
            if t == 0:
                cost2 = cost
            if t != 0 and (cost < cost2):
                cost2 = cost           
            cost = 0
6. Рекурсия
def fac(n):
    if n == 1:
        return n
    else:
        return n*fac(n-1)
7. Метод половинного деления
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
8. Поиск максимума или убить дракона
s = max(ke,s)
9. Если верен каждый или если где-то плохо, то все плохо
if all(jol%c!=0 for c in range(1,jol-1)
10 Преоьраования типов (строка>число и оратно)
b ="23424234234"
int(b)
a =834576
str(a)
