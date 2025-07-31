# Задача 4
#  В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print('Автомобиль заведен')

    def stop_car(self):
        print('Автомобиль заглушен')

    def set_year(self, year):
        self.year = year
        print(f'Год выпуска автомобиля: {self.year}')

    def set_type(self, type):
        self.type = type
        print(f'Тип автомобиля: {self.type}')

    def set_color(self, color):
        self.color = color
        print(f'Цвет автомобиля: {self.color}')

random_car = Car(color='', type='', year='')
random_car.start_car()
random_car.stop_car()
random_car.set_year(2025)
random_car.set_type('cabriolet')
random_car.set_color('pink')

