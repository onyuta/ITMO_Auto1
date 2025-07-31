class Mammal:
    className = 'Млекопитающее'


class Dog(Mammal): #Dog наследуется от класса Mammal
    species = 'Canis Lupus'

dog = Dog()
print(dog.className) #Млекопитающее
