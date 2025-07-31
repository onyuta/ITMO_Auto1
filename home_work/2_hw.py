# #Задание 1
def task_1():
    quantity: int = 120
    temperature: float = 36.7
    congratulations: str = "С Днем дня!"
    characters: list[str] = ["Edward", "Bella"]
    truth: bool = True
    print(quantity, 'относится к типу', type(quantity))
    print(temperature, 'относится к типу', type(temperature))
    print(congratulations, 'относится к типу', type(congratulations))
    print(characters, 'относится к типу', type(characters))
    print(truth, 'относится к типу', type(truth))
    return {
        'quantity': quantity,
        'temperature': temperature,
        'congratulations': congratulations,
        'characters': characters,
        'truth': truth,
        }
result = task_1()
print('Результат функции:', result)



#Задание 2
def task_2() -> list[int]:
    z: list[int] = [1, 2, 3, 5, 8, 13, 21] #Fibonacci sequence
    print('z[0:3 =]', z[0:3])
    return z
result = task_2()
print('Весь список:', result)

#Задание 3
def task_3(number_1: int) -> int:
    return number_1**2
result = task_3(9)
print('Квадрат числа', result)


def task_3(number_2: float) -> float:
    return number_2**2
result = task_3(8.001)
print('Квадрат числа', result)




