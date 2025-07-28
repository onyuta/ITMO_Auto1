# #определить функцию
# def add(x, y):
#     return x + y
#
# #вызвать функцию
# add(1, 2)
# #или
# print(add(1,2))
# print(add('i am ', 'tester'))
# #ab - обязательные аргументы, c,d - необязательные
# def arg(a, b, c=2, d=3):
#     return a + b + c + d
# print(arg(1, 1,1, 1))
# print(arg(2,2))
# print(arg(1,1,1))
# # print(arg(2,2,'1',1)) Ошибка типа данных - не склад. строка и число
#

# def range_arg(a, b, c, d):
#     return a + " " + b + " " + c + " " + d
#
# print(range_arg('1', '2', '3', '4'))
# print(range_arg('1', '2', d='3', c='4'))#обращение к названию аргумента


# def task_func(a = (1, 2, 3, 4)):
#     return a[1]
# print(task_func())

def compute_surface(radius, p=3.14159):
    return p*(radius**2)
print(compute_surface(2))