import PySimpleGUI as sg

sg.theme('LightGreen2')  # Set the theme

s=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
a=[
'''#1
Разделить пункты на две группы количеству входящих в них дорог''',
'''#2 
for x in range(2):
   for y in range(2):
      for z in range(2):
         for w in range(2): - Полный перебор при котором рассматриваем каждое соответствие 
                     if (not(y<=x) or (z<=w) or not(z))==False:''',
'''#3
Фильтруй''',
'''#4
Построй двоичное дерево для 0 и 1 с известными данными, заблокировать все узловые коды выше известных кодов, определить кол-во символов, требующих кода, рассматривай разные наборы символов, начиная с самого малых; если во время рассмотрения не хватает свободных кодов, начинаем расмматривать с большего кода.''',
'''#5
for i in range(1,100):    - Перебор
    chislo=\'\'                  - Создание пустой строки
    num=(bin(i)[2:])          - Перевод числа из цикла в двоичный код
    if num.count('1')%2==0:   - Проверка, кратно ли количество единиц в числе
        chislo='10'+num[2:]+'0'  - Составление строки со срезанными первыми двумя цифрами
        break;                   - Выход из цикла''',
'''#6
from turtle import *      - Активация модуля turtle
forward(90)                   - Поворот на градусную меру
pu()                                - Поднятие пера
for x in range(1,9):      
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)                    - Проставление точек с заданными координатами
done()                        - Окончание работы turtle''',
'''#7
1. Перебираем все комбинации при помощи for rat in product
2. Проверяем строку на условие
3. Вывод счётчика значений''',
'''#8
from itertools import product  - Активация product из модуля itertools
p = product("АБВ", repeat = 4)  - Создание всех возможных комбинаций из символов "АБВ", из 4 символов
for a in p:                                  - Перебор по каждой комбинации''',
'''#9
Полный код для решения задачи
   spisok=[]
   for num in range(2,1000):
     n=0
     for delit in range (2,100):
       if num%delit==0 and x<i: n+=1
  
    if n==0:spisok.append(num)
        
   flag=False
   for i in spisok:
       for y in range (100):
          if y*4+117==i and flag==False:
             print(y, i)
             flag=True''',
'''#10
Перейти в ворд, ГЛАВНАЯ, правый верхний угол - Найти - расширенный поиск''',
'''#11
I = k * i; N = 2^i
I - вес всего сообщения;
k - кол-во символов; 
i - вес одного символа;

1 б = 8 бит
1 кб = 2^10 б''',
'''#12  
cod = str("8"*86)                                                            - Создание строки из заданного повторения некоторой последовательности символов
while cod.count("8888")>=1 or cod.count("1111")>=1:  - Проверка что в строке ещё остались последовательности цифр, которые можно заменить
    if cod.count("1111")>=1:                                            - Проверка что в строке ещё остались "1111", которые можно заменить
        cod = cod.replace("1111", "8", 1)                           - Замена символов в строке
    else:
        cod = cod.replace("8888", "11", 1)                         - Порядок имеет значение''',
'''#13
перестраиваем граф, начиная с точки, из которой выходим, помечаем в точках кол-во способов, которыми в них можно добраться; накопительно; суммируем или умножаем; если из в пункт через другой, то умножаем. ''',
'''#14
while schlon != 0:                         - Ведём операции пока schlon не шлёпнется в 0
    low = low + (schlon % 4 == 3)   - Подсчёт сколько порядков числа schlon в четверичной записи кратны 3
    schlon = schlon // 4                 - Переводим schlon в четверичную степень порядок за порядком''',
'''#15    
surplus = 8 + 3 * 15 + 5 * 15 * 15 + 2 * 15 * 15 * 15 + 2 * 15 * 15 * 15 * 15
addict = x * 15 + x * 15 * 15 * 15  - Разбивка числа по порядкам на сумму произведений
if (addict + surplus) % 14 == 0:    - Проверка кратности числа
   print((addict + surplus)/14)     - Выведение числа, составленного из двух перменных, над суммой которых была совершена операция''',
'''#16
itog1=itog2=1''',
'''#17
s.append(nums[i]+nums[i+1])  - Добавление в массив числа
for i in range(len(nums)-1): - Перебор по элементу массива
        a=abs(nums[i])%10''',
'''#18
1. Копируем исходную таблицу, вставляем её ниже и очищаем от цифр
2. Для первого горизонтального и первого вертикального столбцов применяем формулу сложения с предыдущей клеткой (пишем для одной, потом растягиваем за правый нижний край)
3. Для остальных клеток пишем сумму значения в клетке и макс(клетка_сверху;клетка_слева), снова растягиваем за угол
3,5. Копируем исходную таблицу и вставляем её форматирование (стены)
4. Для клеток снизу и справа от стен меняем формулу на параллельные им, от клеток примукающих к соответствующим стенам
5. Наслаждаемся своей умностью и переписываем число из нижней правой клетки в ответ''',
'''#19-21
    1. Определить точку входа (условие выигрыша)
    2. Расписать на четыре хода назад
    3. Расписать ходы по игрокам (древо)
    ![image](https://user-images.githubusercontent.com/81824679/208224974-77325ccd-b3b7-4c0a-9334-51d312134f3d.png)''',
'''#19-21
    1. Определить точку входа (условие выигрыша)
    2. Расписать на четыре хода назад
    3. Расписать ходы по игрокам (древо)
    ![image](https://user-images.githubusercontent.com/81824679/208224974-77325ccd-b3b7-4c0a-9334-51d312134f3d.png)''',
'''#19-21
    1. Определить точку входа (условие выигрыша)
    2. Расписать на четыре хода назад
    3. Расписать ходы по игрокам (древо)
    ![image](https://user-images.githubusercontent.com/81824679/208224974-77325ccd-b3b7-4c0a-9334-51d312134f3d.png)''',
'''#22
УРАААА, ПОЛОСОЧКИ''',
'''#23
 1. Функцией product содаём объект со всеми комбинациями
 2. Перебираем по комбинации в объекте
 3. Обнуляем стартовое значение
 4. Для отсеивания неподходящих итераций используем continue
 5. Перебираем for x in prog (for prog in product) 
 6. Проверяем по условию (if a == 7: break if a >= 35: break)''',
'''#24    
with open ('24.txt') as f:
    lot = f.readline.replace('C', 'G').replace('F', 'G').replace('A', 'O').replace('E', 'O').replace('GO', '*')  - Через серию замен все интерусующие нас комбинации
    for i in lot:           - Для каждой строки .txt файла                                                         превращаем в 'GO'
      if i =='*':           - Смотрим по '*' в каждой строке''',
'''#25        
for i in range (2023, 10**10, 2023): - перебор с шагом
    num = str(i)                                        - перекладка числа в строку
    if num [0] == '1' and num [2:6] == '2139' and num [-1] == '4': - проверка числа на соответствие маске''',
'''#26
with open('26.txt') as f:
    data=[int(x) for x inf]
    li=sorted(s[1:],reverse=True)
    k = 1
    mel = li[0]
    for i in range(1,len(li)):
        if li[i]+3 <= mel:
            mel = li[i]
            k+=1
print(k,mel)''',
'''#27
А: Тк мало станций, применяем перебор
      1) загружаем данные в список и избавляемся от первого элемента
      2) создаём переменную с длиной списка
      3) сдваиваем список, используя разрез меняем список для работы, чтобы пункт, который рассматриваем всегда стоял первым в списке
      4) когда создаём новый список со срезом, обнуляем стоимость
      5) считаем стоимость доставки для первого элемента
      6) создаём переменную для пересчёта индекса элементов после середины списка - от длины списка отнимаем индекс элемента; 
      7) считаем стоимость накоплением; найденную стоимость для каждого километра добавляем в пустой список
      8) выводим индекс минимального элемента списка со стоимостью + 1
Б: Тк много станций, используем метод итераций (приближение - с кажды м шагом приближаемся к точному определённому решению)
      1) Вся программа находится в бесконечном цикле, выход из которой - точное решение - два раза повторяющийся ответ при шаге бесконечного цикла 1
      2) Большой список перебора организован с учётом трёх переменных: start, finish и step
      3) Шаг настраивается таким образом, чтобы было 20 равнораспределённых замеров по всей дороге
      4) Среди 20 значений находим минимальную стоимость и километр, которому она принадлежит 
      5) После каждого прохода цикла start, finish и step пересчитываются
      Значения start и finish - рамки диапазона поиска; Новые значения границ диапазона - километр + или - step
      7) После перерасчёта start и finish перерассчитываем step;
      Делим нацело step на 10; Если шаг становится 0, то превращаем его в 1''',
'''pass;     - Заглушка, применяется когда нужно заткнуть недоделанные ветвления
break;    - Выход из цикла
continue; - Переход на следующие итерацию цикла
list()    - Функция преобразует аргумент в список'''

]
# Define the layout
layout = [
          [sg.Text('Output Text:', font=('Arial', 12)), sg.Text('', size=(40, 1), key='output')],
          [sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('Ввод', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('Выход', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button')]]

# Create the window
window = sg.Window('ЕГЭ архив', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[int(values['Combo'])-1]
        #print(choice)
        window['outputt'].update('')
        window['outputt'].update(choice)
    if event == 'button':
        break

# Close the window
window.close()
