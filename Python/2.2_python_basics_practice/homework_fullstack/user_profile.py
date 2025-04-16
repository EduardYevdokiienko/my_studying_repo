# **Задание:**
# 1. Создайте переменные для хранения информации:
#     - Имя пользователя.
#     - Профессия.
#     - Любимый инструмент для тестирования.
# 2. Позвольте пользователю изменить данные через ввод.
# 3. Добавьте проверку: если пользователь не ввел данные, программа выводит сообщение об ошибке.
user_name = input("What is your name? ")
if not user_name:
    print("Please try again")
else:
    print(f"Hi {user_name}!")
profession = input(f"What is your profession {user_name}? ")
if not profession:
    print("Please try again")
else:
    print(f"Well done {user_name}, {profession} is very good profession!")
tool = input(f"What is your favorite tool in {profession} profession? ")
if not tool:
    print("Please try again!")
else:
    print(f"{tool} is a very good choice!")
