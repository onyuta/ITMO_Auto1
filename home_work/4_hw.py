# Задача 1
# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_rectangle(self):
        return self.width * self.height

    def perimeter_of_rectangle(self):
        return 2 * (self.width + self.height)

rectangle_1 = Rectangle(5,10)
rectangle_2 = Rectangle(9, 11)
rectangle_3 = Rectangle(1.1, 0.5)

print(f'Площадь первого прямоугольника равна {rectangle_1.area_of_rectangle()} ')
print(f'Периметр первого прямоугольника равен {rectangle_1.perimeter_of_rectangle()} ')
print(f'Площадь второго прямоугольника равна {rectangle_2.area_of_rectangle()} ')
print(f'Периметр второго прямоугольника равен {rectangle_2.perimeter_of_rectangle()} ')
print(f'Площадь третьего прямоугольника равна {rectangle_3.area_of_rectangle()} ')
print(f'Периметр третьего прямоугольника равен {rectangle_3.perimeter_of_rectangle()} ')


# Задача 2
# Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b
# с ними нужно производить соответствующие действия и печатать ответ.


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def substruction(self):
        return self.a - self.b

numbers = Math(10, 2)

print(f'Результат сложения равен {numbers.addition()}')
print(f'Результат умножения равен {numbers.multiplication()}')
print(f'Результат деления равен {numbers.division()}')
print(f'Результат вычитания равен {numbers.substruction()}')


# Задача 3
# откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки


class Sidebar_buttons:
    def __init__(self, button_text):
        self.button_text = button_text
        self.type = 'Кнопка'
        self.locator = ''

    def click(self):
        return self.button_text

text_box = Sidebar_buttons('Text Box')
check_box = Sidebar_buttons('Check Box')
radio_button = Sidebar_buttons('Radio Button')
web_tables = Sidebar_buttons('Web tables')
buttons = Sidebar_buttons('Buttons')
links = Sidebar_buttons('Links')
broken_links_images = Sidebar_buttons('Broken Links - Images')
upload_and_download = Sidebar_buttons('Upload and download')
dynamic_properties = Sidebar_buttons('Dynamic properties')

print(f'Текст кнопки: {text_box.button_text}, Клик по кнопке {text_box.click()}')
print(f'Текст кнопки: {check_box.button_text}, Клик по кнопке {check_box.click()}')
print(f'Текст кнопки: {radio_button.button_text}, Клик по кнопке {radio_button.click()}')
print(f'Текст кнопки: {web_tables.button_text}, Клик по кнопке {web_tables.click()}')
print(f'Текст кнопки: {buttons.button_text}, Клик по кнопке {buttons.click()}')
print(f'Текст кнопки: {links.button_text}, Клик по кнопке {links.click()}')
print(f'Текст кнопки: {broken_links_images.button_text}, Клик по кнопке {broken_links_images.click()}')
print(f'Текст кнопки: {upload_and_download.button_text}, Клик по кнопке {upload_and_download.click()}')
print(f'Текст кнопки: {dynamic_properties.button_text}, Клик по кнопке {dynamic_properties.click()}')
