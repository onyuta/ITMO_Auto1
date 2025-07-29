# class Button: #class - ключевое слово создания класса, Button - имя класса
#
#     type: str = 'Кнопка'
#
#     #Тело класса
#     def __init__(self, text, link): #конструктор класса
#         # атрибуты text, link, self - аргумент, имя для ссылки на объект,указатель взять конкретный атрибут
#         self.text = text #аргументы
#         self.link = link
# #Создаем экземпляры класса
# home = Button ('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# #Получаем доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print('\n')

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

#Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

#Вызываем метод
print(home_two.click())

