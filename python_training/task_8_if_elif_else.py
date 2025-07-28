#Программа проверяет является ли число положительным
# или отрицательным и выводит соответствующее сообщение
num = 0

#Попробовть значения num = -5 и 0


if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

# str_2 содержит в себе str1?
def task8(str_1, str_2):
   if str_1 in str_2:
       print('Да')
   else:
       print('Нет')
task8(str_1='test', str_2='test1')


num_float = -4.5
#Попробовать значения 0 и -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Вы бакалавр')
    elif year_of_study in range(5,7): #Последнее число диапазона не включается
        print('Вы магистр')
    elif 7 <= year_of_study <= 9:
        print('Вы аспирант')
    else:
        print('Введите корректный год обучения')
student_rank(9)


def nomer(number):
    if -100 < number < 100:
        print('-')
    else:
        print('+')
nomer(-1)
#или проще
a = 5
if a > 100 or a < -100:
    print('-')
else:
    print('+')

