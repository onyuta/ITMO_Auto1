#Задача 1 Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел
from itertools import count


def task_1(x,y):
    if x > y:
        print(x)
    else:
        print(y)
task_1(30,40)


#Задача 2 Функция на вход получает два произвольных числа. Вывести в консоль 'yes', если они
#отличаются друг от друга на 135, иначе вывести 'No'
def task_2(a,b):
    if a - b == 135 or a - b == -135:
        print('Yes')
    else:
        print('No')
task_2(135,0)


#Задача 3 Функция на вход получает произвольное число от 1 до 12 (номер месяца)
#Вывести название сезона года в консоль (зима, весна, лето, осень)
def task_3(month):
    if month == 12 or month == 1 or month == 2:
        print('Зима')
    elif month in (3, 4, 5):
        print('Весна')
    elif 6 <= month <= 8:
        print('Лето')
    elif month in (9, 10, 11):
        print('Осень')
    else:
        print('Такого месяца не существует. Число должно быть < 12')
task_3(15)


#Задача 4 Функция на вход получает три произвольных числа
#Если все числа больше 10, то вывести на экран 'Yes', иначе 'No'
def task_4(c, m, d):
    if c > 10 and m > 10 and d > 10:
        print('Yes')
    else:
        print('No')
task_4(30, 70, 90)


#Задание 5 Функция на вход получает список, состоящий из 5 произвольных чисел. Найти кол-во
#положительных чисел среди них
numbers = [9, -3, -8, -9, -2]
def task_5(numbers):
    count = 0
    for z in numbers:
        if z > 0:
            count += 1
    return count
print(task_5(numbers))


#Задание 6 Функция на вход получает 2 переменные: кол-во лет (int) и кол-во месяцев (int)
#Вывести количество дней за это время. 29 дней
def task_6(yrs: int, mnth: int) -> int:
   if yrs < 0 or mnth < 0:
       print('Отрицательное число не допускается')
   elif not isinstance(yrs, int) or not isinstance(mnth, int):
       print('Введите целое число')
   else:
       print((yrs * 12 + mnth) *29)
task_6(9, 8)


