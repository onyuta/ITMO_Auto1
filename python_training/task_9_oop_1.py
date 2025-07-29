# from re import search
#
# # 1. Создать класс input принимающий 1 аргумент при инициализации loc
# # 2. Создать объект search (экземпляр класса input)
# 3. Вывести в консоль значение аргумента loc, объекта search
from re import search


# class Input:
#
#     def __init__(self, loc):
#         self.loc = loc
# search = Input('input#search')
#
# print(search.loc)
#Задача со звёздочкой

class Input:

    def __init__(self, text, loc):
        self.text = text #Текст, например подпись к полю ввода
        self.loc = loc #Локатор (css-селетрор..)


class Button:

    def __init__(self, text, loc):
        self.text = text #Текст кнопки
        self.loc = loc #Локатор кнопки

class Title:
    def __init__(self, text, loc):
        self.text = text #Текст заголовка
        self.loc = loc #Локатор заголовка

class Link:
    def __init__(self, text, loc):
        self.text = text #Текст ссылки
        self.loc = loc #Локатор ссылки

 #Создание объектов
input_obj = Input("Поле ввода", "input#input_obj")
button_obj = Button("Отправить", "button.submit")
title_obj = Title("Заголовок", "р1.main-tittle")
link_obj = Link("Перейти на..", "a.link")

#Выод атрибутов текст и лок
print(input_obj.text, input_obj.loc)
print(button_obj.text, button_obj.loc)
print(title_obj.text, title_obj.loc)
print(link_obj.text, link_obj.loc)

