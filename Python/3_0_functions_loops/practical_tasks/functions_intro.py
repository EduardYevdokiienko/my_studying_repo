# Напишите программу, которая:
# Реализует функцию greet_user(name), принимающую имя пользователя и выводящую приветствие:
# "Привет, [имя]! Добро пожаловать в мир Python!".
# Реализует функцию calculate_sum(a, b), которая принимает два числа и возвращает их сумму.
# Использует обе функции для взаимодействия с пользователем.

# Пример работы программы:
# Введите ваше имя: Анна
# Привет, Анна! Добро пожаловать в мир Python!
# Введите первое число: 5
# Введите второе число: 7
# Сумма чисел: 12
def greet_user(name):
    if name:
        print(f"Hello, {name}! welcome to Python world!")
    else:
        print("Please type your name!")


def calculate_sum(a, b):
    if a and b:
        c = a + b
        print(f"Sum of your numbers: {c}")
    else:
        int(a, b)
        c = a + b
        print(f"Sum of your numbers: {c}")

name = input("Type your name: ")
greet_user(name)
a = int(input("please type your first number: "))
b = int(input("please type your second number: "))
calculate_sum(a, b)
