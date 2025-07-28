# #Задание 1
def task_1():
    nomer: int = 120
    temp: float = 36.7
    tekst: str = "С Днем дня!"
    characters: list[str] = ["Edward", "Bella"]
    pravda: bool = True
    print(nomer, 'относится к типу', type(nomer))
    print(temp, 'относится к типу', type(temp))
    print(tekst, 'относится к типу', type(tekst))
    print(characters, 'относится к типу', type(characters))
    print(pravda, 'относится к типу', type(pravda))
    return {
        'nomer': nomer,
        'temp': temp,
        'tekst': tekst,
        'characters': characters,
        'pravda': pravda,
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




