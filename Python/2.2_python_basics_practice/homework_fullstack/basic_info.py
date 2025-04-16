# ** Задание: **
# Напишите программу, которая:
# 1. Запрашивает имя пользователя и профессию.
# 2. Спрашивает, сколько лет пользователь работает в QA.
# 3. Проверяет, знает ли пользователь, что такое переменная(вопрос: "Что такое переменная?").
# 4. Выводит разные ответы в зависимости от правильности ответа.
#
# ** Пояснения: **
# - Используйте `input()` для ввода данных.
# - Используйте условные операторы(` if `, ` else `) для проверки.
# - Например:
# ```python
# name = input("Введите ваше имя: ")
# print(f"Привет, {name}! Добро пожаловать в мир Python для тестировщиков."")
# ```
# ** Результат: **
# Программа `basic_info.py`, которая:
# - Спрашивает пользователя данные.
# - Проверяет правильность ответа.
# - Выводит соответствующие сообщения.
name = input("What is your name?: ")
profession = input("What is your profession?: ")
print(f"Hi, {name}! Welcome to Python world for {profession}.")
how_long = input(f"How many years you work in {profession}?")
question_1 = input("What is variable?")
correct_answer = "A variable is like a box with a name that stores a value in programming."
if 'value' in question_1 and len(question_1) > 5:
    print(f"Well done {name}!")
else:
    print(f"You need to study more")
