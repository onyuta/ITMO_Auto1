class Soda:

    def __init__(self, additive = None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f'Газировка и {self.additive}')

        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()

